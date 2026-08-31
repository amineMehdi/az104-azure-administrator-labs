# Lab 04 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB04-Q01 — Foundational

A resource hierarchy incident review of the governed disposable-workload hierarchy depends on the ability to create and later remove one owned deployment boundary. Which platform description is reliable?

- A. Azure CLI resource operations target the active subscription unless an explicit subscription is supplied.
- B. Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis.
- C. A resource group is a management container whose deletion attempts to delete all resources it contains.
- D. A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes.

## LAB04-Q02 — Foundational

A governance administrator organizing disposable workloads is updating the resource hierarchy runbook. The requirement is to prevent commands from targeting the wrong Azure subscription. Which statement describes Azure behavior correctly?

- A. Management groups provide governance scope above subscriptions in a tenant hierarchy.
- B. Azure CLI resource operations target the active subscription unless an explicit subscription is supplied.
- C. Resource-group or subscription tags do not automatically become resource tags without policy or automation.
- D. A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move.

## LAB04-Q03 — Foundational

A resource hierarchy peer review asks how the governed disposable-workload hierarchy should handle this outcome: organize subscriptions under the intended governance parent. Which explanation is accurate?

- A. Management groups provide governance scope above subscriptions in a tenant hierarchy.
- B. Policy and access assignments at a management group can flow to descendant subscriptions.
- C. A CanNotDelete lock allows updates but blocks deletion at and below its scope.
- D. A resource group's location stores its management metadata and does not force contained resources into that region.

## LAB04-Q04 — Foundational

For the governed disposable-workload hierarchy, the resource hierarchy plan must apply parent governance consistently to descendant subscriptions. Which statement about resource hierarchy belongs in the governed disposable-workload hierarchy record?

- A. Policy and access assignments at a management group can flow to descendant subscriptions.
- B. Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis.
- C. A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes.
- D. A resource group is a management container whose deletion attempts to delete all resources it contains.

## LAB04-Q05 — Foundational

The resource hierarchy review compares four claims for the governed disposable-workload hierarchy requirement to label resources so cost and ownership queries can find them. Which claim is technically sound?

- A. Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis.
- B. Resource-group or subscription tags do not automatically become resource tags without policy or automation.
- C. A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move.
- D. Azure CLI resource operations target the active subscription unless an explicit subscription is supplied.

## LAB04-Q06 — Foundational

The resource hierarchy architecture note requires the governed disposable-workload hierarchy environment to avoid assuming that a parent label automatically appears on every child. Which statement defines the relevant resource hierarchy boundary?

- A. A CanNotDelete lock allows updates but blocks deletion at and below its scope.
- B. A resource group's location stores its management metadata and does not force contained resources into that region.
- C. Resource-group or subscription tags do not automatically become resource tags without policy or automation.
- D. Management groups provide governance scope above subscriptions in a tenant hierarchy.

## LAB04-Q07 — Foundational

A new resource hierarchy operator must explain why the governed disposable-workload hierarchy can prevent accidental deletion while still allowing supported updates. Which explanation is accurate?

- A. A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes.
- B. A resource group is a management container whose deletion attempts to delete all resources it contains.
- C. Policy and access assignments at a management group can flow to descendant subscriptions.
- D. A CanNotDelete lock allows updates but blocks deletion at and below its scope.

## LAB04-Q08 — Foundational

The governed disposable-workload hierarchy acceptance criteria require operators to prevent both deletion and control-plane modification of a protected resource. Which service fact supports that requirement?

- A. A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move.
- B. A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes.
- C. Azure CLI resource operations target the active subscription unless an explicit subscription is supplied.
- D. Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis.

## LAB04-Q09 — Foundational

A resource hierarchy reviewer challenges whether the governed disposable-workload hierarchy can relocate supported resources without recreating them. Which response resolves the concern?

- A. A resource group's location stores its management metadata and does not force contained resources into that region.
- B. Management groups provide governance scope above subscriptions in a tenant hierarchy.
- C. Resource-group or subscription tags do not automatically become resource tags without policy or automation.
- D. A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move.

## LAB04-Q10 — Foundational

The governed disposable-workload hierarchy handoff omits the resource hierarchy rule needed to choose the metadata region for a deployment boundary independently of its resources. Which statement should the team add?

- A. A resource group is a management container whose deletion attempts to delete all resources it contains.
- B. A resource group's location stores its management metadata and does not force contained resources into that region.
- C. Policy and access assignments at a management group can flow to descendant subscriptions.
- D. A CanNotDelete lock allows updates but blocks deletion at and below its scope.

