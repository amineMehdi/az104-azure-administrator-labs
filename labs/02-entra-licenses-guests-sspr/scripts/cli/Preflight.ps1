
# BEGIN GENERATED AZ104 V2
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZ104_SECONDARY_LOCATION
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Run the repository readiness initializer, then retry.'
}

$account = az account show --output json | ConvertFrom-Json
if (-not $account) { throw 'No active Azure CLI context. Run az login deliberately before this lab.' }
if ($SubscriptionId -and [string]$account.id -ne $SubscriptionId) {
    throw "Context mismatch: active subscription is $($account.id), expected $SubscriptionId. Preflight will not switch it."
}
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
# The account read above is the mandatory context gate. All remaining Azure
# probes are collected as results instead of allowing one unavailable SKU or
# provider query to abort the readiness report before it can explain the gap.
$PSNativeCommandUseErrorActionPreference = $false
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$ResourceGroupName = $(if ('02' -in @('00', '01', '02')) { $null } else { "rg-az104-l02-$RunId" })

$checks = [System.Collections.Generic.List[object]]::new()
function Add-PreflightResult {
    param([string]$Id, [bool]$Required, [bool]$Passed, [string]$Actual)
    $checks.Add([pscustomobject]@{ id = $Id; required = $Required; passed = $Passed; actual = $Actual })
}

Add-PreflightResult -Id 'context' -Required $true -Passed $true -Actual "cloud=$($account.environmentName); tenant=<redacted>; subscription=<redacted>"
$azVersion = (az version --query '"azure-cli"' --output tsv)
$bicepVersion = (az bicep version 2>&1 | Out-String).Trim()
Add-PreflightResult -Id 'azure-cli' -Required $true -Passed ([bool]$azVersion) -Actual $azVersion
Add-PreflightResult -Id 'powershell' -Required $true -Passed ($PSVersionTable.PSVersion -ge [version]'7.4') -Actual $PSVersionTable.PSVersion.ToString()
Add-PreflightResult -Id 'bicep' -Required $true -Passed ([bool]$bicepVersion) -Actual $bicepVersion

$requiredEnvironmentVariables = @()
foreach ($variableName in $requiredEnvironmentVariables) {
    $present = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable($variableName))
    Add-PreflightResult -Id "input:$variableName" -Required $true -Passed $present -Actual $(if ($present) { 'present (value redacted)' } else { 'missing' })
}

$providers = @()
foreach ($provider in $providers) {
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    Add-PreflightResult -Id "provider:$provider" -Required $true -Passed ($registrationState -eq 'Registered') -Actual $(if ($registrationState) { $registrationState } else { 'Unavailable' })
}

$knownLocation = az account list-locations --query "[?name=='$Location'].name | [0]" --output tsv
Add-PreflightResult -Id 'region' -Required $true -Passed ($knownLocation -eq $Location) -Actual $(if ($knownLocation) { $knownLocation } else { 'not available' })

$gatePresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_GUEST_EMAIL'))
Add-PreflightResult -Id 'optional-gate:AZ104_GUEST_EMAIL' -Required $false -Passed $gatePresent -Actual $(if ($gatePresent) { 'present (value redacted)' } else { 'absent; checkpoint will be skipped' })

$gatePresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_LICENSE_SKU_ID'))
Add-PreflightResult -Id 'optional-gate:AZ104_LICENSE_SKU_ID' -Required $false -Passed $gatePresent -Actual $(if ($gatePresent) { 'present (value redacted)' } else { 'absent; checkpoint will be skipped' })

$gatePresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_USAGE_LOCATION'))
Add-PreflightResult -Id 'optional-gate:AZ104_USAGE_LOCATION' -Required $false -Passed $gatePresent -Actual $(if ($gatePresent) { 'present (value redacted)' } else { 'absent; checkpoint will be skipped' })

$gateMatches = [string]::Equals([Environment]::GetEnvironmentVariable('AZ104_ALLOW_SSPR_POLICY_CHANGE'), 'YES', [StringComparison]::Ordinal)
Add-PreflightResult -Id 'optional-gate:AZ104_ALLOW_SSPR_POLICY_CHANGE' -Required $false -Passed $gateMatches -Actual $(if ($gateMatches) { 'exact affirmative value supplied (value redacted)' } else { 'absent or not exact; checkpoint will be skipped' })

$guestEmail = [Environment]::GetEnvironmentVariable('AZ104_GUEST_EMAIL')
$usageLocation = [Environment]::GetEnvironmentVariable('AZ104_USAGE_LOCATION')
$licenseSkuId = [Environment]::GetEnvironmentVariable('AZ104_LICENSE_SKU_ID')
$ssprAuthorization = [Environment]::GetEnvironmentVariable('AZ104_ALLOW_SSPR_POLICY_CHANGE')

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
$policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom,allowedToUseSSPR' --output json | ConvertFrom-Json
$skus = az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus?$select=id,consumedUnits,prepaidUnits' --output json | ConvertFrom-Json
if (-not $policy.id -or $null -eq $skus.value) { throw 'Required Graph policy or SKU inventory is unavailable.' }
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab02.graph-surfaces' -Required $true -Passed $probePassed -Actual $probeActual

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
if ($guestEmail) {
    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom' --output json | ConvertFrom-Json
    if ($policy.allowInvitesFrom -eq 'none') { throw 'Tenant invitation policy disables the requested guest lane.' }
}
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab02.guest-gate' -Required $false -Passed $probePassed -Actual $probeActual

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
if ($guestEmail -or $usageLocation -or $licenseSkuId) {
    if (-not $guestEmail -or -not $licenseSkuId -or $usageLocation -notmatch '^[A-Za-z]{2}$') { throw 'Guest email, exact SKU ID, and two-letter usage location must be supplied together for licensing.' }
    $skus = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus' --output json | ConvertFrom-Json).value
    $selected = @($skus | Where-Object id -eq $licenseSkuId)
    if ($selected.Count -ne 1 -or ($selected[0].prepaidUnits.enabled - $selected[0].consumedUnits) -lt 1) { throw 'The exact license SKU is absent or has no enabled unit available.' }
}
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab02.license-gate' -Required $false -Passed $probePassed -Actual $probeActual

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
if ($ssprAuthorization -eq 'YES') {
    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=id,allowedToUseSSPR' --output json | ConvertFrom-Json
    if (-not $policy.id -or $null -eq $policy.allowedToUseSSPR) { throw 'allowedToUseSSPR cannot be read for recovery.' }
}
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab02.sspr-gate' -Required $false -Passed $probePassed -Actual $probeActual

$checks | Format-Table -AutoSize
$failedRequired = @($checks | Where-Object { $_.required -and -not $_.passed })
if ($failedRequired.Count -gt 0) {
    throw "Preflight blocked: $($failedRequired.id -join ', ')"
}
Write-Host 'Preflight passed. It performed no sign-in, context switch, provider registration, or Azure mutation.'
# END GENERATED AZ104 V2
