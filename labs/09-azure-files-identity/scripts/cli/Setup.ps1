
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
$ResourceGroupName = $(if ('09' -in @('00', '01', '02')) { $null } else { "rg-az104-l09-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-09 execution plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  command surface: Azure CLI hosted in PowerShell'
Write-Host '  state: run.json, validation.json, cleanup.json'
if (-not $Execute) {
    Write-Host 'Preview only. Review context, inputs, cost, tenant scope, and cleanup before using -Execute.'
    return
}
if ($false -and -not $AcknowledgeCost) { throw 'This lab requires -AcknowledgeCost before execution.' }
if ($true -and -not $AcknowledgeTenantChange) { throw 'This lab requires -AcknowledgeTenantChange before execution.' }

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -RunId $RunId -Location $Location -SecondaryLocation $SecondaryLocation
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest. Choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
$now = (Get-Date).ToUniversalTime().ToString('o')
$state = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-09'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB09-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB09-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB09-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB09-CP04'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB09-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '09'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB09-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=09 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB09-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB09-CP01'
}

# CHECKPOINT LAB09-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB09-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB09-CP01'
    Save-RunState

    $storage = "st09$suffix"
    $share = 'teamfiles'
    $availability = az storage account check-name --name $storage --output json | ConvertFrom-Json
    if (-not $availability.nameAvailable) { throw "Storage name unavailable: $($availability.reason)" }
    $requestedIdentitySource = [Environment]::GetEnvironmentVariable('AZ104_FILES_IDENTITY_SOURCE')
    if ($requestedIdentitySource -and $requestedIdentitySource -cne 'entra-kerberos') { throw 'Only the documented entra-kerberos optional lane is supported.' }

    Sync-ManagedResource -CheckpointId 'LAB09-CP01'
    Write-CheckpointState -CheckpointId 'LAB09-CP01' -Status 'pass' -Message 'The deterministic account name is available and any requested identity source exactly selects the documented gated path.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB09-CP01'
    Write-CheckpointState -CheckpointId 'LAB09-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB09-CP01 END

# CHECKPOINT LAB09-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB09-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB09-CP02'
    Save-RunState

    try {
        $created = az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --allow-shared-key-access true --tags purpose=az104-lab labId=09 runId=$RunId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB09-CP02'
    }
    Add-ManagedObject -CheckpointId 'LAB09-CP02' -Kind 'azure-resource' -Id ([string]$created.id) -Name $storage -Type 'Microsoft.Storage/storageAccounts' -Scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" -OwnershipMethod 'manifest-id-and-tags'
    az storage account file-service-properties update --resource-group $ResourceGroupName --account-name $storage --enable-delete-retention true --delete-retention-days 7 --output none
    try {
        $createdShare = az storage share-rm create --resource-group $ResourceGroupName --storage-account $storage --name $share --quota 20 --access-tier TransactionOptimized --enabled-protocols SMB --metadata labId=09 runId=$RunId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB09-CP02'
    }
    Add-ManagedObject -CheckpointId 'LAB09-CP02' -Kind 'azure-resource' -Id ([string]$createdShare.id) -Name $share -Type 'Microsoft.Storage/storageAccounts/fileServices/shares' -Scope ([string]$created.id) -OwnershipMethod 'manifest-id'

    Sync-ManagedResource -CheckpointId 'LAB09-CP02'
    Write-CheckpointState -CheckpointId 'LAB09-CP02' -Status 'pass' -Message 'A tagged Standard_LRS account contains one 20-GiB transaction-optimized SMB share and seven-day share soft delete is enabled.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB09-CP02'
    Write-CheckpointState -CheckpointId 'LAB09-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB09-CP02 END

# CHECKPOINT LAB09-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB09-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB09-CP03'
    Save-RunState

    $sample = Join-Path $StateDir 'sample.txt'
    'AZ-104 Azure Files protected sample' | Set-Content -LiteralPath $sample -Encoding utf8
    $accountKey = az storage account keys list --resource-group $ResourceGroupName --account-name $storage --query '[0].value' --output tsv
    if (-not $accountKey) { throw 'A temporary bootstrap key could not be obtained.' }
    try {
        az storage file upload --account-name $storage --share-name $share --source $sample --path sample.txt --account-key $accountKey --output none
    } finally {
        $accountKey = $null
        Remove-Variable accountKey -ErrorAction SilentlyContinue
    }
    $snapshot = az storage share-rm snapshot --resource-group $ResourceGroupName --storage-account $storage --name $share --output json | ConvertFrom-Json
    if ([string]::IsNullOrWhiteSpace([string]$snapshot.snapshotTime)) { throw 'Snapshot creation returned no snapshot time.' }
    $state.inputs['share-snapshot-time'] = [string]$snapshot.snapshotTime
    Save-RunState

    Sync-ManagedResource -CheckpointId 'LAB09-CP03'
    Write-CheckpointState -CheckpointId 'LAB09-CP03' -Status 'pass' -Message 'The active share contains sample.txt and an ARM-visible snapshot time is recorded without an account key in state.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB09-CP03'
    Write-CheckpointState -CheckpointId 'LAB09-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB09-CP03 END

# CHECKPOINT LAB09-CP04 BEGIN
if (-not ((-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_FILES_PRINCIPAL_OBJECT_ID'))) -and [string]::Equals([Environment]::GetEnvironmentVariable('AZ104_FILES_IDENTITY_SOURCE'), 'entra-kerberos', [StringComparison]::Ordinal))) {
    Write-CheckpointState -CheckpointId 'LAB09-CP04' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB09-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB09-CP04'
    Save-RunState

    $requestedSource = [Environment]::GetEnvironmentVariable('AZ104_FILES_IDENTITY_SOURCE')
    if ($requestedSource -cne 'entra-kerberos') { throw 'Identity mutation requires AZ104_FILES_IDENTITY_SOURCE exactly entra-kerberos.' }
    $identityPrincipalId = [Environment]::GetEnvironmentVariable('AZ104_FILES_PRINCIPAL_OBJECT_ID')
    $principal = az rest --method GET --url "https://graph.microsoft.com/v1.0/directoryObjects/$identityPrincipalId?`$select=id,@odata.type" --output json | ConvertFrom-Json
    if ($principal.id -ne $identityPrincipalId) { throw 'The approved identity principal did not resolve.' }
    $principalType = switch ([string]$principal.'@odata.type') { '#microsoft.graph.user' { 'User' } '#microsoft.graph.group' { 'Group' } '#microsoft.graph.servicePrincipal' { 'ServicePrincipal' } default { throw 'Unsupported principal type for share RBAC.' } }
    $state.inputs['files-principal-object-id'] = $identityPrincipalId
    $state.inputs['files-identity-source'] = $requestedSource
    Save-RunState
    $updatedAccount = az storage account update --name $storage --resource-group $ResourceGroupName --enable-files-aadkerb true --output json | ConvertFrom-Json
    if ($updatedAccount.azureFilesIdentityBasedAuthentication.directoryServiceOptions -ne 'AADKERB') { throw 'Entra Kerberos did not become the active identity source.' }
    $shareId = az storage share-rm show --resource-group $ResourceGroupName --storage-account $storage --name $share --query id --output tsv
    try {
        $injected = az role assignment create --assignee-object-id $identityPrincipalId --assignee-principal-type $principalType --role 'Storage File Data SMB Share Contributor' --scope $shareId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB09-CP04'
    }
    Add-ManagedObject -CheckpointId 'LAB09-CP04' -Kind 'azure-resource' -Id ([string]$injected.id) -Name 'injected-file-share-contributor' -Type 'Microsoft.Authorization/roleAssignments' -Scope $shareId -OwnershipMethod 'manifest-id'
    az role assignment delete --ids $injected.id
    $injectedRecord = @($state.managedObjects | Where-Object id -eq $injected.id)[0]
    $injectedRecord.lifecycleStatus = 'deleted'
    Save-RunState
    $missing = @(az role assignment list --assignee-object-id $identityPrincipalId --scope $shareId --output json | ConvertFrom-Json | Where-Object roleDefinitionName -eq 'Storage File Data SMB Share Contributor')
    if ($missing.Count -ne 0) { throw 'The missing-role fault was not established.' }
    try {
        $repaired = az role assignment create --assignee-object-id $identityPrincipalId --assignee-principal-type $principalType --role 'Storage File Data SMB Share Contributor' --scope $shareId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB09-CP04'
    }
    Add-ManagedObject -CheckpointId 'LAB09-CP04' -Kind 'azure-resource' -Id ([string]$repaired.id) -Name 'file-share-contributor' -Type 'Microsoft.Authorization/roleAssignments' -Scope $shareId -OwnershipMethod 'manifest-id'

    Sync-ManagedResource -CheckpointId 'LAB09-CP04'
    Write-CheckpointState -CheckpointId 'LAB09-CP04' -Status 'pass' -Message 'AADKERB is the only identity source and the approved principal has exactly the intended share-scoped SMB data role after the missing-role fault is repaired.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB09-CP04'
    Write-CheckpointState -CheckpointId 'LAB09-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB09-CP04 END

# CHECKPOINT LAB09-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB09-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB09-CP05'
    Save-RunState

    az storage share-rm delete --resource-group $ResourceGroupName --storage-account $storage --name $share --include snapshots --yes
    $deleted = @(az storage share-rm list --resource-group $ResourceGroupName --storage-account $storage --include-deleted true --output json | ConvertFrom-Json | Where-Object { $_.name -eq $share -and $_.deleted })
    if ($deleted.Count -ne 1 -or [string]::IsNullOrWhiteSpace([string]$deleted[0].deletedVersion)) { throw 'Expected one recoverable deleted share generation.' }
    $state.inputs['deleted-share-version'] = [string]$deleted[0].deletedVersion
    Save-RunState
    $restored = az storage share-rm restore --resource-group $ResourceGroupName --storage-account $storage --name $share --deleted-version $state.inputs['deleted-share-version'] --output json | ConvertFrom-Json
    if (-not $restored.id) { throw 'Share restore returned no resource ID.' }

    Sync-ManagedResource -CheckpointId 'LAB09-CP05'
    Write-CheckpointState -CheckpointId 'LAB09-CP05' -Status 'pass' -Message 'The original share generation is soft-deleted, identified by deletedVersion, restored under the same name, and its sample content remains readable.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB09-CP05'
    Write-CheckpointState -CheckpointId 'LAB09-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB09-CP05 END

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
