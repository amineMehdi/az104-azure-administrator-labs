# Lab 01: Create and manage Microsoft Entra users and groups

Use Azure CLI commands hosted in PowerShell to complete this isolated AZ-104 exercise. The lab never requires a browser portal workflow.

## Learning objectives

| ID | Objective |
|---|---|
| `IG-USERS-01` | See the official objective map. |
| `IG-USERS-02` | See the official objective map. |

## Architecture

![Lab 01 architecture](diagrams/architecture.svg)

The editable source is [diagrams/architecture.mmd](diagrams/architecture.mmd).

## Sign in and confirm Azure CLI context

```powershell
az login
az account show --query '{subscription:id,tenant:tenantId,user:user.name}' --output json
```

Select the intended disposable sandbox yourself if the displayed context is wrong. The lifecycle scripts refuse a mismatch and never switch it for you.

## Command and safety contract

- Install Azure CLI and PowerShell 7.4 or later.
- Sign in deliberately with `az login`, then confirm the displayed tenant and subscription.
- Use a disposable non-production environment and the smallest documented role scope.
- Setup and cleanup are previews until `-Execute` is supplied.
- Keep credentials and tokens out of command evidence, state files, and Git history.
- Use a unique run ID if you repeat the lab or try another execution lane.

<!-- BEGIN GENERATED INLINE COMMANDS -->
## Complete inline command implementation

The lifecycle commands below are the complete learner-facing implementation. They are embedded from the retained script files so the README and automation cannot drift. Review each stage here before running it. Use a different run ID if you later try the optional scripted lane against the same sandbox.

### Preflight: `scripts/cli/Preflight.ps1`

```powershell
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Lifecycle scripts keep one consistent interface across all labs.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Shared safe-naming variables are retained for a consistent learner path.')]
param(
    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$Location
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Install it, run az login deliberately, and retry.'
}

$account = az account show --output json | ConvertFrom-Json
if (-not $account) { throw 'No active Azure CLI context. Run az login deliberately before this lab.' }
if ($SubscriptionId -and $account.id -ne $SubscriptionId) {
    throw "Context mismatch: active subscription is $($account.id), expected $SubscriptionId. This script will not switch it."
}
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }

Write-Host 'Lab: LAB-01'
Write-Host "Tenant: $($account.tenantId)"
Write-Host "Subscription: $SubscriptionId"
Write-Host "Location: $Location"
Write-Host 'Cost class: none'
Write-Host 'Role boundary: User Administrator at tenant scope is recommended for the complete exercise'

$providers = @(

)
foreach ($provider in $providers) {
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $registrationState) { $registrationState = 'Unavailable' }
    Write-Host ('Provider {0,-38} {1}' -f $provider, $registrationState)
}

if ('tenant' -eq 'tenant') {
    $null = az account get-access-token --resource-type ms-graph --query expiresOn --output tsv
    Write-Host 'Microsoft Graph access through Azure CLI is available.'
}
Write-Host 'Preflight is read-only. It does not sign in, switch context, register providers, or create resources.'
```

### Setup: `scripts/cli/Setup.ps1`

