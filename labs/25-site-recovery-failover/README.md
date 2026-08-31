
<!-- BEGIN GENERATED AZ104 V2 -->
# Lab 25: Replicate and fail over an Azure VM with Site Recovery

[Previous: Lab 24](../24-azure-backup-restore/README.md) · [Catalog](../README.md) · [Next: Lab 26](../26-capstone-build/README.md)

This self-contained lab uses Azure CLI commands hosted in PowerShell. Complete the guided lane or the automated lane—not both with the same run ID.

## Scenario, role, and outcome

Scenario: You are a disaster-recovery administrator piloting azure-to-azure replication. Build and prove this disposable service path: The source VM and cache account feed Azure-to-Azure replication through paired fabrics, protection containers, policy, and network mapping; an exactly gated test failover targets only the isolated recovery VNet and is cleaned up asynchronously.

Learner role: A disaster-recovery administrator piloting Azure-to-Azure replication.

Outcome: Use Azure CLI in PowerShell to create the source vm and isolated recovery network, configure azure-to-azure replication behind explicit approval, and reconcile replication health, recovery mapping, and cleanup order, with recoverable state and deterministic cleanup.

| Item | Value |
|---|---|
| Duration | 180 minutes |
| Difficulty | advanced |
| Cost class | `elevated` |
| Command surface | Azure CLI (`az`, `az rest`, Bicep, AzCopy, or KQL where required) hosted in PowerShell |
| Live state | Not executed during this offline rebuild |

Completion criteria:

- All required checkpoints report pass.
- The deterministic break/fix is injected, diagnosed, and repaired.
- cleanup.json reports no active run-owned resources, with any retained item explicitly documented.

## Objectives and checkpoints

| Objective | Skill | Checkpoints |
|---|---|---|
| `MR-RECOVERY-05` | Configure Azure Site Recovery for Azure resources | `LAB25-CP01`, `LAB25-CP03`, `LAB25-CP05` |
| `MR-RECOVERY-06` | Perform a failover to a secondary region by using Site Recovery | `LAB25-CP02`, `LAB25-CP04`, `LAB25-CP05` |

The authoritative objective wording comes from the [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), skills measured as of 2026-04-17.

## Architecture and service topology

![Lab 25 service topology](diagrams/architecture.svg)

The editable source is [architecture.mmd](diagrams/architecture.mmd). The source VM and cache account feed Azure-to-Azure replication through paired fabrics, protection containers, policy, and network mapping; an exactly gated test failover targets only the isolated recovery VNet and is cleaned up asynchronously.

## Concept primer and design decisions

Site Recovery requires source and target fabrics, protection containers, policy, network mapping, replication-protected items, and healthy synchronization. Test failover must use an isolated network and be cleaned up before protection is removed.

Design decisions:

- Use non-overlapping primary and recovery networks.
- Gate elevated cost and secondary-region input.
- Run test failover only after protected health is ready.

## Required and optional inputs

| Input | Required | Source | Safe example | Gate behavior |
|---|:---:|---|---|---|
| `run-id` — Unique lowercase run ownership identifier | Yes | parameter | `az104l25-01` | `block` |
| `subscription-id` — Expected disposable subscription ID | Yes | parameter-or-environment (`AZ104_SUBSCRIPTION_ID`) | `00000000-0000-0000-0000-000000000000` | `block` |
| `location` — Approved primary Azure region | Yes | parameter-or-environment (`AZ104_LOCATION`) | `westeurope` | `block` |
| `secondary-location` — Approved paired recovery region | Yes | parameter-or-environment (`AZ104_SECONDARY_LOCATION`) | `northeurope` | `block` |
| `enable-asr` — Exact YES authorization for billable Site Recovery replication | No | environment (`AZ104_ENABLE_ASR`) | `YES` | `skip-checkpoint` |
| `run-asr-test-failover` — Exact YES authorization for an isolated Site Recovery test failover | No | environment (`AZ104_RUN_ASR_TEST_FAILOVER`) | `YES` | `skip-checkpoint` |

Secrets stay in temporary environment variables and are never written to `run.json`, validation evidence, or Git. A `skip-checkpoint` gate produces a visible partial result; it never becomes a pass.

## Read-only preflight

Sign in deliberately, inspect the active context, then run the lab preflight. It never signs in, changes context, installs an extension, registers a provider, or creates a resource.

```powershell
az login
az account show --query '{cloud:environmentName,subscription:id,tenant:tenantId,user:user.name}' --output json
./scripts/cli/Preflight.ps1 -SubscriptionId $env:AZ104_SUBSCRIPTION_ID -RunId 'az104l25-01' -Location 'westeurope'
```

Representative redacted output:

```text
context                 True  cloud=AzureCloud; tenant=<redacted>; subscription=<redacted>
azure-cli               True  2.88.x
provider:<namespace>    True  Registered
region                  True  westeurope
Preflight passed. It performed no Azure mutation.
```

If a required row fails, stop. Correct the local tool, context, provider, quota, SKU, region, permission, or input outside the lab, then rerun preflight.

## Task 1 — Verify paired-region and Site Recovery prerequisites {#task-1}

Checkpoint: `LAB25-CP01`

Purpose and operational relevance: Read the provider, region, SKU, feature, quota, and companion-tool signals needed for verify paired-region and site recovery prerequisites, without changing Azure state. The change is unsafe when replication cannot start when source and target regions are equal or an ASR provider is unregistered. This checkpoint therefore proves: Source and recovery regions differ, the VM SKU is available, and the site-recovery extension/provider commands are ready.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
if (-not $SecondaryLocation -or $SecondaryLocation -eq $Location) { throw 'Supply a distinct approved secondary region.' }
az extension show --name site-recovery --query version --output tsv
az provider show --namespace Microsoft.RecoveryServices --query registrationState --output tsv
az vm list-skus --location $Location --size Standard_B1s --all --query "[?name=='Standard_B1s'].name" --output tsv
if (-not (Get-Command ssh-keygen -ErrorAction SilentlyContinue)) { throw 'ssh-keygen is required for the source VM key.' }
```

Expected state: Source and recovery regions differ, the VM SKU is available, and the site-recovery extension/provider commands are ready.

Representative redacted output:

```text
Source and recovery regions differ, the VM SKU is available, and the site-recovery extension/provider commands are ready.
```

Positive validation:

```powershell
$extension = az extension show --name site-recovery --query version --output tsv
if (-not $extension) { throw 'The site-recovery Azure CLI extension is not installed.' }
```

Expected positive result: Source and recovery regions differ, the VM SKU is available, and the site-recovery extension/provider commands are ready.

Negative validation:

```powershell
$recoveryRegion = az account list-locations --query "[?name=='$SecondaryLocation'].name | [0]" --output tsv
if (-not $recoveryRegion -or $SecondaryLocation -eq $Location) {
  throw 'Primary and recovery locations must be distinct, available Azure regions.'
}
$recoveryRegion
```

Expected negative result: LAB25-CP01 negative boundary: The undesired state is absent; the negative assertion must not report: Primary and recovery locations must be distinct.

Evidence to retain:

- LAB25-CP01 UTC result for verify paired-region and site recovery prerequisites.
- Exact run-owned resource/object ID returned by the commands in LAB25-CP01.
- Positive assertion proving: Source and recovery regions differ, the VM SKU is available, and the site-recovery extension/provider commands are ready.
- Negative assertion proving absence of: Primary and recovery locations must be distinct.

Common failure and safe retry: Replication cannot start when source and target regions are equal or an ASR provider is unregistered. Retry LAB25-CP01 for verify paired-region and site recovery prerequisites only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB25-CP02, LAB25-CP03, LAB25-CP04, LAB25-CP05, remove the exact manifest IDs created or configured by LAB25-CP01 for verify paired-region and site recovery prerequisites; its residual probe must then return zero active IDs.

## Task 2 — Create the source VM and isolated recovery network {#task-2}

Checkpoint: `LAB25-CP02`

Purpose and operational relevance: Provision and immediately inventory the exact run-owned resources needed to create the source vm and isolated recovery network, so partial completion remains recoverable. The change is unsafe when a cache account in an unsupported region or a target VNet with overlapping address space blocks replication setup. This checkpoint therefore proves: The private source VM, cache storage, source/recovery VNets, and vault are recorded before replication is gated.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$vault = "asr-$suffix"; $vm = "vm-$suffix"; $sourceVnet = "source-$suffix"; $recoveryVnet = "recovery-$suffix"; $testVnet = "test-$suffix"; $cache = "st25$suffix"
$keyPath = Join-Path $StateDir 'id_ed25519'; ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
az network vnet create --resource-group $ResourceGroupName --name $sourceVnet --location $Location --address-prefixes 10.25.0.0/16 --subnet-name workload --subnet-prefixes 10.25.1.0/24 --output none
az network nic create --resource-group $ResourceGroupName --name "nic-$suffix" --location $Location --vnet-name $sourceVnet --subnet workload --output none
az vm create --resource-group $ResourceGroupName --name $vm --location $Location --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --nics "nic-$suffix" --output none
az network vnet create --resource-group $ResourceGroupName --name $recoveryVnet --location $SecondaryLocation --address-prefixes 10.26.0.0/16 --subnet-name recovery --subnet-prefixes 10.26.1.0/24 --output none
az network vnet create --resource-group $ResourceGroupName --name $testVnet --location $SecondaryLocation --address-prefixes 10.126.0.0/16 --subnet-name isolated --subnet-prefixes 10.126.1.0/24 --output none
az storage account create --resource-group $ResourceGroupName --name $cache --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
az backup vault create --resource-group $ResourceGroupName --name $vault --location $SecondaryLocation --output none
```

Expected state: The private source VM, cache storage, source/recovery VNets, and vault are recorded before replication is gated.

Representative redacted output:

```text
The private source VM, cache storage, source/recovery VNets, and vault are recorded before replication is gated.
```

Positive validation:

