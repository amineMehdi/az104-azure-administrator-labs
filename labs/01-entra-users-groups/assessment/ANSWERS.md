# Lab 01 answer key

Review these explanations only after answering all 50 questions.

## LAB01-Q01 — B

A cloud user's userPrincipalName uses an Internet-style alias@domain format, and the domain must belong to the tenant's verified domains collection.

- A: Any suitable verified tenant domain can be used; it is not limited to the initial domain.
- B: Correct. Microsoft Graph and Azure CLI require a verified-domain UPN suffix.
- C: Azure subscription names do not determine Microsoft Entra UPN suffixes.
- D: The new identity is independent of the administrator's email address.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q02 — C

A standard security group used for access assignments is security-enabled and can be non-mail-enabled. Microsoft 365 collaboration capabilities are not required.

- A: A group that is not security-enabled cannot satisfy the access-assignment requirement.
- B: Mail and dynamic membership add capabilities that the requirement does not request.
- C: Correct. These values describe a non-mail-enabled security group.
- D: This describes a mail-enabled object without the required security capability.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q03 — D

Azure RBAC and Microsoft Entra roles protect different resource systems. A suitable directory role such as User Administrator is normally required for the exercise.

- A: Authorized tenant administrators can create cloud-only users directly.
- B: Microsoft Entra user creation is tenant-scoped and not tied to an Azure region.
- C: Microsoft Graph access is not enabled by registering an Azure resource provider.
- D: Correct. Subscription ownership and tenant identity administration are separate authorization planes.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/concept-understand-roles), [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

## LAB01-Q04 — A

A cloud user's userPrincipalName uses an Internet-style alias@domain format, and the domain must belong to the tenant's verified domains collection.

- A: Correct. Microsoft Graph and Azure CLI require a verified-domain UPN suffix.
- B: Azure subscription names do not determine Microsoft Entra UPN suffixes.
- C: The new identity is independent of the administrator's email address.
- D: Any suitable verified tenant domain can be used; it is not limited to the initial domain.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q05 — B

A standard security group used for access assignments is security-enabled and can be non-mail-enabled. Microsoft 365 collaboration capabilities are not required.

- A: Mail and dynamic membership add capabilities that the requirement does not request.
- B: Correct. These values describe a non-mail-enabled security group.
- C: This describes a mail-enabled object without the required security capability.
- D: A group that is not security-enabled cannot satisfy the access-assignment requirement.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q06 — C

Azure RBAC and Microsoft Entra roles protect different resource systems. A suitable directory role such as User Administrator is normally required for the exercise.

- A: Microsoft Entra user creation is tenant-scoped and not tied to an Azure region.
- B: Microsoft Graph access is not enabled by registering an Azure resource provider.
- C: Correct. Subscription ownership and tenant identity administration are separate authorization planes.
- D: Authorized tenant administrators can create cloud-only users directly.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/concept-understand-roles), [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

## LAB01-Q07 — D

A cloud user's userPrincipalName uses an Internet-style alias@domain format, and the domain must belong to the tenant's verified domains collection.

- A: Azure subscription names do not determine Microsoft Entra UPN suffixes.
- B: The new identity is independent of the administrator's email address.
- C: Any suitable verified tenant domain can be used; it is not limited to the initial domain.
- D: Correct. Microsoft Graph and Azure CLI require a verified-domain UPN suffix.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q08 — A

A standard security group used for access assignments is security-enabled and can be non-mail-enabled. Microsoft 365 collaboration capabilities are not required.

- A: Correct. These values describe a non-mail-enabled security group.
- B: This describes a mail-enabled object without the required security capability.
- C: A group that is not security-enabled cannot satisfy the access-assignment requirement.
- D: Mail and dynamic membership add capabilities that the requirement does not request.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q09 — B

Azure RBAC and Microsoft Entra roles protect different resource systems. A suitable directory role such as User Administrator is normally required for the exercise.

- A: Microsoft Graph access is not enabled by registering an Azure resource provider.
- B: Correct. Subscription ownership and tenant identity administration are separate authorization planes.
- C: Authorized tenant administrators can create cloud-only users directly.
- D: Microsoft Entra user creation is tenant-scoped and not tied to an Azure region.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/concept-understand-roles), [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

## LAB01-Q10 — C

A cloud user's userPrincipalName uses an Internet-style alias@domain format, and the domain must belong to the tenant's verified domains collection.

- A: The new identity is independent of the administrator's email address.
- B: Any suitable verified tenant domain can be used; it is not limited to the initial domain.
- C: Correct. Microsoft Graph and Azure CLI require a verified-domain UPN suffix.
- D: Azure subscription names do not determine Microsoft Entra UPN suffixes.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q11 — D

A standard security group used for access assignments is security-enabled and can be non-mail-enabled. Microsoft 365 collaboration capabilities are not required.

- A: This describes a mail-enabled object without the required security capability.
- B: A group that is not security-enabled cannot satisfy the access-assignment requirement.
- C: Mail and dynamic membership add capabilities that the requirement does not request.
- D: Correct. These values describe a non-mail-enabled security group.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q12 — A

Azure RBAC and Microsoft Entra roles protect different resource systems. A suitable directory role such as User Administrator is normally required for the exercise.

- A: Correct. Subscription ownership and tenant identity administration are separate authorization planes.
- B: Authorized tenant administrators can create cloud-only users directly.
- C: Microsoft Entra user creation is tenant-scoped and not tied to an Azure region.
- D: Microsoft Graph access is not enabled by registering an Azure resource provider.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/concept-understand-roles), [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

## LAB01-Q13 — B

A cloud user's userPrincipalName uses an Internet-style alias@domain format, and the domain must belong to the tenant's verified domains collection.

- A: Any suitable verified tenant domain can be used; it is not limited to the initial domain.
- B: Correct. Microsoft Graph and Azure CLI require a verified-domain UPN suffix.
- C: Azure subscription names do not determine Microsoft Entra UPN suffixes.
- D: The new identity is independent of the administrator's email address.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q14 — C

A standard security group used for access assignments is security-enabled and can be non-mail-enabled. Microsoft 365 collaboration capabilities are not required.

- A: A group that is not security-enabled cannot satisfy the access-assignment requirement.
- B: Mail and dynamic membership add capabilities that the requirement does not request.
- C: Correct. These values describe a non-mail-enabled security group.
- D: This describes a mail-enabled object without the required security capability.

Objectives: `IG-USERS-01`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q15 — D

Azure RBAC and Microsoft Entra roles protect different resource systems. A suitable directory role such as User Administrator is normally required for the exercise.

- A: Authorized tenant administrators can create cloud-only users directly.
- B: Microsoft Entra user creation is tenant-scoped and not tied to an Azure region.
- C: Microsoft Graph access is not enabled by registering an Azure resource provider.
- D: Correct. Subscription ownership and tenant identity administration are separate authorization planes.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/concept-understand-roles), [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

## LAB01-Q16 — A

The bootstrap password should be handled as a secret, omitted from state, and changed at the user's first sign-in by setting forceChangePasswordNextSignIn.

- A: Correct. The setting forces replacement of the temporary password at first sign-in.
- B: Group descriptions are visible directory data and must never hold passwords.
- C: Disabling expiration does not replace the temporary bootstrap secret.
- D: Password reuse is unsafe and deleting history does not correct the design.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q17 — B

The az ad group member command group manages Microsoft Entra group membership, and member add accepts the group and member object IDs.

- A: az group manages Azure resource groups, not Microsoft Entra groups.
- B: Correct. This adds the recorded directory object as a direct member.
- C: Azure role assignments grant resource access; they do not edit directory membership.
- D: az ad user update does not expose a group-membership parameter.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q18 — C

Azure CLI can authenticate an az rest request to Microsoft Graph. PATCHing the exact user object exposes writable properties not offered by a simplified command.

- A: Azure subscription metadata has no relationship to Microsoft Entra user properties.
- B: Creating duplicates introduces drift and does not manage the existing identity.
- C: Correct. Microsoft Graph is the appropriate supported property-management surface.
- D: Credential caches must not be edited and a show operation is read-only.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-rest), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-update?view=graph-rest-1.0).

