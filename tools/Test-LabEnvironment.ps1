#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Readiness results are intentionally displayed to the learner.')]
param(
    [switch]$OfflineOnly,
    [ValidatePattern('^LAB-(?:0[0-9]|1[0-9]|2[0-7])$')]
    [string]$LabId,
    [ValidatePattern('^[a-z0-9]+$')]
    [string]$Location = $env:AZ104_LOCATION,
    [string]$ReportPath = (Join-Path (Split-Path -Parent $PSScriptRoot) '.state/readiness.json')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $false

$repoRoot = Split-Path -Parent $PSScriptRoot
$checks = [System.Collections.Generic.List[object]]::new()
if ([string]::IsNullOrWhiteSpace($Location)) { $Location = 'westeurope' }

function Add-ReadinessCheck {
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][ValidateSet('pass', 'fail', 'warning', 'skipped')][string]$Status,
        [Parameter(Mandatory)][string]$Message,
        [string]$Remediation = ''
    )

    $checks.Add([ordered]@{
            name        = $Name
            status      = $Status
            message     = $Message
            remediation = $Remediation
        })
}

function Invoke-Tool {
    param(
        [Parameter(Mandatory)][string]$Command,
        [Parameter(Mandatory)][string[]]$Arguments
    )

    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
        return [pscustomobject]@{ ExitCode = 127; Output = ''; Found = $false }
    }
    try {
        $output = & $Command @Arguments 2>&1
        return [pscustomobject]@{
            ExitCode = $LASTEXITCODE
            Output   = ($output | Out-String).Trim()
            Found    = $true
        }
    } catch {
        return [pscustomobject]@{
            ExitCode = 126
            Output   = $_.Exception.Message
            Found    = $true
        }
    }
}

function Find-Version {
    param([Parameter(Mandatory)][string]$Text)

    $match = [regex]::Match($Text, '(?<!\d)(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)')
    if (-not $match.Success) { return $null }
    try { return [version]$match.Groups[1].Value } catch { return $null }
}

function Test-VersionedTool {
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string]$Command,
        [Parameter(Mandatory)][string[]]$Arguments,
        [Parameter(Mandatory)][version]$MinimumVersion,
        [Parameter(Mandatory)][string]$InstallGuidance
    )

    $invocation = Invoke-Tool -Command $Command -Arguments $Arguments
    if (-not $invocation.Found) {
        Add-ReadinessCheck -Name $Name -Status fail -Message 'Command not found.' -Remediation $InstallGuidance
        return
    }
    if ($invocation.ExitCode -ne 0) {
        Add-ReadinessCheck -Name $Name -Status fail -Message "Version command exited $($invocation.ExitCode)." -Remediation $InstallGuidance
        return
    }
    $version = Find-Version -Text $invocation.Output
    if ($null -eq $version) {
        Add-ReadinessCheck -Name $Name -Status fail -Message 'Could not parse the installed version.' -Remediation $InstallGuidance
        return
    }
    if ($version -lt $MinimumVersion) {
        Add-ReadinessCheck -Name $Name -Status fail -Message "Version $version is below required $MinimumVersion." -Remediation $InstallGuidance
        return
    }
    Add-ReadinessCheck -Name $Name -Status pass -Message "Version $version satisfies minimum $MinimumVersion."
}

Test-VersionedTool -Name Git -Command git -Arguments @('--version') -MinimumVersion ([version]'2.40') -InstallGuidance 'Install a current Git release.'

$powerShellVersion = $PSVersionTable.PSVersion
if ($powerShellVersion -ge [version]'7.4') {
    Add-ReadinessCheck -Name PowerShell -Status pass -Message "Version $powerShellVersion satisfies minimum 7.4."
} else {
    Add-ReadinessCheck -Name PowerShell -Status fail -Message "Version $powerShellVersion is below required 7.4." -Remediation 'Install PowerShell 7.4 or later.'
}

Test-VersionedTool -Name 'Azure CLI' -Command az -Arguments @('version') -MinimumVersion ([version]'2.88') -InstallGuidance 'Install Azure CLI 2.88 or later.'
Test-VersionedTool -Name Python -Command python -Arguments @('--version') -MinimumVersion ([version]'3.12') -InstallGuidance 'Install Python 3.12 or later.'
Test-VersionedTool -Name 'Node.js' -Command node -Arguments @('--version') -MinimumVersion ([version]'22.0') -InstallGuidance 'Install Node.js 22 or later.'

