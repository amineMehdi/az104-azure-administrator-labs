# Lab 27: Capstone — Operate, troubleshoot, back up, and recover an Azure workload

> Status: **offline-authored and contract-tested; live Azure verification is pending.**

Deploy or discover an isolated workload, interpret access and policy state, diagnose a network fault, query logs and metrics, respond to alerts, restore protected data, and execute a documented recovery decision before complete cleanup.

This folder is self-contained. It does not depend on another lab's runtime state. Use a disposable environment, keep the generated run manifest, and never substitute a production scope for a missing lab prerequisite.

## Learning objectives

| ID | Microsoft AZ-104 objective |
|---|---|
| `IG-ACCESS-03` | Interpret access assignments |
| `IG-GOVERN-01` | Implement and manage Azure Policy |
| `IG-GOVERN-02` | Configure resource locks |
| `IG-GOVERN-04` | Manage resource groups |
| `IG-GOVERN-06` | Manage costs by using alerts, budgets, and Azure Advisor recommendations |
| `NW-VNET-05` | Troubleshoot network connectivity |
| `NW-SECURE-02` | Evaluate effective security rules in NSGs |
| `NW-DNSLB-03` | Troubleshoot load balancing |
| `MR-MONITOR-03` | Query and analyze logs in Azure Monitor |
| `MR-MONITOR-04` | Set up alert rules, action groups, and alert processing rules in Azure Monitor |
| `MR-MONITOR-05` | Configure and interpret monitoring of virtual machines, storage accounts, and networks by using Azure Monitor Insights |
| `MR-MONITOR-06` | Use Azure Network Watcher and Connection monitor |
| `MR-RECOVERY-04` | Perform backup and restore operations by using Azure Backup |
| `MR-RECOVERY-06` | Perform a failover to a secondary region by using Site Recovery |
| `MR-RECOVERY-07` | Configure and interpret reports and alerts for backups |

Blueprint source: [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), effective 2026-04-17.

## Architecture

![Lab 27 architecture](diagrams/architecture.svg)

The editable Mermaid source is [diagrams/architecture.mmd](diagrams/architecture.mmd). The diagram describes the learning boundary, not a production reference architecture.

## Scenario and outcome

You are the Azure administrator for a training environment. Your task is to implement the smallest isolated configuration that demonstrates the mapped exam objectives, validate it independently, capture sanitized evidence, and remove only what this run recorded.

The key design idea is: **Operations should follow evidence: establish baseline, detect and scope the fault, repair the smallest cause, validate service state, then prove backup or recovery objectives before cleanup.**

## Time, cost, and permissions

| Item | Value |
|---|---|
| Estimated time | 180 minutes |
| Cost class | `elevated` |
| Command surface | Az PowerShell and KQL |
| Required boundary | Contributor, Monitoring Contributor, Backup Contributor, and Network Contributor on the capstone resource group |
| External/live gate | The live recovery drill requires cost review and an isolated workload; production failover or irreversible deletion is never inferred from this capstone. |

Cost is not a fixed promise. Check current pricing, free allowances, quotas, and regional availability before using `--execute` or `-Execute`. Labs marked moderate or elevated should be cleaned up in the same study session.

## Resources and dependencies

| # | Intended resource or object |
|---:|---|
| 1 | resource group |
| 2 | test workload |
| 3 | Log Analytics workspace |
| 4 | alerts |
| 5 | Recovery Services vault |
| 6 | backup policy |
| 7 | fault injection and recovery evidence |

- Resource providers observed by preflight: `Microsoft.Authorization`, `Microsoft.Compute`, `Microsoft.Insights`, `Microsoft.Network`, `Microsoft.OperationalInsights`, `Microsoft.RecoveryServices`
- PowerShell modules used when applicable: `Az.Accounts`, `Az.Resources`, `Az.Network`, `Az.Compute`, `Az.Monitor`, `Az.OperationalInsights`, `Az.RecoveryServices`
- Repository state: `.state/<run-id>/run.json` and `.state/<run-id>/validation.json`
- Secrets, access keys, SAS tokens, generated passwords, and shared keys must remain in memory and must not enter the manifest, command evidence, or Git history.

## Safety contract

1. Preflight is read-only. It does not sign in, register providers, or switch the active context.
2. Setup is preview-only unless the explicit execution switch is supplied.
3. State is written before the first cloud mutation and updated with exact returned IDs.
4. Validation reads live state independently; it does not repair a failed configuration.
5. Cleanup previews exact targets, verifies run ownership, then requires the explicit execution switch.
6. Tenant-wide, DNS, licensing, notification, failover, and policy gates are never guessed.

## Before you begin

- Use a disposable non-production tenant/subscription and verify the displayed tenant and subscription IDs.
- Install the declared command surface and supporting dependencies.
- Confirm the role boundary above at the smallest possible scope.
- Review provider registration and quota output; preflight reports requirements but does not register providers.
- Read the external gate. An unavailable gate is a documented `skipped` checkpoint, not a pass.
- Choose a unique run ID matching `^[a-z0-9-]+$`, such as `az104l27-01`.

