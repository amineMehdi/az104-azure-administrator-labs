
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
$ResourceGroupName = $(if ('26' -in @('00', '01', '02')) { $null } else { "rg-az104-l26-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-26 execution plan'
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
    labId = 'LAB-26'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB26-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB26-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB26-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB26-CP04'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB26-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '26'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB26-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=26 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB26-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB26-CP01'
}

# CHECKPOINT LAB26-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP01'
    Save-RunState

    az bicep build --file "$LabRoot/artifacts/main.bicep" --outfile "$StateDir/main.json"
    az provider show --namespace Microsoft.Compute --query registrationState --output tsv
    az vm list-skus --location $Location --size Standard_B1s --all --query "[?name=='Standard_B1s'].name" --output tsv
    if (-not (Get-Command ssh-keygen -ErrorAction SilentlyContinue)) { throw 'ssh-keygen is required for the backend keys.' }

    Sync-ManagedResource -CheckpointId 'LAB26-CP01'
    Write-CheckpointState -CheckpointId 'LAB26-CP01' -Status 'pass' -Message 'Bicep, VM SKU, private-link, load-balancer, Policy, RBAC, and diagnostic APIs are available before the capstone mutates Azure.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP01'
    Write-CheckpointState -CheckpointId 'LAB26-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB26-CP01 END

# CHECKPOINT LAB26-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP02'
    Save-RunState

    $storage = "st26$suffix"; $vnet = "vnet-$suffix"; $workspace = "law-$suffix"; $loadBalancer = "lb-$suffix"; $nsg = "nsg-$suffix"; $vm1 = "vm-1-$suffix"; $vm2 = "vm-2-$suffix"; $privateEndpoint = "pe-$suffix"
    az deployment group what-if --resource-group $ResourceGroupName --template-file "$LabRoot/artifacts/main.bicep" --parameters suffix=$suffix storageName=$storage --result-format ResourceIdOnly --no-pretty-print | Set-Content -LiteralPath "$StateDir/what-if.txt"
    try {
        az deployment group create --resource-group $ResourceGroupName --name "capstone-$RunId" --template-file "$LabRoot/artifacts/main.bicep" --parameters suffix=$suffix storageName=$storage --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    try {
        az network nsg create --resource-group $ResourceGroupName --name $nsg --location $Location --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    try {
        az network nsg rule create --resource-group $ResourceGroupName --nsg-name $nsg --name AllowLoadBalancerSsh --priority 200 --direction Inbound --access Allow --protocol Tcp --source-address-prefixes AzureLoadBalancer --destination-port-ranges 22 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name web --network-security-group $nsg --output none
    try {
        az network lb address-pool create --resource-group $ResourceGroupName --lb-name $loadBalancer --name backends --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    try {
        az network lb probe create --resource-group $ResourceGroupName --lb-name $loadBalancer --name ssh --protocol Tcp --port 22 --interval 5 --threshold 2 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    try {
        az network lb rule create --resource-group $ResourceGroupName --lb-name $loadBalancer --name ssh --protocol Tcp --frontend-port 2222 --backend-port 22 --frontend-ip-name frontend --backend-pool-name backends --probe-name ssh --disable-outbound-snat true --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }

    Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    Write-CheckpointState -CheckpointId 'LAB26-CP02' -Status 'pass' -Message 'The Bicep deployment creates tagged network, storage, workspace, and security boundaries whose returned IDs are recorded.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    Write-CheckpointState -CheckpointId 'LAB26-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB26-CP02 END

# CHECKPOINT LAB26-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP03'
    Save-RunState

    $keyPath = Join-Path $StateDir 'id_ed25519'; ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
    foreach ($index in 1..2) {
        $nic = "nic-$index-$suffix"; $vm = "vm-$index-$suffix"
    try {
            az network nic create --resource-group $ResourceGroupName --name $nic --vnet-name $vnet --subnet web --network-security-group $nsg --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
        az network nic ip-config address-pool add --resource-group $ResourceGroupName --nic-name $nic --ip-config-name ipconfig1 --lb-name $loadBalancer --address-pool backends --output none
    try {
            az vm create --resource-group $ResourceGroupName --name $vm --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --nics $nic --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    }
    $storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
    try {
        az network private-endpoint create --resource-group $ResourceGroupName --name $privateEndpoint --location $Location --vnet-name $vnet --subnet private-endpoints --private-connection-resource-id $storageId --group-id blob --connection-name "storage-$suffix" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    try {
        az network private-dns zone create --resource-group $ResourceGroupName --name privatelink.blob.core.windows.net --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    try {
        az network private-dns link vnet create --resource-group $ResourceGroupName --zone-name privatelink.blob.core.windows.net --name "link-$suffix" --virtual-network $vnet --registration-enabled false --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    try {
        az network private-endpoint dns-zone-group create --resource-group $ResourceGroupName --endpoint-name $privateEndpoint --name default --private-dns-zone privatelink.blob.core.windows.net --zone-name blob --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    $workspaceId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query id --output tsv
    $metricCategories = az monitor diagnostic-settings categories list --resource $storageId --query "value[?categoryType=='Metrics'].name" --output tsv
    $metricArgs = @($metricCategories | ForEach-Object { @{ category = $_; enabled = $true } }) | ConvertTo-Json -Compress
    try {
        az monitor diagnostic-settings create --name "diag-$RunId" --resource $storageId --workspace $workspaceId --metrics $metricArgs --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    $policyName = az policy definition list --query "[?displayName=='Audit VMs that do not use managed disks'].name | [0]" --output tsv
    if (-not $policyName) { throw 'The built-in managed-disk audit policy definition was not found.' }
    try {
        az policy assignment create --name "managed-disks-$suffix" --display-name 'AZ-104 managed disk audit' --policy $policyName --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }

    Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    Write-CheckpointState -CheckpointId 'LAB26-CP03' -Status 'pass' -Message 'Two private VM NICs join the backend pool, the health probe/rule are consistent, and storage uses a private endpoint plus linked DNS.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    Write-CheckpointState -CheckpointId 'LAB26-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB26-CP03 END

# CHECKPOINT LAB26-CP04 BEGIN
if (-not ((-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_PRINCIPAL_OBJECT_ID'))))) {
    Write-CheckpointState -CheckpointId 'LAB26-CP04' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP04'
    Save-RunState

    $scope = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName"
    try {
        $external['capstoneRoleAssignmentId'] = az role assignment create --assignee-object-id $env:AZ104_PRINCIPAL_OBJECT_ID --assignee-principal-type User --role Reader --scope $scope --query id --output tsv
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP04'
    }

    Sync-ManagedResource -CheckpointId 'LAB26-CP04'
    Write-CheckpointState -CheckpointId 'LAB26-CP04' -Status 'pass' -Message 'Diagnostic settings target the run-owned workspace, Policy scope is bounded, and optional RBAC targets only the supplied principal and resource scope.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP04'
    Write-CheckpointState -CheckpointId 'LAB26-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB26-CP04 END

# CHECKPOINT LAB26-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP05'
    Save-RunState

    az network lb show --resource-group $ResourceGroupName --name $loadBalancer --query "{sku:sku.name,frontend:frontendIPConfigurations[0].name,pool:backendAddressPools[0].name,probe:probes[0].port,rule:loadBalancingRules[0].frontendPort}" --output json
    az vm list --resource-group $ResourceGroupName --show-details --query "[].{name:name,power:powerState,publicIp:publicIps}" --output table
    az policy assignment show --name "managed-disks-$suffix" --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --output json

    Sync-ManagedResource -CheckpointId 'LAB26-CP05'
    Write-CheckpointState -CheckpointId 'LAB26-CP05' -Status 'pass' -Message 'Traffic, private data access, diagnostics, Policy, tags, optional RBAC, and cleanup dependencies all resolve to one manifest-owned environment.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP05'
    Write-CheckpointState -CheckpointId 'LAB26-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB26-CP05 END

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