$bicep = Invoke-Tool -Command az -Arguments @('bicep', 'version')
$bicepVersion = if ($bicep.Found -and $bicep.ExitCode -eq 0) { Find-Version -Text $bicep.Output } else { $null }
if ($bicepVersion -and $bicepVersion -ge [version]'0.46.1') {
    Add-ReadinessCheck -Name Bicep -Status pass -Message "Version $bicepVersion is available through Azure CLI and satisfies minimum 0.46.1."
} else {
    Add-ReadinessCheck -Name Bicep -Status fail -Message 'Bicep 0.46.1 or later is not available through Azure CLI.' -Remediation 'Run az bicep install --version v0.46.1.'
}

$azCopy = Invoke-Tool -Command azcopy -Arguments @('--version')
$azCopyVersion = if ($azCopy.Found -and $azCopy.ExitCode -eq 0) { Find-Version -Text $azCopy.Output } else { $null }
if ($azCopyVersion -and $azCopyVersion -ge [version]'10.32.8') {
    Add-ReadinessCheck -Name AzCopy -Status pass -Message "Version $azCopyVersion satisfies minimum 10.32.8."
} else {
    Add-ReadinessCheck -Name AzCopy -Status fail -Message 'AzCopy 10.32.8 or later is not available on PATH.' -Remediation 'Run the initializer with -InstallDependencies to install the pinned, hash-verified release.'
}

$containerApp = Invoke-Tool -Command az -Arguments @('extension', 'show', '--name', 'containerapp', '--query', 'version', '--output', 'tsv', '--only-show-errors')
$containerAppVersionMatch = [regex]::Match($containerApp.Output, '^(?<major>\d+)\.(?<minor>\d+)\.(?<patch>\d+)(?:b(?<beta>\d+))?$')
$containerAppReady = $false
if ($containerApp.Found -and $containerApp.ExitCode -eq 0 -and $containerAppVersionMatch.Success) {
    $baseVersion = [version]::new(
        [int]$containerAppVersionMatch.Groups['major'].Value,
        [int]$containerAppVersionMatch.Groups['minor'].Value,
        [int]$containerAppVersionMatch.Groups['patch'].Value
    )
    $isPinnedPrereleaseOrLater = $baseVersion -eq [version]'1.3.0' -and (
        -not $containerAppVersionMatch.Groups['beta'].Success -or
        [int]$containerAppVersionMatch.Groups['beta'].Value -ge 4
    )
    $containerAppReady = $baseVersion -gt [version]'1.3.0' -or $isPinnedPrereleaseOrLater
}
if ($containerAppReady) {
    Add-ReadinessCheck -Name 'Azure CLI containerapp extension' -Status pass -Message "Version $($containerApp.Output)."
} else {
    Add-ReadinessCheck -Name 'Azure CLI containerapp extension' -Status fail -Message 'Container Apps extension 1.3.0b4 or later is not installed.' -Remediation 'Run az extension add --name containerapp --version 1.3.0b4.'
}

if ($OfflineOnly) {
    Add-ReadinessCheck -Name 'Azure CLI sign-in' -Status skipped -Message 'Skipped for offline authoring; no Azure context was queried.'
} else {
    $context = Invoke-Tool -Command az -Arguments @('account', 'show', '--query', 'id', '--output', 'tsv', '--only-show-errors')
    if ($context.Found -and $context.ExitCode -eq 0 -and $context.Output) {
        Add-ReadinessCheck -Name 'Azure CLI sign-in' -Status pass -Message 'An active context exists; identifiers were not retained in this report.'
    } else {
        Add-ReadinessCheck -Name 'Azure CLI sign-in' -Status fail -Message 'No active Azure CLI context is available.' -Remediation 'Run az login, then inspect az account show before selecting a disposable sandbox.'
    }
}

