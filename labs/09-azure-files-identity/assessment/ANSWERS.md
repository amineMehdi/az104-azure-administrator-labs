# Lab 09 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB09-Q01 — C

**Question:** The file-service acceptance architecture note requires the recoverable team file share environment to cap the capacity available to a team file share. Which statement defines the relevant file-service acceptance boundary?

- **A — Incorrect.** The enabled file-share protocol and account configuration determine which clients and identity options can connect.
  The enabled file-share protocol and account configuration determine which clients and identity options can connect. In the recoverable team file share, this statement describes SMB and NFS share protocols. Recoverable team file share asks about file share quota; this SMB and NFS share protocols choice leaves the file share quota explanation missing.
- **B — Incorrect.** For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs.
  For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs. In the recoverable team file share, this statement describes file and directory ACLs. The file and directory ACLs statement accurately describes file and directory ACLs; however, recoverable team file share needs file share quota to cap the capacity available to a team file share; file and directory ACLs cannot replace file share quota.
- **C — Correct.** An Azure file share quota limits the maximum provisioned capacity for that share.
  For the recoverable team file share, the rule for file share quota is defined by this statement: an Azure file share quota limits the maximum provisioned capacity for that share. It supports the required outcome to cap the capacity available to a team file share.
- **D — Incorrect.** Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots.
  Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots. In the recoverable team file share, this statement describes file share soft delete. File share quota governs recoverable team file share; file share soft delete cannot support file share quota when operators must cap the capacity available to a team file share.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Create an Azure file share](https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share)

**Source reviewed:** 2026-08-31

## LAB09-Q02 — A

**Question:** A new file-service acceptance operator must explain why the recoverable team file share can select the file-sharing protocol that matches the client workload. Which explanation is accurate?

- **A — Correct.** The enabled file-share protocol and account configuration determine which clients and identity options can connect.
  The enabled file-share protocol and account configuration determine which clients and identity options can connect. The recoverable team file share applies that SMB and NFS share protocols boundary when operators must select the file-sharing protocol that matches the client workload.
- **B — Incorrect.** Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.
  Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources. In the recoverable team file share, this statement describes identity-based file authentication. Selecting identity-based file authentication for recoverable team file share leaves SMB and NFS share protocols unanswered in recoverable team file share; the recoverable team file share lacks a SMB and NFS share protocols basis to select the file-sharing protocol that matches the client workload.
- **C — Incorrect.** Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements.
  Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements. In the recoverable team file share, this statement describes Azure Files network path. SMB and NFS share protocols governs recoverable team file share; Azure Files network path cannot support SMB and NFS share protocols when operators must select the file-sharing protocol that matches the client workload.
- **D — Incorrect.** AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.
  AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions. In the recoverable team file share, this statement describes AzCopy file transfers. Recoverable team file share asks about SMB and NFS share protocols; this AzCopy file transfers choice leaves the SMB and NFS share protocols explanation missing.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Plan for an Azure Files deployment](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-planning)

**Source reviewed:** 2026-08-31

## LAB09-Q03 — A

**Question:** The recoverable team file share acceptance criteria require operators to authenticate file clients with an approved directory identity. Which service fact supports that requirement?

- **A — Correct.** Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.
  The recoverable team file share needs identity-based file authentication to authenticate file clients with an approved directory identity; this option states the applicable identity-based file authentication rule: identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.
- **B — Incorrect.** Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation.
  Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation. In the recoverable team file share, this statement describes share-level Azure RBAC. Identity-based file authentication governs recoverable team file share; share-level Azure RBAC cannot support identity-based file authentication when operators must authenticate file clients with an approved directory identity.
- **C — Incorrect.** A share snapshot is a read-only point-in-time copy used to recover prior file and directory content.
  A share snapshot is a read-only point-in-time copy used to recover prior file and directory content. In the recoverable team file share, this statement describes file share snapshots. Recoverable team file share asks about identity-based file authentication; this file share snapshots choice leaves the identity-based file authentication explanation missing.
- **D — Incorrect.** Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used.
  Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used. In the recoverable team file share, this statement describes SMB port connectivity. The SMB port connectivity statement accurately describes SMB port connectivity; however, recoverable team file share needs identity-based file authentication to authenticate file clients with an approved directory identity; SMB port connectivity cannot replace identity-based file authentication.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Identity-based authentication for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q04 — A

**Question:** A file-service acceptance reviewer challenges whether the recoverable team file share can grant a principal access at the share boundary. Which response resolves the concern?

- **A — Correct.** Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation.
  Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation. This share-level Azure RBAC fact resolves the recoverable team file share design question about how to grant a principal access at the share boundary.
- **B — Incorrect.** For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs.
  For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs. In the recoverable team file share, this statement describes file and directory ACLs. Recoverable team file share asks about share-level Azure RBAC; this file and directory ACLs choice leaves the share-level Azure RBAC explanation missing.
- **C — Incorrect.** Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots.
  Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots. In the recoverable team file share, this statement describes file share soft delete. The file share soft delete statement accurately describes file share soft delete; however, recoverable team file share needs share-level Azure RBAC to grant a principal access at the share boundary; file share soft delete cannot replace share-level Azure RBAC.
- **D — Incorrect.** An Azure file share quota limits the maximum provisioned capacity for that share.
  An Azure file share quota limits the maximum provisioned capacity for that share. In the recoverable team file share, this statement describes file share quota. Selecting file share quota for recoverable team file share leaves share-level Azure RBAC unanswered in recoverable team file share; the recoverable team file share lacks a share-level Azure RBAC basis to grant a principal access at the share boundary.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Assign share-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-assign-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q05 — D

**Question:** The recoverable team file share handoff omits the file-service acceptance rule needed to limit access to particular directories and files after share access is granted. Which statement should the team add?

- **A — Incorrect.** Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements.
  Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements. In the recoverable team file share, this statement describes Azure Files network path. Recoverable team file share asks about file and directory ACLs; this Azure Files network path choice leaves the file and directory ACLs explanation missing.
- **B — Incorrect.** AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.
  AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions. In the recoverable team file share, this statement describes AzCopy file transfers. The AzCopy file transfers statement accurately describes AzCopy file transfers; however, recoverable team file share needs file and directory ACLs to limit access to particular directories and files after share access is granted; AzCopy file transfers cannot replace file and directory ACLs.
- **C — Incorrect.** The enabled file-share protocol and account configuration determine which clients and identity options can connect.
  The enabled file-share protocol and account configuration determine which clients and identity options can connect. In the recoverable team file share, this statement describes SMB and NFS share protocols. Selecting SMB and NFS share protocols for recoverable team file share leaves file and directory ACLs unanswered in recoverable team file share; the recoverable team file share lacks a file and directory ACLs basis to limit access to particular directories and files after share access is granted.
- **D — Correct.** For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs.
  For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs. For recoverable team file share, file and directory ACLs supplies the service rule needed to limit access to particular directories and files after share access is granted.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Configure directory and file-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-configure-file-level-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q06 — B

**Question:** A file-service acceptance incident review of the recoverable team file share depends on the ability to restrict share connectivity to the sanctioned route. Which platform description is reliable?

- **A — Incorrect.** A share snapshot is a read-only point-in-time copy used to recover prior file and directory content.
  A share snapshot is a read-only point-in-time copy used to recover prior file and directory content. In the recoverable team file share, this statement describes file share snapshots. The file share snapshots statement accurately describes file share snapshots; however, recoverable team file share needs Azure Files network path to restrict share connectivity to the sanctioned route; file share snapshots cannot replace Azure Files network path.
- **B — Correct.** Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements.
  Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements. In the recoverable team file share, this Azure Files network path rule supports the need to restrict share connectivity to the sanctioned route.
- **C — Incorrect.** Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used.
  Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used. In the recoverable team file share, this statement describes SMB port connectivity. Azure Files network path governs recoverable team file share; SMB port connectivity cannot support Azure Files network path when operators must restrict share connectivity to the sanctioned route.
- **D — Incorrect.** Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.
  Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources. In the recoverable team file share, this statement describes identity-based file authentication. Recoverable team file share asks about Azure Files network path; this identity-based file authentication choice leaves the Azure Files network path explanation missing.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Azure Files networking considerations](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-networking-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q07 — A

**Question:** A file-services administrator publishing a recoverable team share is updating the file-service acceptance runbook. The requirement is to capture a point-in-time, read-only view of share contents. Which statement describes Azure behavior correctly?

- **A — Correct.** A share snapshot is a read-only point-in-time copy used to recover prior file and directory content.
  For the recoverable team file share, the rule for file share snapshots is defined by this statement: a share snapshot is a read-only point-in-time copy used to recover prior file and directory content. It supports the required outcome to capture a point-in-time, read-only view of share contents.
- **B — Incorrect.** Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots.
  Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots. In the recoverable team file share, this statement describes file share soft delete. File share snapshots governs recoverable team file share; file share soft delete cannot support file share snapshots when operators must capture a point-in-time, read-only view of share contents.
- **C — Incorrect.** An Azure file share quota limits the maximum provisioned capacity for that share.
  An Azure file share quota limits the maximum provisioned capacity for that share. In the recoverable team file share, this statement describes file share quota. Recoverable team file share asks about file share snapshots; this file share quota choice leaves the file share snapshots explanation missing.
- **D — Incorrect.** Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation.
  Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation. In the recoverable team file share, this statement describes share-level Azure RBAC. The share-level Azure RBAC statement accurately describes share-level Azure RBAC; however, recoverable team file share needs file share snapshots to capture a point-in-time, read-only view of share contents; share-level Azure RBAC cannot replace file share snapshots.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Azure Files snapshots](https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files)

