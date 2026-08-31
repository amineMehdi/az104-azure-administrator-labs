# Lab 09 knowledge check

Configure Azure Files, snapshots, soft delete, and identity access

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Configure identity-based access for Azure Files' in Lab 09? (`LAB09-Q01`)

- A. The shortest command is always correct even when it changes a broader scope.
- B. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- C. Share snapshots and soft delete solve different recovery problems, while identity-based SMB authentication requires an approved directory source and data-plane authorization.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Manage data by using Azure Storage Explorer and AzCopy'? (`LAB09-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Search the whole tenant for a similar display name and modify the first match.
- C. Mark the objective complete after reading documentation without checking any state.
- D. Enable Azure Files share soft delete and create a point-in-time share snapshot.

## 3. Which authorization approach is appropriate before practicing 'Create and configure a file share in Azure Files'? (`LAB09-Q03`)

- A. Confirm the active context and use only the declared role boundary: Contributor and Storage File Data SMB Share Contributor; directory permissions for the optional identity-source path
- B. Use a production subscription because its resources already exist.
- C. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- D. Skip role checks when the run ID contains the lab number.

## 4. A learner previews the implementation for 'Configure snapshots and soft delete for Azure Files'. What behavior is required? (`LAB09-Q04`)

- A. Create the baseline immediately and request approval only before cleanup.
- B. Display the context, intended changes, cost and gated branches without mutating Azure.
- C. Select the first accessible subscription and hide the resulting context.
- D. Delete any older resource whose name resembles the new run ID.

## 5. Which implementation step should the learner perform for 'Configure identity-based access for Azure Files'? (`LAB09-Q05`)

- A. Replace the lab action with a tenant-wide change that is easier to discover.
- B. Copy resource identifiers from another run instead of recording returned IDs.
- C. Create a secure StorageV2 account and transaction-optimized file share with quota.
- D. Skip the operation and edit validation.json to show a passing result.

## 6. Which evidence most directly validates 'Manage data by using Azure Storage Explorer and AzCopy' for storage account? (`LAB09-Q06`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. List the entire subscription and assume similarly named resources belong to this run.
- C. Record a credential so another learner can replay the authenticated session.
- D. Query the exact recorded scope and independently verify Microsoft.Storage/storageAccounts/fileServices/shares.

## 7. The 'Create and configure a file share in Azure Files' checkpoint reaches an external prerequisite. What should happen? (`LAB09-Q07`)

- A. Run the branch only when this documented gate is satisfied: Identity-based SMB configuration is gated by AZ104_FILES_IDENTITY_SOURCE because Entra Kerberos, AD DS, and Entra Domain Services have different prerequisites.
- B. Invent a domain, notification target, license, quota, or tenant value and continue.
- C. Broaden permissions until the prerequisite can no longer block the operation.
- D. Mark the branch passed because its command syntax was checked offline.

## 8. What is the safest command-evidence practice after completing 'Configure snapshots and soft delete for Azure Files'? (`LAB09-Q08`)

- A. Commit the complete account object so reviewers can identify the tenant.
- B. Retain only redacted structured output from an independent query of the recorded run.
- C. Save tokens, keys, passwords, or SAS values beside the validation result.
- D. Reuse successful output from an earlier run with a similar resource name.

## 9. Which negative check strengthens validation of 'Configure identity-based access for Azure Files'? (`LAB09-Q09`)

- A. Check only that at least one resource exists in the subscription.
- B. Repair every warning automatically before recording what caused it.
- C. Confirm the intended state and also prove that broader, anonymous, or unintended access was not introduced.
- D. Ignore denied queries and record them as passing checks.

## 10. Validation for 'Manage data by using Azure Storage Explorer and AzCopy' fails after setup. What is the best break/fix method? (`LAB09-Q10`)

- A. Rerun setup repeatedly with new names until one attempt appears successful.
- B. Change validation.json directly so the failed result reads pass.
- C. Disable unrelated policies, locks, network controls, and monitoring across the subscription.
- D. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.

## 11. The operation for 'Create and configure a file share in Azure Files' is asynchronous or gated. How should completion be recorded? (`LAB09-Q11`)

- A. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
- B. Record pass as soon as the request is accepted, regardless of its final state.
- C. Fabricate expected output so the assessment and documentation appear complete.
- D. Remove the check from validation whenever the service takes longer than expected.

## 12. An administrator discovers drift while validating 'Configure snapshots and soft delete for Azure Files'. Which response preserves least privilege? (`LAB09-Q12`)

- A. Grant subscription Owner and tenant administrator roles to avoid further authorization errors.
- B. Compare the live query with the recorded expectation, change only the mismatched setting, and validate again.
- C. Replace every resource in the subscription instead of identifying the mismatch.
- D. Accept the drift when the resource name still matches the lab prefix.