## LAB04-Q11 — Foundational

The governed disposable-workload hierarchy plan must create and later remove one owned deployment boundary while limiting the mutation scope to resource hierarchy. Which action is appropriate?

- A. Place subscriptions beneath the approved management group before applying inherited governance.
- B. Use Azure Policy or explicit automation when child resources must receive parent tag values.
- C. Validate every dependent resource and destination prerequisite before starting the move.
- D. Group resources that share ownership and lifecycle into a deliberately scoped resource group.

## LAB04-Q12 — Foundational

A resource hierarchy ticket in the governed disposable-workload hierarchy says to prevent commands from targeting the wrong Azure subscription. Which resource hierarchy action completes the governed disposable-workload hierarchy request with minimal change?

- A. Assign shared governance at the lowest management group that contains every intended subscription.
- B. Apply a CanNotDelete lock at the narrowest scope that requires deletion protection.
- C. Choose an approved metadata location while selecting each resource's supported deployment region independently.
- D. Set and re-read the intended subscription before creating any resource group.

## LAB04-Q13 — Foundational

The approach for the governed disposable-workload hierarchy is approved, but the resource hierarchy environment still cannot organize subscriptions under the intended governance parent. Which implementation step closes the gap?

- A. Place subscriptions beneath the approved management group before applying inherited governance.
- B. Apply the required owner, environment, and run ID tags to each managed resource.
- C. Use ReadOnly only when the operational impact of blocking updates is acceptable.
- D. Group resources that share ownership and lifecycle into a deliberately scoped resource group.

## LAB04-Q14 — Foundational

The governance administrator organizing disposable workloads may change the governed disposable-workload hierarchy only to apply parent governance consistently to descendant subscriptions. Which resource hierarchy action stays within that assignment?

- A. Use Azure Policy or explicit automation when child resources must receive parent tag values.
- B. Assign shared governance at the lowest management group that contains every intended subscription.
- C. Validate every dependent resource and destination prerequisite before starting the move.
- D. Set and re-read the intended subscription before creating any resource group.

## LAB04-Q15 — Foundational

A resource hierarchy dry run shows no governed disposable-workload hierarchy command will label resources so cost and ownership queries can find them. Which action belongs before execution?

- A. Apply a CanNotDelete lock at the narrowest scope that requires deletion protection.
- B. Apply the required owner, environment, and run ID tags to each managed resource.
- C. Choose an approved metadata location while selecting each resource's supported deployment region independently.
- D. Place subscriptions beneath the approved management group before applying inherited governance.

## LAB04-Q16 — Applied

For the governed disposable-workload hierarchy, operators need to avoid assuming that a parent label automatically appears on every child. Which change realizes that requirement?

- A. Use ReadOnly only when the operational impact of blocking updates is acceptable.
- B. Use Azure Policy or explicit automation when child resources must receive parent tag values.
- C. Group resources that share ownership and lifecycle into a deliberately scoped resource group.
- D. Assign shared governance at the lowest management group that contains every intended subscription.

## LAB04-Q17 — Applied

Operators must automate the governed disposable-workload hierarchy change needed to prevent accidental deletion while still allowing supported updates. Which resource hierarchy operation belongs in the runbook?

- A. Validate every dependent resource and destination prerequisite before starting the move.
- B. Set and re-read the intended subscription before creating any resource group.
- C. Apply a CanNotDelete lock at the narrowest scope that requires deletion protection.
- D. Apply the required owner, environment, and run ID tags to each managed resource.

## LAB04-Q18 — Applied

A governed disposable-workload hierarchy review finds resource hierarchy drift from the need to prevent both deletion and control-plane modification of a protected resource. Which correction addresses that drift?

- A. Use ReadOnly only when the operational impact of blocking updates is acceptable.
- B. Choose an approved metadata location while selecting each resource's supported deployment region independently.
- C. Place subscriptions beneath the approved management group before applying inherited governance.
- D. Use Azure Policy or explicit automation when child resources must receive parent tag values.

## LAB04-Q19 — Applied

The governed disposable-workload hierarchy window permits only the resource hierarchy change needed to relocate supported resources without recreating them. Which option respects the boundary?

