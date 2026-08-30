#!/usr/bin/env bash
set -Eeuo pipefail

usage() {
  cat <<'EOF'
Usage: setup.sh --run-id <id> --domain <verified-domain> [--tenant-id <guid>] [--execute]

Without --execute, prints the planned tenant changes. With --execute, creates two
cloud-only users and one security group. Set AZ104_LAB_INITIAL_PASSWORD in the
environment before execution. The password is never written to run.json.
EOF
}

run_id=""
domain=""
expected_tenant_id=""
execute=false

while (($#)); do
  case "$1" in
    --run-id) run_id="${2:-}"; shift 2 ;;
    --domain) domain="${2:-}"; shift 2 ;;
    --tenant-id) expected_tenant_id="${2:-}"; shift 2 ;;
    --execute) execute=true; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: Unknown argument: $1" >&2; usage >&2; exit 1 ;;
  esac
done

if [[ ! "$run_id" =~ ^[a-z0-9][a-z0-9-]{2,20}$ ]]; then
  echo "ERROR: --run-id must be 3-21 lowercase letters, digits, or hyphens." >&2
  exit 1
fi
if [[ ! "$domain" =~ ^[A-Za-z0-9][A-Za-z0-9.-]*\.[A-Za-z]{2,}$ ]]; then
  echo "ERROR: --domain must be a verified DNS-style tenant domain." >&2
  exit 1
fi

for tool in az jq; do
  command -v "$tool" >/dev/null 2>&1 || { echo "ERROR: Required tool not found: $tool" >&2; exit 1; }
done

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
lab_root=$(cd -- "$script_dir/../.." && pwd)
state_dir="$lab_root/.state/$run_id"
manifest="$state_dir/run.json"
compact_id=$(tr -cd 'a-z0-9' <<<"$run_id" | cut -c1-16)
user_a_alias="az104l01a${compact_id}"
user_b_alias="az104l01b${compact_id}"
group_alias="az104l01g${compact_id}"
user_a_upn="$user_a_alias@$domain"
user_b_upn="$user_b_alias@$domain"
user_a_name="AZ104-L01-$run_id-Alex"
user_b_name="AZ104-L01-$run_id-Blair"
group_name="AZ104-L01-$run_id-Operators"

cat <<EOF
Planned Microsoft Entra changes for run '$run_id':
  Create user:  $user_a_name ($user_a_upn)
  Create user:  $user_b_name ($user_b_upn)
  Create group: $group_name ($group_alias)
  Set user department/job title properties
  Add user A as a direct group member
  Add user B as a group owner

No Azure resources, licenses, roles, or subscriptions will be changed.
EOF

if [[ "$execute" != "true" ]]; then
  echo "PLAN ONLY: rerun with --execute after reviewing the tenant and names."
  exit 0
fi

