# Lab 08 knowledge check

Manage Blob lifecycle, tiers, versioning, replication, and AzCopy

Choose one answer for each question before opening the answer key.

## 1. Which statement best captures the key design principle for manage blob lifecycle, tiers, versioning, replication, and azcopy? (`LAB08-Q01`)

- A. Object replication depends on versioning and change feed, while lifecycle rules act asynchronously and should be validated as configuration rather than immediate data movement.
- B. Every related control is interchangeable, so choose whichever command is shortest.
- C. A command surface automatically supplies any missing authorization or configuration.
- D. Cleanup evidence is unnecessary when a resource group has a recognizable name.

## 2. You must begin the hands-on path for 'Configure object replication'. Which action matches the reviewed lab sequence? (`LAB08-Q02`)

- A. Delete similarly named resources before recording the current subscription.
- B. Create source and destination general-purpose v2 accounts with change feed and blob versioning.
- C. Change the active tenant automatically and continue without displaying the new context.
- D. Infer configuration from resource names without querying the live control plane.

## 3. Which authorization statement is appropriate before creating resource group, two StorageV2 accounts, blob containers in this lab? (`LAB08-Q03`)

- A. Subscription Reader is sufficient for every create, update, role, policy, and recovery operation.
- B. A local administrator account automatically grants Microsoft Entra and Azure permissions.
- C. Confirm the active context and obtain only the declared role boundary: Contributor and Storage Blob Data Contributor on the lab resource group
- D. Skip authorization checks because all resources use an AZ104 naming prefix.

## 4. The setup command for Lab 08 is run without its execution switch. What should happen? (`LAB08-Q04`)

- A. It should deploy everything and ask for confirmation only before cleanup.
- B. It should log in interactively and select the first available subscription.
- C. It should delete any older run that shares the same lab number.
- D. It should print the intended resources, context, cost class, and gates without changing Azure.

## 5. Which validation evidence most directly proves the baseline resource boundary for Lab 08? (`LAB08-Q05`)

- A. Query the exact recorded scope and verify the intended resource/object types, including Microsoft.Storage/storageAccounts.
- B. Search the whole tenant by display-name prefix and accept the first match.
- C. Treat a successful setup process exit code as proof of every data-plane and relationship requirement.
- D. Verify only that an Azure subscription exists.

## 6. A learner reaches the externally gated checkpoint in Lab 08. What is the safest response? (`LAB08-Q06`)

- A. Invent a placeholder tenant, email address, domain, or production target and continue.
- B. Stop that branch unless its prerequisites are explicitly satisfied: None beyond the declared role and a disposable subscription.
- C. Broaden the assignment to subscription scope so the gate no longer applies.
- D. Mark the checkpoint as passed because the offline tests succeeded.

## 7. Which command-side evidence best supports the first completed checkpoint in Lab 08? (`LAB08-Q07`)

- A. Copy a successful command from an unrelated tenant and treat it as this run's evidence.
- B. Record access tokens and keys so another learner can replay the same session.
- C. Run the independent validator and retain redacted structured output for the exact recorded scope after: Create source and destination general-purpose v2 accounts with change feed and blob versioning.
- D. Use the setup process exit code alone without querying resource state.

## 8. During cleanup of Lab 08, several similarly named resources exist. Which targeting method is correct? (`LAB08-Q08`)

- A. Delete every resource whose name contains az104.
- B. Delete the active subscription to guarantee that no lab resources remain.
- C. Use creation timestamps alone and remove the oldest matching resources.
- D. Use the exact IDs and run metadata recorded before creation, verify the lab tags, then delete only that boundary.

## 9. Setup completed for Lab 08, but one required state check fails. What is the best break/fix approach? (`LAB08-Q09`)

- A. Inspect the failing check and exact recorded resource, repair the smallest identified cause, then rerun validation.
- B. Rerun setup repeatedly with new names until one run reports no error.
- C. Edit validation.json so the failed status reads pass.
- D. Disable all policies, locks, NSGs, and monitoring controls in the subscription.

## 10. Which completion claim is valid immediately after this repository's offline tests pass for Lab 08? (`LAB08-Q10`)

- A. Every command has been proven in every Azure region and tenant type.
- B. The documentation, schemas, script contracts, assessments, diagrams, and fixtures are offline-validated; live Azure state remains pending until executed.
- C. The lab is live-verified even if no subscription was used.
- D. Any pending gated checkpoint can be treated as successfully completed.
