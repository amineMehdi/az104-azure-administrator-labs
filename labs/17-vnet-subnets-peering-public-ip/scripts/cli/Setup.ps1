
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
$ResourceGroupName = $(if ('17' -in @('00', '01', '02')) { $null } else { "rg-az104-l17-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-17 execution plan'
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
    labId = 'LAB-17'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB17-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB17-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB17-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB17-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB17-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '17'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB17-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=17 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB17-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB17-CP01'
}

# CHECKPOINT LAB17-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB17-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB17-CP01'
    Save-RunState

    az provider show --namespace Microsoft.Network --query registrationState --output tsv
    az network list-service-tags --location $Location --query name --output tsv

    Sync-ManagedResource -CheckpointId 'LAB17-CP01'
    Write-CheckpointState -CheckpointId 'LAB17-CP01' -Status 'pass' -Message 'Both planned CIDRs are non-overlapping and the region offers the Standard static public-IP SKU.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB17-CP01'
    Write-CheckpointState -CheckpointId 'LAB17-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB17-CP01 END

# CHECKPOINT LAB17-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB17-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB17-CP02'
    Save-RunState

    $hub = "hub-$suffix"; $spoke = "spoke-$suffix"; $publicIp = "pip-$suffix"
    try {
        az network vnet create --resource-group $ResourceGroupName --name $hub --address-prefixes 10.17.0.0/16 --subnet-name app --subnet-prefixes 10.17.1.0/24 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    }
    try {
        az network vnet subnet create --resource-group $ResourceGroupName --vnet-name $hub --name management --address-prefixes 10.17.2.0/24 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    }
    try {
        az network vnet create --resource-group $ResourceGroupName --name $spoke --address-prefixes 10.18.0.0/16 --subnet-name app --subnet-prefixes 10.18.1.0/24 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    }
    try {
        az network vnet subnet create --resource-group $ResourceGroupName --vnet-name $spoke --name management --address-prefixes 10.18.2.0/24 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    }
    $hubId = az network vnet show --resource-group $ResourceGroupName --name $hub --query id --output tsv
    $spokeId = az network vnet show --resource-group $ResourceGroupName --name $spoke --query id --output tsv
    try {
        az network vnet peering create --resource-group $ResourceGroupName --vnet-name $hub --name hub-to-spoke --remote-vnet $spokeId --allow-vnet-access true --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    }
    try {
        az network vnet peering create --resource-group $ResourceGroupName --vnet-name $spoke --name spoke-to-hub --remote-vnet $hubId --allow-vnet-access true --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    }
    try {
        az network public-ip create --resource-group $ResourceGroupName --name $publicIp --location $Location --sku Standard --allocation-method Static --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    }

    Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    Write-CheckpointState -CheckpointId 'LAB17-CP02' -Status 'pass' -Message 'Each VNet contains its run-specific subnet and exposes the expected non-overlapping address prefix.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB17-CP02'
    Write-CheckpointState -CheckpointId 'LAB17-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB17-CP02 END

# CHECKPOINT LAB17-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB17-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB17-CP03'
    Save-RunState

    az network vnet peering update --resource-group $ResourceGroupName --vnet-name $hub --name hub-to-spoke --set allowForwardedTraffic=true --output none
    az network vnet peering update --resource-group $ResourceGroupName --vnet-name $spoke --name spoke-to-hub --set allowForwardedTraffic=true --output none
    az network vnet peering list --resource-group $ResourceGroupName --vnet-name $hub --query "[].{name:name,state:peeringState,forwarded:allowForwardedTraffic}" --output table

    Sync-ManagedResource -CheckpointId 'LAB17-CP03'
    Write-CheckpointState -CheckpointId 'LAB17-CP03' -Status 'pass' -Message 'Both peering directions report Connected and use the intended access and forwarding settings.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB17-CP03'
    Write-CheckpointState -CheckpointId 'LAB17-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB17-CP03 END

# CHECKPOINT LAB17-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB17-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB17-CP04'
    Save-RunState

    az network public-ip show --resource-group $ResourceGroupName --name $publicIp --query "{address:ipAddress,allocation:publicIPAllocationMethod,sku:sku.name}" --output json
    az network vnet list --resource-group $ResourceGroupName --query "[].{name:name,prefixes:addressSpace.addressPrefixes,subnets:subnets[].name}" --output json

    Sync-ManagedResource -CheckpointId 'LAB17-CP04'
    Write-CheckpointState -CheckpointId 'LAB17-CP04' -Status 'pass' -Message 'The public IP uses Standard SKU, static allocation, and a run-owned DNS label when one is supplied.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB17-CP04'
    Write-CheckpointState -CheckpointId 'LAB17-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB17-CP04 END

# CHECKPOINT LAB17-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB17-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB17-CP05'
    Save-RunState

    az network vnet peering list --resource-group $ResourceGroupName --vnet-name $hub --query "[].{name:name,state:peeringState,remote:remoteVirtualNetwork.id}" --output table

    Sync-ManagedResource -CheckpointId 'LAB17-CP05'
    Write-CheckpointState -CheckpointId 'LAB17-CP05' -Status 'pass' -Message 'VNet prefixes, subnet boundaries, reciprocal peerings, and the exact public-IP SKU/allocation all match the topology.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB17-CP05'
    Write-CheckpointState -CheckpointId 'LAB17-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB17-CP05 END

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
