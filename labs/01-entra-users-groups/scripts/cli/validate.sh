#!/usr/bin/env bash
set -Eeuo pipefail

usage() {
  echo "Usage: validate.sh --run-id <id>" >&2
}

run_id=""
while (($#)); do
  case "$1" in
    --run-id) run_id="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: Unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ ! "$run_id" =~ ^[a-z0-9][a-z0-9-]{2,20}$ ]]; then
  echo "ERROR: Invalid --run-id." >&2
  exit 1
fi
for tool in az jq; do
  command -v "$tool" >/dev/null 2>&1 || { echo "ERROR: Required tool not found: $tool" >&2; exit 1; }
done

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
lab_root=$(cd -- "$script_dir/../.." && pwd)
state_dir="$lab_root/.state/$run_id"
manifest="$state_dir/run.json"
report="$state_dir/validation.json"

[[ -f "$manifest" ]] || { echo "ERROR: Missing state manifest: $manifest" >&2; exit 1; }

umask 077
generated_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)
jq -n --arg labId "LAB-01" --arg runId "$run_id" --arg generatedAt "$generated_at" '{labId:$labId,runId:$runId,generatedAt:$generatedAt,result:"skipped",checks:[]}' >"$report"

add_check() {
  local id="$1" status="$2" message="$3"
  jq --arg id "$id" --arg status "$status" --arg message "$message" '.checks += [{id:$id,status:$status,message:$message}]' "$report" >"$report.tmp"
  mv -f "$report.tmp" "$report"
}

tenant_id=$(jq -r '.tenantId // empty' "$manifest")
active_tenant_id=$(az account show --query tenantId --output tsv 2>/dev/null || true)
if [[ -n "$tenant_id" && "${tenant_id,,}" == "${active_tenant_id,,}" ]]; then
  add_check "context.tenant" "pass" "Active Azure CLI tenant matches the recorded tenant."
else
  add_check "context.tenant" "fail" "Active tenant does not match the recorded tenant; validation stopped before trusting directory results."
  jq '.result="fail"' "$report" >"$report.tmp"
  mv -f "$report.tmp" "$report"
  jq '{labId,runId,generatedAt,result,checks}' "$report"
  exit 1
fi

user_a_id=$(jq -r '.relationships.memberUserId // empty' "$manifest")
user_b_id=$(jq -r '.relationships.ownerUserId // empty' "$manifest")
group_id=$(jq -r '.relationships.groupId // empty' "$manifest")

validate_user() {
  local key="$1" object_id="$2" expected_upn="$3" expected_name="$4" expected_department="$5" expected_title="$6"
  local url user_json actual
  url="https://graph.microsoft.com/v1.0/users/$object_id?\$select=id,displayName,userPrincipalName,accountEnabled,department,jobTitle,officeLocation"
  if user_json=$(az rest --method get --url "$url" --output json 2>/dev/null); then
    actual=$(jq -r '[.id,.userPrincipalName,.displayName,(.accountEnabled|tostring),.department,.jobTitle,.officeLocation] | @tsv' <<<"$user_json")
    expected=$(printf '%s\t%s\t%s\ttrue\t%s\t%s\tAZ104 Lab' "$object_id" "$expected_upn" "$expected_name" "$expected_department" "$expected_title")
    if [[ "$actual" == "$expected" ]]; then
      add_check "identity.$key" "pass" "$expected_upn exists with the expected managed properties."
    else
      add_check "identity.$key" "fail" "$expected_upn exists but one or more managed properties drifted."
    fi
  else
    add_check "identity.$key" "fail" "Recorded user $expected_upn could not be read by exact object ID."
  fi
}

validate_user \
  "user-a" "$user_a_id" \
  "$(jq -r '.names.userA.userPrincipalName' "$manifest")" \
  "$(jq -r '.names.userA.displayName' "$manifest")" \
  "$(jq -r '.expected.userADepartment' "$manifest")" \
  "$(jq -r '.expected.userAJobTitle' "$manifest")"

validate_user \
  "user-b" "$user_b_id" \
  "$(jq -r '.names.userB.userPrincipalName' "$manifest")" \
  "$(jq -r '.names.userB.displayName' "$manifest")" \
  "$(jq -r '.expected.userBDepartment' "$manifest")" \
  "$(jq -r '.expected.userBJobTitle' "$manifest")"

group_url="https://graph.microsoft.com/v1.0/groups/$group_id?\$select=id,displayName,mailNickname,description,securityEnabled,mailEnabled"
if group_json=$(az rest --method get --url "$group_url" --output json 2>/dev/null); then
  group_actual=$(jq -r '[.id,.displayName,.mailNickname,.description,(.securityEnabled|tostring),(.mailEnabled|tostring)] | @tsv' <<<"$group_json")
  group_expected=$(printf '%s\t%s\t%s\t%s\ttrue\tfalse' \
    "$group_id" \
    "$(jq -r '.names.group.displayName' "$manifest")" \
    "$(jq -r '.names.group.mailNickname' "$manifest")" \
    "$(jq -r '.expected.groupDescription' "$manifest")")
  if [[ "$group_actual" == "$group_expected" ]]; then
    add_check "identity.group" "pass" "The recorded security group has the expected managed properties."
  else
    add_check "identity.group" "fail" "The recorded group exists but its type or managed properties drifted."
  fi
else
  add_check "identity.group" "fail" "The recorded group could not be read by exact object ID."
fi

member_value=$(az ad group member check --group "$group_id" --member-id "$user_a_id" --query value --output tsv 2>/dev/null || true)
if [[ "${member_value,,}" == "true" ]]; then
  add_check "relationship.member" "pass" "User A is a direct member of the lab group."
else
  add_check "relationship.member" "fail" "User A is not a direct member of the lab group."
fi

negative_member_value=$(az ad group member check --group "$group_id" --member-id "$user_b_id" --query value --output tsv 2>/dev/null || true)
if [[ "${negative_member_value,,}" == "false" ]]; then
  add_check "relationship.negative-member" "pass" "Negative control passed: user B is not a direct group member."
else
  add_check "relationship.negative-member" "fail" "Negative control failed: user B unexpectedly became a direct member."
fi

owner_count=$(az ad group owner list --group "$group_id" --query "[?id=='$user_b_id'] | length(@)" --output tsv 2>/dev/null || echo 0)
if [[ "$owner_count" == "1" ]]; then
  add_check "relationship.owner" "pass" "User B is an owner of the lab group."
else
  add_check "relationship.owner" "fail" "User B is not recorded as a group owner."
fi

failures=$(jq '[.checks[] | select(.status=="fail")] | length' "$report")
warnings=$(jq '[.checks[] | select(.status=="warning")] | length' "$report")
if ((failures > 0)); then
  result="fail"
  exit_code=1
elif ((warnings > 0)); then
  result="partial"
  exit_code=2
else
  result="pass"
  exit_code=0
fi

jq --arg result "$result" '.result=$result' "$report" >"$report.tmp"
mv -f "$report.tmp" "$report"
jq '{labId,runId,generatedAt,result,checks}' "$report"
exit "$exit_code"