```powershell
$vnetCount = az network vnet list --resource-group $ResourceGroupName --query "[?name=='$sourceVnet' || name=='$recoveryVnet' || name=='$testVnet'] | length(@)" --output tsv
if ([int]$vnetCount -ne 3) { throw 'The source, recovery, and isolated test VNets are not all present.' }
```

Expected positive result: The private source VM, cache storage, source/recovery VNets, and vault are recorded before replication is gated.

Negative validation:

```powershell
$peerings = az network vnet peering list --resource-group $ResourceGroupName --vnet-name $testVnet --query "length(@)" --output tsv
if ([int]$peerings -ne 0) { throw 'The test-failover VNet is peered and is not isolated.' }
```

Expected negative result: LAB25-CP02 negative boundary: The undesired state is absent; the negative assertion must not report: The test-failover VNet is peered and is not isolated.

Evidence to retain:

- LAB25-CP02 UTC result for create the source vm and isolated recovery network.
- Exact run-owned resource/object ID returned by the commands in LAB25-CP02.
- Positive assertion proving: The private source VM, cache storage, source/recovery VNets, and vault are recorded before replication is gated.
- Negative assertion proving absence of: The test-failover VNet is peered and is not isolated.

Common failure and safe retry: A cache account in an unsupported region or a target VNet with overlapping address space blocks replication setup. Retry LAB25-CP02 for create the source vm and isolated recovery network only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB25-CP03, LAB25-CP04, LAB25-CP05, remove the exact manifest IDs created or configured by LAB25-CP02 for create the source vm and isolated recovery network; its residual probe must then return zero active IDs.

## Task 3 — Configure Azure-to-Azure replication behind explicit approval {#task-3}

Checkpoint: `LAB25-CP03`

Purpose and operational relevance: Configure and independently inspect the control-plane and data-path properties needed to configure azure-to-azure replication behind explicit approval. The change is unsafe when a non-affirmative gate value must never start costly replication, and partial configuration can take many minutes to converge. This checkpoint therefore proves: When AZ104_ENABLE_ASR=YES, fabric, containers, policy, mapping, and protected item converge to a protected state; otherwise the optional checkpoint is skipped.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$sourceFabric = "fabric-source-$suffix"; $recoveryFabric = "fabric-recovery-$suffix"; $sourceContainer = "container-source-$suffix"; $recoveryContainer = "container-recovery-$suffix"; $mapping = "mapping-$suffix"; $policy = "policy-$suffix"; $protectedItem = "protected-$suffix"
az site-recovery fabric create --resource-group $ResourceGroupName --vault-name $vault --name $sourceFabric --custom-details "{azure:{location:$Location}}" --output none
az site-recovery fabric create --resource-group $ResourceGroupName --vault-name $vault --name $recoveryFabric --custom-details "{azure:{location:$SecondaryLocation}}" --output none
az site-recovery protection-container create --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --name $sourceContainer --provider-input '[{instance-type:A2A}]' --output none
az site-recovery protection-container create --resource-group $ResourceGroupName --vault-name $vault --fabric-name $recoveryFabric --name $recoveryContainer --provider-input '[{instance-type:A2A}]' --output none
az site-recovery policy create --resource-group $ResourceGroupName --vault-name $vault --name $policy --provider-specific-input '{a2a:{multi-vm-sync-status:Enable}}' --output none
$policyId = az site-recovery policy show --resource-group $ResourceGroupName --vault-name $vault --name $policy --query id --output tsv
$recoveryContainerId = az site-recovery protection-container show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $recoveryFabric --name $recoveryContainer --query id --output tsv
az site-recovery protection-container mapping create --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $mapping --policy-id $policyId --target-container $recoveryContainerId --provider-input '{a2a:{agent-auto-update-status:Disabled}}' --output none
$vmId = az vm show --resource-group $ResourceGroupName --name $vm --query id --output tsv
$osDiskId = az vm show --resource-group $ResourceGroupName --name $vm --query storageProfile.osDisk.managedDisk.id --output tsv
$cacheId = az storage account show --resource-group $ResourceGroupName --name "st25$suffix" --query id --output tsv
$recoveryVnetId = az network vnet show --resource-group $ResourceGroupName --name $recoveryVnet --query id --output tsv
$recoveryGroupId = az group show --name $ResourceGroupName --query id --output tsv
$providerDetails = @{ a2a = @{ 'fabric-object-id' = $vmId; 'vm-managed-disks' = @(@{ 'disk-id' = $osDiskId; 'primary-staging-azure-storage-account-id' = $cacheId; 'recovery-resource-group-id' = $recoveryGroupId }); 'recovery-azure-network-id' = $recoveryVnetId; 'recovery-container-id' = $recoveryContainerId; 'recovery-resource-group-id' = $recoveryGroupId; 'recovery-subnet-name' = 'recovery' } } | ConvertTo-Json -Depth 10 -Compress
az site-recovery protected-item create --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --policy-id $policyId --provider-details $providerDetails --output none
$deadline = (Get-Date).AddMinutes(90)
do { Start-Sleep -Seconds 30; $protectionState = az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --query properties.protectionState --output tsv } until ($protectionState -eq 'Protected' -or (Get-Date) -gt $deadline)
if ($protectionState -ne 'Protected') { throw "Site Recovery did not reach Protected within the bounded wait; current state is $protectionState." }
```

Expected state: When AZ104_ENABLE_ASR=YES, fabric, containers, policy, mapping, and protected item converge to a protected state; otherwise the optional checkpoint is skipped.

Representative redacted output:

```text
When AZ104_ENABLE_ASR=YES, fabric, containers, policy, mapping, and protected item converge to a protected state; otherwise the optional checkpoint is skipped.
```

Positive validation:

```powershell
$stateValue = az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --query properties.protectionState --output tsv
if ($stateValue -ne 'Protected') { throw "Replication protection state is $stateValue." }
```

Expected positive result: When AZ104_ENABLE_ASR=YES, fabric, containers, policy, mapping, and protected item converge to a protected state; otherwise the optional checkpoint is skipped.

Negative validation:

```powershell
$health = az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --query properties.replicationHealth --output tsv
if ($health -notin @('Normal','Healthy')) { throw "Replication health is $health." }
```

Expected negative result: LAB25-CP03 negative boundary: The undesired state is absent; the negative assertion must not report: Replication health is reported health.

Evidence to retain:

- LAB25-CP03 UTC result for configure azure-to-azure replication behind explicit approval.
- Exact run-owned resource/object ID returned by the commands in LAB25-CP03.
- Positive assertion proving: When AZ104_ENABLE_ASR=YES, fabric, containers, policy, mapping, and protected item converge to a protected state; otherwise the optional checkpoint is skipped.
- Negative assertion proving absence of: Replication health is reported health.

Common failure and safe retry: A non-affirmative gate value must never start costly replication, and partial configuration can take many minutes to converge. Retry LAB25-CP03 for configure azure-to-azure replication behind explicit approval only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB25-CP04, LAB25-CP05, remove the exact manifest IDs created or configured by LAB25-CP03 for configure azure-to-azure replication behind explicit approval; its residual probe must then return zero active IDs.

## Task 4 — Run and clean up an isolated test failover {#task-4}

Checkpoint: `LAB25-CP04`

Purpose and operational relevance: Exercise the deterministic operational or denied path needed to run and clean up an isolated test failover, then retain comparable before-and-after results. The change is unsafe when a test failover can be blocked while replication health is not Normal or a previous test VM still exists. This checkpoint therefore proves: When AZ104_RUN_ASR_TEST_FAILOVER=YES, the test uses only the isolated recovery VNet and cleanup removes the test VM before checkpoint completion.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$testVnetId = az network vnet show --resource-group $ResourceGroupName --name $testVnet --query id --output tsv
$protectedItemUrl = "https://management.azure.com/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName/providers/Microsoft.RecoveryServices/vaults/$vault/replicationFabrics/$sourceFabric/replicationProtectionContainers/$sourceContainer/replicationProtectedItems/$protectedItem"
$apiVersion = '2026-02-01'
$testSubmittedAt = (Get-Date).ToUniversalTime()
$testBody = @{ properties = @{ failoverDirection = 'PrimaryToRecovery'; networkId = $testVnetId; networkType = 'VmNetworkAsInput'; providerSpecificDetails = @{ instanceType = 'A2A' } } } | ConvertTo-Json -Depth 10 -Compress
if (($testBody | ConvertFrom-Json).properties.networkId -ne $testVnetId) { throw 'The test-failover request body does not contain the isolated VNet ID.' }
az rest --method post --url "${protectedItemUrl}/testFailover?api-version=$apiVersion" --body $testBody --headers 'Content-Type=application/json' --output none
$deadline = (Get-Date).AddMinutes(60)
$observedAsyncState = $false
do {
    Start-Sleep -Seconds 30
    $testState = az rest --method get --url "${protectedItemUrl}?api-version=$apiVersion" --query properties.testFailoverState --output tsv
    if ($testState -match 'InProgress|Waiting|Completed') { $observedAsyncState = $true }
} until ($testState -match 'WaitingForCompletion|Completed' -or (Get-Date) -gt $deadline)
if (-not $observedAsyncState -or $testState -notmatch 'WaitingForCompletion|Completed') { throw "Test failover did not complete its asynchronous operation; current state is $testState." }
$cleanupBody = @{ properties = @{ comments = "AZ-104 $RunId isolated drill complete" } } | ConvertTo-Json -Depth 5 -Compress
az rest --method post --url "${protectedItemUrl}/testFailoverCleanup?api-version=$apiVersion" --body $cleanupBody --headers 'Content-Type=application/json' --output none
$cleanupDeadline = (Get-Date).AddMinutes(60)
do {
    Start-Sleep -Seconds 30
    $cleanupState = az rest --method get --url "${protectedItemUrl}?api-version=$apiVersion" --query properties.testFailoverState --output tsv
} until ([string]::IsNullOrWhiteSpace($cleanupState) -or $cleanupState -match 'None|Cleaned|Completed' -or (Get-Date) -gt $cleanupDeadline)
$lastTest = az rest --method get --url "${protectedItemUrl}?api-version=$apiVersion" --query properties.lastSuccessfulTestFailoverTime --output tsv
if (-not $lastTest -or [datetime]$lastTest -lt $testSubmittedAt) { throw 'The protected item does not record this successful test failover.' }
if (-not [string]::IsNullOrWhiteSpace($cleanupState) -and $cleanupState -notmatch 'None|Cleaned|Completed') { throw "Test-failover cleanup did not complete; current state is $cleanupState." }
```

