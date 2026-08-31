# Lab 03 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB03-Q01 — Foundational

The least-privilege workload delegation acceptance criteria require operators to separate a role's permissions from the principal and scope that receive them. Which service fact supports that requirement?

- A. Reader can view control-plane resources but cannot change them or automatically read protected data-plane content.
- B. Least privilege chooses the narrowest role whose actions satisfy the required work.
- C. Assigning a role to a group lets eligible members receive access through group membership.
- D. A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope.

## LAB03-Q02 — Foundational

An access delegation reviewer challenges whether the least-privilege workload delegation can let an auditor inspect configuration without changing it. Which response resolves the concern?

- A. Contributor can manage resources but cannot grant Azure RBAC access to other principals.
- B. Reader can view control-plane resources but cannot change them or automatically read protected data-plane content.
- C. An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access.
- D. Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes.

## LAB03-Q03 — Foundational

The least-privilege workload delegation handoff omits the access delegation rule needed to let an operator manage resources without granting access to other principals. Which statement should the team add?

- A. Contributor can manage resources but cannot grant Azure RBAC access to other principals.
- B. User Access Administrator manages access assignments without granting general resource-management permissions.
- C. A resource-level role assignment limits the authorization boundary to one resource.
- D. A deny assignment can block an operation even when a role assignment otherwise allows that action.

## LAB03-Q04 — Foundational

An access delegation incident review of the least-privilege workload delegation depends on the ability to delegate role-assignment administration without granting broad resource changes. Which platform description is reliable?

- A. Least privilege chooses the narrowest role whose actions satisfy the required work.
- B. Assigning a role to a group lets eligible members receive access through group membership.
- C. A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope.
- D. User Access Administrator manages access assignments without granting general resource-management permissions.

## LAB03-Q05 — Foundational

A platform administrator granting least-privilege access to a workload team is updating the access delegation runbook. The requirement is to grant only the permissions and scope needed for the stated job. Which statement describes Azure behavior correctly?

- A. An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access.
- B. Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes.
- C. Least privilege chooses the narrowest role whose actions satisfy the required work.
- D. Reader can view control-plane resources but cannot change them or automatically read protected data-plane content.

## LAB03-Q06 — Foundational

An access delegation peer review asks how the least-privilege workload delegation should handle this outcome: predict access inherited from a parent management boundary. Which explanation is accurate?

- A. An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access.
- B. A resource-level role assignment limits the authorization boundary to one resource.
- C. A deny assignment can block an operation even when a role assignment otherwise allows that action.
- D. Contributor can manage resources but cannot grant Azure RBAC access to other principals.

## LAB03-Q07 — Foundational

For the least-privilege workload delegation, the access delegation plan must limit an assignment to one named resource. Which statement about access delegation belongs in the least-privilege workload delegation record?

- A. A resource-level role assignment limits the authorization boundary to one resource.
- B. Assigning a role to a group lets eligible members receive access through group membership.
- C. A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope.
- D. User Access Administrator manages access assignments without granting general resource-management permissions.

## LAB03-Q08 — Foundational

The access delegation review compares four claims for the least-privilege workload delegation requirement to delegate the same access to a team through one directory group. Which claim is technically sound?

- A. Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes.
- B. Reader can view control-plane resources but cannot change them or automatically read protected data-plane content.
- C. Assigning a role to a group lets eligible members receive access through group membership.
- D. Least privilege chooses the narrowest role whose actions satisfy the required work.

## LAB03-Q09 — Foundational

The access delegation architecture note requires the least-privilege workload delegation environment to explain a principal's final permissions after all applicable assignments are combined. Which statement defines the relevant access delegation boundary?

- A. A deny assignment can block an operation even when a role assignment otherwise allows that action.
- B. Effective access combines direct assignments, group assignments, and assignments inherited from parent scopes.
- C. Contributor can manage resources but cannot grant Azure RBAC access to other principals.
- D. An assignment at a parent scope is inherited by child resource groups and resources unless another control denies access.

## LAB03-Q10 — Foundational

A new access delegation operator must explain why the least-privilege workload delegation can explain why an allow assignment does not overcome an explicit platform block. Which explanation is accurate?

- A. A role definition lists permitted actions, while a role assignment binds that definition to a principal at a scope.
- B. A deny assignment can block an operation even when a role assignment otherwise allows that action.
- C. User Access Administrator manages access assignments without granting general resource-management permissions.
- D. A resource-level role assignment limits the authorization boundary to one resource.