if [[ -z "${AZ104_LAB_INITIAL_PASSWORD:-}" || ${#AZ104_LAB_INITIAL_PASSWORD} -lt 12 ]]; then
  echo "ERROR: Set AZ104_LAB_INITIAL_PASSWORD to a policy-compliant temporary password of at least 12 characters." >&2
  exit 1
fi

preflight_args=(--domain "$domain")
[[ -n "$expected_tenant_id" ]] && preflight_args+=(--tenant-id "$expected_tenant_id")
"$script_dir/preflight.sh" "${preflight_args[@]}"

if [[ -f "$manifest" ]]; then
  state_status=$(jq -r '.status // "unknown"' "$manifest")
  echo "Existing state found for '$run_id'; setup will not create or replace objects."
  if [[ "$state_status" == "created" ]]; then
    "$script_dir/validate.sh" --run-id "$run_id"
    exit $?
  fi
  echo "ERROR: The recorded run status is '$state_status', which can represent a partial or cleaned run." >&2
  echo "Review the manifest and use cleanup's exact-ID preview before choosing a new run ID." >&2
  exit 1
fi

if az ad user show --id "$user_a_upn" --output none >/dev/null 2>&1 \
  || az ad user show --id "$user_b_upn" --output none >/dev/null 2>&1; then
  echo "ERROR: A planned user already exists but is not recorded in this run." >&2
  exit 1
fi

group_collision=$(az ad group list --filter "mailNickname eq '$group_alias'" --query 'length(@)' --output tsv 2>/dev/null || echo 1)
if [[ "$group_collision" != "0" ]]; then
  echo "ERROR: A planned group alias already exists or collision detection failed." >&2
  exit 1
fi

umask 077
mkdir -p "$state_dir"
active_tenant_id=$(az account show --query tenantId --output tsv)
created_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)

jq -n \
  --arg labId "LAB-01" \
  --arg runId "$run_id" \
  --arg tenantId "$active_tenant_id" \
  --arg domain "$domain" \
  --arg createdAt "$created_at" \
  --arg userAUpn "$user_a_upn" \
  --arg userBUpn "$user_b_upn" \
  --arg userAName "$user_a_name" \
  --arg userBName "$user_b_name" \
  --arg groupName "$group_name" \
  --arg groupAlias "$group_alias" \
  '{labId:$labId,runId:$runId,tenantId:$tenantId,domain:$domain,createdAt:$createdAt,status:"creating",names:{userA:{displayName:$userAName,userPrincipalName:$userAUpn},userB:{displayName:$userBName,userPrincipalName:$userBUpn},group:{displayName:$groupName,mailNickname:$groupAlias}},resources:[],passwordStored:false}' \
  >"$manifest"

update_manifest() {
  local filter="$1"
  shift
  jq "$@" "$filter" "$manifest" >"$manifest.tmp"
  mv -f "$manifest.tmp" "$manifest"
}

secret_file=""
secure_remove_secret() {
  [[ -z "$secret_file" || ! -f "$secret_file" ]] && return 0
  if command -v shred >/dev/null 2>&1; then
    shred -u "$secret_file"
  else
    rm -f "$secret_file"
  fi
}
trap secure_remove_secret EXIT

create_user() {
  local key="$1" display_name="$2" alias="$3" upn="$4" department="$5" title="$6"
  secret_file="$state_dir/.${key}-create.json"
  jq -n \
    --arg displayName "$display_name" \
    --arg mailNickname "$alias" \
    --arg userPrincipalName "$upn" \
    --arg password "$AZ104_LAB_INITIAL_PASSWORD" \
    '{accountEnabled:true,displayName:$displayName,mailNickname:$mailNickname,userPrincipalName:$userPrincipalName,passwordProfile:{forceChangePasswordNextSignIn:true,password:$password}}' \
    >"$secret_file"
  chmod 600 "$secret_file"

  local created_json object_id
  created_json=$(az rest --method post --url 'https://graph.microsoft.com/v1.0/users' --body "@$secret_file" --output json)
  secure_remove_secret
  secret_file=""
  object_id=$(jq -r '.id // empty' <<<"$created_json")
  [[ -n "$object_id" ]] || { echo "ERROR: Microsoft Graph did not return an object ID for $upn." >&2; return 1; }

  update_manifest '.resources += [{kind:"user",key:$key,id:$id,userPrincipalName:$upn,displayName:$name}]' \
    --arg key "$key" --arg id "$object_id" --arg upn "$upn" --arg name "$display_name"

  local patch_body
  patch_body=$(jq -nc --arg department "$department" --arg title "$title" --arg office "AZ104 Lab" '{department:$department,jobTitle:$title,officeLocation:$office}')
  az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$object_id" --body "$patch_body" --output none
  printf '%s\n' "$object_id"
}

user_a_id=$(create_user "userA" "$user_a_name" "$user_a_alias" "$user_a_upn" "Cloud Operations" "Azure Administrator Trainee")
user_b_id=$(create_user "userB" "$user_b_name" "$user_b_alias" "$user_b_upn" "Identity Operations" "Identity Administrator Trainee")

group_json=$(az ad group create \
  --display-name "$group_name" \
  --mail-nickname "$group_alias" \
  --description "Initial AZ-104 Lab 01 group; runId=$run_id" \
  --output json)
group_id=$(jq -r '.id // empty' <<<"$group_json")
[[ -n "$group_id" ]] || { echo "ERROR: Azure CLI did not return a group object ID." >&2; exit 1; }

update_manifest '.resources += [{kind:"group",key:"group",id:$id,mailNickname:$alias,displayName:$name}]' \
  --arg id "$group_id" --arg alias "$group_alias" --arg name "$group_name"

managed_description="Managed AZ-104 Lab 01 security group; runId=$run_id"
group_patch=$(jq -nc --arg description "$managed_description" '{description:$description}')
az rest --method patch --url "https://graph.microsoft.com/v1.0/groups/$group_id" --body "$group_patch" --output none
az ad group member add --group "$group_id" --member-id "$user_a_id" --output none
az ad group owner add --group "$group_id" --owner-object-id "$user_b_id" --output none

completed_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)
update_manifest '.status="created" | .completedAt=$completedAt | .relationships={memberUserId:$memberId,ownerUserId:$ownerId,groupId:$groupId} | .expected={userADepartment:"Cloud Operations",userBDepartment:"Identity Operations",userAJobTitle:"Azure Administrator Trainee",userBJobTitle:"Identity Administrator Trainee",officeLocation:"AZ104 Lab",groupDescription:$description}' \
  --arg completedAt "$completed_at" \
  --arg memberId "$user_a_id" \
  --arg ownerId "$user_b_id" \
  --arg groupId "$group_id" \
  --arg description "$managed_description"

unset AZ104_LAB_INITIAL_PASSWORD
echo "PASS: Lab 01 objects were created and exact object IDs were recorded in $manifest"
echo "Run: ./scripts/cli/validate.sh --run-id '$run_id'"