Expected state: When AZ104_RUN_ASR_TEST_FAILOVER=YES, the test uses only the isolated recovery VNet and cleanup removes the test VM before checkpoint completion.

Representative redacted output:

```text
When AZ104_RUN_ASR_TEST_FAILOVER=YES, the test uses only the isolated recovery VNet and cleanup removes the test VM before checkpoint completion.
```

Positive validation:

```powershell
$lastTest = az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --query properties.lastSuccessfulTestFailoverTime --output tsv
if (-not $lastTest) { throw 'No successful test-failover timestamp is recorded.' }
```

Expected positive result: When AZ104_RUN_ASR_TEST_FAILOVER=YES, the test uses only the isolated recovery VNet and cleanup removes the test VM before checkpoint completion.

Negative validation:

```powershell
$peerings = az network vnet peering list --resource-group $ResourceGroupName --vnet-name $testVnet --query "length(@)" --output tsv
if ([int]$peerings -ne 0) { throw 'The drill network is connected to another VNet.' }
```

Expected negative result: LAB25-CP04 negative boundary: The undesired state is absent; the negative assertion must not report: The drill network is connected to another VNet.

Evidence to retain:

- LAB25-CP04 UTC result for run and clean up an isolated test failover.
- Exact run-owned resource/object ID returned by the commands in LAB25-CP04.
- Positive assertion proving: When AZ104_RUN_ASR_TEST_FAILOVER=YES, the test uses only the isolated recovery VNet and cleanup removes the test VM before checkpoint completion.
- Negative assertion proving absence of: The drill network is connected to another VNet.

Common failure and safe retry: A test failover can be blocked while replication health is not Normal or a previous test VM still exists. Retry LAB25-CP04 for run and clean up an isolated test failover only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB25-CP05, remove the exact manifest IDs created or configured by LAB25-CP04 for run and clean up an isolated test failover; its residual probe must then return zero active IDs.

## Task 5 — Reconcile replication health, recovery mapping, and cleanup order {#task-5}

Checkpoint: `LAB25-CP05`

Purpose and operational relevance: Reconcile live service properties, returned IDs, and dependency-aware removal needed to reconcile replication health, recovery mapping, and cleanup order before handoff. The change is unsafe when removing fabric or policy before disabling protection leaves dependent ASR objects and prevents vault deletion. This checkpoint therefore proves: Optional gate status, protected-item health, network mapping, test-failover cleanup, and retained-vault expectations are explicit.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
az backup vault show --resource-group $ResourceGroupName --name $vault --query "{state:properties.provisioningState,location:location}" --output json
az network vnet list --resource-group $ResourceGroupName --query "[].{name:name,location:location,prefix:addressSpace.addressPrefixes[0],peerings:length(virtualNetworkPeerings)}" --output table
```

Expected state: Optional gate status, protected-item health, network mapping, test-failover cleanup, and retained-vault expectations are explicit.

Representative redacted output:

```text
Optional gate status, protected-item health, network mapping, test-failover cleanup, and retained-vault expectations are explicit.
```

Positive validation:

```powershell
$vaultState = az backup vault show --resource-group $ResourceGroupName --name $vault --query properties.provisioningState --output tsv
if ($vaultState -ne 'Succeeded') { throw "Site Recovery vault state is $vaultState." }
```

Expected positive result: Optional gate status, protected-item health, network mapping, test-failover cleanup, and retained-vault expectations are explicit.

Negative validation:

```powershell
$overlap = az network vnet show --resource-group $ResourceGroupName --name $testVnet --query "addressSpace.addressPrefixes[0]" --output tsv
if ($overlap -ne '10.126.0.0/16') { throw 'The test-failover VNet is not the recorded isolated range.' }
```

Expected negative result: LAB25-CP05 negative boundary: The undesired state is absent; the negative assertion must not report: The test-failover VNet is not the recorded isolated range.

Evidence to retain:

- LAB25-CP05 UTC result for reconcile replication health, recovery mapping, and cleanup order.
- Exact run-owned resource/object ID returned by the commands in LAB25-CP05.
- Positive assertion proving: Optional gate status, protected-item health, network mapping, test-failover cleanup, and retained-vault expectations are explicit.
- Negative assertion proving absence of: The test-failover VNet is not the recorded isolated range.

Common failure and safe retry: Removing fabric or policy before disabling protection leaves dependent ASR objects and prevents vault deletion. Retry LAB25-CP05 for reconcile replication health, recovery mapping, and cleanup order only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After all service validation and evidence capture, remove the exact manifest IDs created or configured by LAB25-CP05 for reconcile replication health, recovery mapping, and cleanup order; its residual probe must then return zero active IDs.

## Final validation and result interpretation

Run independent deployment validation after all required checkpoints:

```powershell
./scripts/cli/Validate.ps1 -RunId 'az104l25-01' -Mode Deployment
az resource list --resource-group 'rg-az104-l25-az104l25-01' --query '[].{name:name,type:type}' --output table
```

- `pass`: every required positive and negative check passed.
- `partial`: every required check passed, but at least one optional gate was deliberately skipped.
- `fail`: a required checkpoint failed; do not record the lab as complete.

Keep the redacted `validation.json`; do not retain credentials, tokens, access keys, certificate material, email addresses, tenant IDs, or unredacted command output.

## Deterministic break/fix exercise

Injection: Attempt to use the recovery VNet rather than the isolated test VNet for a drill request.

Inject the bounded fault:

```powershell
$candidateNetworkId = az network vnet show --resource-group $ResourceGroupName --name $recoveryVnet --query id --output tsv; if ($candidateNetworkId -notmatch "/virtualNetworks/$testVnet$") { throw "Safety gate: candidate is not the isolated test VNet." }
```

Capture the failed state with a read-only query:

```powershell
az network vnet list --resource-group $ResourceGroupName --query "[].{name:name,prefix:addressSpace.addressPrefixes[0],peerings:length(virtualNetworkPeerings)}" --output table
```

Repair only the injected setting, then repeat the same query:

```powershell
$candidateNetworkId = az network vnet show --resource-group $ResourceGroupName --name $testVnet --query id --output tsv
if ($candidateNetworkId -notmatch "/virtualNetworks/$testVnet$") { throw "The isolated test VNet is not selected." }
```

Expected symptom: The lab safety assertion refuses the drill because the requested network is not the recorded isolated range.

Diagnose with a read-only service query:

```powershell
az network vnet list --resource-group $ResourceGroupName --query "[].{name:name,prefix:addressSpace.addressPrefixes[0],peerings:length(virtualNetworkPeerings)}" --output table
```

Diagnosis: Compare exact VNet IDs, address spaces, and peerings before submitting test failover.

Repair: Use only the unpeered test VNet ID and re-run the gated test-failover request.

Before/after evidence must show the failed negative or positive check before repair and the same check passing afterward. Do not inject a second fault until the first is removed.

## Optional job-style challenge

Draft a failover decision tree covering test, planned, unplanned, commit, reprotect, and failback.

Deliver a short change record containing assumptions, exact commands, redacted evidence, cost and risk notes, rollback, and residual results. The challenge is optional and never changes required checkpoint status.

## Troubleshooting

| Symptom | Likely cause | Safe next step |
|---|---|---|
| Context mismatch | Active CLI context differs from `run.json` | Stop, inspect `az account show`, and select the intended disposable context yourself. |
| Provider or feature unavailable | Registration, region, feature, or SKU gate is unmet | Read the preflight result; do not register or enable tenant features implicitly. |
| Name already exists | The run ID is reused or a globally unique name collided | Keep existing state intact and choose a new run ID. |
| Expected state is delayed | The service is converging asynchronously | Repeat only the read-only query with bounded retries; do not duplicate creation. |
| Permission denied | Role, Graph scope, or data-plane authorization is insufficient | Confirm the declared least-privilege boundary; do not broaden access automatically. |
| Cleanup refuses ownership | ID, context, or tags differ from the manifest | Investigate the mismatch; never bypass ownership verification. |

## Cleanup and residual verification

Preview exact targets first, execute only after ownership review, then validate post-cleanup:

```powershell
./scripts/cli/Cleanup.ps1 -RunId 'az104l25-01'
./scripts/cli/Cleanup.ps1 -RunId 'az104l25-01' -Execute
./scripts/cli/Validate.ps1 -RunId 'az104l25-01' -Mode PostCleanup
$overlap = az network vnet show --resource-group $ResourceGroupName --name $testVnet --query "addressSpace.addressPrefixes[0]" --output tsv
if ($overlap -ne '10.126.0.0/16') { throw 'The test-failover VNet is not the recorded isolated range.' }
```

`cleanup.json` passes only when no active manifest-managed object remains. Soft-deleted or intentionally retained items must be listed with their reason and expected disposition. The lifecycle never performs irreversible purge automatically.

## Exam debrief and assessment

Explain why the expected state, negative check, and cleanup boundary matter—not only which command was used. Map any missed concept back to its task anchor before reviewing the answer key.

Complete [QUESTIONS.md](assessment/QUESTIONS.md), then use [ANSWERS.md](assessment/ANSWERS.md) for option-by-option remediation. Scores of 85–100% indicate mastery, 70–84% indicate targeted review, and below 70% means repeat the mapped tasks.

## Microsoft Learn sources

- [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Azure CLI Site Recovery extension](https://learn.microsoft.com/en-us/cli/azure/site-recovery)
- [Enable an Azure-to-Azure protected item with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/site-recovery/protected-item)
- [Run an isolated Site Recovery test failover](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-test-failover-to-azure)
- [Site Recovery test-failover REST operation](https://learn.microsoft.com/en-us/rest/api/site-recovery/replication-protected-items/test-failover)

## Lifecycle script appendix

The guided task blocks above and these executable scripts are generated from the same checkpoint data. The scripts are an optional automated lane; use a different run ID if you already completed the guided lane.

### `Preflight.ps1`

```powershell
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
    [string]$SecondaryLocation = $env:AZ104_SECONDARY_LOCATION
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Run the repository readiness initializer, then retry.'
}