- A. Group resources that share ownership and lifecycle into a deliberately scoped resource group.
- B. Assign shared governance at the lowest management group that contains every intended subscription.
- C. Validate every dependent resource and destination prerequisite before starting the move.
- D. Apply a CanNotDelete lock at the narrowest scope that requires deletion protection.

## LAB04-Q20 — Applied

The resource hierarchy preflight has passed; the governed disposable-workload hierarchy must now choose the metadata region for a deployment boundary independently of its resources. Which operation should run?

- A. Choose an approved metadata location while selecting each resource's supported deployment region independently.
- B. Set and re-read the intended subscription before creating any resource group.
- C. Apply the required owner, environment, and run ID tags to each managed resource.
- D. Use ReadOnly only when the operational impact of blocking updates is acceptable.

## LAB04-Q21 — Applied

Before governed disposable-workload hierarchy cleanup, the resource hierarchy team must reconfirm it can create and later remove one owned deployment boundary. Which read-only inspection should run?

- A. Inspect the descendant subscription and identify the inherited assignment's management-group scope.
- B. List the group's resources and verify every managed resource carries the expected lab ownership tag.
- C. Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- D. Query the resource group location and each contained resource location as separate values.

## LAB04-Q22 — Applied

The governed disposable-workload hierarchy setup reports success after the resource hierarchy attempt to prevent commands from targeting the wrong Azure subscription. Which resource hierarchy read-only observation proves the governed disposable-workload hierarchy outcome?

- A. Query resource tags and compare every required key and exact expected value.
- B. List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
- C. List the group's resources and verify every managed resource carries the expected lab ownership tag.
- D. Compare az account show output with the approved subscription and tenant IDs.

## LAB04-Q23 — Applied

The resource hierarchy log says the governed disposable-workload hierarchy can now organize subscriptions under the intended governance parent. Which resource hierarchy state should the governed disposable-workload hierarchy acceptance test retain?

- A. Query both parent and child resources to prove the required tag exists on each child.
- B. Run move validation and then query the resource ID and dependencies in the destination scope.
- C. Query the hierarchy and confirm each subscription's parent management group ID.
- D. Compare az account show output with the approved subscription and tenant IDs.

## LAB04-Q24 — Applied

The governed disposable-workload hierarchy rejects resource hierarchy exit status as proof it can apply parent governance consistently to descendant subscriptions. Which governed disposable-workload hierarchy result is valid evidence?

- A. Inspect the descendant subscription and identify the inherited assignment's management-group scope.
- B. Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- C. Query the resource group location and each contained resource location as separate values.
- D. Query the hierarchy and confirm each subscription's parent management group ID.

## LAB04-Q25 — Applied

The resource hierarchy validator needs one governed disposable-workload hierarchy query after the change to label resources so cost and ownership queries can find them. Which resource hierarchy property should the governed disposable-workload hierarchy validator inspect?

- A. List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
- B. List the group's resources and verify every managed resource carries the expected lab ownership tag.
- C. Query resource tags and compare every required key and exact expected value.
- D. Inspect the descendant subscription and identify the inherited assignment's management-group scope.

## LAB04-Q26 — Applied

The governance administrator organizing disposable workloads must confirm the governed disposable-workload hierarchy, without mutation, can avoid assuming that a parent label automatically appears on every child. Which resource hierarchy check qualifies?

- A. Query both parent and child resources to prove the required tag exists on each child.
- B. Run move validation and then query the resource ID and dependencies in the destination scope.
- C. Compare az account show output with the approved subscription and tenant IDs.
- D. Query resource tags and compare every required key and exact expected value.

## LAB04-Q27 — Applied

The governed disposable-workload hierarchy configuration is complete; the resource hierarchy reviewers need evidence it can prevent accidental deletion while still allowing supported updates. Which observation shows success?

- A. Query the resource group location and each contained resource location as separate values.
- B. Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- C. Query the hierarchy and confirm each subscription's parent management group ID.
- D. Query both parent and child resources to prove the required tag exists on each child.

## LAB04-Q28 — Applied

The resource hierarchy validation asks whether the governed disposable-workload hierarchy can prevent both deletion and control-plane modification of a protected resource. Which observable state is strongest?

- A. List the group's resources and verify every managed resource carries the expected lab ownership tag.
- B. Inspect the descendant subscription and identify the inherited assignment's management-group scope.
- C. Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- D. List locks at the target scope and test a harmless control-plane update in the break/fix exercise.

## LAB04-Q29 — Applied

