#!/usr/bin/env bash
set -euo pipefail

LAB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SUBSCRIPTION_ID="${AZURE_SUBSCRIPTION_ID:-}"
RUN_ID=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --subscription-id) SUBSCRIPTION_ID="$2"; shift 2 ;;
    --run-id) RUN_ID="$2"; shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
[[ -n "$SUBSCRIPTION_ID" && -n "$RUN_ID" ]] || { echo "Supply --subscription-id and --run-id." >&2; exit 2; }

STATE_DIR="$LAB_ROOT/.state/$RUN_ID"
MANIFEST="$STATE_DIR/run.json"
REPORT="$STATE_DIR/validation.json"
[[ -f "$MANIFEST" ]] || { echo "Missing state: $MANIFEST" >&2; exit 5; }
ACTIVE_SUB="$(az account show --query id --output tsv)"
[[ "$ACTIVE_SUB" == "$SUBSCRIPTION_ID" ]] || { echo "Active subscription does not match the requested subscription." >&2; exit 4; }
RECORDED_SUB="$(jq -r '.subscriptionId' "$MANIFEST")"
[[ "$RECORDED_SUB" == "$SUBSCRIPTION_ID" ]] || { echo "Recorded subscription mismatch." >&2; exit 4; }
RG="$(jq -r '.resourceGroup.name' "$MANIFEST")"
RG_ID="$(jq -r '.resourceGroup.id' "$MANIFEST")"

checks='[]'
add_check() {
  checks="$(jq -c --arg id "$1" --arg status "$2" --arg message "$3" '. + [{id:$id,status:$status,message:$message}]' <<<"$checks")"
}

actual_rg_id="$(az group show --subscription "$SUBSCRIPTION_ID" --name "$RG" --query id --output tsv 2>/dev/null || true)"
if [[ -z "$actual_rg_id" ]]; then
  add_check context.resource-group fail "The recorded resource group is absent."
elif [[ "${actual_rg_id,,}" != "${RG_ID,,}" ]]; then
  add_check context.resource-group fail "The resource-group ID does not match the run manifest."
else
  add_check context.resource-group pass "The exact recorded resource group exists."
fi

purpose="$(az group show --name "$RG" --query tags.purpose --output tsv 2>/dev/null || true)"
lab_id="$(az group show --name "$RG" --query tags.labId --output tsv 2>/dev/null || true)"
run_id="$(az group show --name "$RG" --query tags.runId --output tsv 2>/dev/null || true)"
if [[ "$purpose" == "az104-lab" && "$lab_id" == "10" && "$run_id" == "$RUN_ID" ]]; then
  add_check ownership.tags pass "purpose, labId, and runId tags match the manifest."
else
  add_check ownership.tags fail "Ownership tags do not match; cleanup must not proceed."
fi

resources="$(az resource list --subscription "$SUBSCRIPTION_ID" --resource-group "$RG" --output json 2>/dev/null || echo '[]')"
EXPECTED_TYPES=(
  "Microsoft.Resources/deployments"
  "Microsoft.Storage/storageAccounts"
)
if [[ "${#EXPECTED_TYPES[@]}" -eq 0 ]]; then
  add_check resources.baseline warning "This lab validates external or tenant-scoped state separately."
else
  for expected in "${EXPECTED_TYPES[@]}"; do
    count="$(jq --arg expected "${expected,,}" '[.[] | select((.type | ascii_downcase) == $expected)] | length' <<<"$resources")"
    if [[ "$count" -gt 0 ]]; then
      add_check "resource.$(tr '/.' '--' <<<"$expected")" pass "Found $count resource(s) of type $expected."
    else
      add_check "resource.$(tr '/.' '--' <<<"$expected")" warning "No top-level resource of type $expected was returned; inspect nested or gated checkpoint state."
    fi
  done
fi

failures="$(jq '[.[] | select(.status == "fail")] | length' <<<"$checks")"
warnings="$(jq '[.[] | select(.status == "warning" or .status == "skipped")] | length' <<<"$checks")"
result=pass
[[ "$warnings" -eq 0 ]] || result=partial
[[ "$failures" -eq 0 ]] || result=fail
jq -n --arg labId "LAB-10" --arg runId "$RUN_ID" --arg generatedAt "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --arg result "$result" --argjson checks "$checks"   '{labId:$labId,runId:$runId,generatedAt:$generatedAt,result:$result,checks:$checks}' >"$REPORT"
cat "$REPORT"
[[ "$result" != fail ]]
