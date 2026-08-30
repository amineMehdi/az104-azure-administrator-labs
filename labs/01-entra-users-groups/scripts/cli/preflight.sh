#!/usr/bin/env bash
set -Eeuo pipefail

usage() {
  cat <<'EOF'
Usage: preflight.sh --domain <verified-domain> [--tenant-id <tenant-guid>]

Runs read-only checks for the Lab 01 Azure CLI lane. The script never signs in,
changes context, assigns roles, or creates directory objects.
EOF
}

domain=""
expected_tenant_id=""

while (($#)); do
  case "$1" in
    --domain) domain="${2:-}"; shift 2 ;;
    --tenant-id) expected_tenant_id="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: Unknown argument: $1" >&2; usage >&2; exit 1 ;;
  esac
done

for tool in az jq; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "ERROR: Required tool not found: $tool" >&2
    exit 1
  fi
done

if [[ ! "$domain" =~ ^[A-Za-z0-9][A-Za-z0-9.-]*\.[A-Za-z]{2,}$ ]]; then
  echo "ERROR: --domain must be a verified DNS-style tenant domain." >&2
  exit 1
fi

if ! account_json=$(az account show --output json 2>/dev/null); then
  echo "ERROR: Azure CLI is not signed in. Run az login yourself and verify the tenant." >&2
  exit 1
fi

active_tenant_id=$(jq -r '.tenantId // empty' <<<"$account_json")
subscription_name=$(jq -r '.name // "<unknown>"' <<<"$account_json")
subscription_id=$(jq -r '.id // "<unknown>"' <<<"$account_json")

if [[ -z "$active_tenant_id" ]]; then
  echo "ERROR: The active Azure CLI context did not return a tenant ID." >&2
  exit 1
fi

if [[ -n "$expected_tenant_id" && "${active_tenant_id,,}" != "${expected_tenant_id,,}" ]]; then
  echo "ERROR: Active tenant $active_tenant_id does not match --tenant-id $expected_tenant_id." >&2
  exit 1
fi

graph_url="https://graph.microsoft.com/v1.0/domains/$domain?\$select=id,isVerified,authenticationType"
if ! domain_json=$(az rest --method get --url "$graph_url" --output json 2>/dev/null); then
  echo "ERROR: Microsoft Graph could not read domain '$domain'." >&2
  echo "Confirm the domain, Azure CLI sign-in, tenant role, and Graph access." >&2
  exit 1
fi

verified=$(jq -r '.isVerified // false' <<<"$domain_json")
if [[ "$verified" != "true" ]]; then
  echo "ERROR: Domain '$domain' is not reported as verified." >&2
  exit 1
fi

if ! az rest \
  --method get \
  --url 'https://graph.microsoft.com/v1.0/users?$top=1&$select=id,userPrincipalName' \
  --output none 2>/dev/null; then
  echo "ERROR: Microsoft Graph user discovery failed for the signed-in identity." >&2
  exit 1
fi

signed_in_upn=$(az ad signed-in-user show --query userPrincipalName --output tsv 2>/dev/null || true)

cat <<EOF
PASS: Azure CLI and Microsoft Graph read-only checks succeeded.
  Tenant ID:        $active_tenant_id
  Subscription:     $subscription_name ($subscription_id)
  Signed-in user:   ${signed_in_upn:-<not returned>}
  Verified domain:  $domain

Preflight cannot prove write authorization. The complete lab normally requires
Microsoft Entra User Administrator at the intended tenant scope. Azure RBAC roles
such as Owner or Contributor do not grant Microsoft Entra user management rights.
EOF
