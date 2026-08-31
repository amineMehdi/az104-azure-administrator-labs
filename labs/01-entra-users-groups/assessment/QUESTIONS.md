# Lab 01 knowledge check

Choose the single best answer for each question. Record your choices before opening `ANSWERS.md`.

## LAB01-Q01 — Foundational

An administrator is creating a cloud-only Microsoft Entra user. Which UPN requirement must be satisfied?

- A. The UPN must use the tenant's initial domain only.
- B. The UPN suffix must be one of the tenant's verified domains.
- C. The UPN must use the same name as an Azure subscription.
- D. The UPN must match the administrator's email address.

## LAB01-Q02 — Foundational

You need a Microsoft Entra group for assigning access to Azure resources, without creating an email collaboration group. Which group properties fit the requirement?

- A. securityEnabled=false and mailEnabled=false
- B. securityEnabled=true and mailEnabled=true with dynamic membership
- C. securityEnabled=true and mailEnabled=false
- D. securityEnabled=false and mailEnabled=true

## LAB01-Q03 — Foundational

A learner is Owner of an Azure subscription but receives an authorization error when creating Microsoft Entra users. What is the best explanation?

- A. Cloud-only users can be created only by Microsoft Support.
- B. The subscription must be moved to the same region as the tenant.
- C. The Owner role works only after the Microsoft.Graph resource provider is registered.
- D. Azure RBAC Owner does not grant Microsoft Entra directory-management permissions.

## LAB01-Q04 — Foundational

Before making a change, a learner checks this core behavior: An administrator is creating a cloud-only Microsoft Entra user. Which UPN requirement must be satisfied?

- A. The UPN suffix must be one of the tenant's verified domains.
- B. The UPN must use the same name as an Azure subscription.
- C. The UPN must match the administrator's email address.
- D. The UPN must use the tenant's initial domain only.

## LAB01-Q05 — Foundational

During a design vocabulary review, the team evaluates this situation: You need a Microsoft Entra group for assigning access to Azure resources, without creating an email collaboration group. Which group properties fit the requirement?

- A. securityEnabled=true and mailEnabled=true with dynamic membership
- B. securityEnabled=true and mailEnabled=false
- C. securityEnabled=false and mailEnabled=true
- D. securityEnabled=false and mailEnabled=false

## LAB01-Q06 — Foundational

In a command-planning session, an administrator asks this question: A learner is Owner of an Azure subscription but receives an authorization error when creating Microsoft Entra users. What is the best explanation?

- A. The subscription must be moved to the same region as the tenant.
- B. The Owner role works only after the Microsoft.Graph resource provider is registered.
- C. Azure RBAC Owner does not grant Microsoft Entra directory-management permissions.
- D. Cloud-only users can be created only by Microsoft Support.

## LAB01-Q07 — Foundational

While preparing the lab, a learner verifies this platform rule: An administrator is creating a cloud-only Microsoft Entra user. Which UPN requirement must be satisfied?

- A. The UPN must use the same name as an Azure subscription.
- B. The UPN must match the administrator's email address.
- C. The UPN must use the tenant's initial domain only.
- D. The UPN suffix must be one of the tenant's verified domains.

## LAB01-Q08 — Foundational

During peer review, the team must identify the accurate response to this scenario: You need a Microsoft Entra group for assigning access to Azure resources, without creating an email collaboration group. Which group properties fit the requirement?

- A. securityEnabled=true and mailEnabled=false
- B. securityEnabled=false and mailEnabled=true
- C. securityEnabled=false and mailEnabled=false
- D. securityEnabled=true and mailEnabled=true with dynamic membership

## LAB01-Q09 — Foundational

In an operations briefing, a new team member receives this question: A learner is Owner of an Azure subscription but receives an authorization error when creating Microsoft Entra users. What is the best explanation?

- A. The Owner role works only after the Microsoft.Graph resource provider is registered.
- B. Azure RBAC Owner does not grant Microsoft Entra directory-management permissions.
- C. Cloud-only users can be created only by Microsoft Support.
- D. The subscription must be moved to the same region as the tenant.

## LAB01-Q10 — Foundational

While building a support checklist, an engineer reviews this requirement: An administrator is creating a cloud-only Microsoft Entra user. Which UPN requirement must be satisfied?

- A. The UPN must match the administrator's email address.
- B. The UPN must use the tenant's initial domain only.
- C. The UPN suffix must be one of the tenant's verified domains.
- D. The UPN must use the same name as an Azure subscription.

## LAB01-Q11 — Foundational

