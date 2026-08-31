# Lab 06 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB06-Q01 — B

**Question:** A new storage hardening operator must explain why the hardened general-purpose storage account can create the general-purpose account type that supports current storage services. Which explanation is accurate?

- **A — Incorrect.** A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers.
  A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers. In the hardened general-purpose storage account, this statement describes storage account naming. Hardened general-purpose storage account asks about StorageV2 accounts; this storage account naming choice leaves the StorageV2 accounts explanation missing.
- **B — Correct.** A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features.
  For the hardened general-purpose storage account, the rule for StorageV2 accounts is defined by this statement: a StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features. It supports the required outcome to create the general-purpose account type that supports current storage services.
- **C — Incorrect.** RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally.
  RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally. In the hardened general-purpose storage account, this statement describes geo-redundant read access. Selecting geo-redundant read access for hardened general-purpose storage account leaves StorageV2 accounts unanswered in hardened general-purpose storage account; the hardened general-purpose storage account lacks a StorageV2 accounts basis to create the general-purpose account type that supports current storage services.
- **D — Incorrect.** Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism.
  Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism. In the hardened general-purpose storage account, this statement describes shared key authorization. StorageV2 accounts governs hardened general-purpose storage account; shared key authorization cannot support StorageV2 accounts when operators must create the general-purpose account type that supports current storage services.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q02 — D

**Question:** The hardened general-purpose storage account acceptance criteria require operators to produce a globally unique lowercase account name with no punctuation. Which service fact supports that requirement?

- **A — Incorrect.** LRS keeps three synchronous copies within one physical location in the primary region.
  LRS keeps three synchronous copies within one physical location in the primary region. In the hardened general-purpose storage account, this statement describes locally redundant storage. The locally redundant storage statement accurately describes locally redundant storage; however, hardened general-purpose storage account needs storage account naming to produce a globally unique lowercase account name with no punctuation; locally redundant storage cannot replace storage account naming.
- **B — Incorrect.** Secure transfer required rejects supported storage requests made over unencrypted HTTP.
  Secure transfer required rejects supported storage requests made over unencrypted HTTP. In the hardened general-purpose storage account, this statement describes secure transfer required. Selecting secure transfer required for hardened general-purpose storage account leaves storage account naming unanswered in hardened general-purpose storage account; the hardened general-purpose storage account lacks a storage account naming basis to produce a globally unique lowercase account name with no punctuation.
- **C — Incorrect.** Rotating one storage key at a time preserves a second valid key for applications during rollover.
  Rotating one storage key at a time preserves a second valid key for applications during rollover. In the hardened general-purpose storage account, this statement describes access-key rotation. Storage account naming governs hardened general-purpose storage account; access-key rotation cannot support storage account naming when operators must produce a globally unique lowercase account name with no punctuation.
- **D — Correct.** A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers.
  A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers. The hardened general-purpose storage account applies that storage account naming boundary when operators must produce a globally unique lowercase account name with no punctuation.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q03 — A

**Question:** A storage hardening reviewer challenges whether the hardened general-purpose storage account can replicate data synchronously three ways at a single site. Which response resolves the concern?

- **A — Correct.** LRS keeps three synchronous copies within one physical location in the primary region.
  The hardened general-purpose storage account needs locally redundant storage to replicate data synchronously three ways at a single site; this option states the applicable locally redundant storage rule: lRS keeps three synchronous copies within one physical location in the primary region.
- **B — Incorrect.** ZRS synchronously replicates data across availability zones in the primary region.
  ZRS synchronously replicates data across availability zones in the primary region. In the hardened general-purpose storage account, this statement describes zone-redundant storage. Locally redundant storage governs hardened general-purpose storage account; zone-redundant storage cannot support locally redundant storage when operators must replicate data synchronously three ways at a single site.
- **C — Incorrect.** The minimum TLS setting rejects client connections that negotiate an older protocol version.
  The minimum TLS setting rejects client connections that negotiate an older protocol version. In the hardened general-purpose storage account, this statement describes minimum TLS version. Hardened general-purpose storage account asks about locally redundant storage; this minimum TLS version choice leaves the locally redundant storage explanation missing.
- **D — Incorrect.** Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys.
  Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys. In the hardened general-purpose storage account, this statement describes storage service encryption. The storage service encryption statement accurately describes storage service encryption; however, hardened general-purpose storage account needs locally redundant storage to replicate data synchronously three ways at a single site; storage service encryption cannot replace locally redundant storage.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q04 — B

**Question:** The hardened general-purpose storage account handoff omits the storage hardening rule needed to survive a single availability-zone failure within the primary region. Which statement should the team add?

- **A — Incorrect.** RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally.
  RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally. In the hardened general-purpose storage account, this statement describes geo-redundant read access. Zone-redundant storage governs hardened general-purpose storage account; geo-redundant read access cannot support zone-redundant storage when operators must survive a single availability-zone failure within the primary region.
- **B — Correct.** ZRS synchronously replicates data across availability zones in the primary region.
  ZRS synchronously replicates data across availability zones in the primary region. This zone-redundant storage fact resolves the hardened general-purpose storage account design question about how to survive a single availability-zone failure within the primary region.
- **C — Incorrect.** Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism.
  Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism. In the hardened general-purpose storage account, this statement describes shared key authorization. The shared key authorization statement accurately describes shared key authorization; however, hardened general-purpose storage account needs zone-redundant storage to survive a single availability-zone failure within the primary region; shared key authorization cannot replace zone-redundant storage.
- **D — Incorrect.** A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features.
  A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features. In the hardened general-purpose storage account, this statement describes StorageV2 accounts. Selecting StorageV2 accounts for hardened general-purpose storage account leaves zone-redundant storage unanswered in hardened general-purpose storage account; the hardened general-purpose storage account lacks a zone-redundant storage basis to survive a single availability-zone failure within the primary region.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q05 — C

**Question:** A storage hardening incident review of the hardened general-purpose storage account depends on the ability to allow reads from the secondary region when geo-replicated data is available. Which platform description is reliable?

- **A — Incorrect.** Secure transfer required rejects supported storage requests made over unencrypted HTTP.
  Secure transfer required rejects supported storage requests made over unencrypted HTTP. In the hardened general-purpose storage account, this statement describes secure transfer required. Hardened general-purpose storage account asks about geo-redundant read access; this secure transfer required choice leaves the geo-redundant read access explanation missing.
- **B — Incorrect.** Rotating one storage key at a time preserves a second valid key for applications during rollover.
  Rotating one storage key at a time preserves a second valid key for applications during rollover. In the hardened general-purpose storage account, this statement describes access-key rotation. The access-key rotation statement accurately describes access-key rotation; however, hardened general-purpose storage account needs geo-redundant read access to allow reads from the secondary region when geo-replicated data is available; access-key rotation cannot replace geo-redundant read access.
- **C — Correct.** RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally.
  RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally. For hardened general-purpose storage account, geo-redundant read access supplies the service rule needed to allow reads from the secondary region when geo-replicated data is available.
- **D — Incorrect.** A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers.
  A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers. In the hardened general-purpose storage account, this statement describes storage account naming. Geo-redundant read access governs hardened general-purpose storage account; storage account naming cannot support geo-redundant read access when operators must allow reads from the secondary region when geo-replicated data is available.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q06 — C

**Question:** A storage administrator hardening a general-purpose account is updating the storage hardening runbook. The requirement is to reject storage requests that do not use an encrypted transport. Which statement describes Azure behavior correctly?

- **A — Incorrect.** The minimum TLS setting rejects client connections that negotiate an older protocol version.
  The minimum TLS setting rejects client connections that negotiate an older protocol version. In the hardened general-purpose storage account, this statement describes minimum TLS version. The minimum TLS version statement accurately describes minimum TLS version; however, hardened general-purpose storage account needs secure transfer required to reject storage requests that do not use an encrypted transport; minimum TLS version cannot replace secure transfer required.
- **B — Incorrect.** Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys.
  Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys. In the hardened general-purpose storage account, this statement describes storage service encryption. Selecting storage service encryption for hardened general-purpose storage account leaves secure transfer required unanswered in hardened general-purpose storage account; the hardened general-purpose storage account lacks a secure transfer required basis to reject storage requests that do not use an encrypted transport.
- **C — Correct.** Secure transfer required rejects supported storage requests made over unencrypted HTTP.
  Secure transfer required rejects supported storage requests made over unencrypted HTTP. In the hardened general-purpose storage account, this secure transfer required rule supports the need to reject storage requests that do not use an encrypted transport.
- **D — Incorrect.** LRS keeps three synchronous copies within one physical location in the primary region.
  LRS keeps three synchronous copies within one physical location in the primary region. In the hardened general-purpose storage account, this statement describes locally redundant storage. Hardened general-purpose storage account asks about secure transfer required; this locally redundant storage choice leaves the secure transfer required explanation missing.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Require secure transfer for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer)

**Source reviewed:** 2026-08-31

## LAB06-Q07 — B

**Question:** A storage hardening peer review asks how the hardened general-purpose storage account should handle this outcome: refuse clients that negotiate an obsolete transport protocol. Which explanation is accurate?

- **A — Incorrect.** Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism.
  Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism. In the hardened general-purpose storage account, this statement describes shared key authorization. Selecting shared key authorization for hardened general-purpose storage account leaves minimum TLS version unanswered in hardened general-purpose storage account; the hardened general-purpose storage account lacks a minimum TLS version basis to refuse clients that negotiate an obsolete transport protocol.
