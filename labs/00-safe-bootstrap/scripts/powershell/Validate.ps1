[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute(
    'PSAvoidUsingWriteHost',
    '',
    Justification = 'Interactive check status uses host colors; validation.json is the pipeline-safe result.'
)]
param(
    [Parameter(Mandatory)]
    [string] $RunId,
    [string] $StateRoot = (Join-Path $PSScriptRoot '..\..\.state')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$runPattern = '^[a-z0-9][a-z0-9-]{2,31}$'
if ($RunId -notmatch $runPattern) {
    throw "RunId must match $runPattern."
}

$stateRootFull = [IO.Path]::GetFullPath($StateRoot)
$runDirectory = Join-Path $stateRootFull $RunId
$manifestPath = Join-Path $runDirectory 'run.json'
$reportPath = Join-Path $runDirectory 'validation.json'
if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
    throw "Valid run state was not found at '$runDirectory'."
}

$state = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
$checks = [Collections.Generic.List[object]]::new()

function Add-Check {
    param(
        [Parameter(Mandatory)][string] $Id,
        [Parameter(Mandatory)][ValidateSet('pass', 'fail', 'warning', 'skipped')][string] $Status,
        [Parameter(Mandatory)][string] $Message
    )
    $checks.Add([pscustomobject][ordered]@{ id = $Id; status = $Status; message = $Message })
    $color = switch ($Status) {
        'pass' { 'Green' }
        'fail' { 'Red' }
        default { 'Yellow' }
    }
    Write-Host "[$($Status.ToUpperInvariant())] $Message" -ForegroundColor $color
}

Write-Host 'Lab 00 - Az PowerShell validation (Azure reads only)'
Write-Host '====================================================='

if ([string] $state.labId -eq '00-safe-bootstrap' -and [string] $state.runId -eq $RunId) {
    Add-Check -Id 'state.identity' -Status pass -Message "Run manifest belongs to Lab 00 and run '$RunId'."
}
else {
    Add-Check -Id 'state.identity' -Status fail -Message 'Run manifest identity does not match the selected Lab 00 run.'
}

$requiredTagValues = @($state.tags.purpose, $state.tags.labId, $state.tags.runId, $state.tags.expiresOn)
$presentTagCount = @($requiredTagValues | Where-Object {
        -not [string]::IsNullOrWhiteSpace(([string] $_))
    }).Count
if ($presentTagCount -eq 4 -and [string] $state.tags.runId -eq $RunId) {
    Add-Check -Id 'state.tags' -Status pass -Message 'Required purpose, labId, runId, and expiresOn tags are prepared.'
}
else {
    Add-Check -Id 'state.tags' -Status fail -Message 'Required tag metadata is missing or inconsistent.'
}

$resourceCount = @($state.resources).Count
$tenantChangeCount = @($state.tenantScopedChanges).Count
$hasExactFalseMutationFlag = $state.liveAzureMutations -is [bool] -and $state.liveAzureMutations -eq $false
if ($resourceCount -eq 0 -and $tenantChangeCount -eq 0 -and $hasExactFalseMutationFlag) {
    Add-Check -Id 'state.safety-boundary' -Status pass -Message 'State records no Azure resources, tenant changes, or live mutations.'
}
else {
    Add-Check -Id 'state.safety-boundary' -Status fail -Message 'Unexpected Azure resources or shared-setting changes are recorded; stop and review.'
}

$context = $null
try {
    $context = Get-AzContext
}
catch {
    Add-Check -Id 'azure.session' -Status fail -Message "Az context could not be read: $($_.Exception.Message)"
}
if ($null -eq $context -or $null -eq $context.Subscription -or $null -eq $context.Tenant) {
    Add-Check -Id 'azure.session' -Status fail -Message 'No active Az PowerShell context is available.'
}
else {
    try {
        $subscription = Get-AzSubscription -SubscriptionId $context.Subscription.Id -TenantId $context.Tenant.Id
        if ([string] $subscription.State -eq 'Enabled') {
            Add-Check -Id 'azure.session' -Status pass -Message 'Az PowerShell context is active and the subscription state is Enabled.'
        }
        else {
            Add-Check -Id 'azure.session' -Status fail -Message "Active subscription state is '$($subscription.State)', not Enabled."
        }
    }
    catch {
        Add-Check -Id 'azure.session' -Status fail -Message "Subscription state could not be read: $($_.Exception.Message)"
    }
}

$expectedSubscriptionId = [string] $state.context.subscriptionId
$expectedTenantId = [string] $state.context.tenantId
if ($null -ne $context -and [string] $context.Subscription.Id -eq $expectedSubscriptionId) {
    Add-Check -Id 'azure.subscription-context' -Status pass -Message 'Active subscription matches the run manifest.'
}
else {
    Add-Check -Id 'azure.subscription-context' -Status fail -Message 'Active subscription does not match the run manifest.'
}
if ($null -ne $context -and [string] $context.Tenant.Id -eq $expectedTenantId) {
    Add-Check -Id 'azure.tenant-context' -Status pass -Message 'Active tenant matches the run manifest.'
}
else {
    Add-Check -Id 'azure.tenant-context' -Status fail -Message 'Active tenant does not match the run manifest.'
}

