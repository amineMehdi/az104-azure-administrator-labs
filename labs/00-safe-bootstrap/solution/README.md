# Lab 00 solution and break/fix recovery

Use this only after you have completed the checkpoints. The reference outcome is identical in both lanes:

- the active tenant and subscription match the learner-selected sandbox;
- primary and secondary regions exist and differ;
- provider registration and compute quota are observed, not changed;
- `.state/<run-id>/run.json` records naming, tags, and an empty resource inventory;
- validation returns `pass` or the honest `partial` result when optional provider/quota observations warn; and
- cleanup removes only the selected local run after an explicit execute flag.

There is no “deploy everything” solution script because this lab intentionally creates no Azure resource.

## Break/fix recovery

Before introducing drift, create a backup.

Azure CLI:

```bash
cp ".state/$RUN_ID/run.json" ".state/$RUN_ID/run.json.bak"
jq '.regions.primary = "moonbase-1"' \
  ".state/$RUN_ID/run.json.bak" > ".state/$RUN_ID/run.json"
./scripts/cli/validate.sh --run-id "$RUN_ID"
```

Az PowerShell:

```powershell
$manifest = ".state/$runId/run.json"
Copy-Item $manifest "$manifest.bak"
$state = Get-Content $manifest -Raw | ConvertFrom-Json
$state.regions.primary = 'moonbase-1'
$state | ConvertTo-Json -Depth 8 | Set-Content $manifest -Encoding utf8NoBOM
./scripts/powershell/Validate.ps1 -RunId $runId
```

The correct diagnosis is configuration drift in local run state—not an Azure region outage and not insufficient permission. Restore the manifest, confirm that the files differ only as expected, and validate again.

Azure CLI:

```bash
diff -u ".state/$RUN_ID/run.json" ".state/$RUN_ID/run.json.bak" || true
mv ".state/$RUN_ID/run.json.bak" ".state/$RUN_ID/run.json"
./scripts/cli/validate.sh --run-id "$RUN_ID"
```

Az PowerShell:

```powershell
Compare-Object `
  (Get-Content $manifest) `
  (Get-Content "$manifest.bak")
Move-Item "$manifest.bak" $manifest -Force
./scripts/powershell/Validate.ps1 -RunId $runId
```

Do not “fix” the failure by changing Azure context, registering a provider, or weakening the region check. The recorded intent is the source of truth for validation.

## Why context selection stays manual

`az account set` and `Set-AzContext` change local tool context. That is not an Azure control-plane mutation, but silently selecting a context inside automation can hide the most dangerous mistake in a multi-subscription environment. The scripts therefore fail on mismatch and ask the administrator to review and make the choice explicitly.
