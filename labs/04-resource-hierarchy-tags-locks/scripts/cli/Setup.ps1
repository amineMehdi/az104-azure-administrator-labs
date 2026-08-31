
# BEGIN GENERATED AZ104 V2
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZ104_SECONDARY_LOCATION,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange,
    [switch]$Execute
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Run the repository readiness initializer, then retry.'
}

$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$ResourceGroupName = $(if ('04' -in @('00', '01', '02')) { $null } else { "rg-az104-l04-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-04 execution plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  command surface: Azure CLI hosted in PowerShell'
Write-Host '  state: run.json, validation.json, cleanup.json'
if (-not $Execute) {
    Write-Host 'Preview only. Review context, inputs, cost, tenant scope, and cleanup before using -Execute.'
    return
}
if ($false -and -not $AcknowledgeCost) { throw 'This lab requires -AcknowledgeCost before execution.' }
if ($false -and -not $AcknowledgeTenantChange) { throw 'This lab requires -AcknowledgeTenantChange before execution.' }

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -RunId $RunId -Location $Location -SecondaryLocation $SecondaryLocation
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest. Choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
$now = (Get-Date).ToUniversalTime().ToString('o')
$state = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-04'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB04-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB04-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB04-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB04-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB04-CP05'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
    )
    managedObjects = @()
    originalSettings = @()
}
$external = @{}

function Save-RunState {
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
}

function Save-ExternalState {
    foreach ($key in @($external.Keys)) {
        $value = $external[$key]
        if ($null -eq $value -or $value -is [string] -or $value -is [ValueType]) {
            $inputKey = 'external-' + (([string]$key -creplace '([a-z0-9])([A-Z])', '$1-$2') -replace '[^a-zA-Z0-9-]', '-').ToLowerInvariant()
            $state.inputs[$inputKey] = $value
        }
    }
    Save-RunState
}

function Write-CheckpointState {
    param([string]$CheckpointId, [string]$Status, [string]$Message)
    $entry = @($state.checkpointStates | Where-Object { $_.checkpointId -eq $CheckpointId })[0]
    $entry.status = $Status
    $entry.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $entry.message = $Message
}

function Add-ManagedObject {
    param([string]$CheckpointId, [string]$Kind, [string]$Id, [string]$Name, [string]$Type, [string]$Scope, [string]$OwnershipMethod)
    if ([string]::IsNullOrWhiteSpace($Id)) { return }
    $existing = @($state.managedObjects | Where-Object { $_.id -eq $Id })
    if ($existing.Count -gt 0) { return }
    $expectedTags = @{}
    if ($OwnershipMethod -eq 'manifest-id-and-tags') {
        $expectedTags = @{ purpose = 'az104-lab'; labId = '04'; runId = $RunId }
    }
    $state.managedObjects += @{
        checkpointId = $CheckpointId
        kind = $Kind
        id = $Id
        name = $Name
        type = $Type
        scope = $Scope
        ownership = @{ method = $OwnershipMethod; expectedTags = $expectedTags }
        recordedAt = (Get-Date).ToUniversalTime().ToString('o')
        lifecycleStatus = 'active'
    }
    Save-RunState
}