**Source reviewed:** 2026-08-31

## LAB09-Q08 — C

**Question:** A file-service acceptance peer review asks how the recoverable team file share should handle this outcome: restore a share removed during the service retention period. Which explanation is accurate?

- **A — Incorrect.** AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.
  AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions. In the recoverable team file share, this statement describes AzCopy file transfers. File share soft delete governs recoverable team file share; AzCopy file transfers cannot support file share soft delete when operators must restore a share removed during the service retention period.
- **B — Incorrect.** The enabled file-share protocol and account configuration determine which clients and identity options can connect.
  The enabled file-share protocol and account configuration determine which clients and identity options can connect. In the recoverable team file share, this statement describes SMB and NFS share protocols. Recoverable team file share asks about file share soft delete; this SMB and NFS share protocols choice leaves the file share soft delete explanation missing.
- **C — Correct.** Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots.
  Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots. The recoverable team file share applies that file share soft delete boundary when operators must restore a share removed during the service retention period.
- **D — Incorrect.** For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs.
  For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs. In the recoverable team file share, this statement describes file and directory ACLs. Selecting file and directory ACLs for recoverable team file share leaves file share soft delete unanswered in recoverable team file share; the recoverable team file share lacks a file share soft delete basis to restore a share removed during the service retention period.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Prevent accidental deletion of Azure file shares](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion)

**Source reviewed:** 2026-08-31

## LAB09-Q09 — C

**Question:** For the recoverable team file share, the file-service acceptance plan must transfer file-share content with a resumable command-line data mover. Which statement about file-service acceptance belongs in the recoverable team file share record?

- **A — Incorrect.** Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used.
  Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used. In the recoverable team file share, this statement describes SMB port connectivity. Recoverable team file share asks about AzCopy file transfers; this SMB port connectivity choice leaves the AzCopy file transfers explanation missing.
- **B — Incorrect.** Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.
  Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources. In the recoverable team file share, this statement describes identity-based file authentication. The identity-based file authentication statement accurately describes identity-based file authentication; however, recoverable team file share needs AzCopy file transfers to transfer file-share content with a resumable command-line data mover; identity-based file authentication cannot replace AzCopy file transfers.
- **C — Correct.** AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.
  The recoverable team file share needs AzCopy file transfers to transfer file-share content with a resumable command-line data mover; this option states the applicable AzCopy file transfers rule: azCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.
- **D — Incorrect.** Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements.
  Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements. In the recoverable team file share, this statement describes Azure Files network path. AzCopy file transfers governs recoverable team file share; Azure Files network path cannot support AzCopy file transfers when operators must transfer file-share content with a resumable command-line data mover.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Use AzCopy with Azure Files](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files)

**Source reviewed:** 2026-08-31

## LAB09-Q10 — D

**Question:** The file-service acceptance review compares four claims for the recoverable team file share requirement to diagnose clients that cannot reach the SMB endpoint on its required port. Which claim is technically sound?

- **A — Incorrect.** An Azure file share quota limits the maximum provisioned capacity for that share.
  An Azure file share quota limits the maximum provisioned capacity for that share. In the recoverable team file share, this statement describes file share quota. The file share quota statement accurately describes file share quota; however, recoverable team file share needs SMB port connectivity to diagnose clients that cannot reach the SMB endpoint on its required port; file share quota cannot replace SMB port connectivity.
- **B — Incorrect.** Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation.
  Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation. In the recoverable team file share, this statement describes share-level Azure RBAC. Selecting share-level Azure RBAC for recoverable team file share leaves SMB port connectivity unanswered in recoverable team file share; the recoverable team file share lacks a SMB port connectivity basis to diagnose clients that cannot reach the SMB endpoint on its required port.
- **C — Incorrect.** A share snapshot is a read-only point-in-time copy used to recover prior file and directory content.
  A share snapshot is a read-only point-in-time copy used to recover prior file and directory content. In the recoverable team file share, this statement describes file share snapshots. SMB port connectivity governs recoverable team file share; file share snapshots cannot support SMB port connectivity when operators must diagnose clients that cannot reach the SMB endpoint on its required port.
- **D — Correct.** Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used.
  Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used. This SMB port connectivity fact resolves the recoverable team file share design question about how to diagnose clients that cannot reach the SMB endpoint on its required port.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Files SMB connectivity](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-storage/files/connectivity/files-troubleshoot-smb-connectivity)

**Source reviewed:** 2026-08-31

## LAB09-Q11 — D

**Question:** For the recoverable team file share, operators need to cap the capacity available to a team file share. Which change realizes that requirement?

- **A — Incorrect.** Configure the supported directory source on the storage account before assigning users access.
  Configure the supported directory source on the storage account before assigning users access. In the recoverable team file share, this action changes identity-based file authentication. Recoverable team file share approved file share quota, not identity-based file authentication; only the file share quota change can cap the capacity available to a team file share.
- **B — Incorrect.** Provide an approved network path and name resolution in addition to identity permissions.
  Provide an approved network path and name resolution in addition to identity permissions. In the recoverable team file share, this action changes Azure Files network path. Recoverable team file share requires file share quota; changing Azure Files network path leaves file share quota absent in recoverable team file share; recoverable team file share cannot cap the capacity available to a team file share.
- **C — Incorrect.** Authenticate with the least-privilege mechanism and copy a deterministic test directory.
  Authenticate with the least-privilege mechanism and copy a deterministic test directory. In the recoverable team file share, this action changes AzCopy file transfers. AzCopy file transfers does not implement file share quota for recoverable team file share; the recoverable team file share still cannot cap the capacity available to a team file share.
- **D — Correct.** Create the share with an approved quota that fits the account tier and workload forecast.
  Create the share with an approved quota that fits the account tier and workload forecast. In recoverable team file share, applying file share quota is the scoped way to cap the capacity available to a team file share.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Create an Azure file share](https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share)

**Source reviewed:** 2026-08-31

## LAB09-Q12 — C

**Question:** Operators must automate the recoverable team file share change needed to select the file-sharing protocol that matches the client workload. Which file-service acceptance operation belongs in the runbook?

- **A — Incorrect.** Assign the narrowest Storage File Data SMB Share role at the share or account scope.
  Assign the narrowest Storage File Data SMB Share role at the share or account scope. In the recoverable team file share, this action changes share-level Azure RBAC. Recoverable team file share requires SMB and NFS share protocols; changing share-level Azure RBAC leaves SMB and NFS share protocols absent in recoverable team file share; recoverable team file share cannot select the file-sharing protocol that matches the client workload.
- **B — Incorrect.** Create a share snapshot before the controlled file modification in the recovery exercise.
  Create a share snapshot before the controlled file modification in the recovery exercise. In the recoverable team file share, this action changes file share snapshots. File share snapshots does not implement SMB and NFS share protocols for recoverable team file share; the recoverable team file share still cannot select the file-sharing protocol that matches the client workload.
- **C — Correct.** Choose SMB for the identity-based scenario and verify account compatibility before creation.
  Choose SMB for the identity-based scenario and verify account compatibility before creation. The recoverable team file share uses this SMB and NFS share protocols operation to select the file-sharing protocol that matches the client workload within the approved scope.
- **D — Incorrect.** Test the client-to-file-endpoint network path before troubleshooting storage permissions.
  Test the client-to-file-endpoint network path before troubleshooting storage permissions. In the recoverable team file share, this action changes SMB port connectivity. Recoverable team file share approved SMB and NFS share protocols, not SMB port connectivity; only the SMB and NFS share protocols change can select the file-sharing protocol that matches the client workload.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Plan for an Azure Files deployment](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-planning)

**Source reviewed:** 2026-08-31

## LAB09-Q13 — C

**Question:** A recoverable team file share review finds file-service acceptance drift from the need to authenticate file clients with an approved directory identity. Which correction addresses that drift?

- **A — Incorrect.** Grant both the required share-level role and the minimum NTFS ACL on the target path.
  Grant both the required share-level role and the minimum NTFS ACL on the target path. In the recoverable team file share, this action changes file and directory ACLs. File and directory ACLs does not implement identity-based file authentication for recoverable team file share; the recoverable team file share still cannot authenticate file clients with an approved directory identity.
- **B — Incorrect.** Enable share soft delete before testing deletion of the entire share.
  Enable share soft delete before testing deletion of the entire share. In the recoverable team file share, this action changes file share soft delete. Recoverable team file share instead needs identity-based file authentication: Configure the supported directory source on the storage account before assigning users access. The file share soft delete action omits that identity-based file authentication work.
- **C — Correct.** Configure the supported directory source on the storage account before assigning users access.
  For the recoverable team file share, the required identity-based file authentication action is: configure the supported directory source on the storage account before assigning users access. It makes the environment able to authenticate file clients with an approved directory identity.
- **D — Incorrect.** Create the share with an approved quota that fits the account tier and workload forecast.
  Create the share with an approved quota that fits the account tier and workload forecast. In the recoverable team file share, this action changes file share quota. Recoverable team file share requires identity-based file authentication; changing file share quota leaves identity-based file authentication absent in recoverable team file share; recoverable team file share cannot authenticate file clients with an approved directory identity.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Identity-based authentication for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q14 — C