$primaryRegion = [string] $state.regions.primary
$secondaryRegion = [string] $state.regions.secondary
try {
    $locations = @(Get-AzLocation)
    if ($locations.Location -contains $primaryRegion) {
        Add-Check -Id 'azure.primary-region' -Status pass -Message "Primary region '$primaryRegion' is available to the subscription."
    }
    else {
        Add-Check -Id 'azure.primary-region' -Status fail -Message "Primary region '$primaryRegion' is not listed for the subscription."
    }
    if ($locations.Location -contains $secondaryRegion) {
        Add-Check -Id 'azure.secondary-region' -Status pass -Message "Secondary region '$secondaryRegion' is available to the subscription."
    }
    else {
        Add-Check -Id 'azure.secondary-region' -Status fail -Message "Secondary region '$secondaryRegion' is not listed for the subscription."
    }
}
catch {
    Add-Check -Id 'azure.primary-region' -Status fail -Message "Primary region could not be queried: $($_.Exception.Message)"
    Add-Check -Id 'azure.secondary-region' -Status fail -Message "Secondary region could not be queried: $($_.Exception.Message)"
}
if (-not [string]::IsNullOrWhiteSpace($primaryRegion) -and
    -not [string]::IsNullOrWhiteSpace($secondaryRegion) -and
    $primaryRegion -ne $secondaryRegion) {
    Add-Check -Id 'azure.region-separation' -Status pass -Message 'Primary and secondary regions are distinct.'
}
else {
    Add-Check -Id 'azure.region-separation' -Status fail -Message 'Primary and secondary regions must be distinct.'
}

foreach ($provider in @($state.observedProviders)) {
    try {
        $providerState = (Get-AzResourceProvider -ProviderNamespace ([string] $provider)).RegistrationState |
            Select-Object -First 1
        if ($providerState -eq 'Registered') {
            Add-Check -Id "azure.provider.$provider" -Status pass -Message "$provider is Registered."
        }
        elseif ([string]::IsNullOrWhiteSpace([string] $providerState)) {
            Add-Check -Id "azure.provider.$provider" -Status warning -Message "$provider registration state returned no value."
        }
        else {
            Add-Check -Id "azure.provider.$provider" -Status warning -Message "$provider is $providerState; no registration was attempted."
        }
    }
    catch {
        Add-Check -Id "azure.provider.$provider" -Status warning -Message "$provider registration state could not be read."
    }
}

try {
    $usage = @(Get-AzVMUsage -Location $primaryRegion)
    if ($usage.Count -gt 0) {
        Add-Check -Id 'azure.compute-quota' -Status pass -Message "Compute usage/quota returned $($usage.Count) item(s) for '$primaryRegion'."
    }
    else {
        Add-Check -Id 'azure.compute-quota' -Status warning -Message 'Compute usage/quota returned no items; no quota change was attempted.'
    }
}
catch {
    Add-Check -Id 'azure.compute-quota' -Status warning -Message 'Compute usage/quota could not be read; no quota change was attempted.'
}

$failureCount = @($checks | Where-Object status -eq 'fail').Count
$warningCount = @($checks | Where-Object { $_.status -in @('warning', 'skipped') }).Count
if ($failureCount -gt 0) {
    $result = 'fail'
    $exitCode = 1
}
elseif ($warningCount -gt 0) {
    $result = 'partial'
    $exitCode = 2
}
else {
    $result = 'pass'
    $exitCode = 0
}

$moduleVersions = [ordered]@{}
foreach ($moduleName in @('Az.Accounts', 'Az.Resources', 'Az.Compute')) {
    $module = Get-Module -ListAvailable -Name $moduleName | Sort-Object Version -Descending | Select-Object -First 1
    $moduleVersions[$moduleName] = if ($null -eq $module) { $null } else { [string] $module.Version }
}
$report = [ordered]@{
    schemaVersion = '1.0'
    labId         = 'LAB-00'
    runId         = $RunId
    generatedAt   = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
    result        = $result
    toolLane      = 'az-powershell'
    toolVersions  = $moduleVersions
    targetContext = [ordered]@{
        subscriptionId = $expectedSubscriptionId
        tenantId       = $expectedTenantId
    }
    checks         = @($checks)
}

$temporaryPath = Join-Path $runDirectory 'validation.json.tmp'
try {
    $json = $report | ConvertTo-Json -Depth 8
    [IO.File]::WriteAllText($temporaryPath, $json, [Text.UTF8Encoding]::new($false))
    Move-Item -LiteralPath $temporaryPath -Destination $reportPath -Force
}
finally {
    if (Test-Path -LiteralPath $temporaryPath) {
        Remove-Item -LiteralPath $temporaryPath -Force
    }
}

Write-Host ''
Write-Host "Validation result: $result"
Write-Host "Machine-readable report: $reportPath"
exit $exitCode
