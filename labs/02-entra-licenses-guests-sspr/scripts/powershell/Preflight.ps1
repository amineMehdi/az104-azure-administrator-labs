#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lanes keep a consistent explicit context interface.')]
param(
    [string]$SubscriptionId = '',
    [Parameter(Mandatory)][string]$Location
)

$ErrorActionPreference = 'Stop'
$requiredModules = @(
    'Microsoft.Graph.Authentication',
    'Microsoft.Graph.Users',
    'Microsoft.Graph.Groups',
    'Microsoft.Graph.Identity.SignIns'
)
foreach ($module in $requiredModules) {
    if (-not (Get-Module -ListAvailable -Name $module)) { throw "Missing required module: $module" }
}

$graphContext = Get-MgContext
if (-not $graphContext) { throw 'No Microsoft Graph context is active. Sign in deliberately before running this lab.' }
Write-Host "Graph tenant: $($graphContext.TenantId)"
Write-Host "Graph account: $($graphContext.Account)"
Write-Host 'Lab: LAB-02'
Write-Host 'Location:' $Location
Write-Host 'Cost class: none'
Write-Host 'Role boundary: User Administrator and License Administrator; Authentication Policy Administrator for the SSPR policy path'
Write-Host 'Azure provider checks are not applicable to this tenant-scoped lab.'
Write-Host 'Preflight is read-only. It does not connect, change context, register providers, or create resources.'
