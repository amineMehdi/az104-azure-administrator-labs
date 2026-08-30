# Command cheat sheet

## Azure CLI context

```bash
az account show --output table
az account list --output table
az config get core.login_experience_v2
```

## Az PowerShell context

```powershell
Get-AzContext
Get-AzSubscription
Get-AzTenant
```

## Prefer explicit context

Pass subscription, location, lab ID, and run ID through variables or script parameters. Avoid commands that depend on an unknown current context. Query before mutation and validate after mutation.

This sheet is an index, not a substitute for each lab's explanation and safety checks.
