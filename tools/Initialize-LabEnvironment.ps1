#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Initialization progress is intentionally displayed to the learner.')]
param(
    [switch]$InstallDependencies,
    [switch]$OfflineOnly,
    [ValidatePattern('^LAB-(?:0[0-9]|1[0-9]|2[0-7])$')]
    [string]$LabId
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

$repoRoot = Split-Path -Parent $PSScriptRoot
$stateRoot = Join-Path $repoRoot '.state'
$exampleConfig = Join-Path $repoRoot 'learner.config.example.yml'
$localConfig = Join-Path $stateRoot 'learner.config.yml'
$pinnedAzCopyVersion = '10.32.8'
$pinnedContainerAppExtensionVersion = '1.3.0b4'

if (-not (Test-Path -LiteralPath $exampleConfig)) {
    throw 'learner.config.example.yml is missing from the repository root.'
}
if (-not (Test-Path -LiteralPath $stateRoot)) {
    New-Item -ItemType Directory -Path $stateRoot -Force | Out-Null
    Write-Host "Created ignored state directory: $stateRoot"
}
if (-not (Test-Path -LiteralPath $localConfig)) {
    Copy-Item -LiteralPath $exampleConfig -Destination $localConfig
    Write-Host "Created non-secret local configuration: $localConfig"
} else {
    Write-Host "Kept existing local configuration: $localConfig"
}

function Invoke-CheckedCommand {
    param(
        [Parameter(Mandatory)][string]$Command,
        [Parameter(Mandatory)][string[]]$Arguments,
        [Parameter(Mandatory)][string]$Description
    )

    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
        throw "$Description requires '$Command', which is not available on PATH."
    }
    Write-Host $Description
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Description failed with exit code $LASTEXITCODE."
    }
}