During a readiness check, the administrator considers this behavior: You need a Microsoft Entra group for assigning access to Azure resources, without creating an email collaboration group. Which group properties fit the requirement?

- A. securityEnabled=false and mailEnabled=true
- B. securityEnabled=false and mailEnabled=false
- C. securityEnabled=true and mailEnabled=true with dynamic membership
- D. securityEnabled=true and mailEnabled=false

## LAB01-Q12 — Foundational

In a service overview, the team discusses this scenario: A learner is Owner of an Azure subscription but receives an authorization error when creating Microsoft Entra users. What is the best explanation?

- A. Azure RBAC Owner does not grant Microsoft Entra directory-management permissions.
- B. Cloud-only users can be created only by Microsoft Support.
- C. The subscription must be moved to the same region as the tenant.
- D. The Owner role works only after the Microsoft.Graph resource provider is registered.

## LAB01-Q13 — Foundational

While reviewing official guidance, a learner must resolve this question: An administrator is creating a cloud-only Microsoft Entra user. Which UPN requirement must be satisfied?

- A. The UPN must use the tenant's initial domain only.
- B. The UPN suffix must be one of the tenant's verified domains.
- C. The UPN must use the same name as an Azure subscription.
- D. The UPN must match the administrator's email address.

## LAB01-Q14 — Foundational

During a configuration walkthrough, the instructor asks about this situation: You need a Microsoft Entra group for assigning access to Azure resources, without creating an email collaboration group. Which group properties fit the requirement?

- A. securityEnabled=false and mailEnabled=false
- B. securityEnabled=true and mailEnabled=true with dynamic membership
- C. securityEnabled=true and mailEnabled=false
- D. securityEnabled=false and mailEnabled=true

## LAB01-Q15 — Foundational

In a preflight knowledge check, the operator evaluates this requirement: A learner is Owner of an Azure subscription but receives an authorization error when creating Microsoft Entra users. What is the best explanation?

- A. Cloud-only users can be created only by Microsoft Support.
- B. The subscription must be moved to the same region as the tenant.
- C. The Owner role works only after the Microsoft.Graph resource provider is registered.
- D. Azure RBAC Owner does not grant Microsoft Entra directory-management permissions.

## LAB01-Q16 — Applied

You create a temporary cloud user for a lab. Which password-profile choice most directly reduces the risk of the bootstrap password remaining valid as the user's long-term secret?

- A. Set forceChangePasswordNextSignIn to true and avoid persisting the password.
- B. Store the password in the group's description for the owner.
- C. Disable password expiration for the account.
- D. Reuse the administrator's password and delete shell history.

## LAB01-Q17 — Applied

A script has the exact object ID of a security group and the exact object ID of a user. Which Azure CLI operation creates the intended direct membership?

- A. az group update --name \<group-id\> --add members \<user-id\>
- B. az ad group member add --group \<group-id\> --member-id \<user-id\>
- C. az role assignment create --assignee \<group-id\> --scope \<user-id\>
- D. az ad user update --id \<user-id\> --group \<group-id\>

## LAB01-Q18 — Applied

The simplified az ad user update command does not expose the department and jobTitle properties you must change. What is the most appropriate command-first approach?

- A. Rename the Azure subscription so that its tags become user properties.
- B. Create a second user with the desired properties and leave the first user active.
- C. Send an authenticated Microsoft Graph PATCH request for the recorded user ID with az rest.
- D. Edit the local Azure CLI token cache and repeat az ad user show.

## LAB01-Q19 — Applied

User B is added as an owner of a security group but is intentionally not added as a member. Which statement correctly describes the result?

- A. A group cannot have an owner unless that owner is also a direct member.
- B. Ownership converts the security group into a Microsoft 365 group.
- C. The owner is always treated as a transitive member for every access assignment.
- D. Ownership and membership are separate relationships; ownership does not automatically grant member-based access.

## LAB01-Q20 — Applied

A tenant contains two groups with similar display names. Which value should an automated cleanup use to delete only the group created by its own run?

- A. The exact immutable group object ID recorded immediately after creation
- B. The first group returned by a display-name prefix search
- C. The group's position in the Microsoft Entra admin center list
- D. The Azure subscription ID active when the group was created

## LAB01-Q21 — Applied

While validating a configuration, the team evaluates this situation: You create a temporary cloud user for a lab. Which password-profile choice most directly reduces the risk of the bootstrap password remaining valid as the user's long-term secret?

- A. Reuse the administrator's password and delete shell history.
- B. Set forceChangePasswordNextSignIn to true and avoid persisting the password.
- C. Store the password in the group's description for the owner.
- D. Disable password expiration for the account.

