# Lab 06 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB06-Q01 — Foundational

A new storage hardening operator must explain why the hardened general-purpose storage account can create the general-purpose account type that supports current storage services. Which explanation is accurate?

- A. A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers.
- B. A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features.
- C. RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally.
- D. Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism.

## LAB06-Q02 — Foundational

The hardened general-purpose storage account acceptance criteria require operators to produce a globally unique lowercase account name with no punctuation. Which service fact supports that requirement?

- A. LRS keeps three synchronous copies within one physical location in the primary region.
- B. Secure transfer required rejects supported storage requests made over unencrypted HTTP.
- C. Rotating one storage key at a time preserves a second valid key for applications during rollover.
- D. A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers.

## LAB06-Q03 — Foundational

A storage hardening reviewer challenges whether the hardened general-purpose storage account can replicate data synchronously three ways at a single site. Which response resolves the concern?

- A. LRS keeps three synchronous copies within one physical location in the primary region.
- B. ZRS synchronously replicates data across availability zones in the primary region.
- C. The minimum TLS setting rejects client connections that negotiate an older protocol version.
- D. Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys.

## LAB06-Q04 — Foundational

The hardened general-purpose storage account handoff omits the storage hardening rule needed to survive a single availability-zone failure within the primary region. Which statement should the team add?

- A. RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally.
- B. ZRS synchronously replicates data across availability zones in the primary region.
- C. Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism.
- D. A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features.

## LAB06-Q05 — Foundational

A storage hardening incident review of the hardened general-purpose storage account depends on the ability to allow reads from the secondary region when geo-replicated data is available. Which platform description is reliable?

- A. Secure transfer required rejects supported storage requests made over unencrypted HTTP.
- B. Rotating one storage key at a time preserves a second valid key for applications during rollover.
- C. RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally.
- D. A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers.

## LAB06-Q06 — Foundational

A storage administrator hardening a general-purpose account is updating the storage hardening runbook. The requirement is to reject storage requests that do not use an encrypted transport. Which statement describes Azure behavior correctly?

- A. The minimum TLS setting rejects client connections that negotiate an older protocol version.
- B. Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys.
- C. Secure transfer required rejects supported storage requests made over unencrypted HTTP.
- D. LRS keeps three synchronous copies within one physical location in the primary region.

## LAB06-Q07 — Foundational

A storage hardening peer review asks how the hardened general-purpose storage account should handle this outcome: refuse clients that negotiate an obsolete transport protocol. Which explanation is accurate?

- A. Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism.
- B. The minimum TLS setting rejects client connections that negotiate an older protocol version.
- C. A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features.
- D. ZRS synchronously replicates data across availability zones in the primary region.

## LAB06-Q08 — Foundational

For the hardened general-purpose storage account, the storage hardening plan must accept only Microsoft Entra credentials for data access. Which statement about storage hardening belongs in the hardened general-purpose storage account record?

- A. Rotating one storage key at a time preserves a second valid key for applications during rollover.
- B. A storage account name is globally unique, 3–24 characters, and contains only lowercase letters and numbers.
- C. Disabling shared-key authorization forces supported data operations to use Microsoft Entra authorization or another approved mechanism.
- D. RA-GRS adds a readable secondary endpoint to geo-redundant replication, while GRS does not expose secondary reads normally.

## LAB06-Q09 — Foundational

The storage hardening review compares four claims for the hardened general-purpose storage account requirement to replace a compromised credential without losing the second recovery credential. Which claim is technically sound?

- A. Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys.
- B. Rotating one storage key at a time preserves a second valid key for applications during rollover.
- C. LRS keeps three synchronous copies within one physical location in the primary region.
- D. Secure transfer required rejects supported storage requests made over unencrypted HTTP.

## LAB06-Q10 — Foundational

The storage hardening architecture note requires the hardened general-purpose storage account environment to confirm that stored service data is encrypted without an application change. Which statement defines the relevant storage hardening boundary?

- A. A StorageV2 account supports current Blob, Files, Queue, and Table capabilities and access-tier features.
- B. ZRS synchronously replicates data across availability zones in the primary region.
- C. The minimum TLS setting rejects client connections that negotiate an older protocol version.
- D. Azure Storage encrypts persisted data by default and can use Microsoft-managed or customer-managed keys.

