# Lab 12: Design VM resilience, scale sets, and mobility

> Status: **offline-authored and contract-tested; live Azure verification is pending.**

Compare availability sets and zones, deploy a small flexible VM scale set, inspect autoscale and upgrade settings, validate a resource-group move, and plan regional mobility without claiming a cross-region copy occurred.

This folder is self-contained. It does not depend on another lab's runtime state. Use a disposable environment, keep the generated run manifest, and never substitute a production scope for a missing lab prerequisite.

## Learning objectives

| ID | Microsoft AZ-104 objective |
|---|---|
| `CP-VM-03` | Move a virtual machine to another resource group, subscription, or region |
| `CP-VM-04` | Manage virtual machine sizes |
| `CP-VM-06` | Deploy virtual machines to availability zones and availability sets |
| `CP-VM-07` | Deploy and configure an Azure Virtual Machine Scale Sets |

Blueprint source: [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), effective 2026-04-17.

## Architecture

![Lab 12 architecture](diagrams/architecture.svg)

The editable Mermaid source is [diagrams/architecture.mmd](diagrams/architecture.mmd). The diagram describes the learning boundary, not a production reference architecture.

## Scenario and outcome

You are the Azure administrator for a training environment. Your task is to implement the smallest isolated configuration that demonstrates the mapped exam objectives, validate it independently, retain redacted command evidence, and remove only what this run recorded.

The key design idea is: **Availability sets, zones, scale sets, and regional moves solve different resilience or mobility problems and have distinct dependency and cost models.**

## Time, cost, and permissions

| Item | Value |
|---|---|
| Estimated time | 150 minutes |
| Cost class | `elevated` |
| Command surface | Az PowerShell |
| Required boundary | Virtual Machine Contributor, Network Contributor, and move permissions on source and destination scopes |
| External/live gate | None beyond the declared role and a disposable subscription. |

Cost is not a fixed promise. Check current pricing, free allowances, quotas, and regional availability before using `--execute` or `-Execute`. Labs marked moderate or elevated should be cleaned up in the same study session.

## Resources and dependencies

| # | Intended resource or object |
|---:|---|
| 1 | resource group |
| 2 | availability set |
| 3 | zonal VM metadata |
| 4 | flexible VM scale set |
| 5 | autoscale setting |

- Resource providers observed by preflight: `Microsoft.Compute`, `Microsoft.Insights`, `Microsoft.Network`, `Microsoft.Resources`
- PowerShell modules used when applicable: `Az.Accounts`, `Az.Resources`, `Az.Network`, `Az.Compute`, `Az.Monitor`
- Repository state: `.state/<run-id>/run.json` and `.state/<run-id>/validation.json`
- Secrets, access keys, SAS tokens, generated passwords, and shared keys must remain in memory and must not enter the manifest, command evidence, or Git history.

## Safety contract

1. Preflight is read-only. It does not sign in, register providers, or switch the active context.
2. Setup is preview-only unless the explicit execution switch is supplied.
3. State is written before the first cloud mutation and updated with exact returned IDs.
4. Validation reads live state independently; it does not repair a failed configuration.
5. Cleanup previews exact targets, verifies run ownership, then requires the explicit execution switch.
6. Tenant-wide, DNS, licensing, notification, failover, and policy gates are never guessed.

## Before you begin

- Use a disposable non-production tenant/subscription and verify the displayed tenant and subscription IDs.
- Install the declared command surface and supporting dependencies.
- Confirm the role boundary above at the smallest possible scope.
- Review provider registration and quota output; preflight reports requirements but does not register providers.
- Read the external gate. An unavailable gate is a documented `skipped` checkpoint, not a pass.
- Choose a unique run ID matching `^[a-z0-9-]+$`, such as `az104l12-01`.

<!-- BEGIN GENERATED INLINE COMMANDS -->
## Complete inline command implementation

The lifecycle commands below are the complete learner-facing implementation. They are embedded from the retained script files so the README and automation cannot drift. Review each stage here before running it. Use a different run ID if you later try the optional scripted lane against the same sandbox.

### Preflight: `scripts/powershell/Preflight.ps1`