## LAB01-Q22 — Applied

A delegated administrator receives the following support request: A script has the exact object ID of a security group and the exact object ID of a user. Which Azure CLI operation creates the intended direct membership?

- A. az ad user update --id \<user-id\> --group \<group-id\>
- B. az group update --name \<group-id\> --add members \<user-id\>
- C. az ad group member add --group \<group-id\> --member-id \<user-id\>
- D. az role assignment create --assignee \<group-id\> --scope \<user-id\>

## LAB01-Q23 — Applied

During a maintenance window, an engineer must decide how to respond: The simplified az ad user update command does not expose the department and jobTitle properties you must change. What is the most appropriate command-first approach?

- A. Edit the local Azure CLI token cache and repeat az ad user show.
- B. Rename the Azure subscription so that its tags become user properties.
- C. Create a second user with the desired properties and leave the first user active.
- D. Send an authenticated Microsoft Graph PATCH request for the recorded user ID with az rest.

## LAB01-Q24 — Applied

A deployment pipeline reaches this decision point: User B is added as an owner of a security group but is intentionally not added as a member. Which statement correctly describes the result?

- A. Ownership and membership are separate relationships; ownership does not automatically grant member-based access.
- B. A group cannot have an owner unless that owner is also a direct member.
- C. Ownership converts the security group into a Microsoft 365 group.
- D. The owner is always treated as a transitive member for every access assignment.

## LAB01-Q25 — Applied

While applying least-privilege controls, the administrator reviews this scenario: A tenant contains two groups with similar display names. Which value should an automated cleanup use to delete only the group created by its own run?

- A. The Azure subscription ID active when the group was created
- B. The exact immutable group object ID recorded immediately after creation
- C. The first group returned by a display-name prefix search
- D. The group's position in the Microsoft Entra admin center list

## LAB01-Q26 — Applied

A repeatable Azure CLI workflow must address this requirement: You create a temporary cloud user for a lab. Which password-profile choice most directly reduces the risk of the bootstrap password remaining valid as the user's long-term secret?

- A. Disable password expiration for the account.
- B. Reuse the administrator's password and delete shell history.
- C. Set forceChangePasswordNextSignIn to true and avoid persisting the password.
- D. Store the password in the group's description for the owner.

## LAB01-Q27 — Applied

During an environment handoff, the receiving team asks this question: A script has the exact object ID of a security group and the exact object ID of a user. Which Azure CLI operation creates the intended direct membership?

- A. az role assignment create --assignee \<group-id\> --scope \<user-id\>
- B. az ad user update --id \<user-id\> --group \<group-id\>
- C. az group update --name \<group-id\> --add members \<user-id\>
- D. az ad group member add --group \<group-id\> --member-id \<user-id\>

## LAB01-Q28 — Applied

A configuration change produces the following operational choice: The simplified az ad user update command does not expose the department and jobTitle properties you must change. What is the most appropriate command-first approach?

- A. Send an authenticated Microsoft Graph PATCH request for the recorded user ID with az rest.
- B. Edit the local Azure CLI token cache and repeat az ad user show.
- C. Rename the Azure subscription so that its tags become user properties.
- D. Create a second user with the desired properties and leave the first user active.

## LAB01-Q29 — Applied

While preparing independent validation, an engineer considers this scenario: User B is added as an owner of a security group but is intentionally not added as a member. Which statement correctly describes the result?

- A. The owner is always treated as a transitive member for every access assignment.
- B. Ownership and membership are separate relationships; ownership does not automatically grant member-based access.
- C. A group cannot have an owner unless that owner is also a direct member.
- D. Ownership converts the security group into a Microsoft 365 group.

## LAB01-Q30 — Applied

A service owner asks the administrator to resolve this requirement: A tenant contains two groups with similar display names. Which value should an automated cleanup use to delete only the group created by its own run?

- A. The group's position in the Microsoft Entra admin center list
- B. The Azure subscription ID active when the group was created
- C. The exact immutable group object ID recorded immediately after creation
- D. The first group returned by a display-name prefix search

## LAB01-Q31 — Applied

During a scoped cleanup review, the team evaluates this situation: You create a temporary cloud user for a lab. Which password-profile choice most directly reduces the risk of the bootstrap password remaining valid as the user's long-term secret?

- A. Store the password in the group's description for the owner.
- B. Disable password expiration for the account.
- C. Reuse the administrator's password and delete shell history.
- D. Set forceChangePasswordNextSignIn to true and avoid persisting the password.

## LAB01-Q32 — Applied

