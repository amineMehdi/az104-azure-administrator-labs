# Lab 03 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB03-Q01 — D

**Question:** The least-privilege workload delegation acceptance criteria require operators to separate a role's permissions from the principal and scope that receive them. Which service fact supports that requirement?

- **A — Incorrect.** Reader can view control-plane resources but cannot change them or automatically read protected data-plane content.
  Reader can view control-plane resources but cannot change them or automatically read protected data-plane content. In the least-privilege workload delegation, this statement describes Reader role. Least-privilege workload delegation asks about role definitions and assignments; this Reader role choice leaves the role definitions and assignments explanation missing.
- **B — Incorrect.** Least privilege chooses the narrowest role whose actions satisfy the required work.
  Least privilege chooses the narrowest role whose actions satisfy the required work. In the least-privilege workload delegation, this statement describes least-privilege role selection. The least-privilege role selection statement accurately describes least-privilege role selection; however, least-privilege workload delegation needs role definitions and assignments to separate a role's permissions from the principal and scope that receive them; least-privilege role selection cannot replace role definitions and assignments.
- **C — Incorrect.** Assigning a role to a group lets eligible members receive access through group membership.
  Assigning a role to a group lets eligible members receive access through group membership. In the least-privilege workload delegation, this statement describes group-based role assignment. Selecting group-based role assignment for least-privilege workload delegation leaves role definitions and assignments unanswered in least-privilege workload delegation; the least-privilege workload delegation lacks a role definitions and assignments basis to separate a role's permissions from the principal and scope that receive them.
- **D — Correct.** A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope.
  A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope. For least-privilege workload delegation, role definitions and assignments supplies the service rule needed to separate a role's permissions from the principal and scope that receive them.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand Azure role definitions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions)

**Source reviewed:** 2026-08-31

## LAB03-Q02 — B

**Question:** An access delegation reviewer challenges whether the least-privilege workload delegation can let an auditor inspect configuration without changing it. Which response resolves the concern?

- **A — Incorrect.** Contributor can manage resources but cannot grant Azure RBAC access to other principals.
  Contributor can manage resources but cannot grant Azure RBAC access to other principals. In the least-privilege workload delegation, this statement describes Contributor role. The Contributor role statement accurately describes Contributor role; however, least-privilege workload delegation needs Reader role to let an auditor inspect configuration without changing it; Contributor role cannot replace Reader role.
- **B — Correct.** Reader can view control-plane resources but cannot change them or automatically read protected data-plane content.
  Reader can view control-plane resources but cannot change them or automatically read protected data-plane content. In the least-privilege workload delegation, this Reader role rule supports the need to let an auditor inspect configuration without changing it.
- **C — Incorrect.** An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access.
  An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access. In the least-privilege workload delegation, this statement describes scope inheritance. Reader role governs least-privilege workload delegation; scope inheritance cannot support Reader role when operators must let an auditor inspect configuration without changing it.
- **D — Incorrect.** Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes.
  Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes. In the least-privilege workload delegation, this statement describes effective access interpretation. Least-privilege workload delegation asks about Reader role; this effective access interpretation choice leaves the Reader role explanation missing.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q03 — A

**Question:** The least-privilege workload delegation handoff omits the access delegation rule needed to let an operator manage resources without granting access to other principals. Which statement should the team add?

- **A — Correct.** Contributor can manage resources but cannot grant Azure RBAC access to other principals.
  For the least-privilege workload delegation, the rule for Contributor role is defined by this statement: contributor can manage resources but cannot grant Azure RBAC access to other principals. It supports the required outcome to let an operator manage resources without granting access to other principals.
- **B — Incorrect.** User Access Administrator manages access assignments without granting general resource-management permissions.
  User Access Administrator manages access assignments without granting general resource-management permissions. In the least-privilege workload delegation, this statement describes User Access Administrator role. Contributor role governs least-privilege workload delegation; User Access Administrator role cannot support Contributor role when operators must let an operator manage resources without granting access to other principals.
- **C — Incorrect.** A resource-level role assignment limits the authorization boundary to one resource.
  A resource-level role assignment limits the authorization boundary to one resource. In the least-privilege workload delegation, this statement describes resource-level assignments. Least-privilege workload delegation asks about Contributor role; this resource-level assignments choice leaves the Contributor role explanation missing.
- **D — Incorrect.** A deny assignment can block an operation even when a role assignment otherwise allows that action.
  A deny assignment can block an operation even when a role assignment otherwise allows that action. In the least-privilege workload delegation, this statement describes deny assignments. The deny assignments statement accurately describes deny assignments; however, least-privilege workload delegation needs Contributor role to let an operator manage resources without granting access to other principals; deny assignments cannot replace Contributor role.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q04 — D

**Question:** An access delegation incident review of the least-privilege workload delegation depends on the ability to delegate role-assignment administration without granting broad resource changes. Which platform description is reliable?

- **A — Incorrect.** Least privilege chooses the narrowest role whose actions satisfy the required work.
  Least privilege chooses the narrowest role whose actions satisfy the required work. In the least-privilege workload delegation, this statement describes least-privilege role selection. User Access Administrator role governs least-privilege workload delegation; least-privilege role selection cannot support User Access Administrator role when operators must delegate role-assignment administration without granting broad resource changes.
- **B — Incorrect.** Assigning a role to a group lets eligible members receive access through group membership.
  Assigning a role to a group lets eligible members receive access through group membership. In the least-privilege workload delegation, this statement describes group-based role assignment. Least-privilege workload delegation asks about User Access Administrator role; this group-based role assignment choice leaves the User Access Administrator role explanation missing.
- **C — Incorrect.** A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope.
  A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope. In the least-privilege workload delegation, this statement describes role definitions and assignments. The role definitions and assignments statement accurately describes role definitions and assignments; however, least-privilege workload delegation needs User Access Administrator role to delegate role-assignment administration without granting broad resource changes; role definitions and assignments cannot replace User Access Administrator role.
- **D — Correct.** User Access Administrator manages access assignments without granting general resource-management permissions.
  User Access Administrator manages access assignments without granting general resource-management permissions. The least-privilege workload delegation applies that User Access Administrator role boundary when operators must delegate role-assignment administration without granting broad resource changes.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [Azure built-in privileged roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged)

**Source reviewed:** 2026-08-31

## LAB03-Q05 — C

**Question:** A platform administrator granting least-privilege access to a workload team is updating the access delegation runbook. The requirement is to grant only the permissions and scope needed for the stated job. Which statement describes Azure behavior correctly?

- **A — Incorrect.** An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access.
  An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access. In the least-privilege workload delegation, this statement describes scope inheritance. Least-privilege workload delegation asks about least-privilege role selection; this scope inheritance choice leaves the least-privilege role selection explanation missing.
- **B — Incorrect.** Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes.
  Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes. In the least-privilege workload delegation, this statement describes effective access interpretation. The effective access interpretation statement accurately describes effective access interpretation; however, least-privilege workload delegation needs least-privilege role selection to grant only the permissions and scope needed for the stated job; effective access interpretation cannot replace least-privilege role selection.
- **C — Correct.** Least privilege chooses the narrowest role whose actions satisfy the required work.
  The least-privilege workload delegation needs least-privilege role selection to grant only the permissions and scope needed for the stated job; this option states the applicable least-privilege role selection rule: least privilege chooses the narrowest role whose actions satisfy the required work.
- **D — Incorrect.** Reader can view control-plane resources but cannot change them or automatically read protected data-plane content.
  Reader can view control-plane resources but cannot change them or automatically read protected data-plane content. In the least-privilege workload delegation, this statement describes Reader role. Least-privilege role selection governs least-privilege workload delegation; Reader role cannot support least-privilege role selection when operators must grant only the permissions and scope needed for the stated job.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices)

**Source reviewed:** 2026-08-31

## LAB03-Q06 — A

**Question:** An access delegation peer review asks how the least-privilege workload delegation should handle this outcome: predict access inherited from a parent management boundary. Which explanation is accurate?

- **A — Correct.** An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access.
  An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access. This scope inheritance fact resolves the least-privilege workload delegation design question about how to predict access inherited from a parent management boundary.
- **B — Incorrect.** A resource-level role assignment limits the authorization boundary to one resource.
  A resource-level role assignment limits the authorization boundary to one resource. In the least-privilege workload delegation, this statement describes resource-level assignments. Selecting resource-level assignments for least-privilege workload delegation leaves scope inheritance unanswered in least-privilege workload delegation; the least-privilege workload delegation lacks a scope inheritance basis to predict access inherited from a parent management boundary.
- **C — Incorrect.** A deny assignment can block an operation even when a role assignment otherwise allows that action.
  A deny assignment can block an operation even when a role assignment otherwise allows that action. In the least-privilege workload delegation, this statement describes deny assignments. Scope inheritance governs least-privilege workload delegation; deny assignments cannot support scope inheritance when operators must predict access inherited from a parent management boundary.
- **D — Incorrect.** Contributor can manage resources but cannot grant Azure RBAC access to other principals.
  Contributor can manage resources but cannot grant Azure RBAC access to other principals. In the least-privilege workload delegation, this statement describes Contributor role. Least-privilege workload delegation asks about scope inheritance; this Contributor role choice leaves the scope inheritance explanation missing.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q07 — A

**Question:** For the least-privilege workload delegation, the access delegation plan must limit an assignment to one named resource. Which statement about access delegation belongs in the least-privilege workload delegation record?

- **A — Correct.** A resource-level role assignment limits the authorization boundary to one resource.
  A resource-level role assignment limits the authorization boundary to one resource. For least-privilege workload delegation, resource-level assignments supplies the service rule needed to limit an assignment to one named resource.