## LAB03-Q11 — Foundational

A least-privilege workload delegation review finds access delegation drift from the need to separate a role's permissions from the principal and scope that receive them. Which correction addresses that drift?

- A. Select a built-in role definition and create a separate assignment for the intended principal and scope.
- B. Assign Contributor for resource administration that excludes access delegation.
- C. Place an assignment at the common parent only when every child should inherit it.
- D. Enumerate all assignments for the principal with inheritance and group expansion considered.

## LAB03-Q12 — Foundational

The least-privilege workload delegation window permits only the access delegation change needed to let an auditor inspect configuration without changing it. Which option respects the boundary?

- A. Use User Access Administrator at the narrowest scope that needs delegated RBAC management.
- B. Assign Reader when a principal needs observation without resource modification.
- C. Assign the required role directly on the single resource when broader inheritance is unnecessary.
- D. Inspect applicable deny assignments when an apparently authorized action is rejected.

## LAB03-Q13 — Foundational

The access delegation preflight has passed; the least-privilege workload delegation must now let an operator manage resources without granting access to other principals. Which operation should run?

- A. Compare required operations with built-in role actions before creating an assignment.
- B. Bind the role to the group's object ID and manage authorized users through membership.
- C. Select a built-in role definition and create a separate assignment for the intended principal and scope.
- D. Assign Contributor for resource administration that excludes access delegation.

## LAB03-Q14 — Foundational

The least-privilege workload delegation plan must delegate role-assignment administration without granting broad resource changes while limiting the mutation scope to access delegation. Which action is appropriate?

- A. Place an assignment at the common parent only when every child should inherit it.
- B. Use User Access Administrator at the narrowest scope that needs delegated RBAC management.
- C. Enumerate all assignments for the principal with inheritance and group expansion considered.
- D. Assign Reader when a principal needs observation without resource modification.

## LAB03-Q15 — Foundational

An access delegation ticket in the least-privilege workload delegation says to grant only the permissions and scope needed for the stated job. Which access delegation action completes the least-privilege workload delegation request with minimal change?

- A. Compare required operations with built-in role actions before creating an assignment.
- B. Assign the required role directly on the single resource when broader inheritance is unnecessary.
- C. Inspect applicable deny assignments when an apparently authorized action is rejected.
- D. Assign Contributor for resource administration that excludes access delegation.

## LAB03-Q16 — Applied

The approach for the least-privilege workload delegation is approved, but the access delegation environment still cannot predict access inherited from a parent management boundary. Which implementation step closes the gap?

- A. Bind the role to the group's object ID and manage authorized users through membership.
- B. Place an assignment at the common parent only when every child should inherit it.
- C. Select a built-in role definition and create a separate assignment for the intended principal and scope.
- D. Use User Access Administrator at the narrowest scope that needs delegated RBAC management.

## LAB03-Q17 — Applied

The platform administrator granting least-privilege access to a workload team may change the least-privilege workload delegation only to limit an assignment to one named resource. Which access delegation action stays within that assignment?

- A. Enumerate all assignments for the principal with inheritance and group expansion considered.
- B. Assign Reader when a principal needs observation without resource modification.
- C. Compare required operations with built-in role actions before creating an assignment.
- D. Assign the required role directly on the single resource when broader inheritance is unnecessary.

## LAB03-Q18 — Applied

An access delegation dry run shows no least-privilege workload delegation command will delegate the same access to a team through one directory group. Which action belongs before execution?

- A. Inspect applicable deny assignments when an apparently authorized action is rejected.
- B. Assign Contributor for resource administration that excludes access delegation.
- C. Place an assignment at the common parent only when every child should inherit it.
- D. Bind the role to the group's object ID and manage authorized users through membership.

## LAB03-Q19 — Applied

For the least-privilege workload delegation, operators need to explain a principal's final permissions after all applicable assignments are combined. Which change realizes that requirement?

- A. Select a built-in role definition and create a separate assignment for the intended principal and scope.
- B. Use User Access Administrator at the narrowest scope that needs delegated RBAC management.
- C. Assign the required role directly on the single resource when broader inheritance is unnecessary.
- D. Enumerate all assignments for the principal with inheritance and group expansion considered.

## LAB03-Q20 — Applied

Operators must automate the least-privilege workload delegation change needed to explain why an allow assignment does not overcome an explicit platform block. Which access delegation operation belongs in the runbook?

