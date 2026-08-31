
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
$ResourceGroupName = $(if ('27' -in @('00', '01', '02')) { $null } else { "rg-az104-l27-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-27 execution plan'
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
    labId = 'LAB-27'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB27-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB27-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB27-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB27-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB27-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '27'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB27-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=27 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB27-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB27-CP01'
}

# CHECKPOINT LAB27-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB27-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB27-CP01'
    Save-RunState

    az provider show --namespace Microsoft.Insights --query registrationState --output tsv
    az provider show --namespace Microsoft.RecoveryServices --query registrationState --output tsv
    az vm list-skus --location $Location --size Standard_B1s --all --query "[?name=='Standard_B1s'].name" --output tsv
    if (-not (Get-Command ssh-keygen -ErrorAction SilentlyContinue)) { throw 'ssh-keygen is required for the workload key.' }

    Sync-ManagedResource -CheckpointId 'LAB27-CP01'
    Write-CheckpointState -CheckpointId 'LAB27-CP01' -Status 'pass' -Message 'VM, Network Watcher, Monitor, Storage, and Recovery Services capabilities are available for the selected region and SKU.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB27-CP01'
    Write-CheckpointState -CheckpointId 'LAB27-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB27-CP01 END

# CHECKPOINT LAB27-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB27-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB27-CP02'
    Save-RunState

    $workspace = "law-$suffix"; $vault = "rsv-$suffix"; $vnet = "vnet-$suffix"; $nsg = "nsg-$suffix"; $vm = "vm-$suffix"; $storage = "st27$suffix"; $actionGroup = "ag-$suffix"; $alert = "alert-$suffix"
    $keyPath = Join-Path $StateDir 'id_ed25519'; ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
    try {
        az monitor log-analytics workspace create --resource-group $ResourceGroupName --workspace-name $workspace --location $Location --retention-time 30 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    }
    try {
        az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    }
    try {
        az network nsg create --resource-group $ResourceGroupName --name $nsg --location $Location --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    }
    try {
        az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.27.0.0/16 --subnet-name workload --subnet-prefixes 10.27.1.0/24 --network-security-group $nsg --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    }
    try {
        az network nic create --resource-group $ResourceGroupName --name "nic-$suffix" --vnet-name $vnet --subnet workload --network-security-group $nsg --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    }
    try {
        az vm create --resource-group $ResourceGroupName --name $vm --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --nics "nic-$suffix" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    }
    try {
        az backup vault create --resource-group $ResourceGroupName --name $vault --location $Location --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    }

    Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    Write-CheckpointState -CheckpointId 'LAB27-CP02' -Status 'pass' -Message 'The private VM, storage account, workspace, vault, and network-security boundary are recorded immediately after creation.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB27-CP02'
    Write-CheckpointState -CheckpointId 'LAB27-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB27-CP02 END

# CHECKPOINT LAB27-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB27-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB27-CP03'
    Save-RunState

    $storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
    $workspaceId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query id --output tsv
    $metricCategories = az monitor diagnostic-settings categories list --resource $storageId --query "value[?categoryType=='Metrics'].name" --output tsv
    $metricArgs = @($metricCategories | ForEach-Object { @{ category = $_; enabled = $true } }) | ConvertTo-Json -Compress
    try {
        az monitor diagnostic-settings create --name "diag-$RunId" --resource $storageId --workspace $workspaceId --metrics $metricArgs --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP03'
    }
    try {
        az monitor action-group create --resource-group $ResourceGroupName --name $actionGroup --short-name AZ104 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP03'
    }
    $actionGroupId = az monitor action-group show --resource-group $ResourceGroupName --name $actionGroup --query id --output tsv
    try {
        az monitor metrics alert create --resource-group $ResourceGroupName --name $alert --scopes $storageId --condition 'total Transactions > 0' --window-size 15m --evaluation-frequency 5m --action $actionGroupId --description 'AZ-104 operated workload transaction signal' --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP03'
    }
    $oldStorageKey = $env:AZURE_STORAGE_KEY
    try {
        $env:AZURE_STORAGE_KEY = az storage account keys list --resource-group $ResourceGroupName --account-name $storage --query "[0].value" --output tsv
    try {
            az storage container create --account-name $storage --name operations --auth-mode key --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB27-CP03'
    }
        az storage blob list --account-name $storage --container-name operations --auth-mode key --output none
    } finally {
        if ($null -eq $oldStorageKey) { Remove-Item Env:AZURE_STORAGE_KEY -ErrorAction SilentlyContinue } else { $env:AZURE_STORAGE_KEY = $oldStorageKey }
        Remove-Variable oldStorageKey -ErrorAction SilentlyContinue
    }

    Sync-ManagedResource -CheckpointId 'LAB27-CP03'
    Write-CheckpointState -CheckpointId 'LAB27-CP03' -Status 'pass' -Message 'A deterministic storage transaction is routed to the workspace and the metric alert scopes the exact storage resource.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB27-CP03'
    Write-CheckpointState -CheckpointId 'LAB27-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB27-CP03 END

# CHECKPOINT LAB27-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB27-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB27-CP04'
    Save-RunState

    az backup protection enable-for-vm --resource-group $ResourceGroupName --vault-name $vault --vm $vm --policy-name DefaultPolicy --output none
    $retainUntil = (Get-Date).ToUniversalTime().AddDays(7).ToString('dd-MM-yyyy')
    $backupJob = az backup protection backup-now --resource-group $ResourceGroupName --vault-name $vault --container-name $vm --item-name $vm --backup-management-type AzureIaasVM --retain-until $retainUntil --query name --output tsv
    az backup job wait --resource-group $ResourceGroupName --vault-name $vault --name $backupJob --timeout 3600
    $recoveryPoint = az backup recoverypoint list --resource-group $ResourceGroupName --vault-name $vault --container-name $vm --item-name $vm --backup-management-type AzureIaasVM --query "[0].name" --output tsv
    $restoreJob = az backup restore restore-disks --resource-group $ResourceGroupName --vault-name $vault --container-name $vm --item-name $vm --rp-name $recoveryPoint --storage-account $storage --target-resource-group $ResourceGroupName --restore-to-staging-storage-account true --query name --output tsv
    az backup job wait --resource-group $ResourceGroupName --vault-name $vault --name $restoreJob --timeout 3600

    Sync-ManagedResource -CheckpointId 'LAB27-CP04'
    Write-CheckpointState -CheckpointId 'LAB27-CP04' -Status 'pass' -Message 'The deny rule produces the documented effective-security symptom, diagnosis identifies its priority, and repair restores the prior path.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB27-CP04'
    Write-CheckpointState -CheckpointId 'LAB27-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB27-CP04 END

# CHECKPOINT LAB27-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB27-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB27-CP05'
    Save-RunState

    $workspaceCustomerId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query customerId --output tsv
    $deadline = (Get-Date).AddMinutes(15)
    do {
        $metricRows = az monitor log-analytics query --workspace $workspaceCustomerId --analytics-query "AzureMetrics | where TimeGenerated > ago(30m) | where ResourceId =~ '$storageId' | where MetricName == 'Transactions' | count" --query "tables[0].rows[0][0]" --output tsv
        if ([int]$metricRows -lt 1) { Start-Sleep -Seconds 30 }
    } until ([int]$metricRows -ge 1 -or (Get-Date) -gt $deadline)
    if ([int]$metricRows -lt 1) { throw 'No transaction metric reached AzureMetrics within the bounded ingestion wait.' }
    az network nic list-effective-nsg --resource-group $ResourceGroupName --name "nic-$suffix" --output json

    Sync-ManagedResource -CheckpointId 'LAB27-CP05'
    Write-CheckpointState -CheckpointId 'LAB27-CP05' -Status 'pass' -Message 'The backup and disk-restore jobs complete, telemetry remains queryable, effective networking is healthy, and cleanup honors soft-delete retention.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB27-CP05'
    Write-CheckpointState -CheckpointId 'LAB27-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB27-CP05 END

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
