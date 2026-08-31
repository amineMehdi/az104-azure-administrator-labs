# Lab 01 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB01-Q01 — Foundational

An identity administrator onboarding a small operations team is updating the identity onboarding runbook. The requirement is to use a custom tenant suffix when creating an operations account. Which statement describes Azure behavior correctly?

- A. A cloud-only user is a directory object and does not depend on an Azure subscription resource group.
- B. A cloud user's UPN suffix must be a verified domain in the tenant.
- C. A non-mail-enabled security group uses securityEnabled true and mailEnabled false.
- D. The userType property distinguishes tenant members from business-to-business guest identities.

## LAB01-Q02 — Foundational

An identity onboarding peer review asks how the operations-team identity onboarding should handle this outcome: create a user whose identity exists only in this tenant. Which explanation is accurate?

- A. Properties such as department, job title, and usage location belong to the user directory object.
- B. A group member receives access assigned to the group, whereas an owner only administers the group.
- C. A cloud-only user is a directory object and does not depend on an Azure subscription resource group.
- D. A soft-deleted Microsoft Entra user can normally be restored during the directory retention window.

## LAB01-Q03 — Foundational

For the operations-team identity onboarding, the identity onboarding plan must capture organizational profile metadata on the directory object. Which statement about identity onboarding belongs in the operations-team identity onboarding record?

- A. Properties such as department, job title, and usage location belong to the user directory object.
- B. The accountEnabled property controls whether a Microsoft Entra user can authenticate.
- C. Group owners can manage group membership but ownership does not itself make them members.
- D. Object IDs remain the reliable automation key when display names or UPN values change.

## LAB01-Q04 — Foundational

The identity onboarding review compares four claims for the operations-team identity onboarding requirement to block one user from signing in without deleting the account. Which claim is technically sound?

- A. A non-mail-enabled security group uses securityEnabled true and mailEnabled false.
- B. The userType property distinguishes tenant members from business-to-business guest identities.
- C. A cloud user's UPN suffix must be a verified domain in the tenant.
- D. The accountEnabled property controls whether a Microsoft Entra user can authenticate.

## LAB01-Q05 — Foundational

The identity onboarding architecture note requires the operations-team identity onboarding environment to build a security-only group that has no email address. Which statement defines the relevant identity onboarding boundary?

- A. A group member receives access assigned to the group, whereas an owner only administers the group.
- B. A non-mail-enabled security group uses securityEnabled true and mailEnabled false.
- C. A soft-deleted Microsoft Entra user can normally be restored during the directory retention window.
- D. A cloud-only user is a directory object and does not depend on an Azure subscription resource group.

## LAB01-Q06 — Foundational

A new identity onboarding operator must explain why the operations-team identity onboarding can give a user the access assigned to an operations group. Which explanation is accurate?

- A. Group owners can manage group membership but ownership does not itself make them members.
- B. A group member receives access assigned to the group, whereas an owner only administers the group.
- C. Object IDs remain the reliable automation key when display names or UPN values change.
- D. Properties such as department, job title, and usage location belong to the user directory object.

## LAB01-Q07 — Foundational

The operations-team identity onboarding acceptance criteria require operators to let an administrator manage membership without receiving the group's access. Which service fact supports that requirement?

- A. Group owners can manage group membership but ownership does not itself make them members.
- B. The userType property distinguishes tenant members from business-to-business guest identities.
- C. A cloud user's UPN suffix must be a verified domain in the tenant.
- D. The accountEnabled property controls whether a Microsoft Entra user can authenticate.

## LAB01-Q08 — Foundational

An identity onboarding reviewer challenges whether the operations-team identity onboarding can target automation to members while excluding external collaborators. Which response resolves the concern?

- A. A soft-deleted Microsoft Entra user can normally be restored during the directory retention window.
- B. The userType property distinguishes tenant members from business-to-business guest identities.
- C. A cloud-only user is a directory object and does not depend on an Azure subscription resource group.
- D. A non-mail-enabled security group uses securityEnabled true and mailEnabled false.

## LAB01-Q09 — Foundational

The operations-team identity onboarding handoff omits the identity onboarding rule needed to recover a user that was deleted during the retention window. Which statement should the team add?