An automation author must choose the correct response to this scenario: A script has the exact object ID of a security group and the exact object ID of a user. Which Azure CLI operation creates the intended direct membership?

- A. az ad group member add --group \<group-id\> --member-id \<user-id\>
- B. az role assignment create --assignee \<group-id\> --scope \<user-id\>
- C. az ad user update --id \<user-id\> --group \<group-id\>
- D. az group update --name \<group-id\> --add members \<user-id\>

## LAB01-Q33 — Applied

A lab run with a unique run ID reaches this decision: The simplified az ad user update command does not expose the department and jobTitle properties you must change. What is the most appropriate command-first approach?

- A. Create a second user with the desired properties and leave the first user active.
- B. Send an authenticated Microsoft Graph PATCH request for the recorded user ID with az rest.
- C. Edit the local Azure CLI token cache and repeat az ad user show.
- D. Rename the Azure subscription so that its tags become user properties.

## LAB01-Q34 — Applied

While comparing the intended and actual states, the operator asks this question: User B is added as an owner of a security group but is intentionally not added as a member. Which statement correctly describes the result?

- A. Ownership converts the security group into a Microsoft 365 group.
- B. The owner is always treated as a transitive member for every access assignment.
- C. Ownership and membership are separate relationships; ownership does not automatically grant member-based access.
- D. A group cannot have an owner unless that owner is also a direct member.

## LAB01-Q35 — Applied

A peer reviewer examines the proposed implementation for this scenario: A tenant contains two groups with similar display names. Which value should an automated cleanup use to delete only the group created by its own run?

- A. The first group returned by a display-name prefix search
- B. The group's position in the Microsoft Entra admin center list
- C. The Azure subscription ID active when the group was created
- D. The exact immutable group object ID recorded immediately after creation

## LAB01-Q36 — Applied

During a controlled rollout, the change team encounters this requirement: You create a temporary cloud user for a lab. Which password-profile choice most directly reduces the risk of the bootstrap password remaining valid as the user's long-term secret?

- A. Set forceChangePasswordNextSignIn to true and avoid persisting the password.
- B. Store the password in the group's description for the owner.
- C. Disable password expiration for the account.
- D. Reuse the administrator's password and delete shell history.

## LAB01-Q37 — Applied

A support engineer reproduces the following situation in a test environment: A script has the exact object ID of a security group and the exact object ID of a user. Which Azure CLI operation creates the intended direct membership?

- A. az group update --name \<group-id\> --add members \<user-id\>
- B. az ad group member add --group \<group-id\> --member-id \<user-id\>
- C. az role assignment create --assignee \<group-id\> --scope \<user-id\>
- D. az ad user update --id \<user-id\> --group \<group-id\>

## LAB01-Q38 — Applied

While recording validation evidence, the administrator evaluates this question: The simplified az ad user update command does not expose the department and jobTitle properties you must change. What is the most appropriate command-first approach?

- A. Rename the Azure subscription so that its tags become user properties.
- B. Create a second user with the desired properties and leave the first user active.
- C. Send an authenticated Microsoft Graph PATCH request for the recorded user ID with az rest.
- D. Edit the local Azure CLI token cache and repeat az ad user show.

## LAB01-Q39 — Applied

A configuration owner must approve one response to this scenario: User B is added as an owner of a security group but is intentionally not added as a member. Which statement correctly describes the result?

- A. A group cannot have an owner unless that owner is also a direct member.
- B. Ownership converts the security group into a Microsoft 365 group.
- C. The owner is always treated as a transitive member for every access assignment.
- D. Ownership and membership are separate relationships; ownership does not automatically grant member-based access.

## LAB01-Q40 — Applied

During post-deployment verification, the team reviews this situation: A tenant contains two groups with similar display names. Which value should an automated cleanup use to delete only the group created by its own run?

- A. The exact immutable group object ID recorded immediately after creation
- B. The first group returned by a display-name prefix search
- C. The group's position in the Microsoft Entra admin center list
- D. The Azure subscription ID active when the group was created

## LAB01-Q41 — Advanced

Cleanup deletes the lab security group and both cloud users by exact ID. Validation can no longer read the active users, but they appear under Deleted users. How should this state be interpreted?

- A. Cleanup failed because user deletion is unsupported in Microsoft Entra ID.
- B. Active cleanup succeeded; user deletion is recoverable until retention expires or an authorized permanent deletion occurs.
- C. The users automatically became external guests and must be invited again.
- D. The Azure subscription must be deleted to remove the user objects permanently.

## LAB01-Q42 — Advanced

A validation report must prove the intended group relationships and detect accidental privilege expansion. Which pair of checks provides the strongest evidence for this lab design?