$account = az account show --output json | ConvertFrom-Json
if (-not $account) { throw 'No active Azure CLI context. Run az login deliberately before this lab.' }
if ($SubscriptionId -and [string]$account.id -ne $SubscriptionId) {
    throw "Context mismatch: active subscription is $($account.id), expected $SubscriptionId. Preflight will not switch it."
}
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
# The account read above is the mandatory context gate. All remaining Azure
# probes are collected as results instead of allowing one unavailable SKU or
# provider query to abort the readiness report before it can explain the gap.
$PSNativeCommandUseErrorActionPreference = $false
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$ResourceGroupName = $(if ('25' -in @('00', '01', '02')) { $null } else { "rg-az104-l25-$RunId" })

$checks = [System.Collections.Generic.List[object]]::new()
function Add-PreflightResult {
    param([string]$Id, [bool]$Required, [bool]$Passed, [string]$Actual)
    $checks.Add([pscustomobject]@{ id = $Id; required = $Required; passed = $Passed; actual = $Actual })
}

Add-PreflightResult -Id 'context' -Required $true -Passed $true -Actual "cloud=$($account.environmentName); tenant=<redacted>; subscription=<redacted>"
$azVersion = (az version --query '"azure-cli"' --output tsv)
$bicepVersion = (az bicep version 2>&1 | Out-String).Trim()
Add-PreflightResult -Id 'azure-cli' -Required $true -Passed ([bool]$azVersion) -Actual $azVersion
Add-PreflightResult -Id 'powershell' -Required $true -Passed ($PSVersionTable.PSVersion -ge [version]'7.4') -Actual $PSVersionTable.PSVersion.ToString()
Add-PreflightResult -Id 'bicep' -Required $true -Passed ([bool]$bicepVersion) -Actual $bicepVersion

$requiredEnvironmentVariables = @()
foreach ($variableName in $requiredEnvironmentVariables) {
    $present = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable($variableName))
    Add-PreflightResult -Id "input:$variableName" -Required $true -Passed $present -Actual $(if ($present) { 'present (value redacted)' } else { 'missing' })
}

$providers = @(
    'Microsoft.Compute'
    'Microsoft.Network'
    'Microsoft.RecoveryServices'
    'Microsoft.Storage'
)
foreach ($provider in $providers) {
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    Add-PreflightResult -Id "provider:$provider" -Required $true -Passed ($registrationState -eq 'Registered') -Actual $(if ($registrationState) { $registrationState } else { 'Unavailable' })
}

$knownLocation = az account list-locations --query "[?name=='$Location'].name | [0]" --output tsv
Add-PreflightResult -Id 'region' -Required $true -Passed ($knownLocation -eq $Location) -Actual $(if ($knownLocation) { $knownLocation } else { 'not available' })

$gateMatches = [string]::Equals([Environment]::GetEnvironmentVariable('AZ104_ENABLE_ASR'), 'YES', [StringComparison]::Ordinal)
Add-PreflightResult -Id 'optional-gate:AZ104_ENABLE_ASR' -Required $false -Passed $gateMatches -Actual $(if ($gateMatches) { 'exact affirmative value supplied (value redacted)' } else { 'absent or not exact; checkpoint will be skipped' })

$gateMatches = [string]::Equals([Environment]::GetEnvironmentVariable('AZ104_RUN_ASR_TEST_FAILOVER'), 'YES', [StringComparison]::Ordinal)
Add-PreflightResult -Id 'optional-gate:AZ104_RUN_ASR_TEST_FAILOVER' -Required $false -Passed $gateMatches -Actual $(if ($gateMatches) { 'exact affirmative value supplied (value redacted)' } else { 'absent or not exact; checkpoint will be skipped' })

$usage = az vm list-usage --location $Location --output json 2>$null | ConvertFrom-Json
Add-PreflightResult -Id 'regional-compute-quota' -Required $false -Passed ($LASTEXITCODE -eq 0) -Actual "entries=$(@($usage).Count)"

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
$extension = az extension show --name site-recovery --query version --output tsv
if (-not $extension) { throw 'The site-recovery Azure CLI extension is not installed.' }
if (-not $SecondaryLocation -or $SecondaryLocation -eq $Location) { throw 'Primary and recovery locations must be distinct.' }
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.service' -Required $true -Passed $probePassed -Actual $probeActual