- A. A soft-deleted Microsoft Entra user can normally be restored during the directory retention window.
- B. Object IDs remain the reliable automation key when display names or UPN values change.
- C. Properties such as department, job title, and usage location belong to the user directory object.
- D. A group member receives access assigned to the group, whereas an owner only administers the group.

## LAB01-Q10 — Foundational

An identity onboarding incident review of the operations-team identity onboarding depends on the ability to keep automation stable after a display name or sign-in name changes. Which platform description is reliable?

- A. A cloud user's UPN suffix must be a verified domain in the tenant.
- B. The accountEnabled property controls whether a Microsoft Entra user can authenticate.
- C. Object IDs remain the reliable automation key when display names or UPN values change.
- D. Group owners can manage group membership but ownership does not itself make them members.

## LAB01-Q11 — Foundational

An identity onboarding ticket in the operations-team identity onboarding says to use a custom tenant suffix when creating an operations account. Which identity onboarding action completes the operations-team identity onboarding request with minimal change?

- A. Patch the intended user object through Microsoft Graph by using its immutable object ID.
- B. Read the tenant's verified domains before constructing the new userPrincipalName.
- C. Add the user's object ID to the intended group's member collection.
- D. Locate the deleted directory object and restore it before the retention window expires.

## LAB01-Q12 — Foundational

The approach for the operations-team identity onboarding is approved, but the identity onboarding environment still cannot create a user whose identity exists only in this tenant. Which implementation step closes the gap?

- A. Set accountEnabled on the target user while leaving its identity and group memberships intact.
- B. Add the administrator's directory object ID to the group's owner collection.
- C. Persist returned user and group object IDs immediately in the lab run-state record.
- D. Create the user with a unique UPN, display name, and initial password through Azure CLI.

## LAB01-Q13 — Foundational

The identity administrator onboarding a small operations team may change the operations-team identity onboarding only to capture organizational profile metadata on the directory object. Which identity onboarding action stays within that assignment?

- A. Create a security group with a unique mail nickname and security capability enabled.
- B. Read userType before applying automation that should target only member or only guest accounts.
- C. Read the tenant's verified domains before constructing the new userPrincipalName.
- D. Patch the intended user object through Microsoft Graph by using its immutable object ID.

## LAB01-Q14 — Foundational

An identity onboarding dry run shows no operations-team identity onboarding command will block one user from signing in without deleting the account. Which action belongs before execution?

- A. Add the user's object ID to the intended group's member collection.
- B. Set accountEnabled on the target user while leaving its identity and group memberships intact.
- C. Locate the deleted directory object and restore it before the retention window expires.
- D. Create the user with a unique UPN, display name, and initial password through Azure CLI.

## LAB01-Q15 — Foundational

For the operations-team identity onboarding, operators need to build a security-only group that has no email address. Which change realizes that requirement?

- A. Create a security group with a unique mail nickname and security capability enabled.
- B. Add the administrator's directory object ID to the group's owner collection.
- C. Persist returned user and group object IDs immediately in the lab run-state record.
- D. Patch the intended user object through Microsoft Graph by using its immutable object ID.

## LAB01-Q16 — Applied

Operators must automate the operations-team identity onboarding change needed to give a user the access assigned to an operations group. Which identity onboarding operation belongs in the runbook?

- A. Add the user's object ID to the intended group's member collection.
- B. Read userType before applying automation that should target only member or only guest accounts.
- C. Read the tenant's verified domains before constructing the new userPrincipalName.
- D. Set accountEnabled on the target user while leaving its identity and group memberships intact.

## LAB01-Q17 — Applied

An operations-team identity onboarding review finds identity onboarding drift from the need to let an administrator manage membership without receiving the group's access. Which correction addresses that drift?

- A. Add the administrator's directory object ID to the group's owner collection.
- B. Locate the deleted directory object and restore it before the retention window expires.
- C. Create the user with a unique UPN, display name, and initial password through Azure CLI.
- D. Create a security group with a unique mail nickname and security capability enabled.

## LAB01-Q18 — Applied

The operations-team identity onboarding window permits only the identity onboarding change needed to target automation to members while excluding external collaborators. Which option respects the boundary?

