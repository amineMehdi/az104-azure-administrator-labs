# Lab 01 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB01-Q01 — B

**Question:** An identity administrator onboarding a small operations team is updating the identity onboarding runbook. The requirement is to use a custom tenant suffix when creating an operations account. Which statement describes Azure behavior correctly?

- **A — Incorrect.** A cloud-only user is a directory object and does not depend on an Azure subscription resource group.
  A cloud-only user is a directory object and does not depend on an Azure subscription resource group. In the operations-team identity onboarding, this statement describes cloud-only user creation. Operations-team identity onboarding asks about verified UPN suffixes; this cloud-only user creation choice leaves the verified UPN suffixes explanation missing.
- **B — Correct.** A cloud user's UPN suffix must be a verified domain in the tenant.
  A cloud user's UPN suffix must be a verified domain in the tenant. In the operations-team identity onboarding, this verified UPN suffixes rule supports the need to use a custom tenant suffix when creating an operations account.
- **C — Incorrect.** A non-mail-enabled security group uses securityEnabled true and mailEnabled false.
  A non-mail-enabled security group uses securityEnabled true and mailEnabled false. In the operations-team identity onboarding, this statement describes security group creation. Selecting security group creation for operations-team identity onboarding leaves verified UPN suffixes unanswered in operations-team identity onboarding; the operations-team identity onboarding lacks a verified UPN suffixes basis to use a custom tenant suffix when creating an operations account.
- **D — Incorrect.** The userType property distinguishes tenant members from business-to-business guest identities.
  The userType property distinguishes tenant members from business-to-business guest identities. In the operations-team identity onboarding, this statement describes member and guest user types. Verified UPN suffixes governs operations-team identity onboarding; member and guest user types cannot support verified UPN suffixes when operators must use a custom tenant suffix when creating an operations account.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [List domains with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/domain-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q02 — C

**Question:** An identity onboarding peer review asks how the operations-team identity onboarding should handle this outcome: create a user whose identity exists only in this tenant. Which explanation is accurate?

- **A — Incorrect.** Properties such as department, job title, and usage location belong to the user directory object.
  Properties such as department, job title, and usage location belong to the user directory object. In the operations-team identity onboarding, this statement describes user profile properties. The user profile properties statement accurately describes user profile properties; however, operations-team identity onboarding needs cloud-only user creation to create a user whose identity exists only in this tenant; user profile properties cannot replace cloud-only user creation.
- **B — Incorrect.** A group member receives access assigned to the group, whereas an owner only administers the group.
  A group member receives access assigned to the group, whereas an owner only administers the group. In the operations-team identity onboarding, this statement describes group membership. Selecting group membership for operations-team identity onboarding leaves cloud-only user creation unanswered in operations-team identity onboarding; the operations-team identity onboarding lacks a cloud-only user creation basis to create a user whose identity exists only in this tenant.
- **C — Correct.** A cloud-only user is a directory object and does not depend on an Azure subscription resource group.
  For the operations-team identity onboarding, the rule for cloud-only user creation is defined by this statement: a cloud-only user is a directory object and does not depend on an Azure subscription resource group. It supports the required outcome to create a user whose identity exists only in this tenant.
- **D — Incorrect.** A soft-deleted Microsoft Entra user can normally be restored during the directory retention window.
  A soft-deleted Microsoft Entra user can normally be restored during the directory retention window. In the operations-team identity onboarding, this statement describes deleted-user recovery. Operations-team identity onboarding asks about cloud-only user creation; this deleted-user recovery choice leaves the cloud-only user creation explanation missing.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra users](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q03 — A

**Question:** For the operations-team identity onboarding, the identity onboarding plan must capture organizational profile metadata on the directory object. Which statement about identity onboarding belongs in the operations-team identity onboarding record?

- **A — Correct.** Properties such as department, job title, and usage location belong to the user directory object.
  Properties such as department, job title, and usage location belong to the user directory object. The operations-team identity onboarding applies that user profile properties boundary when operators must capture organizational profile metadata on the directory object.
- **B — Incorrect.** The accountEnabled property controls whether a Microsoft Entra user can authenticate.
  The accountEnabled property controls whether a Microsoft Entra user can authenticate. In the operations-team identity onboarding, this statement describes account enabled state. User profile properties governs operations-team identity onboarding; account enabled state cannot support user profile properties when operators must capture organizational profile metadata on the directory object.
- **C — Incorrect.** Group owners can manage group membership but ownership does not itself make them members.
  Group owners can manage group membership but ownership does not itself make them members. In the operations-team identity onboarding, this statement describes group ownership. Operations-team identity onboarding asks about user profile properties; this group ownership choice leaves the user profile properties explanation missing.
- **D — Incorrect.** Object IDs remain the reliable automation key when display names or UPN values change.
  Object IDs remain the reliable automation key when display names or UPN values change. In the operations-team identity onboarding, this statement describes immutable directory object IDs. The immutable directory object IDs statement accurately describes immutable directory object IDs; however, operations-team identity onboarding needs user profile properties to capture organizational profile metadata on the directory object; immutable directory object IDs cannot replace user profile properties.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q04 — D

**Question:** The identity onboarding review compares four claims for the operations-team identity onboarding requirement to block one user from signing in without deleting the account. Which claim is technically sound?

- **A — Incorrect.** A non-mail-enabled security group uses securityEnabled true and mailEnabled false.
  A non-mail-enabled security group uses securityEnabled true and mailEnabled false. In the operations-team identity onboarding, this statement describes security group creation. Account enabled state governs operations-team identity onboarding; security group creation cannot support account enabled state when operators must block one user from signing in without deleting the account.
- **B — Incorrect.** The userType property distinguishes tenant members from business-to-business guest identities.
  The userType property distinguishes tenant members from business-to-business guest identities. In the operations-team identity onboarding, this statement describes member and guest user types. Operations-team identity onboarding asks about account enabled state; this member and guest user types choice leaves the account enabled state explanation missing.
- **C — Incorrect.** A cloud user's UPN suffix must be a verified domain in the tenant.
  A cloud user's UPN suffix must be a verified domain in the tenant. In the operations-team identity onboarding, this statement describes verified UPN suffixes. The verified UPN suffixes statement accurately describes verified UPN suffixes; however, operations-team identity onboarding needs account enabled state to block one user from signing in without deleting the account; verified UPN suffixes cannot replace account enabled state.
- **D — Correct.** The accountEnabled property controls whether a Microsoft Entra user can authenticate.
  The operations-team identity onboarding needs account enabled state to block one user from signing in without deleting the account; this option states the applicable account enabled state rule: the accountEnabled property controls whether a Microsoft Entra user can authenticate.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q05 — B

**Question:** The identity onboarding architecture note requires the operations-team identity onboarding environment to build a security-only group that has no email address. Which statement defines the relevant identity onboarding boundary?

- **A — Incorrect.** A group member receives access assigned to the group, whereas an owner only administers the group.
  A group member receives access assigned to the group, whereas an owner only administers the group. In the operations-team identity onboarding, this statement describes group membership. Operations-team identity onboarding asks about security group creation; this group membership choice leaves the security group creation explanation missing.
- **B — Correct.** A non-mail-enabled security group uses securityEnabled true and mailEnabled false.
  A non-mail-enabled security group uses securityEnabled true and mailEnabled false. This security group creation fact resolves the operations-team identity onboarding design question about how to build a security-only group that has no email address.
- **C — Incorrect.** A soft-deleted Microsoft Entra user can normally be restored during the directory retention window.
  A soft-deleted Microsoft Entra user can normally be restored during the directory retention window. In the operations-team identity onboarding, this statement describes deleted-user recovery. Selecting deleted-user recovery for operations-team identity onboarding leaves security group creation unanswered in operations-team identity onboarding; the operations-team identity onboarding lacks a security group creation basis to build a security-only group that has no email address.
- **D — Incorrect.** A cloud-only user is a directory object and does not depend on an Azure subscription resource group.
  A cloud-only user is a directory object and does not depend on an Azure subscription resource group. In the operations-team identity onboarding, this statement describes cloud-only user creation. Security group creation governs operations-team identity onboarding; cloud-only user creation cannot support security group creation when operators must build a security-only group that has no email address.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra groups](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q06 — B

**Question:** A new identity onboarding operator must explain why the operations-team identity onboarding can give a user the access assigned to an operations group. Which explanation is accurate?

- **A — Incorrect.** Group owners can manage group membership but ownership does not itself make them members.
  Group owners can manage group membership but ownership does not itself make them members. In the operations-team identity onboarding, this statement describes group ownership. The group ownership statement accurately describes group ownership; however, operations-team identity onboarding needs group membership to give a user the access assigned to an operations group; group ownership cannot replace group membership.
- **B — Correct.** A group member receives access assigned to the group, whereas an owner only administers the group.
  A group member receives access assigned to the group, whereas an owner only administers the group. For operations-team identity onboarding, group membership supplies the service rule needed to give a user the access assigned to an operations group.
- **C — Incorrect.** Object IDs remain the reliable automation key when display names or UPN values change.
  Object IDs remain the reliable automation key when display names or UPN values change. In the operations-team identity onboarding, this statement describes immutable directory object IDs. Group membership governs operations-team identity onboarding; immutable directory object IDs cannot support group membership when operators must give a user the access assigned to an operations group.
- **D — Incorrect.** Properties such as department, job title, and usage location belong to the user directory object.
  Properties such as department, job title, and usage location belong to the user directory object. In the operations-team identity onboarding, this statement describes user profile properties. Operations-team identity onboarding asks about group membership; this user profile properties choice leaves the group membership explanation missing.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group membership](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q07 — A

**Question:** The operations-team identity onboarding acceptance criteria require operators to let an administrator manage membership without receiving the group's access. Which service fact supports that requirement?

- **A — Correct.** Group owners can manage group membership but ownership does not itself make them members.
  Group owners can manage group membership but ownership does not itself make them members. In the operations-team identity onboarding, this group ownership rule supports the need to let an administrator manage membership without receiving the group's access.
- **B — Incorrect.** The userType property distinguishes tenant members from business-to-business guest identities.
  The userType property distinguishes tenant members from business-to-business guest identities. In the operations-team identity onboarding, this statement describes member and guest user types. Group ownership governs operations-team identity onboarding; member and guest user types cannot support group ownership when operators must let an administrator manage membership without receiving the group's access.
- **C — Incorrect.** A cloud user's UPN suffix must be a verified domain in the tenant.
  A cloud user's UPN suffix must be a verified domain in the tenant. In the operations-team identity onboarding, this statement describes verified UPN suffixes. Operations-team identity onboarding asks about group ownership; this verified UPN suffixes choice leaves the group ownership explanation missing.
- **D — Incorrect.** The accountEnabled property controls whether a Microsoft Entra user can authenticate.
  The accountEnabled property controls whether a Microsoft Entra user can authenticate. In the operations-team identity onboarding, this statement describes account enabled state. The account enabled state statement accurately describes account enabled state; however, operations-team identity onboarding needs group ownership to let an administrator manage membership without receiving the group's access; account enabled state cannot replace group ownership.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group owners](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q08 — B

**Question:** An identity onboarding reviewer challenges whether the operations-team identity onboarding can target automation to members while excluding external collaborators. Which response resolves the concern?

- **A — Incorrect.** A soft-deleted Microsoft Entra user can normally be restored during the directory retention window.
  A soft-deleted Microsoft Entra user can normally be restored during the directory retention window. In the operations-team identity onboarding, this statement describes deleted-user recovery. Member and guest user types governs operations-team identity onboarding; deleted-user recovery cannot support member and guest user types when operators must target automation to members while excluding external collaborators.
- **B — Correct.** The userType property distinguishes tenant members from business-to-business guest identities.
  For the operations-team identity onboarding, the rule for member and guest user types is defined by this statement: the userType property distinguishes tenant members from business-to-business guest identities. It supports the required outcome to target automation to members while excluding external collaborators.
- **C — Incorrect.** A cloud-only user is a directory object and does not depend on an Azure subscription resource group.
  A cloud-only user is a directory object and does not depend on an Azure subscription resource group. In the operations-team identity onboarding, this statement describes cloud-only user creation. The cloud-only user creation statement accurately describes cloud-only user creation; however, operations-team identity onboarding needs member and guest user types to target automation to members while excluding external collaborators; cloud-only user creation cannot replace member and guest user types.
- **D — Incorrect.** A non-mail-enabled security group uses securityEnabled true and mailEnabled false.
  A non-mail-enabled security group uses securityEnabled true and mailEnabled false. In the operations-team identity onboarding, this statement describes security group creation. Selecting security group creation for operations-team identity onboarding leaves member and guest user types unanswered in operations-team identity onboarding; the operations-team identity onboarding lacks a member and guest user types basis to target automation to members while excluding external collaborators.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q09 — A

**Question:** The operations-team identity onboarding handoff omits the identity onboarding rule needed to recover a user that was deleted during the retention window. Which statement should the team add?

- **A — Correct.** A soft-deleted Microsoft Entra user can normally be restored during the directory retention window.
  A soft-deleted Microsoft Entra user can normally be restored during the directory retention window. The operations-team identity onboarding applies that deleted-user recovery boundary when operators must recover a user that was deleted during the retention window.
- **B — Incorrect.** Object IDs remain the reliable automation key when display names or UPN values change.
  Object IDs remain the reliable automation key when display names or UPN values change. In the operations-team identity onboarding, this statement describes immutable directory object IDs. The immutable directory object IDs statement accurately describes immutable directory object IDs; however, operations-team identity onboarding needs deleted-user recovery to recover a user that was deleted during the retention window; immutable directory object IDs cannot replace deleted-user recovery.
- **C — Incorrect.** Properties such as department, job title, and usage location belong to the user directory object.
  Properties such as department, job title, and usage location belong to the user directory object. In the operations-team identity onboarding, this statement describes user profile properties. Selecting user profile properties for operations-team identity onboarding leaves deleted-user recovery unanswered in operations-team identity onboarding; the operations-team identity onboarding lacks a deleted-user recovery basis to recover a user that was deleted during the retention window.
- **D — Incorrect.** A group member receives access assigned to the group, whereas an owner only administers the group.
  A group member receives access assigned to the group, whereas an owner only administers the group. In the operations-team identity onboarding, this statement describes group membership. Deleted-user recovery governs operations-team identity onboarding; group membership cannot support deleted-user recovery when operators must recover a user that was deleted during the retention window.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Restore or permanently remove recently deleted users](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore)

