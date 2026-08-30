# Lab 00 offline test contract

These checks validate repository content without signing in to Azure. Live query results and Portal screenshots require separate authorization and are not part of offline acceptance.

## Static checks

Run from the lab root.

Run the Pester safety contract first:

```powershell
Invoke-Pester tests/Contract.Tests.ps1 -Output Detailed
```

The contract checks that both command lanes contain the complete lifecycle, never sign in or change context, contain no Azure resource mutations, and require explicit confirmation before local cleanup.

### Bash syntax

```bash
bash -n scripts/cli/preflight.sh
bash -n scripts/cli/setup.sh
bash -n scripts/cli/validate.sh
bash -n scripts/cli/cleanup.sh
```

Then run ShellCheck when available:

```bash
shellcheck scripts/cli/*.sh
```

### PowerShell parse and analysis

```powershell
$parseFailed = $false
Get-ChildItem scripts/powershell/*.ps1 | ForEach-Object {
  $tokens = $null
  $errors = $null
  [void][Management.Automation.Language.Parser]::ParseFile(
    $_.FullName,
    [ref]$tokens,
    [ref]$errors
  )
  if ($errors.Count) {
    $parseFailed = $true
    $errors | ForEach-Object { Write-Error $_ }
  }
}
if ($parseFailed) { throw 'PowerShell parse checks failed.' }

Invoke-ScriptAnalyzer scripts/powershell -Recurse -Severity Warning,Error
```

### Safety assertions

Review command matches rather than blindly treating all text hits as failures:

```bash
# Runtime scripts must not contain Azure create/update/delete/register commands.
rg -n 'az (group|resource|provider|role|policy|lock).*\b(create|delete|register|update)\b' scripts
rg -n '(New|Set|Remove|Register|Unregister)-Az' scripts

# Runtime imports must remain inside this lab.
rg -n '(source|\. ) .*\.\./\.\./\.\.' scripts
```

Expected results: no Azure mutation command and no cross-lab runtime import. Documentation may mention prohibited commands to explain why they are not run.

## Local behavior checks

These require a signed-in sandbox only because setup verifies context and region availability. They still create no Azure resource.

| Scenario | Expected result |
|---|---|
| Missing Azure sign-in | Preflight/setup fail without starting an interactive login. |
| Tenant or subscription mismatch | Required check fails; active context is unchanged. |
| Same primary/secondary region | Preflight returns `2` with a warning. |
| New valid run ID | One run directory and `run.json` are created. |
| Repeat setup with same run ID | Existing manifest remains unchanged. |
| Valid run | `validation.json` contains checks and result `pass` or honest `partial`. |
| Drifted primary region | Validation returns `1` with `azure.primary-region=fail`. |
| Cleanup without execute flag | Deletion plan is printed; state remains. |
| Cleanup with unexpected resources in state | Cleanup refuses. |
| Cleanup with execute flag | Only the selected run directory is removed. |
| Repeated cleanup | Reports nothing remains and returns success. |

## Acceptance boundary

Offline validation proves syntax, documentation, metadata, and safety design. It does not prove Azure permissions, current provider state, quota availability, Portal layout, or live cleanup. Keep `lastLiveVerified: null` and screenshot status `pending` until those checks are performed in an explicitly authorized sandbox.
