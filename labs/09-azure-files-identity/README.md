# Lab 09: Configure Azure Files, snapshots, soft delete, and identity access

> Status: **offline-authored and contract-tested; live Azure verification is pending.**

Create a storage account and file share, enable share soft delete, create a snapshot, copy sample data, and prepare an identity-based SMB configuration through an explicitly gated Entra Kerberos or AD DS path.

This folder is self-contained. It does not depend on another lab's runtime state. Use a disposable environment, keep the generated run manifest, and never substitute a production scope for a missing lab prerequisite.

## Learning objectives

| ID | Microsoft AZ-104 objective |
|---|---|
| `ST-ACCESS-05` | Configure identity-based access for Azure Files |
| `ST-ACCOUNTS-05` | Manage data by using Azure Storage Explorer and AzCopy |
| `ST-DATA-01` | Create and configure a file share in Azure Files |
| `ST-DATA-05` | Configure snapshots and soft delete for Azure Files |

Blueprint source: [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), effective 2026-04-17.

## Architecture

![Lab 09 architecture](diagrams/architecture.svg)

The editable Mermaid source is [diagrams/architecture.mmd](diagrams/architecture.mmd). The diagram describes the learning boundary, not a production reference architecture.

## Scenario and outcome

You are the Azure administrator for a training environment. Your task is to implement the smallest isolated configuration that demonstrates the mapped exam objectives, validate it independently, capture sanitized evidence, and remove only what this run recorded.

The key design idea is: **Share snapshots and soft delete solve different recovery problems, while identity-based SMB authentication requires an approved directory source and data-plane authorization.**

## Time, cost, and permissions

| Item | Value |
|---|---|
| Estimated time | 135 minutes |
| Cost class | `low` |
| Command surface | Az PowerShell |
| Required boundary | Contributor and Storage File Data SMB Share Contributor; directory permissions for the optional identity-source path |
| External/live gate | Identity-based SMB configuration is gated by AZ104_FILES_IDENTITY_SOURCE because Entra Kerberos, AD DS, and Entra Domain Services have different prerequisites. |

Cost is not a fixed promise. Check current pricing, free allowances, quotas, and regional availability before using `--execute` or `-Execute`. Labs marked moderate or elevated should be cleaned up in the same study session.

## Resources and dependencies

| # | Intended resource or object |
|---:|---|
| 1 | resource group |
| 2 | storage account |
| 3 | Azure file share |
| 4 | share snapshot |

- Resource providers observed by preflight: `Microsoft.Storage`
- PowerShell modules used when applicable: `Az.Accounts`, `Az.Resources`, `Az.Storage`
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
- Choose a unique run ID matching `^[a-z0-9-]+$`, such as `az104l09-01`.

## Run the lab

Run these commands from this lab folder. The examples intentionally use placeholders rather than silently reading an arbitrary subscription.

### 1. Preview

```ps1
pwsh ./scripts/powershell/Setup.ps1 -RunId az104l09-01 -SubscriptionId <subscription-id> -Location <region>
```

Review the context, names, tags, cost class, providers, and gated branches printed by the script.

### 2. Execute the approved baseline

```ps1
pwsh ./scripts/powershell/Setup.ps1 -RunId az104l09-01 -SubscriptionId <subscription-id> -Location <region> -Execute
```

The script records its run before creating resources. If a cloud operation fails partway through, keep the state directory and use validation plus cleanup against that exact run.

### 3. Complete and reason through the checkpoints

### Checkpoint 1: Create a secure StorageV2 account and transaction-optimized file share with quota

Create a secure StorageV2 account and transaction-optimized file share with quota.

Evidence to retain:

- The command output or exact resource/object ID for checkpoint 1.
- A positive assertion proving the intended state.
- A negative assertion showing that broader or anonymous access was not introduced.
- Any asynchronous operation state, timestamp, and final result.

### Checkpoint 2: Enable Azure Files share soft delete and create a point-in-time share snapshot

Enable Azure Files share soft delete and create a point-in-time share snapshot.

Evidence to retain:

- The command output or exact resource/object ID for checkpoint 2.
- A positive assertion proving the intended state.
- A negative assertion showing that broader or anonymous access was not introduced.
- Any asynchronous operation state, timestamp, and final result.

### Checkpoint 3: Upload sample content with AzCopy or Az

Upload sample content with AzCopy or Az.Storage without storing account keys.

Evidence to retain:

- The command output or exact resource/object ID for checkpoint 3.
- A positive assertion proving the intended state.
- A negative assertion showing that broader or anonymous access was not introduced.
- Any asynchronous operation state, timestamp, and final result.

### Checkpoint 4: Inventory identity-based SMB options and configure only the authorized AZ104_FILES_IDENTITY_SOURCE path

Inventory identity-based SMB options and configure only the authorized AZ104_FILES_IDENTITY_SOURCE path.

Evidence to retain:

- The command output or exact resource/object ID for checkpoint 4.
- A positive assertion proving the intended state.
- A negative assertion showing that broader or anonymous access was not introduced.
- Any asynchronous operation state, timestamp, and final result.

### 4. Validate independently

```ps1
pwsh ./scripts/powershell/Validate.ps1 -RunId az104l09-01 -SubscriptionId <subscription-id>
```

Inspect `.state/az104l09-01/validation.json`. A `pass` applies only to checks that could be executed. A gated or asynchronous path must remain `warning` or `skipped` until its evidence exists.

Positive checks should prove the intended resources, configuration, relationships, or health. Negative checks should prove that anonymous access, excess scope, accidental inheritance, unresolved DNS, unhealthy probes, or unrecorded resources were not introduced where the scenario forbids them.

## Portal evidence

Portal screenshots are planned evidence captured only during an authorized live run. Until then every entry in [images/portal/manifest.yml](images/portal/manifest.yml) stays `pending`, and no placeholder image is committed. Capture and sanitization rules live in [images/README.md](images/README.md).

| Planned file | Checkpoint | Portal blade | Evidence |
|---|---:|---|---|
| `01-storage-account-file-shares.png` | 1 | Storage account > File shares | The share, quota, and selected tier |
| `02-file-share-snapshots.png` | 2 | File share > Snapshots | The point-in-time share snapshot |
| `03-storage-account-data-protection.png` | 2 | Storage account > Data protection | Azure Files soft-delete retention |
| `04-file-shares-identity-based-access.png` | 4 | Storage account > File shares > Identity-based access | The configured or gated directory source |

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
pwsh ./scripts/powershell/Cleanup.ps1 -RunId az104l09-01 -SubscriptionId <subscription-id>
```

After verifying every printed target belongs to this run:

```ps1
pwsh ./scripts/powershell/Cleanup.ps1 -RunId az104l09-01 -SubscriptionId <subscription-id> -Execute
```

Run validation again after deletion. Some services use soft delete, retained recovery points, asynchronous deletion, or external DNS/tenant state; the cleanup report must distinguish active cleanup from retention and must list residual items instead of claiming success prematurely.

## Exam practice

- Complete [assessment/QUESTIONS.md](assessment/QUESTIONS.md) without opening the answer key.
- Review [assessment/ANSWERS.md](assessment/ANSWERS.md) and trace each explanation to its Microsoft Learn source.
- Revisit every mapped objective whose answer you could not justify from the resource state.

## Microsoft Learn sources

- [https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share](https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share)
- [https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files](https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files)
- [https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion)
- [https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)
- [https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files)

Last curriculum/source review: 2026-08-30. Azure interfaces and command modules evolve; confirm current syntax in the linked primary documentation before a live run.