A governed disposable-workload hierarchy review must prove the resource hierarchy ability to relocate supported resources without recreating them. Which check avoids an adjacent feature?

- A. Compare az account show output with the approved subscription and tenant IDs.
- B. Query resource tags and compare every required key and exact expected value.
- C. Run move validation and then query the resource ID and dependencies in the destination scope.
- D. List locks at the target scope and test a harmless control-plane update in the break/fix exercise.

## LAB04-Q30 — Applied

The governed disposable-workload hierarchy evidence bundle needs a resource hierarchy result showing it can choose the metadata region for a deployment boundary independently of its resources. Which result belongs in the checkpoint?

- A. Query the hierarchy and confirm each subscription's parent management group ID.
- B. Query the resource group location and each contained resource location as separate values.
- C. Query both parent and child resources to prove the required tag exists on each child.
- D. Run move validation and then query the resource ID and dependencies in the destination scope.

## LAB04-Q31 — Applied

Other governed disposable-workload hierarchy components are healthy, but the resource hierarchy still cannot create and later remove one owned deployment boundary. Which state causes the isolated failure?

- A. The active subscription changed after sign-in and points at an unapproved environment.
- B. The runbook assumed a resource inherited its resource group's tags automatically.
- C. The design assumes all resources must share the resource group's metadata location.
- D. Cleanup targets a resource group that contains resources outside the lab's ownership boundary.

## LAB04-Q32 — Applied

During a resource hierarchy fault drill, the governed disposable-workload hierarchy does not prevent commands from targeting the wrong Azure subscription. Which finding identifies the defect?

- A. The subscription remains attached to a different management-group branch.
- B. Cleanup begins before removing the lab-owned CanNotDelete lock.
- C. The active subscription changed after sign-in and points at an unapproved environment.
- D. Cleanup targets a resource group that contains resources outside the lab's ownership boundary.

## LAB04-Q33 — Applied

The governed disposable-workload hierarchy setup finishes, yet the resource hierarchy cannot organize subscriptions under the intended governance parent. Which misconfiguration explains the mismatch?

- A. The assignment was created on a sibling management group with no ancestor relationship to the subscription.
- B. A ReadOnly lock prevents a service from updating configuration that its normal operation requires.
- C. The subscription remains attached to a different management-group branch.
- D. The active subscription changed after sign-in and points at an unapproved environment.

## LAB04-Q34 — Applied

A resource hierarchy break/fix in the governed disposable-workload hierarchy fails when operators try to apply parent governance consistently to descendant subscriptions. Which diagnosis fits?

- A. A required tag value differs in case from the value used by the cost-reporting convention.
- B. The assignment was created on a sibling management group with no ancestor relationship to the subscription.
- C. A dependent resource that must move with the target was omitted from the move request.
- D. The subscription remains attached to a different management-group branch.

## LAB04-Q35 — Applied

The governed disposable-workload hierarchy troubleshooting scope is the resource hierarchy need to label resources so cost and ownership queries can find them. Which condition should be corrected first?

- A. The runbook assumed a resource inherited its resource group's tags automatically.
- B. The design assumes all resources must share the resource group's metadata location.
- C. A required tag value differs in case from the value used by the cost-reporting convention.
- D. The assignment was created on a sibling management group with no ancestor relationship to the subscription.

## LAB04-Q36 — Applied

The governed disposable-workload hierarchy result is partial because the resource hierarchy cannot avoid assuming that a parent label automatically appears on every child. Which condition accounts for that result?

- A. Cleanup begins before removing the lab-owned CanNotDelete lock.
- B. Cleanup targets a resource group that contains resources outside the lab's ownership boundary.
- C. A required tag value differs in case from the value used by the cost-reporting convention.
- D. The runbook assumed a resource inherited its resource group's tags automatically.

## LAB04-Q37 — Applied

The resource hierarchy evidence shows the governed disposable-workload hierarchy cannot prevent accidental deletion while still allowing supported updates. Which root cause fits that evidence?

- A. A ReadOnly lock prevents a service from updating configuration that its normal operation requires.
- B. The active subscription changed after sign-in and points at an unapproved environment.
- C. The runbook assumed a resource inherited its resource group's tags automatically.
- D. Cleanup begins before removing the lab-owned CanNotDelete lock.

## LAB04-Q38 — Applied

