# Lab 16 knowledge check

Configure App Service TLS, DNS, backup, and networking

Choose one answer for each question before opening the answer key.

## 1. Which principle is most important when working on 'Configure certificates and Transport Layer Security (TLS) for an App Service' in Lab 16? (`LAB16-Q01`)

- A. The shortest command is always correct even when it changes a broader scope.
- B. A successful sign-in automatically supplies every required Azure and Microsoft Entra role.
- C. A recognizable resource name removes the need for validation and scoped cleanup.
- D. Custom hostnames prove DNS control, certificate bindings prove TLS identity, VNet integration governs outbound connectivity, and backups require protected storage access.

## 2. Which lab action directly supports the objective 'Map an existing custom DNS name to an App Service'? (`LAB16-Q02`)

- A. Create a delegated integration subnet and configure regional VNet integration.
- B. Change the active tenant without displaying or confirming the resulting context.
- C. Search the whole tenant for a similar display name and modify the first match.
- D. Mark the objective complete after reading documentation without checking any state.

## 3. Which authorization approach is appropriate before practicing 'Configure backup for an App Service'? (`LAB16-Q03`)

- A. Use a production subscription because its resources already exist.
- B. Confirm the active context and use only the declared role boundary: Website Contributor, Network Contributor, and Storage Account Contributor; control of the DNS zone and certificate for gated paths
- C. Assign Global Administrator and subscription Owner for every lab regardless of the operation.
- D. Skip role checks when the run ID contains the lab number.

## 4. A learner previews the implementation for 'Configure networking settings for an App Service'. What behavior is required? (`LAB16-Q04`)

- A. Create the baseline immediately and request approval only before cleanup.
- B. Select the first accessible subscription and hide the resulting context.
- C. Display the context, intended changes, cost and gated branches without mutating Azure.
- D. Delete any older resource whose name resembles the new run ID.

## 5. Which implementation step should the learner perform for 'Configure certificates and Transport Layer Security (TLS) for an App Service'? (`LAB16-Q05`)

- A. Replace the lab action with a tenant-wide change that is easier to discover.
- B. Copy resource identifiers from another run instead of recording returned IDs.
- C. Skip the operation and edit validation.json to show a passing result.
- D. Create an App Service plan and web app with HTTPS-only and minimum TLS 1.2.

## 6. Which evidence most directly validates 'Map an existing custom DNS name to an App Service' for optional custom hostname and TLS binding? (`LAB16-Q06`)

- A. Query the exact recorded scope and independently verify Microsoft.Web/sites.
- B. Treat the setup exit code as proof of every configuration and relationship.
- C. List the entire subscription and assume similarly named resources belong to this run.
- D. Record a credential so another learner can replay the authenticated session.

## 7. Validation for 'Configure backup for an App Service' fails after setup. What is the best break/fix method? (`LAB16-Q07`)

- A. Rerun setup repeatedly with new names until one attempt appears successful.
- B. Inspect the exact failing query, repair the smallest identified mismatch, and rerun independent validation.
- C. Change validation.json directly so the failed result reads pass.
- D. Disable unrelated policies, locks, network controls, and monitoring across the subscription.