**Source reviewed:** 2026-08-31

## LAB01-Q10 — C

**Question:** An identity onboarding incident review of the operations-team identity onboarding depends on the ability to keep automation stable after a display name or sign-in name changes. Which platform description is reliable?

- **A — Incorrect.** A cloud user's UPN suffix must be a verified domain in the tenant.
  A cloud user's UPN suffix must be a verified domain in the tenant. In the operations-team identity onboarding, this statement describes verified UPN suffixes. The verified UPN suffixes statement accurately describes verified UPN suffixes; however, operations-team identity onboarding needs immutable directory object IDs to keep automation stable after a display name or sign-in name changes; verified UPN suffixes cannot replace immutable directory object IDs.
- **B — Incorrect.** The accountEnabled property controls whether a Microsoft Entra user can authenticate.
  The accountEnabled property controls whether a Microsoft Entra user can authenticate. In the operations-team identity onboarding, this statement describes account enabled state. Selecting account enabled state for operations-team identity onboarding leaves immutable directory object IDs unanswered in operations-team identity onboarding; the operations-team identity onboarding lacks a immutable directory object IDs basis to keep automation stable after a display name or sign-in name changes.
- **C — Correct.** Object IDs remain the reliable automation key when display names or UPN values change.
  The operations-team identity onboarding needs immutable directory object IDs to keep automation stable after a display name or sign-in name changes; this option states the applicable immutable directory object IDs rule: object IDs remain the reliable automation key when display names or UPN values change.
- **D — Incorrect.** Group owners can manage group membership but ownership does not itself make them members.
  Group owners can manage group membership but ownership does not itself make them members. In the operations-team identity onboarding, this statement describes group ownership. Operations-team identity onboarding asks about immutable directory object IDs; this group ownership choice leaves the immutable directory object IDs explanation missing.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q11 — B

**Question:** An identity onboarding ticket in the operations-team identity onboarding says to use a custom tenant suffix when creating an operations account. Which identity onboarding action completes the operations-team identity onboarding request with minimal change?

- **A — Incorrect.** Patch the intended user object through Microsoft Graph by using its immutable object ID.
  Patch the intended user object through Microsoft Graph by using its immutable object ID. In the operations-team identity onboarding, this action changes user profile properties. Operations-team identity onboarding approved verified UPN suffixes, not user profile properties; only the verified UPN suffixes change can use a custom tenant suffix when creating an operations account.
- **B — Correct.** Read the tenant's verified domains before constructing the new userPrincipalName.
  Read the tenant's verified domains before constructing the new userPrincipalName. It is the least-change verified UPN suffixes path for the operations-team identity onboarding requirement to use a custom tenant suffix when creating an operations account.
- **C — Incorrect.** Add the user's object ID to the intended group's member collection.
  Add the user's object ID to the intended group's member collection. In the operations-team identity onboarding, this action changes group membership. Group membership does not implement verified UPN suffixes for operations-team identity onboarding; the operations-team identity onboarding still cannot use a custom tenant suffix when creating an operations account.
- **D — Incorrect.** Locate the deleted directory object and restore it before the retention window expires.
  Locate the deleted directory object and restore it before the retention window expires. In the operations-team identity onboarding, this action changes deleted-user recovery. Operations-team identity onboarding instead needs verified UPN suffixes: Read the tenant's verified domains before constructing the new userPrincipalName. The deleted-user recovery action omits that verified UPN suffixes work.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [List domains with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/domain-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q12 — D

**Question:** The approach for the operations-team identity onboarding is approved, but the identity onboarding environment still cannot create a user whose identity exists only in this tenant. Which implementation step closes the gap?

- **A — Incorrect.** Set accountEnabled on the target user while leaving its identity and group memberships intact.
  Set accountEnabled on the target user while leaving its identity and group memberships intact. In the operations-team identity onboarding, this action changes account enabled state. Operations-team identity onboarding requires cloud-only user creation; changing account enabled state leaves cloud-only user creation absent in operations-team identity onboarding; operations-team identity onboarding cannot create a user whose identity exists only in this tenant.
- **B — Incorrect.** Add the administrator's directory object ID to the group's owner collection.
  Add the administrator's directory object ID to the group's owner collection. In the operations-team identity onboarding, this action changes group ownership. Group ownership does not implement cloud-only user creation for operations-team identity onboarding; the operations-team identity onboarding still cannot create a user whose identity exists only in this tenant.