## LAB01-Q19 — D

Owners manage a group according to directory policy, while members receive access or app behavior associated with membership. One relationship does not imply the other.

- A: Microsoft Entra supports group owners who are not direct members.
- B: Changing an owner does not alter mail or group-type properties.
- C: Owner status does not universally create direct or transitive membership.
- D: Correct. Validate owners and members independently.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q20 — A

Display names can be duplicated or changed. A run manifest should record the returned object ID and cleanup should verify that exact object before deletion.

- A: Correct. Exact recorded object IDs provide the safest cleanup boundary.
- B: Prefix search results are ambiguous and can target an unrelated group.
- C: Portal list ordering is not a stable identity or automation input.
- D: Microsoft Entra groups are tenant objects and are not owned by an Azure subscription.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q21 — B

The bootstrap password should be handled as a secret, omitted from state, and changed at the user's first sign-in by setting forceChangePasswordNextSignIn.

- A: Password reuse is unsafe and deleting history does not correct the design.
- B: Correct. The setting forces replacement of the temporary password at first sign-in.
- C: Group descriptions are visible directory data and must never hold passwords.
- D: Disabling expiration does not replace the temporary bootstrap secret.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q22 — C

The az ad group member command group manages Microsoft Entra group membership, and member add accepts the group and member object IDs.

