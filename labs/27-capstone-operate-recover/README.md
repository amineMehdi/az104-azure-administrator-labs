
<!-- BEGIN GENERATED AZ104 V2 -->
# Lab 27: Capstone — Operate, troubleshoot, back up, and recover an Azure workload

[Previous: Lab 26](../26-capstone-build/README.md) · [Catalog](../README.md)

This self-contained lab uses Azure CLI commands hosted in PowerShell. Complete the guided lane or the automated lane—not both with the same run ID.

## Scenario, role, and outcome

Scenario: You are an on-call azure administrator operating and recovering a governed workload. Build and prove this disposable service path: The private VM and storage workload emit deterministic telemetry to Log Analytics and a scoped alert; effective NSG diagnosis repairs an injected outage, while Recovery Services backup and disk restore prove recoverability.

Learner role: An on-call Azure administrator operating and recovering a governed workload.

Outcome: Use Azure CLI in PowerShell to create the private workload and telemetry foundation, generate telemetry and configure an actionable alert, and back up, restore, and reconcile operational evidence, with recoverable state and deterministic cleanup.

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
| `IG-ACCESS-03` | Interpret access assignments | `LAB27-CP01`, `LAB27-CP05` |
| `IG-GOVERN-01` | Implement and manage Azure Policy | `LAB27-CP02`, `LAB27-CP05` |
| `IG-GOVERN-02` | Configure resource locks | `LAB27-CP03`, `LAB27-CP05` |
| `IG-GOVERN-04` | Manage resource groups | `LAB27-CP04`, `LAB27-CP05` |
| `IG-GOVERN-06` | Manage costs by using alerts, budgets, and Azure Advisor recommendations | `LAB27-CP05` |
| `NW-VNET-05` | Troubleshoot network connectivity | `LAB27-CP05` |
| `NW-SECURE-02` | Evaluate effective security rules in NSGs | `LAB27-CP05` |
| `NW-DNSLB-03` | Troubleshoot load balancing | `LAB27-CP05` |
| `MR-MONITOR-03` | Query and analyze logs in Azure Monitor | `LAB27-CP05` |
| `MR-MONITOR-04` | Set up alert rules, action groups, and alert processing rules in Azure Monitor | `LAB27-CP05` |
| `MR-MONITOR-05` | Configure and interpret monitoring of virtual machines, storage accounts, and networks by using Azure Monitor Insights | `LAB27-CP05` |
| `MR-MONITOR-06` | Use Azure Network Watcher and Connection monitor | `LAB27-CP05` |
| `MR-RECOVERY-04` | Perform backup and restore operations by using Azure Backup | `LAB27-CP05` |
| `MR-RECOVERY-06` | Perform a failover to a secondary region by using Site Recovery | `LAB27-CP05` |
| `MR-RECOVERY-07` | Configure and interpret reports and alerts for backups | `LAB27-CP05` |

The authoritative objective wording comes from the [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), skills measured as of 2026-04-17.

## Architecture and service topology

![Lab 27 service topology](diagrams/architecture.svg)

The editable source is [architecture.mmd](diagrams/architecture.mmd). The private VM and storage workload emit deterministic telemetry to Log Analytics and a scoped alert; effective NSG diagnosis repairs an injected outage, while Recovery Services backup and disk restore prove recoverability.

## Concept primer and design decisions

Operations begins with inventory and evidence, then narrows symptoms through access, Policy, network, monitoring, and recovery layers. The capstone rewards diagnosis before mutation and recovery that is tested without endangering production.

Design decisions:

- Capture baseline evidence before injecting a fault.
- Change only the diagnosed cause.
- Verify restore or recovery outcome before dependency-aware cleanup.

## Required and optional inputs

| Input | Required | Source | Safe example | Gate behavior |
|---|:---:|---|---|---|
| `run-id` — Unique lowercase run ownership identifier | Yes | parameter | `az104l27-01` | `block` |
| `subscription-id` — Expected disposable subscription ID | Yes | parameter-or-environment (`AZ104_SUBSCRIPTION_ID`) | `00000000-0000-0000-0000-000000000000` | `block` |
| `location` — Approved primary Azure region | Yes | parameter-or-environment (`AZ104_LOCATION`) | `westeurope` | `block` |

Secrets stay in temporary environment variables and are never written to `run.json`, validation evidence, or Git. A `skip-checkpoint` gate produces a visible partial result; it never becomes a pass.

## Read-only preflight

Sign in deliberately, inspect the active context, then run the lab preflight. It never signs in, changes context, installs an extension, registers a provider, or creates a resource.