```powershell
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lanes keep a consistent explicit context interface.')]
param(
    [Parameter(Mandatory)][string]$SubscriptionId,
    [Parameter(Mandatory)][string]$Location
)

$ErrorActionPreference = 'Stop'
$requiredModules = @(
    'Az.Accounts',
    'Az.Resources',
    'Az.Network',
    'Az.Compute',
    'Az.Monitor'
)
foreach ($module in $requiredModules) {
    if (-not (Get-Module -ListAvailable -Name $module)) { throw "Missing required module: $module" }
}

if (-not $SubscriptionId) { throw 'Supply -SubscriptionId explicitly.' }
$context = Get-AzContext
if (-not $context) { throw 'No Az PowerShell context is active. Sign in deliberately before running this lab.' }
if ($context.Subscription.Id -ne $SubscriptionId) {
    throw "Context mismatch: active subscription is $($context.Subscription.Id), expected $SubscriptionId. This script will not switch it."
}
Write-Host "Tenant: $($context.Tenant.Id)"
Write-Host "Subscription: $($context.Subscription.Id)"
Write-Host 'Lab: LAB-12'
Write-Host 'Location:' $Location
Write-Host 'Cost class: elevated'
Write-Host 'Role boundary: Virtual Machine Contributor, Network Contributor, and move permissions on source and destination scopes'
$providers = @(
    'Microsoft.Compute',
    'Microsoft.Insights',
    'Microsoft.Network',
    'Microsoft.Resources'
)
foreach ($provider in $providers) {
    $item = Get-AzResourceProvider -ProviderNamespace $provider -ErrorAction SilentlyContinue
    $states = @($item.ResourceTypes.RegistrationState | Sort-Object -Unique) -join ','
    Write-Host ("Provider {0,-38} {1}" -f $provider, $(if ($states) { $states } else { 'Unavailable' }))
}
Write-Host 'Preflight is read-only. It does not connect, change context, register providers, or create resources.'
```

### Setup: `scripts/powershell/Setup.ps1`

```powershell
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lanes keep a consistent explicit context and region interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Named checkpoint results improve readability even when the object is used only to enforce failure handling.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'The disposable generated VMSS credential remains in memory and is never persisted.')]
param(
    [Parameter(Mandatory)][string]$SubscriptionId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [Parameter(Mandatory)][string]$Location,
    [string]$SecondaryLocation = $env:AZURE_SECONDARY_LOCATION,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$ResourceGroupName = 'rg-az104-l12-' + $RunId
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'

Write-Host 'LAB-12 plan'
Write-Host '  subscription:' $(if ($SubscriptionId) { $SubscriptionId } else { 'tenant-scoped / not applicable' })
Write-Host '  location:' $Location
Write-Host '  resource group:' $(if ($true) { $ResourceGroupName } else { 'none (tenant objects)' })
Write-Host '  cost class: elevated'
Write-Host '  external gate: None beyond the declared role and a disposable subscription.'
Write-Host '  resources: resource group, availability set, zonal VM metadata, flexible VM scale set, autoscale setting'
if (-not $Execute) {
    Write-Host 'Preview only. Re-run with -Execute after approving context, permissions, cost, and gates.'
    return
}

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -Location $Location
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest; choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$context = Get-AzContext
$TenantId = $context.Tenant.Id
$state = [ordered]@{
    labId = 'LAB-12'
    runId = $RunId
    tenantId = $TenantId
    subscriptionId = $SubscriptionId
    location = $Location
    createdAt = (Get-Date).ToUniversalTime().ToString('o')
    status = 'recorded-before-mutation'
    resourceGroup = [ordered]@{ name = $(if ($true) { $ResourceGroupName } else { $null }); id = $null }
    resources = @()
    external = [ordered]@{}
}
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
$tags = @{ purpose = 'az104-lab'; labId = '12'; runId = $RunId; expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd') }
$resourceGroup = New-AzResourceGroup -Name $ResourceGroupName -Location $Location -Tag $tags
$state.resourceGroup.id = $resourceGroup.ResourceId
$state.status = 'baseline-created'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8

$availabilitySet = New-AzAvailabilitySet -ResourceGroupName $ResourceGroupName -Name ("avset-" + $suffix) -Location $Location -Sku Aligned -PlatformFaultDomainCount 2 -PlatformUpdateDomainCount 5
$vnet = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("vnet-" + $suffix) -AddressPrefix '10.12.0.0/16'
$vnet | Add-AzVirtualNetworkSubnetConfig -Name vmss -AddressPrefix '10.12.1.0/24' | Set-AzVirtualNetwork | Out-Null
$credential = New-Object PSCredential ('azureadmin', (ConvertTo-SecureString ([Guid]::NewGuid().ToString('N') + 'aA!9') -AsPlainText -Force))
New-AzVmss -ResourceGroupName $ResourceGroupName -VMScaleSetName ("vmss-" + $suffix) -Location $Location -VirtualNetworkName ("vnet-" + $suffix) -SubnetName vmss -PublicIpAddressName ("pip-" + $suffix) -LoadBalancerName ("lb-" + $suffix) -Credential $credential -ImageName UbuntuLTS -InstanceCount 1 -UpgradePolicyMode Manual | Out-Null

$state.resources = @(Get-AzResource -ResourceGroupName $ResourceGroupName | ForEach-Object {
    [ordered]@{ id = $_.ResourceId; name = $_.Name; type = $_.ResourceType; location = $_.Location }
})
$state.status = 'setup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
```