**Question:** The recoverable team file share window permits only the file-service acceptance change needed to grant a principal access at the share boundary. Which option respects the boundary?

- **A — Incorrect.** Provide an approved network path and name resolution in addition to identity permissions.
  Provide an approved network path and name resolution in addition to identity permissions. In the recoverable team file share, this action changes Azure Files network path. Recoverable team file share instead needs share-level Azure RBAC: Assign the narrowest Storage File Data SMB Share role at the share or account scope. The Azure Files network path action omits that share-level Azure RBAC work.
- **B — Incorrect.** Authenticate with the least-privilege mechanism and copy a deterministic test directory.
  Authenticate with the least-privilege mechanism and copy a deterministic test directory. In the recoverable team file share, this action changes AzCopy file transfers. Recoverable team file share approved share-level Azure RBAC, not AzCopy file transfers; only the share-level Azure RBAC change can grant a principal access at the share boundary.
- **C — Correct.** Assign the narrowest Storage File Data SMB Share role at the share or account scope.
  Assign the narrowest Storage File Data SMB Share role at the share or account scope. This changes share-level Azure RBAC in the recoverable team file share, supplying the missing state needed to grant a principal access at the share boundary.
- **D — Incorrect.** Choose SMB for the identity-based scenario and verify account compatibility before creation.
  Choose SMB for the identity-based scenario and verify account compatibility before creation. In the recoverable team file share, this action changes SMB and NFS share protocols. SMB and NFS share protocols does not implement share-level Azure RBAC for recoverable team file share; the recoverable team file share still cannot grant a principal access at the share boundary.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Assign share-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-assign-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q15 — B

**Question:** The file-service acceptance preflight has passed; the recoverable team file share must now limit access to particular directories and files after share access is granted. Which operation should run?

- **A — Incorrect.** Create a share snapshot before the controlled file modification in the recovery exercise.
  Create a share snapshot before the controlled file modification in the recovery exercise. In the recoverable team file share, this action changes file share snapshots. Recoverable team file share approved file and directory ACLs, not file share snapshots; only the file and directory ACLs change can limit access to particular directories and files after share access is granted.
- **B — Correct.** Grant both the required share-level role and the minimum NTFS ACL on the target path.
  The recoverable team file share must limit access to particular directories and files after share access is granted; this option performs its direct file and directory ACLs change: grant both the required share-level role and the minimum NTFS ACL on the target path.
- **C — Incorrect.** Test the client-to-file-endpoint network path before troubleshooting storage permissions.
  Test the client-to-file-endpoint network path before troubleshooting storage permissions. In the recoverable team file share, this action changes SMB port connectivity. SMB port connectivity does not implement file and directory ACLs for recoverable team file share; the recoverable team file share still cannot limit access to particular directories and files after share access is granted.
- **D — Incorrect.** Configure the supported directory source on the storage account before assigning users access.
  Configure the supported directory source on the storage account before assigning users access. In the recoverable team file share, this action changes identity-based file authentication. Recoverable team file share instead needs file and directory ACLs: Grant both the required share-level role and the minimum NTFS ACL on the target path. The identity-based file authentication action omits that file and directory ACLs work.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Configure directory and file-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-configure-file-level-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q16 — A

**Question:** The recoverable team file share plan must restrict share connectivity to the sanctioned route while limiting the mutation scope to file-service acceptance. Which action is appropriate?

- **A — Correct.** Provide an approved network path and name resolution in addition to identity permissions.
  Provide an approved network path and name resolution in addition to identity permissions. It is the least-change Azure Files network path path for the recoverable team file share requirement to restrict share connectivity to the sanctioned route.
- **B — Incorrect.** Enable share soft delete before testing deletion of the entire share.
  Enable share soft delete before testing deletion of the entire share. In the recoverable team file share, this action changes file share soft delete. File share soft delete does not implement Azure Files network path for recoverable team file share; the recoverable team file share still cannot restrict share connectivity to the sanctioned route.
- **C — Incorrect.** Create the share with an approved quota that fits the account tier and workload forecast.
  Create the share with an approved quota that fits the account tier and workload forecast. In the recoverable team file share, this action changes file share quota. Recoverable team file share instead needs Azure Files network path: Provide an approved network path and name resolution in addition to identity permissions. The file share quota action omits that Azure Files network path work.
- **D — Incorrect.** Assign the narrowest Storage File Data SMB Share role at the share or account scope.
  Assign the narrowest Storage File Data SMB Share role at the share or account scope. In the recoverable team file share, this action changes share-level Azure RBAC. Recoverable team file share approved Azure Files network path, not share-level Azure RBAC; only the Azure Files network path change can restrict share connectivity to the sanctioned route.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Azure Files networking considerations](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-networking-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q17 — D

**Question:** A file-service acceptance ticket in the recoverable team file share says to capture a point-in-time, read-only view of share contents. Which file-service acceptance action completes the recoverable team file share request with minimal change?

- **A — Incorrect.** Authenticate with the least-privilege mechanism and copy a deterministic test directory.
  Authenticate with the least-privilege mechanism and copy a deterministic test directory. In the recoverable team file share, this action changes AzCopy file transfers. AzCopy file transfers does not implement file share snapshots for recoverable team file share; the recoverable team file share still cannot capture a point-in-time, read-only view of share contents.
- **B — Incorrect.** Choose SMB for the identity-based scenario and verify account compatibility before creation.
  Choose SMB for the identity-based scenario and verify account compatibility before creation. In the recoverable team file share, this action changes SMB and NFS share protocols. Recoverable team file share instead needs file share snapshots: Create a share snapshot before the controlled file modification in the recovery exercise. The SMB and NFS share protocols action omits that file share snapshots work.
- **C — Incorrect.** Grant both the required share-level role and the minimum NTFS ACL on the target path.
  Grant both the required share-level role and the minimum NTFS ACL on the target path. In the recoverable team file share, this action changes file and directory ACLs. Recoverable team file share approved file share snapshots, not file and directory ACLs; only the file share snapshots change can capture a point-in-time, read-only view of share contents.
- **D — Correct.** Create a share snapshot before the controlled file modification in the recovery exercise.
  Create a share snapshot before the controlled file modification in the recovery exercise. In recoverable team file share, applying file share snapshots is the scoped way to capture a point-in-time, read-only view of share contents.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Azure Files snapshots](https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files)

**Source reviewed:** 2026-08-31

## LAB09-Q18 — B

**Question:** The approach for the recoverable team file share is approved, but the file-service acceptance environment still cannot restore a share removed during the service retention period. Which implementation step closes the gap?

- **A — Incorrect.** Test the client-to-file-endpoint network path before troubleshooting storage permissions.
  Test the client-to-file-endpoint network path before troubleshooting storage permissions. In the recoverable team file share, this action changes SMB port connectivity. Recoverable team file share instead needs file share soft delete: Enable share soft delete before testing deletion of the entire share. The SMB port connectivity action omits that file share soft delete work.
- **B — Correct.** Enable share soft delete before testing deletion of the entire share.
  Enable share soft delete before testing deletion of the entire share. The recoverable team file share uses this file share soft delete operation to restore a share removed during the service retention period within the approved scope.
- **C — Incorrect.** Configure the supported directory source on the storage account before assigning users access.
  Configure the supported directory source on the storage account before assigning users access. In the recoverable team file share, this action changes identity-based file authentication. Recoverable team file share requires file share soft delete; changing identity-based file authentication leaves file share soft delete absent in recoverable team file share; recoverable team file share cannot restore a share removed during the service retention period.
- **D — Incorrect.** Provide an approved network path and name resolution in addition to identity permissions.
  Provide an approved network path and name resolution in addition to identity permissions. In the recoverable team file share, this action changes Azure Files network path. Azure Files network path does not implement file share soft delete for recoverable team file share; the recoverable team file share still cannot restore a share removed during the service retention period.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Prevent accidental deletion of Azure file shares](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion)

**Source reviewed:** 2026-08-31

## LAB09-Q19 — A

**Question:** The file-services administrator publishing a recoverable team share may change the recoverable team file share only to transfer file-share content with a resumable command-line data mover. Which file-service acceptance action stays within that assignment?

- **A — Correct.** Authenticate with the least-privilege mechanism and copy a deterministic test directory.
  For the recoverable team file share, the required AzCopy file transfers action is: authenticate with the least-privilege mechanism and copy a deterministic test directory. It makes the environment able to transfer file-share content with a resumable command-line data mover.
- **B — Incorrect.** Create the share with an approved quota that fits the account tier and workload forecast.
  Create the share with an approved quota that fits the account tier and workload forecast. In the recoverable team file share, this action changes file share quota. Recoverable team file share requires AzCopy file transfers; changing file share quota leaves AzCopy file transfers absent in recoverable team file share; recoverable team file share cannot transfer file-share content with a resumable command-line data mover.
- **C — Incorrect.** Assign the narrowest Storage File Data SMB Share role at the share or account scope.
  Assign the narrowest Storage File Data SMB Share role at the share or account scope. In the recoverable team file share, this action changes share-level Azure RBAC. Share-level Azure RBAC does not implement AzCopy file transfers for recoverable team file share; the recoverable team file share still cannot transfer file-share content with a resumable command-line data mover.
