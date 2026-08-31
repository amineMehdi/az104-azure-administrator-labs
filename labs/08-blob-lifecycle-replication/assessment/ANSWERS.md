# Lab 08 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB08-Q01 — B

**Question:** A blob retention peer review asks how the blob retention and replication service should handle this outcome: keep private data from being read without an authorization header. Which explanation is accurate?

- **A — Incorrect.** Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics.
  Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics. In the blob retention and replication service, this statement describes blob access tiers. Blob retention and replication service asks about blob containers; this blob access tiers choice leaves the blob containers explanation missing.
- **B — Correct.** A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls.
  A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls. This blob containers fact resolves the blob retention and replication service design question about how to keep private data from being read without an authorization header.
- **C — Incorrect.** A lifecycle delete action permanently removes eligible current or previous versions after its age condition.
  A lifecycle delete action permanently removes eligible current or previous versions after its age condition. In the blob retention and replication service, this statement describes lifecycle deletion. Selecting lifecycle deletion for blob retention and replication service leaves blob containers unanswered in blob retention and replication service; the blob retention and replication service lacks a blob containers basis to keep private data from being read without an authorization header.
- **D — Incorrect.** Blob versioning preserves a new immutable version when a block blob is modified or deleted.
  Blob versioning preserves a new immutable version when a block blob is modified or deleted. In the blob retention and replication service, this statement describes blob versioning. Blob containers governs blob retention and replication service; blob versioning cannot support blob containers when operators must keep private data from being read without an authorization header.

**Objectives:** `ST-DATA-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Configure anonymous read access for containers and blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure)

**Source reviewed:** 2026-08-31

## LAB08-Q02 — D

**Question:** For the blob retention and replication service, the blob retention plan must place frequently read and rarely read blobs in cost-appropriate tiers. Which statement about blob retention belongs in the blob retention and replication service record?

- **A — Incorrect.** Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters.
  Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters. In the blob retention and replication service, this statement describes lifecycle rule filters. The lifecycle rule filters statement accurately describes lifecycle rule filters; however, blob retention and replication service needs blob access tiers to place frequently read and rarely read blobs in cost-appropriate tiers; lifecycle rule filters cannot replace blob access tiers.
- **B — Incorrect.** Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.
  Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted. In the blob retention and replication service, this statement describes blob soft delete. Selecting blob soft delete for blob retention and replication service leaves blob access tiers unanswered in blob retention and replication service; the blob retention and replication service lacks a blob access tiers basis to place frequently read and rarely read blobs in cost-appropriate tiers.
- **C — Incorrect.** Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements.
  Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements. In the blob retention and replication service, this statement describes object replication. Blob access tiers governs blob retention and replication service; object replication cannot support blob access tiers when operators must place frequently read and rarely read blobs in cost-appropriate tiers.
- **D — Correct.** Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics.
  Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics. For blob retention and replication service, blob access tiers supplies the service rule needed to place frequently read and rarely read blobs in cost-appropriate tiers.

**Objectives:** `ST-DATA-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Access tiers for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q03 — B

**Question:** The blob retention review compares four claims for the blob retention and replication service requirement to apply retention automation only to blobs matching the intended prefix or type. Which claim is technically sound?

- **A — Incorrect.** Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access.
  Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access. In the blob retention and replication service, this statement describes lifecycle tier transitions. Selecting lifecycle tier transitions for blob retention and replication service leaves lifecycle rule filters unanswered in blob retention and replication service; the blob retention and replication service lacks a lifecycle rule filters basis to apply retention automation only to blobs matching the intended prefix or type.
- **B — Correct.** Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters.
  Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters. In the blob retention and replication service, this lifecycle rule filters rule supports the need to apply retention automation only to blobs matching the intended prefix or type.
- **C — Incorrect.** Container soft delete protects a deleted container and its contents for a separate configured retention period.
  Container soft delete protects a deleted container and its contents for a separate configured retention period. In the blob retention and replication service, this statement describes container soft delete. Blob retention and replication service asks about lifecycle rule filters; this container soft delete choice leaves the lifecycle rule filters explanation missing.
- **D — Incorrect.** AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items.
  AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items. In the blob retention and replication service, this statement describes AzCopy copy and sync. The AzCopy copy and sync statement accurately describes AzCopy copy and sync; however, blob retention and replication service needs lifecycle rule filters to apply retention automation only to blobs matching the intended prefix or type; AzCopy copy and sync cannot replace lifecycle rule filters.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q04 — C

**Question:** The blob retention architecture note requires the blob retention and replication service environment to move eligible data to a cooler tier after the configured age. Which statement defines the relevant blob retention boundary?

- **A — Incorrect.** A lifecycle delete action permanently removes eligible current or previous versions after its age condition.
  A lifecycle delete action permanently removes eligible current or previous versions after its age condition. In the blob retention and replication service, this statement describes lifecycle deletion. Lifecycle tier transitions governs blob retention and replication service; lifecycle deletion cannot support lifecycle tier transitions when operators must move eligible data to a cooler tier after the configured age.
- **B — Incorrect.** Blob versioning preserves a new immutable version when a block blob is modified or deleted.
  Blob versioning preserves a new immutable version when a block blob is modified or deleted. In the blob retention and replication service, this statement describes blob versioning. Blob retention and replication service asks about lifecycle tier transitions; this blob versioning choice leaves the lifecycle tier transitions explanation missing.
- **C — Correct.** Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access.
  For the blob retention and replication service, the rule for lifecycle tier transitions is defined by this statement: lifecycle age conditions can tier a current blob version after the configured number of days since modification or access. It supports the required outcome to move eligible data to a cooler tier after the configured age.
- **D — Incorrect.** A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls.
  A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls. In the blob retention and replication service, this statement describes blob containers. Selecting blob containers for blob retention and replication service leaves lifecycle tier transitions unanswered in blob retention and replication service; the blob retention and replication service lacks a lifecycle tier transitions basis to move eligible data to a cooler tier after the configured age.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q05 — C

**Question:** A new blob retention operator must explain why the blob retention and replication service can delete only objects that satisfy the retention rule's age conditions. Which explanation is accurate?

- **A — Incorrect.** Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.
  Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted. In the blob retention and replication service, this statement describes blob soft delete. Blob retention and replication service asks about lifecycle deletion; this blob soft delete choice leaves the lifecycle deletion explanation missing.
- **B — Incorrect.** Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements.
  Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements. In the blob retention and replication service, this statement describes object replication. The object replication statement accurately describes object replication; however, blob retention and replication service needs lifecycle deletion to delete only objects that satisfy the retention rule's age conditions; object replication cannot replace lifecycle deletion.
- **C — Correct.** A lifecycle delete action permanently removes eligible current or previous versions after its age condition.
  A lifecycle delete action permanently removes eligible current or previous versions after its age condition. The blob retention and replication service applies that lifecycle deletion boundary when operators must delete only objects that satisfy the retention rule's age conditions.
- **D — Incorrect.** Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics.
  Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics. In the blob retention and replication service, this statement describes blob access tiers. Lifecycle deletion governs blob retention and replication service; blob access tiers cannot support lifecycle deletion when operators must delete only objects that satisfy the retention rule's age conditions.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q06 — D

**Question:** The blob retention and replication service acceptance criteria require operators to recover a blob deleted after data protection was enabled. Which service fact supports that requirement?

- **A — Incorrect.** Container soft delete protects a deleted container and its contents for a separate configured retention period.
  Container soft delete protects a deleted container and its contents for a separate configured retention period. In the blob retention and replication service, this statement describes container soft delete. The container soft delete statement accurately describes container soft delete; however, blob retention and replication service needs blob soft delete to recover a blob deleted after data protection was enabled; container soft delete cannot replace blob soft delete.
- **B — Incorrect.** AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items.
  AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items. In the blob retention and replication service, this statement describes AzCopy copy and sync. Selecting AzCopy copy and sync for blob retention and replication service leaves blob soft delete unanswered in blob retention and replication service; the blob retention and replication service lacks a blob soft delete basis to recover a blob deleted after data protection was enabled.
- **C — Incorrect.** Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters.
  Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters. In the blob retention and replication service, this statement describes lifecycle rule filters. Blob soft delete governs blob retention and replication service; lifecycle rule filters cannot support blob soft delete when operators must recover a blob deleted after data protection was enabled.