- A. Persist returned user and group object IDs immediately in the lab run-state record.
- B. Patch the intended user object through Microsoft Graph by using its immutable object ID.
- C. Read userType before applying automation that should target only member or only guest accounts.
- D. Add the user's object ID to the intended group's member collection.

## LAB01-Q19 — Applied

The identity onboarding preflight has passed; the operations-team identity onboarding must now recover a user that was deleted during the retention window. Which operation should run?

- A. Locate the deleted directory object and restore it before the retention window expires.
- B. Read the tenant's verified domains before constructing the new userPrincipalName.
- C. Set accountEnabled on the target user while leaving its identity and group memberships intact.
- D. Add the administrator's directory object ID to the group's owner collection.

## LAB01-Q20 — Applied

The operations-team identity onboarding plan must keep automation stable after a display name or sign-in name changes while limiting the mutation scope to identity onboarding. Which action is appropriate?

- A. Persist returned user and group object IDs immediately in the lab run-state record.
- B. Create the user with a unique UPN, display name, and initial password through Azure CLI.
- C. Create a security group with a unique mail nickname and security capability enabled.
- D. Read userType before applying automation that should target only member or only guest accounts.

## LAB01-Q21 — Applied

The operations-team identity onboarding setup reports success after the identity onboarding attempt to use a custom tenant suffix when creating an operations account. Which identity onboarding read-only observation proves the operations-team identity onboarding outcome?

- A. Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
- B. List group owners and confirm the administrator's immutable object ID is present.
- C. Resolve each persisted ID directly and compare its current properties with the intended state.
- D. Query the created user and confirm that userPrincipalName ends in the selected verified domain.

## LAB01-Q22 — Applied

The identity onboarding log says the operations-team identity onboarding can now create a user whose identity exists only in this tenant. Which identity onboarding state should the operations-team identity onboarding acceptance test retain?

- A. Query the group and confirm securityEnabled is true while mailEnabled is false.
- B. Query userType and externalUserState for the exact directory object under review.
- C. Query the created user and confirm that userPrincipalName ends in the selected verified domain.
- D. Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.

## LAB01-Q23 — Applied

The operations-team identity onboarding rejects identity onboarding exit status as proof it can capture organizational profile metadata on the directory object. Which operations-team identity onboarding result is valid evidence?

- A. Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
- B. List group members and match the exact user object ID rather than only its display name.
- C. Query the restored object ID and verify that it has returned to the active users collection.
- D. Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.

## LAB01-Q24 — Applied

The identity onboarding validator needs one operations-team identity onboarding query after the change to block one user from signing in without deleting the account. Which identity onboarding property should the operations-team identity onboarding validator inspect?

- A. List group owners and confirm the administrator's immutable object ID is present.
- B. Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
- C. Resolve each persisted ID directly and compare its current properties with the intended state.
- D. Read the same object ID and project the updated department, jobTitle, and usageLocation properties.

## LAB01-Q25 — Applied

The identity administrator onboarding a small operations team must confirm the operations-team identity onboarding, without mutation, can build a security-only group that has no email address. Which identity onboarding check qualifies?

- A. Query userType and externalUserState for the exact directory object under review.
- B. Query the created user and confirm that userPrincipalName ends in the selected verified domain.
- C. Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
- D. Query the group and confirm securityEnabled is true while mailEnabled is false.

## LAB01-Q26 — Applied

The operations-team identity onboarding configuration is complete; the identity onboarding reviewers need evidence it can give a user the access assigned to an operations group. Which observation shows success?

- A. List group members and match the exact user object ID rather than only its display name.
- B. Query the restored object ID and verify that it has returned to the active users collection.
- C. Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
- D. Query the group and confirm securityEnabled is true while mailEnabled is false.

## LAB01-Q27 — Applied

The identity onboarding validation asks whether the operations-team identity onboarding can let an administrator manage membership without receiving the group's access. Which observable state is strongest?

- A. List group owners and confirm the administrator's immutable object ID is present.
- B. Resolve each persisted ID directly and compare its current properties with the intended state.
- C. Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
- D. List group members and match the exact user object ID rather than only its display name.

## LAB01-Q28 — Applied

An operations-team identity onboarding review must prove the identity onboarding ability to target automation to members while excluding external collaborators. Which check avoids an adjacent feature?

