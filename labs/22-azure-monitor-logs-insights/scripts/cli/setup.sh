#!/usr/bin/env bash
set -euo pipefail

LAB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SUBSCRIPTION_ID="${AZURE_SUBSCRIPTION_ID:-}"
LOCATION="${AZURE_LOCATION:-}"
SECONDARY_LOCATION="${AZURE_SECONDARY_LOCATION:-}"
RUN_ID=""
EXECUTE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --subscription-id) SUBSCRIPTION_ID="$2"; shift 2 ;;
    --location) LOCATION="$2"; shift 2 ;;
    --secondary-location) SECONDARY_LOCATION="$2"; shift 2 ;;
    --run-id) RUN_ID="$2"; shift 2 ;;
    --execute) EXECUTE=true; shift ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

[[ -n "$SUBSCRIPTION_ID" && -n "$LOCATION" && -n "$RUN_ID" ]] || {
  echo "Usage: $0 --subscription-id ID --location REGION --run-id RUN [--secondary-location REGION] [--execute]" >&2
  exit 2
}
[[ "$RUN_ID" =~ ^[a-z0-9-]+$ ]] || { echo "Run ID must match ^[a-z0-9-]+$." >&2; exit 2; }

RG="rg-az104-l22-${RUN_ID}"
SUFFIX="$(printf '%s' "$RUN_ID" | tr -cd 'a-z0-9' | tail -c 12)"
STATE_DIR="$LAB_ROOT/.state/$RUN_ID"
MANIFEST="$STATE_DIR/run.json"
EXPIRES_ON="$(date -u -d '+1 day' +%F 2>/dev/null || date -u +%F)"

echo "LAB-22 plan"
echo "  subscription: $SUBSCRIPTION_ID"
echo "  location: $LOCATION"
echo "  resource group: $RG"
echo "  cost class: moderate"
echo "  external gate: None beyond the declared role and a disposable subscription."
echo "  resources: resource group, Log Analytics workspace, storage account, diagnostic setting, optional data collection rule"

if [[ "$EXECUTE" != true ]]; then
  echo "Preview only. Re-run with --execute after approving context, permissions, cost, and gates."
  exit 0
fi

"$LAB_ROOT/scripts/cli/preflight.sh" --subscription-id "$SUBSCRIPTION_ID" --location "$LOCATION"
[[ ! -e "$MANIFEST" ]] || { echo "State already exists at $MANIFEST; choose a new run ID." >&2; exit 5; }
mkdir -p "$STATE_DIR"
TENANT_ID="$(az account show --query tenantId --output tsv)"
jq -n   --arg labId "LAB-22" --arg runId "$RUN_ID" --arg tenantId "$TENANT_ID"   --arg subscriptionId "$SUBSCRIPTION_ID" --arg location "$LOCATION" --arg rgName "$RG"   --arg createdAt "$(date -u +%Y-%m-%dT%H:%M:%SZ)"   '{labId:$labId,runId:$runId,tenantId:$tenantId,subscriptionId:$subscriptionId,location:$location,createdAt:$createdAt,status:"recorded-before-mutation",resourceGroup:{name:$rgName,id:null},resources:[],external:{}}' >"$MANIFEST"

az group create --subscription "$SUBSCRIPTION_ID" --name "$RG" --location "$LOCATION"   --tags purpose=az104-lab labId=22 runId="$RUN_ID" expiresOn="$EXPIRES_ON" --output none
RG_ID="$(az group show --subscription "$SUBSCRIPTION_ID" --name "$RG" --query id --output tsv)"
jq --arg id "$RG_ID" '.resourceGroup.id=$id | .status="baseline-created"' "$MANIFEST" >"$MANIFEST.tmp"
mv -f "$MANIFEST.tmp" "$MANIFEST"

WORKSPACE="law-${SUFFIX}"
STORAGE="st22${SUFFIX}"
az monitor log-analytics workspace create --resource-group "$RG" --workspace-name "$WORKSPACE" --location "$LOCATION" --retention-time 30 --output none
az storage account create --resource-group "$RG" --name "$STORAGE" --location "$LOCATION" --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
WORKSPACE_ID=$(az monitor log-analytics workspace show --resource-group "$RG" --workspace-name "$WORKSPACE" --query id --output tsv)
STORAGE_ID=$(az storage account show --resource-group "$RG" --name "$STORAGE" --query id --output tsv)
az monitor diagnostic-settings create --name "diag-${RUN_ID}" --resource "$STORAGE_ID" --workspace "$WORKSPACE_ID" --metrics '[{"category":"Transaction","enabled":true}]' --output none

az resource list --subscription "$SUBSCRIPTION_ID" --resource-group "$RG" --output json >"$STATE_DIR/resources.json"
jq --slurpfile resources "$STATE_DIR/resources.json" '.resources=($resources[0] | map({id,name,type,location})) | .status="setup-complete"' "$MANIFEST" >"$MANIFEST.tmp"
mv -f "$MANIFEST.tmp" "$MANIFEST"
echo "Setup complete. State: $MANIFEST"
echo "Run scripts/cli/validate.sh before recording command evidence."