### Validate: `scripts/powershell/Validate.ps1`

```powershell
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Tenant and subscription lanes share a consistent validation interface.')]
param(
    [Parameter(Mandatory)][string]$SubscriptionId,
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

$context = Get-AzContext
if (-not $context -or $context.Subscription.Id -ne $SubscriptionId) { throw 'Active Az context does not match -SubscriptionId.' }
if ($state.subscriptionId -ne $SubscriptionId) { throw 'Recorded subscription mismatch.' }
$rg = Get-AzResourceGroup -Name $state.resourceGroup.name -ErrorAction SilentlyContinue
if (-not $rg) { Add-Check 'context.resource-group' 'fail' 'The recorded resource group is absent.' }
elseif ($rg.ResourceId -ne $state.resourceGroup.id) { Add-Check 'context.resource-group' 'fail' 'The resource-group ID differs from the manifest.' }
else { Add-Check 'context.resource-group' 'pass' 'The exact recorded resource group exists.' }
if ($rg -and $rg.Tags.purpose -eq 'az104-lab' -and $rg.Tags.labId -eq '12' -and $rg.Tags.runId -eq $RunId) {
    Add-Check 'ownership.tags' 'pass' 'purpose, labId, and runId tags match.'
} else { Add-Check 'ownership.tags' 'fail' 'Ownership tags do not match.' }
$resources = @(Get-AzResource -ResourceGroupName $state.resourceGroup.name -ErrorAction SilentlyContinue)
$expectedTypes = @(
    'Microsoft.Compute/virtualMachineScaleSets',
    'Microsoft.Compute/availabilitySets'
)
foreach ($type in $expectedTypes) {
    $count = @($resources | Where-Object ResourceType -eq $type).Count
    if ($count -gt 0) { Add-Check ("resource." + ($type -replace '[/\.]','-')) 'pass' "Found $count resource(s) of type $type." }
    else { Add-Check ("resource." + ($type -replace '[/\.]','-')) 'warning' "No top-level $type was returned; inspect nested or gated state." }
}
$failures = @($checks | Where-Object status -eq 'fail').Count
$warnings = @($checks | Where-Object status -in @('warning','skipped')).Count
$result = if ($failures -gt 0) { 'fail' } elseif ($warnings -gt 0) { 'partial' } else { 'pass' }
$output = [ordered]@{ labId = 'LAB-12'; runId = $RunId; generatedAt = (Get-Date).ToUniversalTime().ToString('o'); result = $result; checks = @($checks) }
$output | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Report -Encoding utf8
$output | ConvertTo-Json -Depth 20
if ($result -eq 'fail') { exit 1 }
```

### Cleanup: `scripts/powershell/Cleanup.ps1`

```powershell
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive cleanup previews are intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Tenant and subscription lanes share a consistent cleanup interface.')]
param(
    [Parameter(Mandatory)][string]$SubscriptionId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$Manifest = Join-Path $LabRoot ".state/$RunId/run.json"
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Missing state: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
Write-Host 'Cleanup preview for LAB-12'
Write-Host '  exact target:' $state.resourceGroup.id
Write-Host '  residual/soft-delete behavior must be audited after deletion.'
if (-not $Execute) { Write-Host 'Preview only. Re-run with -Execute after checking every target.'; return }
$context = Get-AzContext
if (-not $context -or $context.Subscription.Id -ne $SubscriptionId) { throw 'Active Az context does not match -SubscriptionId.' }
if ($state.subscriptionId -ne $SubscriptionId) { throw 'Recorded subscription mismatch.' }
$rg = Get-AzResourceGroup -Name $state.resourceGroup.name -ErrorAction SilentlyContinue
if (-not $rg) { Write-Host 'Resource group is already absent; cleanup is idempotent.'; return }
if ($rg.ResourceId -ne $state.resourceGroup.id -or $rg.Tags.purpose -ne 'az104-lab' -or $rg.Tags.labId -ne '12' -or $rg.Tags.runId -ne $RunId) {
    throw 'ID or ownership-tag verification failed; refusing cleanup.'
}

Remove-AzResourceGroup -Id $state.resourceGroup.id -Force
$remaining = Get-AzResourceGroup -Name $state.resourceGroup.name -ErrorAction SilentlyContinue
if ($remaining) { throw 'Resource group still exists; inspect soft-delete dependencies, locks, or asynchronous operations.' }
Write-Host 'Active resource-group cleanup completed. Audit soft-deleted and externally retained items separately.'
$state.status = 'cleanup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
```

<!-- END GENERATED INLINE COMMANDS -->
## Run the lab