- A. Query the created user and confirm that userPrincipalName ends in the selected verified domain.
- B. Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
- C. Query userType and externalUserState for the exact directory object under review.
- D. List group owners and confirm the administrator's immutable object ID is present.

## LAB01-Q29 — Applied

The operations-team identity onboarding evidence bundle needs an identity onboarding result showing it can recover a user that was deleted during the retention window. Which result belongs in the checkpoint?

- A. Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
- B. Query the restored object ID and verify that it has returned to the active users collection.
- C. Query the group and confirm securityEnabled is true while mailEnabled is false.
- D. Query userType and externalUserState for the exact directory object under review.

## LAB01-Q30 — Applied

Before operations-team identity onboarding cleanup, the identity onboarding team must reconfirm it can keep automation stable after a display name or sign-in name changes. Which read-only inspection should run?

- A. Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
- B. List group members and match the exact user object ID rather than only its display name.
- C. Query the restored object ID and verify that it has returned to the active users collection.
- D. Resolve each persisted ID directly and compare its current properties with the intended state.

## LAB01-Q31 — Applied

During an identity onboarding fault drill, the operations-team identity onboarding does not use a custom tenant suffix when creating an operations account. Which finding identifies the defect?

- A. The runbook discarded the returned object ID and later queried a different user with a similar display name.
- B. The user was added as an owner but never added to the member collection.
- C. The requested UPN uses a domain that is not verified in the tenant.
- D. Cleanup searched by a reused display name and found an unrelated directory object.

## LAB01-Q32 — Applied

The operations-team identity onboarding setup finishes, yet the identity onboarding cannot create a user whose identity exists only in this tenant. Which misconfiguration explains the mismatch?

- A. The update targeted the user's display name instead of the immutable directory object ID.
- B. The administrator appears only in the member list and therefore lacks group-owner responsibility.
- C. The runbook discarded the returned object ID and later queried a different user with a similar display name.
- D. The requested UPN uses a domain that is not verified in the tenant.

## LAB01-Q33 — Applied

An identity onboarding break/fix in the operations-team identity onboarding fails when operators try to capture organizational profile metadata on the directory object. Which diagnosis fits?

- A. The account remains disabled even though its group memberships were configured correctly.
- B. The automation filtered on a UPN naming convention instead of the authoritative userType property.
- C. The update targeted the user's display name instead of the immutable directory object ID.
- D. The runbook discarded the returned object ID and later queried a different user with a similar display name.

## LAB01-Q34 — Applied

The operations-team identity onboarding troubleshooting scope is the identity onboarding need to block one user from signing in without deleting the account. Which condition should be corrected first?

- A. The group was created as a non-security Microsoft 365 collaboration group.
- B. The account remains disabled even though its group memberships were configured correctly.
- C. The object was permanently deleted or its deleted-item retention window has expired.
- D. The update targeted the user's display name instead of the immutable directory object ID.

## LAB01-Q35 — Applied

The operations-team identity onboarding result is partial because the identity onboarding cannot build a security-only group that has no email address. Which condition accounts for that result?

- A. The user was added as an owner but never added to the member collection.
- B. Cleanup searched by a reused display name and found an unrelated directory object.
- C. The group was created as a non-security Microsoft 365 collaboration group.
- D. The account remains disabled even though its group memberships were configured correctly.

## LAB01-Q36 — Applied

The identity onboarding evidence shows the operations-team identity onboarding cannot give a user the access assigned to an operations group. Which root cause fits that evidence?

- A. The administrator appears only in the member list and therefore lacks group-owner responsibility.
- B. The requested UPN uses a domain that is not verified in the tenant.
- C. The user was added as an owner but never added to the member collection.
- D. The group was created as a non-security Microsoft 365 collaboration group.

## LAB01-Q37 — Applied

Although the operations-team identity onboarding is meant to let the identity onboarding let an administrator manage membership without receiving the group's access, its checkpoint fails. Which identity onboarding defect explains the failure?

- A. The automation filtered on a UPN naming convention instead of the authoritative userType property.
- B. The runbook discarded the returned object ID and later queried a different user with a similar display name.
- C. The user was added as an owner but never added to the member collection.
- D. The administrator appears only in the member list and therefore lacks group-owner responsibility.

