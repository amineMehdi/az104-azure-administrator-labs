# Lab 02 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB02-Q01 — C

**Question:** The guest collaboration review compares four claims for the external-collaboration and SSPR pilot requirement to confirm that the tenant has an unused product unit before assignment. Which claim is technically sound?

- **A — Incorrect.** A user's usageLocation must be set before Microsoft Entra can assign many commercial licenses.
  A user's usageLocation must be set before Microsoft Entra can assign many commercial licenses. In the external-collaboration and SSPR pilot, this statement describes usage location prerequisite. External-collaboration and SSPR pilot asks about available license capacity; this usage location prerequisite choice leaves the available license capacity explanation missing.
- **B — Incorrect.** A B2B invitation creates an external user object and sends or returns a redemption invitation.
  A B2B invitation creates an external user object and sends or returns a redemption invitation. In the external-collaboration and SSPR pilot, this statement describes B2B guest invitations. The B2B guest invitations statement accurately describes B2B guest invitations; however, external-collaboration and SSPR pilot needs available license capacity to confirm that the tenant has an unused product unit before assignment; B2B guest invitations cannot replace available license capacity.
- **C — Correct.** A tenant can assign a product license only when its subscribed quantity has an unconsumed unit.
  A tenant can assign a product license only when its subscribed quantity has an unconsumed unit. For external-collaboration and SSPR pilot, available license capacity supplies the service rule needed to confirm that the tenant has an unused product unit before assignment.
