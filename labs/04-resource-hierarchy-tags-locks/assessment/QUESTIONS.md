# Lab 04 knowledge check

Manage hierarchy, resource groups, tags, and locks

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Configure resource locks' in Lab 04? (`LAB04-Q01`)

- A. The shortest command is always correct even when it changes a broader scope.
- B. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- C. Tags are metadata rather than access controls, and resource locks protect the control plane without replacing RBAC or data-plane protection.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Apply and manage tags on resources'? (`LAB04-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Search the whole tenant for a similar display name and modify the first match.
- C. Mark the objective complete after reading documentation without checking any state.
- D. Update tags using merge semantics and verify which values do not inherit automatically.

## 3. Which authorization approach is appropriate before practicing 'Manage resource groups'? (`LAB04-Q03`)

- A. Confirm the active context and use only the declared role boundary: Contributor plus User Access Administrator for lock management; Management Group Contributor for the optional hierarchy path
- B. Use a production subscription because its resources already exist.
- C. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- D. Skip role checks when the run ID contains the lab number.

## 4. A learner previews the implementation for 'Manage subscriptions'. What behavior is required? (`LAB04-Q04`)

- A. Create the baseline immediately and request approval only before cleanup.
- B. Display the context, intended changes, cost and gated branches without mutating Azure.
- C. Select the first accessible subscription and hide the resulting context.
- D. Delete any older resource whose name resembles the new run ID.

## 5. Which implementation step should the learner perform for 'Configure management groups'? (`LAB04-Q05`)

- A. Replace the lab action with a tenant-wide change that is easier to discover.
- B. Copy resource identifiers from another run instead of recording returned IDs.
- C. Create a resource group with purpose, labId, runId, owner, and expiresOn tags.
- D. Skip the operation and edit validation.json to show a passing result.

## 6. Which evidence most directly validates 'Configure resource locks' for optional management group? (`LAB04-Q06`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. List the entire subscription and assume similarly named resources belong to this run.
- C. Record a credential so another learner can replay the authenticated session.
- D. Query the exact recorded scope and independently verify Microsoft.Authorization/locks.

## 7. The 'Apply and manage tags on resources' checkpoint reaches an external prerequisite. What should happen? (`LAB04-Q07`)

- A. Run the branch only when this documented gate is satisfied: Management-group creation is optional and requires explicit tenant hierarchy authorization.
- B. Invent a domain, notification target, license, quota, or tenant value and continue.
- C. Broaden permissions until the prerequisite can no longer block the operation.
- D. Mark the branch passed because its command syntax was checked offline.

## 8. What is the safest command-evidence practice after completing 'Manage resource groups'? (`LAB04-Q08`)

- A. Commit the complete account object so reviewers can identify the tenant.
- B. Retain only redacted structured output from an independent query of the recorded run.
- C. Save tokens, keys, passwords, or SAS values beside the validation result.
- D. Reuse successful output from an earlier run with a similar resource name.

## 9. Validation for 'Manage subscriptions' fails after setup. What is the best break/fix method? (`LAB04-Q09`)

- A. Rerun setup repeatedly with new names until one attempt appears successful.
- B. Change validation.json directly so the failed result reads pass.
- C. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.

## 10. The operation for 'Configure management groups' is asynchronous or gated. How should completion be recorded? (`LAB04-Q10`)

- A. Record pass as soon as the request is accepted, regardless of its final state.
- B. Fabricate expected output so the assessment and documentation appear complete.
- C. Remove the check from validation whenever the service takes longer than expected.
- D. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
