
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
$ResourceGroupName = $(if ('08' -in @('00', '01', '02')) { $null } else { "rg-az104-l08-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-08 execution plan'
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
    labId = 'LAB-08'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB08-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB08-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB08-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB08-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB08-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '08'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB08-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=08 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB08-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB08-CP01'
}

# CHECKPOINT LAB08-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB08-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB08-CP01'
    Save-RunState

    if (-not (Get-Command azcopy -ErrorAction SilentlyContinue)) { throw 'AzCopy v10 is required.' }
    $learnerId = az ad signed-in-user show --query id --output tsv
    if (-not $learnerId) { throw 'Use an interactive Entra user for the Azure CLI backed AzCopy path.' }
    $state.inputs['learner-object-id'] = $learnerId
    Save-RunState
    azcopy --version

    Sync-ManagedResource -CheckpointId 'LAB08-CP01'
    Write-CheckpointState -CheckpointId 'LAB08-CP01' -Status 'pass' -Message 'AzCopy v10 and an interactive learner object ID are available before any storage account is created.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB08-CP01'
    Write-CheckpointState -CheckpointId 'LAB08-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB08-CP01 END

# CHECKPOINT LAB08-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB08-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB08-CP02'
    Save-RunState

    $source = "st08a$suffix"; $destination = "st08b$suffix"
    foreach ($account in @($source,$destination)) {
    try {
            $created = az storage account create --name $account --resource-group $ResourceGroupName --location $Location --kind StorageV2 --sku Standard_LRS --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --allow-cross-tenant-replication false --tags purpose=az104-lab labId=08 runId=$RunId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB08-CP02'
    }
        Add-ManagedObject -CheckpointId 'LAB08-CP02' -Kind 'azure-resource' -Id ([string]$created.id) -Name $account -Type 'Microsoft.Storage/storageAccounts' -Scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" -OwnershipMethod 'manifest-id-and-tags'
        az storage account blob-service-properties update --account-name $account --resource-group $ResourceGroupName --enable-change-feed true --enable-delete-retention true --delete-retention-days 7 --enable-container-delete-retention true --container-delete-retention-days 7 --output none
    try {
            $assignment = az role assignment create --assignee-object-id $state.inputs['learner-object-id'] --assignee-principal-type User --role 'Storage Blob Data Contributor' --scope $created.id --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB08-CP02'
    }
        Add-ManagedObject -CheckpointId 'LAB08-CP02' -Kind 'azure-resource' -Id ([string]$assignment.id) -Name "BlobContributor-$account" -Type 'Microsoft.Authorization/roleAssignments' -Scope ([string]$created.id) -OwnershipMethod 'manifest-id'
    }
    az storage account blob-service-properties update --account-name $source --resource-group $ResourceGroupName --enable-versioning true --output none
    az storage account blob-service-properties update --account-name $destination --resource-group $ResourceGroupName --enable-versioning false --output none
    try {
        az storage container create --name source --account-name $source --auth-mode login --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB08-CP02'
    }
    try {
        az storage container create --name destination --account-name $destination --auth-mode login --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB08-CP02'
    }
    $policyPath = Join-Path $StateDir 'lifecycle-policy.json'
    @{ rules = @(@{ enabled = $true; name = 'tier-and-expire-versions'; type = 'Lifecycle'; definition = @{ actions = @{ baseBlob = @{ tierToCool = @{ daysAfterModificationGreaterThan = 30 } }; version = @{ delete = @{ daysAfterCreationGreaterThan = 45 } } }; filters = @{ blobTypes = @('blockBlob') } } }) } | ConvertTo-Json -Depth 15 | Set-Content -LiteralPath $policyPath -Encoding utf8
    try {
        az storage account management-policy create --account-name $source --resource-group $ResourceGroupName --policy "@$policyPath" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB08-CP02'
    }

    Sync-ManagedResource -CheckpointId 'LAB08-CP02'
    Write-CheckpointState -CheckpointId 'LAB08-CP02' -Status 'pass' -Message 'Both accounts have change feed and soft delete; source versioning is on, destination versioning is intentionally off for the next break/fix, and lifecycle manages base blobs and versions.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB08-CP02'
    Write-CheckpointState -CheckpointId 'LAB08-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB08-CP02 END

# CHECKPOINT LAB08-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB08-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB08-CP03'
    Save-RunState

    $sourceId = az storage account show --resource-group $ResourceGroupName --name $source --query id --output tsv
    $destinationId = az storage account show --resource-group $ResourceGroupName --name $destination --query id --output tsv
    $minimumCreation = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    $PSNativeCommandUseErrorActionPreference = $false
    try {
        $fault = az storage account or-policy create --resource-group $ResourceGroupName --account-name $destination --source-account $sourceId --destination-account $destinationId --source-container source --destination-container destination --min-creation-time $minimumCreation --output json 2>&1
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB08-CP03'
    }
    $faultExit = $LASTEXITCODE
    $PSNativeCommandUseErrorActionPreference = $true
    if ($faultExit -eq 0) {
        $unexpectedPolicy = ([string]($fault -join "`n") | ConvertFrom-Json)
        $state.inputs['object-replication-policy-id'] = [string]$unexpectedPolicy.policyId
        Save-RunState
        throw 'Object replication unexpectedly succeeded while destination versioning was disabled; its policy ID was recorded for cleanup.'
    }
    az storage account blob-service-properties update --account-name $destination --resource-group $ResourceGroupName --enable-versioning true --output none
    try {
        $destinationPolicy = az storage account or-policy create --resource-group $ResourceGroupName --account-name $destination --source-account $sourceId --destination-account $destinationId --source-container source --destination-container destination --min-creation-time $minimumCreation --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB08-CP03'
    }
    $state.inputs['object-replication-policy-id'] = [string]$destinationPolicy.policyId
    Save-RunState
    az storage account or-policy show --resource-group $ResourceGroupName --account-name $destination --policy-id $state.inputs['object-replication-policy-id'] --output json |
    try {
            az storage account or-policy create --resource-group $ResourceGroupName --account-name $source --policy '@-' --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB08-CP03'
    }

    Sync-ManagedResource -CheckpointId 'LAB08-CP03'
    Write-CheckpointState -CheckpointId 'LAB08-CP03' -Status 'pass' -Message 'The pre-repair attempt fails, destination versioning becomes true, and the same policy ID with one rule exists on both accounts.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB08-CP03'
    Write-CheckpointState -CheckpointId 'LAB08-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB08-CP03 END

# CHECKPOINT LAB08-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB08-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB08-CP04'
    Save-RunState

    $sample = Join-Path $StateDir 'replication-sample.txt'
    $tenantId = az account show --query tenantId --output tsv
    $env:AZCOPY_AUTO_LOGIN_TYPE = 'AZCLI'
    $env:AZCOPY_TENANT_ID = $tenantId
    try {
        'revision 1' | Set-Content -LiteralPath $sample -Encoding utf8
        azcopy copy $sample "https://$source.blob.core.windows.net/source/replication-sample.txt" --from-to LocalBlob --overwrite=true
        'revision 2' | Set-Content -LiteralPath $sample -Encoding utf8
        azcopy copy $sample "https://$source.blob.core.windows.net/source/replication-sample.txt" --from-to LocalBlob --overwrite=true
    } finally {
        Remove-Item Env:AZCOPY_AUTO_LOGIN_TYPE -ErrorAction SilentlyContinue
        Remove-Item Env:AZCOPY_TENANT_ID -ErrorAction SilentlyContinue
    }
    az storage blob set-tier --account-name $source --container-name source --name replication-sample.txt --tier Cool --auth-mode login --output none

    Sync-ManagedResource -CheckpointId 'LAB08-CP04'
    Write-CheckpointState -CheckpointId 'LAB08-CP04' -Status 'pass' -Message 'The source has a current Cool blob plus at least one prior version; eligible versions begin asynchronous replication to destination.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB08-CP04'
    Write-CheckpointState -CheckpointId 'LAB08-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB08-CP04 END

# CHECKPOINT LAB08-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB08-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB08-CP05'
    Save-RunState

    $policyId = [string]$state.inputs['object-replication-policy-id']
    $sourcePolicy = az storage account or-policy show --resource-group $ResourceGroupName --account-name $source --policy-id $policyId --output json | ConvertFrom-Json
    $destinationPolicy = az storage account or-policy show --resource-group $ResourceGroupName --account-name $destination --policy-id $policyId --output json | ConvertFrom-Json
    $lifecycle = az storage account management-policy show --resource-group $ResourceGroupName --account-name $source --output json | ConvertFrom-Json
    $sourceVersions = @(az storage blob list --account-name $source --container-name source --include v --auth-mode login --output json | ConvertFrom-Json | Where-Object name -eq 'replication-sample.txt')
    $destinationCopies = @(az storage blob list --account-name $destination --container-name destination --include v --auth-mode login --output json | ConvertFrom-Json | Where-Object name -eq 'replication-sample.txt')
    if ($sourcePolicy.policyId -ne $destinationPolicy.policyId) { throw 'Replication policy IDs do not match.' }
    if (@($lifecycle.policy.rules | Where-Object name -eq 'tier-and-expire-versions').Count -ne 1) { throw 'Lifecycle rule is missing.' }
    if ($sourceVersions.Count -lt 2) { throw 'Source revisions are missing.' }
    [pscustomobject]@{ policyId = $policyId; lifecycleRules = @($lifecycle.policy.rules).Count; sourceVersions = $sourceVersions.Count; destinationCopiesObserved = $destinationCopies.Count; replicationIsAsynchronous = $true }

    Sync-ManagedResource -CheckpointId 'LAB08-CP05'
    Write-CheckpointState -CheckpointId 'LAB08-CP05' -Status 'pass' -Message 'Both policy copies match, the lifecycle rule and source versions exist, and destination-copy count is reported as an observation rather than a synchronous pass gate.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB08-CP05'
    Write-CheckpointState -CheckpointId 'LAB08-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB08-CP05 END

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
