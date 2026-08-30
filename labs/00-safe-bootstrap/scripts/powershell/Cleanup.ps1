[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute(
    'PSAvoidUsingWriteHost',
    '',
    Justification = 'Cleanup is an explicitly interactive preview/execute workflow.'
)]
param(
    [Parameter(Mandatory)]
    [string] $RunId,
    [string] $StateRoot = (Join-Path $PSScriptRoot '..\..\.state'),
    [switch] $Execute
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$runPattern = '^[a-z0-9][a-z0-9-]{2,31}$'
if ($RunId -notmatch $runPattern) {
    throw "RunId must match $runPattern."
}

$stateRootFull = [IO.Path]::GetFullPath($StateRoot).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
if (-not (Test-Path -LiteralPath $stateRootFull -PathType Container)) {
    Write-Host 'Nothing to clean: state root does not exist.'
    exit 0
}

$runDirectory = [IO.Path]::GetFullPath((Join-Path $stateRootFull $RunId))
$requiredPrefix = $stateRootFull + [IO.Path]::DirectorySeparatorChar
if (-not $runDirectory.StartsWith($requiredPrefix, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Resolved run path escapes the selected state root.'
}
if (-not (Test-Path -LiteralPath $runDirectory)) {
    Write-Host "Nothing to clean for run '$RunId'."
    exit 0
}

$runItem = Get-Item -LiteralPath $runDirectory -Force
if (-not $runItem.PSIsContainer -or ($runItem.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
    throw 'Selected run path is not a regular directory; refusing cleanup.'
}

$manifestPath = Join-Path $runDirectory 'run.json'
if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
    throw 'run.json is missing; refusing cleanup.'
}
$state = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json

$resourceCount = @($state.resources).Count
$tenantChangeCount = @($state.tenantScopedChanges).Count
$hasExactFalseMutationFlag = $state.liveAzureMutations -is [bool] -and $state.liveAzureMutations -eq $false
if ([string] $state.labId -ne '00-safe-bootstrap' -or [string] $state.runId -ne $RunId) {
    throw 'Manifest identity does not match the selected run.'
}
if ($resourceCount -ne 0 -or $tenantChangeCount -ne 0 -or -not $hasExactFalseMutationFlag) {
    throw 'State records Azure resources or shared-setting changes. Lab 00 cleanup never deletes Azure objects; review the manifest manually.'
}

$fileCount = @(Get-ChildItem -LiteralPath $runDirectory -File -Recurse -Force).Count
Write-Host 'Cleanup plan'
Write-Host '  Azure deletions:       none'
Write-Host '  Tenant restorations:   none'
Write-Host "  Local directory:       $runDirectory"
Write-Host "  Local files to remove: $fileCount"

if (-not $Execute) {
    Write-Host 'Preview only. Rerun with -Execute to remove exactly this local run directory.'
    exit 0
}

Remove-Item -LiteralPath $runDirectory -Recurse -Force
if (Test-Path -LiteralPath $runDirectory) {
    throw 'Local run directory still exists after cleanup.'
}
Write-Host "Removed local state for run '$RunId'. No Azure changes were made."