- **C — Incorrect.** Persist returned user and group object IDs immediately in the lab run-state record.
  Persist returned user and group object IDs immediately in the lab run-state record. In the operations-team identity onboarding, this action changes immutable directory object IDs. Operations-team identity onboarding instead needs cloud-only user creation: Create the user with a unique UPN, display name, and initial password through Azure CLI. The immutable directory object IDs action omits that cloud-only user creation work.
- **D — Correct.** Create the user with a unique UPN, display name, and initial password through Azure CLI.
  Create the user with a unique UPN, display name, and initial password through Azure CLI. In operations-team identity onboarding, applying cloud-only user creation is the scoped way to create a user whose identity exists only in this tenant.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra users](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q13 — D

**Question:** The identity administrator onboarding a small operations team may change the operations-team identity onboarding only to capture organizational profile metadata on the directory object. Which identity onboarding action stays within that assignment?

- **A — Incorrect.** Create a security group with a unique mail nickname and security capability enabled.
  Create a security group with a unique mail nickname and security capability enabled. In the operations-team identity onboarding, this action changes security group creation. Security group creation does not implement user profile properties for operations-team identity onboarding; the operations-team identity onboarding still cannot capture organizational profile metadata on the directory object.
- **B — Incorrect.** Read userType before applying automation that should target only member or only guest accounts.
  Read userType before applying automation that should target only member or only guest accounts. In the operations-team identity onboarding, this action changes member and guest user types. Operations-team identity onboarding instead needs user profile properties: Patch the intended user object through Microsoft Graph by using its immutable object ID. The member and guest user types action omits that user profile properties work.
- **C — Incorrect.** Read the tenant's verified domains before constructing the new userPrincipalName.
  Read the tenant's verified domains before constructing the new userPrincipalName. In the operations-team identity onboarding, this action changes verified UPN suffixes. Operations-team identity onboarding approved user profile properties, not verified UPN suffixes; only the user profile properties change can capture organizational profile metadata on the directory object.
- **D — Correct.** Patch the intended user object through Microsoft Graph by using its immutable object ID.
  Patch the intended user object through Microsoft Graph by using its immutable object ID. The operations-team identity onboarding uses this user profile properties operation to capture organizational profile metadata on the directory object within the approved scope.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q14 — B

**Question:** An identity onboarding dry run shows no operations-team identity onboarding command will block one user from signing in without deleting the account. Which action belongs before execution?

- **A — Incorrect.** Add the user's object ID to the intended group's member collection.
  Add the user's object ID to the intended group's member collection. In the operations-team identity onboarding, this action changes group membership. Operations-team identity onboarding instead needs account enabled state: Set accountEnabled on the target user while leaving its identity and group memberships intact. The group membership action omits that account enabled state work.
- **B — Correct.** Set accountEnabled on the target user while leaving its identity and group memberships intact.
  For the operations-team identity onboarding, the required account enabled state action is: set accountEnabled on the target user while leaving its identity and group memberships intact. It makes the environment able to block one user from signing in without deleting the account.
- **C — Incorrect.** Locate the deleted directory object and restore it before the retention window expires.
  Locate the deleted directory object and restore it before the retention window expires. In the operations-team identity onboarding, this action changes deleted-user recovery. Operations-team identity onboarding requires account enabled state; changing deleted-user recovery leaves account enabled state absent in operations-team identity onboarding; operations-team identity onboarding cannot block one user from signing in without deleting the account.
- **D — Incorrect.** Create the user with a unique UPN, display name, and initial password through Azure CLI.
  Create the user with a unique UPN, display name, and initial password through Azure CLI. In the operations-team identity onboarding, this action changes cloud-only user creation. Cloud-only user creation does not implement account enabled state for operations-team identity onboarding; the operations-team identity onboarding still cannot block one user from signing in without deleting the account.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q15 — A

**Question:** For the operations-team identity onboarding, operators need to build a security-only group that has no email address. Which change realizes that requirement?

- **A — Correct.** Create a security group with a unique mail nickname and security capability enabled.
  Create a security group with a unique mail nickname and security capability enabled. This changes security group creation in the operations-team identity onboarding, supplying the missing state needed to build a security-only group that has no email address.
- **B — Incorrect.** Add the administrator's directory object ID to the group's owner collection.
  Add the administrator's directory object ID to the group's owner collection. In the operations-team identity onboarding, this action changes group ownership. Operations-team identity onboarding requires security group creation; changing group ownership leaves security group creation absent in operations-team identity onboarding; operations-team identity onboarding cannot build a security-only group that has no email address.
- **C — Incorrect.** Persist returned user and group object IDs immediately in the lab run-state record.
  Persist returned user and group object IDs immediately in the lab run-state record. In the operations-team identity onboarding, this action changes immutable directory object IDs. Immutable directory object IDs does not implement security group creation for operations-team identity onboarding; the operations-team identity onboarding still cannot build a security-only group that has no email address.
- **D — Incorrect.** Patch the intended user object through Microsoft Graph by using its immutable object ID.
  Patch the intended user object through Microsoft Graph by using its immutable object ID. In the operations-team identity onboarding, this action changes user profile properties. Operations-team identity onboarding instead needs security group creation: Create a security group with a unique mail nickname and security capability enabled. The user profile properties action omits that security group creation work.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra groups](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q16 — A

**Question:** Operators must automate the operations-team identity onboarding change needed to give a user the access assigned to an operations group. Which identity onboarding operation belongs in the runbook?

- **A — Correct.** Add the user's object ID to the intended group's member collection.
  The operations-team identity onboarding must give a user the access assigned to an operations group; this option performs its direct group membership change: add the user's object ID to the intended group's member collection.
- **B — Incorrect.** Read userType before applying automation that should target only member or only guest accounts.
  Read userType before applying automation that should target only member or only guest accounts. In the operations-team identity onboarding, this action changes member and guest user types. Member and guest user types does not implement group membership for operations-team identity onboarding; the operations-team identity onboarding still cannot give a user the access assigned to an operations group.
- **C — Incorrect.** Read the tenant's verified domains before constructing the new userPrincipalName.
  Read the tenant's verified domains before constructing the new userPrincipalName. In the operations-team identity onboarding, this action changes verified UPN suffixes. Operations-team identity onboarding instead needs group membership: Add the user's object ID to the intended group's member collection. The verified UPN suffixes action omits that group membership work.
- **D — Incorrect.** Set accountEnabled on the target user while leaving its identity and group memberships intact.
  Set accountEnabled on the target user while leaving its identity and group memberships intact. In the operations-team identity onboarding, this action changes account enabled state. Operations-team identity onboarding approved group membership, not account enabled state; only the group membership change can give a user the access assigned to an operations group.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group membership](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q17 — A

**Question:** An operations-team identity onboarding review finds identity onboarding drift from the need to let an administrator manage membership without receiving the group's access. Which correction addresses that drift?

- **A — Correct.** Add the administrator's directory object ID to the group's owner collection.
  Add the administrator's directory object ID to the group's owner collection. It is the least-change group ownership path for the operations-team identity onboarding requirement to let an administrator manage membership without receiving the group's access.
- **B — Incorrect.** Locate the deleted directory object and restore it before the retention window expires.
  Locate the deleted directory object and restore it before the retention window expires. In the operations-team identity onboarding, this action changes deleted-user recovery. Operations-team identity onboarding instead needs group ownership: Add the administrator's directory object ID to the group's owner collection. The deleted-user recovery action omits that group ownership work.
- **C — Incorrect.** Create the user with a unique UPN, display name, and initial password through Azure CLI.
  Create the user with a unique UPN, display name, and initial password through Azure CLI. In the operations-team identity onboarding, this action changes cloud-only user creation. Operations-team identity onboarding approved group ownership, not cloud-only user creation; only the group ownership change can let an administrator manage membership without receiving the group's access.
- **D — Incorrect.** Create a security group with a unique mail nickname and security capability enabled.
  Create a security group with a unique mail nickname and security capability enabled. In the operations-team identity onboarding, this action changes security group creation. Operations-team identity onboarding requires group ownership; changing security group creation leaves group ownership absent in operations-team identity onboarding; operations-team identity onboarding cannot let an administrator manage membership without receiving the group's access.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group owners](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q18 — C

**Question:** The operations-team identity onboarding window permits only the identity onboarding change needed to target automation to members while excluding external collaborators. Which option respects the boundary?

- **A — Incorrect.** Persist returned user and group object IDs immediately in the lab run-state record.
  Persist returned user and group object IDs immediately in the lab run-state record. In the operations-team identity onboarding, this action changes immutable directory object IDs. Operations-team identity onboarding instead needs member and guest user types: Read userType before applying automation that should target only member or only guest accounts. The immutable directory object IDs action omits that member and guest user types work.
- **B — Incorrect.** Patch the intended user object through Microsoft Graph by using its immutable object ID.
  Patch the intended user object through Microsoft Graph by using its immutable object ID. In the operations-team identity onboarding, this action changes user profile properties. Operations-team identity onboarding approved member and guest user types, not user profile properties; only the member and guest user types change can target automation to members while excluding external collaborators.
- **C — Correct.** Read userType before applying automation that should target only member or only guest accounts.
  Read userType before applying automation that should target only member or only guest accounts. In operations-team identity onboarding, applying member and guest user types is the scoped way to target automation to members while excluding external collaborators.
- **D — Incorrect.** Add the user's object ID to the intended group's member collection.
  Add the user's object ID to the intended group's member collection. In the operations-team identity onboarding, this action changes group membership. Group membership does not implement member and guest user types for operations-team identity onboarding; the operations-team identity onboarding still cannot target automation to members while excluding external collaborators.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q19 — A

**Question:** The identity onboarding preflight has passed; the operations-team identity onboarding must now recover a user that was deleted during the retention window. Which operation should run?

- **A — Correct.** Locate the deleted directory object and restore it before the retention window expires.
  Locate the deleted directory object and restore it before the retention window expires. The operations-team identity onboarding uses this deleted-user recovery operation to recover a user that was deleted during the retention window within the approved scope.
- **B — Incorrect.** Read the tenant's verified domains before constructing the new userPrincipalName.
  Read the tenant's verified domains before constructing the new userPrincipalName. In the operations-team identity onboarding, this action changes verified UPN suffixes. Operations-team identity onboarding requires deleted-user recovery; changing verified UPN suffixes leaves deleted-user recovery absent in operations-team identity onboarding; operations-team identity onboarding cannot recover a user that was deleted during the retention window.
- **C — Incorrect.** Set accountEnabled on the target user while leaving its identity and group memberships intact.
  Set accountEnabled on the target user while leaving its identity and group memberships intact. In the operations-team identity onboarding, this action changes account enabled state. Account enabled state does not implement deleted-user recovery for operations-team identity onboarding; the operations-team identity onboarding still cannot recover a user that was deleted during the retention window.
- **D — Incorrect.** Add the administrator's directory object ID to the group's owner collection.
  Add the administrator's directory object ID to the group's owner collection. In the operations-team identity onboarding, this action changes group ownership. Operations-team identity onboarding instead needs deleted-user recovery: Locate the deleted directory object and restore it before the retention window expires. The group ownership action omits that deleted-user recovery work.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Restore or permanently remove recently deleted users](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore)

