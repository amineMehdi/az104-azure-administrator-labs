#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lanes keep a consistent explicit context and region interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Named checkpoint results improve readability even when the object is used only to enforce failure handling.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'The disposable generated VMSS credential remains in memory and is never persisted.')]
param(
    [string]$SubscriptionId = '',
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [Parameter(Mandatory)][string]$Location,
    [string]$SecondaryLocation = $env:AZURE_SECONDARY_LOCATION,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$ResourceGroupName = 'rg-az104-l02-' + $RunId
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'

Write-Host 'LAB-02 plan'
Write-Host '  subscription:' $(if ($SubscriptionId) { $SubscriptionId } else { 'tenant-scoped / not applicable' })
Write-Host '  location:' $Location
Write-Host '  resource group:' $(if ($false) { $ResourceGroupName } else { 'none (tenant objects)' })
Write-Host '  cost class: none'
Write-Host '  external gate: Requires a real disposable guest email for invitation, an available SKU for license assignment, and an authorized tenant policy change for SSPR.'
Write-Host '  resources: security group, invited guest user, optional license assignment, optional SSPR scope'
if (-not $Execute) {
    Write-Host 'Preview only. Re-run with -Execute after approving context, permissions, cost, and gates.'
    return
}

& (Join-Path $PSScriptRoot 'Preflight.ps1') -Location $Location
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest; choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$graphContext = Get-MgContext
$TenantId = $graphContext.TenantId
$state = [ordered]@{
    labId = 'LAB-02'
    runId = $RunId
    tenantId = $TenantId
    subscriptionId = $SubscriptionId
    location = $Location
    createdAt = (Get-Date).ToUniversalTime().ToString('o')
    status = 'recorded-before-mutation'
    resourceGroup = [ordered]@{ name = $(if ($false) { $ResourceGroupName } else { $null }); id = $null }
    resources = @()
    external = [ordered]@{}
}
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8


$displayName = "AZ104-L02-$RunId-SSPR-Pilot"
$group = New-MgGroup -DisplayName $displayName -MailEnabled:$false -MailNickname ("az104l02" + $suffix) -SecurityEnabled
$state.external.groupId = $group.Id
if ($env:AZ104_GUEST_EMAIL) {
    $invitation = New-MgInvitation -InvitedUserEmailAddress $env:AZ104_GUEST_EMAIL -InviteRedirectUrl 'https://myapps.microsoft.com' -SendInvitationMessage:$false
    $state.external.guestUserId = $invitation.InvitedUser.Id
}
if ($env:AZ104_LICENSE_SKU_ID -and $state.external.guestUserId) {
    Set-MgUserLicense -UserId $state.external.guestUserId -AddLicenses @(@{SkuId = [Guid]$env:AZ104_LICENSE_SKU_ID}) -RemoveLicenses @()
    $state.external.licenseSkuId = $env:AZ104_LICENSE_SKU_ID
}
if ($env:AZ104_ALLOW_SSPR_POLICY_CHANGE -eq 'YES') {
    $policy = Get-MgPolicyAuthorizationPolicy
    $state.external.originalAllowedToUseSspr = $policy.AllowedToUseSspr
    Update-MgPolicyAuthorizationPolicy -AllowedToUseSspr:$true
    $state.external.ssprChanged = $true
}

$state.status = 'setup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