## Run the lab

Run these commands from this lab folder. The examples intentionally use placeholders rather than silently reading an arbitrary subscription.

### 1. Preview

```ps1
pwsh ./scripts/powershell/Setup.ps1 -RunId az104l27-01 -SubscriptionId <subscription-id> -Location <region>
```

Review the context, names, tags, cost class, providers, and gated branches printed by the script.

### 2. Execute the approved baseline

```ps1
pwsh ./scripts/powershell/Setup.ps1 -RunId az104l27-01 -SubscriptionId <subscription-id> -Location <region> -Execute
```

The script records its run before creating resources. If a cloud operation fails partway through, keep the state directory and use validation plus cleanup against that exact run.

### 3. Complete and reason through the checkpoints

### Checkpoint 1: Inventory the workload, interpret direct/inherited access, policy compliance, tags, locks, and current health before changing anythingInventory the workload, interpret direct/inherited access, policy compliance, tags, locks, and current health before changing anything.Evidence to retain:- The command output or exact resource/object ID for checkpoint 1.- A positive assertion proving the intended state.- A negative assertion showing that broader or anonymous access was not introduced.- Any asynchronous operation state, timestamp, and final result.### Checkpoint 2: Inject one bounded NSG or load-balancer fault, use effective rules and Network Watcher evidence to diagnose it, then repair only the identified causeInject one bounded NSG or load-balancer fault, use effective rules and Network Watcher evidence to diagnose it, then repair only the identified cause.Evidence to retain:- The command output or exact resource/object ID for checkpoint 2.- A positive assertion proving the intended state.- A negative assertion showing that broader or anonymous access was not introduced.- Any asynchronous operation state, timestamp, and final result.### Checkpoint 3: Query metrics/logs, process an alert, and record the operational timeline and validation outputQuery metrics/logs, process an alert, and record the operational timeline and validation output.Evidence to retain:- The command output or exact resource/object ID for checkpoint 3.- A positive assertion proving the intended state.- A negative assertion showing that broader or anonymous access was not introduced.- Any asynchronous operation state, timestamp, and final result.### Checkpoint 4: Protect the test workload, run a restore or isolated recovery drill, verify recovered state, and remove protection/resources in dependency orderProtect the test workload, run a restore or isolated recovery drill, verify recovered state, and remove protection/resources in dependency order.Evidence to retain:- The command output or exact resource/object ID for checkpoint 4.- A positive assertion proving the intended state.- A negative assertion showing that broader or anonymous access was not introduced.- Any asynchronous operation state, timestamp, and final result.
### 4. Validate independently

```ps1
pwsh ./scripts/powershell/Validate.ps1 -RunId az104l27-01 -SubscriptionId <subscription-id>
```

Inspect `.state/az104l27-01/validation.json`. A `pass` applies only to checks that could be executed. A gated or asynchronous path must remain `warning` or `skipped` until its evidence exists.

Positive checks should prove the intended resources, configuration, relationships, or health. Negative checks should prove that anonymous access, excess scope, accidental inheritance, unresolved DNS, unhealthy probes, or unrecorded resources were not introduced where the scenario forbids them.

## Break/fix exercise

1. Pick one reversible configuration created inside the recorded lab boundary.
2. Record the exact ID and current value.
3. Introduce one bounded mismatch; do not weaken a tenant-wide or production control.
4. Run validation and connect the failed check to an exact CLI/PowerShell query and the machine-readable validation result.
5. Repair only the identified setting, rerun validation, and compare the evidence.

The [solution notes](solution/README.md) provide a diagnostic sequence without hiding the reasoning behind an opaque repair script.

## Cleanup

Preview cleanup first:

```ps1
pwsh ./scripts/powershell/Cleanup.ps1 -RunId az104l27-01 -SubscriptionId <subscription-id>
```

After verifying every printed target belongs to this run:

```ps1
pwsh ./scripts/powershell/Cleanup.ps1 -RunId az104l27-01 -SubscriptionId <subscription-id> -Execute
```

Run validation again after deletion. Some services use soft delete, retained recovery points, asynchronous deletion, or external DNS/tenant state; the cleanup report must distinguish active cleanup from retention and must list residual items instead of claiming success prematurely.

## Exam practice

- Complete [assessment/QUESTIONS.md](assessment/QUESTIONS.md) without opening the answer key.
- Review [assessment/ANSWERS.md](assessment/ANSWERS.md) and trace each explanation to its Microsoft Learn source.
- Revisit every mapped objective whose answer you could not justify from the resource state.

## Microsoft Learn sources

- [https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview)
- [https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview)
- [https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
- [https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)
- [https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access)

Last curriculum/source review: 2026-08-30. Azure interfaces and command modules evolve; confirm current syntax in the linked primary documentation before a live run.