```powershell
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Lifecycle scripts keep one consistent interface across all labs.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Shared safe-naming variables are retained for a consistent learner path.')]
param(
    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZURE_SECONDARY_LOCATION,
    [switch]$Execute
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
$ResourceGroupName = "rg-az104-l01-$RunId"
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-01 plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  scope: tenant'
Write-Host '  cost class: none'
Write-Host '  resources: Two cloud-only member users, One security group, One group membership, One group owner assignment'
if (-not $Execute) {
    Write-Host 'Preview only. Re-run with -Execute after approving context, permissions, cost, and gates.'
    return
}

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -Location $Location
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest; choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
$state = [ordered]@{
    labId = 'LAB-01'
    runId = $RunId
    tenantId = [string]$account.tenantId
    subscriptionId = $SubscriptionId
    location = $Location
    createdAt = (Get-Date).ToUniversalTime().ToString('o')
    status = 'recorded-before-mutation'
    resourceGroup = [ordered]@{ name = $null; id = $null }
    resources = @()
    external = [ordered]@{}
}
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8

if ('tenant' -eq 'subscription') {
    $expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd')
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=01 runId=$RunId expiresOn=$expiresOn --output none
    $state.resourceGroup.name = $ResourceGroupName
    $state.resourceGroup.id = az group show --subscription $SubscriptionId --name $ResourceGroupName --query id --output tsv
    $state.status = 'baseline-created'
    $state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
}

if (-not $env:AZ104_LAB_INITIAL_PASSWORD -or $env:AZ104_LAB_INITIAL_PASSWORD.Length -lt 12) {
    throw 'Set AZ104_LAB_INITIAL_PASSWORD to a policy-compliant temporary password of at least 12 characters.'
}

if (-not $env:AZ104_TENANT_DOMAIN) { throw 'Set AZ104_TENANT_DOMAIN to a verified tenant domain.' }
$domain = $env:AZ104_TENANT_DOMAIN
$aliases = @("az104l01a$suffix", "az104l01b$suffix")
$displayNames = @("AZ104-L01-$RunId-Alex", "AZ104-L01-$RunId-Blair")
$userIds = @()
for ($index = 0; $index -lt 2; $index++) {
    $upn = "$($aliases[$index])@$domain"
    $secretPath = Join-Path $StateDir ".user-$index.json"
    $body = [ordered]@{
        accountEnabled = $true
        displayName = $displayNames[$index]
        mailNickname = $aliases[$index]
        userPrincipalName = $upn
        passwordProfile = [ordered]@{ forceChangePasswordNextSignIn = $true; password = $env:AZ104_LAB_INITIAL_PASSWORD }
    }
    try {
        $body | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $secretPath -Encoding utf8
        $created = az rest --method post --url 'https://graph.microsoft.com/v1.0/users' --body "@$secretPath" --output json | ConvertFrom-Json
    }
    finally {
        Remove-Item -LiteralPath $secretPath -Force -ErrorAction SilentlyContinue
    }
    $userIds += [string]$created.id
}
$group = az ad group create --display-name "AZ104-L01-$RunId-Operators" --mail-nickname "az104l01g$suffix" --output json | ConvertFrom-Json
az ad group member add --group $group.id --member-id $userIds[0] --output none
az ad group owner add --group $group.id --owner-object-id $userIds[1] --output none
$state.external['userIds'] = @($userIds)
$state.external['groupId'] = [string]$group.id
Remove-Item Env:AZ104_LAB_INITIAL_PASSWORD -ErrorAction SilentlyContinue

if ('tenant' -eq 'subscription') {
    $state.resources = @(az resource list --subscription $SubscriptionId --resource-group $ResourceGroupName --output json | ConvertFrom-Json | ForEach-Object {
        [ordered]@{ id = $_.id; name = $_.name; type = $_.type; location = $_.location }
    })
}
$state.status = 'setup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
```

### Validate: `scripts/cli/Validate.ps1`

