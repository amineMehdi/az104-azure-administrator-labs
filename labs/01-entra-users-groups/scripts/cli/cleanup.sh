#!/usr/bin/env bash
set -Eeuo pipefail

usage() {
  cat <<'EOF'
Usage: cleanup.sh --run-id <id> [--execute] [--purge-deleted-users]

Default behavior is a deletion preview. --execute deletes the exact recorded group
and users. User deletion is recoverable. --purge-deleted-users permanently removes
the two exact deleted user objects and is irreversible.
EOF
}

run_id=""
execute=false
purge=false
while (($#)); do
  case "$1" in
    --run-id) run_id="${2:-}"; shift 2 ;;
    --execute) execute=true; shift ;;
    --purge-deleted-users) purge=true; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: Unknown argument: $1" >&2; usage >&2; exit 1 ;;
  esac
done

if [[ ! "$run_id" =~ ^[a-z0-9][a-z0-9-]{2,20}$ ]]; then
  echo "ERROR: Invalid --run-id." >&2
  exit 1
fi
if [[ "$purge" == "true" && "$execute" != "true" ]]; then
  echo "ERROR: --purge-deleted-users requires --execute." >&2
  exit 1
fi
for tool in az jq; do
  command -v "$tool" >/dev/null 2>&1 || { echo "ERROR: Required tool not found: $tool" >&2; exit 1; }
done

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
lab_root=$(cd -- "$script_dir/../.." && pwd)
state_dir="$lab_root/.state/$run_id"
manifest="$state_dir/run.json"
[[ -f "$manifest" ]] || { echo "Nothing to clean: state does not exist for '$run_id'."; exit 0; }

tenant_id=$(jq -r '.tenantId // empty' "$manifest")
active_tenant_id=$(az account show --query tenantId --output tsv 2>/dev/null || true)
if [[ -z "$tenant_id" || "${tenant_id,,}" != "${active_tenant_id,,}" ]]; then
  echo "ERROR: Active tenant does not match the recorded tenant. No deletion attempted." >&2
  exit 1
fi

resource_count=$(jq '.resources | length' "$manifest")
unknown_resources=$(jq '[.resources[] | select((.kind!="user" and .kind!="group") or (.kind=="user" and (.key!="userA" and .key!="userB")) or (.id|type)!="string" or (.id|length)==0)] | length' "$manifest")
duplicate_keys=$(jq '[.resources[].key] | length != (unique | length)' "$manifest")
if ((resource_count > 3)) || [[ "$unknown_resources" != "0" || "$duplicate_keys" != "false" ]]; then
  echo "ERROR: State contains an unexpected, duplicate, or invalid directory object. No deletion attempted." >&2
  exit 1
fi

group_id=$(jq -r '[.resources[] | select(.kind=="group") | .id][0] // empty' "$manifest")
user_a_id=$(jq -r '[.resources[] | select(.key=="userA") | .id][0] // empty' "$manifest")
user_b_id=$(jq -r '[.resources[] | select(.key=="userB") | .id][0] // empty' "$manifest")

cat <<EOF
Deletion plan for tenant $tenant_id and run '$run_id':
  Group object ID: ${group_id:-<not recorded>}
  User A object ID: ${user_a_id:-<not recorded>}
  User B object ID: ${user_b_id:-<not recorded>}
  User deletion mode: $([[ "$purge" == "true" ]] && echo permanent-purge || echo recoverable-soft-delete)
EOF

if [[ "$execute" != "true" ]]; then
  echo "PLAN ONLY: rerun with --execute after reviewing the exact object IDs."
  exit 0
fi

expected_group_name=$(jq -r '.names.group.displayName' "$manifest")
if [[ -n "$group_id" ]] && group_json=$(az ad group show --group "$group_id" --output json 2>/dev/null); then
  actual_group_name=$(jq -r '.displayName // empty' <<<"$group_json")
  [[ "$actual_group_name" == "$expected_group_name" ]] || { echo "ERROR: Group identity check failed; refusing deletion." >&2; exit 1; }
  az ad group delete --group "$group_id" --output none
fi

delete_user_if_expected() {
  local object_id="$1" expected_upn="$2"
  if user_json=$(az ad user show --id "$object_id" --output json 2>/dev/null); then
    actual_upn=$(jq -r '.userPrincipalName // empty' <<<"$user_json")
    [[ "${actual_upn,,}" == "${expected_upn,,}" ]] || { echo "ERROR: User identity check failed for $object_id; refusing deletion." >&2; return 1; }
    az ad user delete --id "$object_id" --output none
  fi
}

[[ -n "$user_a_id" ]] && delete_user_if_expected "$user_a_id" "$(jq -r '.names.userA.userPrincipalName' "$manifest")"
[[ -n "$user_b_id" ]] && delete_user_if_expected "$user_b_id" "$(jq -r '.names.userB.userPrincipalName' "$manifest")"

if [[ "$purge" == "true" ]]; then
  echo "Permanently purging the two exact recorded deleted user IDs. This cannot be undone."
  for object_id in "$user_a_id" "$user_b_id"; do
    [[ -z "$object_id" ]] && continue
    az rest --method delete --url "https://graph.microsoft.com/v1.0/directory/deletedItems/$object_id" --output none
  done
fi

cleanup_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)
jq --arg cleanupAt "$cleanup_at" --arg mode "$([[ "$purge" == "true" ]] && echo purged || echo soft-deleted)" '.status="cleaned" | .cleanup={completedAt:$cleanupAt,userDeletionMode:$mode}' "$manifest" >"$manifest.tmp"
mv -f "$manifest.tmp" "$manifest"

residual=0
[[ -n "$group_id" ]] && az ad group show --group "$group_id" --output none >/dev/null 2>&1 && residual=$((residual + 1))
[[ -n "$user_a_id" ]] && az ad user show --id "$user_a_id" --output none >/dev/null 2>&1 && residual=$((residual + 1))
[[ -n "$user_b_id" ]] && az ad user show --id "$user_b_id" --output none >/dev/null 2>&1 && residual=$((residual + 1))

if ((residual > 0)); then
  echo "ERROR: $residual active directory object(s) remain. Keep state and investigate." >&2
  exit 1
fi

echo "PASS: No active Lab 01 directory objects remain."
if [[ "$purge" != "true" ]]; then
  echo "INFO: The users remain recoverable in Deleted users until retention expires or an authorized permanent purge is performed."
fi
echo "Local audit state remains at $manifest. Remove it only after reviewing cleanup evidence."