$checks | Format-Table -AutoSize
$failedRequired = @($checks | Where-Object { $_.required -and -not $_.passed })
if ($failedRequired.Count -gt 0) {
    throw "Preflight blocked: $($failedRequired.id -join ', ')"
}
Write-Host 'Preflight passed. It performed no sign-in, context switch, provider registration, or Azure mutation.'
# END GENERATED AZ104 V2
```

### `Setup.ps1`

```powershell
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
$ResourceGroupName = $(if ('25' -in @('00', '01', '02')) { $null } else { "rg-az104-l25-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-25 execution plan'
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
    labId = 'LAB-25'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB25-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB25-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB25-CP03'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB25-CP04'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB25-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '25'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB25-CP01' } else { $CheckpointId })
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
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=25 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB25-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB25-CP01'
}

# CHECKPOINT LAB25-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB25-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB25-CP01'
    Save-RunState

    if (-not $SecondaryLocation -or $SecondaryLocation -eq $Location) { throw 'Supply a distinct approved secondary region.' }
    az extension show --name site-recovery --query version --output tsv
    az provider show --namespace Microsoft.RecoveryServices --query registrationState --output tsv
    az vm list-skus --location $Location --size Standard_B1s --all --query "[?name=='Standard_B1s'].name" --output tsv
    if (-not (Get-Command ssh-keygen -ErrorAction SilentlyContinue)) { throw 'ssh-keygen is required for the source VM key.' }

    Sync-ManagedResource -CheckpointId 'LAB25-CP01'
    Write-CheckpointState -CheckpointId 'LAB25-CP01' -Status 'pass' -Message 'Source and recovery regions differ, the VM SKU is available, and the site-recovery extension/provider commands are ready.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB25-CP01'
    Write-CheckpointState -CheckpointId 'LAB25-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB25-CP01 END

# CHECKPOINT LAB25-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB25-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB25-CP02'
    Save-RunState

    $vault = "asr-$suffix"; $vm = "vm-$suffix"; $sourceVnet = "source-$suffix"; $recoveryVnet = "recovery-$suffix"; $testVnet = "test-$suffix"; $cache = "st25$suffix"
    $keyPath = Join-Path $StateDir 'id_ed25519'; ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
    try {
        az network vnet create --resource-group $ResourceGroupName --name $sourceVnet --location $Location --address-prefixes 10.25.0.0/16 --subnet-name workload --subnet-prefixes 10.25.1.0/24 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    }
    try {
        az network nic create --resource-group $ResourceGroupName --name "nic-$suffix" --location $Location --vnet-name $sourceVnet --subnet workload --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    }
    try {
        az vm create --resource-group $ResourceGroupName --name $vm --location $Location --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --nics "nic-$suffix" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    }
    try {
        az network vnet create --resource-group $ResourceGroupName --name $recoveryVnet --location $SecondaryLocation --address-prefixes 10.26.0.0/16 --subnet-name recovery --subnet-prefixes 10.26.1.0/24 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    }
    try {
        az network vnet create --resource-group $ResourceGroupName --name $testVnet --location $SecondaryLocation --address-prefixes 10.126.0.0/16 --subnet-name isolated --subnet-prefixes 10.126.1.0/24 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    }
    try {
        az storage account create --resource-group $ResourceGroupName --name $cache --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    }
    try {
        az backup vault create --resource-group $ResourceGroupName --name $vault --location $SecondaryLocation --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    }

    Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    Write-CheckpointState -CheckpointId 'LAB25-CP02' -Status 'pass' -Message 'The private source VM, cache storage, source/recovery VNets, and vault are recorded before replication is gated.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB25-CP02'
    Write-CheckpointState -CheckpointId 'LAB25-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB25-CP02 END

# CHECKPOINT LAB25-CP03 BEGIN
if (-not ([string]::Equals([Environment]::GetEnvironmentVariable('AZ104_ENABLE_ASR'), 'YES', [StringComparison]::Ordinal))) {
    Write-CheckpointState -CheckpointId 'LAB25-CP03' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB25-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB25-CP03'
    Save-RunState

    $sourceFabric = "fabric-source-$suffix"; $recoveryFabric = "fabric-recovery-$suffix"; $sourceContainer = "container-source-$suffix"; $recoveryContainer = "container-recovery-$suffix"; $mapping = "mapping-$suffix"; $policy = "policy-$suffix"; $protectedItem = "protected-$suffix"
    try {
        az site-recovery fabric create --resource-group $ResourceGroupName --vault-name $vault --name $sourceFabric --custom-details "{azure:{location:$Location}}" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    }
    try {
        az site-recovery fabric create --resource-group $ResourceGroupName --vault-name $vault --name $recoveryFabric --custom-details "{azure:{location:$SecondaryLocation}}" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    }
    try {
        az site-recovery protection-container create --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --name $sourceContainer --provider-input '[{instance-type:A2A}]' --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    }
    try {
        az site-recovery protection-container create --resource-group $ResourceGroupName --vault-name $vault --fabric-name $recoveryFabric --name $recoveryContainer --provider-input '[{instance-type:A2A}]' --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    }
    try {
        az site-recovery policy create --resource-group $ResourceGroupName --vault-name $vault --name $policy --provider-specific-input '{a2a:{multi-vm-sync-status:Enable}}' --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    }
    $policyId = az site-recovery policy show --resource-group $ResourceGroupName --vault-name $vault --name $policy --query id --output tsv
    $recoveryContainerId = az site-recovery protection-container show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $recoveryFabric --name $recoveryContainer --query id --output tsv
    try {
        az site-recovery protection-container mapping create --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $mapping --policy-id $policyId --target-container $recoveryContainerId --provider-input '{a2a:{agent-auto-update-status:Disabled}}' --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    }
    $vmId = az vm show --resource-group $ResourceGroupName --name $vm --query id --output tsv
    $osDiskId = az vm show --resource-group $ResourceGroupName --name $vm --query storageProfile.osDisk.managedDisk.id --output tsv
    $cacheId = az storage account show --resource-group $ResourceGroupName --name "st25$suffix" --query id --output tsv
    $recoveryVnetId = az network vnet show --resource-group $ResourceGroupName --name $recoveryVnet --query id --output tsv
    $recoveryGroupId = az group show --name $ResourceGroupName --query id --output tsv
    $providerDetails = @{ a2a = @{ 'fabric-object-id' = $vmId; 'vm-managed-disks' = @(@{ 'disk-id' = $osDiskId; 'primary-staging-azure-storage-account-id' = $cacheId; 'recovery-resource-group-id' = $recoveryGroupId }); 'recovery-azure-network-id' = $recoveryVnetId; 'recovery-container-id' = $recoveryContainerId; 'recovery-resource-group-id' = $recoveryGroupId; 'recovery-subnet-name' = 'recovery' } } | ConvertTo-Json -Depth 10 -Compress
    try {
        az site-recovery protected-item create --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --policy-id $policyId --provider-details $providerDetails --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    }
    $deadline = (Get-Date).AddMinutes(90)
    do { Start-Sleep -Seconds 30; $protectionState = az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --query properties.protectionState --output tsv } until ($protectionState -eq 'Protected' -or (Get-Date) -gt $deadline)
    if ($protectionState -ne 'Protected') { throw "Site Recovery did not reach Protected within the bounded wait; current state is $protectionState." }

    Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    Write-CheckpointState -CheckpointId 'LAB25-CP03' -Status 'pass' -Message 'When AZ104_ENABLE_ASR=YES, fabric, containers, policy, mapping, and protected item converge to a protected state; otherwise the optional checkpoint is skipped.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB25-CP03'
    Write-CheckpointState -CheckpointId 'LAB25-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB25-CP03 END

# CHECKPOINT LAB25-CP04 BEGIN
if (-not ([string]::Equals([Environment]::GetEnvironmentVariable('AZ104_ENABLE_ASR'), 'YES', [StringComparison]::Ordinal) -and [string]::Equals([Environment]::GetEnvironmentVariable('AZ104_RUN_ASR_TEST_FAILOVER'), 'YES', [StringComparison]::Ordinal))) {
    Write-CheckpointState -CheckpointId 'LAB25-CP04' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB25-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB25-CP04'
    Save-RunState

    $testVnetId = az network vnet show --resource-group $ResourceGroupName --name $testVnet --query id --output tsv
    $protectedItemUrl = "https://management.azure.com/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName/providers/Microsoft.RecoveryServices/vaults/$vault/replicationFabrics/$sourceFabric/replicationProtectionContainers/$sourceContainer/replicationProtectedItems/$protectedItem"
    $apiVersion = '2026-02-01'
    $testSubmittedAt = (Get-Date).ToUniversalTime()
    $testBody = @{ properties = @{ failoverDirection = 'PrimaryToRecovery'; networkId = $testVnetId; networkType = 'VmNetworkAsInput'; providerSpecificDetails = @{ instanceType = 'A2A' } } } | ConvertTo-Json -Depth 10 -Compress
    if (($testBody | ConvertFrom-Json).properties.networkId -ne $testVnetId) { throw 'The test-failover request body does not contain the isolated VNet ID.' }
    try {
        az rest --method post --url "${protectedItemUrl}/testFailover?api-version=$apiVersion" --body $testBody --headers 'Content-Type=application/json' --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP04'
    }
    $deadline = (Get-Date).AddMinutes(60)
    $observedAsyncState = $false
    do {
        Start-Sleep -Seconds 30
        $testState = az rest --method get --url "${protectedItemUrl}?api-version=$apiVersion" --query properties.testFailoverState --output tsv
        if ($testState -match 'InProgress|Waiting|Completed') { $observedAsyncState = $true }
    } until ($testState -match 'WaitingForCompletion|Completed' -or (Get-Date) -gt $deadline)
    if (-not $observedAsyncState -or $testState -notmatch 'WaitingForCompletion|Completed') { throw "Test failover did not complete its asynchronous operation; current state is $testState." }
    $cleanupBody = @{ properties = @{ comments = "AZ-104 $RunId isolated drill complete" } } | ConvertTo-Json -Depth 5 -Compress
    try {
        az rest --method post --url "${protectedItemUrl}/testFailoverCleanup?api-version=$apiVersion" --body $cleanupBody --headers 'Content-Type=application/json' --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB25-CP04'
    }
    $cleanupDeadline = (Get-Date).AddMinutes(60)
    do {
        Start-Sleep -Seconds 30
        $cleanupState = az rest --method get --url "${protectedItemUrl}?api-version=$apiVersion" --query properties.testFailoverState --output tsv
    } until ([string]::IsNullOrWhiteSpace($cleanupState) -or $cleanupState -match 'None|Cleaned|Completed' -or (Get-Date) -gt $cleanupDeadline)
    $lastTest = az rest --method get --url "${protectedItemUrl}?api-version=$apiVersion" --query properties.lastSuccessfulTestFailoverTime --output tsv
    if (-not $lastTest -or [datetime]$lastTest -lt $testSubmittedAt) { throw 'The protected item does not record this successful test failover.' }
    if (-not [string]::IsNullOrWhiteSpace($cleanupState) -and $cleanupState -notmatch 'None|Cleaned|Completed') { throw "Test-failover cleanup did not complete; current state is $cleanupState." }

    Sync-ManagedResource -CheckpointId 'LAB25-CP04'
    Write-CheckpointState -CheckpointId 'LAB25-CP04' -Status 'pass' -Message 'When AZ104_RUN_ASR_TEST_FAILOVER=YES, the test uses only the isolated recovery VNet and cleanup removes the test VM before checkpoint completion.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB25-CP04'
    Write-CheckpointState -CheckpointId 'LAB25-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB25-CP04 END

# CHECKPOINT LAB25-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB25-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB25-CP05'
    Save-RunState

    az backup vault show --resource-group $ResourceGroupName --name $vault --query "{state:properties.provisioningState,location:location}" --output json
    az network vnet list --resource-group $ResourceGroupName --query "[].{name:name,location:location,prefix:addressSpace.addressPrefixes[0],peerings:length(virtualNetworkPeerings)}" --output table

    Sync-ManagedResource -CheckpointId 'LAB25-CP05'
    Write-CheckpointState -CheckpointId 'LAB25-CP05' -Status 'pass' -Message 'Optional gate status, protected-item health, network mapping, test-failover cleanup, and retained-vault expectations are explicit.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB25-CP05'
    Write-CheckpointState -CheckpointId 'LAB25-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB25-CP05 END

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
```

### `Validate.ps1`

```powershell
# BEGIN GENERATED AZ104 V2
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment'
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
$ValidationPath = Join-Path $StateDir 'validation.json'
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Run manifest not found: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -AsHashtable
if ($state.labId -ne 'LAB-25' -or $state.runId -ne $RunId) { throw 'Manifest ownership does not match this lab and run ID.' }
$PSNativeCommandUseErrorActionPreference = $false
$accountJson = az account show --output json 2>$null
$account = $(if ($LASTEXITCODE -eq 0 -and $accountJson) { $accountJson | ConvertFrom-Json } else { $null })
if (-not $account -or [string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $actualContext = $(if ($account) { "tenant=$($account.tenantId); subscription=$($account.id)" } else { 'active context unavailable' })
    $contextFailure = @{
        schemaVersion = '1.0.0'; labId = 'LAB-25'; runId = $RunId; mode = $Mode
        generatedAt = $capturedAt; result = 'fail'
        summary = @{ required = 1; passed = 0; failed = 1; skipped = 0 }
        checks = @(@{ id = 'context.active'; checkpointId = 'LAB25-CP01'; kind = 'context'; required = $true; status = 'fail'; message = 'Active Azure context does not match the run manifest.'; evidence = @{ command = 'az account show --output json'; expected = 'tenant and subscription exactly match run.json'; actual = $actualContext; capturedAt = $capturedAt; redacted = $true } })
    }
    $contextFailure | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
    Write-Host "Validation $Mode result: fail"
    Write-Host "Artifact: $ValidationPath"
    exit 1
}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('25' -in @('00', '01', '02')) { $null } else { "rg-az104-l25-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$vault = "asr-$suffix"; $vm = "vm-$suffix"; $sourceVnet = "source-$suffix"; $recoveryVnet = "recovery-$suffix"; $testVnet = "test-$suffix"
$sourceFabric = "fabric-source-$suffix"; $recoveryFabric = "fabric-recovery-$suffix"; $sourceContainer = "container-source-$suffix"; $recoveryContainer = "container-recovery-$suffix"; $protectedItem = "protected-$suffix"

$checks = [System.Collections.Generic.List[object]]::new()
function Add-ValidationCheck {
    param([string]$Id, [string]$CheckpointId, [string]$Kind, [bool]$Required, [bool]$Passed, [string]$Command, [string]$Expected, [string]$Actual, [bool]$Skipped = $false)
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $checks.Add(@{
        id = $Id
        checkpointId = $CheckpointId
        kind = $Kind
        required = $Required
        status = $(if ($Skipped) { 'skipped' } elseif ($Passed) { 'pass' } else { 'fail' })
        message = $(if ($Skipped) { 'Optional gate was deliberately skipped.' } elseif ($Passed) { 'Expected state observed.' } else { 'Expected state was not observed.' })
        evidence = @{ command = $Command; expected = $Expected; actual = $Actual; capturedAt = $capturedAt; redacted = $true }
    })
}

# CHECKPOINT LAB25-CP01 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB25-CP01' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP01' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab25-cp01.positive' -CheckpointId 'LAB25-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab25-cp01.negative' -CheckpointId 'LAB25-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$extension = az extension show --name site-recovery --query version --output tsv
if (-not $extension) { throw 'The site-recovery Azure CLI extension is not installed.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab25-cp01.positive' -CheckpointId 'LAB25-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$recoveryRegion = az account list-locations --query "[?name=='$SecondaryLocation'].name | [0]" --output tsv
if (-not $recoveryRegion -or $SecondaryLocation -eq $Location) {
  throw 'Primary and recovery locations must be distinct, available Azure regions.'
}
$recoveryRegion
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab25-cp01.negative' -CheckpointId 'LAB25-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab25-cp01.residual' -CheckpointId 'LAB25-CP01' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB25-CP01 END

# CHECKPOINT LAB25-CP02 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB25-CP02' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP02' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab25-cp02.positive' -CheckpointId 'LAB25-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab25-cp02.negative' -CheckpointId 'LAB25-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$vnetCount = az network vnet list --resource-group $ResourceGroupName --query "[?name=='$sourceVnet' || name=='$recoveryVnet' || name=='$testVnet'] | length(@)" --output tsv
if ([int]$vnetCount -ne 3) { throw 'The source, recovery, and isolated test VNets are not all present.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab25-cp02.positive' -CheckpointId 'LAB25-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$peerings = az network vnet peering list --resource-group $ResourceGroupName --vnet-name $testVnet --query "length(@)" --output tsv
if ([int]$peerings -ne 0) { throw 'The test-failover VNet is peered and is not isolated.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab25-cp02.negative' -CheckpointId 'LAB25-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab25-cp02.residual' -CheckpointId 'LAB25-CP02' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB25-CP02 END

# CHECKPOINT LAB25-CP03 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB25-CP03' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP03' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab25-cp03.positive' -CheckpointId 'LAB25-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab25-cp03.negative' -CheckpointId 'LAB25-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$stateValue = az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --query properties.protectionState --output tsv
if ($stateValue -ne 'Protected') { throw "Replication protection state is $stateValue." }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab25-cp03.positive' -CheckpointId 'LAB25-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$health = az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --query properties.replicationHealth --output tsv
if ($health -notin @('Normal','Healthy')) { throw "Replication health is $health." }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab25-cp03.negative' -CheckpointId 'LAB25-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab25-cp03.residual' -CheckpointId 'LAB25-CP03' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB25-CP03 END

# CHECKPOINT LAB25-CP04 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB25-CP04' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP04' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab25-cp04.positive' -CheckpointId 'LAB25-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab25-cp04.negative' -CheckpointId 'LAB25-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$lastTest = az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --query properties.lastSuccessfulTestFailoverTime --output tsv
if (-not $lastTest) { throw 'No successful test-failover timestamp is recorded.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab25-cp04.positive' -CheckpointId 'LAB25-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$peerings = az network vnet peering list --resource-group $ResourceGroupName --vnet-name $testVnet --query "length(@)" --output tsv
if ([int]$peerings -ne 0) { throw 'The drill network is connected to another VNet.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab25-cp04.negative' -CheckpointId 'LAB25-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab25-cp04.residual' -CheckpointId 'LAB25-CP04' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB25-CP04 END

# CHECKPOINT LAB25-CP05 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB25-CP05' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP05' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab25-cp05.positive' -CheckpointId 'LAB25-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab25-cp05.negative' -CheckpointId 'LAB25-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$vaultState = az backup vault show --resource-group $ResourceGroupName --name $vault --query properties.provisioningState --output tsv
if ($vaultState -ne 'Succeeded') { throw "Site Recovery vault state is $vaultState." }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab25-cp05.positive' -CheckpointId 'LAB25-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$overlap = az network vnet show --resource-group $ResourceGroupName --name $testVnet --query "addressSpace.addressPrefixes[0]" --output tsv
if ($overlap -ne '10.126.0.0/16') { throw 'The test-failover VNet is not the recorded isolated range.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab25-cp05.negative' -CheckpointId 'LAB25-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab25-cp05.residual' -CheckpointId 'LAB25-CP05' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB25-CP05 END

$requiredChecks = @($checks | Where-Object { $_.required })
$failedChecks = @($checks | Where-Object { $_.status -eq 'fail' })
$requiredSkippedChecks = @($checks | Where-Object { $_.required -and $_.status -eq 'skipped' })
$skippedChecks = @($checks | Where-Object { $_.status -eq 'skipped' })
$result = if ($failedChecks.Count -gt 0 -or $requiredSkippedChecks.Count -gt 0) { 'fail' } elseif ($skippedChecks.Count -gt 0) { 'partial' } else { 'pass' }
$document = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-25'
    runId = $RunId
    mode = $Mode
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    result = $result
    summary = @{
        required = $requiredChecks.Count
        passed = @($checks | Where-Object { $_.status -eq 'pass' }).Count
        failed = $failedChecks.Count
        skipped = $skippedChecks.Count
    }
    checks = @($checks)
}
$document | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
Write-Host "Validation $Mode result: $result"
Write-Host "Artifact: $ValidationPath"
if ($result -eq 'fail') { exit 1 }
# END GENERATED AZ104 V2
```

### `Cleanup.ps1`

```powershell
# BEGIN GENERATED AZ104 V2
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
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
$CleanupPath = Join-Path $StateDir 'cleanup.json'
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Run manifest not found: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -AsHashtable
$active = @($state.managedObjects | Where-Object { $_.lifecycleStatus -eq 'active' })
function Write-CleanupRefusal {
    param([string]$Message)
    $refusalActions = @($active | ForEach-Object {
        @{ checkpointId = [string]$_.checkpointId; targetId = [string]$_.id; targetType = [string]$_.type; ownership = @{ method = [string]$_.ownership.method; verified = $false }; status = 'failed'; message = $Message }
    })
    $refusal = @{
        schemaVersion = '1.0.0'; labId = 'LAB-25'; runId = $RunId
        generatedAt = (Get-Date).ToUniversalTime().ToString('o')
        executionMode = $(if ($Execute) { 'execute' } else { 'preview' })
        result = $(if ($Execute) { 'fail' } else { 'preview' })
        ownershipVerified = $false; actions = $refusalActions
        residualChecks = @(@{ id = 'ownership.refusal'; command = 'compare manifest, active context, exact IDs, and ownership proof'; expected = 'all ownership checks pass before mutation'; actual = $Message; status = $(if ($Execute) { 'fail' } else { 'skipped' }) })
        activeManagedObjects = @($active | ForEach-Object id); retainedItems = @()
    }
    $refusal | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
    throw $Message
}
if ($state.labId -ne 'LAB-25' -or $state.runId -ne $RunId) {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: manifest lab ID or run ID does not match.'
}
if ($Execute -and $active.Count -eq 0 -and $state.status -eq 'cleaned') {
    $priorRetained = @()
    if (Test-Path -LiteralPath $CleanupPath) {
        try { $priorRetained = @((Get-Content -LiteralPath $CleanupPath -Raw | ConvertFrom-Json).retainedItems) } catch { $priorRetained = @() }
    }
    $idempotent = @{
        schemaVersion = '1.0.0'; labId = 'LAB-25'; runId = $RunId
        generatedAt = (Get-Date).ToUniversalTime().ToString('o'); executionMode = 'execute'; result = 'pass'
        ownershipVerified = $true; actions = @(); activeManagedObjects = @(); retainedItems = $priorRetained
        residualChecks = @(@{ id = 'cleanup.idempotent'; command = 'read run.json active managed-object inventory'; expected = 'zero active manifest-managed objects'; actual = 'active=0; prior cleanup already completed'; status = 'pass' })
    }
    $idempotent | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
    Write-Host 'Cleanup result: pass (already cleaned)'
    Write-Host "Artifact: $CleanupPath"
    return
}
try {
    $account = az account show --output json | ConvertFrom-Json
} catch {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: active Azure context could not be read.'
}
if ([string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: active context does not match the manifest.'
}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('25' -in @('00', '01', '02')) { $null } else { "rg-az104-l25-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$vault = "asr-$suffix"; $sourceFabric = "fabric-source-$suffix"; $recoveryFabric = "fabric-recovery-$suffix"; $sourceContainer = "container-source-$suffix"; $recoveryContainer = "container-recovery-$suffix"; $protectedItem = "protected-$suffix"; $mapping = "mapping-$suffix"; $policy = "policy-$suffix"

$ownershipVerified = $true
$verifiedOwnershipById = @{}
$absentIds = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$verifiedResourceGroupIds = [System.Collections.Generic.List[string]]::new()
$resourceGroupObjects = @($active | Where-Object { $_.type -eq 'Microsoft.Resources/resourceGroups' })
$resourceGroupObject = $resourceGroupObjects | Select-Object -First 1
$nativeProbePreference = $PSNativeCommandUseErrorActionPreference
$PSNativeCommandUseErrorActionPreference = $false

# A manifest entry is necessary but is not, by itself, proof of ownership. Verify
# each manifest-id-and-tags boundary against the live Azure tags before mutation.
foreach ($groupObject in $resourceGroupObjects) {
    $groupVerified = $false
    try {
        $tagJson = az group show --ids $groupObject.id --query tags --output json 2>$null
        if ($LASTEXITCODE -eq 0 -and $tagJson) {
            $tags = $tagJson | ConvertFrom-Json -AsHashtable
            $expectedTags = $groupObject.ownership.expectedTags
            $groupVerified =
                $groupObject.ownership.method -eq 'manifest-id-and-tags' -and
                [string]$tags['purpose'] -eq [string]$expectedTags['purpose'] -and
                [string]$tags['labId'] -eq [string]$expectedTags['labId'] -and
                [string]$tags['runId'] -eq [string]$expectedTags['runId'] -and
                [string]$tags['purpose'] -eq 'az104-lab' -and
                [string]$tags['labId'] -eq '25' -and
                [string]$tags['runId'] -eq $RunId
        } else {
            $groupExists = az group exists --subscription $state.context.subscriptionId --name $groupObject.name --output tsv 2>$null
            if ($LASTEXITCODE -eq 0 -and $groupExists -eq 'false') {
                $null = $absentIds.Add([string]$groupObject.id)
                $groupVerified = $true
            }
        }
    } catch {
        $groupVerified = $false
    }
    $verifiedOwnershipById[[string]$groupObject.id] = $groupVerified
    if ($groupVerified) { $verifiedResourceGroupIds.Add([string]$groupObject.id) }
    if (-not $groupVerified) { $ownershipVerified = $false }
}

foreach ($object in $active) {
    $objectId = [string]$object.id
    if ($verifiedOwnershipById.ContainsKey($objectId)) { continue }
    $method = [string]$object.ownership.method
    $objectVerified = $false

    $absentGroupBoundary = @($resourceGroupObjects | Where-Object {
        $absentIds.Contains([string]$_.id) -and $objectId.StartsWith("$($_.id)/", [System.StringComparison]::OrdinalIgnoreCase)
    }).Count -gt 0
    if ($absentGroupBoundary) {
        $null = $absentIds.Add($objectId)
        $verifiedOwnershipById[$objectId] = $true
        continue
    }

    if ($method -eq 'manifest-id-and-tags' -and $object.kind -eq 'azure-resource') {
        $expectedTags = $object.ownership.expectedTags
        $manifestTagsMatch =
            [string]$expectedTags['purpose'] -eq 'az104-lab' -and
            [string]$expectedTags['labId'] -eq '25' -and
            [string]$expectedTags['runId'] -eq $RunId
        $verifiedByGroupBoundary = @($verifiedResourceGroupIds | Where-Object {
            $objectId.StartsWith("$_/", [System.StringComparison]::OrdinalIgnoreCase)
        }).Count -gt 0
        $verifiedByOwnTags = $false
        try {
            $tagJson = az resource show --ids $objectId --query tags --output json 2>$null
            if ($LASTEXITCODE -eq 0 -and $tagJson) {
                $tags = $tagJson | ConvertFrom-Json -AsHashtable
                $verifiedByOwnTags =
                    [string]$tags['purpose'] -eq [string]$expectedTags['purpose'] -and
                    [string]$tags['labId'] -eq [string]$expectedTags['labId'] -and
                    [string]$tags['runId'] -eq [string]$expectedTags['runId']
            } elseif ($verifiedByGroupBoundary) {
                $parentGroupObject = $resourceGroupObjects | Where-Object { $objectId.StartsWith("$($_.id)/", [System.StringComparison]::OrdinalIgnoreCase) } | Select-Object -First 1
                $exactCount = az resource list --resource-group $parentGroupObject.name --query "[?id=='$objectId'] | length(@)" --output tsv 2>$null
                if ($LASTEXITCODE -eq 0 -and [int]$exactCount -eq 0) {
                    $null = $absentIds.Add($objectId)
                    $verifiedByOwnTags = $true
                }
            }
        } catch {
            $verifiedByOwnTags = $false
        }
        $objectVerified = $manifestTagsMatch -and ($verifiedByOwnTags -or $verifiedByGroupBoundary)
    } elseif ($method -eq 'manifest-id' -and $object.kind -eq 'azure-resource' -and $object.type -eq 'Microsoft.Management/managementGroups') {
        try {
            $managementGroupJson = az account management-group show --name $object.name --expand --recurse --output json 2>&1
            if ($LASTEXITCODE -eq 0) {
                $managementGroup = $managementGroupJson | ConvertFrom-Json
                $objectVerified = [string]$managementGroup.id -eq $objectId -and @($managementGroup.children).Count -eq 0
            } elseif ([string]$managementGroupJson -match '(?i)404|not.?found') {
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }
        } catch {
            $objectVerified = $false
        }
    } elseif ($method -eq 'manifest-id' -and $object.kind -eq 'entra-object') {
        try {
            $graphResult = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$objectId" --output none 2>&1
            if ($LASTEXITCODE -eq 0) {
                $objectVerified = $true
            } elseif ([string]$graphResult -match '(?i)404|Request_ResourceNotFound') {
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }
        } catch {
            $objectVerified = $false
        }
    } elseif ($method -eq 'manifest-id' -and $object.kind -eq 'azure-resource') {
        try {
            $resourceResult = az resource show --ids $objectId --output none 2>&1
            if ($LASTEXITCODE -eq 0) {
                $objectVerified = $true
            } elseif ([string]$resourceResult -match '(?i)404|ResourceNotFound|could not be found') {
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }
        } catch {
            $objectVerified = $false
        }
    } elseif ($method -eq 'local-path') {
        try {
            $candidate = if ([System.IO.Path]::IsPathRooted($objectId)) { $objectId } else { Join-Path $LabRoot $objectId }
            $fullPath = [System.IO.Path]::GetFullPath($candidate)
            $statePrefix = [System.IO.Path]::GetFullPath($StateDir).TrimEnd([System.IO.Path]::DirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
            $inStateBoundary = $fullPath.StartsWith($statePrefix, [System.StringComparison]::OrdinalIgnoreCase)
            $objectVerified = $inStateBoundary
            if ($inStateBoundary -and -not (Test-Path -LiteralPath $fullPath)) { $null = $absentIds.Add($objectId) }
        } catch {
            $objectVerified = $false
        }
    }

    $verifiedOwnershipById[$objectId] = $objectVerified
    if (-not $objectVerified) { $ownershipVerified = $false }
}
$PSNativeCommandUseErrorActionPreference = $nativeProbePreference

if (-not $ownershipVerified) {
    $failedOwnershipIds = @($active | Where-Object { -not $verifiedOwnershipById[[string]$_.id] } | ForEach-Object id)
    Write-CleanupRefusal -Message "Cleanup ownership refusal: live ID and ownership proof failed for $($failedOwnershipIds -join ', ')."
}

$actions = [System.Collections.Generic.List[object]]::new()
$residualChecks = [System.Collections.Generic.List[object]]::new()
if (-not $Execute) {
    Write-Host 'Preview only. The exact manifest-owned targets below will not be changed.'
}

# CHECKPOINT LAB25-CP05 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP05' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB25-CP05'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB25-CP05 END

# CHECKPOINT LAB25-CP04 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP04' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB25-CP04'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB25-CP04 END

# CHECKPOINT LAB25-CP03 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP03' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB25-CP03'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB25-CP03 END

# CHECKPOINT LAB25-CP02 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP02' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB25-CP02'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB25-CP02 END

# CHECKPOINT LAB25-CP01 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP01' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB25-CP01'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB25-CP01 END

$cleanupFailure = $null
if ($Execute) {
    $PSNativeCommandUseErrorActionPreference = $true
    $state.status = 'cleanup-in-progress'
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8

    try {
        # Restore shared or tenant-wide settings before removing the disposable
        # objects that were used to exercise them.
        foreach ($setting in @($state.originalSettings)) {
            if ($setting.targetId -eq 'authorizationPolicy' -and $setting.property -eq 'allowedToUseSSPR') {
                $restoreBody = @{ allowedToUseSSPR = [bool]$setting.value } | ConvertTo-Json -Compress
                az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --headers 'Content-Type=application/json' --body $restoreBody --output none
                $restored = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowedToUseSSPR' --query allowedToUseSSPR --output tsv
                if ([bool]::Parse([string]$restored) -ne [bool]$setting.value) {
                    throw 'Cleanup stopped because authorizationPolicy.allowedToUseSSPR was not restored.'
                }
            }
        }
        foreach ($object in @($active | Where-Object { $_.type -eq 'Microsoft.Management/managementGroups' -and -not $absentIds.Contains([string]$_.id) })) {
            az account management-group delete --name $object.name --output none
        }
        $hasLiveManagedTarget = @($active | Where-Object { -not $absentIds.Contains([string]$_.id) }).Count -gt 0
        if ($hasLiveManagedTarget) {
function Test-AsrObject {
    param([scriptblock]$Probe)
    $preference = $PSNativeCommandUseErrorActionPreference
    $PSNativeCommandUseErrorActionPreference = $false
    try { & $Probe *> $null; return ($LASTEXITCODE -eq 0) } finally { $PSNativeCommandUseErrorActionPreference = $preference }
}
function Wait-AsrAbsent {
    param([scriptblock]$Probe, [string]$Label, [int]$TimeoutMinutes = 60)
    $deadline = (Get-Date).AddMinutes($TimeoutMinutes)
    do {
        if (-not (Test-AsrObject -Probe $Probe)) { return }
        Start-Sleep -Seconds 30
    } until ((Get-Date) -gt $deadline)
    throw "Site Recovery cleanup timed out waiting for $Label to become absent."
}

$protectedProbe = { az site-recovery protected-item show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --output none }
if (Test-AsrObject -Probe $protectedProbe) {
    $protectedItemUrl = "https://management.azure.com/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName/providers/Microsoft.RecoveryServices/vaults/$vault/replicationFabrics/$sourceFabric/replicationProtectionContainers/$sourceContainer/replicationProtectedItems/$protectedItem"
    $apiVersion = '2026-02-01'
    $testState = az rest --method get --url "${protectedItemUrl}?api-version=$apiVersion" --query properties.testFailoverState --output tsv
    if ($testState -and $testState -notmatch 'None|Cleaned') {
        $cleanupBody = @{ properties = @{ comments = "AZ-104 $RunId cleanup retry" } } | ConvertTo-Json -Compress
        az rest --method post --url "${protectedItemUrl}/testFailoverCleanup?api-version=$apiVersion" --body $cleanupBody --headers 'Content-Type=application/json' --output none
        $testDeadline = (Get-Date).AddMinutes(60)
        do {
            Start-Sleep -Seconds 30
            $testState = az rest --method get --url "${protectedItemUrl}?api-version=$apiVersion" --query properties.testFailoverState --output tsv
        } until ([string]::IsNullOrWhiteSpace($testState) -or $testState -match 'None|Cleaned' -or (Get-Date) -gt $testDeadline)
        if (-not [string]::IsNullOrWhiteSpace($testState) -and $testState -notmatch 'None|Cleaned') { throw "Test-failover cleanup timed out in state $testState." }
    }
    az site-recovery protected-item remove --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $protectedItem --disable-protection-reason NotSpecified --output none
    Wait-AsrAbsent -Probe $protectedProbe -Label 'replication protected item'
}

$mappingProbe = { az site-recovery protection-container mapping show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $mapping --output none }
if (Test-AsrObject -Probe $mappingProbe) {
    az site-recovery protection-container mapping remove --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --protection-container $sourceContainer --name $mapping --output none
    Wait-AsrAbsent -Probe $mappingProbe -Label 'protection-container mapping'
}

$sourceContainerProbe = { az site-recovery protection-container show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --name $sourceContainer --output none }
if (Test-AsrObject -Probe $sourceContainerProbe) {
    az site-recovery protection-container remove --resource-group $ResourceGroupName --vault-name $vault --fabric-name $sourceFabric --name $sourceContainer --output none
    Wait-AsrAbsent -Probe $sourceContainerProbe -Label 'source protection container'
}
$recoveryContainerProbe = { az site-recovery protection-container show --resource-group $ResourceGroupName --vault-name $vault --fabric-name $recoveryFabric --name $recoveryContainer --output none }
if (Test-AsrObject -Probe $recoveryContainerProbe) {
    az site-recovery protection-container remove --resource-group $ResourceGroupName --vault-name $vault --fabric-name $recoveryFabric --name $recoveryContainer --output none
    Wait-AsrAbsent -Probe $recoveryContainerProbe -Label 'recovery protection container'
}

$sourceFabricProbe = { az site-recovery fabric show --resource-group $ResourceGroupName --vault-name $vault --name $sourceFabric --output none }
if (Test-AsrObject -Probe $sourceFabricProbe) {
    az site-recovery fabric remove --resource-group $ResourceGroupName --vault-name $vault --name $sourceFabric --output none
    Wait-AsrAbsent -Probe $sourceFabricProbe -Label 'source fabric'
}
$recoveryFabricProbe = { az site-recovery fabric show --resource-group $ResourceGroupName --vault-name $vault --name $recoveryFabric --output none }
if (Test-AsrObject -Probe $recoveryFabricProbe) {
    az site-recovery fabric remove --resource-group $ResourceGroupName --vault-name $vault --name $recoveryFabric --output none
    Wait-AsrAbsent -Probe $recoveryFabricProbe -Label 'recovery fabric'
}

$policyProbe = { az site-recovery policy show --resource-group $ResourceGroupName --vault-name $vault --name $policy --output none }
if (Test-AsrObject -Probe $policyProbe) {
    az site-recovery policy delete --resource-group $ResourceGroupName --vault-name $vault --name $policy --yes --output none
    Wait-AsrAbsent -Probe $policyProbe -Label 'replication policy'
}
az backup vault delete --resource-group $ResourceGroupName --name $vault --yes --output none
        }
        foreach ($groupToDelete in @($resourceGroupObjects | Where-Object { -not $absentIds.Contains([string]$_.id) })) {
            az group delete --ids $groupToDelete.id --yes
        }
        foreach ($object in @($active | Where-Object { $_.kind -eq 'entra-object' -and -not $absentIds.Contains([string]$_.id) })) {
            $collection = switch ([string]$object.type) {
                'Microsoft.Graph/user' { 'users' }
                'Microsoft.Graph/group' { 'groups' }
                default { 'directoryObjects' }
            }
            az rest --method delete --url "https://graph.microsoft.com/v1.0/$collection/$($object.id)" --output none 2>$null
        }
        foreach ($object in $state.managedObjects) {
            $object.lifecycleStatus = 'deleted'
        }
        foreach ($action in $actions) {
            if ($action.status -eq 'skipped') { continue }
            $action.status = 'deleted'
            $action.message = 'The exact manifest-recorded target was removed through its ownership boundary.'
        }
    } catch {
        $cleanupFailure = "Cleanup mutation failed: $($_.Exception.GetType().Name)"
        foreach ($action in $actions) {
            if ($action.status -eq 'preview') {
                $action.status = 'failed'
                $action.message = $cleanupFailure
            }
        }
    }
}

$PSNativeCommandUseErrorActionPreference = $false
$remaining = [System.Collections.Generic.List[string]]::new()
foreach ($object in $state.managedObjects) {
    if (-not $Execute -and $object.lifecycleStatus -eq 'active') { $remaining.Add([string]$object.id); continue }
    if ($Execute -and $object.type -eq 'Microsoft.Management/managementGroups') {
        $null = az account management-group show --name $object.name --output none 2>$null
        if ($LASTEXITCODE -eq 0) { $remaining.Add([string]$object.id) }
    } elseif ($Execute -and $object.type -eq 'Microsoft.Resources/resourceGroups') {
        $groupExists = az group exists --subscription $SubscriptionId --name $object.name --output tsv 2>$null
        if ($LASTEXITCODE -ne 0 -or $groupExists -ne 'false') { $remaining.Add([string]$object.id) }
    } elseif ($Execute -and $object.kind -eq 'azure-resource') {
        $null = az resource show --ids $object.id --output none 2>$null
        if ($LASTEXITCODE -eq 0) {
            $remaining.Add([string]$object.id)
        } elseif ($object.type -eq 'Microsoft.RecoveryServices/vaults' -and $true) {
            $deletedVault = az backup deleted-vault get --location $Location --name $object.name --output json 2>$null
            if ($LASTEXITCODE -eq 0 -and $deletedVault) {
                $object.lifecycleStatus = 'soft-deleted'
                foreach ($action in @($actions | Where-Object { [string]$_.targetId -eq [string]$object.id -and $_.status -ne 'skipped' })) {
                    $action.status = 'soft-deleted'
                    $action.message = 'The active ARM vault is absent and the exact recoverable deleted-vault record was confirmed; no purge was performed.'
                }
            } else {
                $remaining.Add([string]$object.id)
            }
        }
    } elseif ($Execute -and $object.kind -eq 'entra-object') {
        $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($object.id)" --output none 2>$null
        if ($LASTEXITCODE -eq 0) { $remaining.Add([string]$object.id) }
    }
}
$residualChecks.Clear()
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP01' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp01.residual'; command = 'query manifest-recorded IDs for LAB25-CP01'; expected = 'zero active objects for LAB25-CP01'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP02' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp02.residual'; command = 'query manifest-recorded IDs for LAB25-CP02'; expected = 'zero active objects for LAB25-CP02'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP03' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp03.residual'; command = 'query manifest-recorded IDs for LAB25-CP03'; expected = 'zero active objects for LAB25-CP03'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP04' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp04.residual'; command = 'query manifest-recorded IDs for LAB25-CP04'; expected = 'zero active objects for LAB25-CP04'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB25-CP05' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp05.residual'; command = 'query manifest-recorded IDs for LAB25-CP05'; expected = 'zero active objects for LAB25-CP05'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
if ($Execute -and $remaining.Count -gt 0) {
    foreach ($object in $state.managedObjects) {
        if ([string]$object.id -in @($remaining)) { $object.lifecycleStatus = 'active' }
    }
    foreach ($action in $actions) {
        if ([string]$action.targetId -in @($remaining) -and $action.status -ne 'skipped') {
            $action.status = 'failed'
            $action.message = 'Residual query found the target still active after cleanup.'
        }
    }
}
$result = if (-not $Execute) { 'preview' } elseif ($cleanupFailure -or $remaining.Count -gt 0) { 'fail' } else { 'pass' }
$cleanup = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-25'
    runId = $RunId
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    executionMode = $(if ($Execute) { 'execute' } else { 'preview' })
    result = $result
    ownershipVerified = $ownershipVerified
    actions = @($actions)
    residualChecks = @($residualChecks)
    activeManagedObjects = @($remaining)
    retainedItems = @(
        @{ id = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName/providers/Microsoft.RecoveryServices/vaults/$vault"; type = 'Microsoft.RecoveryServices/vaults'; reason = 'The Recovery Services vault may remain recoverable under service soft-delete controls.'; expectedDisposition = 'Azure removes the recoverable record after its configured retention period; no purge is automated.' }
    )
}
$cleanup | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
if ($Execute) {
    if ($result -eq 'pass') { $state.status = 'cleaned' }
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
}
Write-Host "Cleanup result: $result"
Write-Host "Artifact: $CleanupPath"
Write-Host 'Irreversible purge is never automated; retained or soft-deleted items must be documented explicitly.'
if ($result -eq 'fail') { exit 1 }
# END GENERATED AZ104 V2
```

[Previous: Lab 24](../24-azure-backup-restore/README.md) · [Catalog](../README.md) · [Next: Lab 26](../26-capstone-build/README.md)
<!-- END GENERATED AZ104 V2 -->
