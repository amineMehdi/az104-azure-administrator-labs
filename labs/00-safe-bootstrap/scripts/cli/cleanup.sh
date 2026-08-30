#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
LAB_ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd -P)"

usage() {
  cat <<'EOF'
Preview or remove one Lab 00 local state directory.

Usage:
  ./cleanup.sh --run-id ID [--state-root PATH] [--execute]

Without --execute, cleanup is report-only. Lab 00 never deletes Azure resources.
If state records any Azure resource or tenant-scoped change, cleanup refuses.
EOF
}

run_id=""
state_root="$LAB_ROOT/.state"
execute=false
while (( $# > 0 )); do
  case "$1" in
    --run-id) [[ $# -ge 2 ]] || exit 1; run_id="$2"; shift 2 ;;
    --state-root) [[ $# -ge 2 ]] || exit 1; state_root="$2"; shift 2 ;;
    --execute) execute=true; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: unknown argument '$1'." >&2; usage >&2; exit 1 ;;
  esac
done

run_pattern='^[a-z0-9][a-z0-9-]{2,31}$'
[[ "$run_id" =~ $run_pattern ]] || { echo "ERROR: --run-id is required and must match $run_pattern." >&2; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "ERROR: jq 1.6 or later is required." >&2; exit 1; }

if [[ ! -d "$state_root" ]]; then
  echo "Nothing to clean: state root does not exist."
  exit 0
fi
state_root="$(cd -- "$state_root" && pwd -P)"
run_dir="$state_root/$run_id"

if [[ ! -e "$run_dir" ]]; then
  echo "Nothing to clean for run '$run_id'."
  exit 0
fi
if [[ -L "$run_dir" || ! -d "$run_dir" ]]; then
  echo "ERROR: selected run path is not a regular directory; refusing cleanup." >&2
  exit 1
fi
run_dir_resolved="$(cd -- "$run_dir" && pwd -P)"
case "$run_dir_resolved" in
  "$state_root"/*) ;;
  *) echo "ERROR: resolved run path escapes the selected state root." >&2; exit 1 ;;
esac
[[ "$run_dir_resolved" != "$state_root" ]] || { echo "ERROR: refusing to remove the state root itself." >&2; exit 1; }

manifest="$run_dir_resolved/run.json"
[[ -f "$manifest" ]] || { echo "ERROR: run.json is missing; refusing cleanup." >&2; exit 1; }
jq empty "$manifest" 2>/dev/null || { echo "ERROR: run.json is invalid; refusing cleanup." >&2; exit 1; }

state_lab_id="$(jq -r '.labId // empty' "$manifest")"
state_run_id="$(jq -r '.runId // empty' "$manifest")"
resource_count="$(jq '.resources | if type == "array" then length else -1 end' "$manifest")"
tenant_change_count="$(jq '.tenantScopedChanges | if type == "array" then length else -1 end' "$manifest")"
live_mutations="$(jq -r '.liveAzureMutations // empty' "$manifest")"

if [[ "$state_lab_id" != "00-safe-bootstrap" || "$state_run_id" != "$run_id" ]]; then
  echo "ERROR: manifest identity does not match the selected run." >&2
  exit 1
fi
if [[ "$resource_count" != "0" || "$tenant_change_count" != "0" || "$live_mutations" != "false" ]]; then
  echo "ERROR: state records Azure resources or shared-setting changes." >&2
  echo "Lab 00 cleanup never deletes Azure objects. Stop and review the manifest manually." >&2
  exit 1
fi

echo "Cleanup plan"
echo "  Azure deletions:       none"
echo "  Tenant restorations:   none"
echo "  Local directory:       $run_dir_resolved"
echo "  Local files to remove: $(find "$run_dir_resolved" -type f | wc -l | tr -d ' ')"

if [[ "$execute" != "true" ]]; then
  echo "Preview only. Rerun with --execute to remove exactly this local run directory."
  exit 0
fi

rm -rf -- "$run_dir_resolved"
if [[ -e "$run_dir_resolved" ]]; then
  echo "ERROR: local run directory still exists after cleanup." >&2
  exit 1
fi
echo "Removed local state for run '$run_id'. No Azure changes were made."
