# Lab 08 knowledge check

Manage Blob lifecycle, tiers, versioning, replication, and AzCopy

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Configure object replication' in Lab 08? (`LAB08-Q01`)

- A. Object replication depends on versioning and change feed, while lifecycle rules act asynchronously and should be validated as configuration rather than immediate data movement.
- B. The shortest command is always correct even when it changes a broader scope.
- C. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Manage data by using Azure Storage Explorer and AzCopy'? (`LAB08-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Enable blob and container soft delete and create private containers.
- C. Search the whole tenant for a similar display name and modify the first match.
- D. Mark the objective complete after reading documentation without checking any state.

## 3. Which authorization approach is appropriate before practicing 'Create and configure a container in Azure Blob Storage'? (`LAB08-Q03`)

- A. Use a production subscription because its resources already exist.
- B. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- C. Confirm the active context and use only the declared role boundary: Contributor and Storage Blob Data Contributor on the lab resource group
- D. Skip role checks when the run ID contains the lab number.

## 4. Which resource or object belongs inside the recorded boundary for 'Configure storage tiers'? (`LAB08-Q04`)

- A. Use whichever similarly named object appears first in a broad search.
- B. Use an unrelated shared resource without recording its immutable ID.
- C. Use a production object when the sandbox prerequisite is unavailable.
- D. Use the exact recorded identity and scope for lifecycle policy.

## 5. A learner previews the implementation for 'Configure soft delete for blobs and containers'. What behavior is required? (`LAB08-Q05`)

- A. Display the context, intended changes, cost and gated branches without mutating Azure.
- B. Create the baseline immediately and request approval only before cleanup.
- C. Select the first accessible subscription and hide the resulting context.
- D. Delete any older resource whose name resembles the new run ID.

## 6. Which implementation step should the learner perform for 'Configure blob lifecycle management'? (`LAB08-Q06`)

- A. Replace the lab action with a tenant-wide change that is easier to discover.
- B. Enable blob and container soft delete and create private containers.
- C. Copy resource identifiers from another run instead of recording returned IDs.
- D. Skip the operation and edit validation.json to show a passing result.

## 7. Which evidence most directly validates 'Configure blob versioning' for two StorageV2 accounts? (`LAB08-Q07`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. List the entire subscription and assume similarly named resources belong to this run.
- C. Query the exact recorded scope and independently verify Microsoft.Storage/storageAccounts.
- D. Record a credential so another learner can replay the authenticated session.

## 8. The 'Configure object replication' checkpoint reaches an external prerequisite. What should happen? (`LAB08-Q08`)

- A. Invent a domain, notification target, license, quota, or tenant value and continue.
- B. Broaden permissions until the prerequisite can no longer block the operation.
- C. Mark the branch passed because its command syntax was checked offline.
- D. Run the branch only when this documented gate is satisfied: None beyond the declared role and a disposable subscription.

## 9. What is the safest command-evidence practice after completing 'Manage data by using Azure Storage Explorer and AzCopy'? (`LAB08-Q09`)

- A. Retain only redacted structured output from an independent query of the recorded run.
- B. Commit the complete account object so reviewers can identify the tenant.
- C. Save tokens, keys, passwords, or SAS values beside the validation result.
- D. Reuse successful output from an earlier run with a similar resource name.

## 10. Which negative check strengthens validation of 'Create and configure a container in Azure Blob Storage'? (`LAB08-Q10`)

- A. Check only that at least one resource exists in the subscription.
- B. Confirm the intended state and also prove that broader, anonymous, or unintended access was not introduced.
- C. Repair every warning automatically before recording what caused it.
- D. Ignore denied queries and record them as passing checks.

## 11. Why should the run manifest record the exact ID of resource group? (`LAB08-Q11`)

- A. It lets setup store access tokens and passwords for later reuse.
- B. It allows cleanup to delete every object with the same prefix.
- C. It lets validation and cleanup target the immutable object created by this run rather than a name match.
- D. It removes the need to confirm the tenant or subscription context.

## 12. Validation for 'Configure soft delete for blobs and containers' fails after setup. What is the best break/fix method? (`LAB08-Q12`)

- A. Rerun setup repeatedly with new names until one attempt appears successful.
- B. Change validation.json directly so the failed result reads pass.
- C. Disable unrelated policies, locks, network controls, and monitoring across the subscription.
- D. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.

## 13. The operation for 'Configure blob lifecycle management' is asynchronous or gated. How should completion be recorded? (`LAB08-Q13`)

- A. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
- B. Record pass as soon as the request is accepted, regardless of its final state.
- C. Fabricate expected output so the assessment and documentation appear complete.
- D. Remove the check from validation whenever the service takes longer than expected.

## 14. An administrator discovers drift while validating 'Configure blob versioning'. Which response preserves least privilege? (`LAB08-Q14`)

- A. Grant subscription Owner and tenant administrator roles to avoid further authorization errors.
- B. Compare the live query with the recorded expectation, change only the mismatched setting, and validate again.
- C. Replace every resource in the subscription instead of identifying the mismatch.
- D. Accept the drift when the resource name still matches the lab prefix.
