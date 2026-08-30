[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute(
    'PSAvoidUsingWriteHost',
    '',
    Justification = 'Interactive lab status uses host colors; machine-readable output is produced separately by validation.'
)]
param(
    [string] $SubscriptionId,
    [string] $TenantId,
    [ValidatePattern('^[a-z0-9-]+$')]
    [string] $Location = 'westeurope',
    [ValidatePattern('^[a-z0-9-]+$')]
    [string] $SecondaryLocation = 'northeurope'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:Errors = 0
$script:Warnings = 0

function Write-Pass([string] $Message) {
    Write-Host "[PASS] $Message" -ForegroundColor Green
}
function Write-Fail([string] $Message) {
    Write-Host "[FAIL] $Message" -ForegroundColor Red
    $script:Errors++
}
function Write-WarningCheck([string] $Message) {
    Write-Host "[WARN] $Message" -ForegroundColor Yellow
    $script:Warnings++
}

Write-Host 'Lab 00 - Az PowerShell preflight (read only)'
Write-Host '=============================================='

$requiredModules = @('Az.Accounts', 'Az.Resources', 'Az.Compute')
foreach ($moduleName in $requiredModules) {
    $module = Get-Module -ListAvailable -Name $moduleName |
        Sort-Object Version -Descending |
        Select-Object -First 1
    if ($null -eq $module) {
        Write-Fail "$moduleName is not installed."
    }
    else {
        Write-Pass "$moduleName version $($module.Version) is available."
    }
}
if ($script:Errors -gt 0) {
    exit 1
}

$context = Get-AzContext
if ($null -eq $context -or $null -eq $context.Subscription -or $null -eq $context.Tenant) {
    Write-Fail "No active Az PowerShell context. Run Connect-AzAccount interactively, then rerun preflight."
    exit 1
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
if ($SubscriptionId -notmatch $guidPattern) {
    throw 'SubscriptionId must be a subscription GUID.'
}
if ($TenantId -notmatch $guidPattern) {
    throw 'TenantId must be a tenant GUID.'
}

Write-Host ''
Write-Host 'Exact active context (redact identifiers from any retained evidence):'
Write-Host "  Environment:     $($context.Environment.Name)"
Write-Host "  Subscription:    $($context.Subscription.Name)"
Write-Host "  Subscription ID: $currentSubscriptionId"
Write-Host "  Tenant ID:       $currentTenantId"

if ($currentSubscriptionId -eq $SubscriptionId) {
    Write-Pass 'The active subscription matches the requested subscription.'
}
else {
    Write-Fail "Active subscription does not match -SubscriptionId. Review it, then run Set-AzContext yourself if appropriate."
}
if ($currentTenantId -eq $TenantId) {
    Write-Pass 'The active tenant matches the requested tenant.'
}
else {
    Write-Fail 'Active tenant does not match -TenantId. Stop and connect to the intended sandbox tenant.'
}

try {
    $subscription = Get-AzSubscription -SubscriptionId $currentSubscriptionId -TenantId $currentTenantId
    if ([string] $subscription.State -eq 'Enabled') {
        Write-Pass 'Subscription state is Enabled.'
    }
    else {
        Write-Fail "Subscription state is '$($subscription.State)', not Enabled."
    }
}
catch {
    Write-Fail "Subscription state could not be read: $($_.Exception.Message)"
}

$availableLocations = $null
try {
    $availableLocations = @(Get-AzLocation)
}
catch {
    Write-Fail "Azure locations could not be queried: $($_.Exception.Message)"
}
if ($null -ne $availableLocations) {
    foreach ($region in @($Location, $SecondaryLocation)) {
        if ($availableLocations.Location -contains $region) {
            Write-Pass "Region '$region' is listed for this subscription."
        }
        else {
            Write-Fail "Region '$region' was not found for this subscription."
        }
    }
}
if ($Location -eq $SecondaryLocation) {
    Write-WarningCheck 'Primary and secondary regions are identical; later resilience labs need two regions.'
}

Write-Host ''
Write-Host 'Observed provider registration (this script does not register providers):'
$providers = @(
    'Microsoft.Authorization',
    'Microsoft.Compute',
    'Microsoft.Insights',
    'Microsoft.Network',
    'Microsoft.RecoveryServices',
    'Microsoft.Storage'
)
foreach ($provider in $providers) {
    try {
        $providerState = (Get-AzResourceProvider -ProviderNamespace $provider).RegistrationState |
            Select-Object -First 1
        if ($providerState -eq 'Registered') {
            Write-Pass "$provider is Registered."
        }
        elseif ([string]::IsNullOrWhiteSpace([string] $providerState)) {
            Write-WarningCheck "$provider registration state returned no value."
        }
        else {
            Write-WarningCheck "$provider is $providerState. Register it only when a later authorized lab requires it."
        }
    }
    catch {
        Write-WarningCheck "$provider registration state could not be read with the current permissions."
    }
}

try {
    $usage = @(Get-AzVMUsage -Location $Location)
    if ($usage.Count -gt 0) {
        Write-Pass "Regional compute usage/quota returned $($usage.Count) item(s) in '$Location'."
    }
    else {
        Write-WarningCheck "Compute usage/quota returned no items in '$Location'."
    }
}
catch {
    Write-WarningCheck "Compute usage/quota could not be queried in '$Location'; check Reader access and Microsoft.Compute registration."
}

Write-Host ''
Write-Host 'Cost guardrail'
Write-Host "  This lab creates zero Azure resources and has cost class 'none'."
Write-Host '  Later labs may be billable: estimate first, obtain authorization, tag every'
Write-Host '  resource, and tear it down in the same session. Azure budgets alert; they'
Write-Host '  do not stop resources or consumption.'

Write-Host ''
if ($script:Errors -gt 0) {
    Write-Host "Preflight result: FAIL ($($script:Errors) required check(s) failed, $($script:Warnings) warning(s))."
    exit 1
}
if ($script:Warnings -gt 0) {
    Write-Host "Preflight result: PARTIAL ($($script:Warnings) warning(s); review before later labs)."
    exit 2
}
Write-Host 'Preflight result: PASS.'
exit 0
