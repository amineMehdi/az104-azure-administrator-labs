# Lab 08 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB08-Q01 — Foundational

A blob retention peer review asks how the blob retention and replication service should handle this outcome: keep private data from being read without an authorization header. Which explanation is accurate?

- A. Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics.
- B. A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls.
- C. A lifecycle delete action permanently removes eligible current or previous versions after its age condition.
- D. Blob versioning preserves a new immutable version when a block blob is modified or deleted.

## LAB08-Q02 — Foundational

For the blob retention and replication service, the blob retention plan must place frequently read and rarely read blobs in cost-appropriate tiers. Which statement about blob retention belongs in the blob retention and replication service record?

- A. Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters.
- B. Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.
- C. Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements.
- D. Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics.

## LAB08-Q03 — Foundational

The blob retention review compares four claims for the blob retention and replication service requirement to apply retention automation only to blobs matching the intended prefix or type. Which claim is technically sound?

- A. Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access.
- B. Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters.
- C. Container soft delete protects a deleted container and its contents for a separate configured retention period.
- D. AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items.

## LAB08-Q04 — Foundational

The blob retention architecture note requires the blob retention and replication service environment to move eligible data to a cooler tier after the configured age. Which statement defines the relevant blob retention boundary?

- A. A lifecycle delete action permanently removes eligible current or previous versions after its age condition.
- B. Blob versioning preserves a new immutable version when a block blob is modified or deleted.
- C. Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access.
- D. A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls.

## LAB08-Q05 — Foundational

A new blob retention operator must explain why the blob retention and replication service can delete only objects that satisfy the retention rule's age conditions. Which explanation is accurate?

- A. Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.
- B. Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements.
- C. A lifecycle delete action permanently removes eligible current or previous versions after its age condition.
- D. Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics.

## LAB08-Q06 — Foundational

The blob retention and replication service acceptance criteria require operators to recover a blob deleted after data protection was enabled. Which service fact supports that requirement?

- A. Container soft delete protects a deleted container and its contents for a separate configured retention period.
- B. AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items.
- C. Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters.
- D. Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.

## LAB08-Q07 — Foundational

A blob retention reviewer challenges whether the blob retention and replication service can recover a container removed during its retention window. Which response resolves the concern?

- A. Blob versioning preserves a new immutable version when a block blob is modified or deleted.
- B. A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls.
- C. Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access.
- D. Container soft delete protects a deleted container and its contents for a separate configured retention period.

## LAB08-Q08 — Foundational

The blob retention and replication service handoff omits the blob retention rule needed to retain an earlier block-blob state after a write or deletion. Which statement should the team add?

- A. Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements.
- B. Hot, cool, cold, and archive tiers trade storage cost against access and rehydration characteristics.
- C. A lifecycle delete action permanently removes eligible current or previous versions after its age condition.
- D. Blob versioning preserves a new immutable version when a block blob is modified or deleted.

## LAB08-Q09 — Foundational

A blob retention incident review of the blob retention and replication service depends on the ability to copy supported block-blob changes asynchronously to a second account. Which platform description is reliable?

- A. AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items.
- B. Lifecycle rules can target blobs by prefix, blob type, and supported blob index tag filters.
- C. Object replication asynchronously copies block blobs between source and destination accounts and depends on versioning and change feed requirements.
- D. Blob soft delete retains deleted blobs and versions for the configured retention period so they can be undeleted.

## LAB08-Q10 — Foundational

A data-platform administrator managing blob retention and replication is updating the blob retention runbook. The requirement is to copy a directory safely without deleting unrelated destination data. Which statement describes Azure behavior correctly?

- A. A blob container organizes blobs inside one storage account and its public access setting is independent of account authorization controls.
- B. AzCopy copy transfers selected data, while sync compares source and destination and can optionally delete destination-only items.
- C. Lifecycle age conditions can tier a current blob version after the configured number of days since modification or access.
- D. Container soft delete protects a deleted container and its contents for a separate configured retention period.

## LAB08-Q11 — Foundational

The approach for the blob retention and replication service is approved, but the blob retention environment still cannot keep private data from being read without an authorization header. Which implementation step closes the gap?

