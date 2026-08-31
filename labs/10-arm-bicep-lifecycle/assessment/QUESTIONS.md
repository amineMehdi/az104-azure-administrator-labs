# Lab 10 knowledge check

Interpret, modify, deploy, export, and decompile ARM and Bicep

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Interpret an Azure Resource Manager template or a Bicep file' in Lab 10? (`LAB10-Q01`)

- A. Bicep compiles to ARM JSON, what-if predicts control-plane changes, and exported/decompiled templates require human review rather than being treated as pristine source.
- B. The shortest command is always correct even when it changes a broader scope.
- C. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Modify an existing Azure Resource Manager template'? (`LAB10-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Modify parameter values and run a resource-group what-if before deployment.
- C. Search the whole tenant for a similar display name and modify the first match.
- D. Mark the objective complete after reading documentation without checking any state.

## 3. Which authorization approach is appropriate before practicing 'Modify an existing Bicep file'? (`LAB10-Q03`)

- A. Use a production subscription because its resources already exist.
- B. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- C. Confirm the active context and use only the declared role boundary: Contributor on the lab resource group
- D. Skip role checks when the run ID contains the lab number.

## 4. A learner previews the implementation for 'Deploy resources by using an Azure Resource Manager template or a Bicep file'. What behavior is required? (`LAB10-Q04`)

- A. Create the baseline immediately and request approval only before cleanup.
- B. Select the first accessible subscription and hide the resulting context.
- C. Delete any older resource whose name resembles the new run ID.
- D. Display the context, intended changes, cost and gated branches without mutating Azure.

## 5. Which implementation step should the learner perform for 'Export a deployment as an Azure Resource Manager template or convert an Azure Resource Manager template to a Bicep file'? (`LAB10-Q05`)

- A. Build and lint the supplied Bicep file and inspect its generated ARM JSON.
- B. Replace the lab action with a tenant-wide change that is easier to discover.
- C. Copy resource identifiers from another run instead of recording returned IDs.
- D. Skip the operation and edit validation.json to show a passing result.

## 6. Which evidence most directly validates 'Interpret an Azure Resource Manager template or a Bicep file' for Bicep deployment? (`LAB10-Q06`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. Query the exact recorded scope and independently verify Microsoft.Storage/storageAccounts.
- C. List the entire subscription and assume similarly named resources belong to this run.
- D. Record a credential so another learner can replay the authenticated session.

## 7. The 'Modify an existing Azure Resource Manager template' checkpoint reaches an external prerequisite. What should happen? (`LAB10-Q07`)

- A. Invent a domain, notification target, license, quota, or tenant value and continue.
- B. Broaden permissions until the prerequisite can no longer block the operation.
- C. Run the branch only when this documented gate is satisfied: None beyond the declared role and a disposable subscription.
- D. Mark the branch passed because its command syntax was checked offline.

## 8. What is the safest command-evidence practice after completing 'Modify an existing Bicep file'? (`LAB10-Q08`)

- A. Commit the complete account object so reviewers can identify the tenant.
- B. Save tokens, keys, passwords, or SAS values beside the validation result.
- C. Reuse successful output from an earlier run with a similar resource name.
- D. Retain only redacted structured output from an independent query of the recorded run.

## 9. Validation for 'Deploy resources by using an Azure Resource Manager template or a Bicep file' fails after setup. What is the best break/fix method? (`LAB10-Q09`)

- A. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- B. Rerun setup repeatedly with new names until one attempt appears successful.
- C. Change validation.json directly so the failed result reads pass.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.

## 10. The operation for 'Export a deployment as an Azure Resource Manager template or convert an Azure Resource Manager template to a Bicep file' is asynchronous or gated. How should completion be recorded? (`LAB10-Q10`)

- A. Record pass as soon as the request is accepted, regardless of its final state.
- B. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
- C. Fabricate expected output so the assessment and documentation appear complete.
- D. Remove the check from validation whenever the service takes longer than expected.
