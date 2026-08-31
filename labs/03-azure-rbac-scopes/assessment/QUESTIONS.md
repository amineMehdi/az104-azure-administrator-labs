# Lab 03 knowledge check

Assign and interpret Azure RBAC at multiple scopes

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Manage built-in Azure roles' in Lab 03? (`LAB03-Q01`)

- A. A role definition describes allowed actions; a role assignment binds that definition to a principal at a scope, with inheritance flowing downward.
- B. The shortest command is always correct even when it changes a broader scope.
- C. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Assign roles at different scopes'? (`LAB03-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Resolve Reader and Contributor built-in role definitions without creating custom roles.
- C. Search the whole tenant for a similar display name and modify the first match.
- D. Mark the objective complete after reading documentation without checking any state.

## 3. Which authorization approach is appropriate before practicing 'Interpret access assignments'? (`LAB03-Q03`)

- A. Use a production subscription because its resources already exist.
- B. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- C. Confirm the active context and use only the declared role boundary: User Access Administrator or Owner at the lab resource-group scope
- D. Skip role checks when the run ID contains the lab number.

## 4. A learner previews the implementation for 'Manage built-in Azure roles'. What behavior is required? (`LAB03-Q04`)

- A. Create the baseline immediately and request approval only before cleanup.
- B. Select the first accessible subscription and hide the resulting context.
- C. Delete any older resource whose name resembles the new run ID.
- D. Display the context, intended changes, cost and gated branches without mutating Azure.

## 5. Which implementation step should the learner perform for 'Assign roles at different scopes'? (`LAB03-Q05`)

- A. Create the dedicated tagged resource group.
- B. Replace the lab action with a tenant-wide change that is easier to discover.
- C. Copy resource identifiers from another run instead of recording returned IDs.
- D. Skip the operation and edit validation.json to show a passing result.

## 6. Which evidence most directly validates 'Interpret access assignments' for resource-group-scoped role assignment? (`LAB03-Q06`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. Query the exact recorded scope and independently verify the intended recorded state.
- C. List the entire subscription and assume similarly named resources belong to this run.
- D. Record a credential so another learner can replay the authenticated session.

## 7. The 'Manage built-in Azure roles' checkpoint reaches an external prerequisite. What should happen? (`LAB03-Q07`)

- A. Invent a domain, notification target, license, quota, or tenant value and continue.
- B. Broaden permissions until the prerequisite can no longer block the operation.
- C. Run the branch only when this documented gate is satisfied: Requires the object ID of a disposable principal in AZ104_PRINCIPAL_OBJECT_ID.
- D. Mark the branch passed because its command syntax was checked offline.

## 8. What is the safest command-evidence practice after completing 'Assign roles at different scopes'? (`LAB03-Q08`)

- A. Commit the complete account object so reviewers can identify the tenant.
- B. Save tokens, keys, passwords, or SAS values beside the validation result.
- C. Reuse successful output from an earlier run with a similar resource name.
- D. Retain only redacted structured output from an independent query of the recorded run.

## 9. Validation for 'Interpret access assignments' fails after setup. What is the best break/fix method? (`LAB03-Q09`)

- A. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- B. Rerun setup repeatedly with new names until one attempt appears successful.
- C. Change validation.json directly so the failed result reads pass.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.

## 10. The operation for 'Manage built-in Azure roles' is asynchronous or gated. How should completion be recorded? (`LAB03-Q10`)

- A. Record pass as soon as the request is accepted, regardless of its final state.
- B. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
- C. Fabricate expected output so the assessment and documentation appear complete.
- D. Remove the check from validation whenever the service takes longer than expected.