```powershell
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

if ('tenant' -eq 'local') {
    Add-Check state.local pass 'The manifest records a local-only bootstrap run.'
} elseif ('tenant' -eq 'tenant') {
    foreach ($userId in @($state.external.userIds)) {
        $user = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$userId" --output json 2>$null
        if ($LASTEXITCODE -eq 0 -and $user) { Add-Check "entra.user.$userId" pass 'The exact recorded user exists.' }
        else { Add-Check "entra.user.$userId" fail 'A recorded user is absent.' }
    }
    $group = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($state.external.groupId)" --output json 2>$null
    if ($LASTEXITCODE -eq 0 -and $group) { Add-Check entra.group pass 'The exact recorded group exists.' }
    else { Add-Check entra.group fail 'The recorded group is absent.' }
} else {
    $resourceGroup = az group show --subscription $SubscriptionId --name $state.resourceGroup.name --output json 2>$null | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0 -or -not $resourceGroup) {
        Add-Check context.resource-group fail 'The exact recorded resource group is absent.'
    } elseif ($resourceGroup.id -ne $state.resourceGroup.id) {
        Add-Check context.resource-group fail 'The resource-group ID differs from the manifest.'
    } else {
        Add-Check context.resource-group pass 'The exact recorded resource group exists.'
    }
    if ($resourceGroup.tags.purpose -eq 'az104-lab' -and $resourceGroup.tags.labId -eq '01' -and $resourceGroup.tags.runId -eq $RunId) {
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
$output = [ordered]@{ labId = 'LAB-01'; runId = $RunId; generatedAt = (Get-Date).ToUniversalTime().ToString('o'); result = $result; checks = @($checks) }
$output | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Report -Encoding utf8
$output | ConvertTo-Json -Depth 20
if ($result -eq 'fail') { exit 1 }
```

### Cleanup: `scripts/cli/Cleanup.ps1`

```powershell
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Lifecycle scripts keep one consistent interface across all labs.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Shared safe-naming variables are retained for a consistent learner path.')]
param(
    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [switch]$Execute
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Install it, run az login deliberately, and retry.'
}

$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$Manifest = Join-Path $LabRoot ".state/$RunId/run.json"
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Missing state: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
if ($account.id -ne $SubscriptionId -or $state.subscriptionId -ne $SubscriptionId) { throw 'Active or recorded subscription mismatch.' }
Write-Host 'Cleanup preview for LAB-01'
Write-Host '  exact target scope: tenant objects'
Write-Host ($state | ConvertTo-Json -Depth 6 -Compress)
Write-Host '  residual and soft-delete behavior must be audited after deletion.'
if (-not $Execute) { Write-Host 'Preview only. Re-run with -Execute after checking every target.'; return }

foreach ($userId in @($state.external.userIds)) { az rest --method delete --url "https://graph.microsoft.com/v1.0/users/$userId" --output none 2>$null }
if ($state.external.groupId) { az rest --method delete --url "https://graph.microsoft.com/v1.0/groups/$($state.external.groupId)" --output none 2>$null }

$state.status = 'cleanup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host 'Cleanup completed for the exact recorded boundary. Audit retained or soft-deleted items separately.'
```

<!-- END GENERATED INLINE COMMANDS -->
## Run the lab

Set values for your sandbox, then invoke the lifecycle scripts. For Labs 01 and 02, also read the environment-variable gates embedded in `Setup.ps1`.

```powershell
$subscriptionId = '<subscription-id>'
$location = '<region>'
$runId = 'az104l01-01'

pwsh ./scripts/cli/Preflight.ps1 -SubscriptionId $subscriptionId -Location $location
pwsh ./scripts/cli/Setup.ps1 -SubscriptionId $subscriptionId -Location $location -RunId $runId
pwsh ./scripts/cli/Setup.ps1 -SubscriptionId $subscriptionId -Location $location -RunId $runId -Execute
pwsh ./scripts/cli/Validate.ps1 -SubscriptionId $subscriptionId -RunId $runId
```

## Break/fix exercise

Pass a different subscription ID to validation. Confirm that the script refuses the mismatched context without changing it, then rerun with the correct ID and inspect `validation.json`.

## Cleanup

```powershell
pwsh ./scripts/cli/Cleanup.ps1 -SubscriptionId $subscriptionId -RunId $runId
pwsh ./scripts/cli/Cleanup.ps1 -SubscriptionId $subscriptionId -RunId $runId -Execute
```

Confirm that the exact recorded active resources or tenant objects are absent. Review service-specific soft-delete retention separately.

## Exam practice

Complete [assessment/QUESTIONS.md](assessment/QUESTIONS.md), then review [assessment/ANSWERS.md](assessment/ANSWERS.md).