**Source reviewed:** 2026-08-31

## LAB01-Q20 — A

**Question:** The operations-team identity onboarding plan must keep automation stable after a display name or sign-in name changes while limiting the mutation scope to identity onboarding. Which action is appropriate?

- **A — Correct.** Persist returned user and group object IDs immediately in the lab run-state record.
  For the operations-team identity onboarding, the required immutable directory object IDs action is: persist returned user and group object IDs immediately in the lab run-state record. It makes the environment able to keep automation stable after a display name or sign-in name changes.
- **B — Incorrect.** Create the user with a unique UPN, display name, and initial password through Azure CLI.
  Create the user with a unique UPN, display name, and initial password through Azure CLI. In the operations-team identity onboarding, this action changes cloud-only user creation. Cloud-only user creation does not implement immutable directory object IDs for operations-team identity onboarding; the operations-team identity onboarding still cannot keep automation stable after a display name or sign-in name changes.
- **C — Incorrect.** Create a security group with a unique mail nickname and security capability enabled.
  Create a security group with a unique mail nickname and security capability enabled. In the operations-team identity onboarding, this action changes security group creation. Operations-team identity onboarding instead needs immutable directory object IDs: Persist returned user and group object IDs immediately in the lab run-state record. The security group creation action omits that immutable directory object IDs work.
- **D — Incorrect.** Read userType before applying automation that should target only member or only guest accounts.
  Read userType before applying automation that should target only member or only guest accounts. In the operations-team identity onboarding, this action changes member and guest user types. Operations-team identity onboarding approved immutable directory object IDs, not member and guest user types; only the immutable directory object IDs change can keep automation stable after a display name or sign-in name changes.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q21 — D

**Question:** The operations-team identity onboarding setup reports success after the identity onboarding attempt to use a custom tenant suffix when creating an operations account. Which identity onboarding read-only observation proves the operations-team identity onboarding outcome?

- **A — Incorrect.** Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
  Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state. In the operations-team identity onboarding, this check observes account enabled state. Operations-team identity onboarding output covers account enabled state, not verified UPN suffixes; the verified UPN suffixes requirement to use a custom tenant suffix when creating an operations account remains unverified.
- **B — Incorrect.** List group owners and confirm the administrator's immutable object ID is present.
  List group owners and confirm the administrator's immutable object ID is present. In the operations-team identity onboarding, this check observes group ownership. Group ownership success in operations-team identity onboarding cannot verify verified UPN suffixes; operations-team identity onboarding cannot use a custom tenant suffix when creating an operations account until verified UPN suffixes evidence exists.
- **C — Incorrect.** Resolve each persisted ID directly and compare its current properties with the intended state.
  Resolve each persisted ID directly and compare its current properties with the intended state. In the operations-team identity onboarding, this check observes immutable directory object IDs. Operations-team identity onboarding reads immutable directory object IDs, leaving verified UPN suffixes unproved in operations-team identity onboarding; operations-team identity onboarding still has no verified UPN suffixes proof.