- A: az ad user update does not expose a group-membership parameter.
- B: az group manages Azure resource groups, not Microsoft Entra groups.
- C: Correct. This adds the recorded directory object as a direct member.
- D: Azure role assignments grant resource access; they do not edit directory membership.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q23 — D

Azure CLI can authenticate an az rest request to Microsoft Graph. PATCHing the exact user object exposes writable properties not offered by a simplified command.

- A: Credential caches must not be edited and a show operation is read-only.
- B: Azure subscription metadata has no relationship to Microsoft Entra user properties.
- C: Creating duplicates introduces drift and does not manage the existing identity.
- D: Correct. Microsoft Graph is the appropriate supported property-management surface.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-rest), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-update?view=graph-rest-1.0).

## LAB01-Q24 — A

Owners manage a group according to directory policy, while members receive access or app behavior associated with membership. One relationship does not imply the other.

- A: Correct. Validate owners and members independently.
- B: Microsoft Entra supports group owners who are not direct members.
- C: Changing an owner does not alter mail or group-type properties.
- D: Owner status does not universally create direct or transitive membership.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q25 — B

Display names can be duplicated or changed. A run manifest should record the returned object ID and cleanup should verify that exact object before deletion.

- A: Microsoft Entra groups are tenant objects and are not owned by an Azure subscription.
- B: Correct. Exact recorded object IDs provide the safest cleanup boundary.
- C: Prefix search results are ambiguous and can target an unrelated group.
- D: Portal list ordering is not a stable identity or automation input.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q26 — C

The bootstrap password should be handled as a secret, omitted from state, and changed at the user's first sign-in by setting forceChangePasswordNextSignIn.

- A: Disabling expiration does not replace the temporary bootstrap secret.
- B: Password reuse is unsafe and deleting history does not correct the design.
- C: Correct. The setting forces replacement of the temporary password at first sign-in.
- D: Group descriptions are visible directory data and must never hold passwords.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q27 — D

The az ad group member command group manages Microsoft Entra group membership, and member add accepts the group and member object IDs.

- A: Azure role assignments grant resource access; they do not edit directory membership.
- B: az ad user update does not expose a group-membership parameter.
- C: az group manages Azure resource groups, not Microsoft Entra groups.
- D: Correct. This adds the recorded directory object as a direct member.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q28 — A

Azure CLI can authenticate an az rest request to Microsoft Graph. PATCHing the exact user object exposes writable properties not offered by a simplified command.

- A: Correct. Microsoft Graph is the appropriate supported property-management surface.
- B: Credential caches must not be edited and a show operation is read-only.
- C: Azure subscription metadata has no relationship to Microsoft Entra user properties.
- D: Creating duplicates introduces drift and does not manage the existing identity.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-rest), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-update?view=graph-rest-1.0).

## LAB01-Q29 — B

Owners manage a group according to directory policy, while members receive access or app behavior associated with membership. One relationship does not imply the other.

- A: Owner status does not universally create direct or transitive membership.
- B: Correct. Validate owners and members independently.
- C: Microsoft Entra supports group owners who are not direct members.
- D: Changing an owner does not alter mail or group-type properties.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q30 — C

Display names can be duplicated or changed. A run manifest should record the returned object ID and cleanup should verify that exact object before deletion.

- A: Portal list ordering is not a stable identity or automation input.
- B: Microsoft Entra groups are tenant objects and are not owned by an Azure subscription.
- C: Correct. Exact recorded object IDs provide the safest cleanup boundary.
- D: Prefix search results are ambiguous and can target an unrelated group.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q31 — D

The bootstrap password should be handled as a secret, omitted from state, and changed at the user's first sign-in by setting forceChangePasswordNextSignIn.