- **B — Incorrect.** Assigning a role to a group lets eligible members receive access through group membership.
  Assigning a role to a group lets eligible members receive access through group membership. In the least-privilege workload delegation, this statement describes group-based role assignment. Resource-level assignments governs least-privilege workload delegation; group-based role assignment cannot support resource-level assignments when operators must limit an assignment to one named resource.
- **C — Incorrect.** A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope.
  A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope. In the least-privilege workload delegation, this statement describes role definitions and assignments. Least-privilege workload delegation asks about resource-level assignments; this role definitions and assignments choice leaves the resource-level assignments explanation missing.
- **D — Incorrect.** User Access Administrator manages access assignments without granting general resource-management permissions.
  User Access Administrator manages access assignments without granting general resource-management permissions. In the least-privilege workload delegation, this statement describes User Access Administrator role. The User Access Administrator role statement accurately describes User Access Administrator role; however, least-privilege workload delegation needs resource-level assignments to limit an assignment to one named resource; User Access Administrator role cannot replace resource-level assignments.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q08 — C

**Question:** The access delegation review compares four claims for the least-privilege workload delegation requirement to delegate the same access to a team through one directory group. Which claim is technically sound?

- **A — Incorrect.** Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes.
  Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes. In the least-privilege workload delegation, this statement describes effective access interpretation. Group-based role assignment governs least-privilege workload delegation; effective access interpretation cannot support group-based role assignment when operators must delegate the same access to a team through one directory group.
- **B — Incorrect.** Reader can view control-plane resources but cannot change them or automatically read protected data-plane content.
  Reader can view control-plane resources but cannot change them or automatically read protected data-plane content. In the least-privilege workload delegation, this statement describes Reader role. Least-privilege workload delegation asks about group-based role assignment; this Reader role choice leaves the group-based role assignment explanation missing.
- **C — Correct.** Assigning a role to a group lets eligible members receive access through group membership.
  Assigning a role to a group lets eligible members receive access through group membership. In the least-privilege workload delegation, this group-based role assignment rule supports the need to delegate the same access to a team through one directory group.
- **D — Incorrect.** Least privilege chooses the narrowest role whose actions satisfy the required work.
  Least privilege chooses the narrowest role whose actions satisfy the required work. In the least-privilege workload delegation, this statement describes least-privilege role selection. Selecting least-privilege role selection for least-privilege workload delegation leaves group-based role assignment unanswered in least-privilege workload delegation; the least-privilege workload delegation lacks a group-based role assignment basis to delegate the same access to a team through one directory group.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Assign Azure roles using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q09 — B

**Question:** The access delegation architecture note requires the least-privilege workload delegation environment to explain a principal's final permissions after all applicable assignments are combined. Which statement defines the relevant access delegation boundary?

- **A — Incorrect.** A deny assignment can block an operation even when a role assignment otherwise allows that action.
  A deny assignment can block an operation even when a role assignment otherwise allows that action. In the least-privilege workload delegation, this statement describes deny assignments. Least-privilege workload delegation asks about effective access interpretation; this deny assignments choice leaves the effective access interpretation explanation missing.
- **B — Correct.** Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes.
  For the least-privilege workload delegation, the rule for effective access interpretation is defined by this statement: effective access combines direct assignments, group assignments, and assignments inherited from parent scopes. It supports the required outcome to explain a principal's final permissions after all applicable assignments are combined.
- **C — Incorrect.** Contributor can manage resources but cannot grant Azure RBAC access to other principals.
  Contributor can manage resources but cannot grant Azure RBAC access to other principals. In the least-privilege workload delegation, this statement describes Contributor role. Selecting Contributor role for least-privilege workload delegation leaves effective access interpretation unanswered in least-privilege workload delegation; the least-privilege workload delegation lacks a effective access interpretation basis to explain a principal's final permissions after all applicable assignments are combined.
- **D — Incorrect.** An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access.
  An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access. In the least-privilege workload delegation, this statement describes scope inheritance. Effective access interpretation governs least-privilege workload delegation; scope inheritance cannot support effective access interpretation when operators must explain a principal's final permissions after all applicable assignments are combined.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [List Azure role assignments using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q10 — B

**Question:** A new access delegation operator must explain why the least-privilege workload delegation can explain why an allow assignment does not overcome an explicit platform block. Which explanation is accurate?

- **A — Incorrect.** A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope.
  A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope. In the least-privilege workload delegation, this statement describes role definitions and assignments. The role definitions and assignments statement accurately describes role definitions and assignments; however, least-privilege workload delegation needs deny assignments to explain why an allow assignment does not overcome an explicit platform block; role definitions and assignments cannot replace deny assignments.
- **B — Correct.** A deny assignment can block an operation even when a role assignment otherwise allows that action.
  A deny assignment can block an operation even when a role assignment otherwise allows that action. The least-privilege workload delegation applies that deny assignments boundary when operators must explain why an allow assignment does not overcome an explicit platform block.
- **C — Incorrect.** User Access Administrator manages access assignments without granting general resource-management permissions.
  User Access Administrator manages access assignments without granting general resource-management permissions. In the least-privilege workload delegation, this statement describes User Access Administrator role. Deny assignments governs least-privilege workload delegation; User Access Administrator role cannot support deny assignments when operators must explain why an allow assignment does not overcome an explicit platform block.
- **D — Incorrect.** A resource-level role assignment limits the authorization boundary to one resource.
  A resource-level role assignment limits the authorization boundary to one resource. In the least-privilege workload delegation, this statement describes resource-level assignments. Least-privilege workload delegation asks about deny assignments; this resource-level assignments choice leaves the deny assignments explanation missing.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Understand Azure deny assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/deny-assignments)

**Source reviewed:** 2026-08-31

## LAB03-Q11 — A

**Question:** A least-privilege workload delegation review finds access delegation drift from the need to separate a role's permissions from the principal and scope that receive them. Which correction addresses that drift?

- **A — Correct.** Select a built-in role definition and create a separate assignment for the intended principal and scope.
  The least-privilege workload delegation must separate a role's permissions from the principal and scope that receive them; this option performs its direct role definitions and assignments change: select a built-in role definition and create a separate assignment for the intended principal and scope.
- **B — Incorrect.** Assign Contributor for resource administration that excludes access delegation.
  Assign Contributor for resource administration that excludes access delegation. In the least-privilege workload delegation, this action changes Contributor role. Least-privilege workload delegation requires role definitions and assignments; changing Contributor role leaves role definitions and assignments absent in least-privilege workload delegation; least-privilege workload delegation cannot separate a role's permissions from the principal and scope that receive them.
- **C — Incorrect.** Place an assignment at the common parent only when every child should inherit it.
  Place an assignment at the common parent only when every child should inherit it. In the least-privilege workload delegation, this action changes scope inheritance. Scope inheritance does not implement role definitions and assignments for least-privilege workload delegation; the least-privilege workload delegation still cannot separate a role's permissions from the principal and scope that receive them.
- **D — Incorrect.** Enumerate all assignments for the principal with inheritance and group expansion considered.
  Enumerate all assignments for the principal with inheritance and group expansion considered. In the least-privilege workload delegation, this action changes effective access interpretation. Least-privilege workload delegation instead needs role definitions and assignments: Select a built-in role definition and create a separate assignment for the intended principal and scope. The effective access interpretation action omits that role definitions and assignments work.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand Azure role definitions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions)

**Source reviewed:** 2026-08-31

## LAB03-Q12 — B

**Question:** The least-privilege workload delegation window permits only the access delegation change needed to let an auditor inspect configuration without changing it. Which option respects the boundary?

- **A — Incorrect.** Use User Access Administrator at the narrowest scope that needs delegated RBAC management.
  Use User Access Administrator at the narrowest scope that needs delegated RBAC management. In the least-privilege workload delegation, this action changes User Access Administrator role. Least-privilege workload delegation requires Reader role; changing User Access Administrator role leaves Reader role absent in least-privilege workload delegation; least-privilege workload delegation cannot let an auditor inspect configuration without changing it.
- **B — Correct.** Assign Reader when a principal needs observation without resource modification.
  Assign Reader when a principal needs observation without resource modification. It is the least-change Reader role path for the least-privilege workload delegation requirement to let an auditor inspect configuration without changing it.
- **C — Incorrect.** Assign the required role directly on the single resource when broader inheritance is unnecessary.
  Assign the required role directly on the single resource when broader inheritance is unnecessary. In the least-privilege workload delegation, this action changes resource-level assignments. Least-privilege workload delegation instead needs Reader role: Assign Reader when a principal needs observation without resource modification. The resource-level assignments action omits that Reader role work.
- **D — Incorrect.** Inspect applicable deny assignments when an apparently authorized action is rejected.
  Inspect applicable deny assignments when an apparently authorized action is rejected. In the least-privilege workload delegation, this action changes deny assignments. Least-privilege workload delegation approved Reader role, not deny assignments; only the Reader role change can let an auditor inspect configuration without changing it.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q13 — D

**Question:** The access delegation preflight has passed; the least-privilege workload delegation must now let an operator manage resources without granting access to other principals. Which operation should run?

- **A — Incorrect.** Compare required operations with built-in role actions before creating an assignment.
  Compare required operations with built-in role actions before creating an assignment. In the least-privilege workload delegation, this action changes least-privilege role selection. Least-privilege role selection does not implement Contributor role for least-privilege workload delegation; the least-privilege workload delegation still cannot let an operator manage resources without granting access to other principals.
