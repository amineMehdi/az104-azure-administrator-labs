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
$ResourceGroupName = "rg-az104-l02-$RunId"
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-02 plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  scope: tenant'
Write-Host '  cost class: none'
Write-Host '  resources: security group, invited guest user, optional license assignment, optional SSPR scope'
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
    labId = 'LAB-02'
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=02 runId=$RunId expiresOn=$expiresOn --output none
    $state.resourceGroup.name = $ResourceGroupName
    $state.resourceGroup.id = az group show --subscription $SubscriptionId --name $ResourceGroupName --query id --output tsv
    $state.status = 'baseline-created'
    $state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
}

$group = az ad group create --display-name "AZ104-L02-$RunId-SSPR-Pilot" --mail-nickname "az104l02$suffix" --output json | ConvertFrom-Json
$state.external['groupId'] = [string]$group.id
if ($env:AZ104_GUEST_EMAIL) {
    $inviteBody = @{ invitedUserEmailAddress = $env:AZ104_GUEST_EMAIL; inviteRedirectUrl = 'https://myapps.microsoft.com'; sendInvitationMessage = $false } | ConvertTo-Json -Compress
    $invitation = az rest --method post --url 'https://graph.microsoft.com/v1.0/invitations' --body $inviteBody --output json | ConvertFrom-Json
    $state.external['guestUserId'] = [string]$invitation.invitedUser.id
}
if ($env:AZ104_LICENSE_SKU_ID -and $state.external.guestUserId) {
    $licenseBody = @{ addLicenses = @(@{ skuId = $env:AZ104_LICENSE_SKU_ID }); removeLicenses = @() } | ConvertTo-Json -Depth 6 -Compress
    az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($state.external.guestUserId)/assignLicense" --body $licenseBody --output none
    $state.external['licenseSkuId'] = $env:AZ104_LICENSE_SKU_ID
}
if ($env:AZ104_ALLOW_SSPR_POLICY_CHANGE -eq 'YES') {
    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --output json | ConvertFrom-Json
    $state.external['originalAllowedToUseSspr'] = [bool]$policy.allowedToUseSspr
    az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --body '{"allowedToUseSspr":true}' --output none
    $state.external['ssprChanged'] = $true
}

if ('tenant' -eq 'subscription') {
    $state.resources = @(az resource list --subscription $SubscriptionId --resource-group $ResourceGroupName --output json | ConvertFrom-Json | ForEach-Object {
        [ordered]@{ id = $_.id; name = $_.name; type = $_.type; location = $_.location }
    })
}
$state.status = 'setup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