function Install-UserAzCopy {
    $existingAzCopy = Get-Command azcopy -ErrorAction SilentlyContinue
    if ($existingAzCopy) {
        $existingVersion = (& $existingAzCopy.Source --version 2>&1 | Out-String).Trim()
        if ($existingVersion -match "(?<![0-9])$([regex]::Escape($pinnedAzCopyVersion))(?![0-9])") {
            Write-Host "Pinned AzCopy $pinnedAzCopyVersion is already available; installation skipped."
            return
        }
        Write-Host "AzCopy is present but does not match pinned version $pinnedAzCopyVersion; installing the repository version in the user tool directory."
    }

    $platform = if ($IsWindows) { 'windows' } elseif ($IsMacOS) { 'mac' } else { 'linux' }
    $architecture = switch ([System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture) {
        'X64' { 'amd64' }
        'Arm64' { 'arm64' }
        'X86' { '386' }
        default { throw "AzCopy installation does not support architecture '$($_)'." }
    }
    $assetKey = "$platform-$architecture"
    $asset = switch ($assetKey) {
        'windows-amd64' { @{ Name = "azcopy_windows_amd64_$pinnedAzCopyVersion.zip"; Sha256 = '99fa0387e91250b0aa4f3e6186e3ea07ec21b62e95e42a58da10144ad5bbf38d' } }
        'windows-arm64' { @{ Name = "azcopy_windows_arm64_$pinnedAzCopyVersion.zip"; Sha256 = '938ba0db363f1a9e1df9f953c4eebf0a3206f7332278f706a10776f5be582c2d' } }
        'windows-386' { @{ Name = "azcopy_windows_386_$pinnedAzCopyVersion.zip"; Sha256 = '5dd442d71a4ba646f6d6073727140d5997e51933676c8d5c641d9326945c0e94' } }
        'linux-amd64' { @{ Name = "azcopy_linux_amd64_$pinnedAzCopyVersion.tar.gz"; Sha256 = 'a95277dbc265912cefdddbaf251aa99ec648cb18ba657e8788066357a9022dc3' } }
        'linux-arm64' { @{ Name = "azcopy_linux_arm64_$pinnedAzCopyVersion.tar.gz"; Sha256 = '50e6e58a109f2afd64376b5b003973ff213fbfdec795fe81a95b208982061d9b' } }
        'mac-amd64' { @{ Name = "azcopy_darwin_amd64_$pinnedAzCopyVersion.zip"; Sha256 = '2caddd8ca13cea744847929428f5f4777be1b5ca2c872e368a6158ff8b8d97df' } }
        'mac-arm64' { @{ Name = "azcopy_darwin_arm64_$pinnedAzCopyVersion.zip"; Sha256 = 'd17c2a7df11425f2dbc9df397af41495b32a38009e1a230e3c21892cc7a2c8c1' } }
        default { throw "No pinned AzCopy asset is declared for '$assetKey'." }
    }
    $extension = if ($asset.Name.EndsWith('.zip')) { 'zip' } else { 'tar.gz' }
    $downloadUri = "https://github.com/Azure/azure-storage-azcopy/releases/download/v$pinnedAzCopyVersion/$($asset.Name)"
    $temporaryRoot = Join-Path ([System.IO.Path]::GetTempPath()) "az104-azcopy-$([guid]::NewGuid().ToString('N'))"
    $archivePath = Join-Path $temporaryRoot "azcopy.$extension"
    $extractPath = Join-Path $temporaryRoot 'extract'
    $profilePath = [Environment]::GetFolderPath([Environment+SpecialFolder]::UserProfile)
    $installRoot = Join-Path $profilePath '.az104-tools/azcopy'

    try {
        New-Item -ItemType Directory -Path $extractPath -Force | Out-Null
        Write-Host "Downloading pinned AzCopy $pinnedAzCopyVersion from the official Azure release for $assetKey."
        Invoke-WebRequest -Uri $downloadUri -OutFile $archivePath -UseBasicParsing
        $actualHash = (Get-FileHash -LiteralPath $archivePath -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($actualHash -ne $asset.Sha256) {
            throw "AzCopy archive hash mismatch. Expected $($asset.Sha256); received $actualHash."
        }
        if ($IsWindows) {
            Expand-Archive -LiteralPath $archivePath -DestinationPath $extractPath -Force
        } else {
            Invoke-CheckedCommand -Command tar -Arguments @('-xzf', $archivePath, '-C', $extractPath) -Description 'Extracting AzCopy'
        }
        $binaryName = if ($IsWindows) { 'azcopy.exe' } else { 'azcopy' }
        $binary = Get-ChildItem -LiteralPath $extractPath -Recurse -File -Filter $binaryName | Select-Object -First 1
        if (-not $binary) { throw 'The official AzCopy archive did not contain the expected executable.' }
        New-Item -ItemType Directory -Path $installRoot -Force | Out-Null
        Copy-Item -LiteralPath $binary.FullName -Destination (Join-Path $installRoot $binaryName) -Force
        if (-not $IsWindows) {
            Invoke-CheckedCommand -Command chmod -Arguments @('+x', (Join-Path $installRoot $binaryName)) -Description 'Marking AzCopy executable'
        }
        $env:PATH = "$installRoot$([System.IO.Path]::PathSeparator)$env:PATH"
        $installedVersion = (& (Join-Path $installRoot $binaryName) --version 2>&1 | Out-String).Trim()
        if ($installedVersion -notmatch "(?<![0-9])$([regex]::Escape($pinnedAzCopyVersion))(?![0-9])") {
            throw "Installed AzCopy did not report pinned version $pinnedAzCopyVersion."
        }
        Write-Host "Installed verified AzCopy $pinnedAzCopyVersion for this user at $installRoot. Add that directory to PATH in future shells."
    } finally {
        if (Test-Path -LiteralPath $temporaryRoot) {
            $resolvedTemporaryRoot = [System.IO.Path]::GetFullPath($temporaryRoot)
            $resolvedTemporaryBase = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath()).TrimEnd([System.IO.Path]::DirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
            $temporaryLeaf = Split-Path -Leaf $resolvedTemporaryRoot
            if (-not $resolvedTemporaryRoot.StartsWith($resolvedTemporaryBase, [System.StringComparison]::OrdinalIgnoreCase) -or
                $temporaryLeaf -notmatch '^az104-azcopy-[0-9a-f]{32}$') {
                throw "Refusing to remove unexpected temporary path: $resolvedTemporaryRoot"
            }
            Remove-Item -LiteralPath $resolvedTemporaryRoot -Recurse -Force
        }
    }
}

if ($InstallDependencies) {
    Invoke-CheckedCommand -Command python -Arguments @('-m', 'pip', 'install', '-r', (Join-Path $repoRoot 'requirements-dev.txt'), '-r', (Join-Path $repoRoot 'requirements-docs.txt')) -Description 'Installing pinned Python dependencies'
    Invoke-CheckedCommand -Command az -Arguments @('bicep', 'install', '--version', 'v0.46.1') -Description 'Installing pinned Bicep through Azure CLI'
    Invoke-CheckedCommand -Command az -Arguments @('extension', 'add', '--name', 'containerapp', '--version', $pinnedContainerAppExtensionVersion, '--only-show-errors') -Description "Installing pinned Container Apps extension $pinnedContainerAppExtensionVersion"
    Install-UserAzCopy
} else {
    Write-Host 'Software installation was not requested. Use -InstallDependencies to install repository-managed dependencies.'
}

$testScript = Join-Path $PSScriptRoot 'Test-LabEnvironment.ps1'
$arguments = @('-NoLogo', '-NoProfile', '-File', $testScript)
if ($OfflineOnly) { $arguments += '-OfflineOnly' }
if ($LabId) { $arguments += @('-LabId', $LabId) }

Write-Host 'Running the blocking readiness report.'
& pwsh @arguments
exit $LASTEXITCODE
