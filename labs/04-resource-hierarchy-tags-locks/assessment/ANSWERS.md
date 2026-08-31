# Lab 04 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB04-Q01 — C

**Question:** A resource hierarchy incident review of the governed disposable-workload hierarchy depends on the ability to create and later remove one owned deployment boundary. Which platform description is reliable?

- **A — Incorrect.** Azure CLI resource operations target the active subscription unless an explicit subscription is supplied.
  Azure CLI resource operations target the active subscription unless an explicit subscription is supplied. In the governed disposable-workload hierarchy, this statement describes subscription context. Governed disposable-workload hierarchy asks about resource group lifecycle; this subscription context choice leaves the resource group lifecycle explanation missing.
- **B — Incorrect.** Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis.
  Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis. In the governed disposable-workload hierarchy, this statement describes resource tags. The resource tags statement accurately describes resource tags; however, governed disposable-workload hierarchy needs resource group lifecycle to create and later remove one owned deployment boundary; resource tags cannot replace resource group lifecycle.
- **C — Correct.** A resource group is a management container whose deletion attempts to delete all resources it contains.
  A resource group is a management container whose deletion attempts to delete all resources it contains. This resource group lifecycle fact resolves the governed disposable-workload hierarchy design question about how to create and later remove one owned deployment boundary.
- **D — Incorrect.** A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes.
  A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes. In the governed disposable-workload hierarchy, this statement describes ReadOnly locks. Resource group lifecycle governs governed disposable-workload hierarchy; ReadOnly locks cannot support resource group lifecycle when operators must create and later remove one owned deployment boundary.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q02 — B

**Question:** A governance administrator organizing disposable workloads is updating the resource hierarchy runbook. The requirement is to prevent commands from targeting the wrong Azure subscription. Which statement describes Azure behavior correctly?

- **A — Incorrect.** Management groups provide governance scope above subscriptions in a tenant hierarchy.
  Management groups provide governance scope above subscriptions in a tenant hierarchy. In the governed disposable-workload hierarchy, this statement describes management group hierarchy. The management group hierarchy statement accurately describes management group hierarchy; however, governed disposable-workload hierarchy needs subscription context to prevent commands from targeting the wrong Azure subscription; management group hierarchy cannot replace subscription context.
- **B — Correct.** Azure CLI resource operations target the active subscription unless an explicit subscription is supplied.
  Azure CLI resource operations target the active subscription unless an explicit subscription is supplied. For governed disposable-workload hierarchy, subscription context supplies the service rule needed to prevent commands from targeting the wrong Azure subscription.
- **C — Incorrect.** Resource-group or subscription tags do not automatically become resource tags without policy or automation.
  Resource-group or subscription tags do not automatically become resource tags without policy or automation. In the governed disposable-workload hierarchy, this statement describes tag inheritance limitations. Subscription context governs governed disposable-workload hierarchy; tag inheritance limitations cannot support subscription context when operators must prevent commands from targeting the wrong Azure subscription.
- **D — Incorrect.** A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move.
  A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move. In the governed disposable-workload hierarchy, this statement describes resource moves. Governed disposable-workload hierarchy asks about subscription context; this resource moves choice leaves the subscription context explanation missing.