- **B — Correct.** The minimum TLS setting rejects client connections that negotiate an older protocol version.
  For the hardened general-purpose storage account, the rule for minimum TLS version is defined by this statement: the minimum TLS setting rejects client connections that negotiate an older protocol version. It supports the required outcome to refuse clients that negotiate an obsolete transport protocol.
- **C — Incorrect.** A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features.
  A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features. In the hardened general-purpose storage account, this statement describes StorageV2 accounts. Hardened general-purpose storage account asks about minimum TLS version; this StorageV2 accounts choice leaves the minimum TLS version explanation missing.
- **D — Incorrect.** ZRS synchronously replicates data across availability zones in the primary region.
  ZRS synchronously replicates data across availability zones in the primary region. In the hardened general-purpose storage account, this statement describes zone-redundant storage. The zone-redundant storage statement accurately describes zone-redundant storage; however, hardened general-purpose storage account needs minimum TLS version to refuse clients that negotiate an obsolete transport protocol; zone-redundant storage cannot replace minimum TLS version.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Configure a minimum TLS version for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/transport-layer-security-configure-minimum-version)

**Source reviewed:** 2026-08-31

## LAB06-Q08 — C

**Question:** For the hardened general-purpose storage account, the storage hardening plan must accept only Microsoft Entra credentials for data access. Which statement about storage hardening belongs in the hardened general-purpose storage account record?

- **A — Incorrect.** Rotating one storage key at a time preserves a second valid key for applications during rollover.
  Rotating one storage key at a time preserves a second valid key for applications during rollover. In the hardened general-purpose storage account, this statement describes access-key rotation. Shared key authorization governs hardened general-purpose storage account; access-key rotation cannot support shared key authorization when operators must accept only Microsoft Entra credentials for data access.
- **B — Incorrect.** A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers.
  A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers. In the hardened general-purpose storage account, this statement describes storage account naming. Hardened general-purpose storage account asks about shared key authorization; this storage account naming choice leaves the shared key authorization explanation missing.
- **C — Correct.** Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism.
  Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism. The hardened general-purpose storage account applies that shared key authorization boundary when operators must accept only Microsoft Entra credentials for data access.
- **D — Incorrect.** RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally.
  RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally. In the hardened general-purpose storage account, this statement describes geo-redundant read access. Selecting geo-redundant read access for hardened general-purpose storage account leaves shared key authorization unanswered in hardened general-purpose storage account; the hardened general-purpose storage account lacks a shared key authorization basis to accept only Microsoft Entra credentials for data access.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB06-Q09 — B

**Question:** The storage hardening review compares four claims for the hardened general-purpose storage account requirement to replace a compromised credential without losing the second recovery credential. Which claim is technically sound?

- **A — Incorrect.** Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys.
  Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys. In the hardened general-purpose storage account, this statement describes storage service encryption. Hardened general-purpose storage account asks about access-key rotation; this storage service encryption choice leaves the access-key rotation explanation missing.
- **B — Correct.** Rotating one storage key at a time preserves a second valid key for applications during rollover.
  The hardened general-purpose storage account needs access-key rotation to replace a compromised credential without losing the second recovery credential; this option states the applicable access-key rotation rule: rotating one storage key at a time preserves a second valid key for applications during rollover.
- **C — Incorrect.** LRS keeps three synchronous copies within one physical location in the primary region.
  LRS keeps three synchronous copies within one physical location in the primary region. In the hardened general-purpose storage account, this statement describes locally redundant storage. Selecting locally redundant storage for hardened general-purpose storage account leaves access-key rotation unanswered in hardened general-purpose storage account; the hardened general-purpose storage account lacks a access-key rotation basis to replace a compromised credential without losing the second recovery credential.
- **D — Incorrect.** Secure transfer required rejects supported storage requests made over unencrypted HTTP.
  Secure transfer required rejects supported storage requests made over unencrypted HTTP. In the hardened general-purpose storage account, this statement describes secure transfer required. Access-key rotation governs hardened general-purpose storage account; secure transfer required cannot support access-key rotation when operators must replace a compromised credential without losing the second recovery credential.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Manage Azure Storage account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)

**Source reviewed:** 2026-08-31

## LAB06-Q10 — D

**Question:** The storage hardening architecture note requires the hardened general-purpose storage account environment to confirm that stored service data is encrypted without an application change. Which statement defines the relevant storage hardening boundary?

- **A — Incorrect.** A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features.
  A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features. In the hardened general-purpose storage account, this statement describes StorageV2 accounts. The StorageV2 accounts statement accurately describes StorageV2 accounts; however, hardened general-purpose storage account needs storage service encryption to confirm that stored service data is encrypted without an application change; StorageV2 accounts cannot replace storage service encryption.
- **B — Incorrect.** ZRS synchronously replicates data across availability zones in the primary region.
  ZRS synchronously replicates data across availability zones in the primary region. In the hardened general-purpose storage account, this statement describes zone-redundant storage. Selecting zone-redundant storage for hardened general-purpose storage account leaves storage service encryption unanswered in hardened general-purpose storage account; the hardened general-purpose storage account lacks a storage service encryption basis to confirm that stored service data is encrypted without an application change.
- **C — Incorrect.** The minimum TLS setting rejects client connections that negotiate an older protocol version.
  The minimum TLS setting rejects client connections that negotiate an older protocol version. In the hardened general-purpose storage account, this statement describes minimum TLS version. Storage service encryption governs hardened general-purpose storage account; minimum TLS version cannot support storage service encryption when operators must confirm that stored service data is encrypted without an application change.
- **D — Correct.** Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys.
  Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys. This storage service encryption fact resolves the hardened general-purpose storage account design question about how to confirm that stored service data is encrypted without an application change.

