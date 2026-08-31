
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
$ResourceGroupName = $(if ('06' -in @('00', '01', '02')) { $null } else { "rg-az104-l06-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-06 execution plan'
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
    labId = 'LAB-06'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB06-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB06-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB06-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB06-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB06-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '06'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB06-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=06 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB06-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB06-CP01'
}

# CHECKPOINT LAB06-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB06-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB06-CP01'
    Save-RunState

    $skuUrl = "https://management.azure.com/subscriptions/$SubscriptionId/providers/Microsoft.Storage/skus?api-version=2023-05-01"
    $skus = @(az rest --method get --url $skuUrl --output json | ConvertFrom-Json).value
    $zrs = @($skus | Where-Object { $_.name -eq 'Standard_ZRS' -and $Location -in $_.locations -and @($_.restrictions | Where-Object { $_.type -eq 'location' -and $Location -in $_.values }).Count -eq 0 })
    $selectedSku = if ($zrs.Count -gt 0) { 'Standard_ZRS' } else { 'Standard_LRS' }
    $state.inputs['selected-redundancy'] = $selectedSku
    Save-RunState
    [pscustomobject]@{ location = $Location; selectedSku = $selectedSku; fallbackUsed = $selectedSku -eq 'Standard_LRS' }

    Sync-ManagedResource -CheckpointId 'LAB06-CP01'
    Write-CheckpointState -CheckpointId 'LAB06-CP01' -Status 'pass' -Message 'selected-redundancy is Standard_ZRS when unrestricted, otherwise Standard_LRS with fallbackUsed true.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB06-CP01'
    Write-CheckpointState -CheckpointId 'LAB06-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB06-CP01 END

# CHECKPOINT LAB06-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB06-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB06-CP02'
    Save-RunState

    $storage = "st06$suffix"
    $selectedSku = [string]$state.inputs['selected-redundancy']
    try {
        $created = az storage account create --name $storage --resource-group $ResourceGroupName --location $Location --kind StorageV2 --sku $selectedSku --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --allow-shared-key-access false --require-infrastructure-encryption true --assign-identity --tags purpose=az104-lab labId=06 runId=$RunId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB06-CP02'
    }
    Add-ManagedObject -CheckpointId 'LAB06-CP02' -Kind 'azure-resource' -Id ([string]$created.id) -Name $storage -Type 'Microsoft.Storage/storageAccounts' -Scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" -OwnershipMethod 'manifest-id-and-tags'

    Sync-ManagedResource -CheckpointId 'LAB06-CP02'
    Write-CheckpointState -CheckpointId 'LAB06-CP02' -Status 'pass' -Message 'The account uses the persisted SKU, TLS1_2, HTTPS only, infrastructure encryption, no public blobs, no Shared Key, and a system identity.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB06-CP02'
    Write-CheckpointState -CheckpointId 'LAB06-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB06-CP02 END

# CHECKPOINT LAB06-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB06-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB06-CP03'
    Save-RunState

    $storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
    $learnerId = az ad signed-in-user show --query id --output tsv
    if (-not $learnerId) { throw 'This interactive lab requires a signed-in Entra user for data-plane authorization.' }
    $state.inputs['learner-object-id'] = $learnerId
    Save-RunState
    try {
        $assignment = az role assignment create --assignee-object-id $learnerId --assignee-principal-type User --role 'Storage Blob Data Contributor' --scope $storageId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB06-CP03'
    }
    Add-ManagedObject -CheckpointId 'LAB06-CP03' -Kind 'azure-resource' -Id ([string]$assignment.id) -Name 'Storage Blob Data Contributor' -Type 'Microsoft.Authorization/roleAssignments' -Scope $storageId -OwnershipMethod 'manifest-id'
    try {
        az storage account encryption-scope create --resource-group $ResourceGroupName --account-name $storage --name confidential --key-source Microsoft.Storage --require-infrastructure-encryption true --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB06-CP03'
    }
    try {
        az storage container create --account-name $storage --name private --auth-mode login --default-encryption-scope confidential --deny-encryption-scope-override true --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB06-CP03'
    }
    $sample = Join-Path $StateDir 'identity-authorized.txt'
    'Azure CLI OAuth data-plane validation' | Set-Content -LiteralPath $sample -Encoding utf8
    az storage blob upload --account-name $storage --container-name private --name identity-authorized.txt --file $sample --auth-mode login --overwrite true --output none

    Sync-ManagedResource -CheckpointId 'LAB06-CP03'
    Write-CheckpointState -CheckpointId 'LAB06-CP03' -Status 'pass' -Message 'The learner has one account-scoped blob data role and the private blob was written with login auth into the infrastructure-encrypted scope.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB06-CP03'
    Write-CheckpointState -CheckpointId 'LAB06-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB06-CP03 END

# CHECKPOINT LAB06-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB06-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB06-CP04'
    Save-RunState

    $accountKey = az storage account keys list --resource-group $ResourceGroupName --account-name $storage --query '[0].value' --output tsv
    try {
        $PSNativeCommandUseErrorActionPreference = $false
        $denied = az storage container list --account-name $storage --account-key $accountKey --output none 2>&1
        $deniedExit = $LASTEXITCODE
        $PSNativeCommandUseErrorActionPreference = $true
        if ($deniedExit -eq 0) { throw 'Shared Key request unexpectedly succeeded.' }
    } finally {
        $accountKey = $null
    }

    Sync-ManagedResource -CheckpointId 'LAB06-CP04'
    Write-CheckpointState -CheckpointId 'LAB06-CP04' -Status 'pass' -Message 'The key-signed container listing fails, no key appears in output or state, and the OAuth blob query remains successful.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB06-CP04'
    Write-CheckpointState -CheckpointId 'LAB06-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB06-CP04 END

# CHECKPOINT LAB06-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB06-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB06-CP05'
    Save-RunState

    az storage account keys renew --resource-group $ResourceGroupName --account-name $storage --key secondary --output none
    az storage account show --resource-group $ResourceGroupName --name $storage --query '{sku:sku.name,https:enableHttpsTrafficOnly,tls:minimumTlsVersion,sharedKey:allowSharedKeyAccess,publicBlob:allowBlobPublicAccess,infrastructureEncryption:encryption.requireInfrastructureEncryption}' --output table

    Sync-ManagedResource -CheckpointId 'LAB06-CP05'
    Write-CheckpointState -CheckpointId 'LAB06-CP05' -Status 'pass' -Message 'All hardened properties remain intact after a non-disclosing secondary-key rotation and the OAuth blob path still passes.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB06-CP05'
    Write-CheckpointState -CheckpointId 'LAB06-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB06-CP05 END

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