- **D — Incorrect.** SSPR can target all users or selected groups, subject to tenant licensing and authentication-method policy.
  SSPR can target all users or selected groups, subject to tenant licensing and authentication-method policy. In the external-collaboration and SSPR pilot, this statement describes SSPR registration scope. Available license capacity governs external-collaboration and SSPR pilot; SSPR registration scope cannot support available license capacity when operators must confirm that the tenant has an unused product unit before assignment.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [List subscribed SKUs with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/subscribedsku-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q02 — C

**Question:** The guest collaboration architecture note requires the external-collaboration and SSPR pilot environment to supply the regional attribute required before a cloud license is assigned. Which statement defines the relevant guest collaboration boundary?

- **A — Incorrect.** Direct licensing adds a SKU to one user and can disable selected service plans within that SKU.
  Direct licensing adds a SKU to one user and can disable selected service plans within that SKU. In the external-collaboration and SSPR pilot, this statement describes direct license assignment. The direct license assignment statement accurately describes direct license assignment; however, external-collaboration and SSPR pilot needs usage location prerequisite to supply the regional attribute required before a cloud license is assigned; direct license assignment cannot replace usage location prerequisite.
- **B — Incorrect.** externalUserState changes from PendingAcceptance after the invited guest successfully redeems access.
  externalUserState changes from PendingAcceptance after the invited guest successfully redeems access. In the external-collaboration and SSPR pilot, this statement describes guest redemption state. Selecting guest redemption state for external-collaboration and SSPR pilot leaves usage location prerequisite unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a usage location prerequisite basis to supply the regional attribute required before a cloud license is assigned.
- **C — Correct.** A user's usageLocation must be set before Microsoft Entra can assign many commercial licenses.
  A user's usageLocation must be set before Microsoft Entra can assign many commercial licenses. In the external-collaboration and SSPR pilot, this usage location prerequisite rule supports the need to supply the regional attribute required before a cloud license is assigned.
- **D — Incorrect.** The tenant policy determines how many and which registered methods a user needs for password reset.
  The tenant policy determines how many and which registered methods a user needs for password reset. In the external-collaboration and SSPR pilot, this statement describes SSPR authentication methods. External-collaboration and SSPR pilot asks about usage location prerequisite; this SSPR authentication methods choice leaves the usage location prerequisite explanation missing.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q03 — C

**Question:** A new guest collaboration operator must explain why the external-collaboration and SSPR pilot can license one pilot user without depending on group membership. Which explanation is accurate?

- **A — Incorrect.** Group-based licensing applies assigned product licenses to eligible members of a licensed group.
  Group-based licensing applies assigned product licenses to eligible members of a licensed group. In the external-collaboration and SSPR pilot, this statement describes group-based licensing. Selecting group-based licensing for external-collaboration and SSPR pilot leaves direct license assignment unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a direct license assignment basis to license one pilot user without depending on group membership.
- **B — Incorrect.** A guest remains a tenant directory object whose display name, sponsors, groups, and access require lifecycle governance.
  A guest remains a tenant directory object whose display name, sponsors, groups, and access require lifecycle governance. In the external-collaboration and SSPR pilot, this statement describes guest lifecycle properties. Direct license assignment governs external-collaboration and SSPR pilot; guest lifecycle properties cannot support direct license assignment when operators must license one pilot user without depending on group membership.
- **C — Correct.** Direct licensing adds a SKU to one user and can disable selected service plans within that SKU.
  For the external-collaboration and SSPR pilot, the rule for direct license assignment is defined by this statement: direct licensing adds a SKU to one user and can disable selected service plans within that SKU. It supports the required outcome to license one pilot user without depending on group membership.
- **D — Incorrect.** SSPR capabilities depend on eligible licensing, policy scope, and special rules for administrator accounts.
  SSPR capabilities depend on eligible licensing, policy scope, and special rules for administrator accounts. In the external-collaboration and SSPR pilot, this statement describes SSPR licensing and role gates. The SSPR licensing and role gates statement accurately describes SSPR licensing and role gates; however, external-collaboration and SSPR pilot needs direct license assignment to license one pilot user without depending on group membership; SSPR licensing and role gates cannot replace direct license assignment.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q04 — A

**Question:** The external-collaboration and SSPR pilot acceptance criteria require operators to license a rotating team through membership rather than individual assignments. Which service fact supports that requirement?

- **A — Correct.** Group-based licensing applies assigned product licenses to eligible members of a licensed group.
  Group-based licensing applies assigned product licenses to eligible members of a licensed group. The external-collaboration and SSPR pilot applies that group-based licensing boundary when operators must license a rotating team through membership rather than individual assignments.
- **B — Incorrect.** A B2B invitation creates an external user object and sends or returns a redemption invitation.
  A B2B invitation creates an external user object and sends or returns a redemption invitation. In the external-collaboration and SSPR pilot, this statement describes B2B guest invitations. External-collaboration and SSPR pilot asks about group-based licensing; this B2B guest invitations choice leaves the group-based licensing explanation missing.
- **C — Incorrect.** SSPR can target all users or selected groups, subject to tenant licensing and authentication-method policy.
  SSPR can target all users or selected groups, subject to tenant licensing and authentication-method policy. In the external-collaboration and SSPR pilot, this statement describes SSPR registration scope. The SSPR registration scope statement accurately describes SSPR registration scope; however, external-collaboration and SSPR pilot needs group-based licensing to license a rotating team through membership rather than individual assignments; SSPR registration scope cannot replace group-based licensing.
- **D — Incorrect.** A tenant can assign a product license only when its subscribed quantity has an unconsumed unit.
  A tenant can assign a product license only when its subscribed quantity has an unconsumed unit. In the external-collaboration and SSPR pilot, this statement describes available license capacity. Selecting available license capacity for external-collaboration and SSPR pilot leaves group-based licensing unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a group-based licensing basis to license a rotating team through membership rather than individual assignments.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Group-based licensing fundamentals](https://learn.microsoft.com/en-us/entra/fundamentals/concept-group-based-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q05 — D

**Question:** A guest collaboration reviewer challenges whether the external-collaboration and SSPR pilot can send a redeemable collaboration invitation to an external address. Which response resolves the concern?

- **A — Incorrect.** externalUserState changes from PendingAcceptance after the invited guest successfully redeems access.
  externalUserState changes from PendingAcceptance after the invited guest successfully redeems access. In the external-collaboration and SSPR pilot, this statement describes guest redemption state. External-collaboration and SSPR pilot asks about B2B guest invitations; this guest redemption state choice leaves the B2B guest invitations explanation missing.
- **B — Incorrect.** The tenant policy determines how many and which registered methods a user needs for password reset.
  The tenant policy determines how many and which registered methods a user needs for password reset. In the external-collaboration and SSPR pilot, this statement describes SSPR authentication methods. The SSPR authentication methods statement accurately describes SSPR authentication methods; however, external-collaboration and SSPR pilot needs B2B guest invitations to send a redeemable collaboration invitation to an external address; SSPR authentication methods cannot replace B2B guest invitations.
- **C — Incorrect.** A user's usageLocation must be set before Microsoft Entra can assign many commercial licenses.
  A user's usageLocation must be set before Microsoft Entra can assign many commercial licenses. In the external-collaboration and SSPR pilot, this statement describes usage location prerequisite. Selecting usage location prerequisite for external-collaboration and SSPR pilot leaves B2B guest invitations unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a B2B guest invitations basis to send a redeemable collaboration invitation to an external address.
- **D — Correct.** A B2B invitation creates an external user object and sends or returns a redemption invitation.
  The external-collaboration and SSPR pilot needs B2B guest invitations to send a redeemable collaboration invitation to an external address; this option states the applicable B2B guest invitations rule: a B2B invitation creates an external user object and sends or returns a redemption invitation.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Create a Microsoft Entra B2B invitation](https://learn.microsoft.com/en-us/graph/api/invitation-post?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q06 — A

**Question:** The external-collaboration and SSPR pilot handoff omits the guest collaboration rule needed to distinguish an invited account from one that has accepted its invitation. Which statement should the team add?

- **A — Correct.** externalUserState changes from PendingAcceptance after the invited guest successfully redeems access.
  ExternalUserState changes from PendingAcceptance after the invited guest successfully redeems access. This guest redemption state fact resolves the external-collaboration and SSPR pilot design question about how to distinguish an invited account from one that has accepted its invitation.
- **B — Incorrect.** A guest remains a tenant directory object whose display name, sponsors, groups, and access require lifecycle governance.
  A guest remains a tenant directory object whose display name, sponsors, groups, and access require lifecycle governance. In the external-collaboration and SSPR pilot, this statement describes guest lifecycle properties. Selecting guest lifecycle properties for external-collaboration and SSPR pilot leaves guest redemption state unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a guest redemption state basis to distinguish an invited account from one that has accepted its invitation.
- **C — Incorrect.** SSPR capabilities depend on eligible licensing, policy scope, and special rules for administrator accounts.
  SSPR capabilities depend on eligible licensing, policy scope, and special rules for administrator accounts. In the external-collaboration and SSPR pilot, this statement describes SSPR licensing and role gates. Guest redemption state governs external-collaboration and SSPR pilot; SSPR licensing and role gates cannot support guest redemption state when operators must distinguish an invited account from one that has accepted its invitation.
- **D — Incorrect.** Direct licensing adds a SKU to one user and can disable selected service plans within that SKU.
  Direct licensing adds a SKU to one user and can disable selected service plans within that SKU. In the external-collaboration and SSPR pilot, this statement describes direct license assignment. External-collaboration and SSPR pilot asks about guest redemption state; this direct license assignment choice leaves the guest redemption state explanation missing.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [Microsoft Entra B2B redemption experience](https://learn.microsoft.com/en-us/entra/external-id/redemption-experience)

**Source reviewed:** 2026-08-31

## LAB02-Q07 — D

**Question:** A guest collaboration incident review of the external-collaboration and SSPR pilot depends on the ability to identify external collaborators without relying on their display names. Which platform description is reliable?

- **A — Incorrect.** SSPR can target all users or selected groups, subject to tenant licensing and authentication-method policy.
  SSPR can target all users or selected groups, subject to tenant licensing and authentication-method policy. In the external-collaboration and SSPR pilot, this statement describes SSPR registration scope. Selecting SSPR registration scope for external-collaboration and SSPR pilot leaves guest lifecycle properties unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a guest lifecycle properties basis to identify external collaborators without relying on their display names.
- **B — Incorrect.** A tenant can assign a product license only when its subscribed quantity has an unconsumed unit.
  A tenant can assign a product license only when its subscribed quantity has an unconsumed unit. In the external-collaboration and SSPR pilot, this statement describes available license capacity. Guest lifecycle properties governs external-collaboration and SSPR pilot; available license capacity cannot support guest lifecycle properties when operators must identify external collaborators without relying on their display names.
- **C — Incorrect.** Group-based licensing applies assigned product licenses to eligible members of a licensed group.
  Group-based licensing applies assigned product licenses to eligible members of a licensed group. In the external-collaboration and SSPR pilot, this statement describes group-based licensing. External-collaboration and SSPR pilot asks about guest lifecycle properties; this group-based licensing choice leaves the guest lifecycle properties explanation missing.
- **D — Correct.** A guest remains a tenant directory object whose display name, sponsors, groups, and access require lifecycle governance.
  A guest remains a tenant directory object whose display name, sponsors, groups, and access require lifecycle governance. For external-collaboration and SSPR pilot, guest lifecycle properties supplies the service rule needed to identify external collaborators without relying on their display names.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Properties of a Microsoft Entra B2B collaboration user](https://learn.microsoft.com/en-us/entra/external-id/user-properties)

**Source reviewed:** 2026-08-31

## LAB02-Q08 — C

**Question:** An identity administrator preparing a controlled external-collaboration and SSPR pilot is updating the guest collaboration runbook. The requirement is to limit password-reset registration to the approved pilot population. Which statement describes Azure behavior correctly?

- **A — Incorrect.** The tenant policy determines how many and which registered methods a user needs for password reset.
  The tenant policy determines how many and which registered methods a user needs for password reset. In the external-collaboration and SSPR pilot, this statement describes SSPR authentication methods. SSPR registration scope governs external-collaboration and SSPR pilot; SSPR authentication methods cannot support SSPR registration scope when operators must limit password-reset registration to the approved pilot population.
- **B — Incorrect.** A user's usageLocation must be set before Microsoft Entra can assign many commercial licenses.
  A user's usageLocation must be set before Microsoft Entra can assign many commercial licenses. In the external-collaboration and SSPR pilot, this statement describes usage location prerequisite. External-collaboration and SSPR pilot asks about SSPR registration scope; this usage location prerequisite choice leaves the SSPR registration scope explanation missing.
- **C — Correct.** SSPR can target all users or selected groups, subject to tenant licensing and authentication-method policy.
  SSPR can target all users or selected groups, subject to tenant licensing and authentication-method policy. In the external-collaboration and SSPR pilot, this SSPR registration scope rule supports the need to limit password-reset registration to the approved pilot population.
- **D — Incorrect.** A B2B invitation creates an external user object and sends or returns a redemption invitation.
  A B2B invitation creates an external user object and sends or returns a redemption invitation. In the external-collaboration and SSPR pilot, this statement describes B2B guest invitations. Selecting B2B guest invitations for external-collaboration and SSPR pilot leaves SSPR registration scope unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a SSPR registration scope basis to limit password-reset registration to the approved pilot population.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [How Microsoft Entra self-service password reset works](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks)

**Source reviewed:** 2026-08-31

## LAB02-Q09 — A

**Question:** A guest collaboration peer review asks how the external-collaboration and SSPR pilot should handle this outcome: allow only the approved proofs during password reset. Which explanation is accurate?

- **A — Correct.** The tenant policy determines how many and which registered methods a user needs for password reset.
  For the external-collaboration and SSPR pilot, the rule for SSPR authentication methods is defined by this statement: the tenant policy determines how many and which registered methods a user needs for password reset. It supports the required outcome to allow only the approved proofs during password reset.
- **B — Incorrect.** SSPR capabilities depend on eligible licensing, policy scope, and special rules for administrator accounts.
  SSPR capabilities depend on eligible licensing, policy scope, and special rules for administrator accounts. In the external-collaboration and SSPR pilot, this statement describes SSPR licensing and role gates. The SSPR licensing and role gates statement accurately describes SSPR licensing and role gates; however, external-collaboration and SSPR pilot needs SSPR authentication methods to allow only the approved proofs during password reset; SSPR licensing and role gates cannot replace SSPR authentication methods.
- **C — Incorrect.** Direct licensing adds a SKU to one user and can disable selected service plans within that SKU.
  Direct licensing adds a SKU to one user and can disable selected service plans within that SKU. In the external-collaboration and SSPR pilot, this statement describes direct license assignment. Selecting direct license assignment for external-collaboration and SSPR pilot leaves SSPR authentication methods unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a SSPR authentication methods basis to allow only the approved proofs during password reset.
- **D — Incorrect.** externalUserState changes from PendingAcceptance after the invited guest successfully redeems access.
  externalUserState changes from PendingAcceptance after the invited guest successfully redeems access. In the external-collaboration and SSPR pilot, this statement describes guest redemption state. SSPR authentication methods governs external-collaboration and SSPR pilot; guest redemption state cannot support SSPR authentication methods when operators must allow only the approved proofs during password reset.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Authentication methods for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods)

**Source reviewed:** 2026-08-31

## LAB02-Q10 — D

**Question:** For the external-collaboration and SSPR pilot, the guest collaboration plan must stop safely when the tenant lacks the entitlement or role needed for reset changes. Which statement about guest collaboration belongs in the external-collaboration and SSPR pilot record?

- **A — Incorrect.** A tenant can assign a product license only when its subscribed quantity has an unconsumed unit.
  A tenant can assign a product license only when its subscribed quantity has an unconsumed unit. In the external-collaboration and SSPR pilot, this statement describes available license capacity. The available license capacity statement accurately describes available license capacity; however, external-collaboration and SSPR pilot needs SSPR licensing and role gates to stop safely when the tenant lacks the entitlement or role needed for reset changes; available license capacity cannot replace SSPR licensing and role gates.
- **B — Incorrect.** Group-based licensing applies assigned product licenses to eligible members of a licensed group.
  Group-based licensing applies assigned product licenses to eligible members of a licensed group. In the external-collaboration and SSPR pilot, this statement describes group-based licensing. Selecting group-based licensing for external-collaboration and SSPR pilot leaves SSPR licensing and role gates unanswered in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot lacks a SSPR licensing and role gates basis to stop safely when the tenant lacks the entitlement or role needed for reset changes.
- **C — Incorrect.** A guest remains a tenant directory object whose display name, sponsors, groups, and access require lifecycle governance.
  A guest remains a tenant directory object whose display name, sponsors, groups, and access require lifecycle governance. In the external-collaboration and SSPR pilot, this statement describes guest lifecycle properties. SSPR licensing and role gates governs external-collaboration and SSPR pilot; guest lifecycle properties cannot support SSPR licensing and role gates when operators must stop safely when the tenant lacks the entitlement or role needed for reset changes.
- **D — Correct.** SSPR capabilities depend on eligible licensing, policy scope, and special rules for administrator accounts.
  SSPR capabilities depend on eligible licensing, policy scope, and special rules for administrator accounts. The external-collaboration and SSPR pilot applies that SSPR licensing and role gates boundary when operators must stop safely when the tenant lacks the entitlement or role needed for reset changes.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Licensing requirements for Microsoft Entra self-service password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q11 — D

**Question:** A guest collaboration dry run shows no external-collaboration and SSPR pilot command will confirm that the tenant has an unused product unit before assignment. Which action belongs before execution?

- **A — Incorrect.** Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs.
  Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. In the external-collaboration and SSPR pilot, this action changes direct license assignment. External-collaboration and SSPR pilot approved available license capacity, not direct license assignment; only the available license capacity change can confirm that the tenant has an unused product unit before assignment.
- **B — Incorrect.** Track the guest by object ID and wait for redemption before depending on interactive access.
  Track the guest by object ID and wait for redemption before depending on interactive access. In the external-collaboration and SSPR pilot, this action changes guest redemption state. External-collaboration and SSPR pilot requires available license capacity; changing guest redemption state leaves available license capacity absent in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot cannot confirm that the tenant has an unused product unit before assignment.
- **C — Incorrect.** Configure permitted reset methods and require users to register enough approved methods.
  Configure permitted reset methods and require users to register enough approved methods. In the external-collaboration and SSPR pilot, this action changes SSPR authentication methods. SSPR authentication methods does not implement available license capacity for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot confirm that the tenant has an unused product unit before assignment.
- **D — Correct.** Read subscribedSkus and calculate enabled units minus consumed units before assigning a license.
  The external-collaboration and SSPR pilot must confirm that the tenant has an unused product unit before assignment; this option performs its direct available license capacity change: read subscribedSkus and calculate enabled units minus consumed units before assigning a license.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [List subscribed SKUs with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/subscribedsku-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q12 — B

**Question:** For the external-collaboration and SSPR pilot, operators need to supply the regional attribute required before a cloud license is assigned. Which change realizes that requirement?

- **A — Incorrect.** Assign the SKU to the licensing group and add eligible users as members.
  Assign the SKU to the licensing group and add eligible users as members. In the external-collaboration and SSPR pilot, this action changes group-based licensing. External-collaboration and SSPR pilot requires usage location prerequisite; changing group-based licensing leaves usage location prerequisite absent in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot cannot supply the regional attribute required before a cloud license is assigned.
- **B — Correct.** Set the user's two-letter usage location before submitting the license assignment.
  Set the user's two-letter usage location before submitting the license assignment. It is the least-change usage location prerequisite path for the external-collaboration and SSPR pilot requirement to supply the regional attribute required before a cloud license is assigned.
- **C — Incorrect.** Record the guest object ID and assign only the groups needed for the collaboration period.
  Record the guest object ID and assign only the groups needed for the collaboration period. In the external-collaboration and SSPR pilot, this action changes guest lifecycle properties. External-collaboration and SSPR pilot instead needs usage location prerequisite: Set the user's two-letter usage location before submitting the license assignment. The guest lifecycle properties action omits that usage location prerequisite work.
- **D — Incorrect.** Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path.
  Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. In the external-collaboration and SSPR pilot, this action changes SSPR licensing and role gates. External-collaboration and SSPR pilot approved usage location prerequisite, not SSPR licensing and role gates; only the usage location prerequisite change can supply the regional attribute required before a cloud license is assigned.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q13 — B

**Question:** Operators must automate the external-collaboration and SSPR pilot change needed to license one pilot user without depending on group membership. Which guest collaboration operation belongs in the runbook?

- **A — Incorrect.** Create an invitation with the guest email address and an approved redirect URL.
  Create an invitation with the guest email address and an approved redirect URL. In the external-collaboration and SSPR pilot, this action changes B2B guest invitations. B2B guest invitations does not implement direct license assignment for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot license one pilot user without depending on group membership.
- **B — Correct.** Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs.
  Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. In external-collaboration and SSPR pilot, applying direct license assignment is the scoped way to license one pilot user without depending on group membership.
- **C — Incorrect.** Enable SSPR for the approved pilot group before broadening the scope.
  Enable SSPR for the approved pilot group before broadening the scope. In the external-collaboration and SSPR pilot, this action changes SSPR registration scope. External-collaboration and SSPR pilot approved direct license assignment, not SSPR registration scope; only the direct license assignment change can license one pilot user without depending on group membership.
- **D — Incorrect.** Read subscribedSkus and calculate enabled units minus consumed units before assigning a license.
  Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. In the external-collaboration and SSPR pilot, this action changes available license capacity. External-collaboration and SSPR pilot requires direct license assignment; changing available license capacity leaves direct license assignment absent in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot cannot license one pilot user without depending on group membership.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q14 — C

**Question:** An external-collaboration and SSPR pilot review finds guest collaboration drift from the need to license a rotating team through membership rather than individual assignments. Which correction addresses that drift?

- **A — Incorrect.** Track the guest by object ID and wait for redemption before depending on interactive access.
  Track the guest by object ID and wait for redemption before depending on interactive access. In the external-collaboration and SSPR pilot, this action changes guest redemption state. External-collaboration and SSPR pilot instead needs group-based licensing: Assign the SKU to the licensing group and add eligible users as members. The guest redemption state action omits that group-based licensing work.
- **B — Incorrect.** Configure permitted reset methods and require users to register enough approved methods.
  Configure permitted reset methods and require users to register enough approved methods. In the external-collaboration and SSPR pilot, this action changes SSPR authentication methods. External-collaboration and SSPR pilot approved group-based licensing, not SSPR authentication methods; only the group-based licensing change can license a rotating team through membership rather than individual assignments.
- **C — Correct.** Assign the SKU to the licensing group and add eligible users as members.
  Assign the SKU to the licensing group and add eligible users as members. The external-collaboration and SSPR pilot uses this group-based licensing operation to license a rotating team through membership rather than individual assignments within the approved scope.
- **D — Incorrect.** Set the user's two-letter usage location before submitting the license assignment.
  Set the user's two-letter usage location before submitting the license assignment. In the external-collaboration and SSPR pilot, this action changes usage location prerequisite. Usage location prerequisite does not implement group-based licensing for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot license a rotating team through membership rather than individual assignments.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Group-based licensing fundamentals](https://learn.microsoft.com/en-us/entra/fundamentals/concept-group-based-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q15 — D

**Question:** The external-collaboration and SSPR pilot window permits only the guest collaboration change needed to send a redeemable collaboration invitation to an external address. Which option respects the boundary?

- **A — Incorrect.** Record the guest object ID and assign only the groups needed for the collaboration period.
  Record the guest object ID and assign only the groups needed for the collaboration period. In the external-collaboration and SSPR pilot, this action changes guest lifecycle properties. External-collaboration and SSPR pilot approved B2B guest invitations, not guest lifecycle properties; only the B2B guest invitations change can send a redeemable collaboration invitation to an external address.
- **B — Incorrect.** Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path.
  Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. In the external-collaboration and SSPR pilot, this action changes SSPR licensing and role gates. External-collaboration and SSPR pilot requires B2B guest invitations; changing SSPR licensing and role gates leaves B2B guest invitations absent in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot cannot send a redeemable collaboration invitation to an external address.
- **C — Incorrect.** Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs.
  Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. In the external-collaboration and SSPR pilot, this action changes direct license assignment. Direct license assignment does not implement B2B guest invitations for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot send a redeemable collaboration invitation to an external address.
- **D — Correct.** Create an invitation with the guest email address and an approved redirect URL.
  For the external-collaboration and SSPR pilot, the required B2B guest invitations action is: create an invitation with the guest email address and an approved redirect URL. It makes the environment able to send a redeemable collaboration invitation to an external address.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Create a Microsoft Entra B2B invitation](https://learn.microsoft.com/en-us/graph/api/invitation-post?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q16 — D

**Question:** The guest collaboration preflight has passed; the external-collaboration and SSPR pilot must now distinguish an invited account from one that has accepted its invitation. Which operation should run?

- **A — Incorrect.** Enable SSPR for the approved pilot group before broadening the scope.
  Enable SSPR for the approved pilot group before broadening the scope. In the external-collaboration and SSPR pilot, this action changes SSPR registration scope. External-collaboration and SSPR pilot requires guest redemption state; changing SSPR registration scope leaves guest redemption state absent in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot cannot distinguish an invited account from one that has accepted its invitation.
- **B — Incorrect.** Read subscribedSkus and calculate enabled units minus consumed units before assigning a license.
  Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. In the external-collaboration and SSPR pilot, this action changes available license capacity. Available license capacity does not implement guest redemption state for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot distinguish an invited account from one that has accepted its invitation.
- **C — Incorrect.** Assign the SKU to the licensing group and add eligible users as members.
  Assign the SKU to the licensing group and add eligible users as members. In the external-collaboration and SSPR pilot, this action changes group-based licensing. External-collaboration and SSPR pilot instead needs guest redemption state: Track the guest by object ID and wait for redemption before depending on interactive access. The group-based licensing action omits that guest redemption state work.
- **D — Correct.** Track the guest by object ID and wait for redemption before depending on interactive access.
  Track the guest by object ID and wait for redemption before depending on interactive access. This changes guest redemption state in the external-collaboration and SSPR pilot, supplying the missing state needed to distinguish an invited account from one that has accepted its invitation.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [Microsoft Entra B2B redemption experience](https://learn.microsoft.com/en-us/entra/external-id/redemption-experience)

**Source reviewed:** 2026-08-31

## LAB02-Q17 — D

**Question:** The external-collaboration and SSPR pilot plan must identify external collaborators without relying on their display names while limiting the mutation scope to guest collaboration. Which action is appropriate?

- **A — Incorrect.** Configure permitted reset methods and require users to register enough approved methods.
  Configure permitted reset methods and require users to register enough approved methods. In the external-collaboration and SSPR pilot, this action changes SSPR authentication methods. SSPR authentication methods does not implement guest lifecycle properties for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot identify external collaborators without relying on their display names.
- **B — Incorrect.** Set the user's two-letter usage location before submitting the license assignment.
  Set the user's two-letter usage location before submitting the license assignment. In the external-collaboration and SSPR pilot, this action changes usage location prerequisite. External-collaboration and SSPR pilot instead needs guest lifecycle properties: Record the guest object ID and assign only the groups needed for the collaboration period. The usage location prerequisite action omits that guest lifecycle properties work.
- **C — Incorrect.** Create an invitation with the guest email address and an approved redirect URL.
  Create an invitation with the guest email address and an approved redirect URL. In the external-collaboration and SSPR pilot, this action changes B2B guest invitations. External-collaboration and SSPR pilot approved guest lifecycle properties, not B2B guest invitations; only the guest lifecycle properties change can identify external collaborators without relying on their display names.
- **D — Correct.** Record the guest object ID and assign only the groups needed for the collaboration period.
  The external-collaboration and SSPR pilot must identify external collaborators without relying on their display names; this option performs its direct guest lifecycle properties change: record the guest object ID and assign only the groups needed for the collaboration period.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Properties of a Microsoft Entra B2B collaboration user](https://learn.microsoft.com/en-us/entra/external-id/user-properties)

**Source reviewed:** 2026-08-31

## LAB02-Q18 — A

**Question:** A guest collaboration ticket in the external-collaboration and SSPR pilot says to limit password-reset registration to the approved pilot population. Which guest collaboration action completes the external-collaboration and SSPR pilot request with minimal change?

- **A — Correct.** Enable SSPR for the approved pilot group before broadening the scope.
  Enable SSPR for the approved pilot group before broadening the scope. It is the least-change SSPR registration scope path for the external-collaboration and SSPR pilot requirement to limit password-reset registration to the approved pilot population.
- **B — Incorrect.** Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path.
  Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. In the external-collaboration and SSPR pilot, this action changes SSPR licensing and role gates. External-collaboration and SSPR pilot approved SSPR registration scope, not SSPR licensing and role gates; only the SSPR registration scope change can limit password-reset registration to the approved pilot population.
- **C — Incorrect.** Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs.
  Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. In the external-collaboration and SSPR pilot, this action changes direct license assignment. External-collaboration and SSPR pilot requires SSPR registration scope; changing direct license assignment leaves SSPR registration scope absent in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot cannot limit password-reset registration to the approved pilot population.
- **D — Incorrect.** Track the guest by object ID and wait for redemption before depending on interactive access.
  Track the guest by object ID and wait for redemption before depending on interactive access. In the external-collaboration and SSPR pilot, this action changes guest redemption state. Guest redemption state does not implement SSPR registration scope for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot limit password-reset registration to the approved pilot population.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [How Microsoft Entra self-service password reset works](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks)

**Source reviewed:** 2026-08-31

## LAB02-Q19 — A

**Question:** The approach for the external-collaboration and SSPR pilot is approved, but the guest collaboration environment still cannot allow only the approved proofs during password reset. Which implementation step closes the gap?

- **A — Correct.** Configure permitted reset methods and require users to register enough approved methods.
  Configure permitted reset methods and require users to register enough approved methods. In external-collaboration and SSPR pilot, applying SSPR authentication methods is the scoped way to allow only the approved proofs during password reset.
- **B — Incorrect.** Read subscribedSkus and calculate enabled units minus consumed units before assigning a license.
  Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. In the external-collaboration and SSPR pilot, this action changes available license capacity. External-collaboration and SSPR pilot requires SSPR authentication methods; changing available license capacity leaves SSPR authentication methods absent in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot cannot allow only the approved proofs during password reset.
- **C — Incorrect.** Assign the SKU to the licensing group and add eligible users as members.
  Assign the SKU to the licensing group and add eligible users as members. In the external-collaboration and SSPR pilot, this action changes group-based licensing. Group-based licensing does not implement SSPR authentication methods for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot allow only the approved proofs during password reset.
- **D — Incorrect.** Record the guest object ID and assign only the groups needed for the collaboration period.
  Record the guest object ID and assign only the groups needed for the collaboration period. In the external-collaboration and SSPR pilot, this action changes guest lifecycle properties. External-collaboration and SSPR pilot instead needs SSPR authentication methods: Configure permitted reset methods and require users to register enough approved methods. The guest lifecycle properties action omits that SSPR authentication methods work.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Authentication methods for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods)

**Source reviewed:** 2026-08-31

## LAB02-Q20 — A

**Question:** The identity administrator preparing a controlled external-collaboration and SSPR pilot may change the external-collaboration and SSPR pilot only to stop safely when the tenant lacks the entitlement or role needed for reset changes. Which guest collaboration action stays within that assignment?

- **A — Correct.** Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path.
  Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. The external-collaboration and SSPR pilot uses this SSPR licensing and role gates operation to stop safely when the tenant lacks the entitlement or role needed for reset changes within the approved scope.
- **B — Incorrect.** Set the user's two-letter usage location before submitting the license assignment.
  Set the user's two-letter usage location before submitting the license assignment. In the external-collaboration and SSPR pilot, this action changes usage location prerequisite. Usage location prerequisite does not implement SSPR licensing and role gates for external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot still cannot stop safely when the tenant lacks the entitlement or role needed for reset changes.
- **C — Incorrect.** Create an invitation with the guest email address and an approved redirect URL.
  Create an invitation with the guest email address and an approved redirect URL. In the external-collaboration and SSPR pilot, this action changes B2B guest invitations. External-collaboration and SSPR pilot instead needs SSPR licensing and role gates: Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. The B2B guest invitations action omits that SSPR licensing and role gates work.
- **D — Incorrect.** Enable SSPR for the approved pilot group before broadening the scope.
  Enable SSPR for the approved pilot group before broadening the scope. In the external-collaboration and SSPR pilot, this action changes SSPR registration scope. External-collaboration and SSPR pilot approved SSPR licensing and role gates, not SSPR registration scope; only the SSPR licensing and role gates change can stop safely when the tenant lacks the entitlement or role needed for reset changes.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Licensing requirements for Microsoft Entra self-service password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q21 — B

**Question:** The guest collaboration validator needs one external-collaboration and SSPR pilot query after the change to confirm that the tenant has an unused product unit before assignment. Which guest collaboration property should the external-collaboration and SSPR pilot validator inspect?

- **A — Incorrect.** Inspect the user's inherited assignment state and confirm the assigning group ID.
  Inspect the user's inherited assignment state and confirm the assigning group ID. In the external-collaboration and SSPR pilot, this check observes group-based licensing. External-collaboration and SSPR pilot output covers group-based licensing, not available license capacity; the available license capacity requirement to confirm that the tenant has an unused product unit before assignment remains unverified.
- **B — Correct.** Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
  For the external-collaboration and SSPR pilot, this available license capacity observation is decisive: query the selected SKU and confirm that available units remain greater than or equal to the requested assignments. It is external-collaboration and SSPR pilot evidence that operators can confirm that the tenant has an unused product unit before assignment.
- **C — Incorrect.** Review userType, group memberships, and sign-in state for the exact guest object.
  Review userType, group memberships, and sign-in state for the exact guest object. In the external-collaboration and SSPR pilot, this check observes guest lifecycle properties. External-collaboration and SSPR pilot reads guest lifecycle properties, leaving available license capacity unproved in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot still has no available license capacity proof.
- **D — Incorrect.** Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.
  Confirm the pilot's license assignment, scope membership, and registered methods as separate checks. In the external-collaboration and SSPR pilot, this check observes SSPR licensing and role gates. External-collaboration and SSPR pilot could pass SSPR licensing and role gates while available license capacity is wrong; external-collaboration and SSPR pilot still lacks available license capacity proof.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [List subscribed SKUs with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/subscribedsku-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q22 — A

**Question:** The identity administrator preparing a controlled external-collaboration and SSPR pilot must confirm the external-collaboration and SSPR pilot, without mutation, can supply the regional attribute required before a cloud license is assigned. Which guest collaboration check qualifies?

- **A — Correct.** Read usageLocation for the target object and confirm it is a valid country or region code.
  Read usageLocation for the target object and confirm it is a valid country or region code. Because the external-collaboration and SSPR pilot check observes usage location prerequisite, it independently verifies the requirement to supply the regional attribute required before a cloud license is assigned.
- **B — Incorrect.** Read the invited user's userType and externalUserState from the returned invitedUser ID.
  Read the invited user's userType and externalUserState from the returned invitedUser ID. In the external-collaboration and SSPR pilot, this check observes B2B guest invitations. External-collaboration and SSPR pilot reads B2B guest invitations, leaving usage location prerequisite unproved in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot still has no usage location prerequisite proof.
- **C — Incorrect.** Read the authorization policy and target-group configuration through Microsoft Graph.
  Read the authorization policy and target-group configuration through Microsoft Graph. In the external-collaboration and SSPR pilot, this check observes SSPR registration scope. External-collaboration and SSPR pilot could pass SSPR registration scope while usage location prerequisite is wrong; external-collaboration and SSPR pilot still lacks usage location prerequisite proof.
- **D — Incorrect.** Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
  Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments. In the external-collaboration and SSPR pilot, this check observes available license capacity. External-collaboration and SSPR pilot output covers available license capacity, not usage location prerequisite; the usage location prerequisite requirement to supply the regional attribute required before a cloud license is assigned remains unverified.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q23 — A

**Question:** The external-collaboration and SSPR pilot configuration is complete; the guest collaboration reviewers need evidence it can license one pilot user without depending on group membership. Which observation shows success?

- **A — Correct.** Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
  The external-collaboration and SSPR pilot validator needs this direct license assignment result: read licenseAssignmentStates and confirm the intended SKU is assigned without an error state. It proves the outcome to license one pilot user without depending on group membership rather than an adjacent checkpoint.
- **B — Incorrect.** Query externalUserState and its change timestamp for the invited user.
  Query externalUserState and its change timestamp for the invited user. In the external-collaboration and SSPR pilot, this check observes guest redemption state. External-collaboration and SSPR pilot could pass guest redemption state while direct license assignment is wrong; external-collaboration and SSPR pilot still lacks direct license assignment proof.
- **C — Incorrect.** Compare the user's registered authentication methods with the tenant's SSPR method requirements.
  Compare the user's registered authentication methods with the tenant's SSPR method requirements. In the external-collaboration and SSPR pilot, this check observes SSPR authentication methods. External-collaboration and SSPR pilot output covers SSPR authentication methods, not direct license assignment; the direct license assignment requirement to license one pilot user without depending on group membership remains unverified.
- **D — Incorrect.** Read usageLocation for the target object and confirm it is a valid country or region code.
  Read usageLocation for the target object and confirm it is a valid country or region code. In the external-collaboration and SSPR pilot, this check observes usage location prerequisite. Usage location prerequisite success in external-collaboration and SSPR pilot cannot verify direct license assignment; external-collaboration and SSPR pilot cannot license one pilot user without depending on group membership until direct license assignment evidence exists.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q24 — D

**Question:** The guest collaboration validation asks whether the external-collaboration and SSPR pilot can license a rotating team through membership rather than individual assignments. Which observable state is strongest?

- **A — Incorrect.** Review userType, group memberships, and sign-in state for the exact guest object.
  Review userType, group memberships, and sign-in state for the exact guest object. In the external-collaboration and SSPR pilot, this check observes guest lifecycle properties. External-collaboration and SSPR pilot could pass guest lifecycle properties while group-based licensing is wrong; external-collaboration and SSPR pilot still lacks group-based licensing proof.
- **B — Incorrect.** Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.
  Confirm the pilot's license assignment, scope membership, and registered methods as separate checks. In the external-collaboration and SSPR pilot, this check observes SSPR licensing and role gates. External-collaboration and SSPR pilot output covers SSPR licensing and role gates, not group-based licensing; the group-based licensing requirement to license a rotating team through membership rather than individual assignments remains unverified.
- **C — Incorrect.** Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
  Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state. In the external-collaboration and SSPR pilot, this check observes direct license assignment. Direct license assignment success in external-collaboration and SSPR pilot cannot verify group-based licensing; external-collaboration and SSPR pilot cannot license a rotating team through membership rather than individual assignments until group-based licensing evidence exists.
- **D — Correct.** Inspect the user's inherited assignment state and confirm the assigning group ID.
  Inspect the user's inherited assignment state and confirm the assigning group ID. This is independent group-based licensing evidence for the external-collaboration and SSPR pilot, even if external-collaboration and SSPR pilot setup reports success before group-based licensing becomes observable.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Group-based licensing fundamentals](https://learn.microsoft.com/en-us/entra/fundamentals/concept-group-based-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q25 — D

**Question:** An external-collaboration and SSPR pilot review must prove the guest collaboration ability to send a redeemable collaboration invitation to an external address. Which check avoids an adjacent feature?

- **A — Incorrect.** Read the authorization policy and target-group configuration through Microsoft Graph.
  Read the authorization policy and target-group configuration through Microsoft Graph. In the external-collaboration and SSPR pilot, this check observes SSPR registration scope. External-collaboration and SSPR pilot output covers SSPR registration scope, not B2B guest invitations; the B2B guest invitations requirement to send a redeemable collaboration invitation to an external address remains unverified.
- **B — Incorrect.** Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
  Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments. In the external-collaboration and SSPR pilot, this check observes available license capacity. Available license capacity success in external-collaboration and SSPR pilot cannot verify B2B guest invitations; external-collaboration and SSPR pilot cannot send a redeemable collaboration invitation to an external address until B2B guest invitations evidence exists.
- **C — Incorrect.** Inspect the user's inherited assignment state and confirm the assigning group ID.
  Inspect the user's inherited assignment state and confirm the assigning group ID. In the external-collaboration and SSPR pilot, this check observes group-based licensing. External-collaboration and SSPR pilot reads group-based licensing, leaving B2B guest invitations unproved in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot still has no B2B guest invitations proof.
- **D — Correct.** Read the invited user's userType and externalUserState from the returned invitedUser ID.
  Read the invited user's userType and externalUserState from the returned invitedUser ID. For external-collaboration and SSPR pilot, this B2B guest invitations read confirms the service can send a redeemable collaboration invitation to an external address.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Create a Microsoft Entra B2B invitation](https://learn.microsoft.com/en-us/graph/api/invitation-post?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q26 — B

**Question:** The external-collaboration and SSPR pilot evidence bundle needs a guest collaboration result showing it can distinguish an invited account from one that has accepted its invitation. Which result belongs in the checkpoint?

- **A — Incorrect.** Compare the user's registered authentication methods with the tenant's SSPR method requirements.
  Compare the user's registered authentication methods with the tenant's SSPR method requirements. In the external-collaboration and SSPR pilot, this check observes SSPR authentication methods. SSPR authentication methods success in external-collaboration and SSPR pilot cannot verify guest redemption state; external-collaboration and SSPR pilot cannot distinguish an invited account from one that has accepted its invitation until guest redemption state evidence exists.
- **B — Correct.** Query externalUserState and its change timestamp for the invited user.
  Query externalUserState and its change timestamp for the invited user. The external-collaboration and SSPR pilot reads guest redemption state directly; that guest redemption state result proves the external-collaboration and SSPR pilot can distinguish an invited account from one that has accepted its invitation without another mutation.
- **C — Incorrect.** Read usageLocation for the target object and confirm it is a valid country or region code.
  Read usageLocation for the target object and confirm it is a valid country or region code. In the external-collaboration and SSPR pilot, this check observes usage location prerequisite. External-collaboration and SSPR pilot could pass usage location prerequisite while guest redemption state is wrong; external-collaboration and SSPR pilot still lacks guest redemption state proof.
- **D — Incorrect.** Read the invited user's userType and externalUserState from the returned invitedUser ID.
  Read the invited user's userType and externalUserState from the returned invitedUser ID. In the external-collaboration and SSPR pilot, this check observes B2B guest invitations. External-collaboration and SSPR pilot output covers B2B guest invitations, not guest redemption state; the guest redemption state requirement to distinguish an invited account from one that has accepted its invitation remains unverified.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [Microsoft Entra B2B redemption experience](https://learn.microsoft.com/en-us/entra/external-id/redemption-experience)

**Source reviewed:** 2026-08-31

## LAB02-Q27 — A

**Question:** Before external-collaboration and SSPR pilot cleanup, the guest collaboration team must reconfirm it can identify external collaborators without relying on their display names. Which read-only inspection should run?

- **A — Correct.** Review userType, group memberships, and sign-in state for the exact guest object.
  For the external-collaboration and SSPR pilot, this guest lifecycle properties observation is decisive: review userType, group memberships, and sign-in state for the exact guest object. It is external-collaboration and SSPR pilot evidence that operators can identify external collaborators without relying on their display names.
- **B — Incorrect.** Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.
  Confirm the pilot's license assignment, scope membership, and registered methods as separate checks. In the external-collaboration and SSPR pilot, this check observes SSPR licensing and role gates. External-collaboration and SSPR pilot could pass SSPR licensing and role gates while guest lifecycle properties is wrong; external-collaboration and SSPR pilot still lacks guest lifecycle properties proof.
- **C — Incorrect.** Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
  Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state. In the external-collaboration and SSPR pilot, this check observes direct license assignment. External-collaboration and SSPR pilot output covers direct license assignment, not guest lifecycle properties; the guest lifecycle properties requirement to identify external collaborators without relying on their display names remains unverified.
- **D — Incorrect.** Query externalUserState and its change timestamp for the invited user.
  Query externalUserState and its change timestamp for the invited user. In the external-collaboration and SSPR pilot, this check observes guest redemption state. Guest redemption state success in external-collaboration and SSPR pilot cannot verify guest lifecycle properties; external-collaboration and SSPR pilot cannot identify external collaborators without relying on their display names until guest lifecycle properties evidence exists.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Properties of a Microsoft Entra B2B collaboration user](https://learn.microsoft.com/en-us/entra/external-id/user-properties)

**Source reviewed:** 2026-08-31

## LAB02-Q28 — C

**Question:** The external-collaboration and SSPR pilot setup reports success after the guest collaboration attempt to limit password-reset registration to the approved pilot population. Which guest collaboration read-only observation proves the external-collaboration and SSPR pilot outcome?

- **A — Incorrect.** Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
  Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments. In the external-collaboration and SSPR pilot, this check observes available license capacity. External-collaboration and SSPR pilot could pass available license capacity while SSPR registration scope is wrong; external-collaboration and SSPR pilot still lacks SSPR registration scope proof.
- **B — Incorrect.** Inspect the user's inherited assignment state and confirm the assigning group ID.
  Inspect the user's inherited assignment state and confirm the assigning group ID. In the external-collaboration and SSPR pilot, this check observes group-based licensing. External-collaboration and SSPR pilot output covers group-based licensing, not SSPR registration scope; the SSPR registration scope requirement to limit password-reset registration to the approved pilot population remains unverified.
- **C — Correct.** Read the authorization policy and target-group configuration through Microsoft Graph.
  Read the authorization policy and target-group configuration through Microsoft Graph. Because the external-collaboration and SSPR pilot check observes SSPR registration scope, it independently verifies the requirement to limit password-reset registration to the approved pilot population.
- **D — Incorrect.** Review userType, group memberships, and sign-in state for the exact guest object.
  Review userType, group memberships, and sign-in state for the exact guest object. In the external-collaboration and SSPR pilot, this check observes guest lifecycle properties. External-collaboration and SSPR pilot reads guest lifecycle properties, leaving SSPR registration scope unproved in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot still has no SSPR registration scope proof.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [How Microsoft Entra self-service password reset works](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks)

**Source reviewed:** 2026-08-31

## LAB02-Q29 — B

**Question:** The guest collaboration log says the external-collaboration and SSPR pilot can now allow only the approved proofs during password reset. Which guest collaboration state should the external-collaboration and SSPR pilot acceptance test retain?

- **A — Incorrect.** Read usageLocation for the target object and confirm it is a valid country or region code.
  Read usageLocation for the target object and confirm it is a valid country or region code. In the external-collaboration and SSPR pilot, this check observes usage location prerequisite. External-collaboration and SSPR pilot output covers usage location prerequisite, not SSPR authentication methods; the SSPR authentication methods requirement to allow only the approved proofs during password reset remains unverified.
- **B — Correct.** Compare the user's registered authentication methods with the tenant's SSPR method requirements.
  The external-collaboration and SSPR pilot validator needs this SSPR authentication methods result: compare the user's registered authentication methods with the tenant's SSPR method requirements. It proves the outcome to allow only the approved proofs during password reset rather than an adjacent checkpoint.
- **C — Incorrect.** Read the invited user's userType and externalUserState from the returned invitedUser ID.
  Read the invited user's userType and externalUserState from the returned invitedUser ID. In the external-collaboration and SSPR pilot, this check observes B2B guest invitations. External-collaboration and SSPR pilot reads B2B guest invitations, leaving SSPR authentication methods unproved in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot still has no SSPR authentication methods proof.
- **D — Incorrect.** Read the authorization policy and target-group configuration through Microsoft Graph.
  Read the authorization policy and target-group configuration through Microsoft Graph. In the external-collaboration and SSPR pilot, this check observes SSPR registration scope. External-collaboration and SSPR pilot could pass SSPR registration scope while SSPR authentication methods is wrong; external-collaboration and SSPR pilot still lacks SSPR authentication methods proof.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Authentication methods for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods)

**Source reviewed:** 2026-08-31

## LAB02-Q30 — D

**Question:** The external-collaboration and SSPR pilot rejects guest collaboration exit status as proof it can stop safely when the tenant lacks the entitlement or role needed for reset changes. Which external-collaboration and SSPR pilot result is valid evidence?

- **A — Incorrect.** Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
  Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state. In the external-collaboration and SSPR pilot, this check observes direct license assignment. Direct license assignment success in external-collaboration and SSPR pilot cannot verify SSPR licensing and role gates; external-collaboration and SSPR pilot cannot stop safely when the tenant lacks the entitlement or role needed for reset changes until SSPR licensing and role gates evidence exists.
- **B — Incorrect.** Query externalUserState and its change timestamp for the invited user.
  Query externalUserState and its change timestamp for the invited user. In the external-collaboration and SSPR pilot, this check observes guest redemption state. External-collaboration and SSPR pilot reads guest redemption state, leaving SSPR licensing and role gates unproved in external-collaboration and SSPR pilot; external-collaboration and SSPR pilot still has no SSPR licensing and role gates proof.
- **C — Incorrect.** Compare the user's registered authentication methods with the tenant's SSPR method requirements.
  Compare the user's registered authentication methods with the tenant's SSPR method requirements. In the external-collaboration and SSPR pilot, this check observes SSPR authentication methods. External-collaboration and SSPR pilot could pass SSPR authentication methods while SSPR licensing and role gates is wrong; external-collaboration and SSPR pilot still lacks SSPR licensing and role gates proof.
- **D — Correct.** Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.
  Confirm the pilot's license assignment, scope membership, and registered methods as separate checks. This is independent SSPR licensing and role gates evidence for the external-collaboration and SSPR pilot, even if external-collaboration and SSPR pilot setup reports success before SSPR licensing and role gates becomes observable.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Licensing requirements for Microsoft Entra self-service password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q31 — B

**Question:** The external-collaboration and SSPR pilot troubleshooting scope is the guest collaboration need to confirm that the tenant has an unused product unit before assignment. Which condition should be corrected first?

- **A — Incorrect.** The user has no usageLocation value when the license request is processed.
  The user has no usageLocation value when the license request is processed. The external-collaboration and SSPR pilot fault concerns usage location prerequisite. External-collaboration and SSPR pilot has usage location prerequisite impact, but available license capacity is the external-collaboration and SSPR pilot failed path; the usage location prerequisite state cannot produce available license capacity failure.
- **B — Correct.** All enabled units for the selected SKU are already consumed.
  All enabled units for the selected SKU are already consumed. In external-collaboration and SSPR pilot, this available license capacity cause matches the failure to confirm that the tenant has an unused product unit before assignment.
- **C — Incorrect.** The invitation exists, but the recipient has not completed redemption.
  The invitation exists, but the recipient has not completed redemption. The external-collaboration and SSPR pilot fault concerns guest redemption state. External-collaboration and SSPR pilot failed on available license capacity; this guest redemption state finding redirects external-collaboration and SSPR pilot remediation away from available license capacity.
- **D — Incorrect.** The pilot is a privileged administrator subject to stricter reset-method requirements.
  The pilot is a privileged administrator subject to stricter reset-method requirements. The external-collaboration and SSPR pilot fault concerns SSPR licensing and role gates. External-collaboration and SSPR pilot may fix SSPR licensing and role gates, yet available license capacity still fails; this external-collaboration and SSPR pilot diagnosis of SSPR licensing and role gates is wrong for available license capacity.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [List subscribed SKUs with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/subscribedsku-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q32 — C

**Question:** The external-collaboration and SSPR pilot result is partial because the guest collaboration cannot supply the regional attribute required before a cloud license is assigned. Which condition accounts for that result?

- **A — Incorrect.** The request used a product display name where Microsoft Graph requires the SKU GUID.
  The request used a product display name where Microsoft Graph requires the SKU GUID. The external-collaboration and SSPR pilot fault concerns direct license assignment. External-collaboration and SSPR pilot could repair direct license assignment while usage location prerequisite stays broken in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot remains unable to supply the regional attribute required before a cloud license is assigned.
- **B — Incorrect.** The offboarding job removed an invitation email but left the guest object and its group memberships active.
  The offboarding job removed an invitation email but left the guest object and its group memberships active. The external-collaboration and SSPR pilot fault concerns guest lifecycle properties. External-collaboration and SSPR pilot failed on usage location prerequisite; this guest lifecycle properties finding redirects external-collaboration and SSPR pilot remediation away from usage location prerequisite.
- **C — Correct.** The user has no usageLocation value when the license request is processed.
  The user has no usageLocation value when the license request is processed. This external-collaboration and SSPR pilot condition breaks usage location prerequisite, explaining why operators cannot supply the regional attribute required before a cloud license is assigned.
- **D — Incorrect.** All enabled units for the selected SKU are already consumed.
  All enabled units for the selected SKU are already consumed. The external-collaboration and SSPR pilot fault concerns available license capacity. External-collaboration and SSPR pilot has available license capacity impact, but usage location prerequisite is the external-collaboration and SSPR pilot failed path; the available license capacity state cannot produce usage location prerequisite failure.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q33 — B

**Question:** The guest collaboration evidence shows the external-collaboration and SSPR pilot cannot license one pilot user without depending on group membership. Which root cause fits that evidence?

- **A — Incorrect.** The user was made a group owner but was not added to the licensed group's members.
  The user was made a group owner but was not added to the licensed group's members. The external-collaboration and SSPR pilot fault concerns group-based licensing. External-collaboration and SSPR pilot failed on direct license assignment; this group-based licensing finding redirects external-collaboration and SSPR pilot remediation away from direct license assignment.
- **B — Correct.** The request used a product display name where Microsoft Graph requires the SKU GUID.
  For the external-collaboration and SSPR pilot, the direct license assignment failure is causal: the request used a product display name where Microsoft Graph requires the SKU GUID. Correcting it restores the ability to license one pilot user without depending on group membership.
- **C — Incorrect.** The test user is outside the group selected for SSPR.
  The test user is outside the group selected for SSPR. The external-collaboration and SSPR pilot fault concerns SSPR registration scope. External-collaboration and SSPR pilot has SSPR registration scope impact, but direct license assignment is the external-collaboration and SSPR pilot failed path; the SSPR registration scope state cannot produce direct license assignment failure.
- **D — Incorrect.** The user has no usageLocation value when the license request is processed.
  The user has no usageLocation value when the license request is processed. The external-collaboration and SSPR pilot fault concerns usage location prerequisite. External-collaboration and SSPR pilot could repair usage location prerequisite while direct license assignment stays broken in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot remains unable to license one pilot user without depending on group membership.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q34 — A

**Question:** Although the external-collaboration and SSPR pilot is meant to let the guest collaboration license a rotating team through membership rather than individual assignments, its checkpoint fails. Which guest collaboration defect explains the failure?

- **A — Correct.** The user was made a group owner but was not added to the licensed group's members.
  The user was made a group owner but was not added to the licensed group's members. The finding is specific to group-based licensing in the external-collaboration and SSPR pilot; repairing group-based licensing restores the external-collaboration and SSPR pilot ability to license a rotating team through membership rather than individual assignments.
- **B — Incorrect.** The redirect URL is not authorized for the tenant's invitation workflow.
  The redirect URL is not authorized for the tenant's invitation workflow. The external-collaboration and SSPR pilot fault concerns B2B guest invitations. External-collaboration and SSPR pilot has B2B guest invitations impact, but group-based licensing is the external-collaboration and SSPR pilot failed path; the B2B guest invitations state cannot produce group-based licensing failure.
- **C — Incorrect.** The user registered fewer usable methods than the reset policy requires.
  The user registered fewer usable methods than the reset policy requires. The external-collaboration and SSPR pilot fault concerns SSPR authentication methods. External-collaboration and SSPR pilot could repair SSPR authentication methods while group-based licensing stays broken in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot remains unable to license a rotating team through membership rather than individual assignments.
- **D — Incorrect.** The request used a product display name where Microsoft Graph requires the SKU GUID.
  The request used a product display name where Microsoft Graph requires the SKU GUID. The external-collaboration and SSPR pilot fault concerns direct license assignment. External-collaboration and SSPR pilot failed on group-based licensing; this direct license assignment finding redirects external-collaboration and SSPR pilot remediation away from group-based licensing.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Group-based licensing fundamentals](https://learn.microsoft.com/en-us/entra/fundamentals/concept-group-based-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q35 — B

**Question:** The guest collaboration support team isolated the external-collaboration and SSPR pilot incident to the attempt to send a redeemable collaboration invitation to an external address. Which condition prevents success?

- **A — Incorrect.** The invitation exists, but the recipient has not completed redemption.
  The invitation exists, but the recipient has not completed redemption. The external-collaboration and SSPR pilot fault concerns guest redemption state. External-collaboration and SSPR pilot has guest redemption state impact, but B2B guest invitations is the external-collaboration and SSPR pilot failed path; the guest redemption state state cannot produce B2B guest invitations failure.
- **B — Correct.** The redirect URL is not authorized for the tenant's invitation workflow.
  The external-collaboration and SSPR pilot cannot send a redeemable collaboration invitation to an external address because of this B2B guest invitations defect: the redirect URL is not authorized for the tenant's invitation workflow. The symptom and repair align.
- **C — Incorrect.** The pilot is a privileged administrator subject to stricter reset-method requirements.
  The pilot is a privileged administrator subject to stricter reset-method requirements. The external-collaboration and SSPR pilot fault concerns SSPR licensing and role gates. External-collaboration and SSPR pilot failed on B2B guest invitations; this SSPR licensing and role gates finding redirects external-collaboration and SSPR pilot remediation away from B2B guest invitations.
- **D — Incorrect.** The user was made a group owner but was not added to the licensed group's members.
  The user was made a group owner but was not added to the licensed group's members. The external-collaboration and SSPR pilot fault concerns group-based licensing. External-collaboration and SSPR pilot may fix group-based licensing, yet B2B guest invitations still fails; this external-collaboration and SSPR pilot diagnosis of group-based licensing is wrong for B2B guest invitations.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Create a Microsoft Entra B2B invitation](https://learn.microsoft.com/en-us/graph/api/invitation-post?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q36 — B

**Question:** An external-collaboration and SSPR pilot query surprises the identity administrator preparing a controlled external-collaboration and SSPR pilot during the guest collaboration attempt to distinguish an invited account from one that has accepted its invitation. Which finding explains it?

- **A — Incorrect.** The offboarding job removed an invitation email but left the guest object and its group memberships active.
  The offboarding job removed an invitation email but left the guest object and its group memberships active. The external-collaboration and SSPR pilot fault concerns guest lifecycle properties. External-collaboration and SSPR pilot could repair guest lifecycle properties while guest redemption state stays broken in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot remains unable to distinguish an invited account from one that has accepted its invitation.
- **B — Correct.** The invitation exists, but the recipient has not completed redemption.
  The invitation exists, but the recipient has not completed redemption. Removing this guest redemption state condition lets the external-collaboration and SSPR pilot distinguish an invited account from one that has accepted its invitation while leaving healthy controls unchanged.
- **C — Incorrect.** All enabled units for the selected SKU are already consumed.
  All enabled units for the selected SKU are already consumed. The external-collaboration and SSPR pilot fault concerns available license capacity. External-collaboration and SSPR pilot may fix available license capacity, yet guest redemption state still fails; this external-collaboration and SSPR pilot diagnosis of available license capacity is wrong for guest redemption state.
- **D — Incorrect.** The redirect URL is not authorized for the tenant's invitation workflow.
  The redirect URL is not authorized for the tenant's invitation workflow. The external-collaboration and SSPR pilot fault concerns B2B guest invitations. External-collaboration and SSPR pilot has B2B guest invitations impact, but guest redemption state is the external-collaboration and SSPR pilot failed path; the B2B guest invitations state cannot produce guest redemption state failure.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [Microsoft Entra B2B redemption experience](https://learn.microsoft.com/en-us/entra/external-id/redemption-experience)

**Source reviewed:** 2026-08-31

## LAB02-Q37 — C

**Question:** Other external-collaboration and SSPR pilot components are healthy, but the guest collaboration still cannot identify external collaborators without relying on their display names. Which state causes the isolated failure?

- **A — Incorrect.** The test user is outside the group selected for SSPR.
  The test user is outside the group selected for SSPR. The external-collaboration and SSPR pilot fault concerns SSPR registration scope. External-collaboration and SSPR pilot failed on guest lifecycle properties; this SSPR registration scope finding redirects external-collaboration and SSPR pilot remediation away from guest lifecycle properties.
- **B — Incorrect.** The user has no usageLocation value when the license request is processed.
  The user has no usageLocation value when the license request is processed. The external-collaboration and SSPR pilot fault concerns usage location prerequisite. External-collaboration and SSPR pilot may fix usage location prerequisite, yet guest lifecycle properties still fails; this external-collaboration and SSPR pilot diagnosis of usage location prerequisite is wrong for guest lifecycle properties.
- **C — Correct.** The offboarding job removed an invitation email but left the guest object and its group memberships active.
  The offboarding job removed an invitation email but left the guest object and its group memberships active. In external-collaboration and SSPR pilot, this guest lifecycle properties cause matches the failure to identify external collaborators without relying on their display names.
- **D — Incorrect.** The invitation exists, but the recipient has not completed redemption.
  The invitation exists, but the recipient has not completed redemption. The external-collaboration and SSPR pilot fault concerns guest redemption state. External-collaboration and SSPR pilot could repair guest redemption state while guest lifecycle properties stays broken in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot remains unable to identify external collaborators without relying on their display names.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Properties of a Microsoft Entra B2B collaboration user](https://learn.microsoft.com/en-us/entra/external-id/user-properties)

**Source reviewed:** 2026-08-31

## LAB02-Q38 — D

**Question:** During a guest collaboration fault drill, the external-collaboration and SSPR pilot does not limit password-reset registration to the approved pilot population. Which finding identifies the defect?

- **A — Incorrect.** The user registered fewer usable methods than the reset policy requires.
  The user registered fewer usable methods than the reset policy requires. The external-collaboration and SSPR pilot fault concerns SSPR authentication methods. External-collaboration and SSPR pilot may fix SSPR authentication methods, yet SSPR registration scope still fails; this external-collaboration and SSPR pilot diagnosis of SSPR authentication methods is wrong for SSPR registration scope.
- **B — Incorrect.** The request used a product display name where Microsoft Graph requires the SKU GUID.
  The request used a product display name where Microsoft Graph requires the SKU GUID. The external-collaboration and SSPR pilot fault concerns direct license assignment. External-collaboration and SSPR pilot has direct license assignment impact, but SSPR registration scope is the external-collaboration and SSPR pilot failed path; the direct license assignment state cannot produce SSPR registration scope failure.
- **C — Incorrect.** The offboarding job removed an invitation email but left the guest object and its group memberships active.
  The offboarding job removed an invitation email but left the guest object and its group memberships active. The external-collaboration and SSPR pilot fault concerns guest lifecycle properties. External-collaboration and SSPR pilot could repair guest lifecycle properties while SSPR registration scope stays broken in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot remains unable to limit password-reset registration to the approved pilot population.
- **D — Correct.** The test user is outside the group selected for SSPR.
  The test user is outside the group selected for SSPR. This external-collaboration and SSPR pilot condition breaks SSPR registration scope, explaining why operators cannot limit password-reset registration to the approved pilot population.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [How Microsoft Entra self-service password reset works](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks)

**Source reviewed:** 2026-08-31

## LAB02-Q39 — C

**Question:** The external-collaboration and SSPR pilot setup finishes, yet the guest collaboration cannot allow only the approved proofs during password reset. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The pilot is a privileged administrator subject to stricter reset-method requirements.
  The pilot is a privileged administrator subject to stricter reset-method requirements. The external-collaboration and SSPR pilot fault concerns SSPR licensing and role gates. External-collaboration and SSPR pilot has SSPR licensing and role gates impact, but SSPR authentication methods is the external-collaboration and SSPR pilot failed path; the SSPR licensing and role gates state cannot produce SSPR authentication methods failure.
- **B — Incorrect.** The user was made a group owner but was not added to the licensed group's members.
  The user was made a group owner but was not added to the licensed group's members. The external-collaboration and SSPR pilot fault concerns group-based licensing. External-collaboration and SSPR pilot could repair group-based licensing while SSPR authentication methods stays broken in external-collaboration and SSPR pilot; the external-collaboration and SSPR pilot remains unable to allow only the approved proofs during password reset.
- **C — Correct.** The user registered fewer usable methods than the reset policy requires.
  For the external-collaboration and SSPR pilot, the SSPR authentication methods failure is causal: the user registered fewer usable methods than the reset policy requires. Correcting it restores the ability to allow only the approved proofs during password reset.
- **D — Incorrect.** The test user is outside the group selected for SSPR.
  The test user is outside the group selected for SSPR. The external-collaboration and SSPR pilot fault concerns SSPR registration scope. External-collaboration and SSPR pilot may fix SSPR registration scope, yet SSPR authentication methods still fails; this external-collaboration and SSPR pilot diagnosis of SSPR registration scope is wrong for SSPR authentication methods.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Authentication methods for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods)

**Source reviewed:** 2026-08-31

## LAB02-Q40 — A

**Question:** A guest collaboration break/fix in the external-collaboration and SSPR pilot fails when operators try to stop safely when the tenant lacks the entitlement or role needed for reset changes. Which diagnosis fits?

- **A — Correct.** The pilot is a privileged administrator subject to stricter reset-method requirements.
  The pilot is a privileged administrator subject to stricter reset-method requirements. The finding is specific to SSPR licensing and role gates in the external-collaboration and SSPR pilot; repairing SSPR licensing and role gates restores the external-collaboration and SSPR pilot ability to stop safely when the tenant lacks the entitlement or role needed for reset changes.
- **B — Incorrect.** All enabled units for the selected SKU are already consumed.
  All enabled units for the selected SKU are already consumed. The external-collaboration and SSPR pilot fault concerns available license capacity. External-collaboration and SSPR pilot failed on SSPR licensing and role gates; this available license capacity finding redirects external-collaboration and SSPR pilot remediation away from SSPR licensing and role gates.
- **C — Incorrect.** The redirect URL is not authorized for the tenant's invitation workflow.
  The redirect URL is not authorized for the tenant's invitation workflow. The external-collaboration and SSPR pilot fault concerns B2B guest invitations. External-collaboration and SSPR pilot may fix B2B guest invitations, yet SSPR licensing and role gates still fails; this external-collaboration and SSPR pilot diagnosis of B2B guest invitations is wrong for SSPR licensing and role gates.
- **D — Incorrect.** The user registered fewer usable methods than the reset policy requires.
  The user registered fewer usable methods than the reset policy requires. The external-collaboration and SSPR pilot fault concerns SSPR authentication methods. External-collaboration and SSPR pilot has SSPR authentication methods impact, but SSPR licensing and role gates is the external-collaboration and SSPR pilot failed path; the SSPR authentication methods state cannot produce SSPR licensing and role gates failure.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Licensing requirements for Microsoft Entra self-service password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q41 — C

**Question:** The external-collaboration and SSPR pilot has two guest collaboration gates: confirm that the tenant has an unused product unit before assignment, then prove the external-collaboration and SSPR pilot state. Which guest collaboration sequence works?

- **A — Incorrect.** First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
  First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state. This external-collaboration and SSPR pilot pair serves direct license assignment. Direct license assignment cannot replace available license capacity in external-collaboration and SSPR pilot. Use this available license capacity pair instead: First, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
- **B — Incorrect.** First, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object.
  First, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object. This external-collaboration and SSPR pilot pair serves guest lifecycle properties. External-collaboration and SSPR pilot proves guest lifecycle properties, but available license capacity lacks implementation in external-collaboration and SSPR pilot and available license capacity proof; the available license capacity outcome to confirm that the tenant has an unused product unit before assignment remains open.
- **C — Correct.** First, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
  The external-collaboration and SSPR pilot gets a complete available license capacity sequence here: first, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments. Read-back evidence follows the change.
- **D — Incorrect.** First, Enable SSPR for the approved pilot group before broadening the scope. Then, Read the authorization policy and target-group configuration through Microsoft Graph.
  First, Enable SSPR for the approved pilot group before broadening the scope. Then, Read the authorization policy and target-group configuration through Microsoft Graph. This external-collaboration and SSPR pilot pair serves SSPR registration scope. External-collaboration and SSPR pilot closes SSPR registration scope, not available license capacity; without the available license capacity workflow, it cannot confirm that the tenant has an unused product unit before assignment.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [List subscribed SKUs with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/subscribedsku-list?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q42 — B

**Question:** Which guest collaboration path makes the external-collaboration and SSPR pilot able to supply the regional attribute required before a cloud license is assigned, then inspects the defining properties?

- **A — Incorrect.** First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID.
  First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID. This external-collaboration and SSPR pilot pair serves group-based licensing. External-collaboration and SSPR pilot proves group-based licensing, but usage location prerequisite lacks implementation in external-collaboration and SSPR pilot and usage location prerequisite proof; the usage location prerequisite outcome to supply the regional attribute required before a cloud license is assigned remains open.
- **B — Correct.** First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code.
  First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code. This ordered usage location prerequisite workflow lets the external-collaboration and SSPR pilot supply the regional attribute required before a cloud license is assigned and then verify the resulting state.
- **C — Incorrect.** First, Enable SSPR for the approved pilot group before broadening the scope. Then, Read the authorization policy and target-group configuration through Microsoft Graph.
  First, Enable SSPR for the approved pilot group before broadening the scope. Then, Read the authorization policy and target-group configuration through Microsoft Graph. This external-collaboration and SSPR pilot pair serves SSPR registration scope. External-collaboration and SSPR pilot closes SSPR registration scope, not usage location prerequisite; without the usage location prerequisite workflow, it cannot supply the regional attribute required before a cloud license is assigned.
- **D — Incorrect.** First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements.
  First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements. This external-collaboration and SSPR pilot pair serves SSPR authentication methods. SSPR authentication methods cannot replace usage location prerequisite in external-collaboration and SSPR pilot. Use this usage location prerequisite pair instead: First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q43 — A

**Question:** At the external-collaboration and SSPR pilot approval gate, operators must show that the guest collaboration can license one pilot user without depending on group membership. Which guest collaboration configure-and-check pair is defensible?

- **A — Correct.** First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
  First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state. For external-collaboration and SSPR pilot, the direct license assignment operation precedes its direct license assignment read-back check, allowing it to license one pilot user without depending on group membership.
- **B — Incorrect.** First, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID.
  First, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID. This external-collaboration and SSPR pilot pair serves B2B guest invitations. External-collaboration and SSPR pilot closes B2B guest invitations, not direct license assignment; without the direct license assignment workflow, it cannot license one pilot user without depending on group membership.
- **C — Incorrect.** First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements.
  First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements. This external-collaboration and SSPR pilot pair serves SSPR authentication methods. SSPR authentication methods cannot replace direct license assignment in external-collaboration and SSPR pilot. Use this direct license assignment pair instead: First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
- **D — Incorrect.** First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.
  First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks. This external-collaboration and SSPR pilot pair serves SSPR licensing and role gates. External-collaboration and SSPR pilot proves SSPR licensing and role gates, but direct license assignment lacks implementation in external-collaboration and SSPR pilot and direct license assignment proof; the direct license assignment outcome to license one pilot user without depending on group membership remains open.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [Assign licenses to a user with Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q44 — D

**Question:** The external-collaboration and SSPR pilot forbids a partial guest collaboration result. Operators must first license a rotating team through membership rather than individual assignments and afterward confirm the external-collaboration and SSPR pilot outcome. Which guest collaboration sequence is complete?

- **A — Incorrect.** First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user.
  First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user. This external-collaboration and SSPR pilot pair serves guest redemption state. External-collaboration and SSPR pilot closes guest redemption state, not group-based licensing; without the group-based licensing workflow, it cannot license a rotating team through membership rather than individual assignments.
- **B — Incorrect.** First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.
  First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks. This external-collaboration and SSPR pilot pair serves SSPR licensing and role gates. SSPR licensing and role gates cannot replace group-based licensing in external-collaboration and SSPR pilot. Use this group-based licensing pair instead: First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID.
- **C — Incorrect.** First, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
  First, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments. This external-collaboration and SSPR pilot pair serves available license capacity. External-collaboration and SSPR pilot proves available license capacity, but group-based licensing lacks implementation in external-collaboration and SSPR pilot and group-based licensing proof; the group-based licensing outcome to license a rotating team through membership rather than individual assignments remains open.
- **D — Correct.** First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID.
  First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID. In the external-collaboration and SSPR pilot, the first group-based licensing step runs; the external-collaboration and SSPR pilot then reads group-based licensing state to prove it can license a rotating team through membership rather than individual assignments.

**Objectives:** `IG-USERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Group-based licensing fundamentals](https://learn.microsoft.com/en-us/entra/fundamentals/concept-group-based-licensing)

**Source reviewed:** 2026-08-31

## LAB02-Q45 — B

**Question:** Only the external-collaboration and SSPR pilot change needed to send a redeemable collaboration invitation to an external address is allowed, and guest collaboration proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object.
  First, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object. This external-collaboration and SSPR pilot pair serves guest lifecycle properties. Guest lifecycle properties cannot replace B2B guest invitations in external-collaboration and SSPR pilot. Use this B2B guest invitations pair instead: First, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID.
- **B — Correct.** First, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID.
  For the external-collaboration and SSPR pilot, the safe B2B guest invitations order is: first, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID. The external-collaboration and SSPR pilot records B2B guest invitations proof after configuration.
- **C — Incorrect.** First, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
  First, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments. This external-collaboration and SSPR pilot pair serves available license capacity. External-collaboration and SSPR pilot uses available license capacity for both steps; B2B guest invitations remains untouched in external-collaboration and SSPR pilot, so its B2B guest invitations gate to send a redeemable collaboration invitation to an external address fails.
- **D — Incorrect.** First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code.
  First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code. This external-collaboration and SSPR pilot pair serves usage location prerequisite. External-collaboration and SSPR pilot closes usage location prerequisite, not B2B guest invitations; without the B2B guest invitations workflow, it cannot send a redeemable collaboration invitation to an external address.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Create a Microsoft Entra B2B invitation](https://learn.microsoft.com/en-us/graph/api/invitation-post?view=graph-rest-1.0)

**Source reviewed:** 2026-08-31

## LAB02-Q46 — C

**Question:** The external-collaboration and SSPR pilot runbook separates guest collaboration mutation from validation while it must distinguish an invited account from one that has accepted its invitation. Which sequence proves it cleanly?

- **A — Incorrect.** First, Enable SSPR for the approved pilot group before broadening the scope. Then, Read the authorization policy and target-group configuration through Microsoft Graph.
  First, Enable SSPR for the approved pilot group before broadening the scope. Then, Read the authorization policy and target-group configuration through Microsoft Graph. This external-collaboration and SSPR pilot pair serves SSPR registration scope. External-collaboration and SSPR pilot proves SSPR registration scope, but guest redemption state lacks implementation in external-collaboration and SSPR pilot and guest redemption state proof; the guest redemption state outcome to distinguish an invited account from one that has accepted its invitation remains open.
- **B — Incorrect.** First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code.
  First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code. This external-collaboration and SSPR pilot pair serves usage location prerequisite. External-collaboration and SSPR pilot uses usage location prerequisite for both steps; guest redemption state remains untouched in external-collaboration and SSPR pilot, so its guest redemption state gate to distinguish an invited account from one that has accepted its invitation fails.
- **C — Correct.** First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user.
  First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user. The external-collaboration and SSPR pilot uses its guest redemption state mutation gate and guest redemption state verification gate before it can distinguish an invited account from one that has accepted its invitation.
- **D — Incorrect.** First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
  First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state. This external-collaboration and SSPR pilot pair serves direct license assignment. Direct license assignment cannot replace guest redemption state in external-collaboration and SSPR pilot. Use this guest redemption state pair instead: First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB02-CP01`).

**Microsoft Learn sources:**

- [Microsoft Entra B2B redemption experience](https://learn.microsoft.com/en-us/entra/external-id/redemption-experience)

**Source reviewed:** 2026-08-31

## LAB02-Q47 — A

**Question:** The external-collaboration and SSPR pilot checkpoint requires both this guest collaboration outcome—identify external collaborators without relying on their display names—and a read-only external-collaboration and SSPR pilot state check. Which guest collaboration response is complete?

- **A — Correct.** First, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object.
  The external-collaboration and SSPR pilot gets a complete guest lifecycle properties sequence here: first, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object. Read-back evidence follows the change.
- **B — Incorrect.** First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements.
  First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements. This external-collaboration and SSPR pilot pair serves SSPR authentication methods. External-collaboration and SSPR pilot closes SSPR authentication methods, not guest lifecycle properties; without the guest lifecycle properties workflow, it cannot identify external collaborators without relying on their display names.
- **C — Incorrect.** First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state.
  First, Submit addLicenses for the target user with the required SKU ID and any disabled plan IDs. Then, Read licenseAssignmentStates and confirm the intended SKU is assigned without an error state. This external-collaboration and SSPR pilot pair serves direct license assignment. Direct license assignment cannot replace guest lifecycle properties in external-collaboration and SSPR pilot. Use this guest lifecycle properties pair instead: First, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object.
- **D — Incorrect.** First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID.
  First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID. This external-collaboration and SSPR pilot pair serves group-based licensing. External-collaboration and SSPR pilot proves group-based licensing, but guest lifecycle properties lacks implementation in external-collaboration and SSPR pilot and guest lifecycle properties proof; the guest lifecycle properties outcome to identify external collaborators without relying on their display names remains open.

**Objectives:** `IG-USERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB02-CP02`).

**Microsoft Learn sources:**

- [Properties of a Microsoft Entra B2B collaboration user](https://learn.microsoft.com/en-us/entra/external-id/user-properties)

**Source reviewed:** 2026-08-31

## LAB02-Q48 — B

**Question:** The external-collaboration and SSPR pilot runbook must limit password-reset registration to the approved pilot population, then retain guest collaboration read-back evidence. Which external-collaboration and SSPR pilot pair completes both duties?

- **A — Incorrect.** First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.
  First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks. This external-collaboration and SSPR pilot pair serves SSPR licensing and role gates. External-collaboration and SSPR pilot closes SSPR licensing and role gates, not SSPR registration scope; without the SSPR registration scope workflow, it cannot limit password-reset registration to the approved pilot population.
- **B — Correct.** First, Enable SSPR for the approved pilot group before broadening the scope. Then, Read the authorization policy and target-group configuration through Microsoft Graph.
  First, Enable SSPR for the approved pilot group before broadening the scope. Then, Read the authorization policy and target-group configuration through Microsoft Graph. This ordered SSPR registration scope workflow lets the external-collaboration and SSPR pilot limit password-reset registration to the approved pilot population and then verify the resulting state.
- **C — Incorrect.** First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID.
  First, Assign the SKU to the licensing group and add eligible users as members. Then, Inspect the user's inherited assignment state and confirm the assigning group ID. This external-collaboration and SSPR pilot pair serves group-based licensing. External-collaboration and SSPR pilot proves group-based licensing, but SSPR registration scope lacks implementation in external-collaboration and SSPR pilot and SSPR registration scope proof; the SSPR registration scope outcome to limit password-reset registration to the approved pilot population remains open.
- **D — Incorrect.** First, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID.
  First, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID. This external-collaboration and SSPR pilot pair serves B2B guest invitations. External-collaboration and SSPR pilot uses B2B guest invitations for both steps; SSPR registration scope remains untouched in external-collaboration and SSPR pilot, so its SSPR registration scope gate to limit password-reset registration to the approved pilot population fails.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB02-CP03`).

**Microsoft Learn sources:**

- [How Microsoft Entra self-service password reset works](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks)

**Source reviewed:** 2026-08-31

## LAB02-Q49 — C

**Question:** To satisfy the guest collaboration requirement, operators must change the external-collaboration and SSPR pilot configuration and prove it can allow only the approved proofs during password reset. Which sequence is coherent?

- **A — Incorrect.** First, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments.
  First, Read subscribedSkus and calculate enabled units minus consumed units before assigning a license. Then, Query the selected SKU and confirm that available units remain greater than or equal to the requested assignments. This external-collaboration and SSPR pilot pair serves available license capacity. Available license capacity cannot replace SSPR authentication methods in external-collaboration and SSPR pilot. Use this SSPR authentication methods pair instead: First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements.
- **B — Incorrect.** First, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID.
  First, Create an invitation with the guest email address and an approved redirect URL. Then, Read the invited user's userType and externalUserState from the returned invitedUser ID. This external-collaboration and SSPR pilot pair serves B2B guest invitations. External-collaboration and SSPR pilot proves B2B guest invitations, but SSPR authentication methods lacks implementation in external-collaboration and SSPR pilot and SSPR authentication methods proof; the SSPR authentication methods outcome to allow only the approved proofs during password reset remains open.
- **C — Correct.** First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements.
  First, Configure permitted reset methods and require users to register enough approved methods. Then, Compare the user's registered authentication methods with the tenant's SSPR method requirements. For external-collaboration and SSPR pilot, the SSPR authentication methods operation precedes its SSPR authentication methods read-back check, allowing it to allow only the approved proofs during password reset.
- **D — Incorrect.** First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user.
  First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user. This external-collaboration and SSPR pilot pair serves guest redemption state. External-collaboration and SSPR pilot closes guest redemption state, not SSPR authentication methods; without the SSPR authentication methods workflow, it cannot allow only the approved proofs during password reset.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB02-CP04`).

**Microsoft Learn sources:**

- [Authentication methods for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods)

**Source reviewed:** 2026-08-31

## LAB02-Q50 — B

**Question:** The identity administrator preparing a controlled external-collaboration and SSPR pilot needs a safe external-collaboration and SSPR pilot change to stop safely when the tenant lacks the entitlement or role needed for reset changes, followed by guest collaboration evidence. Which pair merits approval?

- **A — Incorrect.** First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code.
  First, Set the user's two-letter usage location before submitting the license assignment. Then, Read usageLocation for the target object and confirm it is a valid country or region code. This external-collaboration and SSPR pilot pair serves usage location prerequisite. External-collaboration and SSPR pilot proves usage location prerequisite, but SSPR licensing and role gates lacks implementation in external-collaboration and SSPR pilot and SSPR licensing and role gates proof; the SSPR licensing and role gates outcome to stop safely when the tenant lacks the entitlement or role needed for reset changes remains open.
- **B — Correct.** First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.
  First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks. In the external-collaboration and SSPR pilot, the first SSPR licensing and role gates step runs; the external-collaboration and SSPR pilot then reads SSPR licensing and role gates state to prove it can stop safely when the tenant lacks the entitlement or role needed for reset changes.
- **C — Incorrect.** First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user.
  First, Track the guest by object ID and wait for redemption before depending on interactive access. Then, Query externalUserState and its change timestamp for the invited user. This external-collaboration and SSPR pilot pair serves guest redemption state. External-collaboration and SSPR pilot closes guest redemption state, not SSPR licensing and role gates; without the SSPR licensing and role gates workflow, it cannot stop safely when the tenant lacks the entitlement or role needed for reset changes.
- **D — Incorrect.** First, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object.
  First, Record the guest object ID and assign only the groups needed for the collaboration period. Then, Review userType, group memberships, and sign-in state for the exact guest object. This external-collaboration and SSPR pilot pair serves guest lifecycle properties. Guest lifecycle properties cannot replace SSPR licensing and role gates in external-collaboration and SSPR pilot. Use this SSPR licensing and role gates pair instead: First, Verify licensing and use a nonprivileged pilot identity before validating the standard SSPR path. Then, Confirm the pilot's license assignment, scope membership, and registered methods as separate checks.

**Objectives:** `IG-USERS-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB02-CP05`).

**Microsoft Learn sources:**

- [Licensing requirements for Microsoft Entra self-service password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)

**Source reviewed:** 2026-08-31