**Objectives:** `IG-GOVERN-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Manage Azure subscriptions with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q03 — A

**Question:** A resource hierarchy peer review asks how the governed disposable-workload hierarchy should handle this outcome: organize subscriptions under the intended governance parent. Which explanation is accurate?

- **A — Correct.** Management groups provide governance scope above subscriptions in a tenant hierarchy.
  Management groups provide governance scope above subscriptions in a tenant hierarchy. In the governed disposable-workload hierarchy, this management group hierarchy rule supports the need to organize subscriptions under the intended governance parent.
- **B — Incorrect.** Policy and access assignments at a management group can flow to descendant subscriptions.
  Policy and access assignments at a management group can flow to descendant subscriptions. In the governed disposable-workload hierarchy, this statement describes management group inheritance. Management group hierarchy governs governed disposable-workload hierarchy; management group inheritance cannot support management group hierarchy when operators must organize subscriptions under the intended governance parent.
- **C — Incorrect.** A CanNotDelete lock allows updates but blocks deletion at and below its scope.
  A CanNotDelete lock allows updates but blocks deletion at and below its scope. In the governed disposable-workload hierarchy, this statement describes CanNotDelete locks. Governed disposable-workload hierarchy asks about management group hierarchy; this CanNotDelete locks choice leaves the management group hierarchy explanation missing.
- **D — Incorrect.** A resource group's location stores its management metadata and does not force contained resources into that region.
  A resource group's location stores its management metadata and does not force contained resources into that region. In the governed disposable-workload hierarchy, this statement describes resource group location. The resource group location statement accurately describes resource group location; however, governed disposable-workload hierarchy needs management group hierarchy to organize subscriptions under the intended governance parent; resource group location cannot replace management group hierarchy.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q04 — A

**Question:** For the governed disposable-workload hierarchy, the resource hierarchy plan must apply parent governance consistently to descendant subscriptions. Which statement about resource hierarchy belongs in the governed disposable-workload hierarchy record?

- **A — Correct.** Policy and access assignments at a management group can flow to descendant subscriptions.
  For the governed disposable-workload hierarchy, the rule for management group inheritance is defined by this statement: policy and access assignments at a management group can flow to descendant subscriptions. It supports the required outcome to apply parent governance consistently to descendant subscriptions.
- **B — Incorrect.** Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis.
  Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis. In the governed disposable-workload hierarchy, this statement describes resource tags. Governed disposable-workload hierarchy asks about management group inheritance; this resource tags choice leaves the management group inheritance explanation missing.
- **C — Incorrect.** A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes.
  A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes. In the governed disposable-workload hierarchy, this statement describes ReadOnly locks. The ReadOnly locks statement accurately describes ReadOnly locks; however, governed disposable-workload hierarchy needs management group inheritance to apply parent governance consistently to descendant subscriptions; ReadOnly locks cannot replace management group inheritance.
- **D — Incorrect.** A resource group is a management container whose deletion attempts to delete all resources it contains.
  A resource group is a management container whose deletion attempts to delete all resources it contains. In the governed disposable-workload hierarchy, this statement describes resource group lifecycle. Selecting resource group lifecycle for governed disposable-workload hierarchy leaves management group inheritance unanswered in governed disposable-workload hierarchy; the governed disposable-workload hierarchy lacks a management group inheritance basis to apply parent governance consistently to descendant subscriptions.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q05 — A

**Question:** The resource hierarchy review compares four claims for the governed disposable-workload hierarchy requirement to label resources so cost and ownership queries can find them. Which claim is technically sound?

- **A — Correct.** Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis.
  Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis. The governed disposable-workload hierarchy applies that resource tags boundary when operators must label resources so cost and ownership queries can find them.
- **B — Incorrect.** Resource-group or subscription tags do not automatically become resource tags without policy or automation.
  Resource-group or subscription tags do not automatically become resource tags without policy or automation. In the governed disposable-workload hierarchy, this statement describes tag inheritance limitations. The tag inheritance limitations statement accurately describes tag inheritance limitations; however, governed disposable-workload hierarchy needs resource tags to label resources so cost and ownership queries can find them; tag inheritance limitations cannot replace resource tags.
- **C — Incorrect.** A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move.
  A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move. In the governed disposable-workload hierarchy, this statement describes resource moves. Selecting resource moves for governed disposable-workload hierarchy leaves resource tags unanswered in governed disposable-workload hierarchy; the governed disposable-workload hierarchy lacks a resource tags basis to label resources so cost and ownership queries can find them.
- **D — Incorrect.** Azure CLI resource operations target the active subscription unless an explicit subscription is supplied.
  Azure CLI resource operations target the active subscription unless an explicit subscription is supplied. In the governed disposable-workload hierarchy, this statement describes subscription context. Resource tags governs governed disposable-workload hierarchy; subscription context cannot support resource tags when operators must label resources so cost and ownership queries can find them.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q06 — C

**Question:** The resource hierarchy architecture note requires the governed disposable-workload hierarchy environment to avoid assuming that a parent label automatically appears on every child. Which statement defines the relevant resource hierarchy boundary?

- **A — Incorrect.** A CanNotDelete lock allows updates but blocks deletion at and below its scope.
  A CanNotDelete lock allows updates but blocks deletion at and below its scope. In the governed disposable-workload hierarchy, this statement describes CanNotDelete locks. The CanNotDelete locks statement accurately describes CanNotDelete locks; however, governed disposable-workload hierarchy needs tag inheritance limitations to avoid assuming that a parent label automatically appears on every child; CanNotDelete locks cannot replace tag inheritance limitations.
- **B — Incorrect.** A resource group's location stores its management metadata and does not force contained resources into that region.
  A resource group's location stores its management metadata and does not force contained resources into that region. In the governed disposable-workload hierarchy, this statement describes resource group location. Selecting resource group location for governed disposable-workload hierarchy leaves tag inheritance limitations unanswered in governed disposable-workload hierarchy; the governed disposable-workload hierarchy lacks a tag inheritance limitations basis to avoid assuming that a parent label automatically appears on every child.
- **C — Correct.** Resource-group or subscription tags do not automatically become resource tags without policy or automation.
  The governed disposable-workload hierarchy needs tag inheritance limitations to avoid assuming that a parent label automatically appears on every child; this option states the applicable tag inheritance limitations rule: resource-group or subscription tags do not automatically become resource tags without policy or automation.
- **D — Incorrect.** Management groups provide governance scope above subscriptions in a tenant hierarchy.
  Management groups provide governance scope above subscriptions in a tenant hierarchy. In the governed disposable-workload hierarchy, this statement describes management group hierarchy. Governed disposable-workload hierarchy asks about tag inheritance limitations; this management group hierarchy choice leaves the tag inheritance limitations explanation missing.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q07 — D

**Question:** A new resource hierarchy operator must explain why the governed disposable-workload hierarchy can prevent accidental deletion while still allowing supported updates. Which explanation is accurate?

- **A — Incorrect.** A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes.
  A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes. In the governed disposable-workload hierarchy, this statement describes ReadOnly locks. Selecting ReadOnly locks for governed disposable-workload hierarchy leaves CanNotDelete locks unanswered in governed disposable-workload hierarchy; the governed disposable-workload hierarchy lacks a CanNotDelete locks basis to prevent accidental deletion while still allowing supported updates.
- **B — Incorrect.** A resource group is a management container whose deletion attempts to delete all resources it contains.
  A resource group is a management container whose deletion attempts to delete all resources it contains. In the governed disposable-workload hierarchy, this statement describes resource group lifecycle. CanNotDelete locks governs governed disposable-workload hierarchy; resource group lifecycle cannot support CanNotDelete locks when operators must prevent accidental deletion while still allowing supported updates.
- **C — Incorrect.** Policy and access assignments at a management group can flow to descendant subscriptions.
  Policy and access assignments at a management group can flow to descendant subscriptions. In the governed disposable-workload hierarchy, this statement describes management group inheritance. Governed disposable-workload hierarchy asks about CanNotDelete locks; this management group inheritance choice leaves the CanNotDelete locks explanation missing.
- **D — Correct.** A CanNotDelete lock allows updates but blocks deletion at and below its scope.
  A CanNotDelete lock allows updates but blocks deletion at and below its scope. This CanNotDelete locks fact resolves the governed disposable-workload hierarchy design question about how to prevent accidental deletion while still allowing supported updates.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q08 — B

**Question:** The governed disposable-workload hierarchy acceptance criteria require operators to prevent both deletion and control-plane modification of a protected resource. Which service fact supports that requirement?

- **A — Incorrect.** A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move.
  A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move. In the governed disposable-workload hierarchy, this statement describes resource moves. ReadOnly locks governs governed disposable-workload hierarchy; resource moves cannot support ReadOnly locks when operators must prevent both deletion and control-plane modification of a protected resource.
- **B — Correct.** A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes.
  A ReadOnly lock blocks control-plane update operations as well as deletion and can disrupt services that require writes. For governed disposable-workload hierarchy, ReadOnly locks supplies the service rule needed to prevent both deletion and control-plane modification of a protected resource.
- **C — Incorrect.** Azure CLI resource operations target the active subscription unless an explicit subscription is supplied.
  Azure CLI resource operations target the active subscription unless an explicit subscription is supplied. In the governed disposable-workload hierarchy, this statement describes subscription context. The subscription context statement accurately describes subscription context; however, governed disposable-workload hierarchy needs ReadOnly locks to prevent both deletion and control-plane modification of a protected resource; subscription context cannot replace ReadOnly locks.
- **D — Incorrect.** Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis.
  Tags are case-insensitive for key operations but their values are case-sensitive strings used for organization and cost analysis. In the governed disposable-workload hierarchy, this statement describes resource tags. Selecting resource tags for governed disposable-workload hierarchy leaves ReadOnly locks unanswered in governed disposable-workload hierarchy; the governed disposable-workload hierarchy lacks a ReadOnly locks basis to prevent both deletion and control-plane modification of a protected resource.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q09 — D

**Question:** A resource hierarchy reviewer challenges whether the governed disposable-workload hierarchy can relocate supported resources without recreating them. Which response resolves the concern?

- **A — Incorrect.** A resource group's location stores its management metadata and does not force contained resources into that region.
  A resource group's location stores its management metadata and does not force contained resources into that region. In the governed disposable-workload hierarchy, this statement describes resource group location. Governed disposable-workload hierarchy asks about resource moves; this resource group location choice leaves the resource moves explanation missing.
- **B — Incorrect.** Management groups provide governance scope above subscriptions in a tenant hierarchy.
  Management groups provide governance scope above subscriptions in a tenant hierarchy. In the governed disposable-workload hierarchy, this statement describes management group hierarchy. The management group hierarchy statement accurately describes management group hierarchy; however, governed disposable-workload hierarchy needs resource moves to relocate supported resources without recreating them; management group hierarchy cannot replace resource moves.
- **C — Incorrect.** Resource-group or subscription tags do not automatically become resource tags without policy or automation.
  Resource-group or subscription tags do not automatically become resource tags without policy or automation. In the governed disposable-workload hierarchy, this statement describes tag inheritance limitations. Selecting tag inheritance limitations for governed disposable-workload hierarchy leaves resource moves unanswered in governed disposable-workload hierarchy; the governed disposable-workload hierarchy lacks a resource moves basis to relocate supported resources without recreating them.
- **D — Correct.** A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move.
  A resource move changes its parent resource group or subscription while resource IDs and dependencies may change or constrain the move. In the governed disposable-workload hierarchy, this resource moves rule supports the need to relocate supported resources without recreating them.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)

**Source reviewed:** 2026-08-31

## LAB04-Q10 — B

**Question:** The governed disposable-workload hierarchy handoff omits the resource hierarchy rule needed to choose the metadata region for a deployment boundary independently of its resources. Which statement should the team add?

- **A — Incorrect.** A resource group is a management container whose deletion attempts to delete all resources it contains.
  A resource group is a management container whose deletion attempts to delete all resources it contains. In the governed disposable-workload hierarchy, this statement describes resource group lifecycle. The resource group lifecycle statement accurately describes resource group lifecycle; however, governed disposable-workload hierarchy needs resource group location to choose the metadata region for a deployment boundary independently of its resources; resource group lifecycle cannot replace resource group location.
- **B — Correct.** A resource group's location stores its management metadata and does not force contained resources into that region.
  For the governed disposable-workload hierarchy, the rule for resource group location is defined by this statement: a resource group's location stores its management metadata and does not force contained resources into that region. It supports the required outcome to choose the metadata region for a deployment boundary independently of its resources.
- **C — Incorrect.** Policy and access assignments at a management group can flow to descendant subscriptions.
  Policy and access assignments at a management group can flow to descendant subscriptions. In the governed disposable-workload hierarchy, this statement describes management group inheritance. Resource group location governs governed disposable-workload hierarchy; management group inheritance cannot support resource group location when operators must choose the metadata region for a deployment boundary independently of its resources.
- **D — Incorrect.** A CanNotDelete lock allows updates but blocks deletion at and below its scope.
  A CanNotDelete lock allows updates but blocks deletion at and below its scope. In the governed disposable-workload hierarchy, this statement describes CanNotDelete locks. Governed disposable-workload hierarchy asks about resource group location; this CanNotDelete locks choice leaves the resource group location explanation missing.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q11 — D

**Question:** The governed disposable-workload hierarchy plan must create and later remove one owned deployment boundary while limiting the mutation scope to resource hierarchy. Which action is appropriate?

- **A — Incorrect.** Place subscriptions beneath the approved management group before applying inherited governance.
  Place subscriptions beneath the approved management group before applying inherited governance. In the governed disposable-workload hierarchy, this action changes management group hierarchy. Governed disposable-workload hierarchy approved resource group lifecycle, not management group hierarchy; only the resource group lifecycle change can create and later remove one owned deployment boundary.
- **B — Incorrect.** Use Azure Policy or explicit automation when child resources must receive parent tag values.
  Use Azure Policy or explicit automation when child resources must receive parent tag values. In the governed disposable-workload hierarchy, this action changes tag inheritance limitations. Governed disposable-workload hierarchy requires resource group lifecycle; changing tag inheritance limitations leaves resource group lifecycle absent in governed disposable-workload hierarchy; governed disposable-workload hierarchy cannot create and later remove one owned deployment boundary.
- **C — Incorrect.** Validate every dependent resource and destination prerequisite before starting the move.
  Validate every dependent resource and destination prerequisite before starting the move. In the governed disposable-workload hierarchy, this action changes resource moves. Resource moves does not implement resource group lifecycle for governed disposable-workload hierarchy; the governed disposable-workload hierarchy still cannot create and later remove one owned deployment boundary.
- **D — Correct.** Group resources that share ownership and lifecycle into a deliberately scoped resource group.
  Group resources that share ownership and lifecycle into a deliberately scoped resource group. This changes resource group lifecycle in the governed disposable-workload hierarchy, supplying the missing state needed to create and later remove one owned deployment boundary.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q12 — D

**Question:** A resource hierarchy ticket in the governed disposable-workload hierarchy says to prevent commands from targeting the wrong Azure subscription. Which resource hierarchy action completes the governed disposable-workload hierarchy request with minimal change?

- **A — Incorrect.** Assign shared governance at the lowest management group that contains every intended subscription.
  Assign shared governance at the lowest management group that contains every intended subscription. In the governed disposable-workload hierarchy, this action changes management group inheritance. Governed disposable-workload hierarchy requires subscription context; changing management group inheritance leaves subscription context absent in governed disposable-workload hierarchy; governed disposable-workload hierarchy cannot prevent commands from targeting the wrong Azure subscription.
- **B — Incorrect.** Apply a CanNotDelete lock at the narrowest scope that requires deletion protection.
  Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. In the governed disposable-workload hierarchy, this action changes CanNotDelete locks. CanNotDelete locks does not implement subscription context for governed disposable-workload hierarchy; the governed disposable-workload hierarchy still cannot prevent commands from targeting the wrong Azure subscription.
- **C — Incorrect.** Choose an approved metadata location while selecting each resource's supported deployment region independently.
  Choose an approved metadata location while selecting each resource's supported deployment region independently. In the governed disposable-workload hierarchy, this action changes resource group location. Governed disposable-workload hierarchy instead needs subscription context: Set and re-read the intended subscription before creating any resource group. The resource group location action omits that subscription context work.
- **D — Correct.** Set and re-read the intended subscription before creating any resource group.
  The governed disposable-workload hierarchy must prevent commands from targeting the wrong Azure subscription; this option performs its direct subscription context change: set and re-read the intended subscription before creating any resource group.

**Objectives:** `IG-GOVERN-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Manage Azure subscriptions with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q13 — A

**Question:** The approach for the governed disposable-workload hierarchy is approved, but the resource hierarchy environment still cannot organize subscriptions under the intended governance parent. Which implementation step closes the gap?

- **A — Correct.** Place subscriptions beneath the approved management group before applying inherited governance.
  Place subscriptions beneath the approved management group before applying inherited governance. It is the least-change management group hierarchy path for the governed disposable-workload hierarchy requirement to organize subscriptions under the intended governance parent.