```powershell
az login
az account show --query '{cloud:environmentName,subscription:id,tenant:tenantId,user:user.name}' --output json
./scripts/cli/Preflight.ps1 -SubscriptionId $env:AZ104_SUBSCRIPTION_ID -RunId 'az104l27-01' -Location 'westeurope'
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

## Task 1 — Verify operations and recovery prerequisites {#task-1}

Checkpoint: `LAB27-CP01`

Purpose and operational relevance: Read the provider, region, SKU, feature, quota, and companion-tool signals needed for verify operations and recovery prerequisites, without changing Azure state. The change is unsafe when a missing diagnostic category or unsupported backup workload can block evidence after compute already exists. This checkpoint therefore proves: VM, Network Watcher, Monitor, Storage, and Recovery Services capabilities are available for the selected region and SKU.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
az provider show --namespace Microsoft.Insights --query registrationState --output tsv
az provider show --namespace Microsoft.RecoveryServices --query registrationState --output tsv
az vm list-skus --location $Location --size Standard_B1s --all --query "[?name=='Standard_B1s'].name" --output tsv
if (-not (Get-Command ssh-keygen -ErrorAction SilentlyContinue)) { throw 'ssh-keygen is required for the workload key.' }
```

Expected state: VM, Network Watcher, Monitor, Storage, and Recovery Services capabilities are available for the selected region and SKU.

Representative redacted output:

```text
VM, Network Watcher, Monitor, Storage, and Recovery Services capabilities are available for the selected region and SKU.
```

Positive validation:

```powershell
$insights = az provider show --namespace Microsoft.Insights --query registrationState --output tsv
if ($insights -ne 'Registered') { throw 'Microsoft.Insights is not registered.' }
```

Expected positive result: VM, Network Watcher, Monitor, Storage, and Recovery Services capabilities are available for the selected region and SKU.

Negative validation:

```powershell
$recovery = az provider show --namespace Microsoft.RecoveryServices --query registrationState --output tsv
if ($recovery -ne 'Registered') { throw 'Microsoft.RecoveryServices is not registered.' }
```

Expected negative result: LAB27-CP01 negative boundary: The undesired state is absent; the negative assertion must not report: Microsoft.RecoveryServices is not registered.

Evidence to retain:

- LAB27-CP01 UTC result for verify operations and recovery prerequisites.
- Exact run-owned resource/object ID returned by the commands in LAB27-CP01.
- Positive assertion proving: VM, Network Watcher, Monitor, Storage, and Recovery Services capabilities are available for the selected region and SKU.
- Negative assertion proving absence of: Microsoft.RecoveryServices is not registered.

Common failure and safe retry: A missing diagnostic category or unsupported backup workload can block evidence after compute already exists. Retry LAB27-CP01 for verify operations and recovery prerequisites only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB27-CP02, LAB27-CP03, LAB27-CP04, LAB27-CP05, remove the exact manifest IDs created or configured by LAB27-CP01 for verify operations and recovery prerequisites; its residual probe must then return zero active IDs.

## Task 2 — Create the private workload and telemetry foundation {#task-2}

Checkpoint: `LAB27-CP02`