**Objectives:** `ST-ACCOUNTS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage encryption for data at rest](https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption)

**Source reviewed:** 2026-08-31

## LAB06-Q11 — A

**Question:** Operators must automate the hardened general-purpose storage account change needed to create the general-purpose account type that supports current storage services. Which storage hardening operation belongs in the runbook?

- **A — Correct.** Create a standard StorageV2 account unless a workload-specific account kind is required.
  Create a standard StorageV2 account unless a workload-specific account kind is required. In hardened general-purpose storage account, applying StorageV2 accounts is the scoped way to create the general-purpose account type that supports current storage services.
- **B — Incorrect.** Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required.
  Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. In the hardened general-purpose storage account, this action changes locally redundant storage. Hardened general-purpose storage account requires StorageV2 accounts; changing locally redundant storage leaves StorageV2 accounts absent in hardened general-purpose storage account; hardened general-purpose storage account cannot create the general-purpose account type that supports current storage services.
- **C — Incorrect.** Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists.
  Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. In the hardened general-purpose storage account, this action changes secure transfer required. Secure transfer required does not implement StorageV2 accounts for hardened general-purpose storage account; the hardened general-purpose storage account still cannot create the general-purpose account type that supports current storage services.
- **D — Incorrect.** Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation.
  Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. In the hardened general-purpose storage account, this action changes access-key rotation. Hardened general-purpose storage account instead needs StorageV2 accounts: Create a standard StorageV2 account unless a workload-specific account kind is required. The access-key rotation action omits that StorageV2 accounts work.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q12 — D

**Question:** A hardened general-purpose storage account review finds storage hardening drift from the need to produce a globally unique lowercase account name with no punctuation. Which correction addresses that drift?

- **A — Incorrect.** Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication.
  Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. In the hardened general-purpose storage account, this action changes zone-redundant storage. Hardened general-purpose storage account requires storage account naming; changing zone-redundant storage leaves storage account naming absent in hardened general-purpose storage account; hardened general-purpose storage account cannot produce a globally unique lowercase account name with no punctuation.
- **B — Incorrect.** Set minimumTlsVersion to TLS1_2 or the approved stronger baseline.
  Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. In the hardened general-purpose storage account, this action changes minimum TLS version. Minimum TLS version does not implement storage account naming for hardened general-purpose storage account; the hardened general-purpose storage account still cannot produce a globally unique lowercase account name with no punctuation.
- **C — Incorrect.** Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key.
  Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. In the hardened general-purpose storage account, this action changes storage service encryption. Hardened general-purpose storage account instead needs storage account naming: Generate a deterministic lowercase name and check global availability before deployment. The storage service encryption action omits that storage account naming work.
- **D — Correct.** Generate a deterministic lowercase name and check global availability before deployment.
  Generate a deterministic lowercase name and check global availability before deployment. The hardened general-purpose storage account uses this storage account naming operation to produce a globally unique lowercase account name with no punctuation within the approved scope.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q13 — D

**Question:** The hardened general-purpose storage account window permits only the storage hardening change needed to replicate data synchronously three ways at a single site. Which option respects the boundary?

- **A — Incorrect.** Choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
  Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. In the hardened general-purpose storage account, this action changes geo-redundant read access. Geo-redundant read access does not implement locally redundant storage for hardened general-purpose storage account; the hardened general-purpose storage account still cannot replicate data synchronously three ways at a single site.
- **B — Incorrect.** Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization.
  Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. In the hardened general-purpose storage account, this action changes shared key authorization. Hardened general-purpose storage account instead needs locally redundant storage: Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. The shared key authorization action omits that locally redundant storage work.
- **C — Incorrect.** Create a standard StorageV2 account unless a workload-specific account kind is required.
  Create a standard StorageV2 account unless a workload-specific account kind is required. In the hardened general-purpose storage account, this action changes StorageV2 accounts. Hardened general-purpose storage account approved locally redundant storage, not StorageV2 accounts; only the locally redundant storage change can replicate data synchronously three ways at a single site.
- **D — Correct.** Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required.
  For the hardened general-purpose storage account, the required locally redundant storage action is: choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. It makes the environment able to replicate data synchronously three ways at a single site.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q14 — D

**Question:** The storage hardening preflight has passed; the hardened general-purpose storage account must now survive a single availability-zone failure within the primary region. Which operation should run?

- **A — Incorrect.** Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists.
  Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. In the hardened general-purpose storage account, this action changes secure transfer required. Hardened general-purpose storage account instead needs zone-redundant storage: Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. The secure transfer required action omits that zone-redundant storage work.
- **B — Incorrect.** Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation.
  Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. In the hardened general-purpose storage account, this action changes access-key rotation. Hardened general-purpose storage account approved zone-redundant storage, not access-key rotation; only the zone-redundant storage change can survive a single availability-zone failure within the primary region.
- **C — Incorrect.** Generate a deterministic lowercase name and check global availability before deployment.
  Generate a deterministic lowercase name and check global availability before deployment. In the hardened general-purpose storage account, this action changes storage account naming. Hardened general-purpose storage account requires zone-redundant storage; changing storage account naming leaves zone-redundant storage absent in hardened general-purpose storage account; hardened general-purpose storage account cannot survive a single availability-zone failure within the primary region.
- **D — Correct.** Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication.
  Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. This changes zone-redundant storage in the hardened general-purpose storage account, supplying the missing state needed to survive a single availability-zone failure within the primary region.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q15 — C

**Question:** The hardened general-purpose storage account plan must allow reads from the secondary region when geo-replicated data is available while limiting the mutation scope to storage hardening. Which action is appropriate?

- **A — Incorrect.** Set minimumTlsVersion to TLS1_2 or the approved stronger baseline.
  Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. In the hardened general-purpose storage account, this action changes minimum TLS version. Hardened general-purpose storage account approved geo-redundant read access, not minimum TLS version; only the geo-redundant read access change can allow reads from the secondary region when geo-replicated data is available.
- **B — Incorrect.** Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key.
  Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. In the hardened general-purpose storage account, this action changes storage service encryption. Hardened general-purpose storage account requires geo-redundant read access; changing storage service encryption leaves geo-redundant read access absent in hardened general-purpose storage account; hardened general-purpose storage account cannot allow reads from the secondary region when geo-replicated data is available.
- **C — Correct.** Choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
  The hardened general-purpose storage account must allow reads from the secondary region when geo-replicated data is available; this option performs its direct geo-redundant read access change: choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
- **D — Incorrect.** Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required.
  Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. In the hardened general-purpose storage account, this action changes locally redundant storage. Hardened general-purpose storage account instead needs geo-redundant read access: Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. The locally redundant storage action omits that geo-redundant read access work.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q16 — C

**Question:** A storage hardening ticket in the hardened general-purpose storage account says to reject storage requests that do not use an encrypted transport. Which storage hardening action completes the hardened general-purpose storage account request with minimal change?

- **A — Incorrect.** Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization.
  Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. In the hardened general-purpose storage account, this action changes shared key authorization. Hardened general-purpose storage account requires secure transfer required; changing shared key authorization leaves secure transfer required absent in hardened general-purpose storage account; hardened general-purpose storage account cannot reject storage requests that do not use an encrypted transport.
- **B — Incorrect.** Create a standard StorageV2 account unless a workload-specific account kind is required.
  Create a standard StorageV2 account unless a workload-specific account kind is required. In the hardened general-purpose storage account, this action changes StorageV2 accounts. StorageV2 accounts does not implement secure transfer required for hardened general-purpose storage account; the hardened general-purpose storage account still cannot reject storage requests that do not use an encrypted transport.
- **C — Correct.** Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists.
  Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. It is the least-change secure transfer required path for the hardened general-purpose storage account requirement to reject storage requests that do not use an encrypted transport.
- **D — Incorrect.** Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication.
  Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. In the hardened general-purpose storage account, this action changes zone-redundant storage. Hardened general-purpose storage account approved secure transfer required, not zone-redundant storage; only the secure transfer required change can reject storage requests that do not use an encrypted transport.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Require secure transfer for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer)

**Source reviewed:** 2026-08-31

## LAB06-Q17 — D

**Question:** The approach for the hardened general-purpose storage account is approved, but the storage hardening environment still cannot refuse clients that negotiate an obsolete transport protocol. Which implementation step closes the gap?

- **A — Incorrect.** Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation.
  Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. In the hardened general-purpose storage account, this action changes access-key rotation. Access-key rotation does not implement minimum TLS version for hardened general-purpose storage account; the hardened general-purpose storage account still cannot refuse clients that negotiate an obsolete transport protocol.
- **B — Incorrect.** Generate a deterministic lowercase name and check global availability before deployment.
  Generate a deterministic lowercase name and check global availability before deployment. In the hardened general-purpose storage account, this action changes storage account naming. Hardened general-purpose storage account instead needs minimum TLS version: Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. The storage account naming action omits that minimum TLS version work.
- **C — Incorrect.** Choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
  Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. In the hardened general-purpose storage account, this action changes geo-redundant read access. Hardened general-purpose storage account approved minimum TLS version, not geo-redundant read access; only the minimum TLS version change can refuse clients that negotiate an obsolete transport protocol.
- **D — Correct.** Set minimumTlsVersion to TLS1_2 or the approved stronger baseline.
  Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. In hardened general-purpose storage account, applying minimum TLS version is the scoped way to refuse clients that negotiate an obsolete transport protocol.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Configure a minimum TLS version for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/transport-layer-security-configure-minimum-version)

**Source reviewed:** 2026-08-31

## LAB06-Q18 — C

**Question:** The storage administrator hardening a general-purpose account may change the hardened general-purpose storage account only to accept only Microsoft Entra credentials for data access. Which storage hardening action stays within that assignment?

- **A — Incorrect.** Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key.
  Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. In the hardened general-purpose storage account, this action changes storage service encryption. Hardened general-purpose storage account instead needs shared key authorization: Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. The storage service encryption action omits that shared key authorization work.
- **B — Incorrect.** Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required.
  Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. In the hardened general-purpose storage account, this action changes locally redundant storage. Hardened general-purpose storage account approved shared key authorization, not locally redundant storage; only the shared key authorization change can accept only Microsoft Entra credentials for data access.
- **C — Correct.** Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization.
  Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. The hardened general-purpose storage account uses this shared key authorization operation to accept only Microsoft Entra credentials for data access within the approved scope.
- **D — Incorrect.** Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists.
  Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. In the hardened general-purpose storage account, this action changes secure transfer required. Secure transfer required does not implement shared key authorization for hardened general-purpose storage account; the hardened general-purpose storage account still cannot accept only Microsoft Entra credentials for data access.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB06-Q19 — A

**Question:** A storage hardening dry run shows no hardened general-purpose storage account command will replace a compromised credential without losing the second recovery credential. Which action belongs before execution?

- **A — Correct.** Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation.
  For the hardened general-purpose storage account, the required access-key rotation action is: move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. It makes the environment able to replace a compromised credential without losing the second recovery credential.
- **B — Incorrect.** Create a standard StorageV2 account unless a workload-specific account kind is required.
  Create a standard StorageV2 account unless a workload-specific account kind is required. In the hardened general-purpose storage account, this action changes StorageV2 accounts. Hardened general-purpose storage account requires access-key rotation; changing StorageV2 accounts leaves access-key rotation absent in hardened general-purpose storage account; hardened general-purpose storage account cannot replace a compromised credential without losing the second recovery credential.
- **C — Incorrect.** Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication.
  Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. In the hardened general-purpose storage account, this action changes zone-redundant storage. Zone-redundant storage does not implement access-key rotation for hardened general-purpose storage account; the hardened general-purpose storage account still cannot replace a compromised credential without losing the second recovery credential.
- **D — Incorrect.** Set minimumTlsVersion to TLS1_2 or the approved stronger baseline.
  Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. In the hardened general-purpose storage account, this action changes minimum TLS version. Hardened general-purpose storage account instead needs access-key rotation: Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. The minimum TLS version action omits that access-key rotation work.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Manage Azure Storage account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)

**Source reviewed:** 2026-08-31

## LAB06-Q20 — C

**Question:** For the hardened general-purpose storage account, operators need to confirm that stored service data is encrypted without an application change. Which change realizes that requirement?

- **A — Incorrect.** Generate a deterministic lowercase name and check global availability before deployment.
  Generate a deterministic lowercase name and check global availability before deployment. In the hardened general-purpose storage account, this action changes storage account naming. Hardened general-purpose storage account requires storage service encryption; changing storage account naming leaves storage service encryption absent in hardened general-purpose storage account; hardened general-purpose storage account cannot confirm that stored service data is encrypted without an application change.
- **B — Incorrect.** Choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
  Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. In the hardened general-purpose storage account, this action changes geo-redundant read access. Geo-redundant read access does not implement storage service encryption for hardened general-purpose storage account; the hardened general-purpose storage account still cannot confirm that stored service data is encrypted without an application change.
- **C — Correct.** Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key.
  Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. This changes storage service encryption in the hardened general-purpose storage account, supplying the missing state needed to confirm that stored service data is encrypted without an application change.
- **D — Incorrect.** Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization.
  Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. In the hardened general-purpose storage account, this action changes shared key authorization. Hardened general-purpose storage account approved storage service encryption, not shared key authorization; only the storage service encryption change can confirm that stored service data is encrypted without an application change.

**Objectives:** `ST-ACCOUNTS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage encryption for data at rest](https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption)

