#!/usr/bin/env bash
set -euo pipefail

SUBSCRIPTION_ID="${AZURE_SUBSCRIPTION_ID:-}"
LOCATION="${AZURE_LOCATION:-}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --subscription-id) SUBSCRIPTION_ID="$2"; shift 2 ;;
    --location) LOCATION="$2"; shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

[[ -n "$SUBSCRIPTION_ID" ]] || { echo "Supply --subscription-id or AZURE_SUBSCRIPTION_ID." >&2; exit 2; }
[[ -n "$LOCATION" ]] || { echo "Supply --location or AZURE_LOCATION." >&2; exit 2; }

require_tool() { command -v "$1" >/dev/null 2>&1 || { echo "Missing required tool: $1" >&2; exit 3; }; }
require_tool az
require_tool jq


ACCOUNT_JSON="$(az account show --output json)"
ACTIVE_SUBSCRIPTION="$(jq -r '.id' <<<"$ACCOUNT_JSON")"
ACTIVE_TENANT="$(jq -r '.tenantId' <<<"$ACCOUNT_JSON")"
[[ "$ACTIVE_SUBSCRIPTION" == "$SUBSCRIPTION_ID" ]] || {
  echo "Context mismatch: active subscription is $ACTIVE_SUBSCRIPTION, expected $SUBSCRIPTION_ID." >&2
  echo "Select the intended context yourself; this script will not change it." >&2
  exit 4
}

echo "Lab: LAB-06"
echo "Tenant: $ACTIVE_TENANT"
echo "Subscription: $ACTIVE_SUBSCRIPTION"
echo "Location: $LOCATION"
echo "Cost class: low"
echo "Role boundary: Contributor on the lab resource group"

for provider in Microsoft.Storage; do
  state="$(az provider show --namespace "$provider" --query registrationState --output tsv 2>/dev/null || true)"
  printf 'Provider %-38s %s
' "$provider" "${state:-Unavailable}"
done

echo "Preflight is read-only. Register missing providers only after an explicit scope and cost review."