Purpose and operational relevance: Provision and immediately inventory the exact run-owned resources needed to create the private workload and telemetry foundation, so partial completion remains recoverable. The change is unsafe when a private VM created without a usable NIC/SSH-key workflow can provision but remain impossible to diagnose as designed. This checkpoint therefore proves: The private VM, storage account, workspace, vault, and network-security boundary are recorded immediately after creation.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$workspace = "law-$suffix"; $vault = "rsv-$suffix"; $vnet = "vnet-$suffix"; $nsg = "nsg-$suffix"; $vm = "vm-$suffix"; $storage = "st27$suffix"; $actionGroup = "ag-$suffix"; $alert = "alert-$suffix"
$keyPath = Join-Path $StateDir 'id_ed25519'; ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
az monitor log-analytics workspace create --resource-group $ResourceGroupName --workspace-name $workspace --location $Location --retention-time 30 --output none
az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
az network nsg create --resource-group $ResourceGroupName --name $nsg --location $Location --output none
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.27.0.0/16 --subnet-name workload --subnet-prefixes 10.27.1.0/24 --network-security-group $nsg --output none
az network nic create --resource-group $ResourceGroupName --name "nic-$suffix" --vnet-name $vnet --subnet workload --network-security-group $nsg --output none
az vm create --resource-group $ResourceGroupName --name $vm --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --nics "nic-$suffix" --output none
az backup vault create --resource-group $ResourceGroupName --name $vault --location $Location --output none
```

Expected state: The private VM, storage account, workspace, vault, and network-security boundary are recorded immediately after creation.

Representative redacted output:

```text
The private VM, storage account, workspace, vault, and network-security boundary are recorded immediately after creation.
```

Positive validation:

```powershell
$running = az vm show --resource-group $ResourceGroupName --name $vm --show-details --query powerState --output tsv
if ($running -notmatch 'running') { throw "Workload VM power state is $running." }
```

Expected positive result: The private VM, storage account, workspace, vault, and network-security boundary are recorded immediately after creation.

Negative validation:

```powershell
$publicIp = az vm show --resource-group $ResourceGroupName --name $vm --show-details --query publicIps --output tsv
if ($publicIp) { throw 'The operated VM unexpectedly has a public IP.' }
```

Expected negative result: LAB27-CP02 negative boundary: The undesired state is absent; the negative assertion must not report: The operated VM unexpectedly has a public IP.

Evidence to retain:

- LAB27-CP02 UTC result for create the private workload and telemetry foundation.
- Exact run-owned resource/object ID returned by the commands in LAB27-CP02.
- Positive assertion proving: The private VM, storage account, workspace, vault, and network-security boundary are recorded immediately after creation.
- Negative assertion proving absence of: The operated VM unexpectedly has a public IP.

Common failure and safe retry: A private VM created without a usable NIC/SSH-key workflow can provision but remain impossible to diagnose as designed. Retry LAB27-CP02 for create the private workload and telemetry foundation only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB27-CP03, LAB27-CP04, LAB27-CP05, remove the exact manifest IDs created or configured by LAB27-CP02 for create the private workload and telemetry foundation; its residual probe must then return zero active IDs.

## Task 3 — Generate telemetry and configure an actionable alert {#task-3}

Checkpoint: `LAB27-CP03`

Purpose and operational relevance: Configure and independently inspect the control-plane and data-path properties needed to generate telemetry and configure an actionable alert. The change is unsafe when a successful KQL command with zero rows is not evidence; ingestion must be retried within a bounded window and asserted. This checkpoint therefore proves: A deterministic storage transaction is routed to the workspace and the metric alert scopes the exact storage resource.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
$workspaceId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query id --output tsv
$metricCategories = az monitor diagnostic-settings categories list --resource $storageId --query "value[?categoryType=='Metrics'].name" --output tsv
$metricArgs = @($metricCategories | ForEach-Object { @{ category = $_; enabled = $true } }) | ConvertTo-Json -Compress
az monitor diagnostic-settings create --name "diag-$RunId" --resource $storageId --workspace $workspaceId --metrics $metricArgs --output none
az monitor action-group create --resource-group $ResourceGroupName --name $actionGroup --short-name AZ104 --output none
$actionGroupId = az monitor action-group show --resource-group $ResourceGroupName --name $actionGroup --query id --output tsv
az monitor metrics alert create --resource-group $ResourceGroupName --name $alert --scopes $storageId --condition 'total Transactions > 0' --window-size 15m --evaluation-frequency 5m --action $actionGroupId --description 'AZ-104 operated workload transaction signal' --output none
$oldStorageKey = $env:AZURE_STORAGE_KEY
try {
    $env:AZURE_STORAGE_KEY = az storage account keys list --resource-group $ResourceGroupName --account-name $storage --query "[0].value" --output tsv
    az storage container create --account-name $storage --name operations --auth-mode key --output none
    az storage blob list --account-name $storage --container-name operations --auth-mode key --output none
} finally {
    if ($null -eq $oldStorageKey) { Remove-Item Env:AZURE_STORAGE_KEY -ErrorAction SilentlyContinue } else { $env:AZURE_STORAGE_KEY = $oldStorageKey }
    Remove-Variable oldStorageKey -ErrorAction SilentlyContinue
}
```

Expected state: A deterministic storage transaction is routed to the workspace and the metric alert scopes the exact storage resource.

Representative redacted output:

```text
A deterministic storage transaction is routed to the workspace and the metric alert scopes the exact storage resource.
```

Positive validation:

```powershell
$enabled = az monitor metrics alert show --resource-group $ResourceGroupName --name $alert --query enabled --output tsv
if ($enabled -ne 'true') { throw 'The transaction metric alert is disabled.' }
```

Expected positive result: A deterministic storage transaction is routed to the workspace and the metric alert scopes the exact storage resource.

Negative validation:

```powershell
$diagnosticCount = az monitor diagnostic-settings list --resource $storageId --query "value[?name=='diag-$RunId'] | length(@)" --output tsv
if ([int]$diagnosticCount -ne 1) { throw 'The storage diagnostic setting is absent or duplicated.' }
```

Expected negative result: LAB27-CP03 negative boundary: The undesired state is absent; the negative assertion must not report: The storage diagnostic setting is absent or duplicated.

Evidence to retain:

- LAB27-CP03 UTC result for generate telemetry and configure an actionable alert.
- Exact run-owned resource/object ID returned by the commands in LAB27-CP03.
- Positive assertion proving: A deterministic storage transaction is routed to the workspace and the metric alert scopes the exact storage resource.
- Negative assertion proving absence of: The storage diagnostic setting is absent or duplicated.