- **B — Incorrect.** Bind the role to the group's object ID and manage authorized users through membership.
  Bind the role to the group's object ID and manage authorized users through membership. In the least-privilege workload delegation, this action changes group-based role assignment. Least-privilege workload delegation instead needs Contributor role: Assign Contributor for resource administration that excludes access delegation. The group-based role assignment action omits that Contributor role work.
- **C — Incorrect.** Select a built-in role definition and create a separate assignment for the intended principal and scope.
  Select a built-in role definition and create a separate assignment for the intended principal and scope. In the least-privilege workload delegation, this action changes role definitions and assignments. Least-privilege workload delegation approved Contributor role, not role definitions and assignments; only the Contributor role change can let an operator manage resources without granting access to other principals.
- **D — Correct.** Assign Contributor for resource administration that excludes access delegation.
  Assign Contributor for resource administration that excludes access delegation. In least-privilege workload delegation, applying Contributor role is the scoped way to let an operator manage resources without granting access to other principals.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q14 — B

**Question:** The least-privilege workload delegation plan must delegate role-assignment administration without granting broad resource changes while limiting the mutation scope to access delegation. Which action is appropriate?

- **A — Incorrect.** Place an assignment at the common parent only when every child should inherit it.
  Place an assignment at the common parent only when every child should inherit it. In the least-privilege workload delegation, this action changes scope inheritance. Least-privilege workload delegation instead needs User Access Administrator role: Use User Access Administrator at the narrowest scope that needs delegated RBAC management. The scope inheritance action omits that User Access Administrator role work.
- **B — Correct.** Use User Access Administrator at the narrowest scope that needs delegated RBAC management.
  Use User Access Administrator at the narrowest scope that needs delegated RBAC management. The least-privilege workload delegation uses this User Access Administrator role operation to delegate role-assignment administration without granting broad resource changes within the approved scope.
- **C — Incorrect.** Enumerate all assignments for the principal with inheritance and group expansion considered.
  Enumerate all assignments for the principal with inheritance and group expansion considered. In the least-privilege workload delegation, this action changes effective access interpretation. Least-privilege workload delegation requires User Access Administrator role; changing effective access interpretation leaves User Access Administrator role absent in least-privilege workload delegation; least-privilege workload delegation cannot delegate role-assignment administration without granting broad resource changes.
- **D — Incorrect.** Assign Reader when a principal needs observation without resource modification.
  Assign Reader when a principal needs observation without resource modification. In the least-privilege workload delegation, this action changes Reader role. Reader role does not implement User Access Administrator role for least-privilege workload delegation; the least-privilege workload delegation still cannot delegate role-assignment administration without granting broad resource changes.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [Azure built-in privileged roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged)

**Source reviewed:** 2026-08-31

## LAB03-Q15 — A

**Question:** An access delegation ticket in the least-privilege workload delegation says to grant only the permissions and scope needed for the stated job. Which access delegation action completes the least-privilege workload delegation request with minimal change?

- **A — Correct.** Compare required operations with built-in role actions before creating an assignment.
  For the least-privilege workload delegation, the required least-privilege role selection action is: compare required operations with built-in role actions before creating an assignment. It makes the environment able to grant only the permissions and scope needed for the stated job.
- **B — Incorrect.** Assign the required role directly on the single resource when broader inheritance is unnecessary.
  Assign the required role directly on the single resource when broader inheritance is unnecessary. In the least-privilege workload delegation, this action changes resource-level assignments. Least-privilege workload delegation requires least-privilege role selection; changing resource-level assignments leaves least-privilege role selection absent in least-privilege workload delegation; least-privilege workload delegation cannot grant only the permissions and scope needed for the stated job.
- **C — Incorrect.** Inspect applicable deny assignments when an apparently authorized action is rejected.
  Inspect applicable deny assignments when an apparently authorized action is rejected. In the least-privilege workload delegation, this action changes deny assignments. Deny assignments does not implement least-privilege role selection for least-privilege workload delegation; the least-privilege workload delegation still cannot grant only the permissions and scope needed for the stated job.
- **D — Incorrect.** Assign Contributor for resource administration that excludes access delegation.
  Assign Contributor for resource administration that excludes access delegation. In the least-privilege workload delegation, this action changes Contributor role. Least-privilege workload delegation instead needs least-privilege role selection: Compare required operations with built-in role actions before creating an assignment. The Contributor role action omits that least-privilege role selection work.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices)

**Source reviewed:** 2026-08-31

## LAB03-Q16 — B

**Question:** The approach for the least-privilege workload delegation is approved, but the access delegation environment still cannot predict access inherited from a parent management boundary. Which implementation step closes the gap?

- **A — Incorrect.** Bind the role to the group's object ID and manage authorized users through membership.
  Bind the role to the group's object ID and manage authorized users through membership. In the least-privilege workload delegation, this action changes group-based role assignment. Least-privilege workload delegation requires scope inheritance; changing group-based role assignment leaves scope inheritance absent in least-privilege workload delegation; least-privilege workload delegation cannot predict access inherited from a parent management boundary.
- **B — Correct.** Place an assignment at the common parent only when every child should inherit it.
  Place an assignment at the common parent only when every child should inherit it. This changes scope inheritance in the least-privilege workload delegation, supplying the missing state needed to predict access inherited from a parent management boundary.
- **C — Incorrect.** Select a built-in role definition and create a separate assignment for the intended principal and scope.
  Select a built-in role definition and create a separate assignment for the intended principal and scope. In the least-privilege workload delegation, this action changes role definitions and assignments. Least-privilege workload delegation instead needs scope inheritance: Place an assignment at the common parent only when every child should inherit it. The role definitions and assignments action omits that scope inheritance work.
- **D — Incorrect.** Use User Access Administrator at the narrowest scope that needs delegated RBAC management.
  Use User Access Administrator at the narrowest scope that needs delegated RBAC management. In the least-privilege workload delegation, this action changes User Access Administrator role. Least-privilege workload delegation approved scope inheritance, not User Access Administrator role; only the scope inheritance change can predict access inherited from a parent management boundary.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q17 — D

**Question:** The platform administrator granting least-privilege access to a workload team may change the least-privilege workload delegation only to limit an assignment to one named resource. Which access delegation action stays within that assignment?

- **A — Incorrect.** Enumerate all assignments for the principal with inheritance and group expansion considered.
  Enumerate all assignments for the principal with inheritance and group expansion considered. In the least-privilege workload delegation, this action changes effective access interpretation. Effective access interpretation does not implement resource-level assignments for least-privilege workload delegation; the least-privilege workload delegation still cannot limit an assignment to one named resource.
- **B — Incorrect.** Assign Reader when a principal needs observation without resource modification.
  Assign Reader when a principal needs observation without resource modification. In the least-privilege workload delegation, this action changes Reader role. Least-privilege workload delegation instead needs resource-level assignments: Assign the required role directly on the single resource when broader inheritance is unnecessary. The Reader role action omits that resource-level assignments work.
- **C — Incorrect.** Compare required operations with built-in role actions before creating an assignment.
  Compare required operations with built-in role actions before creating an assignment. In the least-privilege workload delegation, this action changes least-privilege role selection. Least-privilege workload delegation approved resource-level assignments, not least-privilege role selection; only the resource-level assignments change can limit an assignment to one named resource.
- **D — Correct.** Assign the required role directly on the single resource when broader inheritance is unnecessary.
  The least-privilege workload delegation must limit an assignment to one named resource; this option performs its direct resource-level assignments change: assign the required role directly on the single resource when broader inheritance is unnecessary.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q18 — D

**Question:** An access delegation dry run shows no least-privilege workload delegation command will delegate the same access to a team through one directory group. Which action belongs before execution?

- **A — Incorrect.** Inspect applicable deny assignments when an apparently authorized action is rejected.
  Inspect applicable deny assignments when an apparently authorized action is rejected. In the least-privilege workload delegation, this action changes deny assignments. Least-privilege workload delegation instead needs group-based role assignment: Bind the role to the group's object ID and manage authorized users through membership. The deny assignments action omits that group-based role assignment work.
- **B — Incorrect.** Assign Contributor for resource administration that excludes access delegation.
  Assign Contributor for resource administration that excludes access delegation. In the least-privilege workload delegation, this action changes Contributor role. Least-privilege workload delegation approved group-based role assignment, not Contributor role; only the group-based role assignment change can delegate the same access to a team through one directory group.
- **C — Incorrect.** Place an assignment at the common parent only when every child should inherit it.
  Place an assignment at the common parent only when every child should inherit it. In the least-privilege workload delegation, this action changes scope inheritance. Least-privilege workload delegation requires group-based role assignment; changing scope inheritance leaves group-based role assignment absent in least-privilege workload delegation; least-privilege workload delegation cannot delegate the same access to a team through one directory group.
- **D — Correct.** Bind the role to the group's object ID and manage authorized users through membership.
  Bind the role to the group's object ID and manage authorized users through membership. It is the least-change group-based role assignment path for the least-privilege workload delegation requirement to delegate the same access to a team through one directory group.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Assign Azure roles using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q19 — D

**Question:** For the least-privilege workload delegation, operators need to explain a principal's final permissions after all applicable assignments are combined. Which change realizes that requirement?

- **A — Incorrect.** Select a built-in role definition and create a separate assignment for the intended principal and scope.
  Select a built-in role definition and create a separate assignment for the intended principal and scope. In the least-privilege workload delegation, this action changes role definitions and assignments. Least-privilege workload delegation approved effective access interpretation, not role definitions and assignments; only the effective access interpretation change can explain a principal's final permissions after all applicable assignments are combined.