- A: Group descriptions are visible directory data and must never hold passwords.
- B: Disabling expiration does not replace the temporary bootstrap secret.
- C: Password reuse is unsafe and deleting history does not correct the design.
- D: Correct. The setting forces replacement of the temporary password at first sign-in.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q32 — A

The az ad group member command group manages Microsoft Entra group membership, and member add accepts the group and member object IDs.

- A: Correct. This adds the recorded directory object as a direct member.
- B: Azure role assignments grant resource access; they do not edit directory membership.
- C: az ad user update does not expose a group-membership parameter.
- D: az group manages Azure resource groups, not Microsoft Entra groups.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q33 — B

Azure CLI can authenticate an az rest request to Microsoft Graph. PATCHing the exact user object exposes writable properties not offered by a simplified command.

- A: Creating duplicates introduces drift and does not manage the existing identity.
- B: Correct. Microsoft Graph is the appropriate supported property-management surface.
- C: Credential caches must not be edited and a show operation is read-only.
- D: Azure subscription metadata has no relationship to Microsoft Entra user properties.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-rest), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-update?view=graph-rest-1.0).

## LAB01-Q34 — C

Owners manage a group according to directory policy, while members receive access or app behavior associated with membership. One relationship does not imply the other.

- A: Changing an owner does not alter mail or group-type properties.
- B: Owner status does not universally create direct or transitive membership.
- C: Correct. Validate owners and members independently.
- D: Microsoft Entra supports group owners who are not direct members.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q35 — D

Display names can be duplicated or changed. A run manifest should record the returned object ID and cleanup should verify that exact object before deletion.

- A: Prefix search results are ambiguous and can target an unrelated group.
- B: Portal list ordering is not a stable identity or automation input.
- C: Microsoft Entra groups are tenant objects and are not owned by an Azure subscription.
- D: Correct. Exact recorded object IDs provide the safest cleanup boundary.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q36 — A

The bootstrap password should be handled as a secret, omitted from state, and changed at the user's first sign-in by setting forceChangePasswordNextSignIn.

- A: Correct. The setting forces replacement of the temporary password at first sign-in.
- B: Group descriptions are visible directory data and must never hold passwords.
- C: Disabling expiration does not replace the temporary bootstrap secret.
- D: Password reuse is unsafe and deleting history does not correct the design.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

## LAB01-Q37 — B

The az ad group member command group manages Microsoft Entra group membership, and member add accepts the group and member object IDs.

- A: az group manages Azure resource groups, not Microsoft Entra groups.
- B: Correct. This adds the recorded directory object as a direct member.
- C: Azure role assignments grant resource access; they do not edit directory membership.
- D: az ad user update does not expose a group-membership parameter.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q38 — C

Azure CLI can authenticate an az rest request to Microsoft Graph. PATCHing the exact user object exposes writable properties not offered by a simplified command.

- A: Azure subscription metadata has no relationship to Microsoft Entra user properties.
- B: Creating duplicates introduces drift and does not manage the existing identity.
- C: Correct. Microsoft Graph is the appropriate supported property-management surface.
- D: Credential caches must not be edited and a show operation is read-only.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-rest), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/user-update?view=graph-rest-1.0).

## LAB01-Q39 — D

Owners manage a group according to directory policy, while members receive access or app behavior associated with membership. One relationship does not imply the other.

- A: Microsoft Entra supports group owners who are not direct members.
- B: Changing an owner does not alter mail or group-type properties.
- C: Owner status does not universally create direct or transitive membership.
- D: Correct. Validate owners and members independently.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest).

## LAB01-Q40 — A

Display names can be duplicated or changed. A run manifest should record the returned object ID and cleanup should verify that exact object before deletion.

- A: Correct. Exact recorded object IDs provide the safest cleanup boundary.
- B: Prefix search results are ambiguous and can target an unrelated group.
- C: Portal list ordering is not a stable identity or automation input.
- D: Microsoft Entra groups are tenant objects and are not owned by an Azure subscription.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

## LAB01-Q41 — B

Microsoft Entra normally soft-deletes users so they can be restored during a retention window. Permanent deletion is a separate, irreversible operation with its own authorization needs.

- A: The presence of recoverable deleted users is expected lifecycle behavior, not proof of failure.
- B: Correct. Audit active-object cleanup separately from deleted-item retention.
- C: Deletion does not transform a member user into a B2B guest.
- D: Microsoft Entra users are tenant objects and are not removed by deleting a subscription.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/directory-deleteditems-delete?view=graph-rest-1.0).