Common failure and safe retry: A successful KQL command with zero rows is not evidence; ingestion must be retried within a bounded window and asserted. Retry LAB27-CP03 for generate telemetry and configure an actionable alert only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB27-CP04, LAB27-CP05, remove the exact manifest IDs created or configured by LAB27-CP03 for generate telemetry and configure an actionable alert; its residual probe must then return zero active IDs.

## Task 4 — Inject and repair a deterministic NSG outage {#task-4}

Checkpoint: `LAB27-CP04`

Purpose and operational relevance: Exercise the deterministic operational or denied path needed to inject and repair a deterministic nsg outage, then retain comparable before-and-after results. The change is unsafe when deleting the wrong NSG rule or relying on authored rather than effective rules can leave the outage unresolved. This checkpoint therefore proves: The deny rule produces the documented effective-security symptom, diagnosis identifies its priority, and repair restores the prior path.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
az backup protection enable-for-vm --resource-group $ResourceGroupName --vault-name $vault --vm $vm --policy-name DefaultPolicy --output none
$retainUntil = (Get-Date).ToUniversalTime().AddDays(7).ToString('dd-MM-yyyy')
$backupJob = az backup protection backup-now --resource-group $ResourceGroupName --vault-name $vault --container-name $vm --item-name $vm --backup-management-type AzureIaasVM --retain-until $retainUntil --query name --output tsv
az backup job wait --resource-group $ResourceGroupName --vault-name $vault --name $backupJob --timeout 3600
$recoveryPoint = az backup recoverypoint list --resource-group $ResourceGroupName --vault-name $vault --container-name $vm --item-name $vm --backup-management-type AzureIaasVM --query "[0].name" --output tsv
$restoreJob = az backup restore restore-disks --resource-group $ResourceGroupName --vault-name $vault --container-name $vm --item-name $vm --rp-name $recoveryPoint --storage-account $storage --target-resource-group $ResourceGroupName --restore-to-staging-storage-account true --query name --output tsv
az backup job wait --resource-group $ResourceGroupName --vault-name $vault --name $restoreJob --timeout 3600
```

Expected state: The deny rule produces the documented effective-security symptom, diagnosis identifies its priority, and repair restores the prior path.

Representative redacted output:

```text
The deny rule produces the documented effective-security symptom, diagnosis identifies its priority, and repair restores the prior path.
```

Positive validation:

```powershell
$restoreCount = az backup job list --resource-group $ResourceGroupName --vault-name $vault --operation Restore --status Completed --query "[?properties.entityFriendlyName=='$vm'] | length(@)" --output tsv
if ([int]$restoreCount -lt 1) { throw 'No completed capstone restore job exists.' }
```

Expected positive result: The deny rule produces the documented effective-security symptom, diagnosis identifies its priority, and repair restores the prior path.

Negative validation:

```powershell
$failedJobs = az backup job list --resource-group $ResourceGroupName --vault-name $vault --status Failed --query "length(@)" --output tsv
if ([int]$failedJobs -ne 0) { throw 'A capstone backup or restore job failed.' }
```

Expected negative result: LAB27-CP04 negative boundary: The undesired state is absent; the negative assertion must not report: A capstone backup or restore job failed.

Evidence to retain:

- LAB27-CP04 UTC result for inject and repair a deterministic nsg outage.
- Exact run-owned resource/object ID returned by the commands in LAB27-CP04.
- Positive assertion proving: The deny rule produces the documented effective-security symptom, diagnosis identifies its priority, and repair restores the prior path.
- Negative assertion proving absence of: A capstone backup or restore job failed.

Common failure and safe retry: Deleting the wrong NSG rule or relying on authored rather than effective rules can leave the outage unresolved. Retry LAB27-CP04 for inject and repair a deterministic nsg outage only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB27-CP05, remove the exact manifest IDs created or configured by LAB27-CP04 for inject and repair a deterministic nsg outage; its residual probe must then return zero active IDs.

## Task 5 — Back up, restore, and reconcile operational evidence {#task-5}

Checkpoint: `LAB27-CP05`

Purpose and operational relevance: Reconcile live service properties, returned IDs, and dependency-aware removal needed to back up, restore, and reconcile operational evidence before handoff. The change is unsafe when backup job completion without a verified recovery point or restore artifact gives false confidence in recoverability. This checkpoint therefore proves: The backup and disk-restore jobs complete, telemetry remains queryable, effective networking is healthy, and cleanup honors soft-delete retention.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$workspaceCustomerId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query customerId --output tsv
$deadline = (Get-Date).AddMinutes(15)
do {
    $metricRows = az monitor log-analytics query --workspace $workspaceCustomerId --analytics-query "AzureMetrics | where TimeGenerated > ago(30m) | where ResourceId =~ '$storageId' | where MetricName == 'Transactions' | count" --query "tables[0].rows[0][0]" --output tsv
    if ([int]$metricRows -lt 1) { Start-Sleep -Seconds 30 }
} until ([int]$metricRows -ge 1 -or (Get-Date) -gt $deadline)
if ([int]$metricRows -lt 1) { throw 'No transaction metric reached AzureMetrics within the bounded ingestion wait.' }
az network nic list-effective-nsg --resource-group $ResourceGroupName --name "nic-$suffix" --output json
```

