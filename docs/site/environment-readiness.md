# Environment readiness

The readiness tools support Windows, Linux, macOS, dev containers, and
Codespaces. PowerShell is the command host; Azure operations remain Azure CLI
commands.

## Required toolchain

| Tool | Blocking minimum or pinned repository version |
|---|---|
| Git | 2.40 or later |
| PowerShell | 7.4 or later |
| Azure CLI | 2.88 or later |
| Python | 3.12 or later |
| Node.js | 22 or later |
| Bicep through `az bicep` | 0.46.1 or later; repository install pins 0.46.1 |
| AzCopy | 10.32.8 or later; repository install pins and verifies 10.32.8 |
| Azure CLI `containerapp` extension | 1.3.0b4 or later; repository install pins 1.3.0b4 |

## Initialize once

From the repository root, run:

```powershell
pwsh -File tools/Initialize-LabEnvironment.ps1
```

This creates an ignored local state directory, copies the non-secret learner
configuration example if needed, and runs the blocking readiness report. It
does not sign in, select a subscription, or install software without permission.

To install repository Python dependencies, Bicep, the pinned Azure CLI
extension, and a pinned, hash-verified user-local AzCopy binary where possible,
run:

```powershell
pwsh -File tools/Initialize-LabEnvironment.ps1 -InstallDependencies
```

Review downloaded-tool policy before using the installation option on a managed
workstation. The initializer deliberately does not install the base Git,
PowerShell, Azure CLI, Python, or Node.js applications; install those through an
approved operating-system or enterprise software channel first.

## Run a readiness check

```powershell
pwsh -File tools/Test-LabEnvironment.ps1
```

The report blocks on unsupported or missing Git, Azure CLI, PowerShell, Python,
Node.js, Bicep, AzCopy, the `containerapp` extension, or Azure CLI sign-in. With
`-LabId`, it also checks declared inputs, provider registration, region, and
applicable compute quota/SKU prerequisites. It writes only non-secret readiness
states—not tenant IDs, subscription IDs, usernames, input values, or tokens—to
`.state/readiness.json`.

For offline authoring and CI, skip Azure sign-in and other Azure-backed checks:

```powershell
pwsh -File tools/Test-LabEnvironment.ps1 -OfflineOnly
```

Without `-LabId`, offline mode skips only sign-in because no lab-specific Azure
queries were requested. With `-LabId`, it also skips provider, region, quota,
SKU, and service-preflight queries. The tool versions and local lab contract
still block. `-OfflineOnly` means no Azure control-plane queries; it does not
make `-InstallDependencies` a network-isolated package installation.

## Configure safe defaults

Edit `.state/learner.config.yml` after initialization. The
[configuration example](../../learner.config.example.yml) contains no
credentials. Keep subscription IDs and other environment-specific values in the
ignored local copy or temporary environment variables, never in Git.

## VS Code and dev containers

The repository includes recommended extensions and tasks for initialization,
readiness, repository validation, tests, strict site builds, site preview,
progress, and cleanup previews. The dev container pins its operating system and
toolchain versions, installs the repository's pinned authoring dependencies,
and runs the readiness report with Azure sign-in and Azure prerequisite queries
disabled.