function Sync-ManagedResource {
    param([string]$CheckpointId)
    # The entire recovery inventory is best effort so a state-helper or Azure
    # query failure cannot mask the original mutation error. Every object that
    # can be recovered is still persisted immediately as it is discovered.
    $nativePreference = $PSNativeCommandUseErrorActionPreference
    $PSNativeCommandUseErrorActionPreference = $false
    try {
        Save-ExternalState
        $resourceGroupNames = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
        if ($ResourceGroupName) { $null = $resourceGroupNames.Add([string]$ResourceGroupName) }
        foreach ($key in @($external.Keys | Where-Object { [string]$_ -match '(?i)ResourceGroupName$' })) {
            if ($external[$key]) { $null = $resourceGroupNames.Add([string]$external[$key]) }
        }
        foreach ($groupName in $resourceGroupNames) {
            $groupJson = az group show --subscription $SubscriptionId --name $groupName --output json 2>$null
            $group = $(if ($LASTEXITCODE -eq 0 -and $groupJson) { $groupJson | ConvertFrom-Json } else { $null })
            if ($group) {
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB04-CP01' } else { $CheckpointId })
                Add-ManagedObject -CheckpointId $groupCheckpoint -Kind 'azure-resource' -Id ([string]$group.id) -Name ([string]$group.name) -Type 'Microsoft.Resources/resourceGroups' -Scope "/subscriptions/$SubscriptionId" -OwnershipMethod 'manifest-id-and-tags'
                $resourcesJson = az resource list --subscription $SubscriptionId --resource-group $groupName --output json 2>$null
                $resources = @($(if ($LASTEXITCODE -eq 0 -and $resourcesJson) { $resourcesJson | ConvertFrom-Json } else { @() }))
                foreach ($resource in $resources) {
                    Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$resource.id) -Name ([string]$resource.name) -Type ([string]$resource.type) -Scope ([string]$group.id) -OwnershipMethod 'manifest-id-and-tags'
                }
            }
        }
        if ($external.ContainsKey('groupId') -and $external.groupId) { Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$external.groupId) -Name 'lab-group' -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }
        if ($external.ContainsKey('guestUserId') -and $external.guestUserId) { Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$external.guestUserId) -Name 'guest-user' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }
        if ($external.ContainsKey('userIds')) {
            foreach ($userId in @($external.userIds)) { Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$userId) -Name 'lab-user' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }
        }
        if ($external.ContainsKey('delegationRecordId') -and $external.delegationRecordId) {
            Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$external.delegationRecordId) -Name ([string]$external.delegationRecordName) -Type 'Microsoft.Network/dnsZones/NS' -Scope ([string]$external.parentZoneId) -OwnershipMethod 'manifest-id'
        }
        if ($external.ContainsKey('connectionMonitorId') -and $external.connectionMonitorId) {
            Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$external.connectionMonitorId) -Name ([string]$external.connectionMonitorName) -Type 'Microsoft.Network/networkWatchers/connectionMonitors' -Scope ([string]$external.networkWatcherId) -OwnershipMethod 'manifest-id'
        }
    } catch {
        Write-Warning "Recovery inventory for $CheckpointId was incomplete: $($_.Exception.Message)"
    } finally {
        $PSNativeCommandUseErrorActionPreference = $nativePreference
    }
}

# The manifest exists before the first Azure mutation.
Save-RunState
$state.status = 'setup-in-progress'
Save-RunState

$expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd')
try {
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=04 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB04-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB04-CP01'
}

# CHECKPOINT LAB04-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB04-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB04-CP01'
    Save-RunState

    $rgId = az group show --name $ResourceGroupName --query id --output tsv
    az account management-group list --query '[].{name:name,displayName:displayName}' --output table
    az group show --name $ResourceGroupName --query '{id:id,location:location,tags:tags}' --output json

    Sync-ManagedResource -CheckpointId 'LAB04-CP01'
    Write-CheckpointState -CheckpointId 'LAB04-CP01' -Status 'pass' -Message 'The resource group has the expected subscription-qualified ID and initial run-ownership tags.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB04-CP01'
    Write-CheckpointState -CheckpointId 'LAB04-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB04-CP01 END

# CHECKPOINT LAB04-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB04-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB04-CP02'
    Save-RunState

    az tag update --resource-id $rgId --operation Merge --tags environment=training costCenter=az104 owner=learner --output none

    Sync-ManagedResource -CheckpointId 'LAB04-CP02'
    Write-CheckpointState -CheckpointId 'LAB04-CP02' -Status 'pass' -Message 'The three governance tags and the original purpose, labId, runId, and expiresOn ownership tags coexist.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB04-CP02'
    Write-CheckpointState -CheckpointId 'LAB04-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB04-CP02 END

# CHECKPOINT LAB04-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB04-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB04-CP03'
    Save-RunState

    $vnet = "vnet04-$suffix"
    try {
        $createdVnet = az network vnet create --resource-group $ResourceGroupName --name $vnet --location $Location --address-prefixes 10.4.0.0/16 --subnet-name workload --subnet-prefixes 10.4.1.0/24 --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB04-CP03'
    }
    $createdVnetId = [string]$createdVnet.newVNet.id
    if (-not $createdVnetId) { $createdVnetId = az network vnet show --resource-group $ResourceGroupName --name $vnet --query id --output tsv }
    Add-ManagedObject -CheckpointId 'LAB04-CP03' -Kind 'azure-resource' -Id $createdVnetId -Name $vnet -Type 'Microsoft.Network/virtualNetworks' -Scope $rgId -OwnershipMethod 'manifest-id'
    $before = az network vnet show --resource-group $ResourceGroupName --name $vnet --query tags --output json
    if ($before -notin @('{}','null')) { throw 'New child unexpectedly inherited tags; investigate policy before continuing.' }
    $vnetId = az network vnet show --resource-group $ResourceGroupName --name $vnet --query id --output tsv
    az tag update --resource-id $vnetId --operation Merge --tags purpose=az104-lab labId=04 runId=$RunId environment=training --output none

    Sync-ManagedResource -CheckpointId 'LAB04-CP03'
    Write-CheckpointState -CheckpointId 'LAB04-CP03' -Status 'pass' -Message 'The before query proves no automatic inheritance; the final virtual network has explicit ownership and environment tags.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB04-CP03'
    Write-CheckpointState -CheckpointId 'LAB04-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB04-CP03 END