**Source reviewed:** 2026-08-31

## LAB06-Q21 — A

**Question:** The hardened general-purpose storage account configuration is complete; the storage hardening reviewers need evidence it can create the general-purpose account type that supports current storage services. Which observation shows success?

- **A — Correct.** Query kind, sku, primaryEndpoints, and provisioningState for the created account.
  The hardened general-purpose storage account validator needs this StorageV2 accounts result: query kind, sku, primaryEndpoints, and provisioningState for the created account. It proves the outcome to create the general-purpose account type that supports current storage services rather than an adjacent checkpoint.
- **B — Incorrect.** Query the account SKU and verify Standard_ZRS is supported in the selected region.
  Query the account SKU and verify Standard_ZRS is supported in the selected region. In the hardened general-purpose storage account, this check observes zone-redundant storage. Zone-redundant storage success in hardened general-purpose storage account cannot verify StorageV2 accounts; hardened general-purpose storage account cannot create the general-purpose account type that supports current storage services until StorageV2 accounts evidence exists.
- **C — Incorrect.** Query minimumTlsVersion and compare it with the security standard.
  Query minimumTlsVersion and compare it with the security standard. In the hardened general-purpose storage account, this check observes minimum TLS version. Hardened general-purpose storage account reads minimum TLS version, leaving StorageV2 accounts unproved in hardened general-purpose storage account; hardened general-purpose storage account still has no StorageV2 accounts proof.
- **D — Incorrect.** Query encryption keySource and service encryption settings for Blob and Files.
  Query encryption keySource and service encryption settings for Blob and Files. In the hardened general-purpose storage account, this check observes storage service encryption. Hardened general-purpose storage account could pass storage service encryption while StorageV2 accounts is wrong; hardened general-purpose storage account still lacks StorageV2 accounts proof.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q22 — A

**Question:** The storage hardening validation asks whether the hardened general-purpose storage account can produce a globally unique lowercase account name with no punctuation. Which observable state is strongest?

- **A — Correct.** Use the name-availability API and confirm nameAvailable is true before creation.
  Use the name-availability API and confirm nameAvailable is true before creation. This is independent storage account naming evidence for the hardened general-purpose storage account, even if hardened general-purpose storage account setup reports success before storage account naming becomes observable.
- **B — Incorrect.** Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
  Query secondary endpoints and the account SKU to confirm read-access geo-redundancy. In the hardened general-purpose storage account, this check observes geo-redundant read access. Hardened general-purpose storage account reads geo-redundant read access, leaving storage account naming unproved in hardened general-purpose storage account; hardened general-purpose storage account still has no storage account naming proof.
- **C — Incorrect.** Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
  Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently. In the hardened general-purpose storage account, this check observes shared key authorization. Hardened general-purpose storage account could pass shared key authorization while storage account naming is wrong; hardened general-purpose storage account still lacks storage account naming proof.
- **D — Incorrect.** Query kind, sku, primaryEndpoints, and provisioningState for the created account.
  Query kind, sku, primaryEndpoints, and provisioningState for the created account. In the hardened general-purpose storage account, this check observes StorageV2 accounts. Hardened general-purpose storage account output covers StorageV2 accounts, not storage account naming; the storage account naming requirement to produce a globally unique lowercase account name with no punctuation remains unverified.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q23 — B

**Question:** A hardened general-purpose storage account review must prove the storage hardening ability to replicate data synchronously three ways at a single site. Which check avoids an adjacent feature?

- **A — Incorrect.** Query enableHttpsTrafficOnly and confirm it is true.
  Query enableHttpsTrafficOnly and confirm it is true. In the hardened general-purpose storage account, this check observes secure transfer required. Hardened general-purpose storage account reads secure transfer required, leaving locally redundant storage unproved in hardened general-purpose storage account; hardened general-purpose storage account still has no locally redundant storage proof.
- **B — Correct.** Query the account SKU and confirm its name is Standard_LRS.
  Query the account SKU and confirm its name is Standard_LRS. For hardened general-purpose storage account, this locally redundant storage read confirms the service can replicate data synchronously three ways at a single site.
- **C — Incorrect.** List key creation times and verify applications no longer use the key scheduled for regeneration.
  List key creation times and verify applications no longer use the key scheduled for regeneration. In the hardened general-purpose storage account, this check observes access-key rotation. Hardened general-purpose storage account output covers access-key rotation, not locally redundant storage; the locally redundant storage requirement to replicate data synchronously three ways at a single site remains unverified.
- **D — Incorrect.** Use the name-availability API and confirm nameAvailable is true before creation.
  Use the name-availability API and confirm nameAvailable is true before creation. In the hardened general-purpose storage account, this check observes storage account naming. Storage account naming success in hardened general-purpose storage account cannot verify locally redundant storage; hardened general-purpose storage account cannot replicate data synchronously three ways at a single site until locally redundant storage evidence exists.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q24 — A

**Question:** The hardened general-purpose storage account evidence bundle needs a storage hardening result showing it can survive a single availability-zone failure within the primary region. Which result belongs in the checkpoint?

- **A — Correct.** Query the account SKU and verify Standard_ZRS is supported in the selected region.
  Query the account SKU and verify Standard_ZRS is supported in the selected region. The hardened general-purpose storage account reads zone-redundant storage directly; that zone-redundant storage result proves the hardened general-purpose storage account can survive a single availability-zone failure within the primary region without another mutation.
- **B — Incorrect.** Query minimumTlsVersion and compare it with the security standard.
  Query minimumTlsVersion and compare it with the security standard. In the hardened general-purpose storage account, this check observes minimum TLS version. Hardened general-purpose storage account output covers minimum TLS version, not zone-redundant storage; the zone-redundant storage requirement to survive a single availability-zone failure within the primary region remains unverified.
- **C — Incorrect.** Query encryption keySource and service encryption settings for Blob and Files.
  Query encryption keySource and service encryption settings for Blob and Files. In the hardened general-purpose storage account, this check observes storage service encryption. Storage service encryption success in hardened general-purpose storage account cannot verify zone-redundant storage; hardened general-purpose storage account cannot survive a single availability-zone failure within the primary region until zone-redundant storage evidence exists.
- **D — Incorrect.** Query the account SKU and confirm its name is Standard_LRS.
  Query the account SKU and confirm its name is Standard_LRS. In the hardened general-purpose storage account, this check observes locally redundant storage. Hardened general-purpose storage account reads locally redundant storage, leaving zone-redundant storage unproved in hardened general-purpose storage account; hardened general-purpose storage account still has no zone-redundant storage proof.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q25 — C

**Question:** Before hardened general-purpose storage account cleanup, the storage hardening team must reconfirm it can allow reads from the secondary region when geo-replicated data is available. Which read-only inspection should run?

- **A — Incorrect.** Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
  Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently. In the hardened general-purpose storage account, this check observes shared key authorization. Hardened general-purpose storage account output covers shared key authorization, not geo-redundant read access; the geo-redundant read access requirement to allow reads from the secondary region when geo-replicated data is available remains unverified.
- **B — Incorrect.** Query kind, sku, primaryEndpoints, and provisioningState for the created account.
  Query kind, sku, primaryEndpoints, and provisioningState for the created account. In the hardened general-purpose storage account, this check observes StorageV2 accounts. StorageV2 accounts success in hardened general-purpose storage account cannot verify geo-redundant read access; hardened general-purpose storage account cannot allow reads from the secondary region when geo-replicated data is available until geo-redundant read access evidence exists.
- **C — Correct.** Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
  For the hardened general-purpose storage account, this geo-redundant read access observation is decisive: query secondary endpoints and the account SKU to confirm read-access geo-redundancy. It is hardened general-purpose storage account evidence that operators can allow reads from the secondary region when geo-replicated data is available.
- **D — Incorrect.** Query the account SKU and verify Standard_ZRS is supported in the selected region.
  Query the account SKU and verify Standard_ZRS is supported in the selected region. In the hardened general-purpose storage account, this check observes zone-redundant storage. Hardened general-purpose storage account could pass zone-redundant storage while geo-redundant read access is wrong; hardened general-purpose storage account still lacks geo-redundant read access proof.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q26 — D

**Question:** The hardened general-purpose storage account setup reports success after the storage hardening attempt to reject storage requests that do not use an encrypted transport. Which storage hardening read-only observation proves the hardened general-purpose storage account outcome?

- **A — Incorrect.** List key creation times and verify applications no longer use the key scheduled for regeneration.
  List key creation times and verify applications no longer use the key scheduled for regeneration. In the hardened general-purpose storage account, this check observes access-key rotation. Access-key rotation success in hardened general-purpose storage account cannot verify secure transfer required; hardened general-purpose storage account cannot reject storage requests that do not use an encrypted transport until secure transfer required evidence exists.
- **B — Incorrect.** Use the name-availability API and confirm nameAvailable is true before creation.
  Use the name-availability API and confirm nameAvailable is true before creation. In the hardened general-purpose storage account, this check observes storage account naming. Hardened general-purpose storage account reads storage account naming, leaving secure transfer required unproved in hardened general-purpose storage account; hardened general-purpose storage account still has no secure transfer required proof.
