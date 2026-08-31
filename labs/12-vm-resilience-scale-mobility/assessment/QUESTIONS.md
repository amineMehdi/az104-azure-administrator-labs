# Lab 12 knowledge check

Design VM resilience, scale sets, and mobility

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Move a virtual machine to another resource group, subscription, or region' in Lab 12? (`LAB12-Q01`)

- A. The shortest command is always correct even when it changes a broader scope.
- B. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- C. Availability sets, zones, scale sets, and regional moves solve different resilience or mobility problems and have distinct dependency and cost models.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Manage virtual machine sizes'? (`LAB12-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Search the whole tenant for a similar display name and modify the first match.
- C. Mark the objective complete after reading documentation without checking any state.
- D. Deploy a small flexible orchestration VM scale set with an explicit instance count and upgrade policy.

## 3. A learner previews the implementation for 'Deploy virtual machines to availability zones and availability sets'. What behavior is required? (`LAB12-Q03`)

- A. Display the context, intended changes, cost and gated branches without mutating Azure.
- B. Create the baseline immediately and request approval only before cleanup.
- C. Select the first accessible subscription and hide the resulting context.
- D. Delete any older resource whose name resembles the new run ID.

## 4. Which implementation step should the learner perform for 'Deploy and configure an Azure Virtual Machine Scale Sets'? (`LAB12-Q04`)

- A. Replace the lab action with a tenant-wide change that is easier to discover.
- B. Use move validation for a destination resource group and document the different process required for another region or subscription.
- C. Copy resource identifiers from another run instead of recording returned IDs.
- D. Skip the operation and edit validation.json to show a passing result.

## 5. Which evidence most directly validates 'Move a virtual machine to another resource group, subscription, or region' for autoscale setting? (`LAB12-Q05`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. List the entire subscription and assume similarly named resources belong to this run.
- C. Query the exact recorded scope and independently verify Microsoft.Compute/virtualMachineScaleSets.
- D. Record a credential so another learner can replay the authenticated session.

## 6. The 'Manage virtual machine sizes' checkpoint reaches an external prerequisite. What should happen? (`LAB12-Q06`)

- A. Invent a domain, notification target, license, quota, or tenant value and continue.
- B. Broaden permissions until the prerequisite can no longer block the operation.
- C. Mark the branch passed because its command syntax was checked offline.
- D. Run the branch only when this documented gate is satisfied: None beyond the declared role and a disposable subscription.

## 7. Validation for 'Deploy virtual machines to availability zones and availability sets' fails after setup. What is the best break/fix method? (`LAB12-Q07`)

- A. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- B. Rerun setup repeatedly with new names until one attempt appears successful.
- C. Change validation.json directly so the failed result reads pass.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.

## 8. The operation for 'Deploy and configure an Azure Virtual Machine Scale Sets' is asynchronous or gated. How should completion be recorded? (`LAB12-Q08`)

- A. Record pass as soon as the request is accepted, regardless of its final state.
- B. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
- C. Fabricate expected output so the assessment and documentation appear complete.
- D. Remove the check from validation whenever the service takes longer than expected.