- **D — Incorrect.** Create a share snapshot before the controlled file modification in the recovery exercise.
  Create a share snapshot before the controlled file modification in the recovery exercise. In the recoverable team file share, this action changes file share snapshots. Recoverable team file share instead needs AzCopy file transfers: Authenticate with the least-privilege mechanism and copy a deterministic test directory. The file share snapshots action omits that AzCopy file transfers work.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Use AzCopy with Azure Files](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files)

**Source reviewed:** 2026-08-31

## LAB09-Q20 — D

**Question:** A file-service acceptance dry run shows no recoverable team file share command will diagnose clients that cannot reach the SMB endpoint on its required port. Which action belongs before execution?

- **A — Incorrect.** Choose SMB for the identity-based scenario and verify account compatibility before creation.
  Choose SMB for the identity-based scenario and verify account compatibility before creation. In the recoverable team file share, this action changes SMB and NFS share protocols. Recoverable team file share requires SMB port connectivity; changing SMB and NFS share protocols leaves SMB port connectivity absent in recoverable team file share; recoverable team file share cannot diagnose clients that cannot reach the SMB endpoint on its required port.
- **B — Incorrect.** Grant both the required share-level role and the minimum NTFS ACL on the target path.
  Grant both the required share-level role and the minimum NTFS ACL on the target path. In the recoverable team file share, this action changes file and directory ACLs. File and directory ACLs does not implement SMB port connectivity for recoverable team file share; the recoverable team file share still cannot diagnose clients that cannot reach the SMB endpoint on its required port.
- **C — Incorrect.** Enable share soft delete before testing deletion of the entire share.
  Enable share soft delete before testing deletion of the entire share. In the recoverable team file share, this action changes file share soft delete. Recoverable team file share instead needs SMB port connectivity: Test the client-to-file-endpoint network path before troubleshooting storage permissions. The file share soft delete action omits that SMB port connectivity work.
- **D — Correct.** Test the client-to-file-endpoint network path before troubleshooting storage permissions.
  Test the client-to-file-endpoint network path before troubleshooting storage permissions. This changes SMB port connectivity in the recoverable team file share, supplying the missing state needed to diagnose clients that cannot reach the SMB endpoint on its required port.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Files SMB connectivity](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-storage/files/connectivity/files-troubleshoot-smb-connectivity)

**Source reviewed:** 2026-08-31

## LAB09-Q21 — D

**Question:** The file-services administrator publishing a recoverable team share must confirm the recoverable team file share, without mutation, can cap the capacity available to a team file share. Which file-service acceptance check qualifies?

- **A — Incorrect.** List the principal's data-role assignment and confirm its scope includes the intended share.
  List the principal's data-role assignment and confirm its scope includes the intended share. In the recoverable team file share, this check observes share-level Azure RBAC. Recoverable team file share output covers share-level Azure RBAC, not file share quota; the file share quota requirement to cap the capacity available to a team file share remains unverified.
- **B — Incorrect.** List snapshots and confirm the snapshot timestamp precedes the modification.
  List snapshots and confirm the snapshot timestamp precedes the modification. In the recoverable team file share, this check observes file share snapshots. File share snapshots success in recoverable team file share cannot verify file share quota; recoverable team file share cannot cap the capacity available to a team file share until file share quota evidence exists.
- **C — Incorrect.** Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
  Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt. In the recoverable team file share, this check observes SMB port connectivity. Recoverable team file share reads SMB port connectivity, leaving file share quota unproved in recoverable team file share; recoverable team file share still has no file share quota proof.
- **D — Correct.** Query share quota and access tier and compare them with the lab inputs.
  The recoverable team file share validator needs this file share quota result: query share quota and access tier and compare them with the lab inputs. It proves the outcome to cap the capacity available to a team file share rather than an adjacent checkpoint.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Create an Azure file share](https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share)

**Source reviewed:** 2026-08-31

## LAB09-Q22 — A

**Question:** The recoverable team file share configuration is complete; the file-service acceptance reviewers need evidence it can select the file-sharing protocol that matches the client workload. Which observation shows success?

- **A — Correct.** Query enabledProtocols and confirm the client uses the matching mount protocol.
  Query enabledProtocols and confirm the client uses the matching mount protocol. This is independent SMB and NFS share protocols evidence for the recoverable team file share, even if recoverable team file share setup reports success before SMB and NFS share protocols becomes observable.
- **B — Incorrect.** Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
  Verify the principal's role assignment and inspect the path ACL from a domain-connected client. In the recoverable team file share, this check observes file and directory ACLs. Recoverable team file share reads file and directory ACLs, leaving SMB and NFS share protocols unproved in recoverable team file share; recoverable team file share still has no SMB and NFS share protocols proof.
- **C — Incorrect.** Query shareDeleteRetentionPolicy and list the deleted share by name.
  Query shareDeleteRetentionPolicy and list the deleted share by name. In the recoverable team file share, this check observes file share soft delete. Recoverable team file share could pass file share soft delete while SMB and NFS share protocols is wrong; recoverable team file share still lacks SMB and NFS share protocols proof.
- **D — Incorrect.** Query share quota and access tier and compare them with the lab inputs.
  Query share quota and access tier and compare them with the lab inputs. In the recoverable team file share, this check observes file share quota. Recoverable team file share output covers file share quota, not SMB and NFS share protocols; the SMB and NFS share protocols requirement to select the file-sharing protocol that matches the client workload remains unverified.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Plan for an Azure Files deployment](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-planning)

**Source reviewed:** 2026-08-31

## LAB09-Q23 — B

**Question:** The file-service acceptance validation asks whether the recoverable team file share can authenticate file clients with an approved directory identity. Which observable state is strongest?

- **A — Incorrect.** Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
  Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access. In the recoverable team file share, this check observes Azure Files network path. Recoverable team file share reads Azure Files network path, leaving identity-based file authentication unproved in recoverable team file share; recoverable team file share still has no identity-based file authentication proof.
- **B — Correct.** Query directoryServiceOptions and the account's identity configuration.
  Query directoryServiceOptions and the account's identity configuration. For recoverable team file share, this identity-based file authentication read confirms the service can authenticate file clients with an approved directory identity.
- **C — Incorrect.** Compare source and destination file counts, relative paths, lengths, and hashes where supported.
  Compare source and destination file counts, relative paths, lengths, and hashes where supported. In the recoverable team file share, this check observes AzCopy file transfers. Recoverable team file share output covers AzCopy file transfers, not identity-based file authentication; the identity-based file authentication requirement to authenticate file clients with an approved directory identity remains unverified.
- **D — Incorrect.** Query enabledProtocols and confirm the client uses the matching mount protocol.
  Query enabledProtocols and confirm the client uses the matching mount protocol. In the recoverable team file share, this check observes SMB and NFS share protocols. SMB and NFS share protocols success in recoverable team file share cannot verify identity-based file authentication; recoverable team file share cannot authenticate file clients with an approved directory identity until identity-based file authentication evidence exists.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Identity-based authentication for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q24 — C

**Question:** A recoverable team file share review must prove the file-service acceptance ability to grant a principal access at the share boundary. Which check avoids an adjacent feature?

- **A — Incorrect.** List snapshots and confirm the snapshot timestamp precedes the modification.
  List snapshots and confirm the snapshot timestamp precedes the modification. In the recoverable team file share, this check observes file share snapshots. Recoverable team file share could pass file share snapshots while share-level Azure RBAC is wrong; recoverable team file share still lacks share-level Azure RBAC proof.
- **B — Incorrect.** Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
  Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt. In the recoverable team file share, this check observes SMB port connectivity. Recoverable team file share output covers SMB port connectivity, not share-level Azure RBAC; the share-level Azure RBAC requirement to grant a principal access at the share boundary remains unverified.
- **C — Correct.** List the principal's data-role assignment and confirm its scope includes the intended share.
  List the principal's data-role assignment and confirm its scope includes the intended share. The recoverable team file share reads share-level Azure RBAC directly; that share-level Azure RBAC result proves the recoverable team file share can grant a principal access at the share boundary without another mutation.
- **D — Incorrect.** Query directoryServiceOptions and the account's identity configuration.
  Query directoryServiceOptions and the account's identity configuration. In the recoverable team file share, this check observes identity-based file authentication. Recoverable team file share reads identity-based file authentication, leaving share-level Azure RBAC unproved in recoverable team file share; recoverable team file share still has no share-level Azure RBAC proof.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Assign share-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-assign-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q25 — A

**Question:** The recoverable team file share evidence bundle needs a file-service acceptance result showing it can limit access to particular directories and files after share access is granted. Which result belongs in the checkpoint?

- **A — Correct.** Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
  For the recoverable team file share, this file and directory ACLs observation is decisive: verify the principal's role assignment and inspect the path ACL from a domain-connected client. It is recoverable team file share evidence that operators can limit access to particular directories and files after share access is granted.
- **B — Incorrect.** Query shareDeleteRetentionPolicy and list the deleted share by name.
  Query shareDeleteRetentionPolicy and list the deleted share by name. In the recoverable team file share, this check observes file share soft delete. File share soft delete success in recoverable team file share cannot verify file and directory ACLs; recoverable team file share cannot limit access to particular directories and files after share access is granted until file and directory ACLs evidence exists.
- **C — Incorrect.** Query share quota and access tier and compare them with the lab inputs.
  Query share quota and access tier and compare them with the lab inputs. In the recoverable team file share, this check observes file share quota. Recoverable team file share reads file share quota, leaving file and directory ACLs unproved in recoverable team file share; recoverable team file share still has no file and directory ACLs proof.