- **C — Incorrect.** Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
  Query secondary endpoints and the account SKU to confirm read-access geo-redundancy. In the hardened general-purpose storage account, this check observes geo-redundant read access. Hardened general-purpose storage account could pass geo-redundant read access while secure transfer required is wrong; hardened general-purpose storage account still lacks secure transfer required proof.
- **D — Correct.** Query enableHttpsTrafficOnly and confirm it is true.
  Query enableHttpsTrafficOnly and confirm it is true. Because the hardened general-purpose storage account check observes secure transfer required, it independently verifies the requirement to reject storage requests that do not use an encrypted transport.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Require secure transfer for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer)

**Source reviewed:** 2026-08-31

## LAB06-Q27 — C

**Question:** The storage hardening log says the hardened general-purpose storage account can now refuse clients that negotiate an obsolete transport protocol. Which storage hardening state should the hardened general-purpose storage account acceptance test retain?

- **A — Incorrect.** Query encryption keySource and service encryption settings for Blob and Files.
  Query encryption keySource and service encryption settings for Blob and Files. In the hardened general-purpose storage account, this check observes storage service encryption. Hardened general-purpose storage account reads storage service encryption, leaving minimum TLS version unproved in hardened general-purpose storage account; hardened general-purpose storage account still has no minimum TLS version proof.
- **B — Incorrect.** Query the account SKU and confirm its name is Standard_LRS.
  Query the account SKU and confirm its name is Standard_LRS. In the hardened general-purpose storage account, this check observes locally redundant storage. Hardened general-purpose storage account could pass locally redundant storage while minimum TLS version is wrong; hardened general-purpose storage account still lacks minimum TLS version proof.
- **C — Correct.** Query minimumTlsVersion and compare it with the security standard.
  The hardened general-purpose storage account validator needs this minimum TLS version result: query minimumTlsVersion and compare it with the security standard. It proves the outcome to refuse clients that negotiate an obsolete transport protocol rather than an adjacent checkpoint.
- **D — Incorrect.** Query enableHttpsTrafficOnly and confirm it is true.
  Query enableHttpsTrafficOnly and confirm it is true. In the hardened general-purpose storage account, this check observes secure transfer required. Secure transfer required success in hardened general-purpose storage account cannot verify minimum TLS version; hardened general-purpose storage account cannot refuse clients that negotiate an obsolete transport protocol until minimum TLS version evidence exists.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Configure a minimum TLS version for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/transport-layer-security-configure-minimum-version)

**Source reviewed:** 2026-08-31

## LAB06-Q28 — C

**Question:** The hardened general-purpose storage account rejects storage hardening exit status as proof it can accept only Microsoft Entra credentials for data access. Which hardened general-purpose storage account result is valid evidence?

- **A — Incorrect.** Query kind, sku, primaryEndpoints, and provisioningState for the created account.
  Query kind, sku, primaryEndpoints, and provisioningState for the created account. In the hardened general-purpose storage account, this check observes StorageV2 accounts. Hardened general-purpose storage account could pass StorageV2 accounts while shared key authorization is wrong; hardened general-purpose storage account still lacks shared key authorization proof.
- **B — Incorrect.** Query the account SKU and verify Standard_ZRS is supported in the selected region.
  Query the account SKU and verify Standard_ZRS is supported in the selected region. In the hardened general-purpose storage account, this check observes zone-redundant storage. Hardened general-purpose storage account output covers zone-redundant storage, not shared key authorization; the shared key authorization requirement to accept only Microsoft Entra credentials for data access remains unverified.
- **C — Correct.** Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
  Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently. This is independent shared key authorization evidence for the hardened general-purpose storage account, even if hardened general-purpose storage account setup reports success before shared key authorization becomes observable.
- **D — Incorrect.** Query minimumTlsVersion and compare it with the security standard.
  Query minimumTlsVersion and compare it with the security standard. In the hardened general-purpose storage account, this check observes minimum TLS version. Hardened general-purpose storage account reads minimum TLS version, leaving shared key authorization unproved in hardened general-purpose storage account; hardened general-purpose storage account still has no shared key authorization proof.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB06-Q29 — D

**Question:** The storage hardening validator needs one hardened general-purpose storage account query after the change to replace a compromised credential without losing the second recovery credential. Which storage hardening property should the hardened general-purpose storage account validator inspect?

- **A — Incorrect.** Use the name-availability API and confirm nameAvailable is true before creation.
  Use the name-availability API and confirm nameAvailable is true before creation. In the hardened general-purpose storage account, this check observes storage account naming. Hardened general-purpose storage account output covers storage account naming, not access-key rotation; the access-key rotation requirement to replace a compromised credential without losing the second recovery credential remains unverified.
- **B — Incorrect.** Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
  Query secondary endpoints and the account SKU to confirm read-access geo-redundancy. In the hardened general-purpose storage account, this check observes geo-redundant read access. Geo-redundant read access success in hardened general-purpose storage account cannot verify access-key rotation; hardened general-purpose storage account cannot replace a compromised credential without losing the second recovery credential until access-key rotation evidence exists.
- **C — Incorrect.** Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
  Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently. In the hardened general-purpose storage account, this check observes shared key authorization. Hardened general-purpose storage account reads shared key authorization, leaving access-key rotation unproved in hardened general-purpose storage account; hardened general-purpose storage account still has no access-key rotation proof.
- **D — Correct.** List key creation times and verify applications no longer use the key scheduled for regeneration.
  List key creation times and verify applications no longer use the key scheduled for regeneration. For hardened general-purpose storage account, this access-key rotation read confirms the service can replace a compromised credential without losing the second recovery credential.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Manage Azure Storage account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)

**Source reviewed:** 2026-08-31

## LAB06-Q30 — B

**Question:** The storage administrator hardening a general-purpose account must confirm the hardened general-purpose storage account, without mutation, can confirm that stored service data is encrypted without an application change. Which storage hardening check qualifies?

- **A — Incorrect.** Query the account SKU and confirm its name is Standard_LRS.
  Query the account SKU and confirm its name is Standard_LRS. In the hardened general-purpose storage account, this check observes locally redundant storage. Locally redundant storage success in hardened general-purpose storage account cannot verify storage service encryption; hardened general-purpose storage account cannot confirm that stored service data is encrypted without an application change until storage service encryption evidence exists.
- **B — Correct.** Query encryption keySource and service encryption settings for Blob and Files.
  Query encryption keySource and service encryption settings for Blob and Files. The hardened general-purpose storage account reads storage service encryption directly; that storage service encryption result proves the hardened general-purpose storage account can confirm that stored service data is encrypted without an application change without another mutation.
- **C — Incorrect.** Query enableHttpsTrafficOnly and confirm it is true.
  Query enableHttpsTrafficOnly and confirm it is true. In the hardened general-purpose storage account, this check observes secure transfer required. Hardened general-purpose storage account could pass secure transfer required while storage service encryption is wrong; hardened general-purpose storage account still lacks storage service encryption proof.
- **D — Incorrect.** List key creation times and verify applications no longer use the key scheduled for regeneration.
  List key creation times and verify applications no longer use the key scheduled for regeneration. In the hardened general-purpose storage account, this check observes access-key rotation. Hardened general-purpose storage account output covers access-key rotation, not storage service encryption; the storage service encryption requirement to confirm that stored service data is encrypted without an application change remains unverified.