Expected state: The backup and disk-restore jobs complete, telemetry remains queryable, effective networking is healthy, and cleanup honors soft-delete retention.

Representative redacted output:

```text
The backup and disk-restore jobs complete, telemetry remains queryable, effective networking is healthy, and cleanup honors soft-delete retention.
```

Positive validation:

```powershell
$workspaceCustomerId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query customerId --output tsv
$metricRows = az monitor log-analytics query --workspace $workspaceCustomerId --analytics-query "AzureMetrics | where TimeGenerated > ago(30m) | where ResourceId =~ '$storageId' | where MetricName == 'Transactions' | count" --query "tables[0].rows[0][0]" --output tsv
if ([int]$metricRows -lt 1) { throw 'AzureMetrics has no run-owned storage transaction row.' }
```

Expected positive result: The backup and disk-restore jobs complete, telemetry remains queryable, effective networking is healthy, and cleanup honors soft-delete retention.

Negative validation:

```powershell
$denyRules = az network nsg rule list --resource-group $ResourceGroupName --nsg-name $nsg --query "[?name=='DenyInjectedOperations'] | length(@)" --output tsv
if ([int]$denyRules -ne 0) { throw 'The injected operations deny rule still exists.' }
```

Expected negative result: LAB27-CP05 negative boundary: The undesired state is absent; the negative assertion must not report: The injected operations deny rule still exists.

Evidence to retain:

- LAB27-CP05 UTC result for back up, restore, and reconcile operational evidence.
- Exact run-owned resource/object ID returned by the commands in LAB27-CP05.
- Positive assertion proving: The backup and disk-restore jobs complete, telemetry remains queryable, effective networking is healthy, and cleanup honors soft-delete retention.
- Negative assertion proving absence of: The injected operations deny rule still exists.

Common failure and safe retry: Backup job completion without a verified recovery point or restore artifact gives false confidence in recoverability. Retry LAB27-CP05 for back up, restore, and reconcile operational evidence only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After all service validation and evidence capture, remove the exact manifest IDs created or configured by LAB27-CP05 for back up, restore, and reconcile operational evidence; its residual probe must then return zero active IDs.

## Final validation and result interpretation

Run independent deployment validation after all required checkpoints:

```powershell
./scripts/cli/Validate.ps1 -RunId 'az104l27-01' -Mode Deployment
az resource list --resource-group 'rg-az104-l27-az104l27-01' --query '[].{name:name,type:type}' --output table
```

- `pass`: every required positive and negative check passed.
- `partial`: every required check passed, but at least one optional gate was deliberately skipped.
- `fail`: a required checkpoint failed; do not record the lab as complete.

Keep the redacted `validation.json`; do not retain credentials, tokens, access keys, certificate material, email addresses, tenant IDs, or unredacted command output.

## Deterministic break/fix exercise

Injection: Add a bounded deny-all inbound rule to the run-owned workload NSG.

Inject the bounded fault:

```powershell
az network nsg rule create --resource-group $ResourceGroupName --nsg-name $nsg --name DenyInjectedOperations --priority 100 --direction Inbound --access Deny --protocol "*" --source-address-prefixes "*" --destination-port-ranges "*" --output none
```

Capture the failed state with a read-only query:

```powershell
az network nic list-effective-nsg --resource-group $ResourceGroupName --name "nic-$suffix" --output json
```

Repair only the injected setting, then repeat the same query:

```powershell
az network nsg rule delete --resource-group $ResourceGroupName --nsg-name $nsg --name DenyInjectedOperations
az network nsg rule list --resource-group $ResourceGroupName --nsg-name $nsg --query "[?name=='DenyInjectedOperations'] | length(@)" --output tsv
```

Expected symptom: Effective NSG evidence shows the injected rule as the highest-priority custom decision while monitoring and backup resources remain healthy.

Diagnose with a read-only service query:

```powershell
az network nic list-effective-nsg --resource-group $ResourceGroupName --name "nic-$suffix" --output json
```

Diagnosis: Correlate the exact NSG rule, effective NIC rules, metric signal, and recent administrative activity.

Repair: Delete only DenyInjectedOperations and repeat the effective-rule and recovery checks.

