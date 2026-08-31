#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Lifecycle scripts keep one consistent interface across all labs.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Shared safe-naming variables are retained for a consistent learner path.')]
param(
    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId
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
$Report = Join-Path $StateDir 'validation.json'
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Missing state: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
if ($account.id -ne $SubscriptionId -or $state.subscriptionId -ne $SubscriptionId) { throw 'Active or recorded subscription mismatch.' }

$checks = [System.Collections.Generic.List[object]]::new()
function Add-Check([string]$Id, [ValidateSet('pass','fail','warning','skipped')][string]$Status, [string]$Message) {
    $checks.Add([ordered]@{ id = $Id; status = $Status; message = $Message })
}

if ('subscription' -eq 'local') {
    Add-Check state.local pass 'The manifest records a local-only bootstrap run.'
} elseif ('subscription' -eq 'tenant') {

} else {
    $resourceGroup = az group show --subscription $SubscriptionId --name $state.resourceGroup.name --output json 2>$null | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0 -or -not $resourceGroup) {
        Add-Check context.resource-group fail 'The exact recorded resource group is absent.'
    } elseif ($resourceGroup.id -ne $state.resourceGroup.id) {
        Add-Check context.resource-group fail 'The resource-group ID differs from the manifest.'
    } else {
        Add-Check context.resource-group pass 'The exact recorded resource group exists.'
    }
    if ($resourceGroup.tags.purpose -eq 'az104-lab' -and $resourceGroup.tags.labId -eq '10' -and $resourceGroup.tags.runId -eq $RunId) {
        Add-Check ownership.tags pass 'purpose, labId, and runId tags match.'
    } else { Add-Check ownership.tags fail 'Ownership tags do not match.' }
    $resources = @(az resource list --subscription $SubscriptionId --resource-group $state.resourceGroup.name --output json | ConvertFrom-Json)
    $expectedTypes = @(

    )
    if ($expectedTypes.Count -eq 0) {
        Add-Check resources.boundary pass "The recorded boundary contains $($resources.Count) top-level resource(s)."
    }
    foreach ($type in $expectedTypes) {
        $count = @($resources | Where-Object type -EQ $type).Count
        if ($count -gt 0) { Add-Check ("resource." + ($type -replace '[/\.]','-')) pass "Found $count resource(s) of type $type." }
        else { Add-Check ("resource." + ($type -replace '[/\.]','-')) warning "No top-level $type was returned; inspect nested or gated state." }
    }
}

$failures = @($checks | Where-Object status -EQ fail).Count
$warnings = @($checks | Where-Object status -IN @('warning', 'skipped')).Count
$result = if ($failures -gt 0) { 'fail' } elseif ($warnings -gt 0) { 'partial' } else { 'pass' }
$output = [ordered]@{ labId = 'LAB-10'; runId = $RunId; generatedAt = (Get-Date).ToUniversalTime().ToString('o'); result = $result; checks = @($checks) }
$output | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Report -Encoding utf8
$output | ConvertTo-Json -Depth 20
if ($result -eq 'fail') { exit 1 }
