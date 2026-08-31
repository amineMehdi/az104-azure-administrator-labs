
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
$ResourceGroupName = $(if ('02' -in @('00', '01', '02')) { $null } else { "rg-az104-l02-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-02 execution plan'
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
    labId = 'LAB-02'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB02-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB02-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB02-CP03'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB02-CP04'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB02-CP05'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '02'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB02-CP01' } else { $CheckpointId })
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

# CHECKPOINT LAB02-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP01'
    Save-RunState

    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom,allowedToUseSSPR' --output json | ConvertFrom-Json
    $skus = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus?$select=id,skuPartNumber,consumedUnits,prepaidUnits' --output json | ConvertFrom-Json).value
    $registrationAccess = $true
    try { $null = az rest --method get --url 'https://graph.microsoft.com/v1.0/reports/authenticationMethods/userRegistrationDetails?$top=1' --output none } catch { $registrationAccess = $false }
    [pscustomobject]@{ invitePolicy = $policy.allowInvitesFrom; subscribedSkus = $skus.Count; registrationReportAccess = $registrationAccess }

    Sync-ManagedResource -CheckpointId 'LAB02-CP01'
    Write-CheckpointState -CheckpointId 'LAB02-CP01' -Status 'pass' -Message 'Invitation policy and subscribed SKUs are readable; registration-report access is explicitly true or recorded as an optional unavailable gate.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP01'
    Write-CheckpointState -CheckpointId 'LAB02-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB02-CP01 END

# CHECKPOINT LAB02-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP02'
    Save-RunState

    try {
        $group = az ad group create --display-name "AZ104-L02-$RunId-SSPR-Pilot" --mail-nickname "az104l02$suffix" --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP02'
    }
    $external['groupId'] = [string]$group.id
    Save-ExternalState
    Add-ManagedObject -CheckpointId 'LAB02-CP02' -Kind 'entra-object' -Id ([string]$group.id) -Name ([string]$group.displayName) -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'

    Sync-ManagedResource -CheckpointId 'LAB02-CP02'
    Write-CheckpointState -CheckpointId 'LAB02-CP02' -Status 'pass' -Message 'Exactly one run-specific security group exists and its ID is manifest-recorded as Microsoft.Graph/group before any optional task.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP02'
    Write-CheckpointState -CheckpointId 'LAB02-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB02-CP02 END