- A. Inspect applicable deny assignments when an apparently authorized action is rejected.
- B. Assign Reader when a principal needs observation without resource modification.
- C. Compare required operations with built-in role actions before creating an assignment.
- D. Bind the role to the group's object ID and manage authorized users through membership.

## LAB03-Q21 — Applied

The access delegation validation asks whether the least-privilege workload delegation can separate a role's permissions from the principal and scope that receive them. Which observable state is strongest?

- A. Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
- B. Read the assignment and confirm its principal ID, role definition ID, and scope independently.
- C. Query assignments at the resource and verify that the scope equals the resource ID.
- D. Query deny assignments at the target and parent scopes and compare their excluded principals and actions.

## LAB03-Q22 — Applied

A least-privilege workload delegation review must prove the access delegation ability to let an auditor inspect configuration without changing it. Which check avoids an adjacent feature?

- A. Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
- B. List effective assignments and test a read operation separately from a write operation.
- C. Show both the group role assignment and the user's transitive membership in that group.
- D. Read the assignment and confirm its principal ID, role definition ID, and scope independently.

## LAB03-Q23 — Applied

The least-privilege workload delegation evidence bundle needs an access delegation result showing it can let an operator manage resources without granting access to other principals. Which result belongs in the checkpoint?

- A. Confirm resource writes succeed and role-assignment creation remains unauthorized.
- B. List assignments with inherited entries at the target resource and identify the parent scope.
- C. Compare direct and inherited assignment records and trace each role to its originating scope.
- D. List effective assignments and test a read operation separately from a write operation.

## LAB03-Q24 — Applied

Before least-privilege workload delegation cleanup, the access delegation team must reconfirm it can delegate role-assignment administration without granting broad resource changes. Which read-only inspection should run?

- A. Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
- B. Query assignments at the resource and verify that the scope equals the resource ID.
- C. Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
- D. Confirm resource writes succeed and role-assignment creation remains unauthorized.

## LAB03-Q25 — Applied

The least-privilege workload delegation setup reports success after the access delegation attempt to grant only the permissions and scope needed for the stated job. Which access delegation read-only observation proves the least-privilege workload delegation outcome?

- A. Show both the group role assignment and the user's transitive membership in that group.
- B. Read the assignment and confirm its principal ID, role definition ID, and scope independently.
- C. Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
- D. Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.

## LAB03-Q26 — Applied

The access delegation log says the least-privilege workload delegation can now predict access inherited from a parent management boundary. Which access delegation state should the least-privilege workload delegation acceptance test retain?

- A. List assignments with inherited entries at the target resource and identify the parent scope.
- B. Compare direct and inherited assignment records and trace each role to its originating scope.
- C. List effective assignments and test a read operation separately from a write operation.
- D. Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.

## LAB03-Q27 — Applied

The least-privilege workload delegation rejects access delegation exit status as proof it can limit an assignment to one named resource. Which least-privilege workload delegation result is valid evidence?

- A. Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
- B. Confirm resource writes succeed and role-assignment creation remains unauthorized.
- C. List assignments with inherited entries at the target resource and identify the parent scope.
- D. Query assignments at the resource and verify that the scope equals the resource ID.

## LAB03-Q28 — Applied

The access delegation validator needs one least-privilege workload delegation query after the change to delegate the same access to a team through one directory group. Which access delegation property should the least-privilege workload delegation validator inspect?

- A. Read the assignment and confirm its principal ID, role definition ID, and scope independently.
- B. Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
- C. Show both the group role assignment and the user's transitive membership in that group.
- D. Query assignments at the resource and verify that the scope equals the resource ID.

## LAB03-Q29 — Applied

The platform administrator granting least-privilege access to a workload team must confirm the least-privilege workload delegation, without mutation, can explain a principal's final permissions after all applicable assignments are combined. Which access delegation check qualifies?

- A. List effective assignments and test a read operation separately from a write operation.
- B. Compare direct and inherited assignment records and trace each role to its originating scope.
- C. Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
- D. Show both the group role assignment and the user's transitive membership in that group.

## LAB03-Q30 — Applied

The least-privilege workload delegation configuration is complete; the access delegation reviewers need evidence it can explain why an allow assignment does not overcome an explicit platform block. Which observation shows success?

- A. Confirm resource writes succeed and role-assignment creation remains unauthorized.
- B. List assignments with inherited entries at the target resource and identify the parent scope.
- C. Compare direct and inherited assignment records and trace each role to its originating scope.
- D. Query deny assignments at the target and parent scopes and compare their excluded principals and actions.