- **B — Incorrect.** Use User Access Administrator at the narrowest scope that needs delegated RBAC management.
  Use User Access Administrator at the narrowest scope that needs delegated RBAC management. In the least-privilege workload delegation, this action changes User Access Administrator role. Least-privilege workload delegation requires effective access interpretation; changing User Access Administrator role leaves effective access interpretation absent in least-privilege workload delegation; least-privilege workload delegation cannot explain a principal's final permissions after all applicable assignments are combined.
- **C — Incorrect.** Assign the required role directly on the single resource when broader inheritance is unnecessary.
  Assign the required role directly on the single resource when broader inheritance is unnecessary. In the least-privilege workload delegation, this action changes resource-level assignments. Resource-level assignments does not implement effective access interpretation for least-privilege workload delegation; the least-privilege workload delegation still cannot explain a principal's final permissions after all applicable assignments are combined.
- **D — Correct.** Enumerate all assignments for the principal with inheritance and group expansion considered.
  Enumerate all assignments for the principal with inheritance and group expansion considered. In least-privilege workload delegation, applying effective access interpretation is the scoped way to explain a principal's final permissions after all applicable assignments are combined.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [List Azure role assignments using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q20 — A

**Question:** Operators must automate the least-privilege workload delegation change needed to explain why an allow assignment does not overcome an explicit platform block. Which access delegation operation belongs in the runbook?

- **A — Correct.** Inspect applicable deny assignments when an apparently authorized action is rejected.
  Inspect applicable deny assignments when an apparently authorized action is rejected. The least-privilege workload delegation uses this deny assignments operation to explain why an allow assignment does not overcome an explicit platform block within the approved scope.
- **B — Incorrect.** Assign Reader when a principal needs observation without resource modification.
  Assign Reader when a principal needs observation without resource modification. In the least-privilege workload delegation, this action changes Reader role. Reader role does not implement deny assignments for least-privilege workload delegation; the least-privilege workload delegation still cannot explain why an allow assignment does not overcome an explicit platform block.
- **C — Incorrect.** Compare required operations with built-in role actions before creating an assignment.
  Compare required operations with built-in role actions before creating an assignment. In the least-privilege workload delegation, this action changes least-privilege role selection. Least-privilege workload delegation instead needs deny assignments: Inspect applicable deny assignments when an apparently authorized action is rejected. The least-privilege role selection action omits that deny assignments work.
- **D — Incorrect.** Bind the role to the group's object ID and manage authorized users through membership.
  Bind the role to the group's object ID and manage authorized users through membership. In the least-privilege workload delegation, this action changes group-based role assignment. Least-privilege workload delegation approved deny assignments, not group-based role assignment; only the deny assignments change can explain why an allow assignment does not overcome an explicit platform block.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Understand Azure deny assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/deny-assignments)

**Source reviewed:** 2026-08-31

## LAB03-Q21 — B

**Question:** The access delegation validation asks whether the least-privilege workload delegation can separate a role's permissions from the principal and scope that receive them. Which observable state is strongest?

- **A — Incorrect.** Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
  Confirm role-assignment operations succeed while unrelated resource updates remain outside the role. In the least-privilege workload delegation, this check observes User Access Administrator role. Least-privilege workload delegation output covers User Access Administrator role, not role definitions and assignments; the role definitions and assignments requirement to separate a role's permissions from the principal and scope that receive them remains unverified.
- **B — Correct.** Read the assignment and confirm its principal ID, role definition ID, and scope independently.
  For the least-privilege workload delegation, this role definitions and assignments observation is decisive: read the assignment and confirm its principal ID, role definition ID, and scope independently. It is least-privilege workload delegation evidence that operators can separate a role's permissions from the principal and scope that receive them.
- **C — Incorrect.** Query assignments at the resource and verify that the scope equals the resource ID.
  Query assignments at the resource and verify that the scope equals the resource ID. In the least-privilege workload delegation, this check observes resource-level assignments. Least-privilege workload delegation reads resource-level assignments, leaving role definitions and assignments unproved in least-privilege workload delegation; least-privilege workload delegation still has no role definitions and assignments proof.
- **D — Incorrect.** Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
  Query deny assignments at the target and parent scopes and compare their excluded principals and actions. In the least-privilege workload delegation, this check observes deny assignments. Least-privilege workload delegation could pass deny assignments while role definitions and assignments is wrong; least-privilege workload delegation still lacks role definitions and assignments proof.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand Azure role definitions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions)

**Source reviewed:** 2026-08-31

## LAB03-Q22 — B

**Question:** A least-privilege workload delegation review must prove the access delegation ability to let an auditor inspect configuration without changing it. Which check avoids an adjacent feature?

- **A — Incorrect.** Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
  Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access. In the least-privilege workload delegation, this check observes least-privilege role selection. Least-privilege role selection success in least-privilege workload delegation cannot verify Reader role; least-privilege workload delegation cannot let an auditor inspect configuration without changing it until Reader role evidence exists.
- **B — Correct.** List effective assignments and test a read operation separately from a write operation.
  List effective assignments and test a read operation separately from a write operation. Because the least-privilege workload delegation check observes Reader role, it independently verifies the requirement to let an auditor inspect configuration without changing it.
- **C — Incorrect.** Show both the group role assignment and the user's transitive membership in that group.
  Show both the group role assignment and the user's transitive membership in that group. In the least-privilege workload delegation, this check observes group-based role assignment. Least-privilege workload delegation could pass group-based role assignment while Reader role is wrong; least-privilege workload delegation still lacks Reader role proof.
- **D — Incorrect.** Read the assignment and confirm its principal ID, role definition ID, and scope independently.
  Read the assignment and confirm its principal ID, role definition ID, and scope independently. In the least-privilege workload delegation, this check observes role definitions and assignments. Least-privilege workload delegation output covers role definitions and assignments, not Reader role; the Reader role requirement to let an auditor inspect configuration without changing it remains unverified.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q23 — A

**Question:** The least-privilege workload delegation evidence bundle needs an access delegation result showing it can let an operator manage resources without granting access to other principals. Which result belongs in the checkpoint?

- **A — Correct.** Confirm resource writes succeed and role-assignment creation remains unauthorized.
  The least-privilege workload delegation validator needs this Contributor role result: confirm resource writes succeed and role-assignment creation remains unauthorized. It proves the outcome to let an operator manage resources without granting access to other principals rather than an adjacent checkpoint.
- **B — Incorrect.** List assignments with inherited entries at the target resource and identify the parent scope.
  List assignments with inherited entries at the target resource and identify the parent scope. In the least-privilege workload delegation, this check observes scope inheritance. Least-privilege workload delegation could pass scope inheritance while Contributor role is wrong; least-privilege workload delegation still lacks Contributor role proof.
- **C — Incorrect.** Compare direct and inherited assignment records and trace each role to its originating scope.
  Compare direct and inherited assignment records and trace each role to its originating scope. In the least-privilege workload delegation, this check observes effective access interpretation. Least-privilege workload delegation output covers effective access interpretation, not Contributor role; the Contributor role requirement to let an operator manage resources without granting access to other principals remains unverified.
- **D — Incorrect.** List effective assignments and test a read operation separately from a write operation.
  List effective assignments and test a read operation separately from a write operation. In the least-privilege workload delegation, this check observes Reader role. Reader role success in least-privilege workload delegation cannot verify Contributor role; least-privilege workload delegation cannot let an operator manage resources without granting access to other principals until Contributor role evidence exists.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q24 — A

**Question:** Before least-privilege workload delegation cleanup, the access delegation team must reconfirm it can delegate role-assignment administration without granting broad resource changes. Which read-only inspection should run?

- **A — Correct.** Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
  Confirm role-assignment operations succeed while unrelated resource updates remain outside the role. This is independent User Access Administrator role evidence for the least-privilege workload delegation, even if least-privilege workload delegation setup reports success before User Access Administrator role becomes observable.
- **B — Incorrect.** Query assignments at the resource and verify that the scope equals the resource ID.
  Query assignments at the resource and verify that the scope equals the resource ID. In the least-privilege workload delegation, this check observes resource-level assignments. Least-privilege workload delegation output covers resource-level assignments, not User Access Administrator role; the User Access Administrator role requirement to delegate role-assignment administration without granting broad resource changes remains unverified.
- **C — Incorrect.** Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
  Query deny assignments at the target and parent scopes and compare their excluded principals and actions. In the least-privilege workload delegation, this check observes deny assignments. Deny assignments success in least-privilege workload delegation cannot verify User Access Administrator role; least-privilege workload delegation cannot delegate role-assignment administration without granting broad resource changes until User Access Administrator role evidence exists.
- **D — Incorrect.** Confirm resource writes succeed and role-assignment creation remains unauthorized.
  Confirm resource writes succeed and role-assignment creation remains unauthorized. In the least-privilege workload delegation, this check observes Contributor role. Least-privilege workload delegation reads Contributor role, leaving User Access Administrator role unproved in least-privilege workload delegation; least-privilege workload delegation still has no User Access Administrator role proof.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [Azure built-in privileged roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged)

**Source reviewed:** 2026-08-31

## LAB03-Q25 — C

**Question:** The least-privilege workload delegation setup reports success after the access delegation attempt to grant only the permissions and scope needed for the stated job. Which access delegation read-only observation proves the least-privilege workload delegation outcome?

- **A — Incorrect.** Show both the group role assignment and the user's transitive membership in that group.
  Show both the group role assignment and the user's transitive membership in that group. In the least-privilege workload delegation, this check observes group-based role assignment. Least-privilege workload delegation output covers group-based role assignment, not least-privilege role selection; the least-privilege role selection requirement to grant only the permissions and scope needed for the stated job remains unverified.