- **D — Incorrect.** List the principal's data-role assignment and confirm its scope includes the intended share.
  List the principal's data-role assignment and confirm its scope includes the intended share. In the recoverable team file share, this check observes share-level Azure RBAC. Recoverable team file share could pass share-level Azure RBAC while file and directory ACLs is wrong; recoverable team file share still lacks file and directory ACLs proof.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Configure directory and file-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-configure-file-level-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q26 — D

**Question:** Before recoverable team file share cleanup, the file-service acceptance team must reconfirm it can restrict share connectivity to the sanctioned route. Which read-only inspection should run?

- **A — Incorrect.** Compare source and destination file counts, relative paths, lengths, and hashes where supported.
  Compare source and destination file counts, relative paths, lengths, and hashes where supported. In the recoverable team file share, this check observes AzCopy file transfers. AzCopy file transfers success in recoverable team file share cannot verify Azure Files network path; recoverable team file share cannot restrict share connectivity to the sanctioned route until Azure Files network path evidence exists.
- **B — Incorrect.** Query enabledProtocols and confirm the client uses the matching mount protocol.
  Query enabledProtocols and confirm the client uses the matching mount protocol. In the recoverable team file share, this check observes SMB and NFS share protocols. Recoverable team file share reads SMB and NFS share protocols, leaving Azure Files network path unproved in recoverable team file share; recoverable team file share still has no Azure Files network path proof.
- **C — Incorrect.** Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
  Verify the principal's role assignment and inspect the path ACL from a domain-connected client. In the recoverable team file share, this check observes file and directory ACLs. Recoverable team file share could pass file and directory ACLs while Azure Files network path is wrong; recoverable team file share still lacks Azure Files network path proof.
- **D — Correct.** Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
  Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access. Because the recoverable team file share check observes Azure Files network path, it independently verifies the requirement to restrict share connectivity to the sanctioned route.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Azure Files networking considerations](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-networking-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q27 — C

**Question:** The recoverable team file share setup reports success after the file-service acceptance attempt to capture a point-in-time, read-only view of share contents. Which file-service acceptance read-only observation proves the recoverable team file share outcome?

- **A — Incorrect.** Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
  Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt. In the recoverable team file share, this check observes SMB port connectivity. Recoverable team file share reads SMB port connectivity, leaving file share snapshots unproved in recoverable team file share; recoverable team file share still has no file share snapshots proof.
- **B — Incorrect.** Query directoryServiceOptions and the account's identity configuration.
  Query directoryServiceOptions and the account's identity configuration. In the recoverable team file share, this check observes identity-based file authentication. Recoverable team file share could pass identity-based file authentication while file share snapshots is wrong; recoverable team file share still lacks file share snapshots proof.
- **C — Correct.** List snapshots and confirm the snapshot timestamp precedes the modification.
  The recoverable team file share validator needs this file share snapshots result: list snapshots and confirm the snapshot timestamp precedes the modification. It proves the outcome to capture a point-in-time, read-only view of share contents rather than an adjacent checkpoint.
- **D — Incorrect.** Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
  Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access. In the recoverable team file share, this check observes Azure Files network path. Azure Files network path success in recoverable team file share cannot verify file share snapshots; recoverable team file share cannot capture a point-in-time, read-only view of share contents until file share snapshots evidence exists.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Azure Files snapshots](https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files)

**Source reviewed:** 2026-08-31

## LAB09-Q28 — C

**Question:** The file-service acceptance log says the recoverable team file share can now restore a share removed during the service retention period. Which file-service acceptance state should the recoverable team file share acceptance test retain?

- **A — Incorrect.** Query share quota and access tier and compare them with the lab inputs.
  Query share quota and access tier and compare them with the lab inputs. In the recoverable team file share, this check observes file share quota. Recoverable team file share could pass file share quota while file share soft delete is wrong; recoverable team file share still lacks file share soft delete proof.
- **B — Incorrect.** List the principal's data-role assignment and confirm its scope includes the intended share.
  List the principal's data-role assignment and confirm its scope includes the intended share. In the recoverable team file share, this check observes share-level Azure RBAC. Recoverable team file share output covers share-level Azure RBAC, not file share soft delete; the file share soft delete requirement to restore a share removed during the service retention period remains unverified.
- **C — Correct.** Query shareDeleteRetentionPolicy and list the deleted share by name.
  Query shareDeleteRetentionPolicy and list the deleted share by name. This is independent file share soft delete evidence for the recoverable team file share, even if recoverable team file share setup reports success before file share soft delete becomes observable.
- **D — Incorrect.** List snapshots and confirm the snapshot timestamp precedes the modification.
  List snapshots and confirm the snapshot timestamp precedes the modification. In the recoverable team file share, this check observes file share snapshots. Recoverable team file share reads file share snapshots, leaving file share soft delete unproved in recoverable team file share; recoverable team file share still has no file share soft delete proof.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Prevent accidental deletion of Azure file shares](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion)

**Source reviewed:** 2026-08-31

## LAB09-Q29 — B

**Question:** The recoverable team file share rejects file-service acceptance exit status as proof it can transfer file-share content with a resumable command-line data mover. Which recoverable team file share result is valid evidence?

- **A — Incorrect.** Query enabledProtocols and confirm the client uses the matching mount protocol.
  Query enabledProtocols and confirm the client uses the matching mount protocol. In the recoverable team file share, this check observes SMB and NFS share protocols. Recoverable team file share output covers SMB and NFS share protocols, not AzCopy file transfers; the AzCopy file transfers requirement to transfer file-share content with a resumable command-line data mover remains unverified.
- **B — Correct.** Compare source and destination file counts, relative paths, lengths, and hashes where supported.
  Compare source and destination file counts, relative paths, lengths, and hashes where supported. For recoverable team file share, this AzCopy file transfers read confirms the service can transfer file-share content with a resumable command-line data mover.
- **C — Incorrect.** Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
  Verify the principal's role assignment and inspect the path ACL from a domain-connected client. In the recoverable team file share, this check observes file and directory ACLs. Recoverable team file share reads file and directory ACLs, leaving AzCopy file transfers unproved in recoverable team file share; recoverable team file share still has no AzCopy file transfers proof.
- **D — Incorrect.** Query shareDeleteRetentionPolicy and list the deleted share by name.
  Query shareDeleteRetentionPolicy and list the deleted share by name. In the recoverable team file share, this check observes file share soft delete. Recoverable team file share could pass file share soft delete while AzCopy file transfers is wrong; recoverable team file share still lacks AzCopy file transfers proof.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Use AzCopy with Azure Files](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files)

**Source reviewed:** 2026-08-31

## LAB09-Q30 — C

**Question:** The file-service acceptance validator needs one recoverable team file share query after the change to diagnose clients that cannot reach the SMB endpoint on its required port. Which file-service acceptance property should the recoverable team file share validator inspect?

- **A — Incorrect.** Query directoryServiceOptions and the account's identity configuration.
  Query directoryServiceOptions and the account's identity configuration. In the recoverable team file share, this check observes identity-based file authentication. Identity-based file authentication success in recoverable team file share cannot verify SMB port connectivity; recoverable team file share cannot diagnose clients that cannot reach the SMB endpoint on its required port until SMB port connectivity evidence exists.
- **B — Incorrect.** Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
  Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access. In the recoverable team file share, this check observes Azure Files network path. Recoverable team file share reads Azure Files network path, leaving SMB port connectivity unproved in recoverable team file share; recoverable team file share still has no SMB port connectivity proof.
- **C — Correct.** Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
  Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt. The recoverable team file share reads SMB port connectivity directly; that SMB port connectivity result proves the recoverable team file share can diagnose clients that cannot reach the SMB endpoint on its required port without another mutation.
- **D — Incorrect.** Compare source and destination file counts, relative paths, lengths, and hashes where supported.
  Compare source and destination file counts, relative paths, lengths, and hashes where supported. In the recoverable team file share, this check observes AzCopy file transfers. Recoverable team file share output covers AzCopy file transfers, not SMB port connectivity; the SMB port connectivity requirement to diagnose clients that cannot reach the SMB endpoint on its required port remains unverified.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Files SMB connectivity](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-storage/files/connectivity/files-troubleshoot-smb-connectivity)

**Source reviewed:** 2026-08-31

## LAB09-Q31 — D

**Question:** The recoverable team file share result is partial because the file-service acceptance cannot cap the capacity available to a team file share. Which condition accounts for that result?

- **A — Incorrect.** The share was created for NFS while the validation client attempts an SMB connection.
  The share was created for NFS while the validation client attempts an SMB connection. The recoverable team file share fault concerns SMB and NFS share protocols. Recoverable team file share has SMB and NFS share protocols impact, but file share quota is the recoverable team file share failed path; the SMB and NFS share protocols state cannot produce file share quota failure.
- **B — Incorrect.** The principal is authorized, but the client network blocks outbound SMB traffic.
  The principal is authorized, but the client network blocks outbound SMB traffic. The recoverable team file share fault concerns Azure Files network path. Recoverable team file share could repair Azure Files network path while file share quota stays broken in recoverable team file share; the recoverable team file share remains unable to cap the capacity available to a team file share.
- **C — Incorrect.** The client network provider blocks outbound TCP 445 to the storage endpoint.
  The client network provider blocks outbound TCP 445 to the storage endpoint. The recoverable team file share fault concerns SMB port connectivity. Recoverable team file share failed on file share quota; this SMB port connectivity finding redirects recoverable team file share remediation away from file share quota.
