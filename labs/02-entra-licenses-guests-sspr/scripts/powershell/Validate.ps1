#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Tenant and subscription lanes share a consistent validation interface.')]
param(
    [string]$SubscriptionId = '',
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId
)

$ErrorActionPreference = 'Stop'
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$Report = Join-Path $StateDir 'validation.json'
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Missing state: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
$checks = [System.Collections.Generic.List[object]]::new()
function Add-Check([string]$Id, [string]$Status, [string]$Message) {
    $checks.Add([ordered]@{ id = $Id; status = $Status; message = $Message })
}

$graphContext = Get-MgContext
if (-not $graphContext) { throw 'No Microsoft Graph context is active.' }
if ($graphContext.TenantId -ne $state.tenantId) { throw 'Recorded tenant does not match the active Graph context.' }
$groupId = $state.external.groupId
if ($groupId) {
    $group = Get-MgGroup -GroupId $groupId -ErrorAction SilentlyContinue
    if ($group) { Add-Check 'entra.group' 'pass' 'The exact recorded pilot group exists.' }
    else { Add-Check 'entra.group' 'fail' 'The recorded pilot group is absent.' }
} else { Add-Check 'entra.group' 'warning' 'No group ID was recorded; setup did not reach the tenant mutation.' }
if ($state.external.guestUserId) {
    $guest = Get-MgUser -UserId $state.external.guestUserId -ErrorAction SilentlyContinue
    if ($guest) { Add-Check 'entra.guest' 'pass' 'The exact invited guest exists.' }
    else { Add-Check 'entra.guest' 'fail' 'A guest ID was recorded but the guest is absent.' }
} else { Add-Check 'entra.guest' 'skipped' 'Guest invitation was gated because AZ104_GUEST_EMAIL was not supplied.' }
$failures = @($checks | Where-Object status -eq 'fail').Count
$warnings = @($checks | Where-Object status -in @('warning','skipped')).Count
$result = if ($failures -gt 0) { 'fail' } elseif ($warnings -gt 0) { 'partial' } else { 'pass' }
$output = [ordered]@{ labId = 'LAB-02'; runId = $RunId; generatedAt = (Get-Date).ToUniversalTime().ToString('o'); result = $result; checks = @($checks) }
$output | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Report -Encoding utf8
$output | ConvertTo-Json -Depth 20
if ($result -eq 'fail') { exit 1 }
