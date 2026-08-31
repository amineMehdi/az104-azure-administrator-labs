# Lab 25 knowledge check

Replicate and fail over an Azure VM with Site Recovery

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Configure Azure Site Recovery for Azure resources' in Lab 25? (`LAB25-Q01`)

- A. Test failover validates recovery without committing production direction, while planned/unplanned failover, commit, reprotect, and failback are separate state transitions with cost and data-loss implications.
- B. The shortest command is always correct even when it changes a broader scope.
- C. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- D. A recognizable resource name removes the need for validation and scoped cleanup.

## 2. Which lab action directly supports the objective 'Perform a failover to a secondary region by using Site Recovery'? (`LAB25-Q02`)

- A. Change the active tenant without displaying or confirming the resulting context.
- B. Create a source VM and Recovery Services vault, then configure Azure-to-Azure fabric, container, policy, and network mappings.
- C. Search the whole tenant for a similar display name and modify the first match.
- D. Mark the objective complete after reading documentation without checking any state.

## 3. Which authorization approach is appropriate before practicing 'Configure Azure Site Recovery for Azure resources'? (`LAB25-Q03`)

- A. Use a production subscription because its resources already exist.
- B. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- C. Confirm the active context and use only the declared role boundary: Site Recovery Contributor, Virtual Machine Contributor, and Network Contributor on both region scopes
- D. Skip role checks when the run ID contains the lab number.

## 4. A learner previews the implementation for 'Perform a failover to a secondary region by using Site Recovery'. What behavior is required? (`LAB25-Q04`)

- A. Create the baseline immediately and request approval only before cleanup.
- B. Select the first accessible subscription and hide the resulting context.
- C. Delete any older resource whose name resembles the new run ID.
- D. Display the context, intended changes, cost and gated branches without mutating Azure.

## 5. Which implementation step should the learner perform for 'Configure Azure Site Recovery for Azure resources'? (`LAB25-Q05`)

- A. Create non-overlapping source and recovery VNets in the configured primary and secondary regions.
- B. Replace the lab action with a tenant-wide change that is easier to discover.
- C. Copy resource identifiers from another run instead of recording returned IDs.
- D. Skip the operation and edit validation.json to show a passing result.

## 6. Which evidence most directly validates 'Perform a failover to a secondary region by using Site Recovery' for replicated item? (`LAB25-Q06`)

- A. Treat the setup exit code as proof of every configuration and relationship.
- B. Query the exact recorded scope and independently verify Microsoft.Network/virtualNetworks.
- C. List the entire subscription and assume similarly named resources belong to this run.
- D. Record a credential so another learner can replay the authenticated session.

## 7. The 'Configure Azure Site Recovery for Azure resources' checkpoint reaches an external prerequisite. What should happen? (`LAB25-Q07`)

- A. Invent a domain, notification target, license, quota, or tenant value and continue.
- B. Broaden permissions until the prerequisite can no longer block the operation.
- C. Run the branch only when this documented gate is satisfied: This elevated lab requires two approved regions and explicit cost review before live execution; test failover must use an isolated network.
- D. Mark the branch passed because its command syntax was checked offline.

## 8. What is the safest command-evidence practice after completing 'Perform a failover to a secondary region by using Site Recovery'? (`LAB25-Q08`)

- A. Commit the complete account object so reviewers can identify the tenant.
- B. Save tokens, keys, passwords, or SAS values beside the validation result.
- C. Reuse successful output from an earlier run with a similar resource name.
- D. Retain only redacted structured output from an independent query of the recorded run.

## 9. Validation for 'Configure Azure Site Recovery for Azure resources' fails after setup. What is the best break/fix method? (`LAB25-Q09`)

- A. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- B. Rerun setup repeatedly with new names until one attempt appears successful.
- C. Change validation.json directly so the failed result reads pass.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.

## 10. The operation for 'Perform a failover to a secondary region by using Site Recovery' is asynchronous or gated. How should completion be recorded? (`LAB25-Q10`)

- A. Record pass as soon as the request is accepted, regardless of its final state.
- B. Record the observed state and timestamp, and keep the result warning, skipped, or partial until final evidence exists.
- C. Fabricate expected output so the assessment and documentation appear complete.
- D. Remove the check from validation whenever the service takes longer than expected.