**Objectives:** `ST-ACCOUNTS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage encryption for data at rest](https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption)

**Source reviewed:** 2026-08-31

## LAB06-Q31 — A

**Question:** The storage hardening evidence shows the hardened general-purpose storage account cannot create the general-purpose account type that supports current storage services. Which root cause fits that evidence?

- **A — Correct.** The account uses a legacy kind that does not support the requested modern storage capability.
  For the hardened general-purpose storage account, the StorageV2 accounts failure is causal: the account uses a legacy kind that does not support the requested modern storage capability. Correcting it restores the ability to create the general-purpose account type that supports current storage services.
- **B — Incorrect.** The proposed account name contains a hyphen and therefore violates the naming rules.
  The proposed account name contains a hyphen and therefore violates the naming rules. The hardened general-purpose storage account fault concerns storage account naming. Hardened general-purpose storage account could repair storage account naming while StorageV2 accounts stays broken in hardened general-purpose storage account; the hardened general-purpose storage account remains unable to create the general-purpose account type that supports current storage services.
- **C — Incorrect.** Secure transfer was disabled to accommodate an obsolete HTTP client.
  Secure transfer was disabled to accommodate an obsolete HTTP client. The hardened general-purpose storage account fault concerns secure transfer required. Hardened general-purpose storage account failed on StorageV2 accounts; this secure transfer required finding redirects hardened general-purpose storage account remediation away from StorageV2 accounts.
- **D — Incorrect.** Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions.
  Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions. The hardened general-purpose storage account fault concerns storage service encryption. Hardened general-purpose storage account may fix storage service encryption, yet StorageV2 accounts still fails; this hardened general-purpose storage account diagnosis of storage service encryption is wrong for StorageV2 accounts.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q32 — A

**Question:** Although the hardened general-purpose storage account is meant to let the storage hardening produce a globally unique lowercase account name with no punctuation, its checkpoint fails. Which storage hardening defect explains the failure?

- **A — Correct.** The proposed account name contains a hyphen and therefore violates the naming rules.
  The proposed account name contains a hyphen and therefore violates the naming rules. The finding is specific to storage account naming in the hardened general-purpose storage account; repairing storage account naming restores the hardened general-purpose storage account ability to produce a globally unique lowercase account name with no punctuation.
- **B — Incorrect.** The design requires zone-level resilience that LRS does not provide.
  The design requires zone-level resilience that LRS does not provide. The hardened general-purpose storage account fault concerns locally redundant storage. Hardened general-purpose storage account failed on storage account naming; this locally redundant storage finding redirects hardened general-purpose storage account remediation away from storage account naming.
- **C — Incorrect.** The client only supports a TLS version lower than the account's configured minimum.
  The client only supports a TLS version lower than the account's configured minimum. The hardened general-purpose storage account fault concerns minimum TLS version. Hardened general-purpose storage account may fix minimum TLS version, yet storage account naming still fails; this hardened general-purpose storage account diagnosis of minimum TLS version is wrong for storage account naming.
- **D — Incorrect.** The account uses a legacy kind that does not support the requested modern storage capability.
  The account uses a legacy kind that does not support the requested modern storage capability. The hardened general-purpose storage account fault concerns StorageV2 accounts. Hardened general-purpose storage account has StorageV2 accounts impact, but storage account naming is the hardened general-purpose storage account failed path; the StorageV2 accounts state cannot produce storage account naming failure.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q33 — D

**Question:** The storage hardening support team isolated the hardened general-purpose storage account incident to the attempt to replicate data synchronously three ways at a single site. Which condition prevents success?

- **A — Incorrect.** The selected region or account feature does not support the requested ZRS combination.
  The selected region or account feature does not support the requested ZRS combination. The hardened general-purpose storage account fault concerns zone-redundant storage. Hardened general-purpose storage account failed on locally redundant storage; this zone-redundant storage finding redirects hardened general-purpose storage account remediation away from locally redundant storage.
- **B — Incorrect.** The workload still depends on an account key after shared-key authorization was disabled.
  The workload still depends on an account key after shared-key authorization was disabled. The hardened general-purpose storage account fault concerns shared key authorization. Hardened general-purpose storage account may fix shared key authorization, yet locally redundant storage still fails; this hardened general-purpose storage account diagnosis of shared key authorization is wrong for locally redundant storage.
- **C — Incorrect.** The proposed account name contains a hyphen and therefore violates the naming rules.
  The proposed account name contains a hyphen and therefore violates the naming rules. The hardened general-purpose storage account fault concerns storage account naming. Hardened general-purpose storage account has storage account naming impact, but locally redundant storage is the hardened general-purpose storage account failed path; the storage account naming state cannot produce locally redundant storage failure.
- **D — Correct.** The design requires zone-level resilience that LRS does not provide.
  The hardened general-purpose storage account cannot replicate data synchronously three ways at a single site because of this locally redundant storage defect: the design requires zone-level resilience that LRS does not provide. The symptom and repair align.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q34 — A

**Question:** A hardened general-purpose storage account query surprises the storage administrator hardening a general-purpose account during the storage hardening attempt to survive a single availability-zone failure within the primary region. Which finding explains it?

- **A — Correct.** The selected region or account feature does not support the requested ZRS combination.
  The selected region or account feature does not support the requested ZRS combination. Removing this zone-redundant storage condition lets the hardened general-purpose storage account survive a single availability-zone failure within the primary region while leaving healthy controls unchanged.
- **B — Incorrect.** The account uses GRS, so applications cannot normally read from the secondary endpoint.
  The account uses GRS, so applications cannot normally read from the secondary endpoint. The hardened general-purpose storage account fault concerns geo-redundant read access. Hardened general-purpose storage account has geo-redundant read access impact, but zone-redundant storage is the hardened general-purpose storage account failed path; the geo-redundant read access state cannot produce zone-redundant storage failure.
- **C — Incorrect.** The active key was regenerated before dependent applications switched to the alternate key.
  The active key was regenerated before dependent applications switched to the alternate key. The hardened general-purpose storage account fault concerns access-key rotation. Hardened general-purpose storage account could repair access-key rotation while zone-redundant storage stays broken in hardened general-purpose storage account; the hardened general-purpose storage account remains unable to survive a single availability-zone failure within the primary region.
- **D — Incorrect.** The design requires zone-level resilience that LRS does not provide.
  The design requires zone-level resilience that LRS does not provide. The hardened general-purpose storage account fault concerns locally redundant storage. Hardened general-purpose storage account failed on zone-redundant storage; this locally redundant storage finding redirects hardened general-purpose storage account remediation away from zone-redundant storage.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q35 — A

**Question:** Other hardened general-purpose storage account components are healthy, but the storage hardening still cannot allow reads from the secondary region when geo-replicated data is available. Which state causes the isolated failure?

- **A — Correct.** The account uses GRS, so applications cannot normally read from the secondary endpoint.
  The account uses GRS, so applications cannot normally read from the secondary endpoint. In hardened general-purpose storage account, this geo-redundant read access cause matches the failure to allow reads from the secondary region when geo-replicated data is available.
- **B — Incorrect.** Secure transfer was disabled to accommodate an obsolete HTTP client.
  Secure transfer was disabled to accommodate an obsolete HTTP client. The hardened general-purpose storage account fault concerns secure transfer required. Hardened general-purpose storage account could repair secure transfer required while geo-redundant read access stays broken in hardened general-purpose storage account; the hardened general-purpose storage account remains unable to allow reads from the secondary region when geo-replicated data is available.
- **C — Incorrect.** Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions.
  Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions. The hardened general-purpose storage account fault concerns storage service encryption. Hardened general-purpose storage account failed on geo-redundant read access; this storage service encryption finding redirects hardened general-purpose storage account remediation away from geo-redundant read access.
- **D — Incorrect.** The selected region or account feature does not support the requested ZRS combination.
  The selected region or account feature does not support the requested ZRS combination. The hardened general-purpose storage account fault concerns zone-redundant storage. Hardened general-purpose storage account may fix zone-redundant storage, yet geo-redundant read access still fails; this hardened general-purpose storage account diagnosis of zone-redundant storage is wrong for geo-redundant read access.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q36 — D

**Question:** During a storage hardening fault drill, the hardened general-purpose storage account does not reject storage requests that do not use an encrypted transport. Which finding identifies the defect?

- **A — Incorrect.** The client only supports a TLS version lower than the account's configured minimum.
  The client only supports a TLS version lower than the account's configured minimum. The hardened general-purpose storage account fault concerns minimum TLS version. Hardened general-purpose storage account could repair minimum TLS version while secure transfer required stays broken in hardened general-purpose storage account; the hardened general-purpose storage account remains unable to reject storage requests that do not use an encrypted transport.
- **B — Incorrect.** The account uses a legacy kind that does not support the requested modern storage capability.
  The account uses a legacy kind that does not support the requested modern storage capability. The hardened general-purpose storage account fault concerns StorageV2 accounts. Hardened general-purpose storage account failed on secure transfer required; this StorageV2 accounts finding redirects hardened general-purpose storage account remediation away from secure transfer required.
- **C — Incorrect.** The account uses GRS, so applications cannot normally read from the secondary endpoint.
  The account uses GRS, so applications cannot normally read from the secondary endpoint. The hardened general-purpose storage account fault concerns geo-redundant read access. Hardened general-purpose storage account may fix geo-redundant read access, yet secure transfer required still fails; this hardened general-purpose storage account diagnosis of geo-redundant read access is wrong for secure transfer required.
- **D — Correct.** Secure transfer was disabled to accommodate an obsolete HTTP client.
  Secure transfer was disabled to accommodate an obsolete HTTP client. This hardened general-purpose storage account condition breaks secure transfer required, explaining why operators cannot reject storage requests that do not use an encrypted transport.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Require secure transfer for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer)

**Source reviewed:** 2026-08-31

## LAB06-Q37 — C

**Question:** The hardened general-purpose storage account setup finishes, yet the storage hardening cannot refuse clients that negotiate an obsolete transport protocol. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The workload still depends on an account key after shared-key authorization was disabled.
  The workload still depends on an account key after shared-key authorization was disabled. The hardened general-purpose storage account fault concerns shared key authorization. Hardened general-purpose storage account failed on minimum TLS version; this shared key authorization finding redirects hardened general-purpose storage account remediation away from minimum TLS version.
- **B — Incorrect.** The proposed account name contains a hyphen and therefore violates the naming rules.
  The proposed account name contains a hyphen and therefore violates the naming rules. The hardened general-purpose storage account fault concerns storage account naming. Hardened general-purpose storage account may fix storage account naming, yet minimum TLS version still fails; this hardened general-purpose storage account diagnosis of storage account naming is wrong for minimum TLS version.
- **C — Correct.** The client only supports a TLS version lower than the account's configured minimum.
  For the hardened general-purpose storage account, the minimum TLS version failure is causal: the client only supports a TLS version lower than the account's configured minimum. Correcting it restores the ability to refuse clients that negotiate an obsolete transport protocol.
- **D — Incorrect.** Secure transfer was disabled to accommodate an obsolete HTTP client.
  Secure transfer was disabled to accommodate an obsolete HTTP client. The hardened general-purpose storage account fault concerns secure transfer required. Hardened general-purpose storage account could repair secure transfer required while minimum TLS version stays broken in hardened general-purpose storage account; the hardened general-purpose storage account remains unable to refuse clients that negotiate an obsolete transport protocol.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Configure a minimum TLS version for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/transport-layer-security-configure-minimum-version)

**Source reviewed:** 2026-08-31

## LAB06-Q38 — B

**Question:** A storage hardening break/fix in the hardened general-purpose storage account fails when operators try to accept only Microsoft Entra credentials for data access. Which diagnosis fits?

- **A — Incorrect.** The active key was regenerated before dependent applications switched to the alternate key.
  The active key was regenerated before dependent applications switched to the alternate key. The hardened general-purpose storage account fault concerns access-key rotation. Hardened general-purpose storage account may fix access-key rotation, yet shared key authorization still fails; this hardened general-purpose storage account diagnosis of access-key rotation is wrong for shared key authorization.
- **B — Correct.** The workload still depends on an account key after shared-key authorization was disabled.
  The workload still depends on an account key after shared-key authorization was disabled. The finding is specific to shared key authorization in the hardened general-purpose storage account; repairing shared key authorization restores the hardened general-purpose storage account ability to accept only Microsoft Entra credentials for data access.
- **C — Incorrect.** The design requires zone-level resilience that LRS does not provide.
  The design requires zone-level resilience that LRS does not provide. The hardened general-purpose storage account fault concerns locally redundant storage. Hardened general-purpose storage account could repair locally redundant storage while shared key authorization stays broken in hardened general-purpose storage account; the hardened general-purpose storage account remains unable to accept only Microsoft Entra credentials for data access.
- **D — Incorrect.** The client only supports a TLS version lower than the account's configured minimum.
  The client only supports a TLS version lower than the account's configured minimum. The hardened general-purpose storage account fault concerns minimum TLS version. Hardened general-purpose storage account failed on shared key authorization; this minimum TLS version finding redirects hardened general-purpose storage account remediation away from shared key authorization.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB06-Q39 — A

**Question:** The hardened general-purpose storage account troubleshooting scope is the storage hardening need to replace a compromised credential without losing the second recovery credential. Which condition should be corrected first?

- **A — Correct.** The active key was regenerated before dependent applications switched to the alternate key.
  The hardened general-purpose storage account cannot replace a compromised credential without losing the second recovery credential because of this access-key rotation defect: the active key was regenerated before dependent applications switched to the alternate key. The symptom and repair align.
- **B — Incorrect.** Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions.
  Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions. The hardened general-purpose storage account fault concerns storage service encryption. Hardened general-purpose storage account could repair storage service encryption while access-key rotation stays broken in hardened general-purpose storage account; the hardened general-purpose storage account remains unable to replace a compromised credential without losing the second recovery credential.
- **C — Incorrect.** The selected region or account feature does not support the requested ZRS combination.
  The selected region or account feature does not support the requested ZRS combination. The hardened general-purpose storage account fault concerns zone-redundant storage. Hardened general-purpose storage account failed on access-key rotation; this zone-redundant storage finding redirects hardened general-purpose storage account remediation away from access-key rotation.
- **D — Incorrect.** The workload still depends on an account key after shared-key authorization was disabled.
  The workload still depends on an account key after shared-key authorization was disabled. The hardened general-purpose storage account fault concerns shared key authorization. Hardened general-purpose storage account may fix shared key authorization, yet access-key rotation still fails; this hardened general-purpose storage account diagnosis of shared key authorization is wrong for access-key rotation.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Manage Azure Storage account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)

**Source reviewed:** 2026-08-31

## LAB06-Q40 — B

**Question:** The hardened general-purpose storage account result is partial because the storage hardening cannot confirm that stored service data is encrypted without an application change. Which condition accounts for that result?

- **A — Incorrect.** The account uses a legacy kind that does not support the requested modern storage capability.
  The account uses a legacy kind that does not support the requested modern storage capability. The hardened general-purpose storage account fault concerns StorageV2 accounts. Hardened general-purpose storage account could repair StorageV2 accounts while storage service encryption stays broken in hardened general-purpose storage account; the hardened general-purpose storage account remains unable to confirm that stored service data is encrypted without an application change.
- **B — Correct.** Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions.
  Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions. Removing this storage service encryption condition lets the hardened general-purpose storage account confirm that stored service data is encrypted without an application change while leaving healthy controls unchanged.
- **C — Incorrect.** The account uses GRS, so applications cannot normally read from the secondary endpoint.
  The account uses GRS, so applications cannot normally read from the secondary endpoint. The hardened general-purpose storage account fault concerns geo-redundant read access. Hardened general-purpose storage account may fix geo-redundant read access, yet storage service encryption still fails; this hardened general-purpose storage account diagnosis of geo-redundant read access is wrong for storage service encryption.
- **D — Incorrect.** The active key was regenerated before dependent applications switched to the alternate key.
  The active key was regenerated before dependent applications switched to the alternate key. The hardened general-purpose storage account fault concerns access-key rotation. Hardened general-purpose storage account has access-key rotation impact, but storage service encryption is the hardened general-purpose storage account failed path; the access-key rotation state cannot produce storage service encryption failure.

**Objectives:** `ST-ACCOUNTS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage encryption for data at rest](https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption)