## LAB06-Q11 — Foundational

Operators must automate the hardened general-purpose storage account change needed to create the general-purpose account type that supports current storage services. Which storage hardening operation belongs in the runbook?

- A. Create a standard StorageV2 account unless a workload-specific account kind is required.
- B. Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required.
- C. Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists.
- D. Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation.

## LAB06-Q12 — Foundational

A hardened general-purpose storage account review finds storage hardening drift from the need to produce a globally unique lowercase account name with no punctuation. Which correction addresses that drift?

- A. Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication.
- B. Set minimumTlsVersion to TLS1_2 or the approved stronger baseline.
- C. Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key.
- D. Generate a deterministic lowercase name and check global availability before deployment.

## LAB06-Q13 — Foundational

The hardened general-purpose storage account window permits only the storage hardening change needed to replicate data synchronously three ways at a single site. Which option respects the boundary?

- A. Choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
- B. Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization.
- C. Create a standard StorageV2 account unless a workload-specific account kind is required.
- D. Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required.

## LAB06-Q14 — Foundational

The storage hardening preflight has passed; the hardened general-purpose storage account must now survive a single availability-zone failure within the primary region. Which operation should run?

- A. Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists.
- B. Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation.
- C. Generate a deterministic lowercase name and check global availability before deployment.
- D. Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication.

## LAB06-Q15 — Foundational

The hardened general-purpose storage account plan must allow reads from the secondary region when geo-replicated data is available while limiting the mutation scope to storage hardening. Which action is appropriate?

- A. Set minimumTlsVersion to TLS1_2 or the approved stronger baseline.
- B. Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key.
- C. Choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
- D. Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required.

## LAB06-Q16 — Applied

A storage hardening ticket in the hardened general-purpose storage account says to reject storage requests that do not use an encrypted transport. Which storage hardening action completes the hardened general-purpose storage account request with minimal change?

- A. Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization.
- B. Create a standard StorageV2 account unless a workload-specific account kind is required.
- C. Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists.
- D. Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication.

## LAB06-Q17 — Applied

The approach for the hardened general-purpose storage account is approved, but the storage hardening environment still cannot refuse clients that negotiate an obsolete transport protocol. Which implementation step closes the gap?

- A. Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation.
- B. Generate a deterministic lowercase name and check global availability before deployment.
- C. Choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
- D. Set minimumTlsVersion to TLS1_2 or the approved stronger baseline.

## LAB06-Q18 — Applied

The storage administrator hardening a general-purpose account may change the hardened general-purpose storage account only to accept only Microsoft Entra credentials for data access. Which storage hardening action stays within that assignment?

- A. Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key.
- B. Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required.
- C. Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization.
- D. Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists.

## LAB06-Q19 — Applied

A storage hardening dry run shows no hardened general-purpose storage account command will replace a compromised credential without losing the second recovery credential. Which action belongs before execution?

- A. Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation.
- B. Create a standard StorageV2 account unless a workload-specific account kind is required.
- C. Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication.
- D. Set minimumTlsVersion to TLS1_2 or the approved stronger baseline.

## LAB06-Q20 — Applied

For the hardened general-purpose storage account, operators need to confirm that stored service data is encrypted without an application change. Which change realizes that requirement?

- A. Generate a deterministic lowercase name and check global availability before deployment.
- B. Choose an RA geo-redundant SKU only when the application needs read access to the secondary region.
- C. Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key.
- D. Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization.

## LAB06-Q21 — Applied

The hardened general-purpose storage account configuration is complete; the storage hardening reviewers need evidence it can create the general-purpose account type that supports current storage services. Which observation shows success?

- A. Query kind, sku, primaryEndpoints, and provisioningState for the created account.
- B. Query the account SKU and verify Standard_ZRS is supported in the selected region.
- C. Query minimumTlsVersion and compare it with the security standard.
- D. Query encryption keySource and service encryption settings for Blob and Files.

## LAB06-Q22 — Applied

The storage hardening validation asks whether the hardened general-purpose storage account can produce a globally unique lowercase account name with no punctuation. Which observable state is strongest?