- **B — Incorrect.** Apply the required owner, environment, and run ID tags to each managed resource.
  Apply the required owner, environment, and run ID tags to each managed resource. In the governed disposable-workload hierarchy, this action changes resource tags. Governed disposable-workload hierarchy instead needs management group hierarchy: Place subscriptions beneath the approved management group before applying inherited governance. The resource tags action omits that management group hierarchy work.
- **C — Incorrect.** Use ReadOnly only when the operational impact of blocking updates is acceptable.
  Use ReadOnly only when the operational impact of blocking updates is acceptable. In the governed disposable-workload hierarchy, this action changes ReadOnly locks. Governed disposable-workload hierarchy approved management group hierarchy, not ReadOnly locks; only the management group hierarchy change can organize subscriptions under the intended governance parent.
- **D — Incorrect.** Group resources that share ownership and lifecycle into a deliberately scoped resource group.
  Group resources that share ownership and lifecycle into a deliberately scoped resource group. In the governed disposable-workload hierarchy, this action changes resource group lifecycle. Governed disposable-workload hierarchy requires management group hierarchy; changing resource group lifecycle leaves management group hierarchy absent in governed disposable-workload hierarchy; governed disposable-workload hierarchy cannot organize subscriptions under the intended governance parent.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q14 — B

**Question:** The governance administrator organizing disposable workloads may change the governed disposable-workload hierarchy only to apply parent governance consistently to descendant subscriptions. Which resource hierarchy action stays within that assignment?

- **A — Incorrect.** Use Azure Policy or explicit automation when child resources must receive parent tag values.
  Use Azure Policy or explicit automation when child resources must receive parent tag values. In the governed disposable-workload hierarchy, this action changes tag inheritance limitations. Governed disposable-workload hierarchy instead needs management group inheritance: Assign shared governance at the lowest management group that contains every intended subscription. The tag inheritance limitations action omits that management group inheritance work.
- **B — Correct.** Assign shared governance at the lowest management group that contains every intended subscription.
  Assign shared governance at the lowest management group that contains every intended subscription. In governed disposable-workload hierarchy, applying management group inheritance is the scoped way to apply parent governance consistently to descendant subscriptions.
- **C — Incorrect.** Validate every dependent resource and destination prerequisite before starting the move.
  Validate every dependent resource and destination prerequisite before starting the move. In the governed disposable-workload hierarchy, this action changes resource moves. Governed disposable-workload hierarchy requires management group inheritance; changing resource moves leaves management group inheritance absent in governed disposable-workload hierarchy; governed disposable-workload hierarchy cannot apply parent governance consistently to descendant subscriptions.
- **D — Incorrect.** Set and re-read the intended subscription before creating any resource group.
  Set and re-read the intended subscription before creating any resource group. In the governed disposable-workload hierarchy, this action changes subscription context. Subscription context does not implement management group inheritance for governed disposable-workload hierarchy; the governed disposable-workload hierarchy still cannot apply parent governance consistently to descendant subscriptions.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q15 — B

**Question:** A resource hierarchy dry run shows no governed disposable-workload hierarchy command will label resources so cost and ownership queries can find them. Which action belongs before execution?

- **A — Incorrect.** Apply a CanNotDelete lock at the narrowest scope that requires deletion protection.
  Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. In the governed disposable-workload hierarchy, this action changes CanNotDelete locks. Governed disposable-workload hierarchy approved resource tags, not CanNotDelete locks; only the resource tags change can label resources so cost and ownership queries can find them.
- **B — Correct.** Apply the required owner, environment, and run ID tags to each managed resource.
  Apply the required owner, environment, and run ID tags to each managed resource. The governed disposable-workload hierarchy uses this resource tags operation to label resources so cost and ownership queries can find them within the approved scope.
- **C — Incorrect.** Choose an approved metadata location while selecting each resource's supported deployment region independently.
  Choose an approved metadata location while selecting each resource's supported deployment region independently. In the governed disposable-workload hierarchy, this action changes resource group location. Resource group location does not implement resource tags for governed disposable-workload hierarchy; the governed disposable-workload hierarchy still cannot label resources so cost and ownership queries can find them.
- **D — Incorrect.** Place subscriptions beneath the approved management group before applying inherited governance.
  Place subscriptions beneath the approved management group before applying inherited governance. In the governed disposable-workload hierarchy, this action changes management group hierarchy. Governed disposable-workload hierarchy instead needs resource tags: Apply the required owner, environment, and run ID tags to each managed resource. The management group hierarchy action omits that resource tags work.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q16 — B

**Question:** For the governed disposable-workload hierarchy, operators need to avoid assuming that a parent label automatically appears on every child. Which change realizes that requirement?

- **A — Incorrect.** Use ReadOnly only when the operational impact of blocking updates is acceptable.
  Use ReadOnly only when the operational impact of blocking updates is acceptable. In the governed disposable-workload hierarchy, this action changes ReadOnly locks. Governed disposable-workload hierarchy requires tag inheritance limitations; changing ReadOnly locks leaves tag inheritance limitations absent in governed disposable-workload hierarchy; governed disposable-workload hierarchy cannot avoid assuming that a parent label automatically appears on every child.
- **B — Correct.** Use Azure Policy or explicit automation when child resources must receive parent tag values.
  For the governed disposable-workload hierarchy, the required tag inheritance limitations action is: use Azure Policy or explicit automation when child resources must receive parent tag values. It makes the environment able to avoid assuming that a parent label automatically appears on every child.
- **C — Incorrect.** Group resources that share ownership and lifecycle into a deliberately scoped resource group.
  Group resources that share ownership and lifecycle into a deliberately scoped resource group. In the governed disposable-workload hierarchy, this action changes resource group lifecycle. Governed disposable-workload hierarchy instead needs tag inheritance limitations: Use Azure Policy or explicit automation when child resources must receive parent tag values. The resource group lifecycle action omits that tag inheritance limitations work.
- **D — Incorrect.** Assign shared governance at the lowest management group that contains every intended subscription.
  Assign shared governance at the lowest management group that contains every intended subscription. In the governed disposable-workload hierarchy, this action changes management group inheritance. Governed disposable-workload hierarchy approved tag inheritance limitations, not management group inheritance; only the tag inheritance limitations change can avoid assuming that a parent label automatically appears on every child.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q17 — C

**Question:** Operators must automate the governed disposable-workload hierarchy change needed to prevent accidental deletion while still allowing supported updates. Which resource hierarchy operation belongs in the runbook?

- **A — Incorrect.** Validate every dependent resource and destination prerequisite before starting the move.
  Validate every dependent resource and destination prerequisite before starting the move. In the governed disposable-workload hierarchy, this action changes resource moves. Resource moves does not implement CanNotDelete locks for governed disposable-workload hierarchy; the governed disposable-workload hierarchy still cannot prevent accidental deletion while still allowing supported updates.
- **B — Incorrect.** Set and re-read the intended subscription before creating any resource group.
  Set and re-read the intended subscription before creating any resource group. In the governed disposable-workload hierarchy, this action changes subscription context. Governed disposable-workload hierarchy instead needs CanNotDelete locks: Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. The subscription context action omits that CanNotDelete locks work.
- **C — Correct.** Apply a CanNotDelete lock at the narrowest scope that requires deletion protection.
  Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. This changes CanNotDelete locks in the governed disposable-workload hierarchy, supplying the missing state needed to prevent accidental deletion while still allowing supported updates.
- **D — Incorrect.** Apply the required owner, environment, and run ID tags to each managed resource.
  Apply the required owner, environment, and run ID tags to each managed resource. In the governed disposable-workload hierarchy, this action changes resource tags. Governed disposable-workload hierarchy requires CanNotDelete locks; changing resource tags leaves CanNotDelete locks absent in governed disposable-workload hierarchy; governed disposable-workload hierarchy cannot prevent accidental deletion while still allowing supported updates.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q18 — A

**Question:** A governed disposable-workload hierarchy review finds resource hierarchy drift from the need to prevent both deletion and control-plane modification of a protected resource. Which correction addresses that drift?

- **A — Correct.** Use ReadOnly only when the operational impact of blocking updates is acceptable.
  The governed disposable-workload hierarchy must prevent both deletion and control-plane modification of a protected resource; this option performs its direct ReadOnly locks change: use ReadOnly only when the operational impact of blocking updates is acceptable.
- **B — Incorrect.** Choose an approved metadata location while selecting each resource's supported deployment region independently.
  Choose an approved metadata location while selecting each resource's supported deployment region independently. In the governed disposable-workload hierarchy, this action changes resource group location. Governed disposable-workload hierarchy approved ReadOnly locks, not resource group location; only the ReadOnly locks change can prevent both deletion and control-plane modification of a protected resource.
- **C — Incorrect.** Place subscriptions beneath the approved management group before applying inherited governance.
  Place subscriptions beneath the approved management group before applying inherited governance. In the governed disposable-workload hierarchy, this action changes management group hierarchy. Governed disposable-workload hierarchy requires ReadOnly locks; changing management group hierarchy leaves ReadOnly locks absent in governed disposable-workload hierarchy; governed disposable-workload hierarchy cannot prevent both deletion and control-plane modification of a protected resource.
- **D — Incorrect.** Use Azure Policy or explicit automation when child resources must receive parent tag values.
  Use Azure Policy or explicit automation when child resources must receive parent tag values. In the governed disposable-workload hierarchy, this action changes tag inheritance limitations. Tag inheritance limitations does not implement ReadOnly locks for governed disposable-workload hierarchy; the governed disposable-workload hierarchy still cannot prevent both deletion and control-plane modification of a protected resource.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q19 — C

**Question:** The governed disposable-workload hierarchy window permits only the resource hierarchy change needed to relocate supported resources without recreating them. Which option respects the boundary?

- **A — Incorrect.** Group resources that share ownership and lifecycle into a deliberately scoped resource group.
  Group resources that share ownership and lifecycle into a deliberately scoped resource group. In the governed disposable-workload hierarchy, this action changes resource group lifecycle. Governed disposable-workload hierarchy approved resource moves, not resource group lifecycle; only the resource moves change can relocate supported resources without recreating them.