- **B — Incorrect.** Read the assignment and confirm its principal ID, role definition ID, and scope independently.
  Read the assignment and confirm its principal ID, role definition ID, and scope independently. In the least-privilege workload delegation, this check observes role definitions and assignments. Role definitions and assignments success in least-privilege workload delegation cannot verify least-privilege role selection; least-privilege workload delegation cannot grant only the permissions and scope needed for the stated job until least-privilege role selection evidence exists.
- **C — Correct.** Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
  Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access. For least-privilege workload delegation, this least-privilege role selection read confirms the service can grant only the permissions and scope needed for the stated job.
- **D — Incorrect.** Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
  Confirm role-assignment operations succeed while unrelated resource updates remain outside the role. In the least-privilege workload delegation, this check observes User Access Administrator role. Least-privilege workload delegation could pass User Access Administrator role while least-privilege role selection is wrong; least-privilege workload delegation still lacks least-privilege role selection proof.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices)

**Source reviewed:** 2026-08-31

## LAB03-Q26 — A

**Question:** The access delegation log says the least-privilege workload delegation can now predict access inherited from a parent management boundary. Which access delegation state should the least-privilege workload delegation acceptance test retain?

- **A — Correct.** List assignments with inherited entries at the target resource and identify the parent scope.
  List assignments with inherited entries at the target resource and identify the parent scope. The least-privilege workload delegation reads scope inheritance directly; that scope inheritance result proves the least-privilege workload delegation can predict access inherited from a parent management boundary without another mutation.
- **B — Incorrect.** Compare direct and inherited assignment records and trace each role to its originating scope.
  Compare direct and inherited assignment records and trace each role to its originating scope. In the least-privilege workload delegation, this check observes effective access interpretation. Least-privilege workload delegation reads effective access interpretation, leaving scope inheritance unproved in least-privilege workload delegation; least-privilege workload delegation still has no scope inheritance proof.
- **C — Incorrect.** List effective assignments and test a read operation separately from a write operation.
  List effective assignments and test a read operation separately from a write operation. In the least-privilege workload delegation, this check observes Reader role. Least-privilege workload delegation could pass Reader role while scope inheritance is wrong; least-privilege workload delegation still lacks scope inheritance proof.
- **D — Incorrect.** Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
  Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access. In the least-privilege workload delegation, this check observes least-privilege role selection. Least-privilege workload delegation output covers least-privilege role selection, not scope inheritance; the scope inheritance requirement to predict access inherited from a parent management boundary remains unverified.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q27 — D

**Question:** The least-privilege workload delegation rejects access delegation exit status as proof it can limit an assignment to one named resource. Which least-privilege workload delegation result is valid evidence?

- **A — Incorrect.** Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
  Query deny assignments at the target and parent scopes and compare their excluded principals and actions. In the least-privilege workload delegation, this check observes deny assignments. Least-privilege workload delegation reads deny assignments, leaving resource-level assignments unproved in least-privilege workload delegation; least-privilege workload delegation still has no resource-level assignments proof.
- **B — Incorrect.** Confirm resource writes succeed and role-assignment creation remains unauthorized.
  Confirm resource writes succeed and role-assignment creation remains unauthorized. In the least-privilege workload delegation, this check observes Contributor role. Least-privilege workload delegation could pass Contributor role while resource-level assignments is wrong; least-privilege workload delegation still lacks resource-level assignments proof.
- **C — Incorrect.** List assignments with inherited entries at the target resource and identify the parent scope.
  List assignments with inherited entries at the target resource and identify the parent scope. In the least-privilege workload delegation, this check observes scope inheritance. Least-privilege workload delegation output covers scope inheritance, not resource-level assignments; the resource-level assignments requirement to limit an assignment to one named resource remains unverified.
- **D — Correct.** Query assignments at the resource and verify that the scope equals the resource ID.
  For the least-privilege workload delegation, this resource-level assignments observation is decisive: query assignments at the resource and verify that the scope equals the resource ID. It is least-privilege workload delegation evidence that operators can limit an assignment to one named resource.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q28 — C

**Question:** The access delegation validator needs one least-privilege workload delegation query after the change to delegate the same access to a team through one directory group. Which access delegation property should the least-privilege workload delegation validator inspect?

- **A — Incorrect.** Read the assignment and confirm its principal ID, role definition ID, and scope independently.
  Read the assignment and confirm its principal ID, role definition ID, and scope independently. In the least-privilege workload delegation, this check observes role definitions and assignments. Least-privilege workload delegation could pass role definitions and assignments while group-based role assignment is wrong; least-privilege workload delegation still lacks group-based role assignment proof.
- **B — Incorrect.** Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
  Confirm role-assignment operations succeed while unrelated resource updates remain outside the role. In the least-privilege workload delegation, this check observes User Access Administrator role. Least-privilege workload delegation output covers User Access Administrator role, not group-based role assignment; the group-based role assignment requirement to delegate the same access to a team through one directory group remains unverified.
- **C — Correct.** Show both the group role assignment and the user's transitive membership in that group.
  Show both the group role assignment and the user's transitive membership in that group. Because the least-privilege workload delegation check observes group-based role assignment, it independently verifies the requirement to delegate the same access to a team through one directory group.
- **D — Incorrect.** Query assignments at the resource and verify that the scope equals the resource ID.
  Query assignments at the resource and verify that the scope equals the resource ID. In the least-privilege workload delegation, this check observes resource-level assignments. Least-privilege workload delegation reads resource-level assignments, leaving group-based role assignment unproved in least-privilege workload delegation; least-privilege workload delegation still has no group-based role assignment proof.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Assign Azure roles using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q29 — B

**Question:** The platform administrator granting least-privilege access to a workload team must confirm the least-privilege workload delegation, without mutation, can explain a principal's final permissions after all applicable assignments are combined. Which access delegation check qualifies?

- **A — Incorrect.** List effective assignments and test a read operation separately from a write operation.
  List effective assignments and test a read operation separately from a write operation. In the least-privilege workload delegation, this check observes Reader role. Least-privilege workload delegation output covers Reader role, not effective access interpretation; the effective access interpretation requirement to explain a principal's final permissions after all applicable assignments are combined remains unverified.
- **B — Correct.** Compare direct and inherited assignment records and trace each role to its originating scope.
  The least-privilege workload delegation validator needs this effective access interpretation result: compare direct and inherited assignment records and trace each role to its originating scope. It proves the outcome to explain a principal's final permissions after all applicable assignments are combined rather than an adjacent checkpoint.
- **C — Incorrect.** Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
  Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access. In the least-privilege workload delegation, this check observes least-privilege role selection. Least-privilege workload delegation reads least-privilege role selection, leaving effective access interpretation unproved in least-privilege workload delegation; least-privilege workload delegation still has no effective access interpretation proof.
- **D — Incorrect.** Show both the group role assignment and the user's transitive membership in that group.
  Show both the group role assignment and the user's transitive membership in that group. In the least-privilege workload delegation, this check observes group-based role assignment. Least-privilege workload delegation could pass group-based role assignment while effective access interpretation is wrong; least-privilege workload delegation still lacks effective access interpretation proof.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [List Azure role assignments using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q30 — D

**Question:** The least-privilege workload delegation configuration is complete; the access delegation reviewers need evidence it can explain why an allow assignment does not overcome an explicit platform block. Which observation shows success?

- **A — Incorrect.** Confirm resource writes succeed and role-assignment creation remains unauthorized.
  Confirm resource writes succeed and role-assignment creation remains unauthorized. In the least-privilege workload delegation, this check observes Contributor role. Contributor role success in least-privilege workload delegation cannot verify deny assignments; least-privilege workload delegation cannot explain why an allow assignment does not overcome an explicit platform block until deny assignments evidence exists.
- **B — Incorrect.** List assignments with inherited entries at the target resource and identify the parent scope.
  List assignments with inherited entries at the target resource and identify the parent scope. In the least-privilege workload delegation, this check observes scope inheritance. Least-privilege workload delegation reads scope inheritance, leaving deny assignments unproved in least-privilege workload delegation; least-privilege workload delegation still has no deny assignments proof.
- **C — Incorrect.** Compare direct and inherited assignment records and trace each role to its originating scope.
  Compare direct and inherited assignment records and trace each role to its originating scope. In the least-privilege workload delegation, this check observes effective access interpretation. Least-privilege workload delegation could pass effective access interpretation while deny assignments is wrong; least-privilege workload delegation still lacks deny assignments proof.
- **D — Correct.** Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
  Query deny assignments at the target and parent scopes and compare their excluded principals and actions. This is independent deny assignments evidence for the least-privilege workload delegation, even if least-privilege workload delegation setup reports success before deny assignments becomes observable.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Understand Azure deny assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/deny-assignments)

**Source reviewed:** 2026-08-31

## LAB03-Q31 — C

**Question:** Although the least-privilege workload delegation is meant to let the access delegation separate a role's permissions from the principal and scope that receive them, its checkpoint fails. Which access delegation defect explains the failure?

- **A — Incorrect.** The principal was given Contributor, which permits resource changes beyond the requirement.
  The principal was given Contributor, which permits resource changes beyond the requirement. The least-privilege workload delegation fault concerns Reader role. Least-privilege workload delegation has Reader role impact, but role definitions and assignments is the least-privilege workload delegation failed path; the Reader role state cannot produce role definitions and assignments failure.
- **B — Incorrect.** Validation listed only assignments created directly on the resource and omitted inherited access.
  Validation listed only assignments created directly on the resource and omitted inherited access. The least-privilege workload delegation fault concerns scope inheritance. Least-privilege workload delegation could repair scope inheritance while role definitions and assignments stays broken in least-privilege workload delegation; the least-privilege workload delegation remains unable to separate a role's permissions from the principal and scope that receive them.