- A. Use the name-availability API and confirm nameAvailable is true before creation.
- B. Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
- C. Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
- D. Query kind, sku, primaryEndpoints, and provisioningState for the created account.

## LAB06-Q23 — Applied

A hardened general-purpose storage account review must prove the storage hardening ability to replicate data synchronously three ways at a single site. Which check avoids an adjacent feature?

- A. Query enableHttpsTrafficOnly and confirm it is true.
- B. Query the account SKU and confirm its name is Standard_LRS.
- C. List key creation times and verify applications no longer use the key scheduled for regeneration.
- D. Use the name-availability API and confirm nameAvailable is true before creation.

## LAB06-Q24 — Applied

The hardened general-purpose storage account evidence bundle needs a storage hardening result showing it can survive a single availability-zone failure within the primary region. Which result belongs in the checkpoint?

- A. Query the account SKU and verify Standard_ZRS is supported in the selected region.
- B. Query minimumTlsVersion and compare it with the security standard.
- C. Query encryption keySource and service encryption settings for Blob and Files.
- D. Query the account SKU and confirm its name is Standard_LRS.

## LAB06-Q25 — Applied

Before hardened general-purpose storage account cleanup, the storage hardening team must reconfirm it can allow reads from the secondary region when geo-replicated data is available. Which read-only inspection should run?

- A. Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
- B. Query kind, sku, primaryEndpoints, and provisioningState for the created account.
- C. Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
- D. Query the account SKU and verify Standard_ZRS is supported in the selected region.

## LAB06-Q26 — Applied

The hardened general-purpose storage account setup reports success after the storage hardening attempt to reject storage requests that do not use an encrypted transport. Which storage hardening read-only observation proves the hardened general-purpose storage account outcome?

- A. List key creation times and verify applications no longer use the key scheduled for regeneration.
- B. Use the name-availability API and confirm nameAvailable is true before creation.
- C. Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
- D. Query enableHttpsTrafficOnly and confirm it is true.

## LAB06-Q27 — Applied

The storage hardening log says the hardened general-purpose storage account can now refuse clients that negotiate an obsolete transport protocol. Which storage hardening state should the hardened general-purpose storage account acceptance test retain?

- A. Query encryption keySource and service encryption settings for Blob and Files.
- B. Query the account SKU and confirm its name is Standard_LRS.
- C. Query minimumTlsVersion and compare it with the security standard.
- D. Query enableHttpsTrafficOnly and confirm it is true.

## LAB06-Q28 — Applied

The hardened general-purpose storage account rejects storage hardening exit status as proof it can accept only Microsoft Entra credentials for data access. Which hardened general-purpose storage account result is valid evidence?

- A. Query kind, sku, primaryEndpoints, and provisioningState for the created account.
- B. Query the account SKU and verify Standard_ZRS is supported in the selected region.
- C. Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
- D. Query minimumTlsVersion and compare it with the security standard.

## LAB06-Q29 — Applied

The storage hardening validator needs one hardened general-purpose storage account query after the change to replace a compromised credential without losing the second recovery credential. Which storage hardening property should the hardened general-purpose storage account validator inspect?

- A. Use the name-availability API and confirm nameAvailable is true before creation.
- B. Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
- C. Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
- D. List key creation times and verify applications no longer use the key scheduled for regeneration.

## LAB06-Q30 — Applied

The storage administrator hardening a general-purpose account must confirm the hardened general-purpose storage account, without mutation, can confirm that stored service data is encrypted without an application change. Which storage hardening check qualifies?

- A. Query the account SKU and confirm its name is Standard_LRS.
- B. Query encryption keySource and service encryption settings for Blob and Files.
- C. Query enableHttpsTrafficOnly and confirm it is true.
- D. List key creation times and verify applications no longer use the key scheduled for regeneration.

## LAB06-Q31 — Applied

The storage hardening evidence shows the hardened general-purpose storage account cannot create the general-purpose account type that supports current storage services. Which root cause fits that evidence?

- A. The account uses a legacy kind that does not support the requested modern storage capability.
- B. The proposed account name contains a hyphen and therefore violates the naming rules.
- C. Secure transfer was disabled to accommodate an obsolete HTTP client.
- D. Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions.

## LAB06-Q32 — Applied

