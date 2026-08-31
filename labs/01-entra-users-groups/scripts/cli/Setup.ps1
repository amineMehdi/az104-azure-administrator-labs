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
$ResourceGroupName = "rg-az104-l01-$RunId"
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-01 plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  scope: tenant'
Write-Host '  cost class: none'
Write-Host '  resources: Two cloud-only member users, One security group, One group membership, One group owner assignment'
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
    labId = 'LAB-01'
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

if ('tenant' -eq 'subscription') {
    $expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd')
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=01 runId=$RunId expiresOn=$expiresOn --output none
    $state.resourceGroup.name = $ResourceGroupName
    $state.resourceGroup.id = az group show --subscription $SubscriptionId --name $ResourceGroupName --query id --output tsv
    $state.status = 'baseline-created'
    $state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
}

if (-not $env:AZ104_LAB_INITIAL_PASSWORD -or $env:AZ104_LAB_INITIAL_PASSWORD.Length -lt 12) {
    throw 'Set AZ104_LAB_INITIAL_PASSWORD to a policy-compliant temporary password of at least 12 characters.'
}

if (-not $env:AZ104_TENANT_DOMAIN) { throw 'Set AZ104_TENANT_DOMAIN to a verified tenant domain.' }
$domain = $env:AZ104_TENANT_DOMAIN
$aliases = @("az104l01a$suffix", "az104l01b$suffix")
$displayNames = @("AZ104-L01-$RunId-Alex", "AZ104-L01-$RunId-Blair")
$userIds = @()
for ($index = 0; $index -lt 2; $index++) {
    $upn = "$($aliases[$index])@$domain"
    $secretPath = Join-Path $StateDir ".user-$index.json"
    $body = [ordered]@{
        accountEnabled = $true
        displayName = $displayNames[$index]
        mailNickname = $aliases[$index]
        userPrincipalName = $upn
        passwordProfile = [ordered]@{ forceChangePasswordNextSignIn = $true; password = $env:AZ104_LAB_INITIAL_PASSWORD }
    }
    try {
        $body | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $secretPath -Encoding utf8
        $created = az rest --method post --url 'https://graph.microsoft.com/v1.0/users' --body "@$secretPath" --output json | ConvertFrom-Json
    }
    finally {
        Remove-Item -LiteralPath $secretPath -Force -ErrorAction SilentlyContinue
    }
    $userIds += [string]$created.id
}
$group = az ad group create --display-name "AZ104-L01-$RunId-Operators" --mail-nickname "az104l01g$suffix" --output json | ConvertFrom-Json
az ad group member add --group $group.id --member-id $userIds[0] --output none
az ad group owner add --group $group.id --owner-object-id $userIds[1] --output none
$state.external['userIds'] = @($userIds)
$state.external['groupId'] = [string]$group.id
Remove-Item Env:AZ104_LAB_INITIAL_PASSWORD -ErrorAction SilentlyContinue

if ('tenant' -eq 'subscription') {
    $state.resources = @(az resource list --subscription $SubscriptionId --resource-group $ResourceGroupName --output json | ConvertFrom-Json | ForEach-Object {
        [ordered]@{ id = $_.id; name = $_.name; type = $_.type; location = $_.location }
    })
}
$state.status = 'setup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