- **C — Correct.** A role definition was inspected, but no role assignment was created for the principal.
  A role definition was inspected, but no role assignment was created for the principal. In least-privilege workload delegation, this role definitions and assignments cause matches the failure to separate a role's permissions from the principal and scope that receive them.
- **D — Incorrect.** Troubleshooting kept adding broader allow roles without checking an applicable deny assignment.
  Troubleshooting kept adding broader allow roles without checking an applicable deny assignment. The least-privilege workload delegation fault concerns deny assignments. Least-privilege workload delegation may fix deny assignments, yet role definitions and assignments still fails; this least-privilege workload delegation diagnosis of deny assignments is wrong for role definitions and assignments.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand Azure role definitions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions)

**Source reviewed:** 2026-08-31

## LAB03-Q32 — C

**Question:** The access delegation support team isolated the least-privilege workload delegation incident to the attempt to let an auditor inspect configuration without changing it. Which condition prevents success?

- **A — Incorrect.** The workflow expects Contributor to create role assignments for another user.
  The workflow expects Contributor to create role assignments for another user. The least-privilege workload delegation fault concerns Contributor role. Least-privilege workload delegation could repair Contributor role while Reader role stays broken in least-privilege workload delegation; the least-privilege workload delegation remains unable to let an auditor inspect configuration without changing it.
- **B — Incorrect.** The assignment scope is the resource group, exposing sibling resources unnecessarily.
  The assignment scope is the resource group, exposing sibling resources unnecessarily. The least-privilege workload delegation fault concerns resource-level assignments. Least-privilege workload delegation failed on Reader role; this resource-level assignments finding redirects least-privilege workload delegation remediation away from Reader role.
- **C — Correct.** The principal was given Contributor, which permits resource changes beyond the requirement.
  The principal was given Contributor, which permits resource changes beyond the requirement. This least-privilege workload delegation condition breaks Reader role, explaining why operators cannot let an auditor inspect configuration without changing it.
- **D — Incorrect.** A role definition was inspected, but no role assignment was created for the principal.
  A role definition was inspected, but no role assignment was created for the principal. The least-privilege workload delegation fault concerns role definitions and assignments. Least-privilege workload delegation has role definitions and assignments impact, but Reader role is the least-privilege workload delegation failed path; the role definitions and assignments state cannot produce Reader role failure.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q33 — A

**Question:** A least-privilege workload delegation query surprises the platform administrator granting least-privilege access to a workload team during the access delegation attempt to let an operator manage resources without granting access to other principals. Which finding explains it?

- **A — Correct.** The workflow expects Contributor to create role assignments for another user.
  For the least-privilege workload delegation, the Contributor role failure is causal: the workflow expects Contributor to create role assignments for another user. Correcting it restores the ability to let an operator manage resources without granting access to other principals.
- **B — Incorrect.** The role was assigned at subscription scope even though delegation was needed for one resource group.
  The role was assigned at subscription scope even though delegation was needed for one resource group. The least-privilege workload delegation fault concerns User Access Administrator role. Least-privilege workload delegation may fix User Access Administrator role, yet Contributor role still fails; this least-privilege workload delegation diagnosis of User Access Administrator role is wrong for Contributor role.
- **C — Incorrect.** The user's object ID was assigned directly, bypassing the required group-based model.
  The user's object ID was assigned directly, bypassing the required group-based model. The least-privilege workload delegation fault concerns group-based role assignment. Least-privilege workload delegation has group-based role assignment impact, but Contributor role is the least-privilege workload delegation failed path; the group-based role assignment state cannot produce Contributor role failure.
- **D — Incorrect.** The principal was given Contributor, which permits resource changes beyond the requirement.
  The principal was given Contributor, which permits resource changes beyond the requirement. The least-privilege workload delegation fault concerns Reader role. Least-privilege workload delegation could repair Reader role while Contributor role stays broken in least-privilege workload delegation; the least-privilege workload delegation remains unable to let an operator manage resources without granting access to other principals.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q34 — D

**Question:** Other least-privilege workload delegation components are healthy, but the access delegation still cannot delegate role-assignment administration without granting broad resource changes. Which state causes the isolated failure?

- **A — Incorrect.** Owner was selected merely to avoid identifying the required built-in role.
  Owner was selected merely to avoid identifying the required built-in role. The least-privilege workload delegation fault concerns least-privilege role selection. Least-privilege workload delegation may fix least-privilege role selection, yet User Access Administrator role still fails; this least-privilege workload delegation diagnosis of least-privilege role selection is wrong for User Access Administrator role.
- **B — Incorrect.** The review considered only assignments whose principal ID exactly matched the user and missed group-derived access.
  The review considered only assignments whose principal ID exactly matched the user and missed group-derived access. The least-privilege workload delegation fault concerns effective access interpretation. Least-privilege workload delegation has effective access interpretation impact, but User Access Administrator role is the least-privilege workload delegation failed path; the effective access interpretation state cannot produce User Access Administrator role failure.
- **C — Incorrect.** The workflow expects Contributor to create role assignments for another user.
  The workflow expects Contributor to create role assignments for another user. The least-privilege workload delegation fault concerns Contributor role. Least-privilege workload delegation could repair Contributor role while User Access Administrator role stays broken in least-privilege workload delegation; the least-privilege workload delegation remains unable to delegate role-assignment administration without granting broad resource changes.
- **D — Correct.** The role was assigned at subscription scope even though delegation was needed for one resource group.
  The role was assigned at subscription scope even though delegation was needed for one resource group. The finding is specific to User Access Administrator role in the least-privilege workload delegation; repairing User Access Administrator role restores the least-privilege workload delegation ability to delegate role-assignment administration without granting broad resource changes.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [Azure built-in privileged roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged)

**Source reviewed:** 2026-08-31

## LAB03-Q35 — C

**Question:** During an access delegation fault drill, the least-privilege workload delegation does not grant only the permissions and scope needed for the stated job. Which finding identifies the defect?

- **A — Incorrect.** Validation listed only assignments created directly on the resource and omitted inherited access.
  Validation listed only assignments created directly on the resource and omitted inherited access. The least-privilege workload delegation fault concerns scope inheritance. Least-privilege workload delegation has scope inheritance impact, but least-privilege role selection is the least-privilege workload delegation failed path; the scope inheritance state cannot produce least-privilege role selection failure.
- **B — Incorrect.** Troubleshooting kept adding broader allow roles without checking an applicable deny assignment.
  Troubleshooting kept adding broader allow roles without checking an applicable deny assignment. The least-privilege workload delegation fault concerns deny assignments. Least-privilege workload delegation could repair deny assignments while least-privilege role selection stays broken in least-privilege workload delegation; the least-privilege workload delegation remains unable to grant only the permissions and scope needed for the stated job.
- **C — Correct.** Owner was selected merely to avoid identifying the required built-in role.
  The least-privilege workload delegation cannot grant only the permissions and scope needed for the stated job because of this least-privilege role selection defect: owner was selected merely to avoid identifying the required built-in role. The symptom and repair align.
- **D — Incorrect.** The role was assigned at subscription scope even though delegation was needed for one resource group.
  The role was assigned at subscription scope even though delegation was needed for one resource group. The least-privilege workload delegation fault concerns User Access Administrator role. Least-privilege workload delegation may fix User Access Administrator role, yet least-privilege role selection still fails; this least-privilege workload delegation diagnosis of User Access Administrator role is wrong for least-privilege role selection.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices)

**Source reviewed:** 2026-08-31

## LAB03-Q36 — A

**Question:** The least-privilege workload delegation setup finishes, yet the access delegation cannot predict access inherited from a parent management boundary. Which misconfiguration explains the mismatch?

- **A — Correct.** Validation listed only assignments created directly on the resource and omitted inherited access.
  Validation listed only assignments created directly on the resource and omitted inherited access. Removing this scope inheritance condition lets the least-privilege workload delegation predict access inherited from a parent management boundary while leaving healthy controls unchanged.
- **B — Incorrect.** The assignment scope is the resource group, exposing sibling resources unnecessarily.
  The assignment scope is the resource group, exposing sibling resources unnecessarily. The least-privilege workload delegation fault concerns resource-level assignments. Least-privilege workload delegation failed on scope inheritance; this resource-level assignments finding redirects least-privilege workload delegation remediation away from scope inheritance.
- **C — Incorrect.** A role definition was inspected, but no role assignment was created for the principal.
  A role definition was inspected, but no role assignment was created for the principal. The least-privilege workload delegation fault concerns role definitions and assignments. Least-privilege workload delegation may fix role definitions and assignments, yet scope inheritance still fails; this least-privilege workload delegation diagnosis of role definitions and assignments is wrong for scope inheritance.
- **D — Incorrect.** Owner was selected merely to avoid identifying the required built-in role.
  Owner was selected merely to avoid identifying the required built-in role. The least-privilege workload delegation fault concerns least-privilege role selection. Least-privilege workload delegation has least-privilege role selection impact, but scope inheritance is the least-privilege workload delegation failed path; the least-privilege role selection state cannot produce scope inheritance failure.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q37 — C

**Question:** An access delegation break/fix in the least-privilege workload delegation fails when operators try to limit an assignment to one named resource. Which diagnosis fits?

- **A — Incorrect.** The user's object ID was assigned directly, bypassing the required group-based model.
  The user's object ID was assigned directly, bypassing the required group-based model. The least-privilege workload delegation fault concerns group-based role assignment. Least-privilege workload delegation failed on resource-level assignments; this group-based role assignment finding redirects least-privilege workload delegation remediation away from resource-level assignments.