- **D — Correct.** Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.
  The blob retention and replication service needs blob soft delete to recover a blob deleted after data protection was enabled; this option states the applicable blob soft delete rule: blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Azure Blob Storage data protection overview](https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q07 — D

**Question:** A blob retention reviewer challenges whether the blob retention and replication service can recover a container removed during its retention window. Which response resolves the concern?

- **A — Incorrect.** Blob versioning preserves a new immutable version when a block blob is modified or deleted.
  Blob versioning preserves a new immutable version when a block blob is modified or deleted. In the blob retention and replication service, this statement describes blob versioning. Selecting blob versioning for blob retention and replication service leaves container soft delete unanswered in blob retention and replication service; the blob retention and replication service lacks a container soft delete basis to recover a container removed during its retention window.
- **B — Incorrect.** A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls.
  A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls. In the blob retention and replication service, this statement describes blob containers. Container soft delete governs blob retention and replication service; blob containers cannot support container soft delete when operators must recover a container removed during its retention window.
- **C — Incorrect.** Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access.
  Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access. In the blob retention and replication service, this statement describes lifecycle tier transitions. Blob retention and replication service asks about container soft delete; this lifecycle tier transitions choice leaves the container soft delete explanation missing.
- **D — Correct.** Container soft delete protects a deleted container and its contents for a separate configured retention period.
  Container soft delete protects a deleted container and its contents for a separate configured retention period. This container soft delete fact resolves the blob retention and replication service design question about how to recover a container removed during its retention window.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Soft delete for containers](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q08 — D

**Question:** The blob retention and replication service handoff omits the blob retention rule needed to retain an earlier block-blob state after a write or deletion. Which statement should the team add?

- **A — Incorrect.** Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements.
  Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements. In the blob retention and replication service, this statement describes object replication. Blob versioning governs blob retention and replication service; object replication cannot support blob versioning when operators must retain an earlier block-blob state after a write or deletion.
- **B — Incorrect.** Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics.
  Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics. In the blob retention and replication service, this statement describes blob access tiers. Blob retention and replication service asks about blob versioning; this blob access tiers choice leaves the blob versioning explanation missing.
- **C — Incorrect.** A lifecycle delete action permanently removes eligible current or previous versions after its age condition.
  A lifecycle delete action permanently removes eligible current or previous versions after its age condition. In the blob retention and replication service, this statement describes lifecycle deletion. The lifecycle deletion statement accurately describes lifecycle deletion; however, blob retention and replication service needs blob versioning to retain an earlier block-blob state after a write or deletion; lifecycle deletion cannot replace blob versioning.
- **D — Correct.** Blob versioning preserves a new immutable version when a block blob is modified or deleted.
  Blob versioning preserves a new immutable version when a block blob is modified or deleted. For blob retention and replication service, blob versioning supplies the service rule needed to retain an earlier block-blob state after a write or deletion.

**Objectives:** `ST-DATA-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q09 — C

**Question:** A blob retention incident review of the blob retention and replication service depends on the ability to copy supported block-blob changes asynchronously to a second account. Which platform description is reliable?

- **A — Incorrect.** AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items.
  AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items. In the blob retention and replication service, this statement describes AzCopy copy and sync. Blob retention and replication service asks about object replication; this AzCopy copy and sync choice leaves the object replication explanation missing.
- **B — Incorrect.** Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters.
  Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters. In the blob retention and replication service, this statement describes lifecycle rule filters. The lifecycle rule filters statement accurately describes lifecycle rule filters; however, blob retention and replication service needs object replication to copy supported block-blob changes asynchronously to a second account; lifecycle rule filters cannot replace object replication.
- **C — Correct.** Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements.
  Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements. In the blob retention and replication service, this object replication rule supports the need to copy supported block-blob changes asynchronously to a second account.
- **D — Incorrect.** Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.
  Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted. In the blob retention and replication service, this statement describes blob soft delete. Object replication governs blob retention and replication service; blob soft delete cannot support object replication when operators must copy supported block-blob changes asynchronously to a second account.

**Objectives:** `ST-ACCOUNTS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Object replication for block blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q10 — B

**Question:** A data-platform administrator managing blob retention and replication is updating the blob retention runbook. The requirement is to copy a directory safely without deleting unrelated destination data. Which statement describes Azure behavior correctly?

- **A — Incorrect.** A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls.
  A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls. In the blob retention and replication service, this statement describes blob containers. The blob containers statement accurately describes blob containers; however, blob retention and replication service needs AzCopy copy and sync to copy a directory safely without deleting unrelated destination data; blob containers cannot replace AzCopy copy and sync.
- **B — Correct.** AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items.
  For the blob retention and replication service, the rule for AzCopy copy and sync is defined by this statement: azCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items. It supports the required outcome to copy a directory safely without deleting unrelated destination data.
- **C — Incorrect.** Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access.
  Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access. In the blob retention and replication service, this statement describes lifecycle tier transitions. AzCopy copy and sync governs blob retention and replication service; lifecycle tier transitions cannot support AzCopy copy and sync when operators must copy a directory safely without deleting unrelated destination data.
- **D — Incorrect.** Container soft delete protects a deleted container and its contents for a separate configured retention period.
  Container soft delete protects a deleted container and its contents for a separate configured retention period. In the blob retention and replication service, this statement describes container soft delete. Blob retention and replication service asks about AzCopy copy and sync; this container soft delete choice leaves the AzCopy copy and sync explanation missing.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Transfer data with AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)

**Source reviewed:** 2026-08-31

## LAB08-Q11 — A

**Question:** The approach for the blob retention and replication service is approved, but the blob retention environment still cannot keep private data from being read without an authorization header. Which implementation step closes the gap?

- **A — Correct.** Create the container with private access unless anonymous blob access is explicitly required.
  Create the container with private access unless anonymous blob access is explicitly required. This changes blob containers in the blob retention and replication service, supplying the missing state needed to keep private data from being read without an authorization header.
- **B — Incorrect.** Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions.
  Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. In the blob retention and replication service, this action changes lifecycle rule filters. Blob retention and replication service requires blob containers; changing lifecycle rule filters leaves blob containers absent in blob retention and replication service; blob retention and replication service cannot keep private data from being read without an authorization header.
- **C — Incorrect.** Enable blob soft delete with the approved retention days before testing deletion recovery.
  Enable blob soft delete with the approved retention days before testing deletion recovery. In the blob retention and replication service, this action changes blob soft delete. Blob soft delete does not implement blob containers for blob retention and replication service; the blob retention and replication service still cannot keep private data from being read without an authorization header.
- **D — Incorrect.** Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules.
  Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. In the blob retention and replication service, this action changes object replication. Blob retention and replication service instead needs blob containers: Create the container with private access unless anonymous blob access is explicitly required. The object replication action omits that blob containers work.

**Objectives:** `ST-DATA-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Configure anonymous read access for containers and blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure)

**Source reviewed:** 2026-08-31

## LAB08-Q12 — C

**Question:** The data-platform administrator managing blob retention and replication may change the blob retention and replication service only to place frequently read and rarely read blobs in cost-appropriate tiers. Which blob retention action stays within that assignment?

- **A — Incorrect.** Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition.
  Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. In the blob retention and replication service, this action changes lifecycle tier transitions. Blob retention and replication service requires blob access tiers; changing lifecycle tier transitions leaves blob access tiers absent in blob retention and replication service; blob retention and replication service cannot place frequently read and rarely read blobs in cost-appropriate tiers.
- **B — Incorrect.** Enable container delete retention and use a unique test container for recovery validation.
  Enable container delete retention and use a unique test container for recovery validation. In the blob retention and replication service, this action changes container soft delete. Container soft delete does not implement blob access tiers for blob retention and replication service; the blob retention and replication service still cannot place frequently read and rarely read blobs in cost-appropriate tiers.
- **C — Correct.** Choose the tier from observed access frequency, retention period, and retrieval-time requirements.
  The blob retention and replication service must place frequently read and rarely read blobs in cost-appropriate tiers; this option performs its direct blob access tiers change: choose the tier from observed access frequency, retention period, and retrieval-time requirements.
- **D — Incorrect.** Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation.
  Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. In the blob retention and replication service, this action changes AzCopy copy and sync. Blob retention and replication service approved blob access tiers, not AzCopy copy and sync; only the blob access tiers change can place frequently read and rarely read blobs in cost-appropriate tiers.

**Objectives:** `ST-DATA-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Access tiers for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q13 — D

**Question:** A blob retention dry run shows no blob retention and replication service command will apply retention automation only to blobs matching the intended prefix or type. Which action belongs before execution?

- **A — Incorrect.** Use a delete action only after data-protection retention and legal requirements are satisfied.
  Use a delete action only after data-protection retention and legal requirements are satisfied. In the blob retention and replication service, this action changes lifecycle deletion. Lifecycle deletion does not implement lifecycle rule filters for blob retention and replication service; the blob retention and replication service still cannot apply retention automation only to blobs matching the intended prefix or type.
- **B — Incorrect.** Enable versioning before overwriting the test blob and persist the returned version IDs.
  Enable versioning before overwriting the test blob and persist the returned version IDs. In the blob retention and replication service, this action changes blob versioning. Blob retention and replication service instead needs lifecycle rule filters: Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. The blob versioning action omits that lifecycle rule filters work.
- **C — Incorrect.** Create the container with private access unless anonymous blob access is explicitly required.
  Create the container with private access unless anonymous blob access is explicitly required. In the blob retention and replication service, this action changes blob containers. Blob retention and replication service approved lifecycle rule filters, not blob containers; only the lifecycle rule filters change can apply retention automation only to blobs matching the intended prefix or type.