Although the hardened general-purpose storage account is meant to let the storage hardening produce a globally unique lowercase account name with no punctuation, its checkpoint fails. Which storage hardening defect explains the failure?

- A. The proposed account name contains a hyphen and therefore violates the naming rules.
- B. The design requires zone-level resilience that LRS does not provide.
- C. The client only supports a TLS version lower than the account's configured minimum.
- D. The account uses a legacy kind that does not support the requested modern storage capability.

## LAB06-Q33 — Applied

The storage hardening support team isolated the hardened general-purpose storage account incident to the attempt to replicate data synchronously three ways at a single site. Which condition prevents success?

- A. The selected region or account feature does not support the requested ZRS combination.
- B. The workload still depends on an account key after shared-key authorization was disabled.
- C. The proposed account name contains a hyphen and therefore violates the naming rules.
- D. The design requires zone-level resilience that LRS does not provide.

## LAB06-Q34 — Applied

A hardened general-purpose storage account query surprises the storage administrator hardening a general-purpose account during the storage hardening attempt to survive a single availability-zone failure within the primary region. Which finding explains it?

- A. The selected region or account feature does not support the requested ZRS combination.
- B. The account uses GRS, so applications cannot normally read from the secondary endpoint.
- C. The active key was regenerated before dependent applications switched to the alternate key.
- D. The design requires zone-level resilience that LRS does not provide.

## LAB06-Q35 — Applied

Other hardened general-purpose storage account components are healthy, but the storage hardening still cannot allow reads from the secondary region when geo-replicated data is available. Which state causes the isolated failure?

- A. The account uses GRS, so applications cannot normally read from the secondary endpoint.
- B. Secure transfer was disabled to accommodate an obsolete HTTP client.
- C. Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions.
- D. The selected region or account feature does not support the requested ZRS combination.

## LAB06-Q36 — Applied

During a storage hardening fault drill, the hardened general-purpose storage account does not reject storage requests that do not use an encrypted transport. Which finding identifies the defect?

- A. The client only supports a TLS version lower than the account's configured minimum.
- B. The account uses a legacy kind that does not support the requested modern storage capability.
- C. The account uses GRS, so applications cannot normally read from the secondary endpoint.
- D. Secure transfer was disabled to accommodate an obsolete HTTP client.

## LAB06-Q37 — Applied

The hardened general-purpose storage account setup finishes, yet the storage hardening cannot refuse clients that negotiate an obsolete transport protocol. Which misconfiguration explains the mismatch?

- A. The workload still depends on an account key after shared-key authorization was disabled.
- B. The proposed account name contains a hyphen and therefore violates the naming rules.
- C. The client only supports a TLS version lower than the account's configured minimum.
- D. Secure transfer was disabled to accommodate an obsolete HTTP client.

## LAB06-Q38 — Applied

A storage hardening break/fix in the hardened general-purpose storage account fails when operators try to accept only Microsoft Entra credentials for data access. Which diagnosis fits?

- A. The active key was regenerated before dependent applications switched to the alternate key.
- B. The workload still depends on an account key after shared-key authorization was disabled.
- C. The design requires zone-level resilience that LRS does not provide.
- D. The client only supports a TLS version lower than the account's configured minimum.

## LAB06-Q39 — Applied

The hardened general-purpose storage account troubleshooting scope is the storage hardening need to replace a compromised credential without losing the second recovery credential. Which condition should be corrected first?

- A. The active key was regenerated before dependent applications switched to the alternate key.
- B. Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions.
- C. The selected region or account feature does not support the requested ZRS combination.
- D. The workload still depends on an account key after shared-key authorization was disabled.

## LAB06-Q40 — Applied

The hardened general-purpose storage account result is partial because the storage hardening cannot confirm that stored service data is encrypted without an application change. Which condition accounts for that result?

- A. The account uses a legacy kind that does not support the requested modern storage capability.
- B. Customer-managed encryption cannot unwrap the key because the storage account identity lacks key permissions.
- C. The account uses GRS, so applications cannot normally read from the secondary endpoint.
- D. The active key was regenerated before dependent applications switched to the alternate key.

## LAB06-Q41 — Advanced

At the hardened general-purpose storage account approval gate, operators must show that the storage hardening can create the general-purpose account type that supports current storage services. Which storage hardening configure-and-check pair is defensible?