- **B — Incorrect.** Assign shared governance at the lowest management group that contains every intended subscription.
  Assign shared governance at the lowest management group that contains every intended subscription. In the governed disposable-workload hierarchy, this action changes management group inheritance. Governed disposable-workload hierarchy requires resource moves; changing management group inheritance leaves resource moves absent in governed disposable-workload hierarchy; governed disposable-workload hierarchy cannot relocate supported resources without recreating them.
- **C — Correct.** Validate every dependent resource and destination prerequisite before starting the move.
  Validate every dependent resource and destination prerequisite before starting the move. It is the least-change resource moves path for the governed disposable-workload hierarchy requirement to relocate supported resources without recreating them.
- **D — Incorrect.** Apply a CanNotDelete lock at the narrowest scope that requires deletion protection.
  Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. In the governed disposable-workload hierarchy, this action changes CanNotDelete locks. Governed disposable-workload hierarchy instead needs resource moves: Validate every dependent resource and destination prerequisite before starting the move. The CanNotDelete locks action omits that resource moves work.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)

**Source reviewed:** 2026-08-31

## LAB04-Q20 — A

**Question:** The resource hierarchy preflight has passed; the governed disposable-workload hierarchy must now choose the metadata region for a deployment boundary independently of its resources. Which operation should run?

- **A — Correct.** Choose an approved metadata location while selecting each resource's supported deployment region independently.
  Choose an approved metadata location while selecting each resource's supported deployment region independently. In governed disposable-workload hierarchy, applying resource group location is the scoped way to choose the metadata region for a deployment boundary independently of its resources.
- **B — Incorrect.** Set and re-read the intended subscription before creating any resource group.
  Set and re-read the intended subscription before creating any resource group. In the governed disposable-workload hierarchy, this action changes subscription context. Subscription context does not implement resource group location for governed disposable-workload hierarchy; the governed disposable-workload hierarchy still cannot choose the metadata region for a deployment boundary independently of its resources.
- **C — Incorrect.** Apply the required owner, environment, and run ID tags to each managed resource.
  Apply the required owner, environment, and run ID tags to each managed resource. In the governed disposable-workload hierarchy, this action changes resource tags. Governed disposable-workload hierarchy instead needs resource group location: Choose an approved metadata location while selecting each resource's supported deployment region independently. The resource tags action omits that resource group location work.
- **D — Incorrect.** Use ReadOnly only when the operational impact of blocking updates is acceptable.
  Use ReadOnly only when the operational impact of blocking updates is acceptable. In the governed disposable-workload hierarchy, this action changes ReadOnly locks. Governed disposable-workload hierarchy approved resource group location, not ReadOnly locks; only the resource group location change can choose the metadata region for a deployment boundary independently of its resources.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q21 — B

**Question:** Before governed disposable-workload hierarchy cleanup, the resource hierarchy team must reconfirm it can create and later remove one owned deployment boundary. Which read-only inspection should run?

- **A — Incorrect.** Inspect the descendant subscription and identify the inherited assignment's management-group scope.
  Inspect the descendant subscription and identify the inherited assignment's management-group scope. In the governed disposable-workload hierarchy, this check observes management group inheritance. Governed disposable-workload hierarchy output covers management group inheritance, not resource group lifecycle; the resource group lifecycle requirement to create and later remove one owned deployment boundary remains unverified.
- **B — Correct.** List the group's resources and verify every managed resource carries the expected lab ownership tag.
  List the group's resources and verify every managed resource carries the expected lab ownership tag. The governed disposable-workload hierarchy reads resource group lifecycle directly; that resource group lifecycle result proves the governed disposable-workload hierarchy can create and later remove one owned deployment boundary without another mutation.
- **C — Incorrect.** Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
  Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied. In the governed disposable-workload hierarchy, this check observes CanNotDelete locks. Governed disposable-workload hierarchy reads CanNotDelete locks, leaving resource group lifecycle unproved in governed disposable-workload hierarchy; governed disposable-workload hierarchy still has no resource group lifecycle proof.
- **D — Incorrect.** Query the resource group location and each contained resource location as separate values.
  Query the resource group location and each contained resource location as separate values. In the governed disposable-workload hierarchy, this check observes resource group location. Governed disposable-workload hierarchy could pass resource group location while resource group lifecycle is wrong; governed disposable-workload hierarchy still lacks resource group lifecycle proof.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q22 — D

**Question:** The governed disposable-workload hierarchy setup reports success after the resource hierarchy attempt to prevent commands from targeting the wrong Azure subscription. Which resource hierarchy read-only observation proves the governed disposable-workload hierarchy outcome?

- **A — Incorrect.** Query resource tags and compare every required key and exact expected value.
  Query resource tags and compare every required key and exact expected value. In the governed disposable-workload hierarchy, this check observes resource tags. Resource tags success in governed disposable-workload hierarchy cannot verify subscription context; governed disposable-workload hierarchy cannot prevent commands from targeting the wrong Azure subscription until subscription context evidence exists.
- **B — Incorrect.** List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
  List locks at the target scope and test a harmless control-plane update in the break/fix exercise. In the governed disposable-workload hierarchy, this check observes ReadOnly locks. Governed disposable-workload hierarchy reads ReadOnly locks, leaving subscription context unproved in governed disposable-workload hierarchy; governed disposable-workload hierarchy still has no subscription context proof.
- **C — Incorrect.** List the group's resources and verify every managed resource carries the expected lab ownership tag.
  List the group's resources and verify every managed resource carries the expected lab ownership tag. In the governed disposable-workload hierarchy, this check observes resource group lifecycle. Governed disposable-workload hierarchy could pass resource group lifecycle while subscription context is wrong; governed disposable-workload hierarchy still lacks subscription context proof.
- **D — Correct.** Compare az account show output with the approved subscription and tenant IDs.
  For the governed disposable-workload hierarchy, this subscription context observation is decisive: compare az account show output with the approved subscription and tenant IDs. It is governed disposable-workload hierarchy evidence that operators can prevent commands from targeting the wrong Azure subscription.