- **D — Correct.** Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions.
  Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. It is the least-change lifecycle rule filters path for the blob retention and replication service requirement to apply retention automation only to blobs matching the intended prefix or type.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q14 — B

**Question:** For the blob retention and replication service, operators need to move eligible data to a cooler tier after the configured age. Which change realizes that requirement?

- **A — Incorrect.** Enable blob soft delete with the approved retention days before testing deletion recovery.
  Enable blob soft delete with the approved retention days before testing deletion recovery. In the blob retention and replication service, this action changes blob soft delete. Blob retention and replication service instead needs lifecycle tier transitions: Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. The blob soft delete action omits that lifecycle tier transitions work.
- **B — Correct.** Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition.
  Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. In blob retention and replication service, applying lifecycle tier transitions is the scoped way to move eligible data to a cooler tier after the configured age.
- **C — Incorrect.** Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules.
  Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. In the blob retention and replication service, this action changes object replication. Blob retention and replication service requires lifecycle tier transitions; changing object replication leaves lifecycle tier transitions absent in blob retention and replication service; blob retention and replication service cannot move eligible data to a cooler tier after the configured age.
- **D — Incorrect.** Choose the tier from observed access frequency, retention period, and retrieval-time requirements.
  Choose the tier from observed access frequency, retention period, and retrieval-time requirements. In the blob retention and replication service, this action changes blob access tiers. Blob access tiers does not implement lifecycle tier transitions for blob retention and replication service; the blob retention and replication service still cannot move eligible data to a cooler tier after the configured age.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q15 — B

**Question:** Operators must automate the blob retention and replication service change needed to delete only objects that satisfy the retention rule's age conditions. Which blob retention operation belongs in the runbook?

- **A — Incorrect.** Enable container delete retention and use a unique test container for recovery validation.
  Enable container delete retention and use a unique test container for recovery validation. In the blob retention and replication service, this action changes container soft delete. Blob retention and replication service approved lifecycle deletion, not container soft delete; only the lifecycle deletion change can delete only objects that satisfy the retention rule's age conditions.
- **B — Correct.** Use a delete action only after data-protection retention and legal requirements are satisfied.
  Use a delete action only after data-protection retention and legal requirements are satisfied. The blob retention and replication service uses this lifecycle deletion operation to delete only objects that satisfy the retention rule's age conditions within the approved scope.
- **C — Incorrect.** Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation.
  Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. In the blob retention and replication service, this action changes AzCopy copy and sync. AzCopy copy and sync does not implement lifecycle deletion for blob retention and replication service; the blob retention and replication service still cannot delete only objects that satisfy the retention rule's age conditions.
- **D — Incorrect.** Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions.
  Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. In the blob retention and replication service, this action changes lifecycle rule filters. Blob retention and replication service instead needs lifecycle deletion: Use a delete action only after data-protection retention and legal requirements are satisfied. The lifecycle rule filters action omits that lifecycle deletion work.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q16 — D

**Question:** A blob retention and replication service review finds blob retention drift from the need to recover a blob deleted after data protection was enabled. Which correction addresses that drift?

- **A — Incorrect.** Enable versioning before overwriting the test blob and persist the returned version IDs.
  Enable versioning before overwriting the test blob and persist the returned version IDs. In the blob retention and replication service, this action changes blob versioning. Blob retention and replication service requires blob soft delete; changing blob versioning leaves blob soft delete absent in blob retention and replication service; blob retention and replication service cannot recover a blob deleted after data protection was enabled.
- **B — Incorrect.** Create the container with private access unless anonymous blob access is explicitly required.
  Create the container with private access unless anonymous blob access is explicitly required. In the blob retention and replication service, this action changes blob containers. Blob containers does not implement blob soft delete for blob retention and replication service; the blob retention and replication service still cannot recover a blob deleted after data protection was enabled.
- **C — Incorrect.** Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition.
  Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. In the blob retention and replication service, this action changes lifecycle tier transitions. Blob retention and replication service instead needs blob soft delete: Enable blob soft delete with the approved retention days before testing deletion recovery. The lifecycle tier transitions action omits that blob soft delete work.
- **D — Correct.** Enable blob soft delete with the approved retention days before testing deletion recovery.
  For the blob retention and replication service, the required blob soft delete action is: enable blob soft delete with the approved retention days before testing deletion recovery. It makes the environment able to recover a blob deleted after data protection was enabled.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Azure Blob Storage data protection overview](https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q17 — D

**Question:** The blob retention and replication service window permits only the blob retention change needed to recover a container removed during its retention window. Which option respects the boundary?

- **A — Incorrect.** Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules.
  Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. In the blob retention and replication service, this action changes object replication. Object replication does not implement container soft delete for blob retention and replication service; the blob retention and replication service still cannot recover a container removed during its retention window.
- **B — Incorrect.** Choose the tier from observed access frequency, retention period, and retrieval-time requirements.
  Choose the tier from observed access frequency, retention period, and retrieval-time requirements. In the blob retention and replication service, this action changes blob access tiers. Blob retention and replication service instead needs container soft delete: Enable container delete retention and use a unique test container for recovery validation. The blob access tiers action omits that container soft delete work.
- **C — Incorrect.** Use a delete action only after data-protection retention and legal requirements are satisfied.
  Use a delete action only after data-protection retention and legal requirements are satisfied. In the blob retention and replication service, this action changes lifecycle deletion. Blob retention and replication service approved container soft delete, not lifecycle deletion; only the container soft delete change can recover a container removed during its retention window.
- **D — Correct.** Enable container delete retention and use a unique test container for recovery validation.
  Enable container delete retention and use a unique test container for recovery validation. This changes container soft delete in the blob retention and replication service, supplying the missing state needed to recover a container removed during its retention window.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Soft delete for containers](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q18 — B

**Question:** The blob retention preflight has passed; the blob retention and replication service must now retain an earlier block-blob state after a write or deletion. Which operation should run?

- **A — Incorrect.** Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation.
  Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. In the blob retention and replication service, this action changes AzCopy copy and sync. Blob retention and replication service instead needs blob versioning: Enable versioning before overwriting the test blob and persist the returned version IDs. The AzCopy copy and sync action omits that blob versioning work.
- **B — Correct.** Enable versioning before overwriting the test blob and persist the returned version IDs.
  The blob retention and replication service must retain an earlier block-blob state after a write or deletion; this option performs its direct blob versioning change: enable versioning before overwriting the test blob and persist the returned version IDs.
- **C — Incorrect.** Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions.
  Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. In the blob retention and replication service, this action changes lifecycle rule filters. Blob retention and replication service requires blob versioning; changing lifecycle rule filters leaves blob versioning absent in blob retention and replication service; blob retention and replication service cannot retain an earlier block-blob state after a write or deletion.
- **D — Incorrect.** Enable blob soft delete with the approved retention days before testing deletion recovery.
  Enable blob soft delete with the approved retention days before testing deletion recovery. In the blob retention and replication service, this action changes blob soft delete. Blob soft delete does not implement blob versioning for blob retention and replication service; the blob retention and replication service still cannot retain an earlier block-blob state after a write or deletion.

**Objectives:** `ST-DATA-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q19 — A

**Question:** The blob retention and replication service plan must copy supported block-blob changes asynchronously to a second account while limiting the mutation scope to blob retention. Which action is appropriate?

- **A — Correct.** Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules.
  Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. It is the least-change object replication path for the blob retention and replication service requirement to copy supported block-blob changes asynchronously to a second account.
- **B — Incorrect.** Create the container with private access unless anonymous blob access is explicitly required.
  Create the container with private access unless anonymous blob access is explicitly required. In the blob retention and replication service, this action changes blob containers. Blob retention and replication service requires object replication; changing blob containers leaves object replication absent in blob retention and replication service; blob retention and replication service cannot copy supported block-blob changes asynchronously to a second account.
- **C — Incorrect.** Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition.
  Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. In the blob retention and replication service, this action changes lifecycle tier transitions. Lifecycle tier transitions does not implement object replication for blob retention and replication service; the blob retention and replication service still cannot copy supported block-blob changes asynchronously to a second account.
- **D — Incorrect.** Enable container delete retention and use a unique test container for recovery validation.
  Enable container delete retention and use a unique test container for recovery validation. In the blob retention and replication service, this action changes container soft delete. Blob retention and replication service instead needs object replication: Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. The container soft delete action omits that object replication work.

**Objectives:** `ST-ACCOUNTS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Object replication for block blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q20 — D

**Question:** A blob retention ticket in the blob retention and replication service says to copy a directory safely without deleting unrelated destination data. Which blob retention action completes the blob retention and replication service request with minimal change?

- **A — Incorrect.** Choose the tier from observed access frequency, retention period, and retrieval-time requirements.
  Choose the tier from observed access frequency, retention period, and retrieval-time requirements. In the blob retention and replication service, this action changes blob access tiers. Blob retention and replication service requires AzCopy copy and sync; changing blob access tiers leaves AzCopy copy and sync absent in blob retention and replication service; blob retention and replication service cannot copy a directory safely without deleting unrelated destination data.
- **B — Incorrect.** Use a delete action only after data-protection retention and legal requirements are satisfied.
  Use a delete action only after data-protection retention and legal requirements are satisfied. In the blob retention and replication service, this action changes lifecycle deletion. Lifecycle deletion does not implement AzCopy copy and sync for blob retention and replication service; the blob retention and replication service still cannot copy a directory safely without deleting unrelated destination data.
- **C — Incorrect.** Enable versioning before overwriting the test blob and persist the returned version IDs.
  Enable versioning before overwriting the test blob and persist the returned version IDs. In the blob retention and replication service, this action changes blob versioning. Blob retention and replication service instead needs AzCopy copy and sync: Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. The blob versioning action omits that AzCopy copy and sync work.
- **D — Correct.** Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation.
  Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. In blob retention and replication service, applying AzCopy copy and sync is the scoped way to copy a directory safely without deleting unrelated destination data.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Transfer data with AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)

