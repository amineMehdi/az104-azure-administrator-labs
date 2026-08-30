#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Read-only preflight for Lab 00.

Usage:
  ./preflight.sh [--subscription-id GUID] [--tenant-id GUID]
                 [--location NAME] [--secondary-location NAME]

Exit codes:
  0  all required checks passed
  1  a required check failed
  2  required checks passed, with warnings or skipped optional checks

This script never signs in, changes the active subscription, registers a
provider, creates a resource, or changes Azure state.
EOF
}

subscription_id=""
expected_tenant_id=""
location="westeurope"
secondary_location="northeurope"

while (( $# > 0 )); do
  case "$1" in
    --subscription-id)
      [[ $# -ge 2 ]] || { echo "ERROR: --subscription-id requires a value." >&2; exit 1; }
      subscription_id="$2"
      shift 2
      ;;
    --tenant-id)
      [[ $# -ge 2 ]] || { echo "ERROR: --tenant-id requires a value." >&2; exit 1; }
      expected_tenant_id="$2"
      shift 2
      ;;
    --location)
      [[ $# -ge 2 ]] || { echo "ERROR: --location requires a value." >&2; exit 1; }
      location="$2"
      shift 2
      ;;
    --secondary-location)
      [[ $# -ge 2 ]] || { echo "ERROR: --secondary-location requires a value." >&2; exit 1; }
      secondary_location="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument '$1'." >&2
      usage >&2
      exit 1
      ;;
  esac
done

guid_pattern='^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
location_pattern='^[a-z0-9-]+$'

if [[ -n "$subscription_id" && ! "$subscription_id" =~ $guid_pattern ]]; then
  echo "ERROR: --subscription-id must be a subscription GUID." >&2
  exit 1
fi
if [[ -n "$expected_tenant_id" && ! "$expected_tenant_id" =~ $guid_pattern ]]; then
  echo "ERROR: --tenant-id must be a tenant GUID." >&2
  exit 1
fi
if [[ ! "$location" =~ $location_pattern || ! "$secondary_location" =~ $location_pattern ]]; then
  echo "ERROR: region names may contain only lowercase letters, digits, and hyphens." >&2
  exit 1
fi

errors=0
warnings=0

pass() { printf '[PASS] %s\n' "$1"; }
fail() { printf '[FAIL] %s\n' "$1" >&2; errors=$((errors + 1)); }
warn() { printf '[WARN] %s\n' "$1"; warnings=$((warnings + 1)); }

echo "Lab 00 - Azure CLI preflight (read only)"
echo "========================================="

if ! command -v az >/dev/null 2>&1; then
  fail "Azure CLI is not available on PATH."
  exit 1
fi

cli_version="$(az version --query '"azure-cli"' --output tsv 2>/dev/null || true)"
if [[ -n "$cli_version" ]]; then
  pass "Azure CLI version: $cli_version"
else
  fail "Azure CLI version could not be read."
fi

account_json="$(az account show --only-show-errors --output json 2>/dev/null || true)"
if [[ -z "$account_json" ]]; then
  fail "No active Azure CLI session. Run 'az login' interactively, then rerun preflight."
  exit 1
fi

current_subscription_id="$(az account show --query id --output tsv --only-show-errors 2>/dev/null || true)"
current_tenant_id="$(az account show --query tenantId --output tsv --only-show-errors 2>/dev/null || true)"
current_subscription_name="$(az account show --query name --output tsv --only-show-errors 2>/dev/null || true)"
current_state="$(az account show --query state --output tsv --only-show-errors 2>/dev/null || true)"
cloud_name="$(az cloud show --query name --output tsv 2>/dev/null || true)"

[[ -n "$subscription_id" ]] || subscription_id="$current_subscription_id"

echo
echo "Exact active context (do not include this block in screenshots):"
printf '  Cloud:        %s\n' "$cloud_name"
printf '  Subscription: %s\n' "$current_subscription_name"
printf '  Subscription ID: %s\n' "$current_subscription_id"
printf '  Tenant ID:       %s\n' "$current_tenant_id"

if [[ "$current_subscription_id" == "$subscription_id" ]]; then
  pass "The active subscription matches the requested subscription."
else
  fail "Active subscription does not match --subscription-id. Review it, then use 'az account set --subscription <id>' yourself."
fi

if [[ -z "$expected_tenant_id" || "$current_tenant_id" == "$expected_tenant_id" ]]; then
  pass "The active tenant matches the requested tenant (or no tenant override was supplied)."
else
  fail "Active tenant does not match --tenant-id. Stop and sign in to the intended sandbox tenant."
fi

if [[ "$current_state" == "Enabled" ]]; then
  pass "Subscription state is Enabled."
else
  fail "Subscription state is '$current_state', not Enabled."
fi

for region in "$location" "$secondary_location"; do
  available="$(az account list-locations --subscription "$subscription_id" --query "length([?name=='$region'])" --output tsv --only-show-errors 2>/dev/null || true)"
  if [[ "$available" == "1" ]]; then
    pass "Region '$region' is listed for this subscription."
  else
    fail "Region '$region' was not found for this subscription. Choose another region."
  fi
done

if [[ "$location" == "$secondary_location" ]]; then
  warn "Primary and secondary regions are identical; later resilience labs need two regions."
fi

echo
echo "Observed provider registration (this script does not register providers):"
providers=(
  Microsoft.Authorization
  Microsoft.Compute
  Microsoft.Insights
  Microsoft.Network
  Microsoft.RecoveryServices
  Microsoft.Storage
)
for provider in "${providers[@]}"; do
  provider_state="$(az provider show --namespace "$provider" --subscription "$subscription_id" --query registrationState --output tsv --only-show-errors 2>/dev/null || true)"
  if [[ "$provider_state" == "Registered" ]]; then
    pass "$provider is Registered."
  elif [[ -n "$provider_state" ]]; then
    warn "$provider is $provider_state. Register it only when a later authorized lab requires it."
  else
    warn "$provider registration state could not be read with the current permissions."
  fi
done

if az vm list-usage --location "$location" --subscription "$subscription_id" --only-show-errors --output none >/dev/null 2>&1; then
  pass "Regional compute usage/quota can be queried in '$location'."
else
  warn "Compute usage/quota could not be queried in '$location'; check Reader access and Microsoft.Compute registration."
fi

echo
echo "Cost guardrail"
echo "  This lab creates zero Azure resources and has cost class 'none'."
echo "  Later labs may be billable: estimate first, obtain authorization, tag every"
echo "  resource, and tear it down in the same session. Azure budgets alert; they"
echo "  do not stop resources or consumption."

echo
if (( errors > 0 )); then
  echo "Preflight result: FAIL ($errors required check(s) failed, $warnings warning(s))."
  exit 1
elif (( warnings > 0 )); then
  echo "Preflight result: PARTIAL ($warnings warning(s); review before later labs)."
  exit 2
else
  echo "Preflight result: PASS."
  exit 0
fi