- A. First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.
- B. First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
- C. First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
- D. First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.

## LAB06-Q42 — Advanced

The hardened general-purpose storage account forbids a partial storage hardening result. Operators must first produce a globally unique lowercase account name with no punctuation and afterward confirm the hardened general-purpose storage account outcome. Which storage hardening sequence is complete?

- A. First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region.
- B. First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
- C. First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.
- D. First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.

## LAB06-Q43 — Advanced

Only the hardened general-purpose storage account change needed to replicate data synchronously three ways at a single site is allowed, and storage hardening proof is mandatory. Which pair fits?

- A. First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.
- B. First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
- C. First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.
- D. First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files.

## LAB06-Q44 — Advanced

The hardened general-purpose storage account runbook separates storage hardening mutation from validation while it must survive a single availability-zone failure within the primary region. Which sequence proves it cleanly?

- A. First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.
- B. First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region.
- C. First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files.
- D. First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.

## LAB06-Q45 — Advanced

The hardened general-purpose storage account checkpoint requires both this storage hardening outcome—allow reads from the secondary region when geo-replicated data is available—and a read-only hardened general-purpose storage account state check. Which storage hardening response is complete?

- A. First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
- B. First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
- C. First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.
- D. First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.

## LAB06-Q46 — Advanced

The hardened general-purpose storage account runbook must reject storage requests that do not use an encrypted transport, then retain storage hardening read-back evidence. Which hardened general-purpose storage account pair completes both duties?

- A. First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.
- B. First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
- C. First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.
- D. First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.

## LAB06-Q47 — Advanced

To satisfy the storage hardening requirement, operators must change the hardened general-purpose storage account configuration and prove it can refuse clients that negotiate an obsolete transport protocol. Which sequence is coherent?

- A. First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.
- B. First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
- C. First, Choose Standard_LRS when lowest redundancy cost is accepted and zone failure protection is not required. Then, Query the account SKU and confirm its name is Standard_LRS.
- D. First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region.

## LAB06-Q48 — Advanced

The storage administrator hardening a general-purpose account needs a safe hardened general-purpose storage account change to accept only Microsoft Entra credentials for data access, followed by storage hardening evidence. Which pair merits approval?

- A. First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files.
- B. First, Disable allowSharedKeyAccess after confirming every required workload supports identity-based authorization. Then, Query allowSharedKeyAccess and test a Microsoft Entra data-plane request independently.
- C. First, Choose Standard_ZRS when the workload must tolerate a zonal failure without regional replication. Then, Query the account SKU and verify Standard_ZRS is supported in the selected region.
- D. First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.

## LAB06-Q49 — Advanced

The hardened general-purpose storage account has two storage hardening gates: replace a compromised credential without losing the second recovery credential, then prove the hardened general-purpose storage account state. Which storage hardening sequence works?

- A. First, Create a standard StorageV2 account unless a workload-specific account kind is required. Then, Query kind, sku, primaryEndpoints, and provisioningState for the created account.
- B. First, Move clients to the secondary key, regenerate the primary key, and then complete the inverse rotation. Then, List key creation times and verify applications no longer use the key scheduled for regeneration.
- C. First, Choose an RA geo-redundant SKU only when the application needs read access to the secondary region. Then, Query secondary endpoints and the account SKU to confirm read-access geo-redundancy.
- D. First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.

## LAB06-Q50 — Advanced

Which storage hardening path makes the hardened general-purpose storage account able to confirm that stored service data is encrypted without an application change, then inspects the defining properties?

- A. First, Generate a deterministic lowercase name and check global availability before deployment. Then, Use the name-availability API and confirm nameAvailable is true before creation.
- B. First, Enable supportsHttpsTrafficOnly on every account unless a documented legacy exception exists. Then, Query enableHttpsTrafficOnly and confirm it is true.
- C. First, Set minimumTlsVersion to TLS1_2 or the approved stronger baseline. Then, Query minimumTlsVersion and compare it with the security standard.
- D. First, Select the approved key source and, for customer-managed keys, grant the account identity access to the key vault key. Then, Query encryption keySource and service encryption settings for Blob and Files.

[Open the answer key](./ANSWERS.md)