**Source reviewed:** 2026-08-31

## LAB08-Q21 — C

**Question:** The blob retention log says the blob retention and replication service can now keep private data from being read without an authorization header. Which blob retention state should the blob retention and replication service acceptance test retain?

- **A — Incorrect.** Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
  Read the lifecycle action and condition, then confirm only eligible test blobs match the rule. In the blob retention and replication service, this check observes lifecycle tier transitions. Blob retention and replication service output covers lifecycle tier transitions, not blob containers; the blob containers requirement to keep private data from being read without an authorization header remains unverified.
- **B — Incorrect.** Query containerDeleteRetentionPolicy and list deleted containers with the test name.
  Query containerDeleteRetentionPolicy and list deleted containers with the test name. In the blob retention and replication service, this check observes container soft delete. Container soft delete success in blob retention and replication service cannot verify blob containers; blob retention and replication service cannot keep private data from being read without an authorization header until blob containers evidence exists.
- **C — Correct.** List the container and confirm its name, lease state, and publicAccess value.
  List the container and confirm its name, lease state, and publicAccess value. The blob retention and replication service reads blob containers directly; that blob containers result proves the blob retention and replication service can keep private data from being read without an authorization header without another mutation.
- **D — Incorrect.** Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
  Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available. In the blob retention and replication service, this check observes AzCopy copy and sync. Blob retention and replication service could pass AzCopy copy and sync while blob containers is wrong; blob retention and replication service still lacks blob containers proof.

**Objectives:** `ST-DATA-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Configure anonymous read access for containers and blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure)

**Source reviewed:** 2026-08-31

## LAB08-Q22 — C

**Question:** The blob retention and replication service rejects blob retention exit status as proof it can place frequently read and rarely read blobs in cost-appropriate tiers. Which blob retention and replication service result is valid evidence?

- **A — Incorrect.** Inspect the delete condition and verify protected or excluded blob prefixes do not match.
  Inspect the delete condition and verify protected or excluded blob prefixes do not match. In the blob retention and replication service, this check observes lifecycle deletion. Lifecycle deletion success in blob retention and replication service cannot verify blob access tiers; blob retention and replication service cannot place frequently read and rarely read blobs in cost-appropriate tiers until blob access tiers evidence exists.
- **B — Incorrect.** List blob versions and confirm distinct version IDs and current-version state.
  List blob versions and confirm distinct version IDs and current-version state. In the blob retention and replication service, this check observes blob versioning. Blob retention and replication service reads blob versioning, leaving blob access tiers unproved in blob retention and replication service; blob retention and replication service still has no blob access tiers proof.
- **C — Correct.** Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
  For the blob retention and replication service, this blob access tiers observation is decisive: read the blob's accessTier and accessTierChangeTime after the tier operation completes. It is blob retention and replication service evidence that operators can place frequently read and rarely read blobs in cost-appropriate tiers.
- **D — Incorrect.** List the container and confirm its name, lease state, and publicAccess value.
  List the container and confirm its name, lease state, and publicAccess value. In the blob retention and replication service, this check observes blob containers. Blob retention and replication service output covers blob containers, not blob access tiers; the blob access tiers requirement to place frequently read and rarely read blobs in cost-appropriate tiers remains unverified.

**Objectives:** `ST-DATA-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Access tiers for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q23 — D

**Question:** The blob retention validator needs one blob retention and replication service query after the change to apply retention automation only to blobs matching the intended prefix or type. Which blob retention property should the blob retention and replication service validator inspect?

- **A — Incorrect.** Query deleteRetentionPolicy and confirm enabled and days values.
  Query deleteRetentionPolicy and confirm enabled and days values. In the blob retention and replication service, this check observes blob soft delete. Blob retention and replication service reads blob soft delete, leaving lifecycle rule filters unproved in blob retention and replication service; blob retention and replication service still has no lifecycle rule filters proof.
- **B — Incorrect.** Query the policy IDs on both accounts and verify replication status on a versioned test blob.
  Query the policy IDs on both accounts and verify replication status on a versioned test blob. In the blob retention and replication service, this check observes object replication. Blob retention and replication service could pass object replication while lifecycle rule filters is wrong; blob retention and replication service still lacks lifecycle rule filters proof.
- **C — Incorrect.** Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
  Read the blob's accessTier and accessTierChangeTime after the tier operation completes. In the blob retention and replication service, this check observes blob access tiers. Blob retention and replication service output covers blob access tiers, not lifecycle rule filters; the lifecycle rule filters requirement to apply retention automation only to blobs matching the intended prefix or type remains unverified.
- **D — Correct.** Read the policy filters and test them against both an included and excluded blob name.
  Read the policy filters and test them against both an included and excluded blob name. Because the blob retention and replication service check observes lifecycle rule filters, it independently verifies the requirement to apply retention automation only to blobs matching the intended prefix or type.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q24 — C

**Question:** The data-platform administrator managing blob retention and replication must confirm the blob retention and replication service, without mutation, can move eligible data to a cooler tier after the configured age. Which blob retention check qualifies?

- **A — Incorrect.** Query containerDeleteRetentionPolicy and list deleted containers with the test name.
  Query containerDeleteRetentionPolicy and list deleted containers with the test name. In the blob retention and replication service, this check observes container soft delete. Blob retention and replication service could pass container soft delete while lifecycle tier transitions is wrong; blob retention and replication service still lacks lifecycle tier transitions proof.
- **B — Incorrect.** Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
  Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available. In the blob retention and replication service, this check observes AzCopy copy and sync. Blob retention and replication service output covers AzCopy copy and sync, not lifecycle tier transitions; the lifecycle tier transitions requirement to move eligible data to a cooler tier after the configured age remains unverified.
- **C — Correct.** Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
  The blob retention and replication service validator needs this lifecycle tier transitions result: read the lifecycle action and condition, then confirm only eligible test blobs match the rule. It proves the outcome to move eligible data to a cooler tier after the configured age rather than an adjacent checkpoint.
- **D — Incorrect.** Read the policy filters and test them against both an included and excluded blob name.
  Read the policy filters and test them against both an included and excluded blob name. In the blob retention and replication service, this check observes lifecycle rule filters. Blob retention and replication service reads lifecycle rule filters, leaving lifecycle tier transitions unproved in blob retention and replication service; blob retention and replication service still has no lifecycle tier transitions proof.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q25 — D

**Question:** The blob retention and replication service configuration is complete; the blob retention reviewers need evidence it can delete only objects that satisfy the retention rule's age conditions. Which observation shows success?

- **A — Incorrect.** List blob versions and confirm distinct version IDs and current-version state.
  List blob versions and confirm distinct version IDs and current-version state. In the blob retention and replication service, this check observes blob versioning. Blob retention and replication service output covers blob versioning, not lifecycle deletion; the lifecycle deletion requirement to delete only objects that satisfy the retention rule's age conditions remains unverified.
- **B — Incorrect.** List the container and confirm its name, lease state, and publicAccess value.
  List the container and confirm its name, lease state, and publicAccess value. In the blob retention and replication service, this check observes blob containers. Blob containers success in blob retention and replication service cannot verify lifecycle deletion; blob retention and replication service cannot delete only objects that satisfy the retention rule's age conditions until lifecycle deletion evidence exists.
- **C — Incorrect.** Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
  Read the lifecycle action and condition, then confirm only eligible test blobs match the rule. In the blob retention and replication service, this check observes lifecycle tier transitions. Blob retention and replication service reads lifecycle tier transitions, leaving lifecycle deletion unproved in blob retention and replication service; blob retention and replication service still has no lifecycle deletion proof.
- **D — Correct.** Inspect the delete condition and verify protected or excluded blob prefixes do not match.
  Inspect the delete condition and verify protected or excluded blob prefixes do not match. This is independent lifecycle deletion evidence for the blob retention and replication service, even if blob retention and replication service setup reports success before lifecycle deletion becomes observable.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q26 — B

**Question:** The blob retention validation asks whether the blob retention and replication service can recover a blob deleted after data protection was enabled. Which observable state is strongest?