- A. Confirm both users exist and skip group relationship queries to reduce API calls.
- B. Confirm user B is an owner and automatically add every owner as a member.
- C. Confirm user A is a direct member and independently confirm user B is an owner but not a direct member.
- D. Confirm the group display name starts with AZ104 and assume all relationships are correct.

## LAB01-Q43 — Advanced

A security and reliability review identifies this design decision: Cleanup deletes the lab security group and both cloud users by exact ID. Validation can no longer read the active users, but they appear under Deleted users. How should this state be interpreted?

- A. The users automatically became external guests and must be invited again.
- B. The Azure subscription must be deleted to remove the user objects permanently.
- C. Cleanup failed because user deletion is unsupported in Microsoft Entra ID.
- D. Active cleanup succeeded; user deletion is recoverable until retention expires or an authorized permanent deletion occurs.

## LAB01-Q44 — Advanced

While diagnosing unexpected Azure behavior, the engineer considers this situation: A validation report must prove the intended group relationships and detect accidental privilege expansion. Which pair of checks provides the strongest evidence for this lab design?

- A. Confirm user A is a direct member and independently confirm user B is an owner but not a direct member.
- B. Confirm the group display name starts with AZ104 and assume all relationships are correct.
- C. Confirm both users exist and skip group relationship queries to reduce API calls.
- D. Confirm user B is an owner and automatically add every owner as a member.

## LAB01-Q45 — Advanced

An architecture review requires the strongest response to this scenario: Cleanup deletes the lab security group and both cloud users by exact ID. Validation can no longer read the active users, but they appear under Deleted users. How should this state be interpreted?

- A. Cleanup failed because user deletion is unsupported in Microsoft Entra ID.
- B. Active cleanup succeeded; user deletion is recoverable until retention expires or an authorized permanent deletion occurs.
- C. The users automatically became external guests and must be invited again.
- D. The Azure subscription must be deleted to remove the user objects permanently.

## LAB01-Q46 — Advanced

During break/fix validation, the operator encounters this question: A validation report must prove the intended group relationships and detect accidental privilege expansion. Which pair of checks provides the strongest evidence for this lab design?

- A. Confirm both users exist and skip group relationship queries to reduce API calls.
- B. Confirm user B is an owner and automatically add every owner as a member.
- C. Confirm user A is a direct member and independently confirm user B is an owner but not a direct member.
- D. Confirm the group display name starts with AZ104 and assume all relationships are correct.

## LAB01-Q47 — Advanced

A complex support case depends on correctly interpreting this requirement: Cleanup deletes the lab security group and both cloud users by exact ID. Validation can no longer read the active users, but they appear under Deleted users. How should this state be interpreted?

- A. The users automatically became external guests and must be invited again.
- B. The Azure subscription must be deleted to remove the user objects permanently.
- C. Cleanup failed because user deletion is unsupported in Microsoft Entra ID.
- D. Active cleanup succeeded; user deletion is recoverable until retention expires or an authorized permanent deletion occurs.

## LAB01-Q48 — Advanced

While correcting configuration drift, the team evaluates this scenario: A validation report must prove the intended group relationships and detect accidental privilege expansion. Which pair of checks provides the strongest evidence for this lab design?

- A. Confirm user A is a direct member and independently confirm user B is an owner but not a direct member.
- B. Confirm the group display name starts with AZ104 and assume all relationships are correct.
- C. Confirm both users exist and skip group relationship queries to reduce API calls.
- D. Confirm user B is an owner and automatically add every owner as a member.

## LAB01-Q49 — Advanced

A recovery exercise exposes the following technical decision: Cleanup deletes the lab security group and both cloud users by exact ID. Validation can no longer read the active users, but they appear under Deleted users. How should this state be interpreted?

- A. Cleanup failed because user deletion is unsupported in Microsoft Entra ID.
- B. Active cleanup succeeded; user deletion is recoverable until retention expires or an authorized permanent deletion occurs.
- C. The users automatically became external guests and must be invited again.
- D. The Azure subscription must be deleted to remove the user objects permanently.

## LAB01-Q50 — Advanced

During final design assurance, the reviewer must resolve this situation: A validation report must prove the intended group relationships and detect accidental privilege expansion. Which pair of checks provides the strongest evidence for this lab design?

- A. Confirm both users exist and skip group relationship queries to reduce API calls.
- B. Confirm user B is an owner and automatically add every owner as a member.
- C. Confirm user A is a direct member and independently confirm user B is an owner but not a direct member.
- D. Confirm the group display name starts with AZ104 and assume all relationships are correct.
