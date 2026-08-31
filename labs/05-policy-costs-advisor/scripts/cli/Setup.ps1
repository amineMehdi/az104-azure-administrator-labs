
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
$ResourceGroupName = $(if ('05' -in @('00', '01', '02')) { $null } else { "rg-az104-l05-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-05 execution plan'
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
    labId = 'LAB-05'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB05-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB05-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB05-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB05-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB05-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '05'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB05-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=05 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB05-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB05-CP01'
}

# CHECKPOINT LAB05-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB05-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB05-CP01'
    Save-RunState

    $definitionGuid = '1e30110a-5ceb-460c-a204-c1c3969c6d62'
    $definitionId = "/providers/Microsoft.Authorization/policyDefinitions/$definitionGuid"
    $definition = az policy definition show --name $definitionGuid --output json | ConvertFrom-Json
    if ($definition.id -ne $definitionId -or $definition.policyRule.then.effect -ne 'deny') { throw 'Required immutable built-in tag Policy definition was not found.' }
    foreach ($provider in @('Microsoft.PolicyInsights','Microsoft.Consumption','Microsoft.Insights','Microsoft.Advisor')) {
        $stateValue = az provider show --namespace $provider --query registrationState --output tsv
        if ($stateValue -ne 'Registered') { throw "Provider is not registered: $provider" }
    }

    Sync-ManagedResource -CheckpointId 'LAB05-CP01'
    Write-CheckpointState -CheckpointId 'LAB05-CP01' -Status 'pass' -Message 'One built-in definition ID is resolved and every governance provider is already Registered without preflight mutation.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB05-CP01'
    Write-CheckpointState -CheckpointId 'LAB05-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB05-CP01 END

# CHECKPOINT LAB05-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB05-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB05-CP02'
    Save-RunState

    $definitionId = '/providers/Microsoft.Authorization/policyDefinitions/1e30110a-5ceb-460c-a204-c1c3969c6d62'
    $parameters = '{"tagName":{"value":"purpose"},"tagValue":{"value":"az104-lab"}}'

    try {
        $assignment = az policy assignment create --name $policyName --display-name "AZ104 require purpose $RunId" --scope $scope --policy $definitionId --params $parameters --enforcement-mode Default --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB05-CP02'
    }

    Add-ManagedObject -CheckpointId 'LAB05-CP02' -Kind 'azure-resource' -Id ([string]$assignment.id) -Name $policyName -Type 'Microsoft.Authorization/policyAssignments' -Scope $scope -OwnershipMethod 'manifest-id'

    Sync-ManagedResource -CheckpointId 'LAB05-CP02'
    Write-CheckpointState -CheckpointId 'LAB05-CP02' -Status 'pass' -Message 'One Default-enforcement assignment targets the exact resource group with tagName purpose and tagValue az104-lab.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB05-CP02'
    Write-CheckpointState -CheckpointId 'LAB05-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB05-CP02 END

# CHECKPOINT LAB05-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB05-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB05-CP03'
    Save-RunState

    try {
        $compliant = az storage account create --name $storage --resource-group $ResourceGroupName --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --tags purpose=az104-lab labId=05 runId=$RunId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB05-CP03'
    }
    Add-ManagedObject -CheckpointId 'LAB05-CP03' -Kind 'azure-resource' -Id ([string]$compliant.id) -Name $storage -Type 'Microsoft.Storage/storageAccounts' -Scope $scope -OwnershipMethod 'manifest-id-and-tags'
    $deniedName = "st05bad$suffix"
    $PSNativeCommandUseErrorActionPreference = $false
    try {
        $deniedOutput = az storage account create --name $deniedName --resource-group $ResourceGroupName --location $Location --sku Standard_LRS --kind StorageV2 --output json 2>&1
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB05-CP03'
    }
    $deniedExit = $LASTEXITCODE
    $PSNativeCommandUseErrorActionPreference = $true
    if ($deniedExit -eq 0) {
        $unexpected = az storage account show --name $deniedName --resource-group $ResourceGroupName --output json | ConvertFrom-Json
        Add-ManagedObject -CheckpointId 'LAB05-CP03' -Kind 'azure-resource' -Id ([string]$unexpected.id) -Name $deniedName -Type 'Microsoft.Storage/storageAccounts' -Scope $scope -OwnershipMethod 'manifest-id'
        throw 'The untagged request was not denied; keep the unexpected resource recorded and wait for Policy propagation before repair.'
    }
    $state.inputs['denied-request-observed'] = $true
    Save-RunState

    Sync-ManagedResource -CheckpointId 'LAB05-CP03'
    Write-CheckpointState -CheckpointId 'LAB05-CP03' -Status 'pass' -Message 'The tagged account exists and the untagged account request returns a Policy denial without creating a resource.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB05-CP03'
    Write-CheckpointState -CheckpointId 'LAB05-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB05-CP03 END

# CHECKPOINT LAB05-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB05-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB05-CP04'
    Save-RunState

    if ($env:AZ104_BUDGET_EMAIL) {
    try {
            $actionGroup = az monitor action-group create --name $actionGroupName --resource-group $ResourceGroupName --short-name az104cost --tags purpose=az104-lab labId=05 runId=$RunId --action email ApprovedBudgetEmail $env:AZ104_BUDGET_EMAIL usecommonalertschema --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB05-CP04'
    }
    } else {
    try {
            $actionGroup = az monitor action-group create --name $actionGroupName --resource-group $ResourceGroupName --short-name az104cost --tags purpose=az104-lab labId=05 runId=$RunId --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB05-CP04'
    }
    }
    Add-ManagedObject -CheckpointId 'LAB05-CP04' -Kind 'azure-resource' -Id ([string]$actionGroup.id) -Name $actionGroupName -Type 'Microsoft.Insights/actionGroups' -Scope $scope -OwnershipMethod 'manifest-id-and-tags'
    $startDate = (Get-Date -Day 1 -Hour 0 -Minute 0 -Second 0).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    $endDate = (Get-Date -Day 1 -Hour 0 -Minute 0 -Second 0).AddYears(1).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    $contacts = if ($env:AZ104_BUDGET_EMAIL) { @($env:AZ104_BUDGET_EMAIL) } else { @() }
    $budgetBody = @{ properties = @{ category = 'Cost'; amount = 25; timeGrain = 'Monthly'; timePeriod = @{ startDate = $startDate; endDate = $endDate }; notifications = @{ Actual_GreaterThanOrEqualTo_80_Percent = @{ enabled = $true; operator = 'GreaterThanOrEqualTo'; threshold = 80; thresholdType = 'Actual'; contactEmails = $contacts; contactGroups = @($actionGroup.id); contactRoles = @() } } } } | ConvertTo-Json -Depth 12 -Compress
    $budgetUrl = "https://management.azure.com$scope/providers/Microsoft.Consumption/budgets/$budgetName?api-version=2023-05-01"
    try {
        $budget = az rest --method put --url $budgetUrl --body $budgetBody --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB05-CP04'
    }
    Add-ManagedObject -CheckpointId 'LAB05-CP04' -Kind 'azure-resource' -Id ([string]$budget.id) -Name $budgetName -Type 'Microsoft.Consumption/budgets' -Scope $scope -OwnershipMethod 'manifest-id'

    Sync-ManagedResource -CheckpointId 'LAB05-CP04'
    Write-CheckpointState -CheckpointId 'LAB05-CP04' -Status 'pass' -Message 'The monthly 25-unit budget has an enabled actual-cost threshold at 80 percent and references the exact action-group ID.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB05-CP04'
    Write-CheckpointState -CheckpointId 'LAB05-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB05-CP04 END

# CHECKPOINT LAB05-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB05-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB05-CP05'
    Save-RunState

    az policy state trigger-scan --resource-group $ResourceGroupName --no-wait
    az policy state list --resource-group $ResourceGroupName --filter "PolicyAssignmentName eq '$policyName'" --all --output table
    az advisor recommendation list --category Cost --query '[].{impact:impact,resource:resourceMetadata.resourceId,problem:shortDescription.problem}' --output table

    Sync-ManagedResource -CheckpointId 'LAB05-CP05'
    Write-CheckpointState -CheckpointId 'LAB05-CP05' -Status 'pass' -Message 'Governance evidence distinguishes current compliant/non-compliant Policy state, configured budget notification, and zero or more contextual Advisor recommendations.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB05-CP05'
    Write-CheckpointState -CheckpointId 'LAB05-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB05-CP05 END

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