- **A — Incorrect.** Query the policy IDs on both accounts and verify replication status on a versioned test blob.
  Query the policy IDs on both accounts and verify replication status on a versioned test blob. In the blob retention and replication service, this check observes object replication. Object replication success in blob retention and replication service cannot verify blob soft delete; blob retention and replication service cannot recover a blob deleted after data protection was enabled until blob soft delete evidence exists.
- **B — Correct.** Query deleteRetentionPolicy and confirm enabled and days values.
  Query deleteRetentionPolicy and confirm enabled and days values. For blob retention and replication service, this blob soft delete read confirms the service can recover a blob deleted after data protection was enabled.
- **C — Incorrect.** Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
  Read the blob's accessTier and accessTierChangeTime after the tier operation completes. In the blob retention and replication service, this check observes blob access tiers. Blob retention and replication service could pass blob access tiers while blob soft delete is wrong; blob retention and replication service still lacks blob soft delete proof.
- **D — Incorrect.** Inspect the delete condition and verify protected or excluded blob prefixes do not match.
  Inspect the delete condition and verify protected or excluded blob prefixes do not match. In the blob retention and replication service, this check observes lifecycle deletion. Blob retention and replication service output covers lifecycle deletion, not blob soft delete; the blob soft delete requirement to recover a blob deleted after data protection was enabled remains unverified.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Azure Blob Storage data protection overview](https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q27 — C

**Question:** A blob retention and replication service review must prove the blob retention ability to recover a container removed during its retention window. Which check avoids an adjacent feature?

- **A — Incorrect.** Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
  Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available. In the blob retention and replication service, this check observes AzCopy copy and sync. Blob retention and replication service reads AzCopy copy and sync, leaving container soft delete unproved in blob retention and replication service; blob retention and replication service still has no container soft delete proof.
- **B — Incorrect.** Read the policy filters and test them against both an included and excluded blob name.
  Read the policy filters and test them against both an included and excluded blob name. In the blob retention and replication service, this check observes lifecycle rule filters. Blob retention and replication service could pass lifecycle rule filters while container soft delete is wrong; blob retention and replication service still lacks container soft delete proof.
- **C — Correct.** Query containerDeleteRetentionPolicy and list deleted containers with the test name.
  Query containerDeleteRetentionPolicy and list deleted containers with the test name. The blob retention and replication service reads container soft delete directly; that container soft delete result proves the blob retention and replication service can recover a container removed during its retention window without another mutation.
- **D — Incorrect.** Query deleteRetentionPolicy and confirm enabled and days values.
  Query deleteRetentionPolicy and confirm enabled and days values. In the blob retention and replication service, this check observes blob soft delete. Blob soft delete success in blob retention and replication service cannot verify container soft delete; blob retention and replication service cannot recover a container removed during its retention window until container soft delete evidence exists.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Soft delete for containers](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q28 — B

**Question:** The blob retention and replication service evidence bundle needs a blob retention result showing it can retain an earlier block-blob state after a write or deletion. Which result belongs in the checkpoint?

- **A — Incorrect.** List the container and confirm its name, lease state, and publicAccess value.
  List the container and confirm its name, lease state, and publicAccess value. In the blob retention and replication service, this check observes blob containers. Blob retention and replication service could pass blob containers while blob versioning is wrong; blob retention and replication service still lacks blob versioning proof.
- **B — Correct.** List blob versions and confirm distinct version IDs and current-version state.
  For the blob retention and replication service, this blob versioning observation is decisive: list blob versions and confirm distinct version IDs and current-version state. It is blob retention and replication service evidence that operators can retain an earlier block-blob state after a write or deletion.
- **C — Incorrect.** Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
  Read the lifecycle action and condition, then confirm only eligible test blobs match the rule. In the blob retention and replication service, this check observes lifecycle tier transitions. Lifecycle tier transitions success in blob retention and replication service cannot verify blob versioning; blob retention and replication service cannot retain an earlier block-blob state after a write or deletion until blob versioning evidence exists.
- **D — Incorrect.** Query containerDeleteRetentionPolicy and list deleted containers with the test name.
  Query containerDeleteRetentionPolicy and list deleted containers with the test name. In the blob retention and replication service, this check observes container soft delete. Blob retention and replication service reads container soft delete, leaving blob versioning unproved in blob retention and replication service; blob retention and replication service still has no blob versioning proof.

**Objectives:** `ST-DATA-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q29 — C

**Question:** Before blob retention and replication service cleanup, the blob retention team must reconfirm it can copy supported block-blob changes asynchronously to a second account. Which read-only inspection should run?

- **A — Incorrect.** Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
  Read the blob's accessTier and accessTierChangeTime after the tier operation completes. In the blob retention and replication service, this check observes blob access tiers. Blob retention and replication service output covers blob access tiers, not object replication; the object replication requirement to copy supported block-blob changes asynchronously to a second account remains unverified.
- **B — Incorrect.** Inspect the delete condition and verify protected or excluded blob prefixes do not match.
  Inspect the delete condition and verify protected or excluded blob prefixes do not match. In the blob retention and replication service, this check observes lifecycle deletion. Lifecycle deletion success in blob retention and replication service cannot verify object replication; blob retention and replication service cannot copy supported block-blob changes asynchronously to a second account until object replication evidence exists.
- **C — Correct.** Query the policy IDs on both accounts and verify replication status on a versioned test blob.
  Query the policy IDs on both accounts and verify replication status on a versioned test blob. Because the blob retention and replication service check observes object replication, it independently verifies the requirement to copy supported block-blob changes asynchronously to a second account.
- **D — Incorrect.** List blob versions and confirm distinct version IDs and current-version state.
  List blob versions and confirm distinct version IDs and current-version state. In the blob retention and replication service, this check observes blob versioning. Blob retention and replication service could pass blob versioning while object replication is wrong; blob retention and replication service still lacks object replication proof.

**Objectives:** `ST-ACCOUNTS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Object replication for block blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q30 — A

**Question:** The blob retention and replication service setup reports success after the blob retention attempt to copy a directory safely without deleting unrelated destination data. Which blob retention read-only observation proves the blob retention and replication service outcome?

- **A — Correct.** Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
  The blob retention and replication service validator needs this AzCopy copy and sync result: run a dry comparison or list both endpoints and verify object counts, names, and hashes where available. It proves the outcome to copy a directory safely without deleting unrelated destination data rather than an adjacent checkpoint.
- **B — Incorrect.** Read the policy filters and test them against both an included and excluded blob name.
  Read the policy filters and test them against both an included and excluded blob name. In the blob retention and replication service, this check observes lifecycle rule filters. Blob retention and replication service reads lifecycle rule filters, leaving AzCopy copy and sync unproved in blob retention and replication service; blob retention and replication service still has no AzCopy copy and sync proof.
- **C — Incorrect.** Query deleteRetentionPolicy and confirm enabled and days values.
  Query deleteRetentionPolicy and confirm enabled and days values. In the blob retention and replication service, this check observes blob soft delete. Blob retention and replication service could pass blob soft delete while AzCopy copy and sync is wrong; blob retention and replication service still lacks AzCopy copy and sync proof.
- **D — Incorrect.** Query the policy IDs on both accounts and verify replication status on a versioned test blob.
  Query the policy IDs on both accounts and verify replication status on a versioned test blob. In the blob retention and replication service, this check observes object replication. Blob retention and replication service output covers object replication, not AzCopy copy and sync; the AzCopy copy and sync requirement to copy a directory safely without deleting unrelated destination data remains unverified.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Transfer data with AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)

**Source reviewed:** 2026-08-31

## LAB08-Q31 — C

**Question:** The blob retention and replication service setup finishes, yet the blob retention cannot keep private data from being read without an authorization header. Which misconfiguration explains the mismatch?

- **A — Incorrect.** Frequently read data was moved to archive even though the application requires immediate retrieval.
  Frequently read data was moved to archive even though the application requires immediate retrieval. The blob retention and replication service fault concerns blob access tiers. Blob retention and replication service has blob access tiers impact, but blob containers is the blob retention and replication service failed path; the blob access tiers state cannot produce blob containers failure.
- **B — Incorrect.** The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state.
  The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state. The blob retention and replication service fault concerns blob soft delete. Blob retention and replication service could repair blob soft delete while blob containers stays broken in blob retention and replication service; the blob retention and replication service remains unable to keep private data from being read without an authorization header.
- **C — Correct.** The container permits anonymous blob reads despite a private-data requirement.
  The container permits anonymous blob reads despite a private-data requirement. Removing this blob containers condition lets the blob retention and replication service keep private data from being read without an authorization header while leaving healthy controls unchanged.
- **D — Incorrect.** Sync was run with destination deletion against a path that contains unrelated retained data.
  Sync was run with destination deletion against a path that contains unrelated retained data. The blob retention and replication service fault concerns AzCopy copy and sync. Blob retention and replication service may fix AzCopy copy and sync, yet blob containers still fails; this blob retention and replication service diagnosis of AzCopy copy and sync is wrong for blob containers.