- **B — Incorrect.** The principal was given Contributor, which permits resource changes beyond the requirement.
  The principal was given Contributor, which permits resource changes beyond the requirement. The least-privilege workload delegation fault concerns Reader role. Least-privilege workload delegation may fix Reader role, yet resource-level assignments still fails; this least-privilege workload delegation diagnosis of Reader role is wrong for resource-level assignments.
- **C — Correct.** The assignment scope is the resource group, exposing sibling resources unnecessarily.
  The assignment scope is the resource group, exposing sibling resources unnecessarily. In least-privilege workload delegation, this resource-level assignments cause matches the failure to limit an assignment to one named resource.
- **D — Incorrect.** Validation listed only assignments created directly on the resource and omitted inherited access.
  Validation listed only assignments created directly on the resource and omitted inherited access. The least-privilege workload delegation fault concerns scope inheritance. Least-privilege workload delegation could repair scope inheritance while resource-level assignments stays broken in least-privilege workload delegation; the least-privilege workload delegation remains unable to limit an assignment to one named resource.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q38 — C

**Question:** The least-privilege workload delegation troubleshooting scope is the access delegation need to delegate the same access to a team through one directory group. Which condition should be corrected first?

- **A — Incorrect.** The review considered only assignments whose principal ID exactly matched the user and missed group-derived access.
  The review considered only assignments whose principal ID exactly matched the user and missed group-derived access. The least-privilege workload delegation fault concerns effective access interpretation. Least-privilege workload delegation may fix effective access interpretation, yet group-based role assignment still fails; this least-privilege workload delegation diagnosis of effective access interpretation is wrong for group-based role assignment.
- **B — Incorrect.** The workflow expects Contributor to create role assignments for another user.
  The workflow expects Contributor to create role assignments for another user. The least-privilege workload delegation fault concerns Contributor role. Least-privilege workload delegation has Contributor role impact, but group-based role assignment is the least-privilege workload delegation failed path; the Contributor role state cannot produce group-based role assignment failure.
- **C — Correct.** The user's object ID was assigned directly, bypassing the required group-based model.
  The user's object ID was assigned directly, bypassing the required group-based model. This least-privilege workload delegation condition breaks group-based role assignment, explaining why operators cannot delegate the same access to a team through one directory group.
- **D — Incorrect.** The assignment scope is the resource group, exposing sibling resources unnecessarily.
  The assignment scope is the resource group, exposing sibling resources unnecessarily. The least-privilege workload delegation fault concerns resource-level assignments. Least-privilege workload delegation failed on group-based role assignment; this resource-level assignments finding redirects least-privilege workload delegation remediation away from group-based role assignment.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Assign Azure roles using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q39 — D

**Question:** The least-privilege workload delegation result is partial because the access delegation cannot explain a principal's final permissions after all applicable assignments are combined. Which condition accounts for that result?

- **A — Incorrect.** Troubleshooting kept adding broader allow roles without checking an applicable deny assignment.
  Troubleshooting kept adding broader allow roles without checking an applicable deny assignment. The least-privilege workload delegation fault concerns deny assignments. Least-privilege workload delegation has deny assignments impact, but effective access interpretation is the least-privilege workload delegation failed path; the deny assignments state cannot produce effective access interpretation failure.
- **B — Incorrect.** The role was assigned at subscription scope even though delegation was needed for one resource group.
  The role was assigned at subscription scope even though delegation was needed for one resource group. The least-privilege workload delegation fault concerns User Access Administrator role. Least-privilege workload delegation could repair User Access Administrator role while effective access interpretation stays broken in least-privilege workload delegation; the least-privilege workload delegation remains unable to explain a principal's final permissions after all applicable assignments are combined.
- **C — Incorrect.** The user's object ID was assigned directly, bypassing the required group-based model.
  The user's object ID was assigned directly, bypassing the required group-based model. The least-privilege workload delegation fault concerns group-based role assignment. Least-privilege workload delegation failed on effective access interpretation; this group-based role assignment finding redirects least-privilege workload delegation remediation away from effective access interpretation.
- **D — Correct.** The review considered only assignments whose principal ID exactly matched the user and missed group-derived access.
  For the least-privilege workload delegation, the effective access interpretation failure is causal: the review considered only assignments whose principal ID exactly matched the user and missed group-derived access. Correcting it restores the ability to explain a principal's final permissions after all applicable assignments are combined.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [List Azure role assignments using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q40 — A

**Question:** The access delegation evidence shows the least-privilege workload delegation cannot explain why an allow assignment does not overcome an explicit platform block. Which root cause fits that evidence?

- **A — Correct.** Troubleshooting kept adding broader allow roles without checking an applicable deny assignment.
  Troubleshooting kept adding broader allow roles without checking an applicable deny assignment. The finding is specific to deny assignments in the least-privilege workload delegation; repairing deny assignments restores the least-privilege workload delegation ability to explain why an allow assignment does not overcome an explicit platform block.
- **B — Incorrect.** A role definition was inspected, but no role assignment was created for the principal.
  A role definition was inspected, but no role assignment was created for the principal. The least-privilege workload delegation fault concerns role definitions and assignments. Least-privilege workload delegation failed on deny assignments; this role definitions and assignments finding redirects least-privilege workload delegation remediation away from deny assignments.
- **C — Incorrect.** Owner was selected merely to avoid identifying the required built-in role.
  Owner was selected merely to avoid identifying the required built-in role. The least-privilege workload delegation fault concerns least-privilege role selection. Least-privilege workload delegation may fix least-privilege role selection, yet deny assignments still fails; this least-privilege workload delegation diagnosis of least-privilege role selection is wrong for deny assignments.
- **D — Incorrect.** The review considered only assignments whose principal ID exactly matched the user and missed group-derived access.
  The review considered only assignments whose principal ID exactly matched the user and missed group-derived access. The least-privilege workload delegation fault concerns effective access interpretation. Least-privilege workload delegation has effective access interpretation impact, but deny assignments is the least-privilege workload delegation failed path; the effective access interpretation state cannot produce deny assignments failure.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Understand Azure deny assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/deny-assignments)

**Source reviewed:** 2026-08-31

## LAB03-Q41 — D

**Question:** The least-privilege workload delegation forbids a partial access delegation result. Operators must first separate a role's permissions from the principal and scope that receive them and afterward confirm the least-privilege workload delegation outcome. Which access delegation sequence is complete?

- **A — Incorrect.** First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized.
  First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized. This least-privilege workload delegation pair serves Contributor role. Contributor role cannot replace role definitions and assignments in least-privilege workload delegation. Use this role definitions and assignments pair instead: First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.
- **B — Incorrect.** First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.
  First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID. This least-privilege workload delegation pair serves resource-level assignments. Least-privilege workload delegation proves resource-level assignments, but role definitions and assignments lacks implementation in least-privilege workload delegation and role definitions and assignments proof; the role definitions and assignments outcome to separate a role's permissions from the principal and scope that receive them remains open.
- **C — Incorrect.** First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
  First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group. This least-privilege workload delegation pair serves group-based role assignment. Least-privilege workload delegation uses group-based role assignment for both steps; role definitions and assignments remains untouched in least-privilege workload delegation, so its role definitions and assignments gate to separate a role's permissions from the principal and scope that receive them fails.
- **D — Correct.** First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.
  The least-privilege workload delegation gets a complete role definitions and assignments sequence here: first, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently. Read-back evidence follows the change.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand Azure role definitions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions)

**Source reviewed:** 2026-08-31

## LAB03-Q42 — D

**Question:** Only the least-privilege workload delegation change needed to let an auditor inspect configuration without changing it is allowed, and access delegation proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
  First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role. This least-privilege workload delegation pair serves User Access Administrator role. Least-privilege workload delegation proves User Access Administrator role, but Reader role lacks implementation in least-privilege workload delegation and Reader role proof; the Reader role outcome to let an auditor inspect configuration without changing it remains open.
- **B — Incorrect.** First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
  First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group. This least-privilege workload delegation pair serves group-based role assignment. Least-privilege workload delegation uses group-based role assignment for both steps; Reader role remains untouched in least-privilege workload delegation, so its Reader role gate to let an auditor inspect configuration without changing it fails.
- **C — Incorrect.** First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
  First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope. This least-privilege workload delegation pair serves effective access interpretation. Least-privilege workload delegation closes effective access interpretation, not Reader role; without the Reader role workflow, it cannot let an auditor inspect configuration without changing it.
- **D — Correct.** First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation.
  First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation. This ordered Reader role workflow lets the least-privilege workload delegation let an auditor inspect configuration without changing it and then verify the resulting state.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q43 — C

**Question:** The least-privilege workload delegation runbook separates access delegation mutation from validation while it must let an operator manage resources without granting access to other principals. Which sequence proves it cleanly?

- **A — Incorrect.** First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
  First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access. This least-privilege workload delegation pair serves least-privilege role selection. Least-privilege workload delegation uses least-privilege role selection for both steps; Contributor role remains untouched in least-privilege workload delegation, so its Contributor role gate to let an operator manage resources without granting access to other principals fails.
- **B — Incorrect.** First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
  First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope. This least-privilege workload delegation pair serves effective access interpretation. Least-privilege workload delegation closes effective access interpretation, not Contributor role; without the Contributor role workflow, it cannot let an operator manage resources without granting access to other principals.
- **C — Correct.** First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized.
  First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized. For least-privilege workload delegation, the Contributor role operation precedes its Contributor role read-back check, allowing it to let an operator manage resources without granting access to other principals.