- **D — Correct.** Query the created user and confirm that userPrincipalName ends in the selected verified domain.
  Query the created user and confirm that userPrincipalName ends in the selected verified domain. Because the operations-team identity onboarding check observes verified UPN suffixes, it independently verifies the requirement to use a custom tenant suffix when creating an operations account.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [List domains with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/domain-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q22 — D

**Question:** The identity onboarding log says the operations-team identity onboarding can now create a user whose identity exists only in this tenant. Which identity onboarding state should the operations-team identity onboarding acceptance test retain?

- **A — Incorrect.** Query the group and confirm securityEnabled is true while mailEnabled is false.
  Query the group and confirm securityEnabled is true while mailEnabled is false. In the operations-team identity onboarding, this check observes security group creation. Security group creation success in operations-team identity onboarding cannot verify cloud-only user creation; operations-team identity onboarding cannot create a user whose identity exists only in this tenant until cloud-only user creation evidence exists.
- **B — Incorrect.** Query userType and externalUserState for the exact directory object under review.
  Query userType and externalUserState for the exact directory object under review. In the operations-team identity onboarding, this check observes member and guest user types. Operations-team identity onboarding reads member and guest user types, leaving cloud-only user creation unproved in operations-team identity onboarding; operations-team identity onboarding still has no cloud-only user creation proof.
- **C — Incorrect.** Query the created user and confirm that userPrincipalName ends in the selected verified domain.
  Query the created user and confirm that userPrincipalName ends in the selected verified domain. In the operations-team identity onboarding, this check observes verified UPN suffixes. Operations-team identity onboarding could pass verified UPN suffixes while cloud-only user creation is wrong; operations-team identity onboarding still lacks cloud-only user creation proof.
- **D — Correct.** Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
  The operations-team identity onboarding validator needs this cloud-only user creation result: query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values. It proves the outcome to create a user whose identity exists only in this tenant rather than an adjacent checkpoint.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra users](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q23 — A

**Question:** The operations-team identity onboarding rejects identity onboarding exit status as proof it can capture organizational profile metadata on the directory object. Which operations-team identity onboarding result is valid evidence?

- **A — Correct.** Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
  Read the same object ID and project the updated department, jobTitle, and usageLocation properties. This is independent user profile properties evidence for the operations-team identity onboarding, even if operations-team identity onboarding setup reports success before user profile properties becomes observable.
- **B — Incorrect.** List group members and match the exact user object ID rather than only its display name.
  List group members and match the exact user object ID rather than only its display name. In the operations-team identity onboarding, this check observes group membership. Operations-team identity onboarding could pass group membership while user profile properties is wrong; operations-team identity onboarding still lacks user profile properties proof.
- **C — Incorrect.** Query the restored object ID and verify that it has returned to the active users collection.
  Query the restored object ID and verify that it has returned to the active users collection. In the operations-team identity onboarding, this check observes deleted-user recovery. Operations-team identity onboarding output covers deleted-user recovery, not user profile properties; the user profile properties requirement to capture organizational profile metadata on the directory object remains unverified.
- **D — Incorrect.** Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
  Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values. In the operations-team identity onboarding, this check observes cloud-only user creation. Cloud-only user creation success in operations-team identity onboarding cannot verify user profile properties; operations-team identity onboarding cannot capture organizational profile metadata on the directory object until user profile properties evidence exists.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q24 — B

**Question:** The identity onboarding validator needs one operations-team identity onboarding query after the change to block one user from signing in without deleting the account. Which identity onboarding property should the operations-team identity onboarding validator inspect?

- **A — Incorrect.** List group owners and confirm the administrator's immutable object ID is present.
  List group owners and confirm the administrator's immutable object ID is present. In the operations-team identity onboarding, this check observes group ownership. Operations-team identity onboarding could pass group ownership while account enabled state is wrong; operations-team identity onboarding still lacks account enabled state proof.
- **B — Correct.** Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
  Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state. For operations-team identity onboarding, this account enabled state read confirms the service can block one user from signing in without deleting the account.
- **C — Incorrect.** Resolve each persisted ID directly and compare its current properties with the intended state.
  Resolve each persisted ID directly and compare its current properties with the intended state. In the operations-team identity onboarding, this check observes immutable directory object IDs. Immutable directory object IDs success in operations-team identity onboarding cannot verify account enabled state; operations-team identity onboarding cannot block one user from signing in without deleting the account until account enabled state evidence exists.
- **D — Incorrect.** Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
  Read the same object ID and project the updated department, jobTitle, and usageLocation properties. In the operations-team identity onboarding, this check observes user profile properties. Operations-team identity onboarding reads user profile properties, leaving account enabled state unproved in operations-team identity onboarding; operations-team identity onboarding still has no account enabled state proof.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q25 — D

**Question:** The identity administrator onboarding a small operations team must confirm the operations-team identity onboarding, without mutation, can build a security-only group that has no email address. Which identity onboarding check qualifies?

- **A — Incorrect.** Query userType and externalUserState for the exact directory object under review.
  Query userType and externalUserState for the exact directory object under review. In the operations-team identity onboarding, this check observes member and guest user types. Operations-team identity onboarding output covers member and guest user types, not security group creation; the security group creation requirement to build a security-only group that has no email address remains unverified.
- **B — Incorrect.** Query the created user and confirm that userPrincipalName ends in the selected verified domain.
  Query the created user and confirm that userPrincipalName ends in the selected verified domain. In the operations-team identity onboarding, this check observes verified UPN suffixes. Verified UPN suffixes success in operations-team identity onboarding cannot verify security group creation; operations-team identity onboarding cannot build a security-only group that has no email address until security group creation evidence exists.
- **C — Incorrect.** Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
  Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state. In the operations-team identity onboarding, this check observes account enabled state. Operations-team identity onboarding reads account enabled state, leaving security group creation unproved in operations-team identity onboarding; operations-team identity onboarding still has no security group creation proof.
- **D — Correct.** Query the group and confirm securityEnabled is true while mailEnabled is false.
  Query the group and confirm securityEnabled is true while mailEnabled is false. The operations-team identity onboarding reads security group creation directly; that security group creation result proves the operations-team identity onboarding can build a security-only group that has no email address without another mutation.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra groups](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q26 — A

**Question:** The operations-team identity onboarding configuration is complete; the identity onboarding reviewers need evidence it can give a user the access assigned to an operations group. Which observation shows success?

- **A — Correct.** List group members and match the exact user object ID rather than only its display name.
  For the operations-team identity onboarding, this group membership observation is decisive: list group members and match the exact user object ID rather than only its display name. It is operations-team identity onboarding evidence that operators can give a user the access assigned to an operations group.
- **B — Incorrect.** Query the restored object ID and verify that it has returned to the active users collection.
  Query the restored object ID and verify that it has returned to the active users collection. In the operations-team identity onboarding, this check observes deleted-user recovery. Operations-team identity onboarding reads deleted-user recovery, leaving group membership unproved in operations-team identity onboarding; operations-team identity onboarding still has no group membership proof.
- **C — Incorrect.** Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
  Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values. In the operations-team identity onboarding, this check observes cloud-only user creation. Operations-team identity onboarding could pass cloud-only user creation while group membership is wrong; operations-team identity onboarding still lacks group membership proof.
- **D — Incorrect.** Query the group and confirm securityEnabled is true while mailEnabled is false.
  Query the group and confirm securityEnabled is true while mailEnabled is false. In the operations-team identity onboarding, this check observes security group creation. Operations-team identity onboarding output covers security group creation, not group membership; the group membership requirement to give a user the access assigned to an operations group remains unverified.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group membership](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q27 — A

**Question:** The identity onboarding validation asks whether the operations-team identity onboarding can let an administrator manage membership without receiving the group's access. Which observable state is strongest?

- **A — Correct.** List group owners and confirm the administrator's immutable object ID is present.
  List group owners and confirm the administrator's immutable object ID is present. Because the operations-team identity onboarding check observes group ownership, it independently verifies the requirement to let an administrator manage membership without receiving the group's access.
- **B — Incorrect.** Resolve each persisted ID directly and compare its current properties with the intended state.
  Resolve each persisted ID directly and compare its current properties with the intended state. In the operations-team identity onboarding, this check observes immutable directory object IDs. Operations-team identity onboarding could pass immutable directory object IDs while group ownership is wrong; operations-team identity onboarding still lacks group ownership proof.
- **C — Incorrect.** Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
  Read the same object ID and project the updated department, jobTitle, and usageLocation properties. In the operations-team identity onboarding, this check observes user profile properties. Operations-team identity onboarding output covers user profile properties, not group ownership; the group ownership requirement to let an administrator manage membership without receiving the group's access remains unverified.
- **D — Incorrect.** List group members and match the exact user object ID rather than only its display name.
  List group members and match the exact user object ID rather than only its display name. In the operations-team identity onboarding, this check observes group membership. Group membership success in operations-team identity onboarding cannot verify group ownership; operations-team identity onboarding cannot let an administrator manage membership without receiving the group's access until group ownership evidence exists.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group owners](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q28 — C

**Question:** An operations-team identity onboarding review must prove the identity onboarding ability to target automation to members while excluding external collaborators. Which check avoids an adjacent feature?

- **A — Incorrect.** Query the created user and confirm that userPrincipalName ends in the selected verified domain.
  Query the created user and confirm that userPrincipalName ends in the selected verified domain. In the operations-team identity onboarding, this check observes verified UPN suffixes. Operations-team identity onboarding could pass verified UPN suffixes while member and guest user types is wrong; operations-team identity onboarding still lacks member and guest user types proof.
- **B — Incorrect.** Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
  Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state. In the operations-team identity onboarding, this check observes account enabled state. Operations-team identity onboarding output covers account enabled state, not member and guest user types; the member and guest user types requirement to target automation to members while excluding external collaborators remains unverified.
- **C — Correct.** Query userType and externalUserState for the exact directory object under review.
  The operations-team identity onboarding validator needs this member and guest user types result: query userType and externalUserState for the exact directory object under review. It proves the outcome to target automation to members while excluding external collaborators rather than an adjacent checkpoint.
- **D — Incorrect.** List group owners and confirm the administrator's immutable object ID is present.
  List group owners and confirm the administrator's immutable object ID is present. In the operations-team identity onboarding, this check observes group ownership. Operations-team identity onboarding reads group ownership, leaving member and guest user types unproved in operations-team identity onboarding; operations-team identity onboarding still has no member and guest user types proof.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q29 — B

**Question:** The operations-team identity onboarding evidence bundle needs an identity onboarding result showing it can recover a user that was deleted during the retention window. Which result belongs in the checkpoint?

- **A — Incorrect.** Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
  Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values. In the operations-team identity onboarding, this check observes cloud-only user creation. Operations-team identity onboarding output covers cloud-only user creation, not deleted-user recovery; the deleted-user recovery requirement to recover a user that was deleted during the retention window remains unverified.
- **B — Correct.** Query the restored object ID and verify that it has returned to the active users collection.
  Query the restored object ID and verify that it has returned to the active users collection. This is independent deleted-user recovery evidence for the operations-team identity onboarding, even if operations-team identity onboarding setup reports success before deleted-user recovery becomes observable.
- **C — Incorrect.** Query the group and confirm securityEnabled is true while mailEnabled is false.
  Query the group and confirm securityEnabled is true while mailEnabled is false. In the operations-team identity onboarding, this check observes security group creation. Operations-team identity onboarding reads security group creation, leaving deleted-user recovery unproved in operations-team identity onboarding; operations-team identity onboarding still has no deleted-user recovery proof.
- **D — Incorrect.** Query userType and externalUserState for the exact directory object under review.
  Query userType and externalUserState for the exact directory object under review. In the operations-team identity onboarding, this check observes member and guest user types. Operations-team identity onboarding could pass member and guest user types while deleted-user recovery is wrong; operations-team identity onboarding still lacks deleted-user recovery proof.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Restore or permanently remove recently deleted users](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore)

**Source reviewed:** 2026-08-31

## LAB01-Q30 — D

**Question:** Before operations-team identity onboarding cleanup, the identity onboarding team must reconfirm it can keep automation stable after a display name or sign-in name changes. Which read-only inspection should run?

- **A — Incorrect.** Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
  Read the same object ID and project the updated department, jobTitle, and usageLocation properties. In the operations-team identity onboarding, this check observes user profile properties. User profile properties success in operations-team identity onboarding cannot verify immutable directory object IDs; operations-team identity onboarding cannot keep automation stable after a display name or sign-in name changes until immutable directory object IDs evidence exists.
- **B — Incorrect.** List group members and match the exact user object ID rather than only its display name.
  List group members and match the exact user object ID rather than only its display name. In the operations-team identity onboarding, this check observes group membership. Operations-team identity onboarding reads group membership, leaving immutable directory object IDs unproved in operations-team identity onboarding; operations-team identity onboarding still has no immutable directory object IDs proof.
- **C — Incorrect.** Query the restored object ID and verify that it has returned to the active users collection.
  Query the restored object ID and verify that it has returned to the active users collection. In the operations-team identity onboarding, this check observes deleted-user recovery. Operations-team identity onboarding could pass deleted-user recovery while immutable directory object IDs is wrong; operations-team identity onboarding still lacks immutable directory object IDs proof.
- **D — Correct.** Resolve each persisted ID directly and compare its current properties with the intended state.
  Resolve each persisted ID directly and compare its current properties with the intended state. For operations-team identity onboarding, this immutable directory object IDs read confirms the service can keep automation stable after a display name or sign-in name changes.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q31 — C

**Question:** During an identity onboarding fault drill, the operations-team identity onboarding does not use a custom tenant suffix when creating an operations account. Which finding identifies the defect?

- **A — Incorrect.** The runbook discarded the returned object ID and later queried a different user with a similar display name.
  The runbook discarded the returned object ID and later queried a different user with a similar display name. The operations-team identity onboarding fault concerns cloud-only user creation. Operations-team identity onboarding has cloud-only user creation impact, but verified UPN suffixes is the operations-team identity onboarding failed path; the cloud-only user creation state cannot produce verified UPN suffixes failure.