**Objectives:** `IG-GOVERN-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Manage Azure subscriptions with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q23 — C

**Question:** The resource hierarchy log says the governed disposable-workload hierarchy can now organize subscriptions under the intended governance parent. Which resource hierarchy state should the governed disposable-workload hierarchy acceptance test retain?

- **A — Incorrect.** Query both parent and child resources to prove the required tag exists on each child.
  Query both parent and child resources to prove the required tag exists on each child. In the governed disposable-workload hierarchy, this check observes tag inheritance limitations. Governed disposable-workload hierarchy reads tag inheritance limitations, leaving management group hierarchy unproved in governed disposable-workload hierarchy; governed disposable-workload hierarchy still has no management group hierarchy proof.
- **B — Incorrect.** Run move validation and then query the resource ID and dependencies in the destination scope.
  Run move validation and then query the resource ID and dependencies in the destination scope. In the governed disposable-workload hierarchy, this check observes resource moves. Governed disposable-workload hierarchy could pass resource moves while management group hierarchy is wrong; governed disposable-workload hierarchy still lacks management group hierarchy proof.
- **C — Correct.** Query the hierarchy and confirm each subscription's parent management group ID.
  Query the hierarchy and confirm each subscription's parent management group ID. Because the governed disposable-workload hierarchy check observes management group hierarchy, it independently verifies the requirement to organize subscriptions under the intended governance parent.
- **D — Incorrect.** Compare az account show output with the approved subscription and tenant IDs.
  Compare az account show output with the approved subscription and tenant IDs. In the governed disposable-workload hierarchy, this check observes subscription context. Subscription context success in governed disposable-workload hierarchy cannot verify management group hierarchy; governed disposable-workload hierarchy cannot organize subscriptions under the intended governance parent until management group hierarchy evidence exists.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q24 — A

**Question:** The governed disposable-workload hierarchy rejects resource hierarchy exit status as proof it can apply parent governance consistently to descendant subscriptions. Which governed disposable-workload hierarchy result is valid evidence?

- **A — Correct.** Inspect the descendant subscription and identify the inherited assignment's management-group scope.
  The governed disposable-workload hierarchy validator needs this management group inheritance result: inspect the descendant subscription and identify the inherited assignment's management-group scope. It proves the outcome to apply parent governance consistently to descendant subscriptions rather than an adjacent checkpoint.
- **B — Incorrect.** Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
  Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied. In the governed disposable-workload hierarchy, this check observes CanNotDelete locks. Governed disposable-workload hierarchy output covers CanNotDelete locks, not management group inheritance; the management group inheritance requirement to apply parent governance consistently to descendant subscriptions remains unverified.
- **C — Incorrect.** Query the resource group location and each contained resource location as separate values.
  Query the resource group location and each contained resource location as separate values. In the governed disposable-workload hierarchy, this check observes resource group location. Resource group location success in governed disposable-workload hierarchy cannot verify management group inheritance; governed disposable-workload hierarchy cannot apply parent governance consistently to descendant subscriptions until management group inheritance evidence exists.
- **D — Incorrect.** Query the hierarchy and confirm each subscription's parent management group ID.
  Query the hierarchy and confirm each subscription's parent management group ID. In the governed disposable-workload hierarchy, this check observes management group hierarchy. Governed disposable-workload hierarchy reads management group hierarchy, leaving management group inheritance unproved in governed disposable-workload hierarchy; governed disposable-workload hierarchy still has no management group inheritance proof.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q25 — C

**Question:** The resource hierarchy validator needs one governed disposable-workload hierarchy query after the change to label resources so cost and ownership queries can find them. Which resource hierarchy property should the governed disposable-workload hierarchy validator inspect?

- **A — Incorrect.** List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
  List locks at the target scope and test a harmless control-plane update in the break/fix exercise. In the governed disposable-workload hierarchy, this check observes ReadOnly locks. Governed disposable-workload hierarchy output covers ReadOnly locks, not resource tags; the resource tags requirement to label resources so cost and ownership queries can find them remains unverified.
- **B — Incorrect.** List the group's resources and verify every managed resource carries the expected lab ownership tag.
  List the group's resources and verify every managed resource carries the expected lab ownership tag. In the governed disposable-workload hierarchy, this check observes resource group lifecycle. Resource group lifecycle success in governed disposable-workload hierarchy cannot verify resource tags; governed disposable-workload hierarchy cannot label resources so cost and ownership queries can find them until resource tags evidence exists.
- **C — Correct.** Query resource tags and compare every required key and exact expected value.
  Query resource tags and compare every required key and exact expected value. This is independent resource tags evidence for the governed disposable-workload hierarchy, even if governed disposable-workload hierarchy setup reports success before resource tags becomes observable.
- **D — Incorrect.** Inspect the descendant subscription and identify the inherited assignment's management-group scope.
  Inspect the descendant subscription and identify the inherited assignment's management-group scope. In the governed disposable-workload hierarchy, this check observes management group inheritance. Governed disposable-workload hierarchy could pass management group inheritance while resource tags is wrong; governed disposable-workload hierarchy still lacks resource tags proof.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q26 — A

**Question:** The governance administrator organizing disposable workloads must confirm the governed disposable-workload hierarchy, without mutation, can avoid assuming that a parent label automatically appears on every child. Which resource hierarchy check qualifies?

- **A — Correct.** Query both parent and child resources to prove the required tag exists on each child.
  Query both parent and child resources to prove the required tag exists on each child. For governed disposable-workload hierarchy, this tag inheritance limitations read confirms the service can avoid assuming that a parent label automatically appears on every child.
- **B — Incorrect.** Run move validation and then query the resource ID and dependencies in the destination scope.
  Run move validation and then query the resource ID and dependencies in the destination scope. In the governed disposable-workload hierarchy, this check observes resource moves. Governed disposable-workload hierarchy reads resource moves, leaving tag inheritance limitations unproved in governed disposable-workload hierarchy; governed disposable-workload hierarchy still has no tag inheritance limitations proof.
- **C — Incorrect.** Compare az account show output with the approved subscription and tenant IDs.
  Compare az account show output with the approved subscription and tenant IDs. In the governed disposable-workload hierarchy, this check observes subscription context. Governed disposable-workload hierarchy could pass subscription context while tag inheritance limitations is wrong; governed disposable-workload hierarchy still lacks tag inheritance limitations proof.
- **D — Incorrect.** Query resource tags and compare every required key and exact expected value.
  Query resource tags and compare every required key and exact expected value. In the governed disposable-workload hierarchy, this check observes resource tags. Governed disposable-workload hierarchy output covers resource tags, not tag inheritance limitations; the tag inheritance limitations requirement to avoid assuming that a parent label automatically appears on every child remains unverified.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q27 — B

**Question:** The governed disposable-workload hierarchy configuration is complete; the resource hierarchy reviewers need evidence it can prevent accidental deletion while still allowing supported updates. Which observation shows success?

- **A — Incorrect.** Query the resource group location and each contained resource location as separate values.
  Query the resource group location and each contained resource location as separate values. In the governed disposable-workload hierarchy, this check observes resource group location. Governed disposable-workload hierarchy reads resource group location, leaving CanNotDelete locks unproved in governed disposable-workload hierarchy; governed disposable-workload hierarchy still has no CanNotDelete locks proof.
- **B — Correct.** Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
  Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied. The governed disposable-workload hierarchy reads CanNotDelete locks directly; that CanNotDelete locks result proves the governed disposable-workload hierarchy can prevent accidental deletion while still allowing supported updates without another mutation.
- **C — Incorrect.** Query the hierarchy and confirm each subscription's parent management group ID.
  Query the hierarchy and confirm each subscription's parent management group ID. In the governed disposable-workload hierarchy, this check observes management group hierarchy. Governed disposable-workload hierarchy output covers management group hierarchy, not CanNotDelete locks; the CanNotDelete locks requirement to prevent accidental deletion while still allowing supported updates remains unverified.
- **D — Incorrect.** Query both parent and child resources to prove the required tag exists on each child.
  Query both parent and child resources to prove the required tag exists on each child. In the governed disposable-workload hierarchy, this check observes tag inheritance limitations. Tag inheritance limitations success in governed disposable-workload hierarchy cannot verify CanNotDelete locks; governed disposable-workload hierarchy cannot prevent accidental deletion while still allowing supported updates until CanNotDelete locks evidence exists.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q28 — D

**Question:** The resource hierarchy validation asks whether the governed disposable-workload hierarchy can prevent both deletion and control-plane modification of a protected resource. Which observable state is strongest?

- **A — Incorrect.** List the group's resources and verify every managed resource carries the expected lab ownership tag.
  List the group's resources and verify every managed resource carries the expected lab ownership tag. In the governed disposable-workload hierarchy, this check observes resource group lifecycle. Governed disposable-workload hierarchy could pass resource group lifecycle while ReadOnly locks is wrong; governed disposable-workload hierarchy still lacks ReadOnly locks proof.
- **B — Incorrect.** Inspect the descendant subscription and identify the inherited assignment's management-group scope.
  Inspect the descendant subscription and identify the inherited assignment's management-group scope. In the governed disposable-workload hierarchy, this check observes management group inheritance. Governed disposable-workload hierarchy output covers management group inheritance, not ReadOnly locks; the ReadOnly locks requirement to prevent both deletion and control-plane modification of a protected resource remains unverified.
- **C — Incorrect.** Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
  Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied. In the governed disposable-workload hierarchy, this check observes CanNotDelete locks. CanNotDelete locks success in governed disposable-workload hierarchy cannot verify ReadOnly locks; governed disposable-workload hierarchy cannot prevent both deletion and control-plane modification of a protected resource until ReadOnly locks evidence exists.
- **D — Correct.** List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
  For the governed disposable-workload hierarchy, this ReadOnly locks observation is decisive: list locks at the target scope and test a harmless control-plane update in the break/fix exercise. It is governed disposable-workload hierarchy evidence that operators can prevent both deletion and control-plane modification of a protected resource.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q29 — C

**Question:** A governed disposable-workload hierarchy review must prove the resource hierarchy ability to relocate supported resources without recreating them. Which check avoids an adjacent feature?

- **A — Incorrect.** Compare az account show output with the approved subscription and tenant IDs.
  Compare az account show output with the approved subscription and tenant IDs. In the governed disposable-workload hierarchy, this check observes subscription context. Governed disposable-workload hierarchy output covers subscription context, not resource moves; the resource moves requirement to relocate supported resources without recreating them remains unverified.
- **B — Incorrect.** Query resource tags and compare every required key and exact expected value.
  Query resource tags and compare every required key and exact expected value. In the governed disposable-workload hierarchy, this check observes resource tags. Resource tags success in governed disposable-workload hierarchy cannot verify resource moves; governed disposable-workload hierarchy cannot relocate supported resources without recreating them until resource moves evidence exists.
- **C — Correct.** Run move validation and then query the resource ID and dependencies in the destination scope.
  Run move validation and then query the resource ID and dependencies in the destination scope. Because the governed disposable-workload hierarchy check observes resource moves, it independently verifies the requirement to relocate supported resources without recreating them.
- **D — Incorrect.** List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
  List locks at the target scope and test a harmless control-plane update in the break/fix exercise. In the governed disposable-workload hierarchy, this check observes ReadOnly locks. Governed disposable-workload hierarchy could pass ReadOnly locks while resource moves is wrong; governed disposable-workload hierarchy still lacks resource moves proof.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)

**Source reviewed:** 2026-08-31

## LAB04-Q30 — B

**Question:** The governed disposable-workload hierarchy evidence bundle needs a resource hierarchy result showing it can choose the metadata region for a deployment boundary independently of its resources. Which result belongs in the checkpoint?

- **A — Incorrect.** Query the hierarchy and confirm each subscription's parent management group ID.
  Query the hierarchy and confirm each subscription's parent management group ID. In the governed disposable-workload hierarchy, this check observes management group hierarchy. Management group hierarchy success in governed disposable-workload hierarchy cannot verify resource group location; governed disposable-workload hierarchy cannot choose the metadata region for a deployment boundary independently of its resources until resource group location evidence exists.
- **B — Correct.** Query the resource group location and each contained resource location as separate values.
  The governed disposable-workload hierarchy validator needs this resource group location result: query the resource group location and each contained resource location as separate values. It proves the outcome to choose the metadata region for a deployment boundary independently of its resources rather than an adjacent checkpoint.
- **C — Incorrect.** Query both parent and child resources to prove the required tag exists on each child.
  Query both parent and child resources to prove the required tag exists on each child. In the governed disposable-workload hierarchy, this check observes tag inheritance limitations. Governed disposable-workload hierarchy could pass tag inheritance limitations while resource group location is wrong; governed disposable-workload hierarchy still lacks resource group location proof.
- **D — Incorrect.** Run move validation and then query the resource ID and dependencies in the destination scope.
  Run move validation and then query the resource ID and dependencies in the destination scope. In the governed disposable-workload hierarchy, this check observes resource moves. Governed disposable-workload hierarchy output covers resource moves, not resource group location; the resource group location requirement to choose the metadata region for a deployment boundary independently of its resources remains unverified.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q31 — D

**Question:** Other governed disposable-workload hierarchy components are healthy, but the resource hierarchy still cannot create and later remove one owned deployment boundary. Which state causes the isolated failure?

- **A — Incorrect.** The active subscription changed after sign-in and points at an unapproved environment.
  The active subscription changed after sign-in and points at an unapproved environment. The governed disposable-workload hierarchy fault concerns subscription context. Governed disposable-workload hierarchy has subscription context impact, but resource group lifecycle is the governed disposable-workload hierarchy failed path; the subscription context state cannot produce resource group lifecycle failure.
- **B — Incorrect.** The runbook assumed a resource inherited its resource group's tags automatically.
  The runbook assumed a resource inherited its resource group's tags automatically. The governed disposable-workload hierarchy fault concerns tag inheritance limitations. Governed disposable-workload hierarchy could repair tag inheritance limitations while resource group lifecycle stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to create and later remove one owned deployment boundary.
- **C — Incorrect.** The design assumes all resources must share the resource group's metadata location.
  The design assumes all resources must share the resource group's metadata location. The governed disposable-workload hierarchy fault concerns resource group location. Governed disposable-workload hierarchy failed on resource group lifecycle; this resource group location finding redirects governed disposable-workload hierarchy remediation away from resource group lifecycle.
- **D — Correct.** Cleanup targets a resource group that contains resources outside the lab's ownership boundary.
  Cleanup targets a resource group that contains resources outside the lab's ownership boundary. Removing this resource group lifecycle condition lets the governed disposable-workload hierarchy create and later remove one owned deployment boundary while leaving healthy controls unchanged.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q32 — C

**Question:** During a resource hierarchy fault drill, the governed disposable-workload hierarchy does not prevent commands from targeting the wrong Azure subscription. Which finding identifies the defect?

- **A — Incorrect.** The subscription remains attached to a different management-group branch.
  The subscription remains attached to a different management-group branch. The governed disposable-workload hierarchy fault concerns management group hierarchy. Governed disposable-workload hierarchy could repair management group hierarchy while subscription context stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to prevent commands from targeting the wrong Azure subscription.
- **B — Incorrect.** Cleanup begins before removing the lab-owned CanNotDelete lock.
  Cleanup begins before removing the lab-owned CanNotDelete lock. The governed disposable-workload hierarchy fault concerns CanNotDelete locks. Governed disposable-workload hierarchy failed on subscription context; this CanNotDelete locks finding redirects governed disposable-workload hierarchy remediation away from subscription context.
- **C — Correct.** The active subscription changed after sign-in and points at an unapproved environment.
  The active subscription changed after sign-in and points at an unapproved environment. In governed disposable-workload hierarchy, this subscription context cause matches the failure to prevent commands from targeting the wrong Azure subscription.
- **D — Incorrect.** Cleanup targets a resource group that contains resources outside the lab's ownership boundary.
  Cleanup targets a resource group that contains resources outside the lab's ownership boundary. The governed disposable-workload hierarchy fault concerns resource group lifecycle. Governed disposable-workload hierarchy has resource group lifecycle impact, but subscription context is the governed disposable-workload hierarchy failed path; the resource group lifecycle state cannot produce subscription context failure.

**Objectives:** `IG-GOVERN-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Manage Azure subscriptions with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q33 — C

