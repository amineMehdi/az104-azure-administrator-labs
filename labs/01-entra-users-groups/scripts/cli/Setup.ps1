
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
$ResourceGroupName = $(if ('01' -in @('00', '01', '02')) { $null } else { "rg-az104-l01-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-01 execution plan'
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
    labId = 'LAB-01'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB01-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB01-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB01-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB01-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB01-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '01'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB01-CP01' } else { $CheckpointId })
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

# CHECKPOINT LAB01-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP01'
    Save-RunState

    $tenant = az account show --query tenantId --output tsv
    $domains = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/domains?$select=id,isVerified,isDefault' --output json | ConvertFrom-Json).value
    $domain = @($domains | Where-Object { $_.id -eq $env:AZ104_TENANT_DOMAIN -and $_.isVerified })
    if ($domain.Count -ne 1) { throw 'AZ104_TENANT_DOMAIN must name one verified domain in the active tenant.' }
    [pscustomobject]@{ tenant = '<redacted>'; domain = $domain[0].id; verified = $domain[0].isVerified }

    Sync-ManagedResource -CheckpointId 'LAB01-CP01'
    Write-CheckpointState -CheckpointId 'LAB01-CP01' -Status 'pass' -Message 'The supplied domain appears exactly once with isVerified true, and the Graph request succeeds in the active tenant.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP01'
    Write-CheckpointState -CheckpointId 'LAB01-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP01 END

# CHECKPOINT LAB01-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP02'
    Save-RunState

    if ($env:AZ104_LAB_INITIAL_PASSWORD.Length -lt 12) { throw 'The temporary password must contain at least 12 characters.' }
    $domain = $env:AZ104_TENANT_DOMAIN
    $userIds = @()
    $users = @(
        @{ alias = "az104l01a$suffix"; displayName = "AZ104-L01-$RunId-Alex"; department = 'Operations' },
        @{ alias = "az104l01b$suffix"; displayName = "AZ104-L01-$RunId-Blair"; department = 'Operations' }
    )
    foreach ($user in $users) {
        $bodyPath = Join-Path $StateDir ".user-$($user.alias).json"
        $body = @{
            accountEnabled = $true
            displayName = $user.displayName
            mailNickname = $user.alias
            userPrincipalName = "$($user.alias)@$domain"
            department = $user.department
            passwordProfile = @{ forceChangePasswordNextSignIn = $true; password = $env:AZ104_LAB_INITIAL_PASSWORD }
        }
        try {
            $body | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $bodyPath -Encoding utf8
    try {
                $created = az rest --method post --url 'https://graph.microsoft.com/v1.0/users' --body "@$bodyPath" --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP02'
    }
        } finally {
            Remove-Item -LiteralPath $bodyPath -Force -ErrorAction SilentlyContinue
        }
        $userIds += [string]$created.id
        $external['userIds'] = @($userIds)
    Save-ExternalState
        Add-ManagedObject -CheckpointId 'LAB01-CP02' -Kind 'entra-object' -Id ([string]$created.id) -Name $user.displayName -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
    }
    Remove-Item Env:AZ104_LAB_INITIAL_PASSWORD -ErrorAction SilentlyContinue

    Sync-ManagedResource -CheckpointId 'LAB01-CP02'
    Write-CheckpointState -CheckpointId 'LAB01-CP02' -Status 'pass' -Message 'Two enabled cloud-only users exist with unique UPNs, Operations department, and IDs already present in run.json.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP02'
    Write-CheckpointState -CheckpointId 'LAB01-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP02 END

# CHECKPOINT LAB01-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP03'
    Save-RunState

    $groupBodyPath = Join-Path $StateDir '.group.json'
    @{ displayName = "AZ104-L01-$RunId-Operators"; mailEnabled = $false; mailNickname = "az104l01g$suffix"; securityEnabled = $true } |
        ConvertTo-Json | Set-Content -LiteralPath $groupBodyPath -Encoding utf8
    try {
    try {
            $group = az rest --method post --url 'https://graph.microsoft.com/v1.0/groups' --body "@$groupBodyPath" --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP03'
    }
    } finally {
        Remove-Item -LiteralPath $groupBodyPath -Force -ErrorAction SilentlyContinue
    }
    $external['groupId'] = [string]$group.id
    Save-ExternalState
    Add-ManagedObject -CheckpointId 'LAB01-CP03' -Kind 'entra-object' -Id ([string]$group.id) -Name ([string]$group.displayName) -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
    $memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.userIds[0])" } | ConvertTo-Json -Compress
    try {
        az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/`$ref" --body $memberBody --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP03'
    }

    Sync-ManagedResource -CheckpointId 'LAB01-CP03'
    Write-CheckpointState -CheckpointId 'LAB01-CP03' -Status 'pass' -Message 'One security-enabled group exists and its direct members collection contains Alex but not Blair.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP03'
    Write-CheckpointState -CheckpointId 'LAB01-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP03 END

# CHECKPOINT LAB01-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP04'
    Save-RunState

    $ownerBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" } | ConvertTo-Json -Compress
    try {
        az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/owners/`$ref" --body $ownerBody --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP04'
    }
    $members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?`$select=id" --output json | ConvertFrom-Json).value.id
    if ($external.userIds[1] -in $members) { throw 'Blair must be an owner only for this checkpoint.' }

    Sync-ManagedResource -CheckpointId 'LAB01-CP04'
    Write-CheckpointState -CheckpointId 'LAB01-CP04' -Status 'pass' -Message 'Blair is the sole explicit owner, Alex is the sole member, and the two object-ID sets do not overlap.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP04'
    Write-CheckpointState -CheckpointId 'LAB01-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP04 END

# CHECKPOINT LAB01-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP05'
    Save-RunState

    az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[0])" --body '{"jobTitle":"Cloud Operations Analyst"}' --output none
    az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" --body '{"accountEnabled":false}' --output none
    $disabled = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])?`$select=accountEnabled" --query accountEnabled --output tsv
    if ($disabled -ne 'false') { throw 'The disabled-state validation did not converge.' }
    az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" --body '{"accountEnabled":true}' --output none
    az rest --method delete --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/$($external.userIds[0])/%24ref" --output none
    $faultMembers = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
    if ($external.userIds[0] -in @($faultMembers.id)) { throw 'The missing-membership fault was not established.' }
    $memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.userIds[0])" } | ConvertTo-Json -Compress
    try {
        az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/%24ref" --body $memberBody --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP05'
    }
    $repairedMembers = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
    if ($repairedMembers.Count -ne 1 -or $repairedMembers[0].id -ne $external.userIds[0]) { throw 'Alex membership repair failed.' }

    Sync-ManagedResource -CheckpointId 'LAB01-CP05'
    Write-CheckpointState -CheckpointId 'LAB01-CP05' -Status 'pass' -Message 'Alex has the new job title, Blair is enabled again, and the final relationship inventory still has one distinct member and owner.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP05'
    Write-CheckpointState -CheckpointId 'LAB01-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP05 END

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