Although the governed disposable-workload hierarchy is meant to let the resource hierarchy prevent both deletion and control-plane modification of a protected resource, its checkpoint fails. Which resource hierarchy defect explains the failure?

- A. A dependent resource that must move with the target was omitted from the move request.
- B. The subscription remains attached to a different management-group branch.
- C. Cleanup begins before removing the lab-owned CanNotDelete lock.
- D. A ReadOnly lock prevents a service from updating configuration that its normal operation requires.

## LAB04-Q39 — Applied

The resource hierarchy support team isolated the governed disposable-workload hierarchy incident to the attempt to relocate supported resources without recreating them. Which condition prevents success?

- A. A dependent resource that must move with the target was omitted from the move request.
- B. The design assumes all resources must share the resource group's metadata location.
- C. The assignment was created on a sibling management group with no ancestor relationship to the subscription.
- D. A ReadOnly lock prevents a service from updating configuration that its normal operation requires.

## LAB04-Q40 — Applied

A governed disposable-workload hierarchy query surprises the governance administrator organizing disposable workloads during the resource hierarchy attempt to choose the metadata region for a deployment boundary independently of its resources. Which finding explains it?

- A. Cleanup targets a resource group that contains resources outside the lab's ownership boundary.
- B. A required tag value differs in case from the value used by the cost-reporting convention.
- C. The design assumes all resources must share the resource group's metadata location.
- D. A dependent resource that must move with the target was omitted from the move request.

## LAB04-Q41 — Advanced

The governed disposable-workload hierarchy checkpoint requires both this resource hierarchy outcome—create and later remove one owned deployment boundary—and a read-only governed disposable-workload hierarchy state check. Which resource hierarchy response is complete?

- A. First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
- B. First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.
- C. First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- D. First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.

## LAB04-Q42 — Advanced

The governed disposable-workload hierarchy runbook must prevent commands from targeting the wrong Azure subscription, then retain resource hierarchy read-back evidence. Which governed disposable-workload hierarchy pair completes both duties?

- A. First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.
- B. First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.
- C. First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
- D. First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.

## LAB04-Q43 — Advanced

To satisfy the resource hierarchy requirement, operators must change the governed disposable-workload hierarchy configuration and prove it can organize subscriptions under the intended governance parent. Which sequence is coherent?

- A. First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
- B. First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value.
- C. First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.
- D. First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values.

## LAB04-Q44 — Advanced

The governance administrator organizing disposable workloads needs a safe governed disposable-workload hierarchy change to apply parent governance consistently to descendant subscriptions, followed by resource hierarchy evidence. Which pair merits approval?

- A. First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child.
- B. First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values.
- C. First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.
- D. First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.

## LAB04-Q45 — Advanced

The governed disposable-workload hierarchy has two resource hierarchy gates: label resources so cost and ownership queries can find them, then prove the governed disposable-workload hierarchy state. Which resource hierarchy sequence works?

- A. First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value.
- B. First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- C. First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.
- D. First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.

## LAB04-Q46 — Advanced

Which resource hierarchy path makes the governed disposable-workload hierarchy able to avoid assuming that a parent label automatically appears on every child, then inspects the defining properties?

- A. First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
- B. First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.
- C. First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
- D. First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child.

## LAB04-Q47 — Advanced

At the governed disposable-workload hierarchy approval gate, operators must show that the resource hierarchy can prevent accidental deletion while still allowing supported updates. Which resource hierarchy configure-and-check pair is defensible?

- A. First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.
- B. First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- C. First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
- D. First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.

## LAB04-Q48 — Advanced

The governed disposable-workload hierarchy forbids a partial resource hierarchy result. Operators must first prevent both deletion and control-plane modification of a protected resource and afterward confirm the governed disposable-workload hierarchy outcome. Which resource hierarchy sequence is complete?

- A. First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
- B. First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values.
- C. First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.
- D. First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value.

## LAB04-Q49 — Advanced

Only the governed disposable-workload hierarchy change needed to relocate supported resources without recreating them is allowed, and resource hierarchy proof is mandatory. Which pair fits?

- A. First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.
- B. First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value.
- C. First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child.
- D. First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.

## LAB04-Q50 — Advanced

The governed disposable-workload hierarchy runbook separates resource hierarchy mutation from validation while it must choose the metadata region for a deployment boundary independently of its resources. Which sequence proves it cleanly?

- A. First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.
- B. First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child.
- C. First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- D. First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values.

[Open the answer key](./ANSWERS.md)