# CHECKPOINT LAB02-CP03 BEGIN
if (-not ((-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_GUEST_EMAIL'))))) {
    Write-CheckpointState -CheckpointId 'LAB02-CP03' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP03'
    Save-RunState

    $inviteBody = @{ invitedUserEmailAddress = $env:AZ104_GUEST_EMAIL; inviteRedirectUrl = 'https://myapps.microsoft.com'; sendInvitationMessage = $false } | ConvertTo-Json -Compress
    try {
        $invitation = az rest --method post --url 'https://graph.microsoft.com/v1.0/invitations' --body $inviteBody --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP03'
    }
    $external['guestUserId'] = [string]$invitation.invitedUser.id
    Save-ExternalState
    if (-not $external.guestUserId) { throw 'Invitation returned no guest user ID.' }
    Add-ManagedObject -CheckpointId 'LAB02-CP03' -Kind 'entra-object' -Id ([string]$external.guestUserId) -Name 'invited-guest' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
    $state.inputs['guest-email'] = [string]$env:AZ104_GUEST_EMAIL
    Save-RunState
    $memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.guestUserId)" } | ConvertTo-Json -Compress
    try {
        az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/`$ref" --body $memberBody --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP03'
    }

    Sync-ManagedResource -CheckpointId 'LAB02-CP03'
    Write-CheckpointState -CheckpointId 'LAB02-CP03' -Status 'pass' -Message 'One manifest-recorded userType Guest exists and is a direct member of the exact pilot group.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP03'
    Write-CheckpointState -CheckpointId 'LAB02-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB02-CP03 END

# CHECKPOINT LAB02-CP04 BEGIN
if (-not ((-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_GUEST_EMAIL'))) -and (-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_LICENSE_SKU_ID'))) -and (-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_USAGE_LOCATION'))))) {
    Write-CheckpointState -CheckpointId 'LAB02-CP04' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP04'
    Save-RunState

    if ($env:AZ104_USAGE_LOCATION -notmatch '^[A-Za-z]{2}$') { throw 'AZ104_USAGE_LOCATION must be a two-letter ISO country code.' }
    if (-not $external.guestUserId) { throw 'The guest checkpoint must complete before licensing.' }
    $PSNativeCommandUseErrorActionPreference = $false
    try {
        $denied = az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)/assignLicense" --body '{"addLicenses":[{"skuId":"00000000-0000-0000-0000-000000000000"}],"removeLicenses":[]}' --output none 2>&1
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP04'
    }
    $deniedExit = $LASTEXITCODE
    $PSNativeCommandUseErrorActionPreference = $true
    if ($deniedExit -eq 0) { throw 'The invalid-SKU break/fix request unexpectedly succeeded.' }
    $locationBody = @{ usageLocation = $env:AZ104_USAGE_LOCATION.ToUpperInvariant() } | ConvertTo-Json -Compress
    az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)" --body $locationBody --output none
    $state.inputs['usage-location'] = $env:AZ104_USAGE_LOCATION.ToUpperInvariant()
    Save-RunState
    $skus = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus' --output json | ConvertFrom-Json).value
    $sku = @($skus | Where-Object id -eq $env:AZ104_LICENSE_SKU_ID)
    if ($sku.Count -ne 1) { throw 'AZ104_LICENSE_SKU_ID is not a subscribed tenant SKU.' }
    if (($sku[0].prepaidUnits.enabled - $sku[0].consumedUnits) -lt 1) { throw 'The selected SKU has no enabled unit available.' }
    $licenseBody = @{ addLicenses = @(@{ skuId = $env:AZ104_LICENSE_SKU_ID }); removeLicenses = @() } | ConvertTo-Json -Depth 6 -Compress
    try {
        $assignmentResult = az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)/assignLicense" --body $licenseBody --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP04'
    }
    $state.inputs['license-sku-id'] = [string]$env:AZ104_LICENSE_SKU_ID
    Save-RunState
    if ($state.inputs['license-sku-id'] -notin @($assignmentResult.assignedLicenses.skuId)) { throw 'assignLicense did not return the approved SKU.' }

    Sync-ManagedResource -CheckpointId 'LAB02-CP04'
    Write-CheckpointState -CheckpointId 'LAB02-CP04' -Status 'pass' -Message 'The impossible SKU is denied, usageLocation is uppercase and persisted, and exactly the approved subscribed SKU is assigned.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP04'
    Write-CheckpointState -CheckpointId 'LAB02-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB02-CP04 END

# CHECKPOINT LAB02-CP05 BEGIN
if (-not ([string]::Equals([Environment]::GetEnvironmentVariable('AZ104_ALLOW_SSPR_POLICY_CHANGE'), 'YES', [StringComparison]::Ordinal))) {
    Write-CheckpointState -CheckpointId 'LAB02-CP05' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP05'
    Save-RunState

    if ($env:AZ104_ALLOW_SSPR_POLICY_CHANGE -cne 'YES') { throw 'Administrator SSPR mutation requires the exact YES authorization value.' }
    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=id,allowedToUseSSPR' --output json | ConvertFrom-Json
    if (-not @($state.originalSettings | Where-Object property -eq 'allowedToUseSSPR')) {
        $state.originalSettings += @{
            checkpointId = 'LAB02-CP05'; targetId = 'authorizationPolicy'; property = 'allowedToUseSSPR'
            value = [bool]$policy.allowedToUseSSPR; recordedAt = (Get-Date).ToUniversalTime().ToString('o')
        }
        Save-RunState
    }
    az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --body '{"allowedToUseSSPR":true}' --output none
    $members = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?`$select=id,userType,usageLocation,assignedLicenses" --output json | ConvertFrom-Json
    $baseline = @($state.originalSettings | Where-Object property -eq 'allowedToUseSSPR')
    if ($baseline.Count -ne 1) { throw 'Exactly one recoverable allowedToUseSSPR baseline is required.' }
    $registrationAccess = $true
    try { $registration = az rest --method get --url 'https://graph.microsoft.com/v1.0/reports/authenticationMethods/userRegistrationDetails?$top=1' --output json | ConvertFrom-Json } catch { $registrationAccess = $false }
    [pscustomobject]@{ memberCount = $members.value.Count; adminSspr = $true; recoverableBaselines = $baseline.Count; registrationReportAccess = $registrationAccess; selectedGroupScopeMutation = $false }

    Sync-ManagedResource -CheckpointId 'LAB02-CP05'
    Write-CheckpointState -CheckpointId 'LAB02-CP05' -Status 'pass' -Message 'The supported administrator property is true, exactly one prior Boolean is durable, and reconciliation explicitly reports that no selected-group scope endpoint was mutated.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP05'
    Write-CheckpointState -CheckpointId 'LAB02-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB02-CP05 END

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