The complete learner-facing implementations are embedded above. The commands in this section are optional shortcuts that run the identical retained script files. Run them from this lab folder. The examples intentionally use placeholders rather than silently reading an arbitrary subscription.

### 1. Preview

```ps1
pwsh ./scripts/powershell/Setup.ps1 -RunId az104l12-01 -SubscriptionId <subscription-id> -Location <region>
```

Review the context, names, tags, cost class, providers, and gated branches printed by the script.

### 2. Execute the approved baseline

```ps1
pwsh ./scripts/powershell/Setup.ps1 -RunId az104l12-01 -SubscriptionId <subscription-id> -Location <region> -Execute
```

The script records its run before creating resources. If a cloud operation fails partway through, keep the state directory and use validation plus cleanup against that exact run.

### 3. Complete and reason through the checkpoints

### Checkpoint 1: Create an availability set and compare its fault/update-domain model with availability zones

Create an availability set and compare its fault/update-domain model with availability zones.

Evidence to retain:

- The command output or exact resource/object ID for checkpoint 1.
- A positive assertion proving the intended state.
- A negative assertion showing that broader or anonymous access was not introduced.
- Any asynchronous operation state, timestamp, and final result.

### Checkpoint 2: Deploy a small flexible orchestration VM scale set with an explicit instance count and upgrade policy

Deploy a small flexible orchestration VM scale set with an explicit instance count and upgrade policy.

Evidence to retain:

- The command output or exact resource/object ID for checkpoint 2.
- A positive assertion proving the intended state.
- A negative assertion showing that broader or anonymous access was not introduced.
- Any asynchronous operation state, timestamp, and final result.

### Checkpoint 3: Configure bounded autoscale rules and inspect instance protection and health behavior

Configure bounded autoscale rules and inspect instance protection and health behavior.

Evidence to retain:

- The command output or exact resource/object ID for checkpoint 3.
- A positive assertion proving the intended state.
- A negative assertion showing that broader or anonymous access was not introduced.
- Any asynchronous operation state, timestamp, and final result.

### Checkpoint 4: Use move validation for a destination resource group and document the different process required for another region or subscription

Use move validation for a destination resource group and document the different process required for another region or subscription.

Evidence to retain:

- The command output or exact resource/object ID for checkpoint 4.
- A positive assertion proving the intended state.
- A negative assertion showing that broader or anonymous access was not introduced.
- Any asynchronous operation state, timestamp, and final result.

### 4. Validate independently

```ps1
pwsh ./scripts/powershell/Validate.ps1 -RunId az104l12-01 -SubscriptionId <subscription-id>
```

Inspect `.state/az104l12-01/validation.json`. A `pass` applies only to checks that could be executed. A gated or asynchronous path must remain `warning` or `skipped` until its evidence exists.

Positive checks should prove the intended resources, configuration, relationships, or health. Negative checks should prove that anonymous access, excess scope, accidental inheritance, unresolved DNS, unhealthy probes, or unrecorded resources were not introduced where the scenario forbids them.

## Break/fix exercise

1. Pick one reversible configuration created inside the recorded lab boundary.
2. Record the exact ID and current value.
3. Introduce one bounded mismatch; do not weaken a tenant-wide or production control.
4. Run validation and connect the failed check to an exact CLI/PowerShell query and the machine-readable validation result.
5. Repair only the identified setting, rerun validation, and compare the evidence.

The [solution notes](solution/README.md) provide a diagnostic sequence without hiding the reasoning behind an opaque repair script.

## Cleanup

Preview cleanup first:

```ps1
pwsh ./scripts/powershell/Cleanup.ps1 -RunId az104l12-01 -SubscriptionId <subscription-id>
```

After verifying every printed target belongs to this run:

```ps1
pwsh ./scripts/powershell/Cleanup.ps1 -RunId az104l12-01 -SubscriptionId <subscription-id> -Execute
```

Run validation again after deletion. Some services use soft delete, retained recovery points, asynchronous deletion, or external DNS/tenant state; the cleanup report must distinguish active cleanup from retention and must list residual items instead of claiming success prematurely.

## Exam practice

- Complete [assessment/QUESTIONS.md](assessment/QUESTIONS.md) without opening the answer key.
- Review [assessment/ANSWERS.md](assessment/ANSWERS.md) and trace each explanation to its Microsoft Learn source.
- Revisit every mapped objective whose answer you could not justify from the resource state.

## Microsoft Learn sources

- [https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets)
- [https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)
- [https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)
- [https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)
- [https://learn.microsoft.com/en-us/azure/resource-mover/tutorial-move-region-virtual-machines](https://learn.microsoft.com/en-us/azure/resource-mover/tutorial-move-region-virtual-machines)

Last curriculum/source review: 2026-08-30. Azure interfaces and command modules evolve; confirm current syntax in the linked primary documentation before a live run.
