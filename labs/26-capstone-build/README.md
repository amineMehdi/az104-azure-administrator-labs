# Lab 26: Capstone — Build a governed, secure, observable Azure workload

> Status: **offline-authored and contract-tested; live Azure verification is pending.**

Build a small multi-tier workload from Bicep with governance tags, RBAC, secure storage, segmented networking, private access, resilient compute, load balancing, diagnostics, alerts, and a complete evidence/cleanup record.

This folder is self-contained. It does not depend on another lab's runtime state. Use a disposable environment, keep the generated run manifest, and never substitute a production scope for a missing lab prerequisite.

## Learning objectives

| ID | Microsoft AZ-104 objective |
|---|---|
| `IG-ACCESS-01` | Manage built-in Azure roles |
| `IG-ACCESS-02` | Assign roles at different scopes |
| `IG-GOVERN-01` | Implement and manage Azure Policy |
| `IG-GOVERN-03` | Apply and manage tags on resources |
| `IG-GOVERN-04` | Manage resource groups |
| `ST-ACCOUNTS-01` | Create and configure storage accounts |
| `CP-IAC-04` | Deploy resources by using an Azure Resource Manager template or a Bicep file |
| `CP-VM-01` | Create a virtual machine |
| `CP-VM-06` | Deploy virtual machines to availability zones and availability sets |
| `CP-VM-07` | Deploy and configure an Azure Virtual Machine Scale Sets |
| `NW-VNET-01` | Create and configure virtual networks and subnets |
| `NW-SECURE-01` | Create and configure network security groups (NSGs) and application security groups |
| `NW-SECURE-05` | Configure private endpoints for Azure PaaS |
| `NW-DNSLB-02` | Configure an internal or public load balancer |
| `MR-MONITOR-02` | Configure log settings in Azure Monitor |
| `MR-MONITOR-04` | Set up alert rules, action groups, and alert processing rules in Azure Monitor |

Blueprint source: [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), effective 2026-04-17.

## Architecture

![Lab 26 architecture](diagrams/architecture.svg)

The editable Mermaid source is [diagrams/architecture.mmd](diagrams/architecture.mmd). The diagram describes the learning boundary, not a production reference architecture.

## Scenario and outcome

You are the Azure administrator for a training environment. Your task is to implement the smallest isolated configuration that demonstrates the mapped exam objectives, validate it independently, capture sanitized evidence, and remove only what this run recorded.

The key design idea is: **The build capstone proves that governance, identity, networking, compute, storage, and observability are coupled design decisions and must share a recorded deployment and cleanup boundary.**

## Time, cost, and permissions

| Item | Value |
|---|---|
| Estimated time | 180 minutes |
| Cost class | `moderate` |
| Command surface | Azure CLI and Bicep |
| Required boundary | Contributor, User Access Administrator, Resource Policy Contributor, and Monitoring Contributor on the capstone resource group |
| External/live gate | Requires AZ104_PRINCIPAL_OBJECT_ID for the RBAC checkpoint; the workload path remains deployable without assigning a role when the value is absent. |

Cost is not a fixed promise. Check current pricing, free allowances, quotas, and regional availability before using `--execute` or `-Execute`. Labs marked moderate or elevated should be cleaned up in the same study session.

## Resources and dependencies

| # | Intended resource or object |
|---:|---|
| 1 | resource group |
| 2 | Bicep deployment |
| 3 | segmented VNet |
| 4 | NSG |
| 5 | private storage |
| 6 | resilient compute |
| 7 | load balancer |
| 8 | Log Analytics workspace |
| 9 | diagnostic settings |
| 10 | alerts |

- Resource providers observed by preflight: `Microsoft.Authorization`, `Microsoft.Compute`, `Microsoft.Insights`, `Microsoft.Network`, `Microsoft.OperationalInsights`, `Microsoft.Storage`
- PowerShell modules used when applicable: No extra PowerShell modules
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
- Choose a unique run ID matching `^[a-z0-9-]+$`, such as `az104l26-01`.