- A. Create the container with private access unless anonymous blob access is explicitly required.
- B. Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions.
- C. Enable blob soft delete with the approved retention days before testing deletion recovery.
- D. Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules.

## LAB08-Q12 — Foundational

The data-platform administrator managing blob retention and replication may change the blob retention and replication service only to place frequently read and rarely read blobs in cost-appropriate tiers. Which blob retention action stays within that assignment?

- A. Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition.
- B. Enable container delete retention and use a unique test container for recovery validation.
- C. Choose the tier from observed access frequency, retention period, and retrieval-time requirements.
- D. Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation.

## LAB08-Q13 — Foundational

A blob retention dry run shows no blob retention and replication service command will apply retention automation only to blobs matching the intended prefix or type. Which action belongs before execution?

- A. Use a delete action only after data-protection retention and legal requirements are satisfied.
- B. Enable versioning before overwriting the test blob and persist the returned version IDs.
- C. Create the container with private access unless anonymous blob access is explicitly required.
- D. Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions.

## LAB08-Q14 — Foundational

For the blob retention and replication service, operators need to move eligible data to a cooler tier after the configured age. Which change realizes that requirement?

- A. Enable blob soft delete with the approved retention days before testing deletion recovery.
- B. Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition.
- C. Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules.
- D. Choose the tier from observed access frequency, retention period, and retrieval-time requirements.

## LAB08-Q15 — Foundational

Operators must automate the blob retention and replication service change needed to delete only objects that satisfy the retention rule's age conditions. Which blob retention operation belongs in the runbook?

- A. Enable container delete retention and use a unique test container for recovery validation.
- B. Use a delete action only after data-protection retention and legal requirements are satisfied.
- C. Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation.
- D. Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions.

## LAB08-Q16 — Applied

A blob retention and replication service review finds blob retention drift from the need to recover a blob deleted after data protection was enabled. Which correction addresses that drift?

- A. Enable versioning before overwriting the test blob and persist the returned version IDs.
- B. Create the container with private access unless anonymous blob access is explicitly required.
- C. Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition.
- D. Enable blob soft delete with the approved retention days before testing deletion recovery.

## LAB08-Q17 — Applied

The blob retention and replication service window permits only the blob retention change needed to recover a container removed during its retention window. Which option respects the boundary?

- A. Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules.
- B. Choose the tier from observed access frequency, retention period, and retrieval-time requirements.
- C. Use a delete action only after data-protection retention and legal requirements are satisfied.
- D. Enable container delete retention and use a unique test container for recovery validation.

## LAB08-Q18 — Applied

The blob retention preflight has passed; the blob retention and replication service must now retain an earlier block-blob state after a write or deletion. Which operation should run?

- A. Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation.
- B. Enable versioning before overwriting the test blob and persist the returned version IDs.
- C. Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions.
- D. Enable blob soft delete with the approved retention days before testing deletion recovery.

## LAB08-Q19 — Applied

The blob retention and replication service plan must copy supported block-blob changes asynchronously to a second account while limiting the mutation scope to blob retention. Which action is appropriate?

- A. Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules.
- B. Create the container with private access unless anonymous blob access is explicitly required.
- C. Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition.
- D. Enable container delete retention and use a unique test container for recovery validation.

## LAB08-Q20 — Applied

A blob retention ticket in the blob retention and replication service says to copy a directory safely without deleting unrelated destination data. Which blob retention action completes the blob retention and replication service request with minimal change?

- A. Choose the tier from observed access frequency, retention period, and retrieval-time requirements.
- B. Use a delete action only after data-protection retention and legal requirements are satisfied.
- C. Enable versioning before overwriting the test blob and persist the returned version IDs.
- D. Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation.

## LAB08-Q21 — Applied

The blob retention log says the blob retention and replication service can now keep private data from being read without an authorization header. Which blob retention state should the blob retention and replication service acceptance test retain?

- A. Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
- B. Query containerDeleteRetentionPolicy and list deleted containers with the test name.
- C. List the container and confirm its name, lease state, and publicAccess value.
- D. Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.

## LAB08-Q22 — Applied

The blob retention and replication service rejects blob retention exit status as proof it can place frequently read and rarely read blobs in cost-appropriate tiers. Which blob retention and replication service result is valid evidence?