- **B — Incorrect.** The user was added as an owner but never added to the member collection.
  The user was added as an owner but never added to the member collection. The operations-team identity onboarding fault concerns group membership. Operations-team identity onboarding could repair group membership while verified UPN suffixes stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to use a custom tenant suffix when creating an operations account.
- **C — Correct.** The requested UPN uses a domain that is not verified in the tenant.
  The requested UPN uses a domain that is not verified in the tenant. This operations-team identity onboarding condition breaks verified UPN suffixes, explaining why operators cannot use a custom tenant suffix when creating an operations account.
- **D — Incorrect.** Cleanup searched by a reused display name and found an unrelated directory object.
  Cleanup searched by a reused display name and found an unrelated directory object. The operations-team identity onboarding fault concerns immutable directory object IDs. Operations-team identity onboarding may fix immutable directory object IDs, yet verified UPN suffixes still fails; this operations-team identity onboarding diagnosis of immutable directory object IDs is wrong for verified UPN suffixes.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [List domains with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/domain-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q32 — C

**Question:** The operations-team identity onboarding setup finishes, yet the identity onboarding cannot create a user whose identity exists only in this tenant. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The update targeted the user's display name instead of the immutable directory object ID.
  The update targeted the user's display name instead of the immutable directory object ID. The operations-team identity onboarding fault concerns user profile properties. Operations-team identity onboarding could repair user profile properties while cloud-only user creation stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to create a user whose identity exists only in this tenant.
- **B — Incorrect.** The administrator appears only in the member list and therefore lacks group-owner responsibility.
  The administrator appears only in the member list and therefore lacks group-owner responsibility. The operations-team identity onboarding fault concerns group ownership. Operations-team identity onboarding failed on cloud-only user creation; this group ownership finding redirects operations-team identity onboarding remediation away from cloud-only user creation.
- **C — Correct.** The runbook discarded the returned object ID and later queried a different user with a similar display name.
  For the operations-team identity onboarding, the cloud-only user creation failure is causal: the runbook discarded the returned object ID and later queried a different user with a similar display name. Correcting it restores the ability to create a user whose identity exists only in this tenant.
- **D — Incorrect.** The requested UPN uses a domain that is not verified in the tenant.
  The requested UPN uses a domain that is not verified in the tenant. The operations-team identity onboarding fault concerns verified UPN suffixes. Operations-team identity onboarding has verified UPN suffixes impact, but cloud-only user creation is the operations-team identity onboarding failed path; the verified UPN suffixes state cannot produce cloud-only user creation failure.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra users](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q33 — C

**Question:** An identity onboarding break/fix in the operations-team identity onboarding fails when operators try to capture organizational profile metadata on the directory object. Which diagnosis fits?

- **A — Incorrect.** The account remains disabled even though its group memberships were configured correctly.
  The account remains disabled even though its group memberships were configured correctly. The operations-team identity onboarding fault concerns account enabled state. Operations-team identity onboarding failed on user profile properties; this account enabled state finding redirects operations-team identity onboarding remediation away from user profile properties.
- **B — Incorrect.** The automation filtered on a UPN naming convention instead of the authoritative userType property.
  The automation filtered on a UPN naming convention instead of the authoritative userType property. The operations-team identity onboarding fault concerns member and guest user types. Operations-team identity onboarding may fix member and guest user types, yet user profile properties still fails; this operations-team identity onboarding diagnosis of member and guest user types is wrong for user profile properties.
- **C — Correct.** The update targeted the user's display name instead of the immutable directory object ID.
  The update targeted the user's display name instead of the immutable directory object ID. The finding is specific to user profile properties in the operations-team identity onboarding; repairing user profile properties restores the operations-team identity onboarding ability to capture organizational profile metadata on the directory object.
- **D — Incorrect.** The runbook discarded the returned object ID and later queried a different user with a similar display name.
  The runbook discarded the returned object ID and later queried a different user with a similar display name. The operations-team identity onboarding fault concerns cloud-only user creation. Operations-team identity onboarding could repair cloud-only user creation while user profile properties stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to capture organizational profile metadata on the directory object.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q34 — B

**Question:** The operations-team identity onboarding troubleshooting scope is the identity onboarding need to block one user from signing in without deleting the account. Which condition should be corrected first?

- **A — Incorrect.** The group was created as a non-security Microsoft 365 collaboration group.
  The group was created as a non-security Microsoft 365 collaboration group. The operations-team identity onboarding fault concerns security group creation. Operations-team identity onboarding may fix security group creation, yet account enabled state still fails; this operations-team identity onboarding diagnosis of security group creation is wrong for account enabled state.
- **B — Correct.** The account remains disabled even though its group memberships were configured correctly.
  The operations-team identity onboarding cannot block one user from signing in without deleting the account because of this account enabled state defect: the account remains disabled even though its group memberships were configured correctly. The symptom and repair align.
- **C — Incorrect.** The object was permanently deleted or its deleted-item retention window has expired.
  The object was permanently deleted or its deleted-item retention window has expired. The operations-team identity onboarding fault concerns deleted-user recovery. Operations-team identity onboarding could repair deleted-user recovery while account enabled state stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to block one user from signing in without deleting the account.
- **D — Incorrect.** The update targeted the user's display name instead of the immutable directory object ID.
  The update targeted the user's display name instead of the immutable directory object ID. The operations-team identity onboarding fault concerns user profile properties. Operations-team identity onboarding failed on account enabled state; this user profile properties finding redirects operations-team identity onboarding remediation away from account enabled state.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q35 — C

**Question:** The operations-team identity onboarding result is partial because the identity onboarding cannot build a security-only group that has no email address. Which condition accounts for that result?

- **A — Incorrect.** The user was added as an owner but never added to the member collection.
  The user was added as an owner but never added to the member collection. The operations-team identity onboarding fault concerns group membership. Operations-team identity onboarding has group membership impact, but security group creation is the operations-team identity onboarding failed path; the group membership state cannot produce security group creation failure.
- **B — Incorrect.** Cleanup searched by a reused display name and found an unrelated directory object.
  Cleanup searched by a reused display name and found an unrelated directory object. The operations-team identity onboarding fault concerns immutable directory object IDs. Operations-team identity onboarding could repair immutable directory object IDs while security group creation stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to build a security-only group that has no email address.
- **C — Correct.** The group was created as a non-security Microsoft 365 collaboration group.
  The group was created as a non-security Microsoft 365 collaboration group. Removing this security group creation condition lets the operations-team identity onboarding build a security-only group that has no email address while leaving healthy controls unchanged.
- **D — Incorrect.** The account remains disabled even though its group memberships were configured correctly.
  The account remains disabled even though its group memberships were configured correctly. The operations-team identity onboarding fault concerns account enabled state. Operations-team identity onboarding may fix account enabled state, yet security group creation still fails; this operations-team identity onboarding diagnosis of account enabled state is wrong for security group creation.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra groups](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q36 — C

**Question:** The identity onboarding evidence shows the operations-team identity onboarding cannot give a user the access assigned to an operations group. Which root cause fits that evidence?

- **A — Incorrect.** The administrator appears only in the member list and therefore lacks group-owner responsibility.
  The administrator appears only in the member list and therefore lacks group-owner responsibility. The operations-team identity onboarding fault concerns group ownership. Operations-team identity onboarding could repair group ownership while group membership stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to give a user the access assigned to an operations group.
- **B — Incorrect.** The requested UPN uses a domain that is not verified in the tenant.
  The requested UPN uses a domain that is not verified in the tenant. The operations-team identity onboarding fault concerns verified UPN suffixes. Operations-team identity onboarding failed on group membership; this verified UPN suffixes finding redirects operations-team identity onboarding remediation away from group membership.
- **C — Correct.** The user was added as an owner but never added to the member collection.
  The user was added as an owner but never added to the member collection. In operations-team identity onboarding, this group membership cause matches the failure to give a user the access assigned to an operations group.
- **D — Incorrect.** The group was created as a non-security Microsoft 365 collaboration group.
  The group was created as a non-security Microsoft 365 collaboration group. The operations-team identity onboarding fault concerns security group creation. Operations-team identity onboarding has security group creation impact, but group membership is the operations-team identity onboarding failed path; the security group creation state cannot produce group membership failure.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group membership](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q37 — D

**Question:** Although the operations-team identity onboarding is meant to let the identity onboarding let an administrator manage membership without receiving the group's access, its checkpoint fails. Which identity onboarding defect explains the failure?

- **A — Incorrect.** The automation filtered on a UPN naming convention instead of the authoritative userType property.
  The automation filtered on a UPN naming convention instead of the authoritative userType property. The operations-team identity onboarding fault concerns member and guest user types. Operations-team identity onboarding failed on group ownership; this member and guest user types finding redirects operations-team identity onboarding remediation away from group ownership.
- **B — Incorrect.** The runbook discarded the returned object ID and later queried a different user with a similar display name.
  The runbook discarded the returned object ID and later queried a different user with a similar display name. The operations-team identity onboarding fault concerns cloud-only user creation. Operations-team identity onboarding may fix cloud-only user creation, yet group ownership still fails; this operations-team identity onboarding diagnosis of cloud-only user creation is wrong for group ownership.
- **C — Incorrect.** The user was added as an owner but never added to the member collection.
  The user was added as an owner but never added to the member collection. The operations-team identity onboarding fault concerns group membership. Operations-team identity onboarding has group membership impact, but group ownership is the operations-team identity onboarding failed path; the group membership state cannot produce group ownership failure.
- **D — Correct.** The administrator appears only in the member list and therefore lacks group-owner responsibility.
  The administrator appears only in the member list and therefore lacks group-owner responsibility. This operations-team identity onboarding condition breaks group ownership, explaining why operators cannot let an administrator manage membership without receiving the group's access.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group owners](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q38 — B

**Question:** The identity onboarding support team isolated the operations-team identity onboarding incident to the attempt to target automation to members while excluding external collaborators. Which condition prevents success?

- **A — Incorrect.** The object was permanently deleted or its deleted-item retention window has expired.
  The object was permanently deleted or its deleted-item retention window has expired. The operations-team identity onboarding fault concerns deleted-user recovery. Operations-team identity onboarding may fix deleted-user recovery, yet member and guest user types still fails; this operations-team identity onboarding diagnosis of deleted-user recovery is wrong for member and guest user types.
- **B — Correct.** The automation filtered on a UPN naming convention instead of the authoritative userType property.
  For the operations-team identity onboarding, the member and guest user types failure is causal: the automation filtered on a UPN naming convention instead of the authoritative userType property. Correcting it restores the ability to target automation to members while excluding external collaborators.
- **C — Incorrect.** The update targeted the user's display name instead of the immutable directory object ID.
  The update targeted the user's display name instead of the immutable directory object ID. The operations-team identity onboarding fault concerns user profile properties. Operations-team identity onboarding could repair user profile properties while member and guest user types stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to target automation to members while excluding external collaborators.
- **D — Incorrect.** The administrator appears only in the member list and therefore lacks group-owner responsibility.
  The administrator appears only in the member list and therefore lacks group-owner responsibility. The operations-team identity onboarding fault concerns group ownership. Operations-team identity onboarding failed on member and guest user types; this group ownership finding redirects operations-team identity onboarding remediation away from member and guest user types.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q39 — D

**Question:** An operations-team identity onboarding query surprises the identity administrator onboarding a small operations team during the identity onboarding attempt to recover a user that was deleted during the retention window. Which finding explains it?

- **A — Incorrect.** Cleanup searched by a reused display name and found an unrelated directory object.
  Cleanup searched by a reused display name and found an unrelated directory object. The operations-team identity onboarding fault concerns immutable directory object IDs. Operations-team identity onboarding has immutable directory object IDs impact, but deleted-user recovery is the operations-team identity onboarding failed path; the immutable directory object IDs state cannot produce deleted-user recovery failure.
- **B — Incorrect.** The account remains disabled even though its group memberships were configured correctly.
  The account remains disabled even though its group memberships were configured correctly. The operations-team identity onboarding fault concerns account enabled state. Operations-team identity onboarding could repair account enabled state while deleted-user recovery stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to recover a user that was deleted during the retention window.
- **C — Incorrect.** The automation filtered on a UPN naming convention instead of the authoritative userType property.
  The automation filtered on a UPN naming convention instead of the authoritative userType property. The operations-team identity onboarding fault concerns member and guest user types. Operations-team identity onboarding failed on deleted-user recovery; this member and guest user types finding redirects operations-team identity onboarding remediation away from deleted-user recovery.
- **D — Correct.** The object was permanently deleted or its deleted-item retention window has expired.
  The object was permanently deleted or its deleted-item retention window has expired. The finding is specific to deleted-user recovery in the operations-team identity onboarding; repairing deleted-user recovery restores the operations-team identity onboarding ability to recover a user that was deleted during the retention window.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Restore or permanently remove recently deleted users](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore)