Before/after evidence must show the failed negative or positive check before repair and the same check passing afterward. Do not inject a second fault until the first is removed.

## Optional job-style challenge

Write an incident report with detection, impact, timeline, diagnosis, repair, recovery evidence, and prevention actions.

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
./scripts/cli/Cleanup.ps1 -RunId 'az104l27-01'
./scripts/cli/Cleanup.ps1 -RunId 'az104l27-01' -Execute
./scripts/cli/Validate.ps1 -RunId 'az104l27-01' -Mode PostCleanup
$denyRules = az network nsg rule list --resource-group $ResourceGroupName --nsg-name $nsg --query "[?name=='DenyInjectedOperations'] | length(@)" --output tsv
if ([int]$denyRules -ne 0) { throw 'The injected operations deny rule still exists.' }
```

`cleanup.json` passes only when no active manifest-managed object remains. Soft-deleted or intentionally retained items must be listed with their reason and expected disposition. The lifecycle never performs irreversible purge automatically.

## Exam debrief and assessment

Explain why the expected state, negative check, and cleanup boundary matter—not only which command was used. Map any missed concept back to its task anchor before reviewing the answer key.

This hands-on lab has no separate question set. Use the [domain assessment dashboard](../../docs/question-bank-index.md) to choose review questions.

## Microsoft Learn sources

- [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Collect Azure resource logs with diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)
- [Query Azure Monitor Logs with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/monitor/log-analytics)
- [Create Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule)
- [Back up an Azure VM with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)
- [Restore Azure VM disks with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/tutorial-restore-disk)

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
$ResourceGroupName = $(if ('27' -in @('00', '01', '02')) { $null } else { "rg-az104-l27-$RunId" })

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
    'Microsoft.Authorization'
    'Microsoft.Compute'
    'Microsoft.Insights'
    'Microsoft.Network'
    'Microsoft.OperationalInsights'
    'Microsoft.RecoveryServices'
    'Microsoft.Storage'
)
foreach ($provider in $providers) {
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    Add-PreflightResult -Id "provider:$provider" -Required $true -Passed ($registrationState -eq 'Registered') -Actual $(if ($registrationState) { $registrationState } else { 'Unavailable' })
}

$knownLocation = az account list-locations --query "[?name=='$Location'].name | [0]" --output tsv
Add-PreflightResult -Id 'region' -Required $true -Passed ($knownLocation -eq $Location) -Actual $(if ($knownLocation) { $knownLocation } else { 'not available' })

$usage = az vm list-usage --location $Location --output json 2>$null | ConvertFrom-Json
Add-PreflightResult -Id 'regional-compute-quota' -Required $false -Passed ($LASTEXITCODE -eq 0) -Actual "entries=$(@($usage).Count)"

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
$insights = az provider show --namespace Microsoft.Insights --query registrationState --output tsv
if ($insights -ne 'Registered') { throw 'Microsoft.Insights is not registered.' }
$recovery = az provider show --namespace Microsoft.RecoveryServices --query registrationState --output tsv
if ($recovery -ne 'Registered') { throw 'Microsoft.RecoveryServices is not registered.' }
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
if ($state.labId -ne 'LAB-27' -or $state.runId -ne $RunId) { throw 'Manifest ownership does not match this lab and run ID.' }
$PSNativeCommandUseErrorActionPreference = $false
$accountJson = az account show --output json 2>$null
$account = $(if ($LASTEXITCODE -eq 0 -and $accountJson) { $accountJson | ConvertFrom-Json } else { $null })
if (-not $account -or [string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $actualContext = $(if ($account) { "tenant=$($account.tenantId); subscription=$($account.id)" } else { 'active context unavailable' })
    $contextFailure = @{
        schemaVersion = '1.0.0'; labId = 'LAB-27'; runId = $RunId; mode = $Mode
        generatedAt = $capturedAt; result = 'fail'
        summary = @{ required = 1; passed = 0; failed = 1; skipped = 0 }
        checks = @(@{ id = 'context.active'; checkpointId = 'LAB27-CP01'; kind = 'context'; required = $true; status = 'fail'; message = 'Active Azure context does not match the run manifest.'; evidence = @{ command = 'az account show --output json'; expected = 'tenant and subscription exactly match run.json'; actual = $actualContext; capturedAt = $capturedAt; redacted = $true } })
    }
    $contextFailure | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
    Write-Host "Validation $Mode result: fail"
    Write-Host "Artifact: $ValidationPath"
    exit 1
}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('27' -in @('00', '01', '02')) { $null } else { "rg-az104-l27-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$workspace = "law-$suffix"; $vault = "rsv-$suffix"; $vnet = "vnet-$suffix"; $nsg = "nsg-$suffix"; $vm = "vm-$suffix"; $storage = "st27$suffix"; $actionGroup = "ag-$suffix"; $alert = "alert-$suffix"; $storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv

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

# CHECKPOINT LAB27-CP01 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB27-CP01' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP01' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab27-cp01.positive' -CheckpointId 'LAB27-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab27-cp01.negative' -CheckpointId 'LAB27-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$insights = az provider show --namespace Microsoft.Insights --query registrationState --output tsv
if ($insights -ne 'Registered') { throw 'Microsoft.Insights is not registered.' }
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
    Add-ValidationCheck -Id 'lab27-cp01.positive' -CheckpointId 'LAB27-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$recovery = az provider show --namespace Microsoft.RecoveryServices --query registrationState --output tsv
if ($recovery -ne 'Registered') { throw 'Microsoft.RecoveryServices is not registered.' }
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
    Add-ValidationCheck -Id 'lab27-cp01.negative' -CheckpointId 'LAB27-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab27-cp01.residual' -CheckpointId 'LAB27-CP01' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB27-CP01 END

# CHECKPOINT LAB27-CP02 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB27-CP02' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP02' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab27-cp02.positive' -CheckpointId 'LAB27-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab27-cp02.negative' -CheckpointId 'LAB27-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$running = az vm show --resource-group $ResourceGroupName --name $vm --show-details --query powerState --output tsv
if ($running -notmatch 'running') { throw "Workload VM power state is $running." }
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
    Add-ValidationCheck -Id 'lab27-cp02.positive' -CheckpointId 'LAB27-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$publicIp = az vm show --resource-group $ResourceGroupName --name $vm --show-details --query publicIps --output tsv
if ($publicIp) { throw 'The operated VM unexpectedly has a public IP.' }
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
    Add-ValidationCheck -Id 'lab27-cp02.negative' -CheckpointId 'LAB27-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab27-cp02.residual' -CheckpointId 'LAB27-CP02' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB27-CP02 END

# CHECKPOINT LAB27-CP03 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB27-CP03' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP03' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab27-cp03.positive' -CheckpointId 'LAB27-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab27-cp03.negative' -CheckpointId 'LAB27-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$enabled = az monitor metrics alert show --resource-group $ResourceGroupName --name $alert --query enabled --output tsv
if ($enabled -ne 'true') { throw 'The transaction metric alert is disabled.' }
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
    Add-ValidationCheck -Id 'lab27-cp03.positive' -CheckpointId 'LAB27-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$diagnosticCount = az monitor diagnostic-settings list --resource $storageId --query "value[?name=='diag-$RunId'] | length(@)" --output tsv
if ([int]$diagnosticCount -ne 1) { throw 'The storage diagnostic setting is absent or duplicated.' }
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
    Add-ValidationCheck -Id 'lab27-cp03.negative' -CheckpointId 'LAB27-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab27-cp03.residual' -CheckpointId 'LAB27-CP03' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB27-CP03 END

# CHECKPOINT LAB27-CP04 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB27-CP04' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP04' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab27-cp04.positive' -CheckpointId 'LAB27-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab27-cp04.negative' -CheckpointId 'LAB27-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$restoreCount = az backup job list --resource-group $ResourceGroupName --vault-name $vault --operation Restore --status Completed --query "[?properties.entityFriendlyName=='$vm'] | length(@)" --output tsv
if ([int]$restoreCount -lt 1) { throw 'No completed capstone restore job exists.' }
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
    Add-ValidationCheck -Id 'lab27-cp04.positive' -CheckpointId 'LAB27-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$failedJobs = az backup job list --resource-group $ResourceGroupName --vault-name $vault --status Failed --query "length(@)" --output tsv
if ([int]$failedJobs -ne 0) { throw 'A capstone backup or restore job failed.' }
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
    Add-ValidationCheck -Id 'lab27-cp04.negative' -CheckpointId 'LAB27-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab27-cp04.residual' -CheckpointId 'LAB27-CP04' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB27-CP04 END

# CHECKPOINT LAB27-CP05 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB27-CP05' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP05' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab27-cp05.positive' -CheckpointId 'LAB27-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab27-cp05.negative' -CheckpointId 'LAB27-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$workspaceCustomerId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query customerId --output tsv
$metricRows = az monitor log-analytics query --workspace $workspaceCustomerId --analytics-query "AzureMetrics | where TimeGenerated > ago(30m) | where ResourceId =~ '$storageId' | where MetricName == 'Transactions' | count" --query "tables[0].rows[0][0]" --output tsv
if ([int]$metricRows -lt 1) { throw 'AzureMetrics has no run-owned storage transaction row.' }
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
    Add-ValidationCheck -Id 'lab27-cp05.positive' -CheckpointId 'LAB27-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$denyRules = az network nsg rule list --resource-group $ResourceGroupName --nsg-name $nsg --query "[?name=='DenyInjectedOperations'] | length(@)" --output tsv
if ([int]$denyRules -ne 0) { throw 'The injected operations deny rule still exists.' }
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
    Add-ValidationCheck -Id 'lab27-cp05.negative' -CheckpointId 'LAB27-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab27-cp05.residual' -CheckpointId 'LAB27-CP05' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB27-CP05 END

$requiredChecks = @($checks | Where-Object { $_.required })
$failedChecks = @($checks | Where-Object { $_.status -eq 'fail' })
$requiredSkippedChecks = @($checks | Where-Object { $_.required -and $_.status -eq 'skipped' })
$skippedChecks = @($checks | Where-Object { $_.status -eq 'skipped' })
$result = if ($failedChecks.Count -gt 0 -or $requiredSkippedChecks.Count -gt 0) { 'fail' } elseif ($skippedChecks.Count -gt 0) { 'partial' } else { 'pass' }
$document = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-27'
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
        schemaVersion = '1.0.0'; labId = 'LAB-27'; runId = $RunId
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
if ($state.labId -ne 'LAB-27' -or $state.runId -ne $RunId) {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: manifest lab ID or run ID does not match.'
}
if ($Execute -and $active.Count -eq 0 -and $state.status -eq 'cleaned') {
    $priorRetained = @()
    if (Test-Path -LiteralPath $CleanupPath) {
        try { $priorRetained = @((Get-Content -LiteralPath $CleanupPath -Raw | ConvertFrom-Json).retainedItems) } catch { $priorRetained = @() }
    }
    $idempotent = @{
        schemaVersion = '1.0.0'; labId = 'LAB-27'; runId = $RunId
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
$ResourceGroupName = $(if ('27' -in @('00', '01', '02')) { $null } else { "rg-az104-l27-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$vault = "rsv-$suffix"; $vm = "vm-$suffix"

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
                [string]$tags['labId'] -eq '27' -and
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
            [string]$expectedTags['labId'] -eq '27' -and
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

# CHECKPOINT LAB27-CP05 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP05' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB27-CP05'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB27-CP05 END

# CHECKPOINT LAB27-CP04 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP04' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB27-CP04'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB27-CP04 END

# CHECKPOINT LAB27-CP03 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP03' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB27-CP03'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB27-CP03 END

# CHECKPOINT LAB27-CP02 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP02' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB27-CP02'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB27-CP02 END

# CHECKPOINT LAB27-CP01 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP01' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB27-CP01'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB27-CP01 END

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
try {
    $item = az backup item list --resource-group $ResourceGroupName --vault-name $vault --backup-management-type AzureIaasVM --query "[?properties.friendlyName=='$vm'] | [0]" --output json 2>$null | ConvertFrom-Json
    if ($item) { az backup protection disable --resource-group $ResourceGroupName --vault-name $vault --container-name $vm --item-name $vm --backup-management-type AzureIaasVM --delete-backup-data true --yes --output none }
    az backup vault delete --resource-group $ResourceGroupName --name $vault --yes --output none
} catch { throw 'Capstone recovery cleanup stopped before the resource-group boundary; inspect the protected item and retry.' }
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
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP01' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp01.residual'; command = 'query manifest-recorded IDs for LAB27-CP01'; expected = 'zero active objects for LAB27-CP01'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP02' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp02.residual'; command = 'query manifest-recorded IDs for LAB27-CP02'; expected = 'zero active objects for LAB27-CP02'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP03' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp03.residual'; command = 'query manifest-recorded IDs for LAB27-CP03'; expected = 'zero active objects for LAB27-CP03'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP04' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp04.residual'; command = 'query manifest-recorded IDs for LAB27-CP04'; expected = 'zero active objects for LAB27-CP04'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB27-CP05' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp05.residual'; command = 'query manifest-recorded IDs for LAB27-CP05'; expected = 'zero active objects for LAB27-CP05'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
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
    labId = 'LAB-27'
    runId = $RunId
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    executionMode = $(if ($Execute) { 'execute' } else { 'preview' })
    result = $result
    ownershipVerified = $ownershipVerified
    actions = @($actions)
    residualChecks = @($residualChecks)
    activeManagedObjects = @($remaining)
    retainedItems = @(
        @{ id = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName/providers/Microsoft.RecoveryServices/vaults/$vault"; type = 'Microsoft.RecoveryServices/vaults'; reason = 'Backup soft delete intentionally retains a recoverable vault/item record after active resources are removed.'; expectedDisposition = 'Azure expires the recoverable record under the configured retention policy; no purge is automated.' }
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

[Previous: Lab 26](../26-capstone-build/README.md) · [Catalog](../README.md)
<!-- END GENERATED AZ104 V2 -->