**Objectives:** `ST-DATA-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Configure anonymous read access for containers and blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure)

**Source reviewed:** 2026-08-31

## LAB08-Q32 — C

**Question:** A blob retention break/fix in the blob retention and replication service fails when operators try to place frequently read and rarely read blobs in cost-appropriate tiers. Which diagnosis fits?

- **A — Incorrect.** The rule has no prefix filter and therefore evaluates unrelated containers in the account.
  The rule has no prefix filter and therefore evaluates unrelated containers in the account. The blob retention and replication service fault concerns lifecycle rule filters. Blob retention and replication service could repair lifecycle rule filters while blob access tiers stays broken in blob retention and replication service; the blob retention and replication service remains unable to place frequently read and rarely read blobs in cost-appropriate tiers.
- **B — Incorrect.** Only blob soft delete is enabled, so deleting the entire container is not covered by container retention.
  Only blob soft delete is enabled, so deleting the entire container is not covered by container retention. The blob retention and replication service fault concerns container soft delete. Blob retention and replication service failed on blob access tiers; this container soft delete finding redirects blob retention and replication service remediation away from blob access tiers.
- **C — Correct.** Frequently read data was moved to archive even though the application requires immediate retrieval.
  Frequently read data was moved to archive even though the application requires immediate retrieval. In blob retention and replication service, this blob access tiers cause matches the failure to place frequently read and rarely read blobs in cost-appropriate tiers.
- **D — Incorrect.** The container permits anonymous blob reads despite a private-data requirement.
  The container permits anonymous blob reads despite a private-data requirement. The blob retention and replication service fault concerns blob containers. Blob retention and replication service has blob containers impact, but blob access tiers is the blob retention and replication service failed path; the blob containers state cannot produce blob access tiers failure.

**Objectives:** `ST-DATA-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Access tiers for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q33 — B

**Question:** The blob retention and replication service troubleshooting scope is the blob retention need to apply retention automation only to blobs matching the intended prefix or type. Which condition should be corrected first?

- **A — Incorrect.** The rule uses daysAfterModificationGreaterThan later than the required retention transition.
  The rule uses daysAfterModificationGreaterThan later than the required retention transition. The blob retention and replication service fault concerns lifecycle tier transitions. Blob retention and replication service failed on lifecycle rule filters; this lifecycle tier transitions finding redirects blob retention and replication service remediation away from lifecycle rule filters.
- **B — Correct.** The rule has no prefix filter and therefore evaluates unrelated containers in the account.
  The rule has no prefix filter and therefore evaluates unrelated containers in the account. This blob retention and replication service condition breaks lifecycle rule filters, explaining why operators cannot apply retention automation only to blobs matching the intended prefix or type.
- **C — Incorrect.** The overwrite occurred before versioning was enabled, so no earlier version was created.
  The overwrite occurred before versioning was enabled, so no earlier version was created. The blob retention and replication service fault concerns blob versioning. Blob retention and replication service has blob versioning impact, but lifecycle rule filters is the blob retention and replication service failed path; the blob versioning state cannot produce lifecycle rule filters failure.
- **D — Incorrect.** Frequently read data was moved to archive even though the application requires immediate retrieval.
  Frequently read data was moved to archive even though the application requires immediate retrieval. The blob retention and replication service fault concerns blob access tiers. Blob retention and replication service could repair blob access tiers while lifecycle rule filters stays broken in blob retention and replication service; the blob retention and replication service remains unable to apply retention automation only to blobs matching the intended prefix or type.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q34 — B

**Question:** The blob retention and replication service result is partial because the blob retention cannot move eligible data to a cooler tier after the configured age. Which condition accounts for that result?

- **A — Incorrect.** The delete action targets current versions before the mandated retention period ends.
  The delete action targets current versions before the mandated retention period ends. The blob retention and replication service fault concerns lifecycle deletion. Blob retention and replication service may fix lifecycle deletion, yet lifecycle tier transitions still fails; this blob retention and replication service diagnosis of lifecycle deletion is wrong for lifecycle tier transitions.
- **B — Correct.** The rule uses daysAfterModificationGreaterThan later than the required retention transition.
  For the blob retention and replication service, the lifecycle tier transitions failure is causal: the rule uses daysAfterModificationGreaterThan later than the required retention transition. Correcting it restores the ability to move eligible data to a cooler tier after the configured age.
- **C — Incorrect.** Versioning is disabled on one account, preventing the replication policy from operating.
  Versioning is disabled on one account, preventing the replication policy from operating. The blob retention and replication service fault concerns object replication. Blob retention and replication service could repair object replication while lifecycle tier transitions stays broken in blob retention and replication service; the blob retention and replication service remains unable to move eligible data to a cooler tier after the configured age.
- **D — Incorrect.** The rule has no prefix filter and therefore evaluates unrelated containers in the account.
  The rule has no prefix filter and therefore evaluates unrelated containers in the account. The blob retention and replication service fault concerns lifecycle rule filters. Blob retention and replication service failed on lifecycle tier transitions; this lifecycle rule filters finding redirects blob retention and replication service remediation away from lifecycle tier transitions.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q35 — D

**Question:** The blob retention evidence shows the blob retention and replication service cannot delete only objects that satisfy the retention rule's age conditions. Which root cause fits that evidence?

- **A — Incorrect.** The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state.
  The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state. The blob retention and replication service fault concerns blob soft delete. Blob retention and replication service has blob soft delete impact, but lifecycle deletion is the blob retention and replication service failed path; the blob soft delete state cannot produce lifecycle deletion failure.
- **B — Incorrect.** Sync was run with destination deletion against a path that contains unrelated retained data.
  Sync was run with destination deletion against a path that contains unrelated retained data. The blob retention and replication service fault concerns AzCopy copy and sync. Blob retention and replication service could repair AzCopy copy and sync while lifecycle deletion stays broken in blob retention and replication service; the blob retention and replication service remains unable to delete only objects that satisfy the retention rule's age conditions.
- **C — Incorrect.** The rule uses daysAfterModificationGreaterThan later than the required retention transition.
  The rule uses daysAfterModificationGreaterThan later than the required retention transition. The blob retention and replication service fault concerns lifecycle tier transitions. Blob retention and replication service failed on lifecycle deletion; this lifecycle tier transitions finding redirects blob retention and replication service remediation away from lifecycle deletion.
- **D — Correct.** The delete action targets current versions before the mandated retention period ends.
  The delete action targets current versions before the mandated retention period ends. The finding is specific to lifecycle deletion in the blob retention and replication service; repairing lifecycle deletion restores the blob retention and replication service ability to delete only objects that satisfy the retention rule's age conditions.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q36 — A

**Question:** Although the blob retention and replication service is meant to let the blob retention recover a blob deleted after data protection was enabled, its checkpoint fails. Which blob retention defect explains the failure?

- **A — Correct.** The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state.
  The blob retention and replication service cannot recover a blob deleted after data protection was enabled because of this blob soft delete defect: the blob was deleted before soft delete was enabled and has no recoverable soft-deleted state. The symptom and repair align.
- **B — Incorrect.** Only blob soft delete is enabled, so deleting the entire container is not covered by container retention.
  Only blob soft delete is enabled, so deleting the entire container is not covered by container retention. The blob retention and replication service fault concerns container soft delete. Blob retention and replication service failed on blob soft delete; this container soft delete finding redirects blob retention and replication service remediation away from blob soft delete.
- **C — Incorrect.** The container permits anonymous blob reads despite a private-data requirement.
  The container permits anonymous blob reads despite a private-data requirement. The blob retention and replication service fault concerns blob containers. Blob retention and replication service may fix blob containers, yet blob soft delete still fails; this blob retention and replication service diagnosis of blob containers is wrong for blob soft delete.
