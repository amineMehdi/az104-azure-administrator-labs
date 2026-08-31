# Lab 06 knowledge check

Secure storage accounts, redundancy, encryption, and keys

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Manage access keys' in Lab 06? (`LAB06-Q01`)

- A. Redundancy protects copies of data, encryption protects data at rest, and access keys are broad secrets that must be rotated without entering state or command evidence.
- B. The shortest command is always correct even when it changes a broader scope.
- C. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Create and configure storage accounts'? (`LAB06-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Require HTTPS, TLS 1.2, and disabled anonymous blob access.
- C. Search the whole tenant for a similar display name and modify the first match.
- D. Mark the objective complete after reading documentation without checking any state.

## 3. Which authorization approach is appropriate before practicing 'Configure Azure Storage redundancy'? (`LAB06-Q03`)

- A. Use a production subscription because its resources already exist.
- B. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- C. Confirm the active context and use only the declared role boundary: Contributor on the lab resource group
- D. Skip role checks when the run ID contains the lab number.

## 4. Which resource or object belongs inside the recorded boundary for 'Configure storage account encryption'? (`LAB06-Q04`)

- A. Use whichever similarly named object appears first in a broad search.
- B. Use an unrelated shared resource without recording its immutable ID.
- C. Use a production object when the sandbox prerequisite is unavailable.
- D. Use the exact recorded identity and scope for StorageV2 account.

## 5. A learner previews the implementation for 'Manage access keys'. What behavior is required? (`LAB06-Q05`)

- A. Display the context, intended changes, cost and gated branches without mutating Azure.
- B. Create the baseline immediately and request approval only before cleanup.
- C. Select the first accessible subscription and hide the resulting context.
- D. Delete any older resource whose name resembles the new run ID.

## 6. Which implementation step should the learner perform for 'Create and configure storage accounts'? (`LAB06-Q06`)

- A. Replace the lab action with a tenant-wide change that is easier to discover.
- B. Require HTTPS, TLS 1.2, and disabled anonymous blob access.
- C. Copy resource identifiers from another run instead of recording returned IDs.
- D. Skip the operation and edit validation.json to show a passing result.

## 7. Which evidence most directly validates 'Configure Azure Storage redundancy' for resource group? (`LAB06-Q07`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. List the entire subscription and assume similarly named resources belong to this run.
- C. Query the exact recorded scope and independently verify Microsoft.Storage/storageAccounts.
- D. Record a credential so another learner can replay the authenticated session.

## 8. The 'Configure storage account encryption' checkpoint reaches an external prerequisite. What should happen? (`LAB06-Q08`)

- A. Invent a domain, notification target, license, quota, or tenant value and continue.
- B. Broaden permissions until the prerequisite can no longer block the operation.
- C. Mark the branch passed because its command syntax was checked offline.
- D. Run the branch only when this documented gate is satisfied: None beyond the declared role and a disposable subscription.

## 9. What is the safest command-evidence practice after completing 'Manage access keys'? (`LAB06-Q09`)

- A. Retain only redacted structured output from an independent query of the recorded run.
- B. Commit the complete account object so reviewers can identify the tenant.
- C. Save tokens, keys, passwords, or SAS values beside the validation result.
- D. Reuse successful output from an earlier run with a similar resource name.

## 10. Which negative check strengthens validation of 'Create and configure storage accounts'? (`LAB06-Q10`)

- A. Check only that at least one resource exists in the subscription.
- B. Confirm the intended state and also prove that broader, anonymous, or unintended access was not introduced.
- C. Repair every warning automatically before recording what caused it.
- D. Ignore denied queries and record them as passing checks.

## 11. Validation for 'Configure Azure Storage redundancy' fails after setup. What is the best break/fix method? (`LAB06-Q11`)

- A. Rerun setup repeatedly with new names until one attempt appears successful.
- B. Change validation.json directly so the failed result reads pass.
- C. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.

## 12. The operation for 'Configure storage account encryption' is asynchronous or gated. How should completion be recorded? (`LAB06-Q12`)

- A. Record pass as soon as the request is accepted, regardless of its final state.
- B. Fabricate expected output so the assessment and documentation appear complete.
- C. Remove the check from validation whenever the service takes longer than expected.
- D. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