- **D — Incorrect.** First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
  First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions. This least-privilege workload delegation pair serves deny assignments. Least-privilege workload delegation proves deny assignments, but Contributor role lacks implementation in least-privilege workload delegation and Contributor role proof; the Contributor role outcome to let an operator manage resources without granting access to other principals remains open.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Azure built-in general roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general)

**Source reviewed:** 2026-08-31

## LAB03-Q44 — B

**Question:** The least-privilege workload delegation checkpoint requires both this access delegation outcome—delegate role-assignment administration without granting broad resource changes—and a read-only least-privilege workload delegation state check. Which access delegation response is complete?

- **A — Incorrect.** First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.
  First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope. This least-privilege workload delegation pair serves scope inheritance. Least-privilege workload delegation closes scope inheritance, not User Access Administrator role; without the User Access Administrator role workflow, it cannot delegate role-assignment administration without granting broad resource changes.
- **B — Correct.** First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
  First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role. In the least-privilege workload delegation, the first User Access Administrator role step runs; the least-privilege workload delegation then reads User Access Administrator role state to prove it can delegate role-assignment administration without granting broad resource changes.
- **C — Incorrect.** First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
  First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions. This least-privilege workload delegation pair serves deny assignments. Least-privilege workload delegation proves deny assignments, but User Access Administrator role lacks implementation in least-privilege workload delegation and User Access Administrator role proof; the User Access Administrator role outcome to delegate role-assignment administration without granting broad resource changes remains open.
- **D — Incorrect.** First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.
  First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently. This least-privilege workload delegation pair serves role definitions and assignments. Least-privilege workload delegation uses role definitions and assignments for both steps; User Access Administrator role remains untouched in least-privilege workload delegation, so its User Access Administrator role gate to delegate role-assignment administration without granting broad resource changes fails.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [Azure built-in privileged roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged)

**Source reviewed:** 2026-08-31

## LAB03-Q45 — C

**Question:** The least-privilege workload delegation runbook must grant only the permissions and scope needed for the stated job, then retain access delegation read-back evidence. Which least-privilege workload delegation pair completes both duties?

- **A — Incorrect.** First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.
  First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID. This least-privilege workload delegation pair serves resource-level assignments. Resource-level assignments cannot replace least-privilege role selection in least-privilege workload delegation. Use this least-privilege role selection pair instead: First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
- **B — Incorrect.** First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.
  First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently. This least-privilege workload delegation pair serves role definitions and assignments. Least-privilege workload delegation proves role definitions and assignments, but least-privilege role selection lacks implementation in least-privilege workload delegation and least-privilege role selection proof; the least-privilege role selection outcome to grant only the permissions and scope needed for the stated job remains open.
- **C — Correct.** First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
  For the least-privilege workload delegation, the safe least-privilege role selection order is: first, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access. The least-privilege workload delegation records least-privilege role selection proof after configuration.
- **D — Incorrect.** First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation.
  First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation. This least-privilege workload delegation pair serves Reader role. Least-privilege workload delegation closes Reader role, not least-privilege role selection; without the least-privilege role selection workflow, it cannot grant only the permissions and scope needed for the stated job.

**Objectives:** `IG-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices)

**Source reviewed:** 2026-08-31

## LAB03-Q46 — B

**Question:** To satisfy the access delegation requirement, operators must change the least-privilege workload delegation configuration and prove it can predict access inherited from a parent management boundary. Which sequence is coherent?

- **A — Incorrect.** First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
  First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group. This least-privilege workload delegation pair serves group-based role assignment. Least-privilege workload delegation proves group-based role assignment, but scope inheritance lacks implementation in least-privilege workload delegation and scope inheritance proof; the scope inheritance outcome to predict access inherited from a parent management boundary remains open.
- **B — Correct.** First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.
  First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope. The least-privilege workload delegation uses its scope inheritance mutation gate and scope inheritance verification gate before it can predict access inherited from a parent management boundary.
- **C — Incorrect.** First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation.
  First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation. This least-privilege workload delegation pair serves Reader role. Least-privilege workload delegation closes Reader role, not scope inheritance; without the scope inheritance workflow, it cannot predict access inherited from a parent management boundary.
- **D — Incorrect.** First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized.
  First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized. This least-privilege workload delegation pair serves Contributor role. Contributor role cannot replace scope inheritance in least-privilege workload delegation. Use this scope inheritance pair instead: First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB03-CP01`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q47 — B

**Question:** The platform administrator granting least-privilege access to a workload team needs a safe least-privilege workload delegation change to limit an assignment to one named resource, followed by access delegation evidence. Which pair merits approval?

- **A — Incorrect.** First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
  First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope. This least-privilege workload delegation pair serves effective access interpretation. Least-privilege workload delegation uses effective access interpretation for both steps; resource-level assignments remains untouched in least-privilege workload delegation, so its resource-level assignments gate to limit an assignment to one named resource fails.
- **B — Correct.** First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.
  The least-privilege workload delegation gets a complete resource-level assignments sequence here: first, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID. Read-back evidence follows the change.
- **C — Incorrect.** First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized.
  First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized. This least-privilege workload delegation pair serves Contributor role. Contributor role cannot replace resource-level assignments in least-privilege workload delegation. Use this resource-level assignments pair instead: First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.
- **D — Incorrect.** First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
  First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role. This least-privilege workload delegation pair serves User Access Administrator role. Least-privilege workload delegation proves User Access Administrator role, but resource-level assignments lacks implementation in least-privilege workload delegation and resource-level assignments proof; the resource-level assignments outcome to limit an assignment to one named resource remains open.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB03-CP02`).

**Microsoft Learn sources:**

- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)

**Source reviewed:** 2026-08-31

## LAB03-Q48 — C

**Question:** The least-privilege workload delegation has two access delegation gates: delegate the same access to a team through one directory group, then prove the least-privilege workload delegation state. Which access delegation sequence works?

- **A — Incorrect.** First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
  First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions. This least-privilege workload delegation pair serves deny assignments. Least-privilege workload delegation closes deny assignments, not group-based role assignment; without the group-based role assignment workflow, it cannot delegate the same access to a team through one directory group.
- **B — Incorrect.** First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
  First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role. This least-privilege workload delegation pair serves User Access Administrator role. User Access Administrator role cannot replace group-based role assignment in least-privilege workload delegation. Use this group-based role assignment pair instead: First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
- **C — Correct.** First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
  First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group. This ordered group-based role assignment workflow lets the least-privilege workload delegation delegate the same access to a team through one directory group and then verify the resulting state.
- **D — Incorrect.** First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
  First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access. This least-privilege workload delegation pair serves least-privilege role selection. Least-privilege workload delegation uses least-privilege role selection for both steps; group-based role assignment remains untouched in least-privilege workload delegation, so its group-based role assignment gate to delegate the same access to a team through one directory group fails.

**Objectives:** `IG-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB03-CP03`).

**Microsoft Learn sources:**

- [Assign Azure roles using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q49 — C

**Question:** Which access delegation path makes the least-privilege workload delegation able to explain a principal's final permissions after all applicable assignments are combined, then inspects the defining properties?

- **A — Incorrect.** First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.
  First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently. This least-privilege workload delegation pair serves role definitions and assignments. Role definitions and assignments cannot replace effective access interpretation in least-privilege workload delegation. Use this effective access interpretation pair instead: First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
- **B — Incorrect.** First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
  First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access. This least-privilege workload delegation pair serves least-privilege role selection. Least-privilege workload delegation proves least-privilege role selection, but effective access interpretation lacks implementation in least-privilege workload delegation and effective access interpretation proof; the effective access interpretation outcome to explain a principal's final permissions after all applicable assignments are combined remains open.
- **C — Correct.** First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
  First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope. For least-privilege workload delegation, the effective access interpretation operation precedes its effective access interpretation read-back check, allowing it to explain a principal's final permissions after all applicable assignments are combined.
- **D — Incorrect.** First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.
  First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope. This least-privilege workload delegation pair serves scope inheritance. Least-privilege workload delegation closes scope inheritance, not effective access interpretation; without the effective access interpretation workflow, it cannot explain a principal's final permissions after all applicable assignments are combined.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB03-CP04`).

**Microsoft Learn sources:**

- [List Azure role assignments using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)

**Source reviewed:** 2026-08-31

## LAB03-Q50 — A

**Question:** At the least-privilege workload delegation approval gate, operators must show that the access delegation can explain why an allow assignment does not overcome an explicit platform block. Which access delegation configure-and-check pair is defensible?

- **A — Correct.** First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
  First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions. In the least-privilege workload delegation, the first deny assignments step runs; the least-privilege workload delegation then reads deny assignments state to prove it can explain why an allow assignment does not overcome an explicit platform block.
- **B — Incorrect.** First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation.
  First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation. This least-privilege workload delegation pair serves Reader role. Least-privilege workload delegation uses Reader role for both steps; deny assignments remains untouched in least-privilege workload delegation, so its deny assignments gate to explain why an allow assignment does not overcome an explicit platform block fails.
- **C — Incorrect.** First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.
  First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope. This least-privilege workload delegation pair serves scope inheritance. Least-privilege workload delegation closes scope inheritance, not deny assignments; without the deny assignments workflow, it cannot explain why an allow assignment does not overcome an explicit platform block.
- **D — Incorrect.** First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.
  First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID. This least-privilege workload delegation pair serves resource-level assignments. Resource-level assignments cannot replace deny assignments in least-privilege workload delegation. Use this deny assignments pair instead: First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.

**Objectives:** `IG-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB03-CP05`).

**Microsoft Learn sources:**

- [Understand Azure deny assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/deny-assignments)

**Source reviewed:** 2026-08-31