**Source reviewed:** 2026-08-31

## LAB06-Q41 — D

**Question:** At the hardened general-purpose storage account approval gate, operators must show that the storage hardening can create the general-purpose account type that supports current storage services. Which storage hardening configure-and-check pair is defensible?

- **A — Incorrect.** First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.
  First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS. This hardened general-purpose storage account pair serves locally redundant storage. Locally redundant storage cannot replace StorageV2 accounts in hardened general-purpose storage account. Use this StorageV2 accounts pair instead: First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.
- **B — Incorrect.** First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
  First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard. This hardened general-purpose storage account pair serves minimum TLS version. Hardened general-purpose storage account proves minimum TLS version, but StorageV2 accounts lacks implementation in hardened general-purpose storage account and StorageV2 accounts proof; the StorageV2 accounts outcome to create the general-purpose account type that supports current storage services remains open.
- **C — Incorrect.** First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
  First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently. This hardened general-purpose storage account pair serves shared key authorization. Hardened general-purpose storage account uses shared key authorization for both steps; StorageV2 accounts remains untouched in hardened general-purpose storage account, so its StorageV2 accounts gate to create the general-purpose account type that supports current storage services fails.
- **D — Correct.** First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.
  First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account. For hardened general-purpose storage account, the StorageV2 accounts operation precedes its StorageV2 accounts read-back check, allowing it to create the general-purpose account type that supports current storage services.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q42 — C

**Question:** The hardened general-purpose storage account forbids a partial storage hardening result. Operators must first produce a globally unique lowercase account name with no punctuation and afterward confirm the hardened general-purpose storage account outcome. Which storage hardening sequence is complete?

- **A — Incorrect.** First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region.
  First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region. This hardened general-purpose storage account pair serves zone-redundant storage. Hardened general-purpose storage account proves zone-redundant storage, but storage account naming lacks implementation in hardened general-purpose storage account and storage account naming proof; the storage account naming outcome to produce a globally unique lowercase account name with no punctuation remains open.
- **B — Incorrect.** First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
  First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently. This hardened general-purpose storage account pair serves shared key authorization. Hardened general-purpose storage account uses shared key authorization for both steps; storage account naming remains untouched in hardened general-purpose storage account, so its storage account naming gate to produce a globally unique lowercase account name with no punctuation fails.
- **C — Correct.** First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.
  First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation. In the hardened general-purpose storage account, the first storage account naming step runs; the hardened general-purpose storage account then reads storage account naming state to prove it can produce a globally unique lowercase account name with no punctuation.
- **D — Incorrect.** First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.
  First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration. This hardened general-purpose storage account pair serves access-key rotation. Access-key rotation cannot replace storage account naming in hardened general-purpose storage account. Use this storage account naming pair instead: First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

**Source reviewed:** 2026-08-31

## LAB06-Q43 — A

**Question:** Only the hardened general-purpose storage account change needed to replicate data synchronously three ways at a single site is allowed, and storage hardening proof is mandatory. Which pair fits?

- **A — Correct.** First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.
  For the hardened general-purpose storage account, the safe locally redundant storage order is: first, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS. The hardened general-purpose storage account records locally redundant storage proof after configuration.
- **B — Incorrect.** First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
  First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy. This hardened general-purpose storage account pair serves geo-redundant read access. Hardened general-purpose storage account closes geo-redundant read access, not locally redundant storage; without the locally redundant storage workflow, it cannot replicate data synchronously three ways at a single site.
- **C — Incorrect.** First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.
  First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration. This hardened general-purpose storage account pair serves access-key rotation. Access-key rotation cannot replace locally redundant storage in hardened general-purpose storage account. Use this locally redundant storage pair instead: First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.
- **D — Incorrect.** First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files.
  First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files. This hardened general-purpose storage account pair serves storage service encryption. Hardened general-purpose storage account proves storage service encryption, but locally redundant storage lacks implementation in hardened general-purpose storage account and locally redundant storage proof; the locally redundant storage outcome to replicate data synchronously three ways at a single site remains open.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q44 — B

**Question:** The hardened general-purpose storage account runbook separates storage hardening mutation from validation while it must survive a single availability-zone failure within the primary region. Which sequence proves it cleanly?

- **A — Incorrect.** First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.
  First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true. This hardened general-purpose storage account pair serves secure transfer required. Hardened general-purpose storage account closes secure transfer required, not zone-redundant storage; without the zone-redundant storage workflow, it cannot survive a single availability-zone failure within the primary region.