if ($LabId) {
    $number = $LabId.Substring(4)
    $labFolder = Get-ChildItem -LiteralPath (Join-Path $repoRoot 'labs') -Directory |
        Where-Object { $_.Name -like "$number-*" } |
        Select-Object -First 1
    if ($labFolder -and
        (Test-Path -LiteralPath (Join-Path $labFolder.FullName 'lab.yml')) -and
        (Test-Path -LiteralPath (Join-Path $labFolder.FullName 'README.md'))) {
        $metadataPath = Join-Path $labFolder.FullName 'lab.yml'
        $metadataCode = @'
import json
import sys

import yaml

with open(sys.argv[1], encoding="utf-8") as handle:
    lab = yaml.safe_load(handle)

required_environment = [
    item["environmentVariable"]
    for item in lab.get("inputs", [])
    if item.get("required")
    and item.get("source") == "environment"
    and item.get("environmentVariable")
]
print(json.dumps({
    "domain": lab.get("domain"),
    "costClass": lab.get("cost", {}).get("class"),
    "providers": lab.get("providers", {}).get("required", []),
    "requiredEnvironment": required_environment,
    "costAcknowledgement": lab.get("acknowledgements", {}).get("cost", {}).get("required", False),
    "tenantAcknowledgement": lab.get("acknowledgements", {}).get("tenantChange", {}).get("required", False),
}))
'@
        $metadataResult = Invoke-Tool -Command python -Arguments @('-c', $metadataCode, $metadataPath)
        if ($metadataResult.ExitCode -ne 0 -or -not $metadataResult.Output) {
            Add-ReadinessCheck -Name "$LabId metadata" -Status fail -Message 'The strict lab contract could not be read.' -Remediation 'Install requirements-dev.txt and rerun readiness.'
        } else {
            try {
                $metadata = $metadataResult.Output | ConvertFrom-Json
                Add-ReadinessCheck -Name "$LabId content" -Status pass -Message "Strict metadata and guided instructions are present; cost class is $($metadata.costClass)."

                foreach ($variableName in @($metadata.requiredEnvironment)) {
                    $present = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable([string]$variableName))
                    Add-ReadinessCheck -Name "$LabId input $variableName" -Status $(if ($present) { 'pass' } else { 'fail' }) -Message $(if ($present) { 'Required environment input is present; its value was not retained.' } else { 'Required environment input is missing.' }) -Remediation $(if ($present) { '' } else { 'Set the documented temporary environment variable, then rerun readiness.' })
                }

                if ($metadata.costAcknowledgement) {
                    Add-ReadinessCheck -Name "$LabId cost gate" -Status warning -Message 'Execution requires an explicit cost acknowledgement after pricing, quota, and cleanup review.'
                }
                if ($metadata.tenantAcknowledgement) {
                    Add-ReadinessCheck -Name "$LabId tenant-change gate" -Status warning -Message 'Execution requires separate tenant-change authorization and restoration review.'
                }

                if ($OfflineOnly) {
                    Add-ReadinessCheck -Name "$LabId Azure prerequisites" -Status skipped -Message 'Provider, region, quota, and SKU queries were skipped in offline mode.'
                } else {
                    $region = Invoke-Tool -Command az -Arguments @('account', 'list-locations', '--query', "[?name=='$Location'].name | [0]", '--output', 'tsv', '--only-show-errors')
                    $regionReady = $region.ExitCode -eq 0 -and $region.Output -eq $Location
                    Add-ReadinessCheck -Name "$LabId region" -Status $(if ($regionReady) { 'pass' } else { 'fail' }) -Message $(if ($regionReady) { "$Location is available to the active subscription." } else { "$Location was not returned for the active subscription." }) -Remediation $(if ($regionReady) { '' } else { 'Choose an approved supported region and rerun readiness.' })

                    foreach ($provider in @($metadata.providers)) {
                        $providerResult = Invoke-Tool -Command az -Arguments @('provider', 'show', '--namespace', [string]$provider, '--query', 'registrationState', '--output', 'tsv', '--only-show-errors')
                        $providerReady = $providerResult.ExitCode -eq 0 -and $providerResult.Output -eq 'Registered'
                        Add-ReadinessCheck -Name "$LabId provider $provider" -Status $(if ($providerReady) { 'pass' } else { 'fail' }) -Message $(if ($providerReady) { 'Registered.' } else { "State is $($providerResult.Output); readiness never registers it automatically." }) -Remediation $(if ($providerReady) { '' } else { 'Obtain authorization to register the provider outside the lab, or use an approved prepared subscription.' })
                    }

                    if ($metadata.domain -in @('compute', 'monitor-recovery', 'capstone') -and $metadata.costClass -in @('moderate', 'elevated')) {
                        $quota = Invoke-Tool -Command az -Arguments @('vm', 'list-usage', '--location', $Location, '--query', 'length(@)', '--output', 'tsv', '--only-show-errors')
                        $quotaCount = 0
                        $quotaCountIsValid = [int]::TryParse($quota.Output, [ref]$quotaCount)
                        $quotaReady = $quota.ExitCode -eq 0 -and $quotaCountIsValid -and $quotaCount -gt 0
                        Add-ReadinessCheck -Name "$LabId regional compute quota" -Status $(if ($quotaReady) { 'pass' } else { 'fail' }) -Message $(if ($quotaReady) { 'Regional quota records are readable; compare required cores in lab preflight.' } else { 'Regional compute quota could not be read.' }) -Remediation $(if ($quotaReady) { '' } else { 'Confirm Compute permissions and regional quota before execution.' })

                        $skus = Invoke-Tool -Command az -Arguments @('vm', 'list-skus', '--location', $Location, '--resource-type', 'virtualMachines', '--query', 'length(@)', '--output', 'tsv', '--only-show-errors')
                        $skuCount = 0
                        $skuCountIsValid = [int]::TryParse($skus.Output, [ref]$skuCount)
                        $skuReady = $skus.ExitCode -eq 0 -and $skuCountIsValid -and $skuCount -gt 0
                        Add-ReadinessCheck -Name "$LabId regional VM SKUs" -Status $(if ($skuReady) { 'pass' } else { 'fail' }) -Message $(if ($skuReady) { 'Regional VM SKU inventory is readable; the lab preflight checks its exact SKU.' } else { 'No regional VM SKU inventory was returned.' }) -Remediation $(if ($skuReady) { '' } else { 'Choose an approved region with the documented SKU.' })
                    }

                    $labPreflight = Join-Path $labFolder.FullName 'scripts/cli/Preflight.ps1'
                    if (Test-Path -LiteralPath $labPreflight) {
                        $preflightResult = Invoke-Tool -Command pwsh -Arguments @(
                            '-NoLogo', '-NoProfile', '-File', $labPreflight,
                            '-RunId', 'readiness', '-Location', $Location
                        )
                        $preflightReady = $preflightResult.ExitCode -eq 0
                        Add-ReadinessCheck -Name "$LabId service preflight" -Status $(if ($preflightReady) { 'pass' } else { 'fail' }) -Message $(if ($preflightReady) { 'The lab-specific read-only assertions passed.' } else { 'One or more lab-specific input, permission, provider, quota, SKU, region, or service assertions failed.' }) -Remediation $(if ($preflightReady) { '' } else { 'Run the lab Preflight.ps1 directly for its redacted check table and remediation details.' })
                    } else {
                        Add-ReadinessCheck -Name "$LabId service preflight" -Status fail -Message 'The lab-specific preflight script is missing.' -Remediation 'Restore the complete repository checkout.'
                    }
                }
            } catch {
                Add-ReadinessCheck -Name "$LabId metadata" -Status fail -Message 'The lab metadata summary was invalid.' -Remediation 'Run python tools/validate_repository.py --release.'
            }
        }
    } else {
        Add-ReadinessCheck -Name "$LabId content" -Status fail -Message 'The requested lab folder or contract files are missing.' -Remediation 'Restore the complete repository checkout.'
    }
}

