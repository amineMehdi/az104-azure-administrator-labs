
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
$ResourceGroupName = $(if ('07' -in @('00', '01', '02')) { $null } else { "rg-az104-l07-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-07 execution plan'
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
    labId = 'LAB-07'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB07-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB07-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB07-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB07-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB07-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '07'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB07-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=07 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB07-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB07-CP01'
}

# CHECKPOINT LAB07-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB07-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB07-CP01'
    Save-RunState

    $provider = az provider show --namespace Microsoft.Storage --query registrationState --output tsv
    if ($provider -ne 'Registered') { throw 'Microsoft.Storage must already be Registered.' }
    [pscustomobject]@{ vnet = "vnet-$suffix"; subnet = '10.7.1.0/24'; account = "st07$suffix"; firewallTarget = 'Deny' }

    Sync-ManagedResource -CheckpointId 'LAB07-CP01'
    Write-CheckpointState -CheckpointId 'LAB07-CP01' -Status 'pass' -Message 'Storage is registered and the plan contains one non-overlapping subnet and a default-deny target.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB07-CP01'
    Write-CheckpointState -CheckpointId 'LAB07-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB07-CP01 END

# CHECKPOINT LAB07-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB07-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB07-CP02'
    Save-RunState

    $vnet = "vnet-$suffix"; $storage = "st07$suffix"
    try {
        $createdVnet = az network vnet create --resource-group $ResourceGroupName --name $vnet --location $Location --address-prefixes 10.7.0.0/16 --subnet-name storage --subnet-prefixes 10.7.1.0/24 --tags purpose=az104-lab labId=07 runId=$RunId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB07-CP02'
    }
    $vnetId = [string]$createdVnet.newVNet.id
    if (-not $vnetId) { $vnetId = az network vnet show --resource-group $ResourceGroupName --name $vnet --query id --output tsv }
    Add-ManagedObject -CheckpointId 'LAB07-CP02' -Kind 'azure-resource' -Id $vnetId -Name $vnet -Type 'Microsoft.Network/virtualNetworks' -Scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" -OwnershipMethod 'manifest-id-and-tags'
    az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name storage --service-endpoints Microsoft.Storage --output none
    $subnetId = az network vnet subnet show --resource-group $ResourceGroupName --vnet-name $vnet --name storage --query id --output tsv
    try {
        $createdStorage = az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --default-action Allow --tags purpose=az104-lab labId=07 runId=$RunId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB07-CP02'
    }
    Add-ManagedObject -CheckpointId 'LAB07-CP02' -Kind 'azure-resource' -Id ([string]$createdStorage.id) -Name $storage -Type 'Microsoft.Storage/storageAccounts' -Scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" -OwnershipMethod 'manifest-id-and-tags'
    $accountKey = az storage account keys list --resource-group $ResourceGroupName --account-name $storage --query '[0].value' --output tsv
    try {
    try {
            az storage container create --name private --account-name $storage --account-key $accountKey --public-access off --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB07-CP02'
    }
        $start = (Get-Date).ToUniversalTime().AddMinutes(-5).ToString('yyyy-MM-ddTHH:mmZ')
        $expiry = (Get-Date).ToUniversalTime().AddHours(2).ToString('yyyy-MM-ddTHH:mmZ')
    try {
            az storage container policy create --account-name $storage --container-name private --name az104 --permissions rwl --start $start --expiry $expiry --account-key $accountKey --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB07-CP02'
    }
    } finally { $accountKey = $null }
    az storage account network-rule add --resource-group $ResourceGroupName --account-name $storage --subnet $subnetId --output none
    az storage account update --resource-group $ResourceGroupName --name $storage --default-action Deny --bypass None --output none

    Sync-ManagedResource -CheckpointId 'LAB07-CP02'
    Write-CheckpointState -CheckpointId 'LAB07-CP02' -Status 'pass' -Message 'The subnet exposes Microsoft.Storage, the account is default-deny with one VNet rule, and the private container has one stored access policy.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB07-CP02'
    Write-CheckpointState -CheckpointId 'LAB07-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB07-CP02 END

# CHECKPOINT LAB07-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB07-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB07-CP03'
    Save-RunState

    $accountKey = az storage account keys list --resource-group $ResourceGroupName --account-name $storage --query '[0].value' --output tsv
    try {
        $sas = az storage container generate-sas --account-name $storage --name private --policy-name az104 --account-key $accountKey --output tsv
        if (-not $sas -or $sas -notmatch '(^|&)si=az104(&|$)') { throw 'Generated SAS does not reference the az104 stored access policy.' }
        Write-Host "Generated a policy-bound SAS in memory (length=$($sas.Length)); token redacted."
    } finally { $sas = $null; $accountKey = $null }

    Sync-ManagedResource -CheckpointId 'LAB07-CP03'
    Write-CheckpointState -CheckpointId 'LAB07-CP03' -Status 'pass' -Message 'A non-empty service SAS references policy az104 and is cleared without entering command output, state, or evidence.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB07-CP03'
    Write-CheckpointState -CheckpointId 'LAB07-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB07-CP03 END

# CHECKPOINT LAB07-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB07-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB07-CP04'
    Save-RunState

    $accountKey = az storage account keys list --resource-group $ResourceGroupName --account-name $storage --query '[0].value' --output tsv
    try {
        $sas = az storage container generate-sas --account-name $storage --name private --policy-name az104 --account-key $accountKey --output tsv
        $PSNativeCommandUseErrorActionPreference = $false
        $denied = az storage blob list --account-name $storage --container-name private --sas-token $sas --output none 2>&1
        $deniedExit = $LASTEXITCODE
        $PSNativeCommandUseErrorActionPreference = $true
        if ($deniedExit -eq 0) { throw 'The learner workstation unexpectedly passed the storage firewall.' }
    } finally { $sas = $null; $accountKey = $null }

    Sync-ManagedResource -CheckpointId 'LAB07-CP04'
    Write-CheckpointState -CheckpointId 'LAB07-CP04' -Status 'pass' -Message 'SAS signing succeeds locally, the data-plane request fails from the unapproved origin, and no token is retained.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB07-CP04'
    Write-CheckpointState -CheckpointId 'LAB07-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB07-CP04 END

# CHECKPOINT LAB07-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB07-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB07-CP05'
    Save-RunState

    az storage account network-rule remove --resource-group $ResourceGroupName --account-name $storage --subnet $subnetId --output none
    $afterInjection = az storage account network-rule list --resource-group $ResourceGroupName --account-name $storage --output json | ConvertFrom-Json
    if (@($afterInjection.virtualNetworkRules).Count -ne 0) { throw 'Subnet-rule injection did not produce the expected symptom.' }
    az storage account network-rule add --resource-group $ResourceGroupName --account-name $storage --subnet $subnetId --output none
    $accountKey = az storage account keys list --resource-group $ResourceGroupName --account-name $storage --query '[0].value' --output tsv
    try {
        az storage account update --resource-group $ResourceGroupName --name $storage --default-action Allow --output none
        az storage container policy delete --account-name $storage --container-name private --name az104 --account-key $accountKey --output none
    } finally {
        az storage account update --resource-group $ResourceGroupName --name $storage --default-action Deny --bypass None --output none
        $accountKey = $null
    }

    Sync-ManagedResource -CheckpointId 'LAB07-CP05'
    Write-CheckpointState -CheckpointId 'LAB07-CP05' -Status 'pass' -Message 'The exact subnet rule is restored, defaultAction is Deny, and policy az104 is revoked before cleanup.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB07-CP05'
    Write-CheckpointState -CheckpointId 'LAB07-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB07-CP05 END

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