**Question:** The governed disposable-workload hierarchy setup finishes, yet the resource hierarchy cannot organize subscriptions under the intended governance parent. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The assignment was created on a sibling management group with no ancestor relationship to the subscription.
  The assignment was created on a sibling management group with no ancestor relationship to the subscription. The governed disposable-workload hierarchy fault concerns management group inheritance. Governed disposable-workload hierarchy failed on management group hierarchy; this management group inheritance finding redirects governed disposable-workload hierarchy remediation away from management group hierarchy.
- **B — Incorrect.** A ReadOnly lock prevents a service from updating configuration that its normal operation requires.
  A ReadOnly lock prevents a service from updating configuration that its normal operation requires. The governed disposable-workload hierarchy fault concerns ReadOnly locks. Governed disposable-workload hierarchy may fix ReadOnly locks, yet management group hierarchy still fails; this governed disposable-workload hierarchy diagnosis of ReadOnly locks is wrong for management group hierarchy.
- **C — Correct.** The subscription remains attached to a different management-group branch.
  The subscription remains attached to a different management-group branch. This governed disposable-workload hierarchy condition breaks management group hierarchy, explaining why operators cannot organize subscriptions under the intended governance parent.
- **D — Incorrect.** The active subscription changed after sign-in and points at an unapproved environment.
  The active subscription changed after sign-in and points at an unapproved environment. The governed disposable-workload hierarchy fault concerns subscription context. Governed disposable-workload hierarchy could repair subscription context while management group hierarchy stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to organize subscriptions under the intended governance parent.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q34 — B

**Question:** A resource hierarchy break/fix in the governed disposable-workload hierarchy fails when operators try to apply parent governance consistently to descendant subscriptions. Which diagnosis fits?

- **A — Incorrect.** A required tag value differs in case from the value used by the cost-reporting convention.
  A required tag value differs in case from the value used by the cost-reporting convention. The governed disposable-workload hierarchy fault concerns resource tags. Governed disposable-workload hierarchy may fix resource tags, yet management group inheritance still fails; this governed disposable-workload hierarchy diagnosis of resource tags is wrong for management group inheritance.
- **B — Correct.** The assignment was created on a sibling management group with no ancestor relationship to the subscription.
  For the governed disposable-workload hierarchy, the management group inheritance failure is causal: the assignment was created on a sibling management group with no ancestor relationship to the subscription. Correcting it restores the ability to apply parent governance consistently to descendant subscriptions.
- **C — Incorrect.** A dependent resource that must move with the target was omitted from the move request.
  A dependent resource that must move with the target was omitted from the move request. The governed disposable-workload hierarchy fault concerns resource moves. Governed disposable-workload hierarchy could repair resource moves while management group inheritance stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to apply parent governance consistently to descendant subscriptions.
- **D — Incorrect.** The subscription remains attached to a different management-group branch.
  The subscription remains attached to a different management-group branch. The governed disposable-workload hierarchy fault concerns management group hierarchy. Governed disposable-workload hierarchy failed on management group inheritance; this management group hierarchy finding redirects governed disposable-workload hierarchy remediation away from management group inheritance.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q35 — C

**Question:** The governed disposable-workload hierarchy troubleshooting scope is the resource hierarchy need to label resources so cost and ownership queries can find them. Which condition should be corrected first?

- **A — Incorrect.** The runbook assumed a resource inherited its resource group's tags automatically.
  The runbook assumed a resource inherited its resource group's tags automatically. The governed disposable-workload hierarchy fault concerns tag inheritance limitations. Governed disposable-workload hierarchy has tag inheritance limitations impact, but resource tags is the governed disposable-workload hierarchy failed path; the tag inheritance limitations state cannot produce resource tags failure.
- **B — Incorrect.** The design assumes all resources must share the resource group's metadata location.
  The design assumes all resources must share the resource group's metadata location. The governed disposable-workload hierarchy fault concerns resource group location. Governed disposable-workload hierarchy could repair resource group location while resource tags stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to label resources so cost and ownership queries can find them.
- **C — Correct.** A required tag value differs in case from the value used by the cost-reporting convention.
  A required tag value differs in case from the value used by the cost-reporting convention. The finding is specific to resource tags in the governed disposable-workload hierarchy; repairing resource tags restores the governed disposable-workload hierarchy ability to label resources so cost and ownership queries can find them.
- **D — Incorrect.** The assignment was created on a sibling management group with no ancestor relationship to the subscription.
  The assignment was created on a sibling management group with no ancestor relationship to the subscription. The governed disposable-workload hierarchy fault concerns management group inheritance. Governed disposable-workload hierarchy may fix management group inheritance, yet resource tags still fails; this governed disposable-workload hierarchy diagnosis of management group inheritance is wrong for resource tags.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q36 — D

**Question:** The governed disposable-workload hierarchy result is partial because the resource hierarchy cannot avoid assuming that a parent label automatically appears on every child. Which condition accounts for that result?

- **A — Incorrect.** Cleanup begins before removing the lab-owned CanNotDelete lock.
  Cleanup begins before removing the lab-owned CanNotDelete lock. The governed disposable-workload hierarchy fault concerns CanNotDelete locks. Governed disposable-workload hierarchy could repair CanNotDelete locks while tag inheritance limitations stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to avoid assuming that a parent label automatically appears on every child.
- **B — Incorrect.** Cleanup targets a resource group that contains resources outside the lab's ownership boundary.
  Cleanup targets a resource group that contains resources outside the lab's ownership boundary. The governed disposable-workload hierarchy fault concerns resource group lifecycle. Governed disposable-workload hierarchy failed on tag inheritance limitations; this resource group lifecycle finding redirects governed disposable-workload hierarchy remediation away from tag inheritance limitations.
- **C — Incorrect.** A required tag value differs in case from the value used by the cost-reporting convention.
  A required tag value differs in case from the value used by the cost-reporting convention. The governed disposable-workload hierarchy fault concerns resource tags. Governed disposable-workload hierarchy may fix resource tags, yet tag inheritance limitations still fails; this governed disposable-workload hierarchy diagnosis of resource tags is wrong for tag inheritance limitations.
- **D — Correct.** The runbook assumed a resource inherited its resource group's tags automatically.
  The governed disposable-workload hierarchy cannot avoid assuming that a parent label automatically appears on every child because of this tag inheritance limitations defect: the runbook assumed a resource inherited its resource group's tags automatically. The symptom and repair align.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q37 — D

**Question:** The resource hierarchy evidence shows the governed disposable-workload hierarchy cannot prevent accidental deletion while still allowing supported updates. Which root cause fits that evidence?

- **A — Incorrect.** A ReadOnly lock prevents a service from updating configuration that its normal operation requires.
  A ReadOnly lock prevents a service from updating configuration that its normal operation requires. The governed disposable-workload hierarchy fault concerns ReadOnly locks. Governed disposable-workload hierarchy failed on CanNotDelete locks; this ReadOnly locks finding redirects governed disposable-workload hierarchy remediation away from CanNotDelete locks.
- **B — Incorrect.** The active subscription changed after sign-in and points at an unapproved environment.
  The active subscription changed after sign-in and points at an unapproved environment. The governed disposable-workload hierarchy fault concerns subscription context. Governed disposable-workload hierarchy may fix subscription context, yet CanNotDelete locks still fails; this governed disposable-workload hierarchy diagnosis of subscription context is wrong for CanNotDelete locks.
- **C — Incorrect.** The runbook assumed a resource inherited its resource group's tags automatically.
  The runbook assumed a resource inherited its resource group's tags automatically. The governed disposable-workload hierarchy fault concerns tag inheritance limitations. Governed disposable-workload hierarchy has tag inheritance limitations impact, but CanNotDelete locks is the governed disposable-workload hierarchy failed path; the tag inheritance limitations state cannot produce CanNotDelete locks failure.
