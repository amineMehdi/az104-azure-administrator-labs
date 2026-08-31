#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Lifecycle scripts keep one consistent interface across all labs.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Shared safe-naming variables are retained for a consistent learner path.')]
param(
    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZURE_SECONDARY_LOCATION,
    [switch]$Execute
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Install it, run az login deliberately, and retry.'
}

$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$ResourceGroupName = "rg-az104-l16-$RunId"
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-16 plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  scope: subscription'
Write-Host '  cost class: moderate'
Write-Host '  resources: resource group, App Service plan, web app, storage account, virtual network integration subnet, optional custom hostname and TLS binding'
if (-not $Execute) {
    Write-Host 'Preview only. Re-run with -Execute after approving context, permissions, cost, and gates.'
    return
}

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -Location $Location
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest; choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
$state = [ordered]@{
    labId = 'LAB-16'
    runId = $RunId
    tenantId = [string]$account.tenantId
    subscriptionId = $SubscriptionId
    location = $Location
    createdAt = (Get-Date).ToUniversalTime().ToString('o')
    status = 'recorded-before-mutation'
    resourceGroup = [ordered]@{ name = $null; id = $null }
    resources = @()
    external = [ordered]@{}
}
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8

if ('subscription' -eq 'subscription') {
    $expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd')
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=16 runId=$RunId expiresOn=$expiresOn --output none
    $state.resourceGroup.name = $ResourceGroupName
    $state.resourceGroup.id = az group show --subscription $SubscriptionId --name $ResourceGroupName --query id --output tsv
    $state.status = 'baseline-created'
    $state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
}

$plan = "plan-$suffix"; $app = "app-$suffix"; $storage = "st16$suffix"; $vnet = "vnet-$suffix"
az appservice plan create --resource-group $ResourceGroupName --name $plan --is-linux --sku B1 --output none
az webapp create --resource-group $ResourceGroupName --plan $plan --name $app --runtime 'PYTHON:3.12' --output none
az webapp update --resource-group $ResourceGroupName --name $app --https-only true --set siteConfig.minTlsVersion=1.2 --output none
az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.16.0.0/16 --subnet-name integration --subnet-prefixes 10.16.1.0/24 --output none
az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name integration --delegations Microsoft.Web/serverFarms --output none
az webapp vnet-integration add --resource-group $ResourceGroupName --name $app --vnet $vnet --subnet integration --output none

if ('subscription' -eq 'subscription') {
    $state.resources = @(az resource list --subscription $SubscriptionId --resource-group $ResourceGroupName --output json | ConvertFrom-Json | ForEach-Object {
        [ordered]@{ id = $_.id; name = $_.name; type = $_.type; location = $_.location }
    })
}
$state.status = 'setup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
