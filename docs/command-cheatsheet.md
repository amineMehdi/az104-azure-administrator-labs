# Azure CLI command cheatsheet

Run every command from PowerShell 7.4 or later. Azure CLI is the only Azure
administration surface used by the labs.

## Confirm context

```powershell
az account show --output table
az account list --output table
az account show --query '{subscription:id,tenant:tenantId,user:user.name}' --output json
```

The lab scripts never run `az login` or switch subscriptions. Sign in and select
the intended sandbox context deliberately before preflight.

## Inspect resources

```powershell
az group show --name '<resource-group>' --output json
az resource list --resource-group '<resource-group>' --output table
az resource show --ids '<resource-id>' --output json
```

## Microsoft Entra and Graph

```powershell
az ad user show --id '<user-object-id>' --output json
az ad group show --group '<group-object-id>' --output json
az rest --method get --url 'https://graph.microsoft.com/v1.0/organization' --output json
```

## Preview and cleanup

```powershell
pwsh ./scripts/cli/Setup.ps1 -SubscriptionId '<subscription-id>' -Location '<region>' -RunId '<run-id>'
pwsh ./scripts/cli/Cleanup.ps1 -SubscriptionId '<subscription-id>' -RunId '<run-id>'
```

Add `-Execute` only after reviewing the exact context and targets printed by the
preview. Cleanup is scoped to IDs recorded in `.state/<run-id>/run.json`.
