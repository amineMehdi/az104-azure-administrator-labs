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
$ResourceGroupName = "rg-az104-l11-$RunId"
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-11 plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  scope: subscription'
Write-Host '  cost class: moderate'
Write-Host '  resources: resource group, virtual network, network security group, network interface, Linux virtual machine, managed data disk'
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
    labId = 'LAB-11'
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=11 runId=$RunId expiresOn=$expiresOn --output none
    $state.resourceGroup.name = $ResourceGroupName
    $state.resourceGroup.id = az group show --subscription $SubscriptionId --name $ResourceGroupName --query id --output tsv
    $state.status = 'baseline-created'
    $state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
}

$vnet = "vnet-$suffix"; $vm = "vm-$suffix"; $disk = "disk-$suffix"
$keyPath = Join-Path $StateDir 'id_ed25519'
ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.11.0.0/16 --subnet-name workload --subnet-prefixes 10.11.1.0/24 --output none
az vm create --resource-group $ResourceGroupName --name $vm --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --vnet-name $vnet --subnet workload --public-ip-address '""' --nsg-rule NONE --output none
az disk create --resource-group $ResourceGroupName --name $disk --size-gb 8 --sku Standard_LRS --output none
az vm disk attach --resource-group $ResourceGroupName --vm-name $vm --name $disk --caching ReadWrite --output none

if ('subscription' -eq 'subscription') {
    $state.resources = @(az resource list --subscription $SubscriptionId --resource-group $ResourceGroupName --output json | ConvertFrom-Json | ForEach-Object {
        [ordered]@{ id = $_.id; name = $_.name; type = $_.type; location = $_.location }
    })
}
$state.status = 'setup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
