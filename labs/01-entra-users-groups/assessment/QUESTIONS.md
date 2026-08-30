# Lab 01 knowledge check

Choose the single best answer for each question. Record your choices before opening `ANSWERS.md`.

## LAB01-Q01 — Foundational

An administrator is creating a cloud-only Microsoft Entra user. Which UPN requirement must be satisfied?

- A. The UPN must match the administrator's email address.
- B. The UPN must use the tenant's initial domain only.
- C. The UPN suffix must be one of the tenant's verified domains.
- D. The UPN must use the same name as an Azure subscription.

## LAB01-Q02 — Foundational

You need a Microsoft Entra group for assigning access to Azure resources, without creating an email collaboration group. Which group properties fit the requirement?

- A. `securityEnabled=true` and `mailEnabled=false`
- B. `securityEnabled=false` and `mailEnabled=true`
- C. `securityEnabled=false` and `mailEnabled=false`
- D. `securityEnabled=true` and `mailEnabled=true` with dynamic membership

## LAB01-Q03 — Foundational

A learner is Owner of an Azure subscription but receives an authorization error when creating Microsoft Entra users. What is the best explanation?

- A. The Owner role works only after the Microsoft.Graph resource provider is registered.
- B. Azure RBAC Owner does not grant Microsoft Entra directory-management permissions.
- C. Cloud-only users can be created only by Microsoft Support.
- D. The subscription must be moved to the same region as the tenant.

## LAB01-Q04 — Applied

You create a temporary cloud user for a lab. Which password-profile choice most directly reduces the risk of the bootstrap password remaining valid as the user's long-term secret?

- A. Store the password in the group's description for the owner.
- B. Disable password expiration for the account.
- C. Reuse the administrator's password and delete shell history.
- D. Set `forceChangePasswordNextSignIn` to true and avoid persisting the password.

## LAB01-Q05 — Applied

A script has the exact object ID of a security group and the exact object ID of a user. Which Azure CLI operation creates the intended direct membership?

- A. `az ad group member add --group <group-id> --member-id <user-id>`
- B. `az role assignment create --assignee <group-id> --scope <user-id>`
- C. `az ad user update --id <user-id> --group <group-id>`
- D. `az group update --name <group-id> --add members <user-id>`

## LAB01-Q06 — Applied

The simplified `az ad user update` command does not expose the department and jobTitle properties you must change. What is the most appropriate command-first approach?

- A. Rename the Azure subscription so that its tags become user properties.
- B. Create a second user with the desired properties and leave the first user active.
- C. Send an authenticated Microsoft Graph PATCH request for the recorded user ID with `az rest`.
- D. Edit the local Azure CLI token cache and repeat `az ad user show`.

## LAB01-Q07 — Applied

User B is added as an owner of a security group but is intentionally not added as a member. Which statement correctly describes the result?

- A. The owner is always treated as a transitive member for every access assignment.
- B. Ownership and membership are separate relationships; ownership does not automatically grant member-based access.
- C. A group cannot have an owner unless that owner is also a direct member.
- D. Ownership converts the security group into a Microsoft 365 group.

## LAB01-Q08 — Applied

A tenant contains two groups with similar display names. Which value should an automated cleanup use to delete only the group created by its own run?

- A. The first group returned by a display-name prefix search
- B. The group's position in the Microsoft Entra admin center list
- C. The Azure subscription ID active when the group was created
- D. The exact immutable group object ID recorded immediately after creation

## LAB01-Q09 — Advanced

Cleanup deletes the lab security group and both cloud users by exact ID. Validation can no longer read the active users, but they appear under Deleted users. How should this state be interpreted?

- A. Cleanup failed because user deletion is unsupported in Microsoft Entra ID.
- B. Active cleanup succeeded; user deletion is recoverable until retention expires or an authorized permanent deletion occurs.
- C. The users automatically became external guests and must be invited again.
- D. The Azure subscription must be deleted to remove the user objects permanently.

## LAB01-Q10 — Advanced

A validation report must prove the intended group relationships and detect accidental privilege expansion. Which pair of checks provides the strongest evidence for this lab design?

- A. Confirm user A is a direct member and independently confirm user B is an owner but not a direct member.
- B. Confirm the group display name starts with AZ104 and assume all relationships are correct.
- C. Confirm both users exist and skip group relationship queries to reduce API calls.
- D. Confirm user B is an owner and automatically add every owner as a member.