## LAB03-Q31 — Applied

Although the least-privilege workload delegation is meant to let the access delegation separate a role's permissions from the principal and scope that receive them, its checkpoint fails. Which access delegation defect explains the failure?

- A. The principal was given Contributor, which permits resource changes beyond the requirement.
- B. Validation listed only assignments created directly on the resource and omitted inherited access.
- C. A role definition was inspected, but no role assignment was created for the principal.
- D. Troubleshooting kept adding broader allow roles without checking an applicable deny assignment.

## LAB03-Q32 — Applied

The access delegation support team isolated the least-privilege workload delegation incident to the attempt to let an auditor inspect configuration without changing it. Which condition prevents success?

- A. The workflow expects Contributor to create role assignments for another user.
- B. The assignment scope is the resource group, exposing sibling resources unnecessarily.
- C. The principal was given Contributor, which permits resource changes beyond the requirement.
- D. A role definition was inspected, but no role assignment was created for the principal.

## LAB03-Q33 — Applied

A least-privilege workload delegation query surprises the platform administrator granting least-privilege access to a workload team during the access delegation attempt to let an operator manage resources without granting access to other principals. Which finding explains it?

- A. The workflow expects Contributor to create role assignments for another user.
- B. The role was assigned at subscription scope even though delegation was needed for one resource group.
- C. The user's object ID was assigned directly, bypassing the required group-based model.
- D. The principal was given Contributor, which permits resource changes beyond the requirement.

## LAB03-Q34 — Applied

Other least-privilege workload delegation components are healthy, but the access delegation still cannot delegate role-assignment administration without granting broad resource changes. Which state causes the isolated failure?

- A. Owner was selected merely to avoid identifying the required built-in role.
- B. The review considered only assignments whose principal ID exactly matched the user and missed group-derived access.
- C. The workflow expects Contributor to create role assignments for another user.
- D. The role was assigned at subscription scope even though delegation was needed for one resource group.

## LAB03-Q35 — Applied

During an access delegation fault drill, the least-privilege workload delegation does not grant only the permissions and scope needed for the stated job. Which finding identifies the defect?

- A. Validation listed only assignments created directly on the resource and omitted inherited access.
- B. Troubleshooting kept adding broader allow roles without checking an applicable deny assignment.
- C. Owner was selected merely to avoid identifying the required built-in role.
- D. The role was assigned at subscription scope even though delegation was needed for one resource group.

## LAB03-Q36 — Applied

The least-privilege workload delegation setup finishes, yet the access delegation cannot predict access inherited from a parent management boundary. Which misconfiguration explains the mismatch?

- A. Validation listed only assignments created directly on the resource and omitted inherited access.
- B. The assignment scope is the resource group, exposing sibling resources unnecessarily.
- C. A role definition was inspected, but no role assignment was created for the principal.
- D. Owner was selected merely to avoid identifying the required built-in role.

## LAB03-Q37 — Applied

An access delegation break/fix in the least-privilege workload delegation fails when operators try to limit an assignment to one named resource. Which diagnosis fits?

- A. The user's object ID was assigned directly, bypassing the required group-based model.
- B. The principal was given Contributor, which permits resource changes beyond the requirement.
- C. The assignment scope is the resource group, exposing sibling resources unnecessarily.
- D. Validation listed only assignments created directly on the resource and omitted inherited access.

## LAB03-Q38 — Applied

The least-privilege workload delegation troubleshooting scope is the access delegation need to delegate the same access to a team through one directory group. Which condition should be corrected first?

- A. The review considered only assignments whose principal ID exactly matched the user and missed group-derived access.
- B. The workflow expects Contributor to create role assignments for another user.
- C. The user's object ID was assigned directly, bypassing the required group-based model.
- D. The assignment scope is the resource group, exposing sibling resources unnecessarily.

## LAB03-Q39 — Applied

The least-privilege workload delegation result is partial because the access delegation cannot explain a principal's final permissions after all applicable assignments are combined. Which condition accounts for that result?

- A. Troubleshooting kept adding broader allow roles without checking an applicable deny assignment.
- B. The role was assigned at subscription scope even though delegation was needed for one resource group.
- C. The user's object ID was assigned directly, bypassing the required group-based model.
- D. The review considered only assignments whose principal ID exactly matched the user and missed group-derived access.

## LAB03-Q40 — Applied

The access delegation evidence shows the least-privilege workload delegation cannot explain why an allow assignment does not overcome an explicit platform block. Which root cause fits that evidence?

