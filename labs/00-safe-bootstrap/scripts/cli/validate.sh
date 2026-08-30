#!/usr/bin/env bash

set -euo pipefail
umask 077

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
LAB_ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd -P)"

usage() {
  cat <<'EOF'
Read-only Azure validation for an initialized Lab 00 run.

Usage:
  ./validate.sh --run-id ID [--state-root PATH]

The only write is the local .state/<run-id>/validation.json report.
EOF
}

run_id=""
state_root="$LAB_ROOT/.state"
while (( $# > 0 )); do
  case "$1" in
    --run-id) [[ $# -ge 2 ]] || exit 1; run_id="$2"; shift 2 ;;
    --state-root) [[ $# -ge 2 ]] || exit 1; state_root="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: unknown argument '$1'." >&2; usage >&2; exit 1 ;;
  esac
done

run_pattern='^[a-z0-9][a-z0-9-]{2,31}$'
[[ "$run_id" =~ $run_pattern ]] || { echo "ERROR: --run-id is required and must match $run_pattern." >&2; exit 1; }
command -v az >/dev/null 2>&1 || { echo "ERROR: Azure CLI is required." >&2; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "ERROR: jq 1.6 or later is required." >&2; exit 1; }

state_root="$(cd -- "$state_root" 2>/dev/null && pwd -P)" || { echo "ERROR: state root does not exist." >&2; exit 1; }
run_dir="$state_root/$run_id"
manifest="$run_dir/run.json"
report="$run_dir/validation.json"
[[ -f "$manifest" && ! -L "$run_dir" ]] || { echo "ERROR: valid run state was not found at '$run_dir'." >&2; exit 1; }
jq empty "$manifest" 2>/dev/null || { echo "ERROR: run.json is not valid JSON." >&2; exit 1; }

checks='[]'
add_check() {
  local id="$1" status="$2" message="$3"
  checks="$(jq -c --arg id "$id" --arg status "$status" --arg message "$message" '. + [{id:$id,status:$status,message:$message}]' <<<"$checks")"
  printf '[%s] %s\n' "$(tr '[:lower:]' '[:upper:]' <<<"$status")" "$message"
}

echo "Lab 00 - Azure CLI validation (Azure reads only)"
echo "================================================"

state_lab_id="$(jq -r '.labId // empty' "$manifest")"
state_run_id="$(jq -r '.runId // empty' "$manifest")"
expected_subscription_id="$(jq -r '.context.subscriptionId // empty' "$manifest")"
expected_tenant_id="$(jq -r '.context.tenantId // empty' "$manifest")"
primary_region="$(jq -r '.regions.primary // empty' "$manifest")"
secondary_region="$(jq -r '.regions.secondary // empty' "$manifest")"

if [[ "$state_lab_id" == "00-safe-bootstrap" && "$state_run_id" == "$run_id" ]]; then
  add_check "state.identity" "pass" "Run manifest belongs to Lab 00 and run '$run_id'."
else
  add_check "state.identity" "fail" "Run manifest identity does not match the selected Lab 00 run."
fi

required_tag_count="$(jq '[.tags.purpose,.tags.labId,.tags.runId,.tags.expiresOn] | map(select(type == "string" and length > 0)) | length' "$manifest")"
if [[ "$required_tag_count" == "4" && "$(jq -r '.tags.runId' "$manifest")" == "$run_id" ]]; then
  add_check "state.tags" "pass" "Required purpose, labId, runId, and expiresOn tags are prepared."
else
  add_check "state.tags" "fail" "Required tag metadata is missing or inconsistent."
fi

resource_count="$(jq '.resources | if type == "array" then length else -1 end' "$manifest")"
tenant_change_count="$(jq '.tenantScopedChanges | if type == "array" then length else -1 end' "$manifest")"
live_mutations="$(jq -r '.liveAzureMutations // empty' "$manifest")"
if [[ "$resource_count" == "0" && "$tenant_change_count" == "0" && "$live_mutations" == "false" ]]; then
  add_check "state.safety-boundary" "pass" "State records no Azure resources, tenant changes, or live mutations."
else
  add_check "state.safety-boundary" "fail" "Unexpected Azure resources or shared-setting changes are recorded; stop and review."
fi

account_json="$(az account show --only-show-errors --output json 2>/dev/null || true)"
if [[ -z "$account_json" ]]; then
  add_check "azure.session" "fail" "No active Azure CLI session is available."
  current_subscription_id=""
  current_tenant_id=""
else
  current_subscription_id="$(jq -r '.id // empty' <<<"$account_json")"
  current_tenant_id="$(jq -r '.tenantId // empty' <<<"$account_json")"
  current_state="$(jq -r '.state // empty' <<<"$account_json")"
  if [[ "$current_state" == "Enabled" ]]; then
    add_check "azure.session" "pass" "Azure CLI session is active and the subscription state is Enabled."
  else
    add_check "azure.session" "fail" "Active subscription state is '$current_state', not Enabled."
  fi
fi

if [[ -n "${current_subscription_id:-}" && "$current_subscription_id" == "$expected_subscription_id" ]]; then
  add_check "azure.subscription-context" "pass" "Active subscription matches the run manifest."
else
  add_check "azure.subscription-context" "fail" "Active subscription does not match the run manifest."
fi
if [[ -n "${current_tenant_id:-}" && "$current_tenant_id" == "$expected_tenant_id" ]]; then
  add_check "azure.tenant-context" "pass" "Active tenant matches the run manifest."
else
  add_check "azure.tenant-context" "fail" "Active tenant does not match the run manifest."
fi

if [[ -n "$expected_subscription_id" && -n "$primary_region" ]]; then
  location_count="$(az account list-locations --subscription "$expected_subscription_id" --query "length([?name=='$primary_region'])" --output tsv --only-show-errors 2>/dev/null || true)"
  if [[ "$location_count" == "1" ]]; then
    add_check "azure.primary-region" "pass" "Primary region '$primary_region' is available to the subscription."
  else
    add_check "azure.primary-region" "fail" "Primary region '$primary_region' is not available or could not be queried."
  fi
else
  add_check "azure.primary-region" "fail" "Subscription or primary-region metadata is missing."
fi

if [[ -n "$expected_subscription_id" && -n "$secondary_region" ]]; then
  location_count="$(az account list-locations --subscription "$expected_subscription_id" --query "length([?name=='$secondary_region'])" --output tsv --only-show-errors 2>/dev/null || true)"
  if [[ "$location_count" == "1" ]]; then
    add_check "azure.secondary-region" "pass" "Secondary region '$secondary_region' is available to the subscription."
  else
    add_check "azure.secondary-region" "fail" "Secondary region '$secondary_region' is not available or could not be queried."
  fi
else
  add_check "azure.secondary-region" "fail" "Subscription or secondary-region metadata is missing."
fi

if [[ -n "$primary_region" && -n "$secondary_region" && "$primary_region" != "$secondary_region" ]]; then
  add_check "azure.region-separation" "pass" "Primary and secondary regions are distinct."
else
  add_check "azure.region-separation" "fail" "Primary and secondary regions must be distinct."
fi

mapfile -t providers < <(jq -r '.observedProviders[]?' "$manifest")
if (( ${#providers[@]} == 0 )); then
  add_check "azure.providers" "fail" "No provider namespaces are declared in run state."
else
  for provider in "${providers[@]}"; do
    provider_state="$(az provider show --namespace "$provider" --subscription "$expected_subscription_id" --query registrationState --output tsv --only-show-errors 2>/dev/null || true)"
    if [[ "$provider_state" == "Registered" ]]; then
      add_check "azure.provider.$provider" "pass" "$provider is Registered."
    elif [[ -n "$provider_state" ]]; then
      add_check "azure.provider.$provider" "warning" "$provider is $provider_state; no registration was attempted."
    else
      add_check "azure.provider.$provider" "warning" "$provider registration state could not be read."
    fi
  done
fi

quota_items="$(az vm list-usage --location "$primary_region" --subscription "$expected_subscription_id" --query 'length(@)' --output tsv --only-show-errors 2>/dev/null || true)"
if [[ "$quota_items" =~ ^[1-9][0-9]*$ ]]; then
  add_check "azure.compute-quota" "pass" "Compute usage/quota returned $quota_items item(s) for '$primary_region'."
else
  add_check "azure.compute-quota" "warning" "Compute usage/quota could not be read; no quota change was attempted."
fi

failure_count="$(jq '[.[] | select(.status == "fail")] | length' <<<"$checks")"
warning_count="$(jq '[.[] | select(.status == "warning" or .status == "skipped")] | length' <<<"$checks")"
if (( failure_count > 0 )); then
  result="fail"
  exit_code=1
elif (( warning_count > 0 )); then
  result="partial"
  exit_code=2
else
  result="pass"
  exit_code=0
fi

generated_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
cli_version="$(az version --query '"azure-cli"' --output tsv 2>/dev/null || true)"
temp_report="$run_dir/validation.json.tmp"
trap 'rm -f -- "$temp_report"' EXIT
jq -n \
  --arg generatedAt "$generated_at" \
  --arg runId "$run_id" \
  --arg result "$result" \
  --arg subscriptionId "$expected_subscription_id" \
  --arg tenantId "$expected_tenant_id" \
  --arg cliVersion "$cli_version" \
  --argjson checks "$checks" \
  '{
    schemaVersion: "1.0",
    labId: "LAB-00",
    runId: $runId,
    generatedAt: $generatedAt,
    result: $result,
    toolLane: "azure-cli",
    toolVersions: {azureCli: $cliVersion},
    targetContext: {subscriptionId: $subscriptionId, tenantId: $tenantId},
    checks: $checks
  }' >"$temp_report"
mv -- "$temp_report" "$report"
trap - EXIT

echo
echo "Validation result: $result"
echo "Machine-readable report: $report"
exit "$exit_code"