- **D — Correct.** The requested quota exceeds the supported limit for the selected account and share tier.
  For the recoverable team file share, the file share quota failure is causal: the requested quota exceeds the supported limit for the selected account and share tier. Correcting it restores the ability to cap the capacity available to a team file share.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Create an Azure file share](https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share)

**Source reviewed:** 2026-08-31

## LAB09-Q32 — A

**Question:** The file-service acceptance evidence shows the recoverable team file share cannot select the file-sharing protocol that matches the client workload. Which root cause fits that evidence?

- **A — Correct.** The share was created for NFS while the validation client attempts an SMB connection.
  The share was created for NFS while the validation client attempts an SMB connection. The finding is specific to SMB and NFS share protocols in the recoverable team file share; repairing SMB and NFS share protocols restores the recoverable team file share ability to select the file-sharing protocol that matches the client workload.
- **B — Incorrect.** The storage account has no configured directory service for SMB identity authentication.
  The storage account has no configured directory service for SMB identity authentication. The recoverable team file share fault concerns identity-based file authentication. Recoverable team file share failed on SMB and NFS share protocols; this identity-based file authentication finding redirects recoverable team file share remediation away from SMB and NFS share protocols.
- **C — Incorrect.** The snapshot was created after the unwanted file change and contains only the changed content.
  The snapshot was created after the unwanted file change and contains only the changed content. The recoverable team file share fault concerns file share snapshots. Recoverable team file share may fix file share snapshots, yet SMB and NFS share protocols still fails; this recoverable team file share diagnosis of file share snapshots is wrong for SMB and NFS share protocols.
- **D — Incorrect.** The requested quota exceeds the supported limit for the selected account and share tier.
  The requested quota exceeds the supported limit for the selected account and share tier. The recoverable team file share fault concerns file share quota. Recoverable team file share has file share quota impact, but SMB and NFS share protocols is the recoverable team file share failed path; the file share quota state cannot produce SMB and NFS share protocols failure.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Plan for an Azure Files deployment](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-planning)

**Source reviewed:** 2026-08-31

## LAB09-Q33 — B

**Question:** Although the recoverable team file share is meant to let the file-service acceptance authenticate file clients with an approved directory identity, its checkpoint fails. Which file-service acceptance defect explains the failure?

- **A — Incorrect.** The principal has Reader, which grants control-plane visibility but not SMB file data access.
  The principal has Reader, which grants control-plane visibility but not SMB file data access. The recoverable team file share fault concerns share-level Azure RBAC. Recoverable team file share failed on identity-based file authentication; this share-level Azure RBAC finding redirects recoverable team file share remediation away from identity-based file authentication.
- **B — Correct.** The storage account has no configured directory service for SMB identity authentication.
  The recoverable team file share cannot authenticate file clients with an approved directory identity because of this identity-based file authentication defect: the storage account has no configured directory service for SMB identity authentication. The symptom and repair align.
- **C — Incorrect.** Soft delete was disabled when the share was removed.
  Soft delete was disabled when the share was removed. The recoverable team file share fault concerns file share soft delete. Recoverable team file share has file share soft delete impact, but identity-based file authentication is the recoverable team file share failed path; the file share soft delete state cannot produce identity-based file authentication failure.
- **D — Incorrect.** The share was created for NFS while the validation client attempts an SMB connection.
  The share was created for NFS while the validation client attempts an SMB connection. The recoverable team file share fault concerns SMB and NFS share protocols. Recoverable team file share could repair SMB and NFS share protocols while identity-based file authentication stays broken in recoverable team file share; the recoverable team file share remains unable to authenticate file clients with an approved directory identity.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Identity-based authentication for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q34 — D

**Question:** The file-service acceptance support team isolated the recoverable team file share incident to the attempt to grant a principal access at the share boundary. Which condition prevents success?

- **A — Incorrect.** The user has a share-level role but the directory ACL denies the requested operation.
  The user has a share-level role but the directory ACL denies the requested operation. The recoverable team file share fault concerns file and directory ACLs. Recoverable team file share may fix file and directory ACLs, yet share-level Azure RBAC still fails; this recoverable team file share diagnosis of file and directory ACLs is wrong for share-level Azure RBAC.
- **B — Incorrect.** The SAS omits a permission required to create files in the destination share.
  The SAS omits a permission required to create files in the destination share. The recoverable team file share fault concerns AzCopy file transfers. Recoverable team file share has AzCopy file transfers impact, but share-level Azure RBAC is the recoverable team file share failed path; the AzCopy file transfers state cannot produce share-level Azure RBAC failure.
- **C — Incorrect.** The storage account has no configured directory service for SMB identity authentication.
  The storage account has no configured directory service for SMB identity authentication. The recoverable team file share fault concerns identity-based file authentication. Recoverable team file share could repair identity-based file authentication while share-level Azure RBAC stays broken in recoverable team file share; the recoverable team file share remains unable to grant a principal access at the share boundary.
- **D — Correct.** The principal has Reader, which grants control-plane visibility but not SMB file data access.
  The principal has Reader, which grants control-plane visibility but not SMB file data access. Removing this share-level Azure RBAC condition lets the recoverable team file share grant a principal access at the share boundary while leaving healthy controls unchanged.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Assign share-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-assign-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q35 — D

**Question:** A recoverable team file share query surprises the file-services administrator publishing a recoverable team share during the file-service acceptance attempt to limit access to particular directories and files after share access is granted. Which finding explains it?

- **A — Incorrect.** The principal is authorized, but the client network blocks outbound SMB traffic.
  The principal is authorized, but the client network blocks outbound SMB traffic. The recoverable team file share fault concerns Azure Files network path. Recoverable team file share has Azure Files network path impact, but file and directory ACLs is the recoverable team file share failed path; the Azure Files network path state cannot produce file and directory ACLs failure.
- **B — Incorrect.** The client network provider blocks outbound TCP 445 to the storage endpoint.
  The client network provider blocks outbound TCP 445 to the storage endpoint. The recoverable team file share fault concerns SMB port connectivity. Recoverable team file share could repair SMB port connectivity while file and directory ACLs stays broken in recoverable team file share; the recoverable team file share remains unable to limit access to particular directories and files after share access is granted.
- **C — Incorrect.** The principal has Reader, which grants control-plane visibility but not SMB file data access.
  The principal has Reader, which grants control-plane visibility but not SMB file data access. The recoverable team file share fault concerns share-level Azure RBAC. Recoverable team file share failed on file and directory ACLs; this share-level Azure RBAC finding redirects recoverable team file share remediation away from file and directory ACLs.
- **D — Correct.** The user has a share-level role but the directory ACL denies the requested operation.
  The user has a share-level role but the directory ACL denies the requested operation. In recoverable team file share, this file and directory ACLs cause matches the failure to limit access to particular directories and files after share access is granted.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Configure directory and file-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-configure-file-level-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q36 — C

**Question:** Other recoverable team file share components are healthy, but the file-service acceptance still cannot restrict share connectivity to the sanctioned route. Which state causes the isolated failure?

- **A — Incorrect.** The snapshot was created after the unwanted file change and contains only the changed content.
  The snapshot was created after the unwanted file change and contains only the changed content. The recoverable team file share fault concerns file share snapshots. Recoverable team file share could repair file share snapshots while Azure Files network path stays broken in recoverable team file share; the recoverable team file share remains unable to restrict share connectivity to the sanctioned route.
- **B — Incorrect.** The requested quota exceeds the supported limit for the selected account and share tier.
  The requested quota exceeds the supported limit for the selected account and share tier. The recoverable team file share fault concerns file share quota. Recoverable team file share failed on Azure Files network path; this file share quota finding redirects recoverable team file share remediation away from Azure Files network path.
- **C — Correct.** The principal is authorized, but the client network blocks outbound SMB traffic.
  The principal is authorized, but the client network blocks outbound SMB traffic. This recoverable team file share condition breaks Azure Files network path, explaining why operators cannot restrict share connectivity to the sanctioned route.
- **D — Incorrect.** The user has a share-level role but the directory ACL denies the requested operation.
  The user has a share-level role but the directory ACL denies the requested operation. The recoverable team file share fault concerns file and directory ACLs. Recoverable team file share has file and directory ACLs impact, but Azure Files network path is the recoverable team file share failed path; the file and directory ACLs state cannot produce Azure Files network path failure.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Azure Files networking considerations](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-networking-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q37 — B

**Question:** During a file-service acceptance fault drill, the recoverable team file share does not capture a point-in-time, read-only view of share contents. Which finding identifies the defect?

- **A — Incorrect.** Soft delete was disabled when the share was removed.
  Soft delete was disabled when the share was removed. The recoverable team file share fault concerns file share soft delete. Recoverable team file share failed on file share snapshots; this file share soft delete finding redirects recoverable team file share remediation away from file share snapshots.
- **B — Correct.** The snapshot was created after the unwanted file change and contains only the changed content.
  For the recoverable team file share, the file share snapshots failure is causal: the snapshot was created after the unwanted file change and contains only the changed content. Correcting it restores the ability to capture a point-in-time, read-only view of share contents.
- **C — Incorrect.** The share was created for NFS while the validation client attempts an SMB connection.
  The share was created for NFS while the validation client attempts an SMB connection. The recoverable team file share fault concerns SMB and NFS share protocols. Recoverable team file share has SMB and NFS share protocols impact, but file share snapshots is the recoverable team file share failed path; the SMB and NFS share protocols state cannot produce file share snapshots failure.
- **D — Incorrect.** The principal is authorized, but the client network blocks outbound SMB traffic.
  The principal is authorized, but the client network blocks outbound SMB traffic. The recoverable team file share fault concerns Azure Files network path. Recoverable team file share could repair Azure Files network path while file share snapshots stays broken in recoverable team file share; the recoverable team file share remains unable to capture a point-in-time, read-only view of share contents.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Azure Files snapshots](https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files)