- A. Inspect the delete condition and verify protected or excluded blob prefixes do not match.
- B. List blob versions and confirm distinct version IDs and current-version state.
- C. Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
- D. List the container and confirm its name, lease state, and publicAccess value.

## LAB08-Q23 — Applied

The blob retention validator needs one blob retention and replication service query after the change to apply retention automation only to blobs matching the intended prefix or type. Which blob retention property should the blob retention and replication service validator inspect?

- A. Query deleteRetentionPolicy and confirm enabled and days values.
- B. Query the policy IDs on both accounts and verify replication status on a versioned test blob.
- C. Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
- D. Read the policy filters and test them against both an included and excluded blob name.

## LAB08-Q24 — Applied

The data-platform administrator managing blob retention and replication must confirm the blob retention and replication service, without mutation, can move eligible data to a cooler tier after the configured age. Which blob retention check qualifies?

- A. Query containerDeleteRetentionPolicy and list deleted containers with the test name.
- B. Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
- C. Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
- D. Read the policy filters and test them against both an included and excluded blob name.

## LAB08-Q25 — Applied

The blob retention and replication service configuration is complete; the blob retention reviewers need evidence it can delete only objects that satisfy the retention rule's age conditions. Which observation shows success?

- A. List blob versions and confirm distinct version IDs and current-version state.
- B. List the container and confirm its name, lease state, and publicAccess value.
- C. Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
- D. Inspect the delete condition and verify protected or excluded blob prefixes do not match.

## LAB08-Q26 — Applied

The blob retention validation asks whether the blob retention and replication service can recover a blob deleted after data protection was enabled. Which observable state is strongest?

- A. Query the policy IDs on both accounts and verify replication status on a versioned test blob.
- B. Query deleteRetentionPolicy and confirm enabled and days values.
- C. Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
- D. Inspect the delete condition and verify protected or excluded blob prefixes do not match.

## LAB08-Q27 — Applied

A blob retention and replication service review must prove the blob retention ability to recover a container removed during its retention window. Which check avoids an adjacent feature?

- A. Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
- B. Read the policy filters and test them against both an included and excluded blob name.
- C. Query containerDeleteRetentionPolicy and list deleted containers with the test name.
- D. Query deleteRetentionPolicy and confirm enabled and days values.

## LAB08-Q28 — Applied

The blob retention and replication service evidence bundle needs a blob retention result showing it can retain an earlier block-blob state after a write or deletion. Which result belongs in the checkpoint?

- A. List the container and confirm its name, lease state, and publicAccess value.
- B. List blob versions and confirm distinct version IDs and current-version state.
- C. Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
- D. Query containerDeleteRetentionPolicy and list deleted containers with the test name.

## LAB08-Q29 — Applied

Before blob retention and replication service cleanup, the blob retention team must reconfirm it can copy supported block-blob changes asynchronously to a second account. Which read-only inspection should run?

- A. Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
- B. Inspect the delete condition and verify protected or excluded blob prefixes do not match.
- C. Query the policy IDs on both accounts and verify replication status on a versioned test blob.
- D. List blob versions and confirm distinct version IDs and current-version state.

## LAB08-Q30 — Applied

The blob retention and replication service setup reports success after the blob retention attempt to copy a directory safely without deleting unrelated destination data. Which blob retention read-only observation proves the blob retention and replication service outcome?

- A. Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
- B. Read the policy filters and test them against both an included and excluded blob name.
- C. Query deleteRetentionPolicy and confirm enabled and days values.
- D. Query the policy IDs on both accounts and verify replication status on a versioned test blob.

## LAB08-Q31 — Applied

The blob retention and replication service setup finishes, yet the blob retention cannot keep private data from being read without an authorization header. Which misconfiguration explains the mismatch?

- A. Frequently read data was moved to archive even though the application requires immediate retrieval.
- B. The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state.
- C. The container permits anonymous blob reads despite a private-data requirement.
- D. Sync was run with destination deletion against a path that contains unrelated retained data.

## LAB08-Q32 — Applied

A blob retention break/fix in the blob retention and replication service fails when operators try to place frequently read and rarely read blobs in cost-appropriate tiers. Which diagnosis fits?