$blockingFailures = @($checks | Where-Object status -eq 'fail')
$overallStatus = if ($blockingFailures.Count -eq 0) { 'pass' } else { 'fail' }
$report = [ordered]@{
    schemaVersion = '1.0.0'
    generatedAt   = [DateTimeOffset]::UtcNow.ToString('o')
    mode          = if ($OfflineOnly) { 'offline' } else { 'azure-ready' }
    requestedLab  = if ($LabId) { $LabId } else { $null }
    result        = $overallStatus
    checks        = @($checks)
}

$resolvedReportPath = [System.IO.Path]::GetFullPath($ReportPath)
$reportDirectory = Split-Path -Parent $resolvedReportPath
if (-not (Test-Path -LiteralPath $reportDirectory)) {
    New-Item -ItemType Directory -Path $reportDirectory -Force | Out-Null
}
$report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $resolvedReportPath -Encoding utf8

foreach ($check in $checks) {
    $label = $check.status.ToUpperInvariant().PadRight(7)
    Write-Host "$label $($check.name): $($check.message)"
    if ($check.remediation) { Write-Host "        Remediation: $($check.remediation)" }
}
Write-Host "Readiness report: $resolvedReportPath"

if ($overallStatus -eq 'fail') {
    Write-Error "Environment readiness failed with $($blockingFailures.Count) blocking check(s)."
    exit 1
}
Write-Host 'Environment readiness passed.'
exit 0