- **D — Incorrect.** The delete action targets current versions before the mandated retention period ends.
  The delete action targets current versions before the mandated retention period ends. The blob retention and replication service fault concerns lifecycle deletion. Blob retention and replication service has lifecycle deletion impact, but blob soft delete is the blob retention and replication service failed path; the lifecycle deletion state cannot produce blob soft delete failure.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Azure Blob Storage data protection overview](https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q37 — A

**Question:** The blob retention support team isolated the blob retention and replication service incident to the attempt to recover a container removed during its retention window. Which condition prevents success?

- **A — Correct.** Only blob soft delete is enabled, so deleting the entire container is not covered by container retention.
  Only blob soft delete is enabled, so deleting the entire container is not covered by container retention. Removing this container soft delete condition lets the blob retention and replication service recover a container removed during its retention window while leaving healthy controls unchanged.
- **B — Incorrect.** The overwrite occurred before versioning was enabled, so no earlier version was created.
  The overwrite occurred before versioning was enabled, so no earlier version was created. The blob retention and replication service fault concerns blob versioning. Blob retention and replication service may fix blob versioning, yet container soft delete still fails; this blob retention and replication service diagnosis of blob versioning is wrong for container soft delete.
- **C — Incorrect.** Frequently read data was moved to archive even though the application requires immediate retrieval.
  Frequently read data was moved to archive even though the application requires immediate retrieval. The blob retention and replication service fault concerns blob access tiers. Blob retention and replication service has blob access tiers impact, but container soft delete is the blob retention and replication service failed path; the blob access tiers state cannot produce container soft delete failure.
- **D — Incorrect.** The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state.
  The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state. The blob retention and replication service fault concerns blob soft delete. Blob retention and replication service could repair blob soft delete while container soft delete stays broken in blob retention and replication service; the blob retention and replication service remains unable to recover a container removed during its retention window.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Soft delete for containers](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q38 — A

**Question:** A blob retention and replication service query surprises the data-platform administrator managing blob retention and replication during the blob retention attempt to retain an earlier block-blob state after a write or deletion. Which finding explains it?

- **A — Correct.** The overwrite occurred before versioning was enabled, so no earlier version was created.
  The overwrite occurred before versioning was enabled, so no earlier version was created. In blob retention and replication service, this blob versioning cause matches the failure to retain an earlier block-blob state after a write or deletion.
- **B — Incorrect.** Versioning is disabled on one account, preventing the replication policy from operating.
  Versioning is disabled on one account, preventing the replication policy from operating. The blob retention and replication service fault concerns object replication. Blob retention and replication service has object replication impact, but blob versioning is the blob retention and replication service failed path; the object replication state cannot produce blob versioning failure.
- **C — Incorrect.** The rule has no prefix filter and therefore evaluates unrelated containers in the account.
  The rule has no prefix filter and therefore evaluates unrelated containers in the account. The blob retention and replication service fault concerns lifecycle rule filters. Blob retention and replication service could repair lifecycle rule filters while blob versioning stays broken in blob retention and replication service; the blob retention and replication service remains unable to retain an earlier block-blob state after a write or deletion.
- **D — Incorrect.** Only blob soft delete is enabled, so deleting the entire container is not covered by container retention.
  Only blob soft delete is enabled, so deleting the entire container is not covered by container retention. The blob retention and replication service fault concerns container soft delete. Blob retention and replication service failed on blob versioning; this container soft delete finding redirects blob retention and replication service remediation away from blob versioning.

**Objectives:** `ST-DATA-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q39 — B

**Question:** Other blob retention and replication service components are healthy, but the blob retention still cannot copy supported block-blob changes asynchronously to a second account. Which state causes the isolated failure?

- **A — Incorrect.** Sync was run with destination deletion against a path that contains unrelated retained data.
  Sync was run with destination deletion against a path that contains unrelated retained data. The blob retention and replication service fault concerns AzCopy copy and sync. Blob retention and replication service has AzCopy copy and sync impact, but object replication is the blob retention and replication service failed path; the AzCopy copy and sync state cannot produce object replication failure.
- **B — Correct.** Versioning is disabled on one account, preventing the replication policy from operating.
  Versioning is disabled on one account, preventing the replication policy from operating. This blob retention and replication service condition breaks object replication, explaining why operators cannot copy supported block-blob changes asynchronously to a second account.
- **C — Incorrect.** The rule uses daysAfterModificationGreaterThan later than the required retention transition.
  The rule uses daysAfterModificationGreaterThan later than the required retention transition. The blob retention and replication service fault concerns lifecycle tier transitions. Blob retention and replication service failed on object replication; this lifecycle tier transitions finding redirects blob retention and replication service remediation away from object replication.
- **D — Incorrect.** The overwrite occurred before versioning was enabled, so no earlier version was created.
  The overwrite occurred before versioning was enabled, so no earlier version was created. The blob retention and replication service fault concerns blob versioning. Blob retention and replication service may fix blob versioning, yet object replication still fails; this blob retention and replication service diagnosis of blob versioning is wrong for object replication.

**Objectives:** `ST-ACCOUNTS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Object replication for block blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q40 — A

**Question:** During a blob retention fault drill, the blob retention and replication service does not copy a directory safely without deleting unrelated destination data. Which finding identifies the defect?

- **A — Correct.** Sync was run with destination deletion against a path that contains unrelated retained data.
  For the blob retention and replication service, the AzCopy copy and sync failure is causal: sync was run with destination deletion against a path that contains unrelated retained data. Correcting it restores the ability to copy a directory safely without deleting unrelated destination data.
- **B — Incorrect.** The container permits anonymous blob reads despite a private-data requirement.
  The container permits anonymous blob reads despite a private-data requirement. The blob retention and replication service fault concerns blob containers. Blob retention and replication service failed on AzCopy copy and sync; this blob containers finding redirects blob retention and replication service remediation away from AzCopy copy and sync.
- **C — Incorrect.** The delete action targets current versions before the mandated retention period ends.
  The delete action targets current versions before the mandated retention period ends. The blob retention and replication service fault concerns lifecycle deletion. Blob retention and replication service may fix lifecycle deletion, yet AzCopy copy and sync still fails; this blob retention and replication service diagnosis of lifecycle deletion is wrong for AzCopy copy and sync.
- **D — Incorrect.** Versioning is disabled on one account, preventing the replication policy from operating.
  Versioning is disabled on one account, preventing the replication policy from operating. The blob retention and replication service fault concerns object replication. Blob retention and replication service has object replication impact, but AzCopy copy and sync is the blob retention and replication service failed path; the object replication state cannot produce AzCopy copy and sync failure.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Transfer data with AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)

**Source reviewed:** 2026-08-31

## LAB08-Q41 — A

**Question:** To satisfy the blob retention requirement, operators must change the blob retention and replication service configuration and prove it can keep private data from being read without an authorization header. Which sequence is coherent?

- **A — Correct.** First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value.
  First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value. The blob retention and replication service uses its blob containers mutation gate and blob containers verification gate before it can keep private data from being read without an authorization header.
- **B — Incorrect.** First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.
  First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name. This blob retention and replication service pair serves lifecycle rule filters. Blob retention and replication service proves lifecycle rule filters, but blob containers lacks implementation in blob retention and replication service and blob containers proof; the blob containers outcome to keep private data from being read without an authorization header remains open.
- **C — Incorrect.** First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.
  First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name. This blob retention and replication service pair serves container soft delete. Blob retention and replication service uses container soft delete for both steps; blob containers remains untouched in blob retention and replication service, so its blob containers gate to keep private data from being read without an authorization header fails.
- **D — Incorrect.** First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.
  First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state. This blob retention and replication service pair serves blob versioning. Blob retention and replication service closes blob versioning, not blob containers; without the blob containers workflow, it cannot keep private data from being read without an authorization header.

**Objectives:** `ST-DATA-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Configure anonymous read access for containers and blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure)

**Source reviewed:** 2026-08-31

## LAB08-Q42 — C

**Question:** The data-platform administrator managing blob retention and replication needs a safe blob retention and replication service change to place frequently read and rarely read blobs in cost-appropriate tiers, followed by blob retention evidence. Which pair merits approval?

- **A — Incorrect.** First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
  First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule. This blob retention and replication service pair serves lifecycle tier transitions. Blob retention and replication service proves lifecycle tier transitions, but blob access tiers lacks implementation in blob retention and replication service and blob access tiers proof; the blob access tiers outcome to place frequently read and rarely read blobs in cost-appropriate tiers remains open.
- **B — Incorrect.** First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.
  First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state. This blob retention and replication service pair serves blob versioning. Blob retention and replication service uses blob versioning for both steps; blob access tiers remains untouched in blob retention and replication service, so its blob access tiers gate to place frequently read and rarely read blobs in cost-appropriate tiers fails.
- **C — Correct.** First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
  The blob retention and replication service gets a complete blob access tiers sequence here: first, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes. Read-back evidence follows the change.
- **D — Incorrect.** First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.
  First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob. This blob retention and replication service pair serves object replication. Object replication cannot replace blob access tiers in blob retention and replication service. Use this blob access tiers pair instead: First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.

**Objectives:** `ST-DATA-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Access tiers for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q43 — A

**Question:** The blob retention and replication service has two blob retention gates: apply retention automation only to blobs matching the intended prefix or type, then prove the blob retention and replication service state. Which blob retention sequence works?

- **A — Correct.** First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.
  First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name. This ordered lifecycle rule filters workflow lets the blob retention and replication service apply retention automation only to blobs matching the intended prefix or type and then verify the resulting state.
- **B — Incorrect.** First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match.
  First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match. This blob retention and replication service pair serves lifecycle deletion. Blob retention and replication service closes lifecycle deletion, not lifecycle rule filters; without the lifecycle rule filters workflow, it cannot apply retention automation only to blobs matching the intended prefix or type.
- **C — Incorrect.** First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.
  First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob. This blob retention and replication service pair serves object replication. Object replication cannot replace lifecycle rule filters in blob retention and replication service. Use this lifecycle rule filters pair instead: First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.
- **D — Incorrect.** First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
  First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available. This blob retention and replication service pair serves AzCopy copy and sync. Blob retention and replication service proves AzCopy copy and sync, but lifecycle rule filters lacks implementation in blob retention and replication service and lifecycle rule filters proof; the lifecycle rule filters outcome to apply retention automation only to blobs matching the intended prefix or type remains open.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q44 — A