- A. Troubleshooting kept adding broader allow roles without checking an applicable deny assignment.
- B. A role definition was inspected, but no role assignment was created for the principal.
- C. Owner was selected merely to avoid identifying the required built-in role.
- D. The review considered only assignments whose principal ID exactly matched the user and missed group-derived access.

## LAB03-Q41 — Advanced

The least-privilege workload delegation forbids a partial access delegation result. Operators must first separate a role's permissions from the principal and scope that receive them and afterward confirm the least-privilege workload delegation outcome. Which access delegation sequence is complete?

- A. First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized.
- B. First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.
- C. First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
- D. First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.

## LAB03-Q42 — Advanced

Only the least-privilege workload delegation change needed to let an auditor inspect configuration without changing it is allowed, and access delegation proof is mandatory. Which pair fits?

- A. First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
- B. First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
- C. First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
- D. First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation.

## LAB03-Q43 — Advanced

The least-privilege workload delegation runbook separates access delegation mutation from validation while it must let an operator manage resources without granting access to other principals. Which sequence proves it cleanly?

- A. First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
- B. First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
- C. First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized.
- D. First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.

## LAB03-Q44 — Advanced

The least-privilege workload delegation checkpoint requires both this access delegation outcome—delegate role-assignment administration without granting broad resource changes—and a read-only least-privilege workload delegation state check. Which access delegation response is complete?

- A. First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.
- B. First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
- C. First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
- D. First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.

## LAB03-Q45 — Advanced

The least-privilege workload delegation runbook must grant only the permissions and scope needed for the stated job, then retain access delegation read-back evidence. Which least-privilege workload delegation pair completes both duties?

- A. First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.
- B. First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.
- C. First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
- D. First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation.

## LAB03-Q46 — Advanced

To satisfy the access delegation requirement, operators must change the least-privilege workload delegation configuration and prove it can predict access inherited from a parent management boundary. Which sequence is coherent?

- A. First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
- B. First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.
- C. First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation.
- D. First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized.

## LAB03-Q47 — Advanced

The platform administrator granting least-privilege access to a workload team needs a safe least-privilege workload delegation change to limit an assignment to one named resource, followed by access delegation evidence. Which pair merits approval?

- A. First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
- B. First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.
- C. First, Assign Contributor for resource administration that excludes access delegation. Then, Confirm resource writes succeed and role-assignment creation remains unauthorized.
- D. First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.

## LAB03-Q48 — Advanced

The least-privilege workload delegation has two access delegation gates: delegate the same access to a team through one directory group, then prove the least-privilege workload delegation state. Which access delegation sequence works?

- A. First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
- B. First, Use User Access Administrator at the narrowest scope that needs delegated RBAC management. Then, Confirm role-assignment operations succeed while unrelated resource updates remain outside the role.
- C. First, Bind the role to the group's object ID and manage authorized users through membership. Then, Show both the group role assignment and the user's transitive membership in that group.
- D. First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.

## LAB03-Q49 — Advanced

Which access delegation path makes the least-privilege workload delegation able to explain a principal's final permissions after all applicable assignments are combined, then inspects the defining properties?

- A. First, Select a built-in role definition and create a separate assignment for the intended principal and scope. Then, Read the assignment and confirm its principal ID, role definition ID, and scope independently.
- B. First, Compare required operations with built-in role actions before creating an assignment. Then, Inspect the chosen role definition and show that its allowed actions cover the task without broad wildcard access.
- C. First, Enumerate all assignments for the principal with inheritance and group expansion considered. Then, Compare direct and inherited assignment records and trace each role to its originating scope.
- D. First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.

## LAB03-Q50 — Advanced

At the least-privilege workload delegation approval gate, operators must show that the access delegation can explain why an allow assignment does not overcome an explicit platform block. Which access delegation configure-and-check pair is defensible?

- A. First, Inspect applicable deny assignments when an apparently authorized action is rejected. Then, Query deny assignments at the target and parent scopes and compare their excluded principals and actions.
- B. First, Assign Reader when a principal needs observation without resource modification. Then, List effective assignments and test a read operation separately from a write operation.
- C. First, Place an assignment at the common parent only when every child should inherit it. Then, List assignments with inherited entries at the target resource and identify the parent scope.
- D. First, Assign the required role directly on the single resource when broader inheritance is unnecessary. Then, Query assignments at the resource and verify that the scope equals the resource ID.

[Open the answer key](./ANSWERS.md)