- **D — Correct.** Cleanup begins before removing the lab-owned CanNotDelete lock.
  Cleanup begins before removing the lab-owned CanNotDelete lock. Removing this CanNotDelete locks condition lets the governed disposable-workload hierarchy prevent accidental deletion while still allowing supported updates while leaving healthy controls unchanged.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q38 — D

**Question:** Although the governed disposable-workload hierarchy is meant to let the resource hierarchy prevent both deletion and control-plane modification of a protected resource, its checkpoint fails. Which resource hierarchy defect explains the failure?

- **A — Incorrect.** A dependent resource that must move with the target was omitted from the move request.
  A dependent resource that must move with the target was omitted from the move request. The governed disposable-workload hierarchy fault concerns resource moves. Governed disposable-workload hierarchy may fix resource moves, yet ReadOnly locks still fails; this governed disposable-workload hierarchy diagnosis of resource moves is wrong for ReadOnly locks.
- **B — Incorrect.** The subscription remains attached to a different management-group branch.
  The subscription remains attached to a different management-group branch. The governed disposable-workload hierarchy fault concerns management group hierarchy. Governed disposable-workload hierarchy has management group hierarchy impact, but ReadOnly locks is the governed disposable-workload hierarchy failed path; the management group hierarchy state cannot produce ReadOnly locks failure.
- **C — Incorrect.** Cleanup begins before removing the lab-owned CanNotDelete lock.
  Cleanup begins before removing the lab-owned CanNotDelete lock. The governed disposable-workload hierarchy fault concerns CanNotDelete locks. Governed disposable-workload hierarchy could repair CanNotDelete locks while ReadOnly locks stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to prevent both deletion and control-plane modification of a protected resource.
- **D — Correct.** A ReadOnly lock prevents a service from updating configuration that its normal operation requires.
  A ReadOnly lock prevents a service from updating configuration that its normal operation requires. In governed disposable-workload hierarchy, this ReadOnly locks cause matches the failure to prevent both deletion and control-plane modification of a protected resource.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q39 — A

**Question:** The resource hierarchy support team isolated the governed disposable-workload hierarchy incident to the attempt to relocate supported resources without recreating them. Which condition prevents success?

- **A — Correct.** A dependent resource that must move with the target was omitted from the move request.
  A dependent resource that must move with the target was omitted from the move request. This governed disposable-workload hierarchy condition breaks resource moves, explaining why operators cannot relocate supported resources without recreating them.
- **B — Incorrect.** The design assumes all resources must share the resource group's metadata location.
  The design assumes all resources must share the resource group's metadata location. The governed disposable-workload hierarchy fault concerns resource group location. Governed disposable-workload hierarchy could repair resource group location while resource moves stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to relocate supported resources without recreating them.
- **C — Incorrect.** The assignment was created on a sibling management group with no ancestor relationship to the subscription.
  The assignment was created on a sibling management group with no ancestor relationship to the subscription. The governed disposable-workload hierarchy fault concerns management group inheritance. Governed disposable-workload hierarchy failed on resource moves; this management group inheritance finding redirects governed disposable-workload hierarchy remediation away from resource moves.
- **D — Incorrect.** A ReadOnly lock prevents a service from updating configuration that its normal operation requires.
  A ReadOnly lock prevents a service from updating configuration that its normal operation requires. The governed disposable-workload hierarchy fault concerns ReadOnly locks. Governed disposable-workload hierarchy may fix ReadOnly locks, yet resource moves still fails; this governed disposable-workload hierarchy diagnosis of ReadOnly locks is wrong for resource moves.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)

**Source reviewed:** 2026-08-31

## LAB04-Q40 — C

**Question:** A governed disposable-workload hierarchy query surprises the governance administrator organizing disposable workloads during the resource hierarchy attempt to choose the metadata region for a deployment boundary independently of its resources. Which finding explains it?

- **A — Incorrect.** Cleanup targets a resource group that contains resources outside the lab's ownership boundary.
  Cleanup targets a resource group that contains resources outside the lab's ownership boundary. The governed disposable-workload hierarchy fault concerns resource group lifecycle. Governed disposable-workload hierarchy could repair resource group lifecycle while resource group location stays broken in governed disposable-workload hierarchy; the governed disposable-workload hierarchy remains unable to choose the metadata region for a deployment boundary independently of its resources.
- **B — Incorrect.** A required tag value differs in case from the value used by the cost-reporting convention.
  A required tag value differs in case from the value used by the cost-reporting convention. The governed disposable-workload hierarchy fault concerns resource tags. Governed disposable-workload hierarchy failed on resource group location; this resource tags finding redirects governed disposable-workload hierarchy remediation away from resource group location.
- **C — Correct.** The design assumes all resources must share the resource group's metadata location.
  For the governed disposable-workload hierarchy, the resource group location failure is causal: the design assumes all resources must share the resource group's metadata location. Correcting it restores the ability to choose the metadata region for a deployment boundary independently of its resources.
- **D — Incorrect.** A dependent resource that must move with the target was omitted from the move request.
  A dependent resource that must move with the target was omitted from the move request. The governed disposable-workload hierarchy fault concerns resource moves. Governed disposable-workload hierarchy has resource moves impact, but resource group location is the governed disposable-workload hierarchy failed path; the resource moves state cannot produce resource group location failure.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q41 — B

**Question:** The governed disposable-workload hierarchy checkpoint requires both this resource hierarchy outcome—create and later remove one owned deployment boundary—and a read-only governed disposable-workload hierarchy state check. Which resource hierarchy response is complete?

- **A — Incorrect.** First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
  First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID. This governed disposable-workload hierarchy pair serves management group hierarchy. Management group hierarchy cannot replace resource group lifecycle in governed disposable-workload hierarchy. Use this resource group lifecycle pair instead: First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.
- **B — Correct.** First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.
  First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag. The governed disposable-workload hierarchy uses its resource group lifecycle mutation gate and resource group lifecycle verification gate before it can create and later remove one owned deployment boundary.
- **C — Incorrect.** First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
  First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied. This governed disposable-workload hierarchy pair serves CanNotDelete locks. Governed disposable-workload hierarchy uses CanNotDelete locks for both steps; resource group lifecycle remains untouched in governed disposable-workload hierarchy, so its resource group lifecycle gate to create and later remove one owned deployment boundary fails.
- **D — Incorrect.** First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
  First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise. This governed disposable-workload hierarchy pair serves ReadOnly locks. Governed disposable-workload hierarchy closes ReadOnly locks, not resource group lifecycle; without the resource group lifecycle workflow, it cannot create and later remove one owned deployment boundary.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q42 — B

**Question:** The governed disposable-workload hierarchy runbook must prevent commands from targeting the wrong Azure subscription, then retain resource hierarchy read-back evidence. Which governed disposable-workload hierarchy pair completes both duties?

- **A — Incorrect.** First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.
  First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope. This governed disposable-workload hierarchy pair serves management group inheritance. Governed disposable-workload hierarchy proves management group inheritance, but subscription context lacks implementation in governed disposable-workload hierarchy and subscription context proof; the subscription context outcome to prevent commands from targeting the wrong Azure subscription remains open.
- **B — Correct.** First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.
  The governed disposable-workload hierarchy gets a complete subscription context sequence here: first, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs. Read-back evidence follows the change.
- **C — Incorrect.** First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
  First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise. This governed disposable-workload hierarchy pair serves ReadOnly locks. Governed disposable-workload hierarchy closes ReadOnly locks, not subscription context; without the subscription context workflow, it cannot prevent commands from targeting the wrong Azure subscription.
- **D — Incorrect.** First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.
  First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope. This governed disposable-workload hierarchy pair serves resource moves. Resource moves cannot replace subscription context in governed disposable-workload hierarchy. Use this subscription context pair instead: First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.