## Run the lab

Run these commands from this lab folder. The examples intentionally use placeholders rather than silently reading an arbitrary subscription.

### 1. Preview

```sh
./scripts/cli/setup.sh --subscription-id <subscription-id> --location <region> --run-id az104l26-01
```

Review the context, names, tags, cost class, providers, and gated branches printed by the script.

### 2. Execute the approved baseline

```sh
./scripts/cli/setup.sh --subscription-id <subscription-id> --location <region> --run-id az104l26-01 --execute
```

The script records its run before creating resources. If a cloud operation fails partway through, keep the state directory and use validation plus cleanup against that exact run.

### 3. Complete and reason through the checkpoints

### Checkpoint 1: Run Bicep build and what-if, then deploy the governed resource group and deterministic tagsRun Bicep build and what-if, then deploy the governed resource group and deterministic tags.Evidence to retain:- The command output or exact resource/object ID for checkpoint 1.- A positive assertion proving the intended state.- A negative assertion showing that broader or anonymous access was not introduced.- Any asynchronous operation state, timestamp, and final result.### Checkpoint 2: Create segmented networking, NSG/ASG controls, resilient compute, load balancing, and a private storage endpointCreate segmented networking, NSG/ASG controls, resilient compute, load balancing, and a private storage endpoint.Evidence to retain:- The command output or exact resource/object ID for checkpoint 2.- A positive assertion proving the intended state.- A negative assertion showing that broader or anonymous access was not introduced.- Any asynchronous operation state, timestamp, and final result.### Checkpoint 3: Apply the least-privileged recorded RBAC assignment and a scoped governance policyApply the least-privileged recorded RBAC assignment and a scoped governance policy.Evidence to retain:- The command output or exact resource/object ID for checkpoint 3.- A positive assertion proving the intended state.- A negative assertion showing that broader or anonymous access was not introduced.- Any asynchronous operation state, timestamp, and final result.### Checkpoint 4: Enable diagnostic settings, queries, alerts, and an operator dashboard before running end-to-end validation and cleanupEnable diagnostic settings, queries, alerts, and an operator dashboard before running end-to-end validation and cleanup.Evidence to retain:- The command output or exact resource/object ID for checkpoint 4.- A positive assertion proving the intended state.- A negative assertion showing that broader or anonymous access was not introduced.- Any asynchronous operation state, timestamp, and final result.
### 4. Validate independently

```sh
./scripts/cli/validate.sh --subscription-id <subscription-id> --run-id az104l26-01
```

Inspect `.state/az104l26-01/validation.json`. A `pass` applies only to checks that could be executed. A gated or asynchronous path must remain `warning` or `skipped` until its evidence exists.

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

```sh
./scripts/cli/cleanup.sh --subscription-id <subscription-id> --run-id az104l26-01
```

After verifying every printed target belongs to this run:

```sh
./scripts/cli/cleanup.sh --subscription-id <subscription-id> --run-id az104l26-01 --execute
```

Run validation again after deletion. Some services use soft delete, retained recovery points, asynchronous deletion, or external DNS/tenant state; the cleanup report must distinguish active cleanup from retention and must list residual items instead of claiming success prematurely.

## Exam practice

- Complete [assessment/QUESTIONS.md](assessment/QUESTIONS.md) without opening the answer key.
- Review [assessment/ANSWERS.md](assessment/ANSWERS.md) and trace each explanation to its Microsoft Learn source.
- Revisit every mapped objective whose answer you could not justify from the resource state.

## Microsoft Learn sources

- [https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)
- [https://learn.microsoft.com/en-us/azure/architecture/framework/](https://learn.microsoft.com/en-us/azure/architecture/framework/)
- [https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
- [https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)
- [https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli)

Last curriculum/source review: 2026-08-30. Azure interfaces and command modules evolve; confirm current syntax in the linked primary documentation before a live run.
