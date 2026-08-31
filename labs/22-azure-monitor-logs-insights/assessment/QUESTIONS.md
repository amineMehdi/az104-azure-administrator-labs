# Lab 22 knowledge check

Collect and analyze Azure Monitor metrics, logs, and Insights

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Interpret metrics in Azure Monitor' in Lab 22? (`LAB22-Q01`)

- A. Metrics are numeric time series, logs are queryable records with ingestion delay and cost, and Insights packages add curated collection and interpretation for particular resource types.
- B. The shortest command is always correct even when it changes a broader scope.
- C. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Configure log settings in Azure Monitor'? (`LAB22-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Discover diagnostic categories and create settings that send supported logs and metrics to the workspace.
- C. Search the whole tenant for a similar display name and modify the first match.
- D. Mark the objective complete after reading documentation without checking any state.

## 3. Which authorization approach is appropriate before practicing 'Query and analyze logs in Azure Monitor'? (`LAB22-Q03`)

- A. Use a production subscription because its resources already exist.
- B. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- C. Confirm the active context and use only the declared role boundary: Monitoring Contributor and Log Analytics Contributor on the lab resource group
- D. Skip role checks when the run ID contains the lab number.

## 4. Which resource or object belongs inside the recorded boundary for 'Configure and interpret monitoring of virtual machines, storage accounts, and networks by using Azure Monitor Insights'? (`LAB22-Q04`)

- A. Use whichever similarly named object appears first in a broad search.
- B. Use an unrelated shared resource without recording its immutable ID.
- C. Use a production object when the sandbox prerequisite is unavailable.
- D. Use the exact recorded identity and scope for diagnostic setting.

## 5. What must an administrator verify before changing optional data collection rule for 'Use Azure Network Watcher and Connection monitor'? (`LAB22-Q05`)

- A. Verify the tenant or subscription context, permissions, intended scope, and live gate before mutation.
- B. Verify only that the command-line tool starts successfully.
- C. Verify only that a resource with a similar name exists somewhere in Azure.
- D. Verify the result after cleanup and omit the pre-change context check.

## 6. A learner previews the implementation for 'Interpret metrics in Azure Monitor'. What behavior is required? (`LAB22-Q06`)

- A. Create the baseline immediately and request approval only before cleanup.
- B. Display the context, intended changes, cost and gated branches without mutating Azure.
- C. Select the first accessible subscription and hide the resulting context.
- D. Delete any older resource whose name resembles the new run ID.

## 7. Which implementation step should the learner perform for 'Configure log settings in Azure Monitor'? (`LAB22-Q07`)

- A. Replace the lab action with a tenant-wide change that is easier to discover.
- B. Copy resource identifiers from another run instead of recording returned IDs.
- C. Run KQL queries that summarize activity by operation, result, and time range without assuming immediate ingestion.
- D. Skip the operation and edit validation.json to show a passing result.

## 8. Which evidence most directly validates 'Query and analyze logs in Azure Monitor' for storage account? (`LAB22-Q08`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. List the entire subscription and assume similarly named resources belong to this run.
- C. Record a credential so another learner can replay the authenticated session.
- D. Query the exact recorded scope and independently verify Microsoft.Insights/diagnosticSettings.

## 9. The 'Configure and interpret monitoring of virtual machines, storage accounts, and networks by using Azure Monitor Insights' checkpoint reaches an external prerequisite. What should happen? (`LAB22-Q09`)

- A. Run the branch only when this documented gate is satisfied: None beyond the declared role and a disposable subscription.
- B. Invent a domain, notification target, license, quota, or tenant value and continue.
- C. Broaden permissions until the prerequisite can no longer block the operation.
- D. Mark the branch passed because its command syntax was checked offline.

## 10. What is the safest command-evidence practice after completing 'Use Azure Network Watcher and Connection monitor'? (`LAB22-Q10`)

- A. Commit the complete account object so reviewers can identify the tenant.
- B. Retain only redacted structured output from an independent query of the recorded run.
- C. Save tokens, keys, passwords, or SAS values beside the validation result.
- D. Reuse successful output from an earlier run with a similar resource name.

## 11. Which negative check strengthens validation of 'Interpret metrics in Azure Monitor'? (`LAB22-Q11`)

- A. Check only that at least one resource exists in the subscription.
- B. Repair every warning automatically before recording what caused it.
- C. Confirm the intended state and also prove that broader, anonymous, or unintended access was not introduced.
- D. Ignore denied queries and record them as passing checks.

## 12. Why should the run manifest record the exact ID of Log Analytics workspace? (`LAB22-Q12`)

- A. It lets setup store access tokens and passwords for later reuse.
- B. It allows cleanup to delete every object with the same prefix.
- C. It removes the need to confirm the tenant or subscription context.
- D. It lets validation and cleanup target the immutable object created by this run rather than a name match.

## 13. Validation for 'Query and analyze logs in Azure Monitor' fails after setup. What is the best break/fix method? (`LAB22-Q13`)

- A. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- B. Rerun setup repeatedly with new names until one attempt appears successful.
- C. Change validation.json directly so the failed result reads pass.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.

## 14. The operation for 'Configure and interpret monitoring of virtual machines, storage accounts, and networks by using Azure Monitor Insights' is asynchronous or gated. How should completion be recorded? (`LAB22-Q14`)

- A. Record pass as soon as the request is accepted, regardless of its final state.
- B. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
- C. Fabricate expected output so the assessment and documentation appear complete.
- D. Remove the check from validation whenever the service takes longer than expected.

## 15. An administrator discovers drift while validating 'Use Azure Network Watcher and Connection monitor'. Which response preserves least privilege? (`LAB22-Q15`)

- A. Grant subscription Owner and tenant administrator roles to avoid further authorization errors.
- B. Replace every resource in the subscription instead of identifying the mismatch.
- C. Compare the live query with the recorded expectation, change only the mismatched setting, and validate again.
- D. Accept the drift when the resource name still matches the lab prefix.