**Objectives:** `IG-GOVERN-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Manage Azure subscriptions with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q43 — A

**Question:** To satisfy the resource hierarchy requirement, operators must change the governed disposable-workload hierarchy configuration and prove it can organize subscriptions under the intended governance parent. Which sequence is coherent?

- **A — Correct.** First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
  First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID. This ordered management group hierarchy workflow lets the governed disposable-workload hierarchy organize subscriptions under the intended governance parent and then verify the resulting state.
- **B — Incorrect.** First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value.
  First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value. This governed disposable-workload hierarchy pair serves resource tags. Governed disposable-workload hierarchy closes resource tags, not management group hierarchy; without the management group hierarchy workflow, it cannot organize subscriptions under the intended governance parent.
- **C — Incorrect.** First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.
  First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope. This governed disposable-workload hierarchy pair serves resource moves. Resource moves cannot replace management group hierarchy in governed disposable-workload hierarchy. Use this management group hierarchy pair instead: First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
- **D — Incorrect.** First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values.
  First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values. This governed disposable-workload hierarchy pair serves resource group location. Governed disposable-workload hierarchy proves resource group location, but management group hierarchy lacks implementation in governed disposable-workload hierarchy and management group hierarchy proof; the management group hierarchy outcome to organize subscriptions under the intended governance parent remains open.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q44 — C

**Question:** The governance administrator organizing disposable workloads needs a safe governed disposable-workload hierarchy change to apply parent governance consistently to descendant subscriptions, followed by resource hierarchy evidence. Which pair merits approval?

- **A — Incorrect.** First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child.
  First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child. This governed disposable-workload hierarchy pair serves tag inheritance limitations. Governed disposable-workload hierarchy closes tag inheritance limitations, not management group inheritance; without the management group inheritance workflow, it cannot apply parent governance consistently to descendant subscriptions.
- **B — Incorrect.** First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values.
  First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values. This governed disposable-workload hierarchy pair serves resource group location. Resource group location cannot replace management group inheritance in governed disposable-workload hierarchy. Use this management group inheritance pair instead: First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.
- **C — Correct.** First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.
  First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope. For governed disposable-workload hierarchy, the management group inheritance operation precedes its management group inheritance read-back check, allowing it to apply parent governance consistently to descendant subscriptions.
- **D — Incorrect.** First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.
  First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag. This governed disposable-workload hierarchy pair serves resource group lifecycle. Governed disposable-workload hierarchy uses resource group lifecycle for both steps; management group inheritance remains untouched in governed disposable-workload hierarchy, so its management group inheritance gate to apply parent governance consistently to descendant subscriptions fails.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Azure management group hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

**Source reviewed:** 2026-08-31

## LAB04-Q45 — A

**Question:** The governed disposable-workload hierarchy has two resource hierarchy gates: label resources so cost and ownership queries can find them, then prove the governed disposable-workload hierarchy state. Which resource hierarchy sequence works?

- **A — Correct.** First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value.
  First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value. In the governed disposable-workload hierarchy, the first resource tags step runs; the governed disposable-workload hierarchy then reads resource tags state to prove it can label resources so cost and ownership queries can find them.
- **B — Incorrect.** First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
  First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied. This governed disposable-workload hierarchy pair serves CanNotDelete locks. Governed disposable-workload hierarchy proves CanNotDelete locks, but resource tags lacks implementation in governed disposable-workload hierarchy and resource tags proof; the resource tags outcome to label resources so cost and ownership queries can find them remains open.
- **C — Incorrect.** First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.
  First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag. This governed disposable-workload hierarchy pair serves resource group lifecycle. Governed disposable-workload hierarchy uses resource group lifecycle for both steps; resource tags remains untouched in governed disposable-workload hierarchy, so its resource tags gate to label resources so cost and ownership queries can find them fails.
- **D — Incorrect.** First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.
  First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs. This governed disposable-workload hierarchy pair serves subscription context. Governed disposable-workload hierarchy closes subscription context, not resource tags; without the resource tags workflow, it cannot label resources so cost and ownership queries can find them.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q46 — D

**Question:** Which resource hierarchy path makes the governed disposable-workload hierarchy able to avoid assuming that a parent label automatically appears on every child, then inspects the defining properties?

- **A — Incorrect.** First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
  First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise. This governed disposable-workload hierarchy pair serves ReadOnly locks. Governed disposable-workload hierarchy proves ReadOnly locks, but tag inheritance limitations lacks implementation in governed disposable-workload hierarchy and tag inheritance limitations proof; the tag inheritance limitations outcome to avoid assuming that a parent label automatically appears on every child remains open.
- **B — Incorrect.** First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.
  First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs. This governed disposable-workload hierarchy pair serves subscription context. Governed disposable-workload hierarchy uses subscription context for both steps; tag inheritance limitations remains untouched in governed disposable-workload hierarchy, so its tag inheritance limitations gate to avoid assuming that a parent label automatically appears on every child fails.
- **C — Incorrect.** First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
  First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID. This governed disposable-workload hierarchy pair serves management group hierarchy. Governed disposable-workload hierarchy closes management group hierarchy, not tag inheritance limitations; without the tag inheritance limitations workflow, it cannot avoid assuming that a parent label automatically appears on every child.
- **D — Correct.** First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child.
  For the governed disposable-workload hierarchy, the safe tag inheritance limitations order is: first, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child. The governed disposable-workload hierarchy records tag inheritance limitations proof after configuration.

**Objectives:** `IG-GOVERN-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB04-CP01`).

**Microsoft Learn sources:**

- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli)

**Source reviewed:** 2026-08-31

## LAB04-Q47 — B

**Question:** At the governed disposable-workload hierarchy approval gate, operators must show that the resource hierarchy can prevent accidental deletion while still allowing supported updates. Which resource hierarchy configure-and-check pair is defensible?

- **A — Incorrect.** First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.
  First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope. This governed disposable-workload hierarchy pair serves resource moves. Governed disposable-workload hierarchy uses resource moves for both steps; CanNotDelete locks remains untouched in governed disposable-workload hierarchy, so its CanNotDelete locks gate to prevent accidental deletion while still allowing supported updates fails.
- **B — Correct.** First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
  First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied. The governed disposable-workload hierarchy uses its CanNotDelete locks mutation gate and CanNotDelete locks verification gate before it can prevent accidental deletion while still allowing supported updates.
- **C — Incorrect.** First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID.
  First, Place subscriptions beneath the approved management group before applying inherited governance. Then, Query the hierarchy and confirm each subscription's parent management group ID. This governed disposable-workload hierarchy pair serves management group hierarchy. Management group hierarchy cannot replace CanNotDelete locks in governed disposable-workload hierarchy. Use this CanNotDelete locks pair instead: First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
- **D — Incorrect.** First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.
  First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope. This governed disposable-workload hierarchy pair serves management group inheritance. Governed disposable-workload hierarchy proves management group inheritance, but CanNotDelete locks lacks implementation in governed disposable-workload hierarchy and CanNotDelete locks proof; the CanNotDelete locks outcome to prevent accidental deletion while still allowing supported updates remains open.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB04-CP02`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q48 — A

**Question:** The governed disposable-workload hierarchy forbids a partial resource hierarchy result. Operators must first prevent both deletion and control-plane modification of a protected resource and afterward confirm the governed disposable-workload hierarchy outcome. Which resource hierarchy sequence is complete?

- **A — Correct.** First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
  The governed disposable-workload hierarchy gets a complete ReadOnly locks sequence here: first, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise. Read-back evidence follows the change.
- **B — Incorrect.** First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values.
  First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values. This governed disposable-workload hierarchy pair serves resource group location. Resource group location cannot replace ReadOnly locks in governed disposable-workload hierarchy. Use this ReadOnly locks pair instead: First, Use ReadOnly only when the operational impact of blocking updates is acceptable. Then, List locks at the target scope and test a harmless control-plane update in the break/fix exercise.
- **C — Incorrect.** First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope.
  First, Assign shared governance at the lowest management group that contains every intended subscription. Then, Inspect the descendant subscription and identify the inherited assignment's management-group scope. This governed disposable-workload hierarchy pair serves management group inheritance. Governed disposable-workload hierarchy proves management group inheritance, but ReadOnly locks lacks implementation in governed disposable-workload hierarchy and ReadOnly locks proof; the ReadOnly locks outcome to prevent both deletion and control-plane modification of a protected resource remains open.
- **D — Incorrect.** First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value.
  First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value. This governed disposable-workload hierarchy pair serves resource tags. Governed disposable-workload hierarchy uses resource tags for both steps; ReadOnly locks remains untouched in governed disposable-workload hierarchy, so its ReadOnly locks gate to prevent both deletion and control-plane modification of a protected resource fails.

**Objectives:** `IG-GOVERN-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB04-CP03`).

**Microsoft Learn sources:**

- [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Source reviewed:** 2026-08-31

## LAB04-Q49 — D

**Question:** Only the governed disposable-workload hierarchy change needed to relocate supported resources without recreating them is allowed, and resource hierarchy proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag.
  First, Group resources that share ownership and lifecycle into a deliberately scoped resource group. Then, List the group's resources and verify every managed resource carries the expected lab ownership tag. This governed disposable-workload hierarchy pair serves resource group lifecycle. Resource group lifecycle cannot replace resource moves in governed disposable-workload hierarchy. Use this resource moves pair instead: First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.
- **B — Incorrect.** First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value.
  First, Apply the required owner, environment, and run ID tags to each managed resource. Then, Query resource tags and compare every required key and exact expected value. This governed disposable-workload hierarchy pair serves resource tags. Governed disposable-workload hierarchy proves resource tags, but resource moves lacks implementation in governed disposable-workload hierarchy and resource moves proof; the resource moves outcome to relocate supported resources without recreating them remains open.
- **C — Incorrect.** First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child.
  First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child. This governed disposable-workload hierarchy pair serves tag inheritance limitations. Governed disposable-workload hierarchy uses tag inheritance limitations for both steps; resource moves remains untouched in governed disposable-workload hierarchy, so its resource moves gate to relocate supported resources without recreating them fails.
- **D — Correct.** First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope.
  First, Validate every dependent resource and destination prerequisite before starting the move. Then, Run move validation and then query the resource ID and dependencies in the destination scope. This ordered resource moves workflow lets the governed disposable-workload hierarchy relocate supported resources without recreating them and then verify the resulting state.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB04-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)

**Source reviewed:** 2026-08-31

## LAB04-Q50 — D

**Question:** The governed disposable-workload hierarchy runbook separates resource hierarchy mutation from validation while it must choose the metadata region for a deployment boundary independently of its resources. Which sequence proves it cleanly?

- **A — Incorrect.** First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs.
  First, Set and re-read the intended subscription before creating any resource group. Then, Compare az account show output with the approved subscription and tenant IDs. This governed disposable-workload hierarchy pair serves subscription context. Governed disposable-workload hierarchy proves subscription context, but resource group location lacks implementation in governed disposable-workload hierarchy and resource group location proof; the resource group location outcome to choose the metadata region for a deployment boundary independently of its resources remains open.
- **B — Incorrect.** First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child.
  First, Use Azure Policy or explicit automation when child resources must receive parent tag values. Then, Query both parent and child resources to prove the required tag exists on each child. This governed disposable-workload hierarchy pair serves tag inheritance limitations. Governed disposable-workload hierarchy uses tag inheritance limitations for both steps; resource group location remains untouched in governed disposable-workload hierarchy, so its resource group location gate to choose the metadata region for a deployment boundary independently of its resources fails.
- **C — Incorrect.** First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied.
  First, Apply a CanNotDelete lock at the narrowest scope that requires deletion protection. Then, Read the lock and demonstrate a safe update is allowed while a controlled delete attempt is denied. This governed disposable-workload hierarchy pair serves CanNotDelete locks. Governed disposable-workload hierarchy closes CanNotDelete locks, not resource group location; without the resource group location workflow, it cannot choose the metadata region for a deployment boundary independently of its resources.
- **D — Correct.** First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values.
  First, Choose an approved metadata location while selecting each resource's supported deployment region independently. Then, Query the resource group location and each contained resource location as separate values. For governed disposable-workload hierarchy, the resource group location operation precedes its resource group location read-back check, allowing it to choose the metadata region for a deployment boundary independently of its resources.

**Objectives:** `IG-GOVERN-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB04-CP05`).

**Microsoft Learn sources:**

- [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)

**Source reviewed:** 2026-08-31
