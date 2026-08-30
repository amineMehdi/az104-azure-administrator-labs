# Lab 01 break/fix solution

Open this only after validation detects the missing membership.

## Diagnose

Read the exact IDs from the run manifest instead of searching by display name:

```bash
GROUP_ID=$(jq -r '.relationships.groupId' ".state/$RUN_ID/run.json")
USER_A_ID=$(jq -r '.relationships.memberUserId' ".state/$RUN_ID/run.json")

az ad group member check \
  --group "$GROUP_ID" \
  --member-id "$USER_A_ID" \
  --output json
```

The returned `value` is `false`. Validation reports `relationship.member=fail`; it should not rewrite membership automatically.

## Repair

Restore only the missing relationship:

```bash
az ad group member add \
  --group "$GROUP_ID" \
  --member-id "$USER_A_ID" \
  --output none

./scripts/cli/validate.sh --run-id "$RUN_ID"
```

Expected result: `relationship.member` returns to `pass`, user B remains an owner but not a direct member, and overall result becomes `pass`.

## Why this repair is safe

- Both IDs came from the lab's state manifest.
- The repair changes one relationship and does not recreate either object.
- It does not search by a non-unique display name.
- It leaves the negative membership control intact.

If any recorded ID resolves to an unexpected object, stop and use cleanup's preview. Never substitute an object found only by display-name prefix.