**Source reviewed:** 2026-08-31

## LAB09-Q38 — B

**Question:** The recoverable team file share setup finishes, yet the file-service acceptance cannot restore a share removed during the service retention period. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The SAS omits a permission required to create files in the destination share.
  The SAS omits a permission required to create files in the destination share. The recoverable team file share fault concerns AzCopy file transfers. Recoverable team file share may fix AzCopy file transfers, yet file share soft delete still fails; this recoverable team file share diagnosis of AzCopy file transfers is wrong for file share soft delete.
- **B — Correct.** Soft delete was disabled when the share was removed.
  Soft delete was disabled when the share was removed. The finding is specific to file share soft delete in the recoverable team file share; repairing file share soft delete restores the recoverable team file share ability to restore a share removed during the service retention period.
- **C — Incorrect.** The storage account has no configured directory service for SMB identity authentication.
  The storage account has no configured directory service for SMB identity authentication. The recoverable team file share fault concerns identity-based file authentication. Recoverable team file share could repair identity-based file authentication while file share soft delete stays broken in recoverable team file share; the recoverable team file share remains unable to restore a share removed during the service retention period.
- **D — Incorrect.** The snapshot was created after the unwanted file change and contains only the changed content.
  The snapshot was created after the unwanted file change and contains only the changed content. The recoverable team file share fault concerns file share snapshots. Recoverable team file share failed on file share soft delete; this file share snapshots finding redirects recoverable team file share remediation away from file share soft delete.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Prevent accidental deletion of Azure file shares](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion)

**Source reviewed:** 2026-08-31

## LAB09-Q39 — B

**Question:** A file-service acceptance break/fix in the recoverable team file share fails when operators try to transfer file-share content with a resumable command-line data mover. Which diagnosis fits?

- **A — Incorrect.** The client network provider blocks outbound TCP 445 to the storage endpoint.
  The client network provider blocks outbound TCP 445 to the storage endpoint. The recoverable team file share fault concerns SMB port connectivity. Recoverable team file share has SMB port connectivity impact, but AzCopy file transfers is the recoverable team file share failed path; the SMB port connectivity state cannot produce AzCopy file transfers failure.
- **B — Correct.** The SAS omits a permission required to create files in the destination share.
  The recoverable team file share cannot transfer file-share content with a resumable command-line data mover because of this AzCopy file transfers defect: the SAS omits a permission required to create files in the destination share. The symptom and repair align.
- **C — Incorrect.** The principal has Reader, which grants control-plane visibility but not SMB file data access.
  The principal has Reader, which grants control-plane visibility but not SMB file data access. The recoverable team file share fault concerns share-level Azure RBAC. Recoverable team file share failed on AzCopy file transfers; this share-level Azure RBAC finding redirects recoverable team file share remediation away from AzCopy file transfers.
- **D — Incorrect.** Soft delete was disabled when the share was removed.
  Soft delete was disabled when the share was removed. The recoverable team file share fault concerns file share soft delete. Recoverable team file share may fix file share soft delete, yet AzCopy file transfers still fails; this recoverable team file share diagnosis of file share soft delete is wrong for AzCopy file transfers.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Use AzCopy with Azure Files](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files)

**Source reviewed:** 2026-08-31

## LAB09-Q40 — A

**Question:** The recoverable team file share troubleshooting scope is the file-service acceptance need to diagnose clients that cannot reach the SMB endpoint on its required port. Which condition should be corrected first?

- **A — Correct.** The client network provider blocks outbound TCP 445 to the storage endpoint.
  The client network provider blocks outbound TCP 445 to the storage endpoint. Removing this SMB port connectivity condition lets the recoverable team file share diagnose clients that cannot reach the SMB endpoint on its required port while leaving healthy controls unchanged.
- **B — Incorrect.** The requested quota exceeds the supported limit for the selected account and share tier.
  The requested quota exceeds the supported limit for the selected account and share tier. The recoverable team file share fault concerns file share quota. Recoverable team file share failed on SMB port connectivity; this file share quota finding redirects recoverable team file share remediation away from SMB port connectivity.
- **C — Incorrect.** The user has a share-level role but the directory ACL denies the requested operation.
  The user has a share-level role but the directory ACL denies the requested operation. The recoverable team file share fault concerns file and directory ACLs. Recoverable team file share may fix file and directory ACLs, yet SMB port connectivity still fails; this recoverable team file share diagnosis of file and directory ACLs is wrong for SMB port connectivity.
- **D — Incorrect.** The SAS omits a permission required to create files in the destination share.
  The SAS omits a permission required to create files in the destination share. The recoverable team file share fault concerns AzCopy file transfers. Recoverable team file share has AzCopy file transfers impact, but SMB port connectivity is the recoverable team file share failed path; the AzCopy file transfers state cannot produce SMB port connectivity failure.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Files SMB connectivity](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-storage/files/connectivity/files-troubleshoot-smb-connectivity)

**Source reviewed:** 2026-08-31

## LAB09-Q41 — A

**Question:** Which file-service acceptance path makes the recoverable team file share able to cap the capacity available to a team file share, then inspects the defining properties?

- **A — Correct.** First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs.
  First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs. For recoverable team file share, the file share quota operation precedes its file share quota read-back check, allowing it to cap the capacity available to a team file share.
- **B — Incorrect.** First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration.
  First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration. This recoverable team file share pair serves identity-based file authentication. Recoverable team file share proves identity-based file authentication, but file share quota lacks implementation in recoverable team file share and file share quota proof; the file share quota outcome to cap the capacity available to a team file share remains open.
- **C — Incorrect.** First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.
  First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification. This recoverable team file share pair serves file share snapshots. Recoverable team file share uses file share snapshots for both steps; file share quota remains untouched in recoverable team file share, so its file share quota gate to cap the capacity available to a team file share fails.
- **D — Incorrect.** First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.
  First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name. This recoverable team file share pair serves file share soft delete. Recoverable team file share closes file share soft delete, not file share quota; without the file share quota workflow, it cannot cap the capacity available to a team file share.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Create an Azure file share](https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share)

**Source reviewed:** 2026-08-31

## LAB09-Q42 — D

**Question:** At the recoverable team file share approval gate, operators must show that the file-service acceptance can select the file-sharing protocol that matches the client workload. Which file-service acceptance configure-and-check pair is defensible?

- **A — Incorrect.** First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share.
  First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share. This recoverable team file share pair serves share-level Azure RBAC. Recoverable team file share proves share-level Azure RBAC, but SMB and NFS share protocols lacks implementation in recoverable team file share and SMB and NFS share protocols proof; the SMB and NFS share protocols outcome to select the file-sharing protocol that matches the client workload remains open.
- **B — Incorrect.** First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.
  First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name. This recoverable team file share pair serves file share soft delete. Recoverable team file share uses file share soft delete for both steps; SMB and NFS share protocols remains untouched in recoverable team file share, so its SMB and NFS share protocols gate to select the file-sharing protocol that matches the client workload fails.
- **C — Incorrect.** First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
  First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported. This recoverable team file share pair serves AzCopy file transfers. Recoverable team file share closes AzCopy file transfers, not SMB and NFS share protocols; without the SMB and NFS share protocols workflow, it cannot select the file-sharing protocol that matches the client workload.
- **D — Correct.** First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol.
  First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol. In the recoverable team file share, the first SMB and NFS share protocols step runs; the recoverable team file share then reads SMB and NFS share protocols state to prove it can select the file-sharing protocol that matches the client workload.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Plan for an Azure Files deployment](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-planning)

**Source reviewed:** 2026-08-31

## LAB09-Q43 — C

**Question:** The recoverable team file share forbids a partial file-service acceptance result. Operators must first authenticate file clients with an approved directory identity and afterward confirm the recoverable team file share outcome. Which file-service acceptance sequence is complete?

- **A — Incorrect.** First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
  First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client. This recoverable team file share pair serves file and directory ACLs. Recoverable team file share uses file and directory ACLs for both steps; identity-based file authentication remains untouched in recoverable team file share, so its identity-based file authentication gate to authenticate file clients with an approved directory identity fails.
- **B — Incorrect.** First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
  First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported. This recoverable team file share pair serves AzCopy file transfers. Recoverable team file share closes AzCopy file transfers, not identity-based file authentication; without the identity-based file authentication workflow, it cannot authenticate file clients with an approved directory identity.
- **C — Correct.** First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration.
  For the recoverable team file share, the safe identity-based file authentication order is: first, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration. The recoverable team file share records identity-based file authentication proof after configuration.
- **D — Incorrect.** First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
  First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt. This recoverable team file share pair serves SMB port connectivity. Recoverable team file share proves SMB port connectivity, but identity-based file authentication lacks implementation in recoverable team file share and identity-based file authentication proof; the identity-based file authentication outcome to authenticate file clients with an approved directory identity remains open.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Identity-based authentication for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q44 — B