**Source reviewed:** 2026-08-31

## LAB01-Q40 — C

**Question:** Other operations-team identity onboarding components are healthy, but the identity onboarding still cannot keep automation stable after a display name or sign-in name changes. Which state causes the isolated failure?

- **A — Incorrect.** The requested UPN uses a domain that is not verified in the tenant.
  The requested UPN uses a domain that is not verified in the tenant. The operations-team identity onboarding fault concerns verified UPN suffixes. Operations-team identity onboarding could repair verified UPN suffixes while immutable directory object IDs stays broken in operations-team identity onboarding; the operations-team identity onboarding remains unable to keep automation stable after a display name or sign-in name changes.
- **B — Incorrect.** The group was created as a non-security Microsoft 365 collaboration group.
  The group was created as a non-security Microsoft 365 collaboration group. The operations-team identity onboarding fault concerns security group creation. Operations-team identity onboarding failed on immutable directory object IDs; this security group creation finding redirects operations-team identity onboarding remediation away from immutable directory object IDs.
- **C — Correct.** Cleanup searched by a reused display name and found an unrelated directory object.
  The operations-team identity onboarding cannot keep automation stable after a display name or sign-in name changes because of this immutable directory object IDs defect: cleanup searched by a reused display name and found an unrelated directory object. The symptom and repair align.
- **D — Incorrect.** The object was permanently deleted or its deleted-item retention window has expired.
  The object was permanently deleted or its deleted-item retention window has expired. The operations-team identity onboarding fault concerns deleted-user recovery. Operations-team identity onboarding has deleted-user recovery impact, but immutable directory object IDs is the operations-team identity onboarding failed path; the deleted-user recovery state cannot produce immutable directory object IDs failure.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q41 — D

**Question:** The operations-team identity onboarding runbook must use a custom tenant suffix when creating an operations account, then retain identity onboarding read-back evidence. Which operations-team identity onboarding pair completes both duties?

- **A — Incorrect.** First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
  First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties. This operations-team identity onboarding pair serves user profile properties. User profile properties cannot replace verified UPN suffixes in operations-team identity onboarding. Use this verified UPN suffixes pair instead: First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.
- **B — Incorrect.** First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.
  First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present. This operations-team identity onboarding pair serves group ownership. Operations-team identity onboarding proves group ownership, but verified UPN suffixes lacks implementation in operations-team identity onboarding and verified UPN suffixes proof; the verified UPN suffixes outcome to use a custom tenant suffix when creating an operations account remains open.
- **C — Incorrect.** First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
  First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review. This operations-team identity onboarding pair serves member and guest user types. Operations-team identity onboarding uses member and guest user types for both steps; verified UPN suffixes remains untouched in operations-team identity onboarding, so its verified UPN suffixes gate to use a custom tenant suffix when creating an operations account fails.