## LAB01-Q38 — Applied

The identity onboarding support team isolated the operations-team identity onboarding incident to the attempt to target automation to members while excluding external collaborators. Which condition prevents success?

- A. The object was permanently deleted or its deleted-item retention window has expired.
- B. The automation filtered on a UPN naming convention instead of the authoritative userType property.
- C. The update targeted the user's display name instead of the immutable directory object ID.
- D. The administrator appears only in the member list and therefore lacks group-owner responsibility.

## LAB01-Q39 — Applied

An operations-team identity onboarding query surprises the identity administrator onboarding a small operations team during the identity onboarding attempt to recover a user that was deleted during the retention window. Which finding explains it?

- A. Cleanup searched by a reused display name and found an unrelated directory object.
- B. The account remains disabled even though its group memberships were configured correctly.
- C. The automation filtered on a UPN naming convention instead of the authoritative userType property.
- D. The object was permanently deleted or its deleted-item retention window has expired.

## LAB01-Q40 — Applied

Other operations-team identity onboarding components are healthy, but the identity onboarding still cannot keep automation stable after a display name or sign-in name changes. Which state causes the isolated failure?

- A. The requested UPN uses a domain that is not verified in the tenant.
- B. The group was created as a non-security Microsoft 365 collaboration group.
- C. Cleanup searched by a reused display name and found an unrelated directory object.
- D. The object was permanently deleted or its deleted-item retention window has expired.

## LAB01-Q41 — Advanced

The operations-team identity onboarding runbook must use a custom tenant suffix when creating an operations account, then retain identity onboarding read-back evidence. Which operations-team identity onboarding pair completes both duties?

- A. First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
- B. First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.
- C. First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
- D. First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.

## LAB01-Q42 — Advanced

To satisfy the identity onboarding requirement, operators must change the operations-team identity onboarding configuration and prove it can create a user whose identity exists only in this tenant. Which sequence is coherent?

- A. First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
- B. First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
- C. First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
- D. First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.

## LAB01-Q43 — Advanced

The identity administrator onboarding a small operations team needs a safe operations-team identity onboarding change to capture organizational profile metadata on the directory object, followed by identity onboarding evidence. Which pair merits approval?

- A. First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.
- B. First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
- C. First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.
- D. First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.

## LAB01-Q44 — Advanced

The operations-team identity onboarding has two identity onboarding gates: block one user from signing in without deleting the account, then prove the operations-team identity onboarding state. Which identity onboarding sequence works?

- A. First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.
- B. First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.
- C. First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.
- D. First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.

## LAB01-Q45 — Advanced

Which identity onboarding path makes the operations-team identity onboarding able to build a security-only group that has no email address, then inspects the defining properties?

- A. First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.
- B. First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.
- C. First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.
- D. First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.

## LAB01-Q46 — Advanced

At the operations-team identity onboarding approval gate, operators must show that the identity onboarding can give a user the access assigned to an operations group. Which identity onboarding configure-and-check pair is defensible?

- A. First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
- B. First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
- C. First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.
- D. First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.

## LAB01-Q47 — Advanced

The operations-team identity onboarding forbids a partial identity onboarding result. Operators must first let an administrator manage membership without receiving the group's access and afterward confirm the operations-team identity onboarding outcome. Which identity onboarding sequence is complete?

- A. First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.
- B. First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
- C. First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
- D. First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.

## LAB01-Q48 — Advanced

Only the operations-team identity onboarding change needed to target automation to members while excluding external collaborators is allowed, and identity onboarding proof is mandatory. Which pair fits?

- A. First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
- B. First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.
- C. First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
- D. First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.

## LAB01-Q49 — Advanced

The operations-team identity onboarding runbook separates identity onboarding mutation from validation while it must recover a user that was deleted during the retention window. Which sequence proves it cleanly?

- A. First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.
- B. First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.
- C. First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.
- D. First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.

## LAB01-Q50 — Advanced

The operations-team identity onboarding checkpoint requires both this identity onboarding outcome—keep automation stable after a display name or sign-in name changes—and a read-only operations-team identity onboarding state check. Which identity onboarding response is complete?

- A. First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
- B. First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.
- C. First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.
- D. First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.

[Open the answer key](./ANSWERS.md)