- A. The rule has no prefix filter and therefore evaluates unrelated containers in the account.
- B. Only blob soft delete is enabled, so deleting the entire container is not covered by container retention.
- C. Frequently read data was moved to archive even though the application requires immediate retrieval.
- D. The container permits anonymous blob reads despite a private-data requirement.

## LAB08-Q33 — Applied

The blob retention and replication service troubleshooting scope is the blob retention need to apply retention automation only to blobs matching the intended prefix or type. Which condition should be corrected first?

- A. The rule uses daysAfterModificationGreaterThan later than the required retention transition.
- B. The rule has no prefix filter and therefore evaluates unrelated containers in the account.
- C. The overwrite occurred before versioning was enabled, so no earlier version was created.
- D. Frequently read data was moved to archive even though the application requires immediate retrieval.

## LAB08-Q34 — Applied

The blob retention and replication service result is partial because the blob retention cannot move eligible data to a cooler tier after the configured age. Which condition accounts for that result?

- A. The delete action targets current versions before the mandated retention period ends.
- B. The rule uses daysAfterModificationGreaterThan later than the required retention transition.
- C. Versioning is disabled on one account, preventing the replication policy from operating.
- D. The rule has no prefix filter and therefore evaluates unrelated containers in the account.

## LAB08-Q35 — Applied

The blob retention evidence shows the blob retention and replication service cannot delete only objects that satisfy the retention rule's age conditions. Which root cause fits that evidence?

- A. The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state.
- B. Sync was run with destination deletion against a path that contains unrelated retained data.
- C. The rule uses daysAfterModificationGreaterThan later than the required retention transition.
- D. The delete action targets current versions before the mandated retention period ends.

## LAB08-Q36 — Applied

Although the blob retention and replication service is meant to let the blob retention recover a blob deleted after data protection was enabled, its checkpoint fails. Which blob retention defect explains the failure?

- A. The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state.
- B. Only blob soft delete is enabled, so deleting the entire container is not covered by container retention.
- C. The container permits anonymous blob reads despite a private-data requirement.
- D. The delete action targets current versions before the mandated retention period ends.

## LAB08-Q37 — Applied

The blob retention support team isolated the blob retention and replication service incident to the attempt to recover a container removed during its retention window. Which condition prevents success?

- A. Only blob soft delete is enabled, so deleting the entire container is not covered by container retention.
- B. The overwrite occurred before versioning was enabled, so no earlier version was created.
- C. Frequently read data was moved to archive even though the application requires immediate retrieval.
- D. The blob was deleted before soft delete was enabled and has no recoverable soft-deleted state.

## LAB08-Q38 — Applied

A blob retention and replication service query surprises the data-platform administrator managing blob retention and replication during the blob retention attempt to retain an earlier block-blob state after a write or deletion. Which finding explains it?

- A. The overwrite occurred before versioning was enabled, so no earlier version was created.
- B. Versioning is disabled on one account, preventing the replication policy from operating.
- C. The rule has no prefix filter and therefore evaluates unrelated containers in the account.
- D. Only blob soft delete is enabled, so deleting the entire container is not covered by container retention.

## LAB08-Q39 — Applied

Other blob retention and replication service components are healthy, but the blob retention still cannot copy supported block-blob changes asynchronously to a second account. Which state causes the isolated failure?

- A. Sync was run with destination deletion against a path that contains unrelated retained data.
- B. Versioning is disabled on one account, preventing the replication policy from operating.
- C. The rule uses daysAfterModificationGreaterThan later than the required retention transition.
- D. The overwrite occurred before versioning was enabled, so no earlier version was created.

## LAB08-Q40 — Applied

During a blob retention fault drill, the blob retention and replication service does not copy a directory safely without deleting unrelated destination data. Which finding identifies the defect?

- A. Sync was run with destination deletion against a path that contains unrelated retained data.
- B. The container permits anonymous blob reads despite a private-data requirement.
- C. The delete action targets current versions before the mandated retention period ends.
- D. Versioning is disabled on one account, preventing the replication policy from operating.

## LAB08-Q41 — Advanced

