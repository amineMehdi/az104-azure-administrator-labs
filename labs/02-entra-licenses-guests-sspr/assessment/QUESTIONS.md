# Lab 02 knowledge check

Manage Entra licenses, guests, and self-service password reset

Choose one answer for each question before opening the answer key.

## 1. Which statement best captures the key design principle for manage entra licenses, guests, and self-service password reset? (`LAB02-Q01`)

- A. SSPR and group-based licensing are tenant capabilities with role and license gates; inventory and scoped pilots are safer than tenant-wide changes.
- B. Every related control is interchangeable, so choose whichever command is shortest.
- C. A command surface automatically supplies any missing authorization or configuration.
- D. Cleanup evidence is unnecessary when a resource group has a recognizable name.

## 2. You must begin the hands-on path for 'Manage licenses in Microsoft Entra ID'. Which action matches the reviewed lab sequence? (`LAB02-Q02`)

- A. Delete similarly named resources before recording the current subscription.
- B. Create a security group that represents the SSPR pilot cohort.
- C. Change the active tenant automatically and continue without displaying the new context.
- D. Infer configuration from resource names without querying the live control plane.

## 3. Which authorization statement is appropriate before creating security group, invited guest user, optional license assignment in this lab? (`LAB02-Q03`)

- A. Subscription Reader is sufficient for every create, update, role, policy, and recovery operation.
- B. A local administrator account automatically grants Microsoft Entra and Azure permissions.
- C. Confirm the active context and obtain only the declared role boundary: User Administrator and License Administrator; Authentication Policy Administrator for the SSPR policy path
- D. Skip authorization checks because all resources use an AZ104 naming prefix.

## 4. The setup command for Lab 02 is run without its execution switch. What should happen? (`LAB02-Q04`)

- A. It should deploy everything and ask for confirmation only before cleanup.
- B. It should log in interactively and select the first available subscription.
- C. It should delete any older run that shares the same lab number.
- D. It should print the intended resources, context, cost class, and gates without changing Azure.

## 5. Which validation evidence most directly proves the baseline resource boundary for Lab 02? (`LAB02-Q05`)

- A. Query the exact recorded scope and verify the intended resource/object types, including the exact recorded object IDs.
- B. Search the whole tenant by display-name prefix and accept the first match.
- C. Treat a successful setup process exit code as proof of every data-plane and relationship requirement.
- D. Verify only that an Azure subscription exists.

## 6. A learner reaches the externally gated checkpoint in Lab 02. What is the safest response? (`LAB02-Q06`)

- A. Invent a placeholder tenant, email address, domain, or production target and continue.
- B. Stop that branch unless its prerequisites are explicitly satisfied: Requires a real disposable guest email for invitation, an available SKU for license assignment, and an authorized tenant policy change for SSPR.
- C. Broaden the assignment to subscription scope so the gate no longer applies.
- D. Mark the checkpoint as passed because the offline tests succeeded.

## 7. Which command-side evidence best supports the first completed checkpoint in Lab 02? (`LAB02-Q07`)

- A. Copy a successful command from an unrelated tenant and treat it as this run's evidence.
- B. Record access tokens and keys so another learner can replay the same session.
- C. Run the independent validator and retain redacted structured output for the exact recorded scope after: Create a security group that represents the SSPR pilot cohort.
- D. Use the setup process exit code alone without querying resource state.

## 8. During cleanup of Lab 02, several similarly named resources exist. Which targeting method is correct? (`LAB02-Q08`)

- A. Delete every resource whose name contains az104.
- B. Delete the active subscription to guarantee that no lab resources remain.
- C. Use creation timestamps alone and remove the oldest matching resources.
- D. Use the exact IDs and run metadata recorded before creation, verify the lab tags, then delete only that boundary.

## 9. Setup completed for Lab 02, but one required state check fails. What is the best break/fix approach? (`LAB02-Q09`)

- A. Inspect the failing check and exact recorded resource, repair the smallest identified cause, then rerun validation.
- B. Rerun setup repeatedly with new names until one run reports no error.
- C. Edit validation.json so the failed status reads pass.
- D. Disable all policies, locks, NSGs, and monitoring controls in the subscription.

## 10. Which completion claim is valid immediately after this repository's offline tests pass for Lab 02? (`LAB02-Q10`)

- A. Every command has been proven in every Azure region and tenant type.
- B. The documentation, schemas, script contracts, assessments, diagrams, and fixtures are offline-validated; live Azure state remains pending until executed.
- C. The lab is live-verified even if no subscription was used.
- D. Any pending gated checkpoint can be treated as successfully completed.