- **B — Correct.** First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region.
  First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region. The hardened general-purpose storage account uses its zone-redundant storage mutation gate and zone-redundant storage verification gate before it can survive a single availability-zone failure within the primary region.
- **C — Incorrect.** First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files.
  First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files. This hardened general-purpose storage account pair serves storage service encryption. Hardened general-purpose storage account proves storage service encryption, but zone-redundant storage lacks implementation in hardened general-purpose storage account and zone-redundant storage proof; the zone-redundant storage outcome to survive a single availability-zone failure within the primary region remains open.
- **D — Incorrect.** First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.
  First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account. This hardened general-purpose storage account pair serves StorageV2 accounts. Hardened general-purpose storage account uses StorageV2 accounts for both steps; zone-redundant storage remains untouched in hardened general-purpose storage account, so its zone-redundant storage gate to survive a single availability-zone failure within the primary region fails.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q45 — B

**Question:** The hardened general-purpose storage account checkpoint requires both this storage hardening outcome—allow reads from the secondary region when geo-replicated data is available—and a read-only hardened general-purpose storage account state check. Which storage hardening response is complete?

- **A — Incorrect.** First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
  First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard. This hardened general-purpose storage account pair serves minimum TLS version. Minimum TLS version cannot replace geo-redundant read access in hardened general-purpose storage account. Use this geo-redundant read access pair instead: First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
- **B — Correct.** First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
  The hardened general-purpose storage account gets a complete geo-redundant read access sequence here: first, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy. Read-back evidence follows the change.
- **C — Incorrect.** First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.
  First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account. This hardened general-purpose storage account pair serves StorageV2 accounts. Hardened general-purpose storage account uses StorageV2 accounts for both steps; geo-redundant read access remains untouched in hardened general-purpose storage account, so its geo-redundant read access gate to allow reads from the secondary region when geo-replicated data is available fails.
- **D — Incorrect.** First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.
  First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation. This hardened general-purpose storage account pair serves storage account naming. Hardened general-purpose storage account closes storage account naming, not geo-redundant read access; without the geo-redundant read access workflow, it cannot allow reads from the secondary region when geo-replicated data is available.

**Objectives:** `ST-ACCOUNTS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

**Source reviewed:** 2026-08-31

## LAB06-Q46 — A

**Question:** The hardened general-purpose storage account runbook must reject storage requests that do not use an encrypted transport, then retain storage hardening read-back evidence. Which hardened general-purpose storage account pair completes both duties?

- **A — Correct.** First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.
  First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true. This ordered secure transfer required workflow lets the hardened general-purpose storage account reject storage requests that do not use an encrypted transport and then verify the resulting state.
- **B — Incorrect.** First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
  First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently. This hardened general-purpose storage account pair serves shared key authorization. Hardened general-purpose storage account uses shared key authorization for both steps; secure transfer required remains untouched in hardened general-purpose storage account, so its secure transfer required gate to reject storage requests that do not use an encrypted transport fails.
- **C — Incorrect.** First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.
  First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation. This hardened general-purpose storage account pair serves storage account naming. Hardened general-purpose storage account closes storage account naming, not secure transfer required; without the secure transfer required workflow, it cannot reject storage requests that do not use an encrypted transport.
- **D — Incorrect.** First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.
  First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS. This hardened general-purpose storage account pair serves locally redundant storage. Locally redundant storage cannot replace secure transfer required in hardened general-purpose storage account. Use this secure transfer required pair instead: First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB06-CP01`).

**Microsoft Learn sources:**

- [Require secure transfer for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer)

**Source reviewed:** 2026-08-31

## LAB06-Q47 — B

**Question:** To satisfy the storage hardening requirement, operators must change the hardened general-purpose storage account configuration and prove it can refuse clients that negotiate an obsolete transport protocol. Which sequence is coherent?

- **A — Incorrect.** First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.
  First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration. This hardened general-purpose storage account pair serves access-key rotation. Hardened general-purpose storage account uses access-key rotation for both steps; minimum TLS version remains untouched in hardened general-purpose storage account, so its minimum TLS version gate to refuse clients that negotiate an obsolete transport protocol fails.
- **B — Correct.** First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
  First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard. For hardened general-purpose storage account, the minimum TLS version operation precedes its minimum TLS version read-back check, allowing it to refuse clients that negotiate an obsolete transport protocol.
- **C — Incorrect.** First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.
  First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS. This hardened general-purpose storage account pair serves locally redundant storage. Locally redundant storage cannot replace minimum TLS version in hardened general-purpose storage account. Use this minimum TLS version pair instead: First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
- **D — Incorrect.** First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region.
  First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region. This hardened general-purpose storage account pair serves zone-redundant storage. Hardened general-purpose storage account proves zone-redundant storage, but minimum TLS version lacks implementation in hardened general-purpose storage account and minimum TLS version proof; the minimum TLS version outcome to refuse clients that negotiate an obsolete transport protocol remains open.

**Objectives:** `ST-ACCOUNTS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB06-CP02`).

**Microsoft Learn sources:**

- [Configure a minimum TLS version for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/transport-layer-security-configure-minimum-version)

**Source reviewed:** 2026-08-31

## LAB06-Q48 — B

**Question:** The storage administrator hardening a general-purpose account needs a safe hardened general-purpose storage account change to accept only Microsoft Entra credentials for data access, followed by storage hardening evidence. Which pair merits approval?

- **A — Incorrect.** First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files.
  First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files. This hardened general-purpose storage account pair serves storage service encryption. Hardened general-purpose storage account closes storage service encryption, not shared key authorization; without the shared key authorization workflow, it cannot accept only Microsoft Entra credentials for data access.
- **B — Correct.** First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
  First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently. In the hardened general-purpose storage account, the first shared key authorization step runs; the hardened general-purpose storage account then reads shared key authorization state to prove it can accept only Microsoft Entra credentials for data access.
- **C — Incorrect.** First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region.
  First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region. This hardened general-purpose storage account pair serves zone-redundant storage. Hardened general-purpose storage account proves zone-redundant storage, but shared key authorization lacks implementation in hardened general-purpose storage account and shared key authorization proof; the shared key authorization outcome to accept only Microsoft Entra credentials for data access remains open.
- **D — Incorrect.** First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
  First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy. This hardened general-purpose storage account pair serves geo-redundant read access. Hardened general-purpose storage account uses geo-redundant read access for both steps; shared key authorization remains untouched in hardened general-purpose storage account, so its shared key authorization gate to accept only Microsoft Entra credentials for data access fails.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB06-CP03`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB06-Q49 — B

**Question:** The hardened general-purpose storage account has two storage hardening gates: replace a compromised credential without losing the second recovery credential, then prove the hardened general-purpose storage account state. Which storage hardening sequence works?

- **A — Incorrect.** First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.
  First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account. This hardened general-purpose storage account pair serves StorageV2 accounts. StorageV2 accounts cannot replace access-key rotation in hardened general-purpose storage account. Use this access-key rotation pair instead: First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.
- **B — Correct.** First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.
  For the hardened general-purpose storage account, the safe access-key rotation order is: first, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration. The hardened general-purpose storage account records access-key rotation proof after configuration.
- **C — Incorrect.** First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
  First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy. This hardened general-purpose storage account pair serves geo-redundant read access. Hardened general-purpose storage account uses geo-redundant read access for both steps; access-key rotation remains untouched in hardened general-purpose storage account, so its access-key rotation gate to replace a compromised credential without losing the second recovery credential fails.
- **D — Incorrect.** First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.
  First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true. This hardened general-purpose storage account pair serves secure transfer required. Hardened general-purpose storage account closes secure transfer required, not access-key rotation; without the access-key rotation workflow, it cannot replace a compromised credential without losing the second recovery credential.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB06-CP04`).

**Microsoft Learn sources:**

- [Manage Azure Storage account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)

**Source reviewed:** 2026-08-31

## LAB06-Q50 — D

**Question:** Which storage hardening path makes the hardened general-purpose storage account able to confirm that stored service data is encrypted without an application change, then inspects the defining properties?

- **A — Incorrect.** First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.
  First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation. This hardened general-purpose storage account pair serves storage account naming. Hardened general-purpose storage account proves storage account naming, but storage service encryption lacks implementation in hardened general-purpose storage account and storage service encryption proof; the storage service encryption outcome to confirm that stored service data is encrypted without an application change remains open.
- **B — Incorrect.** First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.
  First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true. This hardened general-purpose storage account pair serves secure transfer required. Hardened general-purpose storage account uses secure transfer required for both steps; storage service encryption remains untouched in hardened general-purpose storage account, so its storage service encryption gate to confirm that stored service data is encrypted without an application change fails.
- **C — Incorrect.** First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
  First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard. This hardened general-purpose storage account pair serves minimum TLS version. Hardened general-purpose storage account closes minimum TLS version, not storage service encryption; without the storage service encryption workflow, it cannot confirm that stored service data is encrypted without an application change.
- **D — Correct.** First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files.
  First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files. The hardened general-purpose storage account uses its storage service encryption mutation gate and storage service encryption verification gate before it can confirm that stored service data is encrypted without an application change.

**Objectives:** `ST-ACCOUNTS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB06-CP05`).

**Microsoft Learn sources:**

- [Azure Storage encryption for data at rest](https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption)

**Source reviewed:** 2026-08-31
