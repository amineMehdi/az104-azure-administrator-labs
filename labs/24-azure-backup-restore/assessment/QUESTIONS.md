# Lab 24 knowledge check

Configure Azure Backup policies, protection, restore, reports, and alerts

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Create a Recovery Services vault' in Lab 24? (`LAB24-Q01`)

- A. The shortest command is always correct even when it changes a broader scope.
- B. Vault type must match the workload, protection creates retained recovery points, and vault deletion requires ordered removal of protected items, soft-delete state, and dependencies.
- C. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Create an Azure Backup vault'? (`LAB24-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Search the whole tenant for a similar display name and modify the first match.
- C. Create a bounded-retention VM backup policy and enable protection for the test VM.
- D. Mark the objective complete after reading documentation without checking any state.

## 3. Which authorization approach is appropriate before practicing 'Create and configure a backup policy'? (`LAB24-Q03`)

- A. Use a production subscription because its resources already exist.
- B. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- C. Skip role checks when the run ID contains the lab number.
- D. Confirm the active context and use only the declared role boundary: Backup Contributor and Virtual Machine Contributor on the lab resource group

## 4. Which resource or object belongs inside the recorded boundary for 'Perform backup and restore operations by using Azure Backup'? (`LAB24-Q04`)

- A. Use the exact recorded identity and scope for backup policy.
- B. Use whichever similarly named object appears first in a broad search.
- C. Use an unrelated shared resource without recording its immutable ID.
- D. Use a production object when the sandbox prerequisite is unavailable.

## 5. A learner previews the implementation for 'Configure and interpret reports and alerts for backups'. What behavior is required? (`LAB24-Q05`)

- A. Create the baseline immediately and request approval only before cleanup.
- B. Display the context, intended changes, cost and gated branches without mutating Azure.
- C. Select the first accessible subscription and hide the resulting context.
- D. Delete any older resource whose name resembles the new run ID.

## 6. Which implementation step should the learner perform for 'Create a Recovery Services vault'? (`LAB24-Q06`)

- A. Replace the lab action with a tenant-wide change that is easier to discover.
- B. Copy resource identifiers from another run instead of recording returned IDs.
- C. Create a bounded-retention VM backup policy and enable protection for the test VM.
- D. Skip the operation and edit validation.json to show a passing result.

## 7. Which evidence most directly validates 'Create an Azure Backup vault' for resource group? (`LAB24-Q07`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. List the entire subscription and assume similarly named resources belong to this run.
- C. Record a credential so another learner can replay the authenticated session.
- D. Query the exact recorded scope and independently verify Microsoft.RecoveryServices/vaults.

## 8. The 'Create and configure a backup policy' checkpoint reaches an external prerequisite. What should happen? (`LAB24-Q08`)

- A. Run the branch only when this documented gate is satisfied: None beyond the declared role and a disposable subscription.
- B. Invent a domain, notification target, license, quota, or tenant value and continue.
- C. Broaden permissions until the prerequisite can no longer block the operation.
- D. Mark the branch passed because its command syntax was checked offline.

## 9. What is the safest command-evidence practice after completing 'Perform backup and restore operations by using Azure Backup'? (`LAB24-Q09`)

- A. Commit the complete account object so reviewers can identify the tenant.
- B. Retain only redacted structured output from an independent query of the recorded run.
- C. Save tokens, keys, passwords, or SAS values beside the validation result.
- D. Reuse successful output from an earlier run with a similar resource name.

## 10. Which negative check strengthens validation of 'Configure and interpret reports and alerts for backups'? (`LAB24-Q10`)

- A. Check only that at least one resource exists in the subscription.
- B. Repair every warning automatically before recording what caused it.
- C. Confirm the intended state and also prove that broader, anonymous, or unintended access was not introduced.
- D. Ignore denied queries and record them as passing checks.

## 11. Why should the run manifest record the exact ID of protected test VM? (`LAB24-Q11`)

- A. It lets setup store access tokens and passwords for later reuse.
- B. It allows cleanup to delete every object with the same prefix.
- C. It removes the need to confirm the tenant or subscription context.
- D. It lets validation and cleanup target the immutable object created by this run rather than a name match.

## 12. Several similarly named resources exist when cleaning up 'Create an Azure Backup vault'. What is correct? (`LAB24-Q12`)

- A. Verify the recorded IDs and ownership tags, preview the targets, and delete only this run's boundary.
- B. Delete all resources containing az104 in their names.
- C. Delete the active subscription to guarantee that no lab state remains.
- D. Choose targets only by creation time and remove the oldest objects.

## 13. Validation for 'Create and configure a backup policy' fails after setup. What is the best break/fix method? (`LAB24-Q13`)

- A. Rerun setup repeatedly with new names until one attempt appears successful.
- B. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- C. Change validation.json directly so the failed result reads pass.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.

## 14. The operation for 'Perform backup and restore operations by using Azure Backup' is asynchronous or gated. How should completion be recorded? (`LAB24-Q14`)

- A. Record pass as soon as the request is accepted, regardless of its final state.
- B. Fabricate expected output so the assessment and documentation appear complete.
- C. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
- D. Remove the check from validation whenever the service takes longer than expected.

## 15. An administrator discovers drift while validating 'Configure and interpret reports and alerts for backups'. Which response preserves least privilege? (`LAB24-Q15`)

- A. Grant subscription Owner and tenant administrator roles to avoid further authorization errors.
- B. Replace every resource in the subscription instead of identifying the mismatch.
- C. Accept the drift when the resource name still matches the lab prefix.
- D. Compare the live query with the recorded expectation, change only the mismatched setting, and validate again.