To satisfy the blob retention requirement, operators must change the blob retention and replication service configuration and prove it can keep private data from being read without an authorization header. Which sequence is coherent?

- A. First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value.
- B. First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.
- C. First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.
- D. First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.

## LAB08-Q42 — Advanced

The data-platform administrator managing blob retention and replication needs a safe blob retention and replication service change to place frequently read and rarely read blobs in cost-appropriate tiers, followed by blob retention evidence. Which pair merits approval?

- A. First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
- B. First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.
- C. First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
- D. First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.

## LAB08-Q43 — Advanced

The blob retention and replication service has two blob retention gates: apply retention automation only to blobs matching the intended prefix or type, then prove the blob retention and replication service state. Which blob retention sequence works?

- A. First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.
- B. First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match.
- C. First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.
- D. First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.

## LAB08-Q44 — Advanced

Which blob retention path makes the blob retention and replication service able to move eligible data to a cooler tier after the configured age, then inspects the defining properties?

- A. First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
- B. First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.
- C. First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
- D. First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value.

## LAB08-Q45 — Advanced

At the blob retention and replication service approval gate, operators must show that the blob retention can delete only objects that satisfy the retention rule's age conditions. Which blob retention configure-and-check pair is defensible?

- A. First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match.
- B. First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.
- C. First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value.
- D. First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.

## LAB08-Q46 — Advanced

The blob retention and replication service forbids a partial blob retention result. Operators must first recover a blob deleted after data protection was enabled and afterward confirm the blob retention and replication service outcome. Which blob retention sequence is complete?

- A. First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.
- B. First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.
- C. First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
- D. First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.

## LAB08-Q47 — Advanced

Only the blob retention and replication service change needed to recover a container removed during its retention window is allowed, and blob retention proof is mandatory. Which pair fits?

- A. First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.
- B. First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.
- C. First, Constrain the lifecycle rule to the intended container prefix and blob type before enabling destructive actions. Then, Read the policy filters and test them against both an included and excluded blob name.
- D. First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.

## LAB08-Q48 — Advanced

The blob retention and replication service runbook separates blob retention mutation from validation while it must retain an earlier block-blob state after a write or deletion. Which sequence proves it cleanly?

- A. First, Enable versioning before overwriting the test blob and persist the returned version IDs. Then, List blob versions and confirm distinct version IDs and current-version state.
- B. First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
- C. First, Configure the appropriate baseBlob tierToCool, tierToCold, or tierToArchive action with an age condition. Then, Read the lifecycle action and condition, then confirm only eligible test blobs match the rule.
- D. First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match.

## LAB08-Q49 — Advanced

The blob retention and replication service checkpoint requires both this blob retention outcome—copy supported block-blob changes asynchronously to a second account—and a read-only blob retention and replication service state check. Which blob retention response is complete?

- A. First, Create the container with private access unless anonymous blob access is explicitly required. Then, List the container and confirm its name, lease state, and publicAccess value.
- B. First, Use a delete action only after data-protection retention and legal requirements are satisfied. Then, Inspect the delete condition and verify protected or excluded blob prefixes do not match.
- C. First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.
- D. First, Enable prerequisites on both accounts and create a replication policy with matching source and destination container rules. Then, Query the policy IDs on both accounts and verify replication status on a versioned test blob.

## LAB08-Q50 — Advanced

The blob retention and replication service runbook must copy a directory safely without deleting unrelated destination data, then retain blob retention read-back evidence. Which blob retention and replication service pair completes both duties?

- A. First, Choose the tier from observed access frequency, retention period, and retrieval-time requirements. Then, Read the blob's accessTier and accessTierChangeTime after the tier operation completes.
- B. First, Enable blob soft delete with the approved retention days before testing deletion recovery. Then, Query deleteRetentionPolicy and confirm enabled and days values.
- C. First, Use copy for a one-time transfer and reserve sync deletion for an explicitly reviewed mirror operation. Then, Run a dry comparison or list both endpoints and verify object counts, names, and hashes where available.
- D. First, Enable container delete retention and use a unique test container for recovery validation. Then, Query containerDeleteRetentionPolicy and list deleted containers with the test name.

[Open the answer key](./ANSWERS.md)