- **D — Correct.** First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.
  First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain. This ordered verified UPN suffixes workflow lets the operations-team identity onboarding use a custom tenant suffix when creating an operations account and then verify the resulting state.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [List domains with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/domain-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q42 — A

**Question:** To satisfy the identity onboarding requirement, operators must change the operations-team identity onboarding configuration and prove it can create a user whose identity exists only in this tenant. Which sequence is coherent?

- **A — Correct.** First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
  First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values. For operations-team identity onboarding, the cloud-only user creation operation precedes its cloud-only user creation read-back check, allowing it to create a user whose identity exists only in this tenant.
- **B — Incorrect.** First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
  First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state. This operations-team identity onboarding pair serves account enabled state. Operations-team identity onboarding uses account enabled state for both steps; cloud-only user creation remains untouched in operations-team identity onboarding, so its cloud-only user creation gate to create a user whose identity exists only in this tenant fails.
- **C — Incorrect.** First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
  First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review. This operations-team identity onboarding pair serves member and guest user types. Operations-team identity onboarding closes member and guest user types, not cloud-only user creation; without the cloud-only user creation workflow, it cannot create a user whose identity exists only in this tenant.
- **D — Incorrect.** First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.
  First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection. This operations-team identity onboarding pair serves deleted-user recovery. Deleted-user recovery cannot replace cloud-only user creation in operations-team identity onboarding. Use this cloud-only user creation pair instead: First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra users](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q43 — B

**Question:** The identity administrator onboarding a small operations team needs a safe operations-team identity onboarding change to capture organizational profile metadata on the directory object, followed by identity onboarding evidence. Which pair merits approval?

- **A — Incorrect.** First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.
  First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false. This operations-team identity onboarding pair serves security group creation. Operations-team identity onboarding uses security group creation for both steps; user profile properties remains untouched in operations-team identity onboarding, so its user profile properties gate to capture organizational profile metadata on the directory object fails.
- **B — Correct.** First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
  First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties. In the operations-team identity onboarding, the first user profile properties step runs; the operations-team identity onboarding then reads user profile properties state to prove it can capture organizational profile metadata on the directory object.
- **C — Incorrect.** First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.
  First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection. This operations-team identity onboarding pair serves deleted-user recovery. Deleted-user recovery cannot replace user profile properties in operations-team identity onboarding. Use this user profile properties pair instead: First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
- **D — Incorrect.** First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.
  First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state. This operations-team identity onboarding pair serves immutable directory object IDs. Operations-team identity onboarding proves immutable directory object IDs, but user profile properties lacks implementation in operations-team identity onboarding and user profile properties proof; the user profile properties outcome to capture organizational profile metadata on the directory object remains open.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q44 — D

**Question:** The operations-team identity onboarding has two identity onboarding gates: block one user from signing in without deleting the account, then prove the operations-team identity onboarding state. Which identity onboarding sequence works?

- **A — Incorrect.** First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.
  First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name. This operations-team identity onboarding pair serves group membership. Operations-team identity onboarding closes group membership, not account enabled state; without the account enabled state workflow, it cannot block one user from signing in without deleting the account.
- **B — Incorrect.** First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.
  First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state. This operations-team identity onboarding pair serves immutable directory object IDs. Immutable directory object IDs cannot replace account enabled state in operations-team identity onboarding. Use this account enabled state pair instead: First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
- **C — Incorrect.** First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.
  First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain. This operations-team identity onboarding pair serves verified UPN suffixes. Operations-team identity onboarding proves verified UPN suffixes, but account enabled state lacks implementation in operations-team identity onboarding and account enabled state proof; the account enabled state outcome to block one user from signing in without deleting the account remains open.
- **D — Correct.** First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
  For the operations-team identity onboarding, the safe account enabled state order is: first, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state. The operations-team identity onboarding records account enabled state proof after configuration.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q45 — C

**Question:** Which identity onboarding path makes the operations-team identity onboarding able to build a security-only group that has no email address, then inspects the defining properties?

- **A — Incorrect.** First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.
  First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present. This operations-team identity onboarding pair serves group ownership. Group ownership cannot replace security group creation in operations-team identity onboarding. Use this security group creation pair instead: First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.
- **B — Incorrect.** First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.
  First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain. This operations-team identity onboarding pair serves verified UPN suffixes. Operations-team identity onboarding proves verified UPN suffixes, but security group creation lacks implementation in operations-team identity onboarding and security group creation proof; the security group creation outcome to build a security-only group that has no email address remains open.
- **C — Correct.** First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.
  First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false. The operations-team identity onboarding uses its security group creation mutation gate and security group creation verification gate before it can build a security-only group that has no email address.
- **D — Incorrect.** First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
  First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values. This operations-team identity onboarding pair serves cloud-only user creation. Operations-team identity onboarding closes cloud-only user creation, not security group creation; without the security group creation workflow, it cannot build a security-only group that has no email address.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra groups](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q46 — C

**Question:** At the operations-team identity onboarding approval gate, operators must show that the identity onboarding can give a user the access assigned to an operations group. Which identity onboarding configure-and-check pair is defensible?

- **A — Incorrect.** First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
  First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review. This operations-team identity onboarding pair serves member and guest user types. Operations-team identity onboarding proves member and guest user types, but group membership lacks implementation in operations-team identity onboarding and group membership proof; the group membership outcome to give a user the access assigned to an operations group remains open.
- **B — Incorrect.** First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
  First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values. This operations-team identity onboarding pair serves cloud-only user creation. Operations-team identity onboarding uses cloud-only user creation for both steps; group membership remains untouched in operations-team identity onboarding, so its group membership gate to give a user the access assigned to an operations group fails.
- **C — Correct.** First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.
  The operations-team identity onboarding gets a complete group membership sequence here: first, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name. Read-back evidence follows the change.
- **D — Incorrect.** First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
  First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties. This operations-team identity onboarding pair serves user profile properties. User profile properties cannot replace group membership in operations-team identity onboarding. Use this group membership pair instead: First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.

**Objectives:** `IG-USERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB01-CP01`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group membership](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q47 — D

**Question:** The operations-team identity onboarding forbids a partial identity onboarding result. Operators must first let an administrator manage membership without receiving the group's access and afterward confirm the operations-team identity onboarding outcome. Which identity onboarding sequence is complete?

- **A — Incorrect.** First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.
  First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection. This operations-team identity onboarding pair serves deleted-user recovery. Operations-team identity onboarding uses deleted-user recovery for both steps; group ownership remains untouched in operations-team identity onboarding, so its group ownership gate to let an administrator manage membership without receiving the group's access fails.
- **B — Incorrect.** First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties.
  First, Patch the intended user object through Microsoft Graph by using its immutable object ID. Then, Read the same object ID and project the updated department, jobTitle, and usageLocation properties. This operations-team identity onboarding pair serves user profile properties. Operations-team identity onboarding closes user profile properties, not group ownership; without the group ownership workflow, it cannot let an administrator manage membership without receiving the group's access.
- **C — Incorrect.** First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
  First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state. This operations-team identity onboarding pair serves account enabled state. Account enabled state cannot replace group ownership in operations-team identity onboarding. Use this group ownership pair instead: First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.
- **D — Correct.** First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.
  First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present. This ordered group ownership workflow lets the operations-team identity onboarding let an administrator manage membership without receiving the group's access and then verify the resulting state.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB01-CP02`).

**Microsoft Learn sources:**

- [Azure CLI reference for Microsoft Entra group owners](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest)

**Source reviewed:** 2026-08-31

## LAB01-Q48 — A

**Question:** Only the operations-team identity onboarding change needed to target automation to members while excluding external collaborators is allowed, and identity onboarding proof is mandatory. Which pair fits?

- **A — Correct.** First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
  First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review. For operations-team identity onboarding, the member and guest user types operation precedes its member and guest user types read-back check, allowing it to target automation to members while excluding external collaborators.
- **B — Incorrect.** First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.
  First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state. This operations-team identity onboarding pair serves immutable directory object IDs. Immutable directory object IDs cannot replace member and guest user types in operations-team identity onboarding. Use this member and guest user types pair instead: First, Read userType before applying automation that should target only member or only guest accounts. Then, Query userType and externalUserState for the exact directory object under review.
- **C — Incorrect.** First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state.
  First, Set accountEnabled on the target user while leaving its identity and group memberships intact. Then, Read accountEnabled from Microsoft Graph and confirm it matches the intended sign-in state. This operations-team identity onboarding pair serves account enabled state. Operations-team identity onboarding proves account enabled state, but member and guest user types lacks implementation in operations-team identity onboarding and member and guest user types proof; the member and guest user types outcome to target automation to members while excluding external collaborators remains open.
- **D — Incorrect.** First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.
  First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false. This operations-team identity onboarding pair serves security group creation. Operations-team identity onboarding uses security group creation for both steps; member and guest user types remains untouched in operations-team identity onboarding, so its member and guest user types gate to target automation to members while excluding external collaborators fails.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB01-CP03`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB01-Q49 — B

**Question:** The operations-team identity onboarding runbook separates identity onboarding mutation from validation while it must recover a user that was deleted during the retention window. Which sequence proves it cleanly?

- **A — Incorrect.** First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain.
  First, Read the tenant's verified domains before constructing the new userPrincipalName. Then, Query the created user and confirm that userPrincipalName ends in the selected verified domain. This operations-team identity onboarding pair serves verified UPN suffixes. Verified UPN suffixes cannot replace deleted-user recovery in operations-team identity onboarding. Use this deleted-user recovery pair instead: First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.
- **B — Correct.** First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection.
  First, Locate the deleted directory object and restore it before the retention window expires. Then, Query the restored object ID and verify that it has returned to the active users collection. In the operations-team identity onboarding, the first deleted-user recovery step runs; the operations-team identity onboarding then reads deleted-user recovery state to prove it can recover a user that was deleted during the retention window.
- **C — Incorrect.** First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false.
  First, Create a security group with a unique mail nickname and security capability enabled. Then, Query the group and confirm securityEnabled is true while mailEnabled is false. This operations-team identity onboarding pair serves security group creation. Operations-team identity onboarding uses security group creation for both steps; deleted-user recovery remains untouched in operations-team identity onboarding, so its deleted-user recovery gate to recover a user that was deleted during the retention window fails.
- **D — Incorrect.** First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.
  First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name. This operations-team identity onboarding pair serves group membership. Operations-team identity onboarding closes group membership, not deleted-user recovery; without the deleted-user recovery workflow, it cannot recover a user that was deleted during the retention window.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB01-CP04`).

**Microsoft Learn sources:**

- [Restore or permanently remove recently deleted users](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore)

**Source reviewed:** 2026-08-31

## LAB01-Q50 — B

**Question:** The operations-team identity onboarding checkpoint requires both this identity onboarding outcome—keep automation stable after a display name or sign-in name changes—and a read-only operations-team identity onboarding state check. Which identity onboarding response is complete?

- **A — Incorrect.** First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values.
  First, Create the user with a unique UPN, display name, and initial password through Azure CLI. Then, Query the returned object ID and confirm the displayName, userPrincipalName, and accountEnabled values. This operations-team identity onboarding pair serves cloud-only user creation. Operations-team identity onboarding proves cloud-only user creation, but immutable directory object IDs lacks implementation in operations-team identity onboarding and immutable directory object IDs proof; the immutable directory object IDs outcome to keep automation stable after a display name or sign-in name changes remains open.
- **B — Correct.** First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.
  For the operations-team identity onboarding, the safe immutable directory object IDs order is: first, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state. The operations-team identity onboarding records immutable directory object IDs proof after configuration.
- **C — Incorrect.** First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name.
  First, Add the user's object ID to the intended group's member collection. Then, List group members and match the exact user object ID rather than only its display name. This operations-team identity onboarding pair serves group membership. Operations-team identity onboarding closes group membership, not immutable directory object IDs; without the immutable directory object IDs workflow, it cannot keep automation stable after a display name or sign-in name changes.
- **D — Incorrect.** First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present.
  First, Add the administrator's directory object ID to the group's owner collection. Then, List group owners and confirm the administrator's immutable object ID is present. This operations-team identity onboarding pair serves group ownership. Group ownership cannot replace immutable directory object IDs in operations-team identity onboarding. Use this immutable directory object IDs pair instead: First, Persist returned user and group object IDs immediately in the lab run-state record. Then, Resolve each persisted ID directly and compare its current properties with the intended state.

**Objectives:** `IG-USERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB01-CP05`).

**Microsoft Learn sources:**

- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31