**Question:** Only the recoverable team file share change needed to grant a principal access at the share boundary is allowed, and file-service acceptance proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
  First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access. This recoverable team file share pair serves Azure Files network path. Recoverable team file share closes Azure Files network path, not share-level Azure RBAC; without the share-level Azure RBAC workflow, it cannot grant a principal access at the share boundary.
- **B — Correct.** First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share.
  First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share. The recoverable team file share uses its share-level Azure RBAC mutation gate and share-level Azure RBAC verification gate before it can grant a principal access at the share boundary.
- **C — Incorrect.** First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
  First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt. This recoverable team file share pair serves SMB port connectivity. Recoverable team file share proves SMB port connectivity, but share-level Azure RBAC lacks implementation in recoverable team file share and share-level Azure RBAC proof; the share-level Azure RBAC outcome to grant a principal access at the share boundary remains open.
- **D — Incorrect.** First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs.
  First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs. This recoverable team file share pair serves file share quota. Recoverable team file share uses file share quota for both steps; share-level Azure RBAC remains untouched in recoverable team file share, so its share-level Azure RBAC gate to grant a principal access at the share boundary fails.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Assign share-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-assign-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q45 — B

**Question:** The recoverable team file share runbook separates file-service acceptance mutation from validation while it must limit access to particular directories and files after share access is granted. Which sequence proves it cleanly?

- **A — Incorrect.** First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.
  First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification. This recoverable team file share pair serves file share snapshots. File share snapshots cannot replace file and directory ACLs in recoverable team file share. Use this file and directory ACLs pair instead: First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
- **B — Correct.** First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
  The recoverable team file share gets a complete file and directory ACLs sequence here: first, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client. Read-back evidence follows the change.
- **C — Incorrect.** First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs.
  First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs. This recoverable team file share pair serves file share quota. Recoverable team file share uses file share quota for both steps; file and directory ACLs remains untouched in recoverable team file share, so its file and directory ACLs gate to limit access to particular directories and files after share access is granted fails.
- **D — Incorrect.** First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol.
  First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol. This recoverable team file share pair serves SMB and NFS share protocols. Recoverable team file share closes SMB and NFS share protocols, not file and directory ACLs; without the file and directory ACLs workflow, it cannot limit access to particular directories and files after share access is granted.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Configure directory and file-level permissions for Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-configure-file-level-permissions)

**Source reviewed:** 2026-08-31

## LAB09-Q46 — D

**Question:** The recoverable team file share checkpoint requires both this file-service acceptance outcome—restrict share connectivity to the sanctioned route—and a read-only recoverable team file share state check. Which file-service acceptance response is complete?

- **A — Incorrect.** First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.
  First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name. This recoverable team file share pair serves file share soft delete. Recoverable team file share proves file share soft delete, but Azure Files network path lacks implementation in recoverable team file share and Azure Files network path proof; the Azure Files network path outcome to restrict share connectivity to the sanctioned route remains open.
- **B — Incorrect.** First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol.
  First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol. This recoverable team file share pair serves SMB and NFS share protocols. Recoverable team file share uses SMB and NFS share protocols for both steps; Azure Files network path remains untouched in recoverable team file share, so its Azure Files network path gate to restrict share connectivity to the sanctioned route fails.
- **C — Incorrect.** First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration.
  First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration. This recoverable team file share pair serves identity-based file authentication. Recoverable team file share closes identity-based file authentication, not Azure Files network path; without the Azure Files network path workflow, it cannot restrict share connectivity to the sanctioned route.
- **D — Correct.** First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
  First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access. This ordered Azure Files network path workflow lets the recoverable team file share restrict share connectivity to the sanctioned route and then verify the resulting state.

**Objectives:** `ST-ACCESS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB09-CP01`).

**Microsoft Learn sources:**

- [Azure Files networking considerations](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-networking-overview)

**Source reviewed:** 2026-08-31

## LAB09-Q47 — D

**Question:** The recoverable team file share runbook must capture a point-in-time, read-only view of share contents, then retain file-service acceptance read-back evidence. Which recoverable team file share pair completes both duties?

- **A — Incorrect.** First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
  First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported. This recoverable team file share pair serves AzCopy file transfers. Recoverable team file share uses AzCopy file transfers for both steps; file share snapshots remains untouched in recoverable team file share, so its file share snapshots gate to capture a point-in-time, read-only view of share contents fails.
- **B — Incorrect.** First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration.
  First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration. This recoverable team file share pair serves identity-based file authentication. Recoverable team file share closes identity-based file authentication, not file share snapshots; without the file share snapshots workflow, it cannot capture a point-in-time, read-only view of share contents.
- **C — Incorrect.** First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share.
  First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share. This recoverable team file share pair serves share-level Azure RBAC. Share-level Azure RBAC cannot replace file share snapshots in recoverable team file share. Use this file share snapshots pair instead: First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.
- **D — Correct.** First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.
  First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification. For recoverable team file share, the file share snapshots operation precedes its file share snapshots read-back check, allowing it to capture a point-in-time, read-only view of share contents.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB09-CP02`).

**Microsoft Learn sources:**

- [Azure Files snapshots](https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files)

**Source reviewed:** 2026-08-31

## LAB09-Q48 — A

**Question:** To satisfy the file-service acceptance requirement, operators must change the recoverable team file share configuration and prove it can restore a share removed during the service retention period. Which sequence is coherent?

- **A — Correct.** First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.
  First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name. In the recoverable team file share, the first file share soft delete step runs; the recoverable team file share then reads file share soft delete state to prove it can restore a share removed during the service retention period.
- **B — Incorrect.** First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
  First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt. This recoverable team file share pair serves SMB port connectivity. SMB port connectivity cannot replace file share soft delete in recoverable team file share. Use this file share soft delete pair instead: First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.
- **C — Incorrect.** First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share.
  First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share. This recoverable team file share pair serves share-level Azure RBAC. Recoverable team file share proves share-level Azure RBAC, but file share soft delete lacks implementation in recoverable team file share and file share soft delete proof; the file share soft delete outcome to restore a share removed during the service retention period remains open.
- **D — Incorrect.** First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
  First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client. This recoverable team file share pair serves file and directory ACLs. Recoverable team file share uses file and directory ACLs for both steps; file share soft delete remains untouched in recoverable team file share, so its file share soft delete gate to restore a share removed during the service retention period fails.

**Objectives:** `ST-DATA-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB09-CP03`).

**Microsoft Learn sources:**

- [Prevent accidental deletion of Azure file shares](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion)

**Source reviewed:** 2026-08-31

## LAB09-Q49 — B

**Question:** The file-services administrator publishing a recoverable team share needs a safe recoverable team file share change to transfer file-share content with a resumable command-line data mover, followed by file-service acceptance evidence. Which pair merits approval?

- **A — Incorrect.** First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs.
  First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs. This recoverable team file share pair serves file share quota. File share quota cannot replace AzCopy file transfers in recoverable team file share. Use this AzCopy file transfers pair instead: First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
- **B — Correct.** First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
  For the recoverable team file share, the safe AzCopy file transfers order is: first, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported. The recoverable team file share records AzCopy file transfers proof after configuration.
- **C — Incorrect.** First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
  First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client. This recoverable team file share pair serves file and directory ACLs. Recoverable team file share uses file and directory ACLs for both steps; AzCopy file transfers remains untouched in recoverable team file share, so its AzCopy file transfers gate to transfer file-share content with a resumable command-line data mover fails.
- **D — Incorrect.** First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
  First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access. This recoverable team file share pair serves Azure Files network path. Recoverable team file share closes Azure Files network path, not AzCopy file transfers; without the AzCopy file transfers workflow, it cannot transfer file-share content with a resumable command-line data mover.

**Objectives:** `ST-ACCOUNTS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB09-CP04`).

**Microsoft Learn sources:**

- [Use AzCopy with Azure Files](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files)

**Source reviewed:** 2026-08-31

## LAB09-Q50 — B

**Question:** The recoverable team file share has two file-service acceptance gates: diagnose clients that cannot reach the SMB endpoint on its required port, then prove the recoverable team file share state. Which file-service acceptance sequence works?

- **A — Incorrect.** First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol.
  First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol. This recoverable team file share pair serves SMB and NFS share protocols. Recoverable team file share proves SMB and NFS share protocols, but SMB port connectivity lacks implementation in recoverable team file share and SMB port connectivity proof; the SMB port connectivity outcome to diagnose clients that cannot reach the SMB endpoint on its required port remains open.
- **B — Correct.** First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
  First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt. The recoverable team file share uses its SMB port connectivity mutation gate and SMB port connectivity verification gate before it can diagnose clients that cannot reach the SMB endpoint on its required port.
- **C — Incorrect.** First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
  First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access. This recoverable team file share pair serves Azure Files network path. Recoverable team file share closes Azure Files network path, not SMB port connectivity; without the SMB port connectivity workflow, it cannot diagnose clients that cannot reach the SMB endpoint on its required port.
- **D — Incorrect.** First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.
  First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification. This recoverable team file share pair serves file share snapshots. File share snapshots cannot replace SMB port connectivity in recoverable team file share. Use this SMB port connectivity pair instead: First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.

**Objectives:** `ST-DATA-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB09-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Files SMB connectivity](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-storage/files/connectivity/files-troubleshoot-smb-connectivity)

**Source reviewed:** 2026-08-31
