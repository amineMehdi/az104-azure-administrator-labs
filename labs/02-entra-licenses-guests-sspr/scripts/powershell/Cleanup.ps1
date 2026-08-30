#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive cleanup previews are intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Tenant and subscription lanes share a consistent cleanup interface.')]
param(
    [string]$SubscriptionId = '',
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$Manifest = Join-Path $LabRoot ".state/$RunId/run.json"
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Missing state: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
Write-Host 'Cleanup preview for LAB-02'
Write-Host '  exact target:' $($state.external | ConvertTo-Json -Compress)
Write-Host '  residual/soft-delete behavior must be audited after deletion.'
if (-not $Execute) { Write-Host 'Preview only. Re-run with -Execute after checking every target.'; return }
$graphContext = Get-MgContext
if (-not $graphContext -or $graphContext.TenantId -ne $state.tenantId) { throw 'Active Graph tenant does not match the manifest.' }
if ($state.external.licenseSkuId -and $state.external.guestUserId) {
    Set-MgUserLicense -UserId $state.external.guestUserId -AddLicenses @() -RemoveLicenses @([Guid]$state.external.licenseSkuId)
}
if ($state.external.guestUserId) { Remove-MgUser -UserId $state.external.guestUserId -Confirm:$false -ErrorAction SilentlyContinue }
if ($state.external.groupId) { Remove-MgGroup -GroupId $state.external.groupId -Confirm:$false -ErrorAction SilentlyContinue }
if ($state.external.ssprChanged -and $null -ne $state.external.originalAllowedToUseSspr) {
    Update-MgPolicyAuthorizationPolicy -AllowedToUseSspr ([bool]$state.external.originalAllowedToUseSspr)
}
Write-Host 'Exact active tenant objects were removed. Deleted-user retention was not purged.'
$state.status = 'cleanup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
