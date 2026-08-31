#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Progress status is intentionally displayed to the learner.')]
param(
    [ValidatePattern('^LAB-(?:0[0-9]|1[0-9]|2[0-7])$')]
    [string]$LabId,
    [ValidateSet('not-started', 'in-progress', 'complete')]
    [string]$Status,
    [ValidateSet('true', 'false')]
    [string]$ValidationPassed,
    [ValidateSet('true', 'false')]
    [string]$CleanupPassed,
    [Nullable[int]]$AssessmentScore,
    [string]$ImportPath,
    [string]$ExportPath,
    [switch]$Show,
    [string]$ProgressPath = (Join-Path (Split-Path -Parent $PSScriptRoot) '.state/progress.json')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$schemaVersion = '1.0.0'
$allowedTopLevel = @('schemaVersion', 'exportedAt', 'labs')
$allowedEntry = @('status', 'validationPassed', 'cleanupPassed', 'assessmentScore', 'updatedAt')
$forbiddenKeys = @('tenantId', 'subscriptionId', 'userId', 'userName', 'username', 'resourceId', 'token')

function Test-Iso8601Timestamp {
    param([AllowNull()]$Value)

    # PowerShell 7.5 may deserialize RFC 3339 JSON strings as DateTime values;
    # those values could only have come from a recognized timestamp token.
    if ($Value -is [datetime] -or $Value -is [DateTimeOffset]) {
        return $true
    }
    if ($Value -isnot [string] -or $Value -cnotmatch '^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})$') {
        return $false
    }
    $parsed = [DateTimeOffset]::MinValue
    return [DateTimeOffset]::TryParse([string]$Value, [ref]$parsed)
}

function Get-EmptyProgressRecord {
    $timestamp = [DateTimeOffset]::UtcNow.ToString('o')
    $labs = [ordered]@{}
    foreach ($number in 0..27) {
        $labs[('LAB-{0:d2}' -f $number)] = [ordered]@{
            status           = 'not-started'
            validationPassed = $false
            cleanupPassed    = $false
            assessmentScore  = $null
            updatedAt        = $timestamp
        }
    }
    return [ordered]@{
        schemaVersion = $schemaVersion
        exportedAt   = $timestamp
        labs          = $labs
    }
}

function Find-ForbiddenKey {
    param([Parameter(Mandatory)][AllowNull()]$Value)

    if ($Value -is [System.Collections.IDictionary]) {
        foreach ($key in $Value.Keys) {
            if ($forbiddenKeys -contains [string]$key) { return [string]$key }
            $nested = Find-ForbiddenKey -Value $Value[$key]
            if ($nested) { return $nested }
        }
    } elseif ($Value -is [System.Collections.IEnumerable] -and $Value -isnot [string]) {
        foreach ($item in $Value) {
            $nested = Find-ForbiddenKey -Value $item
            if ($nested) { return $nested }
        }
    }
    return $null
}

function Assert-ProgressRecord {
    param([Parameter(Mandatory)][System.Collections.IDictionary]$Record)

    $unexpected = @($Record.Keys | Where-Object { $_ -notin $allowedTopLevel })
    if ($unexpected.Count -gt 0) { throw "Unexpected top-level progress field(s): $($unexpected -join ', ')." }
    if ($Record.schemaVersion -ne $schemaVersion) { throw "Progress must use schemaVersion $schemaVersion." }
    if (-not (Test-Iso8601Timestamp -Value $Record.exportedAt)) {
        throw 'Progress exportedAt must be an ISO 8601 timestamp.'
    }
    if ($Record.labs -isnot [System.Collections.IDictionary]) { throw 'Progress labs must be an object keyed by LAB-00 through LAB-27.' }
    if ($Record.labs.Count -ne 28) { throw 'Progress must contain exactly LAB-00 through LAB-27.' }
    $forbidden = Find-ForbiddenKey -Value $Record
    if ($forbidden) { throw "Progress contains forbidden private field '$forbidden'." }

    foreach ($entryPair in $Record.labs.GetEnumerator()) {
        $entryId = [string]$entryPair.Key
        $entry = $entryPair.Value
        if ($entryId -notmatch '^LAB-(?:0[0-9]|1[0-9]|2[0-7])$') { throw "Invalid lab progress key '$entryId'." }
        if ($entry -isnot [System.Collections.IDictionary]) { throw "$entryId progress must be an object." }
        $unexpectedEntry = @($entry.Keys | Where-Object { $_ -notin $allowedEntry })
        if ($unexpectedEntry.Count -gt 0) { throw "$entryId has unexpected field(s): $($unexpectedEntry -join ', ')." }
        foreach ($required in $allowedEntry) {
            if (-not $entry.Contains($required)) { throw "$entryId is missing '$required'." }
        }
        if ($entry.status -notin @('not-started', 'in-progress', 'complete')) { throw "$entryId has an invalid status." }
        if ($entry.validationPassed -isnot [bool] -or $entry.cleanupPassed -isnot [bool]) { throw "$entryId validation and cleanup values must be Boolean." }
        if ($entry.status -eq 'complete' -and (-not $entry.validationPassed -or -not $entry.cleanupPassed)) {
            throw "$entryId cannot be complete until validation and cleanup pass."
        }
        if ($null -ne $entry.assessmentScore) {
            if ($entryId -in @('LAB-00', 'LAB-26', 'LAB-27')) {
                throw "$entryId is hands-on only and cannot contain an assessmentScore."
            }
            $score = 0
            if (-not [int]::TryParse([string]$entry.assessmentScore, [ref]$score) -or $score -lt 0 -or $score -gt 100) {
                throw "$entryId assessmentScore must be null or an integer from 0 through 100."
            }
        }
        if (-not (Test-Iso8601Timestamp -Value $entry.updatedAt)) {
            throw "$entryId updatedAt must be an ISO 8601 timestamp."
        }
    }
}

function Read-ProgressRecord {
    param([Parameter(Mandatory)][string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) { return Get-EmptyProgressRecord }
    $record = Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json -AsHashtable
    Assert-ProgressRecord -Record $record
    return $record
}

function Write-ProgressRecord {
    param(
        [Parameter(Mandatory)][System.Collections.IDictionary]$Record,
        [Parameter(Mandatory)][string]$Path
    )

    $Record.exportedAt = [DateTimeOffset]::UtcNow.ToString('o')
    Assert-ProgressRecord -Record $Record
    $resolvedPath = [System.IO.Path]::GetFullPath($Path)
    $directory = Split-Path -Parent $resolvedPath
    if (-not (Test-Path -LiteralPath $directory)) {
        New-Item -ItemType Directory -Path $directory -Force | Out-Null
    }
    $temporaryPath = Join-Path $directory ".az104-progress-$([guid]::NewGuid().ToString('N')).tmp"
    try {
        $Record | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $temporaryPath -Encoding utf8
        [System.IO.File]::Move($temporaryPath, $resolvedPath, $true)
    } finally {
        if (Test-Path -LiteralPath $temporaryPath) {
            Remove-Item -LiteralPath $temporaryPath -Force
        }
    }
    return $resolvedPath
}

$resolvedProgressPath = [System.IO.Path]::GetFullPath($ProgressPath)
$labUpdateArguments = @('LabId', 'Status', 'ValidationPassed', 'CleanupPassed', 'AssessmentScore')
$hasLabUpdateArgument = @($labUpdateArguments | Where-Object { $PSBoundParameters.ContainsKey($_) }).Count -gt 0
$hasLabUpdateValue = @($labUpdateArguments[1..4] | Where-Object { $PSBoundParameters.ContainsKey($_) }).Count -gt 0
if ($ImportPath -and $hasLabUpdateArgument) { throw 'Import and lab update arguments cannot be combined.' }
if (-not $LabId -and $hasLabUpdateValue) {
    throw '-Status, validation, cleanup, and assessment values require -LabId.'
}
if ($ImportPath) {
    $imported = Get-Content -LiteralPath ([System.IO.Path]::GetFullPath($ImportPath)) -Raw | ConvertFrom-Json -AsHashtable
    Assert-ProgressRecord -Record $imported
    $resolvedProgressPath = Write-ProgressRecord -Record $imported -Path $resolvedProgressPath
    Write-Host "Imported progress to $resolvedProgressPath"
}

$record = Read-ProgressRecord -Path $resolvedProgressPath
if ($LabId) {
    if (-not $Status) { throw '-Status is required when -LabId is supplied.' }
    $existing = $record.labs[$LabId]
    $existing.status = $Status
    if ($ValidationPassed) { $existing.validationPassed = [bool]::Parse($ValidationPassed) }
    if ($CleanupPassed) { $existing.cleanupPassed = [bool]::Parse($CleanupPassed) }
    if ($null -ne $AssessmentScore) {
        if ($LabId -in @('LAB-00', 'LAB-26', 'LAB-27')) {
            throw "$LabId is hands-on only and does not accept -AssessmentScore."
        }
        $scoreValue = [int]$AssessmentScore
        if ($scoreValue -lt 0 -or $scoreValue -gt 100) { throw '-AssessmentScore must be from 0 through 100.' }
        $existing.assessmentScore = $scoreValue
    }
    $existing.updatedAt = [DateTimeOffset]::UtcNow.ToString('o')
    $record.labs[$LabId] = $existing
    $resolvedProgressPath = Write-ProgressRecord -Record $record -Path $resolvedProgressPath
    Write-Host "Updated $LabId progress in $resolvedProgressPath"
}

if ($ExportPath) {
    $resolvedExportPath = Write-ProgressRecord -Record $record -Path $ExportPath
    Write-Host "Exported progress to $resolvedExportPath"
}
if ($Show -or (-not $LabId -and -not $ImportPath -and -not $ExportPath)) {
    $record | ConvertTo-Json -Depth 8
}
