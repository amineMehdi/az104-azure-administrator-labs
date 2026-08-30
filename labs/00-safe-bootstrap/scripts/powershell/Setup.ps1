[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute(
    'PSAvoidUsingWriteHost',
    '',
    Justification = 'Interactive lab status uses host output; structured state is written to run.json.'
)]
param(
    [string] $SubscriptionId,
    [string] $TenantId,
    [ValidatePattern('^[a-z0-9-]+$')]
    [string] $Location = 'westeurope',
    [ValidatePattern('^[a-z0-9-]+$')]
    [string] $SecondaryLocation = 'northeurope',
    [string] $RunId,
    [string] $StateRoot = (Join-Path $PSScriptRoot '..\..\.state')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

foreach ($moduleName in @('Az.Accounts', 'Az.Resources')) {
    if ($null -eq (Get-Module -ListAvailable -Name $moduleName | Select-Object -First 1)) {
        throw "$moduleName is required."
    }
}

$context = Get-AzContext
if ($null -eq $context -or $null -eq $context.Subscription -or $null -eq $context.Tenant) {
    throw 'No active Az PowerShell context. Run Connect-AzAccount interactively.'
}

$currentSubscriptionId = [string] $context.Subscription.Id
$currentTenantId = [string] $context.Tenant.Id
if ([string]::IsNullOrWhiteSpace($SubscriptionId)) {
    $SubscriptionId = $currentSubscriptionId
}
if ([string]::IsNullOrWhiteSpace($TenantId)) {
    $TenantId = $currentTenantId
}

$guidPattern = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
if ($SubscriptionId -notmatch $guidPattern -or $TenantId -notmatch $guidPattern) {
    throw 'SubscriptionId and TenantId must be GUIDs.'
}
if ($currentSubscriptionId -ne $SubscriptionId -or $currentTenantId -ne $TenantId) {
    throw 'Active Az context does not match the requested tenant/subscription. Review Get-AzContext, change context yourself, and rerun setup.'
}

$subscription = Get-AzSubscription -SubscriptionId $SubscriptionId -TenantId $TenantId
if ([string] $subscription.State -ne 'Enabled') {
    throw "Subscription state is '$($subscription.State)', not Enabled."
}

$availableLocations = @(Get-AzLocation)
foreach ($region in @($Location, $SecondaryLocation)) {
    if ($availableLocations.Location -notcontains $region) {
        throw "Region '$region' is unavailable to the active subscription."
    }
}
if ($Location -eq $SecondaryLocation) {
    throw 'Primary and secondary regions must differ.'
}

if ([string]::IsNullOrWhiteSpace($RunId)) {
    $randomSuffix = (Get-Random -Minimum 0 -Maximum 10000).ToString('0000')
    $RunId = 'az10400-{0}-{1}' -f [DateTime]::UtcNow.ToString('yyyyMMddHHmmss'), $randomSuffix
}
$runPattern = '^[a-z0-9][a-z0-9-]{2,31}$'
if ($RunId -notmatch $runPattern) {
    throw "RunId must match $runPattern."
}

$stateRootFull = [IO.Path]::GetFullPath($StateRoot)
$null = New-Item -ItemType Directory -Path $stateRootFull -Force
$runDirectory = Join-Path $stateRootFull $RunId
$manifestPath = Join-Path $runDirectory 'run.json'

if (Test-Path -LiteralPath $manifestPath -PathType Leaf) {
    $existing = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    if ([string] $existing.labId -eq '00-safe-bootstrap' -and [string] $existing.runId -eq $RunId) {
        Write-Host "Run '$RunId' is already initialized; existing state was left unchanged."
        Write-Host "State: $manifestPath"
        exit 0
    }
    throw "An incompatible manifest already exists at '$manifestPath'."
}
if (Test-Path -LiteralPath $runDirectory) {
    throw "'$runDirectory' exists without a valid run manifest; refusing to overwrite it."
}

$null = New-Item -ItemType Directory -Path $runDirectory
$token = ($RunId -replace '[^a-z0-9]', '')
if ($token.Length -gt 10) {
    $token = $token.Substring($token.Length - 10)
}
$resourceGroupName = "rg-az104-00-$token"
$globalNameStem = "az10400$token"
if ($globalNameStem.Length -gt 24) {
    $globalNameStem = $globalNameStem.Substring(0, 24)
}
$expiresOn = [DateTime]::UtcNow.AddDays(1).ToString('yyyy-MM-dd')

$state = [ordered]@{
    schemaVersion       = '1.0'
    labId              = '00-safe-bootstrap'
    runId              = $RunId
    createdAt          = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
    context            = [ordered]@{
        cloudName      = [string] $context.Environment.Name
        subscriptionId = $SubscriptionId
        tenantId       = $TenantId
    }
    regions            = [ordered]@{
        primary   = $Location
        secondary = $SecondaryLocation
    }
    naming             = [ordered]@{
        resourceGroup  = $resourceGroupName
        globalNameStem = $globalNameStem
    }
    tags               = [ordered]@{
        purpose   = 'az104-lab'
        labId     = '00-safe-bootstrap'
        runId     = $RunId
        expiresOn = $expiresOn
    }
    observedProviders  = @(
        'Microsoft.Authorization',
        'Microsoft.Compute',
        'Microsoft.Insights',
        'Microsoft.Network',
        'Microsoft.RecoveryServices',
        'Microsoft.Storage'
    )
    resources           = @()
    tenantScopedChanges = @()
    liveAzureMutations  = $false
}

$temporaryPath = Join-Path $runDirectory 'run.json.tmp'
try {
    $json = $state | ConvertTo-Json -Depth 8
    [IO.File]::WriteAllText($temporaryPath, $json, [Text.UTF8Encoding]::new($false))
    Move-Item -LiteralPath $temporaryPath -Destination $manifestPath
}
finally {
    if (Test-Path -LiteralPath $temporaryPath) {
        Remove-Item -LiteralPath $temporaryPath -Force
    }
}

Write-Host 'Local Lab 00 state initialized.'
Write-Host "  Run ID:           $RunId"
Write-Host "  Primary region:   $Location"
Write-Host "  Secondary region: $SecondaryLocation"
Write-Host "  Name example:     $resourceGroupName"
Write-Host "  State:            $manifestPath"
Write-Host 'No Azure resources or settings were changed.'