## LAB01-Q42 — C

The design has a positive membership assertion and a negative membership control while ownership is validated separately. Together they detect missing access and unintended expansion.

- A: Object existence alone does not prove the required relationships.
- B: Automatic repair would destroy the negative control and broaden access.
- C: Correct. Independent positive, negative, and ownership checks prove the intended relationship model.
- D: A naming convention cannot establish membership or ownership state.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest).

## LAB01-Q43 — D

Microsoft Entra normally soft-deletes users so they can be restored during a retention window. Permanent deletion is a separate, irreversible operation with its own authorization needs.

- A: Deletion does not transform a member user into a B2B guest.
- B: Microsoft Entra users are tenant objects and are not removed by deleting a subscription.
- C: The presence of recoverable deleted users is expected lifecycle behavior, not proof of failure.
- D: Correct. Audit active-object cleanup separately from deleted-item retention.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/directory-deleteditems-delete?view=graph-rest-1.0).

## LAB01-Q44 — A

The design has a positive membership assertion and a negative membership control while ownership is validated separately. Together they detect missing access and unintended expansion.

- A: Correct. Independent positive, negative, and ownership checks prove the intended relationship model.
- B: A naming convention cannot establish membership or ownership state.
- C: Object existence alone does not prove the required relationships.
- D: Automatic repair would destroy the negative control and broaden access.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest).

## LAB01-Q45 — B

Microsoft Entra normally soft-deletes users so they can be restored during a retention window. Permanent deletion is a separate, irreversible operation with its own authorization needs.

- A: The presence of recoverable deleted users is expected lifecycle behavior, not proof of failure.
- B: Correct. Audit active-object cleanup separately from deleted-item retention.
- C: Deletion does not transform a member user into a B2B guest.
- D: Microsoft Entra users are tenant objects and are not removed by deleting a subscription.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/directory-deleteditems-delete?view=graph-rest-1.0).

## LAB01-Q46 — C

The design has a positive membership assertion and a negative membership control while ownership is validated separately. Together they detect missing access and unintended expansion.

- A: Object existence alone does not prove the required relationships.
- B: Automatic repair would destroy the negative control and broaden access.
- C: Correct. Independent positive, negative, and ownership checks prove the intended relationship model.
- D: A naming convention cannot establish membership or ownership state.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest).

## LAB01-Q47 — D

Microsoft Entra normally soft-deletes users so they can be restored during a retention window. Permanent deletion is a separate, irreversible operation with its own authorization needs.

- A: Deletion does not transform a member user into a B2B guest.
- B: Microsoft Entra users are tenant objects and are not removed by deleting a subscription.
- C: The presence of recoverable deleted users is expected lifecycle behavior, not proof of failure.
- D: Correct. Audit active-object cleanup separately from deleted-item retention.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/directory-deleteditems-delete?view=graph-rest-1.0).

## LAB01-Q48 — A

The design has a positive membership assertion and a negative membership control while ownership is validated separately. Together they detect missing access and unintended expansion.

- A: Correct. Independent positive, negative, and ownership checks prove the intended relationship model.
- B: A naming convention cannot establish membership or ownership state.
- C: Object existence alone does not prove the required relationships.
- D: Automatic repair would destroy the negative control and broaden access.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest).

## LAB01-Q49 — B

Microsoft Entra normally soft-deletes users so they can be restored during a retention window. Permanent deletion is a separate, irreversible operation with its own authorization needs.

- A: The presence of recoverable deleted users is expected lifecycle behavior, not proof of failure.
- B: Correct. Audit active-object cleanup separately from deleted-item retention.
- C: Deletion does not transform a member user into a B2B guest.
- D: Microsoft Entra users are tenant objects and are not removed by deleting a subscription.

Objectives: `IG-USERS-01`, `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore), [Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/directory-deleteditems-delete?view=graph-rest-1.0).

## LAB01-Q50 — C

The design has a positive membership assertion and a negative membership control while ownership is validated separately. Together they detect missing access and unintended expansion.

- A: Object existence alone does not prove the required relationships.
- B: Automatic repair would destroy the negative control and broaden access.
- C: Correct. Independent positive, negative, and ownership checks prove the intended relationship model.
- D: A naming convention cannot establish membership or ownership state.

Objectives: `IG-USERS-02`.

Official sources: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest), [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest).