**Question:** Which blob retention path makes the blob retention and replication service able to move eligible data to a cooler tier after the configured age, then inspects the defining properties?

- **A — Correct.** First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
  First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule. For blob retention and replication service, the lifecycle tier transitions operation precedes its lifecycle tier transitions read-back check, allowing it to move eligible data to a cooler tier after the configured age.
- **B — Incorrect.** First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.
  First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values. This blob retention and replication service pair serves blob soft delete. Blob soft delete cannot replace lifecycle tier transitions in blob retention and replication service. Use this lifecycle tier transitions pair instead: First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
- **C — Incorrect.** First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
  First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available. This blob retention and replication service pair serves AzCopy copy and sync. Blob retention and replication service proves AzCopy copy and sync, but lifecycle tier transitions lacks implementation in blob retention and replication service and lifecycle tier transitions proof; the lifecycle tier transitions outcome to move eligible data to a cooler tier after the configured age remains open.
- **D — Incorrect.** First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value.
  First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value. This blob retention and replication service pair serves blob containers. Blob retention and replication service uses blob containers for both steps; lifecycle tier transitions remains untouched in blob retention and replication service, so its lifecycle tier transitions gate to move eligible data to a cooler tier after the configured age fails.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q45 — A

**Question:** At the blob retention and replication service approval gate, operators must show that the blob retention can delete only objects that satisfy the retention rule's age conditions. Which blob retention configure-and-check pair is defensible?

- **A — Correct.** First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match.
  First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match. In the blob retention and replication service, the first lifecycle deletion step runs; the blob retention and replication service then reads lifecycle deletion state to prove it can delete only objects that satisfy the retention rule's age conditions.
- **B — Incorrect.** First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.
  First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name. This blob retention and replication service pair serves container soft delete. Blob retention and replication service proves container soft delete, but lifecycle deletion lacks implementation in blob retention and replication service and lifecycle deletion proof; the lifecycle deletion outcome to delete only objects that satisfy the retention rule's age conditions remains open.
- **C — Incorrect.** First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value.
  First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value. This blob retention and replication service pair serves blob containers. Blob retention and replication service uses blob containers for both steps; lifecycle deletion remains untouched in blob retention and replication service, so its lifecycle deletion gate to delete only objects that satisfy the retention rule's age conditions fails.
- **D — Incorrect.** First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
  First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes. This blob retention and replication service pair serves blob access tiers. Blob retention and replication service closes blob access tiers, not lifecycle deletion; without the lifecycle deletion workflow, it cannot delete only objects that satisfy the retention rule's age conditions.

**Objectives:** `ST-DATA-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Azure Blob Storage lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q46 — B

**Question:** The blob retention and replication service forbids a partial blob retention result. Operators must first recover a blob deleted after data protection was enabled and afterward confirm the blob retention and replication service outcome. Which blob retention sequence is complete?

- **A — Incorrect.** First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.
  First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state. This blob retention and replication service pair serves blob versioning. Blob retention and replication service proves blob versioning, but blob soft delete lacks implementation in blob retention and replication service and blob soft delete proof; the blob soft delete outcome to recover a blob deleted after data protection was enabled remains open.
- **B — Correct.** First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.
  For the blob retention and replication service, the safe blob soft delete order is: first, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values. The blob retention and replication service records blob soft delete proof after configuration.
- **C — Incorrect.** First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
  First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes. This blob retention and replication service pair serves blob access tiers. Blob retention and replication service closes blob access tiers, not blob soft delete; without the blob soft delete workflow, it cannot recover a blob deleted after data protection was enabled.
- **D — Incorrect.** First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.
  First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name. This blob retention and replication service pair serves lifecycle rule filters. Lifecycle rule filters cannot replace blob soft delete in blob retention and replication service. Use this blob soft delete pair instead: First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB08-CP01`).

**Microsoft Learn sources:**

- [Azure Blob Storage data protection overview](https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q47 — A

**Question:** Only the blob retention and replication service change needed to recover a container removed during its retention window is allowed, and blob retention proof is mandatory. Which pair fits?

- **A — Correct.** First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.
  First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name. The blob retention and replication service uses its container soft delete mutation gate and container soft delete verification gate before it can recover a container removed during its retention window.
- **B — Incorrect.** First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.
  First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob. This blob retention and replication service pair serves object replication. Blob retention and replication service closes object replication, not container soft delete; without the container soft delete workflow, it cannot recover a container removed during its retention window.
- **C — Incorrect.** First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.
  First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name. This blob retention and replication service pair serves lifecycle rule filters. Lifecycle rule filters cannot replace container soft delete in blob retention and replication service. Use this container soft delete pair instead: First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.
- **D — Incorrect.** First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
  First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule. This blob retention and replication service pair serves lifecycle tier transitions. Blob retention and replication service proves lifecycle tier transitions, but container soft delete lacks implementation in blob retention and replication service and container soft delete proof; the container soft delete outcome to recover a container removed during its retention window remains open.

**Objectives:** `ST-DATA-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB08-CP02`).

**Microsoft Learn sources:**

- [Soft delete for containers](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q48 — A

**Question:** The blob retention and replication service runbook separates blob retention mutation from validation while it must retain an earlier block-blob state after a write or deletion. Which sequence proves it cleanly?

- **A — Correct.** First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.
  The blob retention and replication service gets a complete blob versioning sequence here: first, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state. Read-back evidence follows the change.
- **B — Incorrect.** First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
  First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available. This blob retention and replication service pair serves AzCopy copy and sync. AzCopy copy and sync cannot replace blob versioning in blob retention and replication service. Use this blob versioning pair instead: First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.
- **C — Incorrect.** First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
  First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule. This blob retention and replication service pair serves lifecycle tier transitions. Blob retention and replication service proves lifecycle tier transitions, but blob versioning lacks implementation in blob retention and replication service and blob versioning proof; the blob versioning outcome to retain an earlier block-blob state after a write or deletion remains open.
- **D — Incorrect.** First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match.
  First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match. This blob retention and replication service pair serves lifecycle deletion. Blob retention and replication service uses lifecycle deletion for both steps; blob versioning remains untouched in blob retention and replication service, so its blob versioning gate to retain an earlier block-blob state after a write or deletion fails.

**Objectives:** `ST-DATA-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB08-CP03`).

**Microsoft Learn sources:**

- [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q49 — D

**Question:** The blob retention and replication service checkpoint requires both this blob retention outcome—copy supported block-blob changes asynchronously to a second account—and a read-only blob retention and replication service state check. Which blob retention response is complete?

- **A — Incorrect.** First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value.
  First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value. This blob retention and replication service pair serves blob containers. Blob containers cannot replace object replication in blob retention and replication service. Use this object replication pair instead: First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.
- **B — Incorrect.** First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match.
  First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match. This blob retention and replication service pair serves lifecycle deletion. Blob retention and replication service proves lifecycle deletion, but object replication lacks implementation in blob retention and replication service and object replication proof; the object replication outcome to copy supported block-blob changes asynchronously to a second account remains open.
- **C — Incorrect.** First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.
  First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values. This blob retention and replication service pair serves blob soft delete. Blob retention and replication service uses blob soft delete for both steps; object replication remains untouched in blob retention and replication service, so its object replication gate to copy supported block-blob changes asynchronously to a second account fails.
- **D — Correct.** First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.
  First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob. This ordered object replication workflow lets the blob retention and replication service copy supported block-blob changes asynchronously to a second account and then verify the resulting state.

**Objectives:** `ST-ACCOUNTS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB08-CP04`).

**Microsoft Learn sources:**

- [Object replication for block blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview)

**Source reviewed:** 2026-08-31

## LAB08-Q50 — C

**Question:** The blob retention and replication service runbook must copy a directory safely without deleting unrelated destination data, then retain blob retention read-back evidence. Which blob retention and replication service pair completes both duties?

- **A — Incorrect.** First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
  First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes. This blob retention and replication service pair serves blob access tiers. Blob retention and replication service proves blob access tiers, but AzCopy copy and sync lacks implementation in blob retention and replication service and AzCopy copy and sync proof; the AzCopy copy and sync outcome to copy a directory safely without deleting unrelated destination data remains open.
- **B — Incorrect.** First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.
  First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values. This blob retention and replication service pair serves blob soft delete. Blob retention and replication service uses blob soft delete for both steps; AzCopy copy and sync remains untouched in blob retention and replication service, so its AzCopy copy and sync gate to copy a directory safely without deleting unrelated destination data fails.
- **C — Correct.** First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
  First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available. For blob retention and replication service, the AzCopy copy and sync operation precedes its AzCopy copy and sync read-back check, allowing it to copy a directory safely without deleting unrelated destination data.
- **D — Incorrect.** First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.
  First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name. This blob retention and replication service pair serves container soft delete. Container soft delete cannot replace AzCopy copy and sync in blob retention and replication service. Use this AzCopy copy and sync pair instead: First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB08-CP05`).

**Microsoft Learn sources:**

- [Transfer data with AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)

**Source reviewed:** 2026-08-31
