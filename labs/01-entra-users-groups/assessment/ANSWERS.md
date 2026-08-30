# Lab 01 answer key

Review these explanations only after answering all ten questions.

## LAB01-Q01 — C

A cloud user's UPN uses an `alias@domain` format, and the suffix must be in the tenant's verified domains collection.

- A is incorrect because the identity is independent of the administrator's email.
- B is incorrect because a suitable verified custom or initial domain can be used.
- C is correct because Microsoft Graph validates the UPN suffix against verified domains.
- D is incorrect because subscription names do not define directory UPNs.

Objectives: `IG-USERS-01`.

## LAB01-Q02 — A

A standard security group used for access assignments is security-enabled and can be non-mail-enabled.

- A is correct for a non-mail-enabled security group.
- B lacks the required security capability.
- C is not security-enabled and therefore does not meet the access requirement.
- D introduces mail and dynamic-membership capabilities that were not requested.

Objectives: `IG-USERS-01`.

## LAB01-Q03 — B

Azure RBAC roles and Microsoft Entra roles protect different systems. User Administrator is the appropriate role model for this tenant identity exercise.

- A is incorrect because Microsoft Graph is not activated through Azure provider registration.
- B is correct because subscription Owner does not grant directory user management.
- C is incorrect because authorized tenant administrators can create cloud users.
- D is incorrect because directory objects are not deployed to an Azure region.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

## LAB01-Q04 — D

The bootstrap password should remain secret, stay out of run state, and be replaced at first sign-in.

- A is unsafe because group descriptions are visible directory properties.
- B leaves the bootstrap password as the continuing secret.
- C violates password isolation and is unsafe even if history is removed.
- D is correct because the password profile forces first-sign-in replacement.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

## LAB01-Q05 — A

`az ad group member add` changes Microsoft Entra group membership and accepts exact group and member object IDs.

- A is the correct directory membership command.
- B creates Azure resource access assignments rather than directory membership.
- C uses a nonexistent group parameter on user update.
- D manages Azure resource groups, not Microsoft Entra groups.

Objectives: `IG-USERS-02`.

## LAB01-Q06 — C

`az rest` can obtain the appropriate token and call Microsoft Graph. A `PATCH` request against the exact user ID exposes supported writable properties that a simplified CLI command omits.

- A cannot transfer Azure subscription tags into a directory user.
- B creates identity drift rather than managing the target user.
- C is the supported command-first solution.
- D is unsafe, unsupported, and does not turn a read operation into an update.

Objectives: `IG-USERS-02`.

## LAB01-Q07 — B

Group ownership and group membership must be evaluated independently. An owner can manage a group according to policy but does not automatically receive member-based access.

- A incorrectly treats ownership as universal transitive membership.
- B correctly separates the two relationships.
- C is incorrect because non-member owners are supported.
- D is incorrect because ownership does not alter group type.

Objectives: `IG-USERS-02`.

## LAB01-Q08 — D

The object ID returned at creation is the safest automation identifier. Display names can be duplicated or changed.

- A risks deleting an unrelated prefix match.
- B relies on unstable presentation order.
- C uses a subscription identifier for a tenant-scoped object.
- D correctly limits cleanup to the object created by the run.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

## LAB01-Q09 — B

Microsoft Entra user deletion normally creates a recoverable deleted item. Active-object cleanup can therefore pass while retention still allows restoration.

- A mistakes expected soft-deletion behavior for a failure.
- B correctly distinguishes active deletion from permanent deletion.
- C is incorrect because deletion does not convert a member into a guest.
- D is incorrect because subscription deletion does not manage tenant users.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

## LAB01-Q10 — A

The strongest evidence combines a required positive relationship, an expected negative relationship, and an independent owner check.

- A validates the exact intended member/owner model and detects unintended expansion.
- B proves only a naming convention.
- C proves object existence but ignores the required relationships.
- D changes access automatically and destroys the negative control.

Objectives: `IG-USERS-02`.
