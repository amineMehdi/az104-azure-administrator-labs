
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
$ResourceGroupName = $(if ('21' -in @('00', '01', '02')) { $null } else { "rg-az104-l21-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-21 execution plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  command surface: Azure CLI hosted in PowerShell'
Write-Host '  state: run.json, validation.json, cleanup.json'
if (-not $Execute) {
    Write-Host 'Preview only. Review context, inputs, cost, tenant scope, and cleanup before using -Execute.'
    return
}
if ($true -and -not $AcknowledgeCost) { throw 'This lab requires -AcknowledgeCost before execution.' }
if ($false -and -not $AcknowledgeTenantChange) { throw 'This lab requires -AcknowledgeTenantChange before execution.' }

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -RunId $RunId -Location $Location -SecondaryLocation $SecondaryLocation
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest. Choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
$now = (Get-Date).ToUniversalTime().ToString('o')
$state = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-21'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB21-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB21-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB21-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB21-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB21-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '21'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB21-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=21 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB21-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB21-CP01'
}

# CHECKPOINT LAB21-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB21-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB21-CP01'
    Save-RunState

    az provider show --namespace Microsoft.Network --query registrationState --output tsv
    az provider show --namespace Microsoft.Compute --query registrationState --output tsv
    az network watcher list --query "[?location=='$Location'].{name:name,resourceGroup:resourceGroup}" --output table

    Sync-ManagedResource -CheckpointId 'LAB21-CP01'
    Write-CheckpointState -CheckpointId 'LAB21-CP01' -Status 'pass' -Message 'The Standard load-balancer SKU and Network Watcher diagnostic commands are available in the selected region.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB21-CP01'
    Write-CheckpointState -CheckpointId 'LAB21-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB21-CP01 END

# CHECKPOINT LAB21-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB21-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB21-CP02'
    Save-RunState

    $vnet = "vnet-$suffix"; $publicIp = "pip-$suffix"; $loadBalancer = "lb-$suffix"; $nsg = "nsg-$suffix"; $vm1 = "vm-1-$suffix"; $vm2 = "vm-2-$suffix"
    $keyPath = Join-Path $StateDir 'id_ed25519'
    ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
    try {
        az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.21.0.0/16 --subnet-name backend --subnet-prefixes 10.21.1.0/24 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP02'
    }
    try {
        az network public-ip create --resource-group $ResourceGroupName --name $publicIp --location $Location --sku Standard --allocation-method Static --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP02'
    }
    try {
        az network lb create --resource-group $ResourceGroupName --name $loadBalancer --sku Standard --public-ip-address $publicIp --frontend-ip-name frontend --backend-pool-name backend --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP02'
    }
    try {
        az network lb probe create --resource-group $ResourceGroupName --lb-name $loadBalancer --name ssh --protocol Tcp --port 22 --interval 15 --threshold 2 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP02'
    }
    try {
        az network lb rule create --resource-group $ResourceGroupName --lb-name $loadBalancer --name ssh --protocol Tcp --frontend-port 2222 --backend-port 22 --frontend-ip-name frontend --backend-pool-name backend --probe-name ssh --idle-timeout 4 --disable-outbound-snat true --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP02'
    }
    try {
        az network lb outbound-rule create --resource-group $ResourceGroupName --lb-name $loadBalancer --name outbound --frontend-ip-configs frontend --address-pool backend --protocol All --outbound-ports 1024 --idle-timeout 4 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP02'
    }

    Sync-ManagedResource -CheckpointId 'LAB21-CP02'
    Write-CheckpointState -CheckpointId 'LAB21-CP02' -Status 'pass' -Message 'Both backend NICs join the pool and the frontend, health probe, and rule reference one consistent load-balancer resource.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB21-CP02'
    Write-CheckpointState -CheckpointId 'LAB21-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB21-CP02 END

# CHECKPOINT LAB21-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB21-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB21-CP03'
    Save-RunState

    try {
        az network nsg create --resource-group $ResourceGroupName --name $nsg --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    }
    try {
        az network nsg rule create --resource-group $ResourceGroupName --nsg-name $nsg --name AllowLoadBalancerProbe --priority 200 --direction Inbound --access Allow --protocol Tcp --source-address-prefixes AzureLoadBalancer --destination-port-ranges 22 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    }
    try {
        az network nsg rule create --resource-group $ResourceGroupName --nsg-name $nsg --name AllowFrontendSsh --priority 210 --direction Inbound --access Allow --protocol Tcp --source-address-prefixes Internet --destination-port-ranges 22 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    }
    try {
        az network nic create --resource-group $ResourceGroupName --name "nic-1-$suffix" --vnet-name $vnet --subnet backend --network-security-group $nsg --lb-name $loadBalancer --lb-address-pools backend --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    }
    try {
        az network nic create --resource-group $ResourceGroupName --name "nic-2-$suffix" --vnet-name $vnet --subnet backend --network-security-group $nsg --lb-name $loadBalancer --lb-address-pools backend --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    }
    try {
        az vm create --resource-group $ResourceGroupName --name $vm1 --nics "nic-1-$suffix" --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    }
    try {
        az vm create --resource-group $ResourceGroupName --name $vm2 --nics "nic-2-$suffix" --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    }

    Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    Write-CheckpointState -CheckpointId 'LAB21-CP03' -Status 'pass' -Message 'The TCP probe and load-balancing rule share the intended ports, backend pool, and idle-timeout behavior.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB21-CP03'
    Write-CheckpointState -CheckpointId 'LAB21-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB21-CP03 END

# CHECKPOINT LAB21-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB21-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB21-CP04'
    Save-RunState

    $vm1Id = az vm show --resource-group $ResourceGroupName --name $vm1 --query id --output tsv
    $vm2Id = az vm show --resource-group $ResourceGroupName --name $vm2 --query id --output tsv
    foreach ($vmName in @($vm1, $vm2)) {
        az vm extension set --resource-group $ResourceGroupName --vm-name $vmName --publisher Microsoft.Azure.NetworkWatcher --name NetworkWatcherAgentLinux --enable-auto-upgrade true --output none
        $extensionState = az vm extension show --resource-group $ResourceGroupName --vm-name $vmName --name NetworkWatcherAgentLinux --query provisioningState --output tsv
        if ($extensionState -ne 'Succeeded') { throw "Network Watcher agent on $vmName is $extensionState." }
    }
    $watcher = az network watcher list --query "[?location=='$Location'] | [0]" --output json | ConvertFrom-Json
    if (-not $watcher) { throw 'No Network Watcher exists in the selected region.' }
    $external.networkWatcherId = [string]$watcher.id
    $external.networkWatcherName = [string]$watcher.name
    $external.networkWatcherResourceGroup = [string]$watcher.resourceGroup
    $external.connectionMonitorName = "cm-$suffix"
    try {
        $external.connectionMonitorId = az network watcher connection-monitor create --location $Location --name $external.connectionMonitorName --endpoint-source-name source-vm --endpoint-source-resource-id $vm1Id --endpoint-source-type AzureVM --endpoint-dest-name destination-vm --endpoint-dest-resource-id $vm2Id --endpoint-dest-type AzureVM --test-config-name ssh-tcp --protocol Tcp --tcp-port 22 --frequency 60 --test-group-name backend-ssh --tags purpose=az104-lab labId=21 runId=$RunId --query id --output tsv
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB21-CP04'
    }
    $vm2Address = az vm list-ip-addresses --resource-group $ResourceGroupName --name $vm2 --query "[0].virtualMachine.network.privateIpAddresses[0]" --output tsv
    az network watcher test-connectivity --resource-group $ResourceGroupName --source-resource $vm1 --dest-address $vm2Address --dest-port 22 --protocol Tcp --output json

    Sync-ManagedResource -CheckpointId 'LAB21-CP04'
    Write-CheckpointState -CheckpointId 'LAB21-CP04' -Status 'pass' -Message 'IP-flow, next-hop, or connection-troubleshoot evidence identifies the effective network decision without relying on an unavailable public path.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB21-CP04'
    Write-CheckpointState -CheckpointId 'LAB21-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB21-CP04 END

# CHECKPOINT LAB21-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB21-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB21-CP05'
    Save-RunState

    az network lb show --resource-group $ResourceGroupName --name $loadBalancer --query "{sku:sku.name,frontend:frontendIPConfigurations[0].name,backendPool:backendAddressPools[0].name,probe:probes[0].port,rule:loadBalancingRules[0].frontendPort}" --output json
    $sourceIp = az vm list-ip-addresses --resource-group $ResourceGroupName --name $vm1 --query "[0].virtualMachine.network.privateIpAddresses[0]" --output tsv
    $destinationIp = az vm list-ip-addresses --resource-group $ResourceGroupName --name $vm2 --query "[0].virtualMachine.network.privateIpAddresses[0]" --output tsv
    az network watcher show-next-hop --resource-group $ResourceGroupName --vm $vm1 --source-ip $sourceIp --dest-ip $destinationIp --output json
    az network watcher connection-monitor show --location $Location --name $external.connectionMonitorName --query "{state:provisioningState,source:endpoints[0].resourceId,destination:endpoints[1].resourceId}" --output json

    Sync-ManagedResource -CheckpointId 'LAB21-CP05'
    Write-CheckpointState -CheckpointId 'LAB21-CP05' -Status 'pass' -Message 'Frontend configuration, backend membership, probe/rule bindings, and diagnostic results all refer to the same run-owned traffic path.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB21-CP05'
    Write-CheckpointState -CheckpointId 'LAB21-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB21-CP05 END

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
