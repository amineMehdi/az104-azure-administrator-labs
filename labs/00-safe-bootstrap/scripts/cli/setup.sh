#!/usr/bin/env bash

set -euo pipefail
umask 077

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
LAB_ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd -P)"

usage() {
  cat <<'EOF'
Create Lab 00 local run state. No Azure resources or settings are changed.

Usage:
  ./setup.sh [--subscription-id GUID] [--tenant-id GUID]
             [--location NAME] [--secondary-location NAME]
             [--run-id ID] [--state-root PATH]

The active Azure CLI subscription and tenant must match any IDs supplied.
EOF
}

subscription_id=""
expected_tenant_id=""
location="westeurope"
secondary_location="northeurope"
run_id=""
state_root="$LAB_ROOT/.state"

while (( $# > 0 )); do
  case "$1" in
    --subscription-id) [[ $# -ge 2 ]] || exit 1; subscription_id="$2"; shift 2 ;;
    --tenant-id) [[ $# -ge 2 ]] || exit 1; expected_tenant_id="$2"; shift 2 ;;
    --location) [[ $# -ge 2 ]] || exit 1; location="$2"; shift 2 ;;
    --secondary-location) [[ $# -ge 2 ]] || exit 1; secondary_location="$2"; shift 2 ;;
    --run-id) [[ $# -ge 2 ]] || exit 1; run_id="$2"; shift 2 ;;
    --state-root) [[ $# -ge 2 ]] || exit 1; state_root="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: unknown argument '$1'." >&2; usage >&2; exit 1 ;;
  esac
done

guid_pattern='^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
location_pattern='^[a-z0-9-]+$'
run_pattern='^[a-z0-9][a-z0-9-]{2,31}$'

command -v az >/dev/null 2>&1 || { echo "ERROR: Azure CLI is required." >&2; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "ERROR: jq 1.6 or later is required by the CLI lane." >&2; exit 1; }

current_account="$(az account show --only-show-errors --output json 2>/dev/null || true)"
[[ -n "$current_account" ]] || { echo "ERROR: no active Azure CLI session. Run 'az login' interactively." >&2; exit 1; }

current_subscription_id="$(jq -r '.id // empty' <<<"$current_account")"
current_tenant_id="$(jq -r '.tenantId // empty' <<<"$current_account")"
current_state="$(jq -r '.state // empty' <<<"$current_account")"
cloud_name="$(jq -r '.environmentName // empty' <<<"$current_account")"

[[ -n "$subscription_id" ]] || subscription_id="$current_subscription_id"
[[ -n "$expected_tenant_id" ]] || expected_tenant_id="$current_tenant_id"

[[ "$subscription_id" =~ $guid_pattern ]] || { echo "ERROR: subscription ID must be a GUID." >&2; exit 1; }
[[ "$expected_tenant_id" =~ $guid_pattern ]] || { echo "ERROR: tenant ID must be a GUID." >&2; exit 1; }
[[ "$location" =~ $location_pattern && "$secondary_location" =~ $location_pattern ]] || { echo "ERROR: invalid region name." >&2; exit 1; }
[[ "$location" != "$secondary_location" ]] || { echo "ERROR: primary and secondary regions must differ." >&2; exit 1; }

if [[ "$current_subscription_id" != "$subscription_id" || "$current_tenant_id" != "$expected_tenant_id" ]]; then
  echo "ERROR: active Azure context does not match the requested tenant/subscription." >&2
  echo "Review 'az account show', change context yourself, and rerun setup." >&2
  exit 1
fi
[[ "$current_state" == "Enabled" ]] || { echo "ERROR: subscription state is '$current_state'." >&2; exit 1; }

for region in "$location" "$secondary_location"; do
  available="$(az account list-locations --subscription "$subscription_id" --query "length([?name=='$region'])" --output tsv --only-show-errors 2>/dev/null || true)"
  [[ "$available" == "1" ]] || { echo "ERROR: region '$region' is unavailable to this subscription." >&2; exit 1; }
done

if [[ -z "$run_id" ]]; then
  run_id="az10400-$(date -u +%Y%m%d%H%M%S)-$(printf '%04d' "$((RANDOM % 10000))")"
fi
[[ "$run_id" =~ $run_pattern ]] || { echo "ERROR: run ID must match $run_pattern." >&2; exit 1; }

mkdir -p -- "$state_root"
state_root="$(cd -- "$state_root" && pwd -P)"
run_dir="$state_root/$run_id"
manifest="$run_dir/run.json"

if [[ -f "$manifest" ]]; then
  existing_lab="$(jq -r '.labId // empty' "$manifest" 2>/dev/null || true)"
  existing_run="$(jq -r '.runId // empty' "$manifest" 2>/dev/null || true)"
  if [[ "$existing_lab" == "00-safe-bootstrap" && "$existing_run" == "$run_id" ]]; then
    echo "Run '$run_id' is already initialized; existing state was left unchanged."
    echo "State: $manifest"
    exit 0
  fi
  echo "ERROR: an incompatible manifest already exists at '$manifest'." >&2
  exit 1
fi
if [[ -e "$run_dir" ]]; then
  echo "ERROR: '$run_dir' exists without a valid run manifest; refusing to overwrite it." >&2
  exit 1
fi

mkdir -- "$run_dir"
token="$(printf '%s' "$run_id" | tr -cd 'a-z0-9')"
token="${token: -10}"
resource_group_name="rg-az104-00-$token"
global_name_stem="az10400$token"
global_name_stem="${global_name_stem:0:24}"
created_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
if expires_on="$(date -u -d '+1 day' +%Y-%m-%d 2>/dev/null)"; then
  :
elif expires_on="$(date -u -v+1d +%Y-%m-%d 2>/dev/null)"; then
  :
else
  expires_on="$(date -u +%Y-%m-%d)"
fi

temp_manifest="$run_dir/run.json.tmp"
trap 'rm -f -- "$temp_manifest"' EXIT

jq -n \
  --arg createdAt "$created_at" \
  --arg runId "$run_id" \
  --arg subscriptionId "$subscription_id" \
  --arg tenantId "$expected_tenant_id" \
  --arg cloudName "$cloud_name" \
  --arg primaryRegion "$location" \
  --arg secondaryRegion "$secondary_location" \
  --arg resourceGroup "$resource_group_name" \
  --arg globalNameStem "$global_name_stem" \
  --arg expiresOn "$expires_on" \
  '{
    schemaVersion: "1.0",
    labId: "00-safe-bootstrap",
    runId: $runId,
    createdAt: $createdAt,
    context: {
      cloudName: $cloudName,
      subscriptionId: $subscriptionId,
      tenantId: $tenantId
    },
    regions: {
      primary: $primaryRegion,
      secondary: $secondaryRegion
    },
    naming: {
      resourceGroup: $resourceGroup,
      globalNameStem: $globalNameStem
    },
    tags: {
      purpose: "az104-lab",
      labId: "00-safe-bootstrap",
      runId: $runId,
      expiresOn: $expiresOn
    },
    observedProviders: [
      "Microsoft.Authorization",
      "Microsoft.Compute",
      "Microsoft.Insights",
      "Microsoft.Network",
      "Microsoft.RecoveryServices",
      "Microsoft.Storage"
    ],
    resources: [],
    tenantScopedChanges: [],
    liveAzureMutations: false
  }' >"$temp_manifest"

mv -- "$temp_manifest" "$manifest"
trap - EXIT

echo "Local Lab 00 state initialized."
echo "  Run ID:          $run_id"
echo "  Primary region:  $location"
echo "  Secondary region:$secondary_location"
echo "  Name example:    $resource_group_name"
echo "  State:           $manifest"
echo "No Azure resources or settings were changed."