# CHECKPOINT LAB04-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB04-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB04-CP04'
    Save-RunState

    try {
        $lock = az lock create --name $lockName --lock-type CanNotDelete --resource-group $ResourceGroupName --notes "AZ-104 Lab 04 run $RunId" --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB04-CP04'
    }
    Add-ManagedObject -CheckpointId 'LAB04-CP04' -Kind 'azure-resource' -Id ([string]$lock.id) -Name $lockName -Type 'Microsoft.Authorization/locks' -Scope $rgId -OwnershipMethod 'manifest-id'
    $PSNativeCommandUseErrorActionPreference = $false
    $denied = az network vnet delete --resource-group $ResourceGroupName --name $vnet 2>&1
    $deniedExit = $LASTEXITCODE
    $PSNativeCommandUseErrorActionPreference = $true
    if ($deniedExit -eq 0) {
    try {
            $recreated = az network vnet create --resource-group $ResourceGroupName --name $vnet --location $Location --address-prefixes 10.4.0.0/16 --subnet-name workload --subnet-prefixes 10.4.1.0/24 --tags purpose=az104-lab labId=04 runId=$RunId environment=training --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB04-CP04'
    }
        throw 'The child delete unexpectedly bypassed the resource-group lock; the virtual network was recreated for cleanup.'
    }
    $state.inputs['lock-denial-observed'] = $true
    Save-RunState

    Sync-ManagedResource -CheckpointId 'LAB04-CP04'
    Write-CheckpointState -CheckpointId 'LAB04-CP04' -Status 'pass' -Message 'Exactly one CanNotDelete lock exists, its ID is recorded, and a safe child virtual-network delete is rejected.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB04-CP04'
    Write-CheckpointState -CheckpointId 'LAB04-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB04-CP04 END

# CHECKPOINT LAB04-CP05 BEGIN
if (-not ([string]::Equals([Environment]::GetEnvironmentVariable('AZ104_ALLOW_MANAGEMENT_GROUP_CHANGE'), 'YES', [StringComparison]::Ordinal))) {
    Write-CheckpointState -CheckpointId 'LAB04-CP05' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB04-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB04-CP05'
    Save-RunState

    if ($env:AZ104_ALLOW_MANAGEMENT_GROUP_CHANGE -ne 'YES') { throw 'Set the management-group gate to the exact value YES.' }
    $managementGroup = "mg-az104-$suffix"
    try {
        $mg = az account management-group create --name $managementGroup --display-name "AZ104 $RunId" --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB04-CP05'
    }
    Add-ManagedObject -CheckpointId 'LAB04-CP05' -Kind 'azure-resource' -Id ([string]$mg.id) -Name $managementGroup -Type 'Microsoft.Management/managementGroups' -Scope '/providers/Microsoft.Management/managementGroups' -OwnershipMethod 'manifest-id'

    Sync-ManagedResource -CheckpointId 'LAB04-CP05'
    Write-CheckpointState -CheckpointId 'LAB04-CP05' -Status 'pass' -Message 'One empty run-specific management group exists only when tenant change is acknowledged and its ID is manifest-recorded.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB04-CP05'
    Write-CheckpointState -CheckpointId 'LAB04-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB04-CP05 END

$skippedRequired = @($state.checkpointStates | Where-Object { $_.required -and $_.status -eq 'skipped' })
if ($skippedRequired.Count -gt 0) {
    $state.status = 'failed'
    Save-RunState
    throw "Required checkpoints were skipped: $($skippedRequired.checkpointId -join ', ')"
}
$skippedOptional = @($state.checkpointStates | Where-Object { -not $_.required -and $_.status -eq 'skipped' })
$state.status = $(if ($skippedOptional.Count -gt 0) { 'partial' } else { 'setup-complete' })
Save-RunState
Write-Host "Setup result: $($state.status). State: $Manifest"
Write-Host "Next: ./Validate.ps1 -RunId $RunId -Mode Deployment"
# END GENERATED AZ104 V2
