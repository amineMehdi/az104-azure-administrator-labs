#!/usr/bin/env bash
set -euo pipefail

LAB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SUBSCRIPTION_ID="${AZURE_SUBSCRIPTION_ID:-}"
RUN_ID=""
EXECUTE=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --subscription-id) SUBSCRIPTION_ID="$2"; shift 2 ;;
    --run-id) RUN_ID="$2"; shift 2 ;;
    --execute) EXECUTE=true; shift ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
[[ -n "$SUBSCRIPTION_ID" && -n "$RUN_ID" ]] || { echo "Supply --subscription-id and --run-id." >&2; exit 2; }

MANIFEST="$LAB_ROOT/.state/$RUN_ID/run.json"
[[ -f "$MANIFEST" ]] || { echo "Missing state: $MANIFEST" >&2; exit 5; }
[[ "$(az account show --query id --output tsv)" == "$SUBSCRIPTION_ID" ]] || { echo "Active subscription mismatch." >&2; exit 4; }
[[ "$(jq -r '.subscriptionId' "$MANIFEST")" == "$SUBSCRIPTION_ID" ]] || { echo "Recorded subscription mismatch." >&2; exit 4; }
RG="$(jq -r '.resourceGroup.name' "$MANIFEST")"
RG_ID="$(jq -r '.resourceGroup.id' "$MANIFEST")"
echo "Cleanup preview for LAB-06:"
echo "  exact resource group ID: $RG_ID"
echo "  recorded child resources: $(jq '.resources | length' "$MANIFEST")"
echo "  residual/soft-delete behavior must be audited after deletion."
if [[ "$EXECUTE" != true ]]; then
  echo "Preview only. Re-run with --execute after checking every target."
  exit 0
fi

actual="$(az group show --name "$RG" --query id --output tsv 2>/dev/null || true)"
if [[ -z "$actual" ]]; then echo "Resource group is already absent; cleanup is idempotent."; exit 0; fi
purpose="$(az group show --name "$RG" --query tags.purpose --output tsv)"
lab_id="$(az group show --name "$RG" --query tags.labId --output tsv)"
run_id="$(az group show --name "$RG" --query tags.runId --output tsv)"
[[ "${actual,,}" == "${RG_ID,,}" && "$purpose" == az104-lab && "$lab_id" == 06 && "$run_id" == "$RUN_ID" ]] || {
  echo "ID or ownership-tag verification failed; refusing cleanup." >&2; exit 6;
}

az group delete --ids "$RG_ID" --yes --output none

if az group exists --name "$RG" | grep -qi true; then
  echo "Resource group still exists; deletion may be asynchronous or blocked." >&2
  exit 7
fi
jq '.status="cleanup-complete"' "$MANIFEST" >"$MANIFEST.tmp" && mv -f "$MANIFEST.tmp" "$MANIFEST"
echo "Active resource-group cleanup complete. Audit soft-deleted or externally retained items separately."
