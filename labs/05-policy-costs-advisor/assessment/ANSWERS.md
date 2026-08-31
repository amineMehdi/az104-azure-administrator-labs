# Lab 05 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB05-Q01 — C

**Question:** For the policy-and-cost governance rollout, the cost governance plan must package a governance rule and apply it at the intended scope. Which statement about cost governance belongs in the policy-and-cost governance rollout record?

- **A — Incorrect.** An initiative groups multiple policy definitions so they can be assigned and reported together.
  An initiative groups multiple policy definitions so they can be assigned and reported together. In the policy-and-cost governance rollout, this statement describes policy initiatives. Policy-and-cost governance rollout asks about policy definitions and assignments; this policy initiatives choice leaves the policy definitions and assignments explanation missing.
- **B — Incorrect.** Modify can correct supported properties and existing resources require a remediation task with an authorized managed identity.
  Modify can correct supported properties and existing resources require a remediation task with an authorized managed identity. In the policy-and-cost governance rollout, this statement describes modify and remediation. The modify and remediation statement accurately describes modify and remediation; however, policy-and-cost governance rollout needs policy definitions and assignments to package a governance rule and apply it at the intended scope; modify and remediation cannot replace policy definitions and assignments.
- **C — Correct.** A policy definition expresses a rule, while an assignment applies that rule at a selected scope.
  A policy definition expresses a rule, while an assignment applies that rule at a selected scope. In the policy-and-cost governance rollout, this policy definitions and assignments rule supports the need to package a governance rule and apply it at the intended scope.
- **D — Incorrect.** Budget notifications require supported contact emails, roles, or action groups at the budget scope.
  Budget notifications require supported contact emails, roles, or action groups at the budget scope. In the policy-and-cost governance rollout, this statement describes budget notification contacts. Policy definitions and assignments governs policy-and-cost governance rollout; budget notification contacts cannot support policy definitions and assignments when operators must package a governance rule and apply it at the intended scope.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

**Source reviewed:** 2026-08-31

## LAB05-Q02 — D

**Question:** The cost governance review compares four claims for the policy-and-cost governance rollout requirement to deploy several related governance rules as one versioned assignment. Which claim is technically sound?

- **A — Incorrect.** Azure Policy compliance state can lag a change until the next evaluation or an explicit scan completes.
  Azure Policy compliance state can lag a change until the next evaluation or an explicit scan completes. In the policy-and-cost governance rollout, this statement describes policy compliance evaluation. The policy compliance evaluation statement accurately describes policy compliance evaluation; however, policy-and-cost governance rollout needs policy initiatives to deploy several related governance rules as one versioned assignment; policy compliance evaluation cannot replace policy initiatives.
- **B — Incorrect.** An Azure budget tracks actual or forecast cost and sends notifications but does not stop resource consumption.
  An Azure budget tracks actual or forecast cost and sends notifications but does not stop resource consumption. In the policy-and-cost governance rollout, this statement describes budget behavior. Selecting budget behavior for policy-and-cost governance rollout leaves policy initiatives unanswered in policy-and-cost governance rollout; the policy-and-cost governance rollout lacks a policy initiatives basis to deploy several related governance rules as one versioned assignment.
- **C — Incorrect.** Azure Advisor analyzes resource use and publishes recommendations; it does not automatically apply cost changes.
  Azure Advisor analyzes resource use and publishes recommendations; it does not automatically apply cost changes. In the policy-and-cost governance rollout, this statement describes Advisor cost recommendations. Policy initiatives governs policy-and-cost governance rollout; Advisor cost recommendations cannot support policy initiatives when operators must deploy several related governance rules as one versioned assignment.
- **D — Correct.** An initiative groups multiple policy definitions so they can be assigned and reported together.
  For the policy-and-cost governance rollout, the rule for policy initiatives is defined by this statement: an initiative groups multiple policy definitions so they can be assigned and reported together. It supports the required outcome to deploy several related governance rules as one versioned assignment.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Azure Policy initiative definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure)

**Source reviewed:** 2026-08-31

## LAB05-Q03 — C

**Question:** The cost governance architecture note requires the policy-and-cost governance rollout environment to measure existing resources against an assigned governance rule. Which statement defines the relevant cost governance boundary?

- **A — Incorrect.** The deny effect rejects a noncompliant create or update request before the resource provider completes it.
  The deny effect rejects a noncompliant create or update request before the resource provider completes it. In the policy-and-cost governance rollout, this statement describes deny policy effect. Selecting deny policy effect for policy-and-cost governance rollout leaves policy compliance evaluation unanswered in policy-and-cost governance rollout; the policy-and-cost governance rollout lacks a policy compliance evaluation basis to measure existing resources against an assigned governance rule.
- **B — Incorrect.** A forecast threshold warns when projected spend is expected to cross a percentage of the budget.
  A forecast threshold warns when projected spend is expected to cross a percentage of the budget. In the policy-and-cost governance rollout, this statement describes forecast budget alerts. Policy compliance evaluation governs policy-and-cost governance rollout; forecast budget alerts cannot support policy compliance evaluation when operators must measure existing resources against an assigned governance rule.
- **C — Correct.** Azure Policy compliance state can lag a change until the next evaluation or an explicit scan completes.
  Azure Policy compliance state can lag a change until the next evaluation or an explicit scan completes. The policy-and-cost governance rollout applies that policy compliance evaluation boundary when operators must measure existing resources against an assigned governance rule.
- **D — Incorrect.** A management-group policy assignment affects descendant subscriptions except explicitly excluded scopes.
  A management-group policy assignment affects descendant subscriptions except explicitly excluded scopes. In the policy-and-cost governance rollout, this statement describes governance scope and exclusions. The governance scope and exclusions statement accurately describes governance scope and exclusions; however, policy-and-cost governance rollout needs policy compliance evaluation to measure existing resources against an assigned governance rule; governance scope and exclusions cannot replace policy compliance evaluation.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Get Azure Policy compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data)

**Source reviewed:** 2026-08-31

## LAB05-Q04 — A

**Question:** A new cost governance operator must explain why the policy-and-cost governance rollout can block a noncompliant creation request before the resource is deployed. Which explanation is accurate?

- **A — Correct.** The deny effect rejects a noncompliant create or update request before the resource provider completes it.
  The policy-and-cost governance rollout needs deny policy effect to block a noncompliant creation request before the resource is deployed; this option states the applicable deny policy effect rule: the deny effect rejects a noncompliant create or update request before the resource provider completes it.
- **B — Incorrect.** Modify can correct supported properties and existing resources require a remediation task with an authorized managed identity.
  Modify can correct supported properties and existing resources require a remediation task with an authorized managed identity. In the policy-and-cost governance rollout, this statement describes modify and remediation. Policy-and-cost governance rollout asks about deny policy effect; this modify and remediation choice leaves the deny policy effect explanation missing.
- **C — Incorrect.** Budget notifications require supported contact emails, roles, or action groups at the budget scope.
  Budget notifications require supported contact emails, roles, or action groups at the budget scope. In the policy-and-cost governance rollout, this statement describes budget notification contacts. The budget notification contacts statement accurately describes budget notification contacts; however, policy-and-cost governance rollout needs deny policy effect to block a noncompliant creation request before the resource is deployed; budget notification contacts cannot replace deny policy effect.
- **D — Incorrect.** A policy definition expresses a rule, while an assignment applies that rule at a selected scope.
  A policy definition expresses a rule, while an assignment applies that rule at a selected scope. In the policy-and-cost governance rollout, this statement describes policy definitions and assignments. Selecting policy definitions and assignments for policy-and-cost governance rollout leaves deny policy effect unanswered in policy-and-cost governance rollout; the policy-and-cost governance rollout lacks a deny policy effect basis to block a noncompliant creation request before the resource is deployed.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Understand Azure Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)

**Source reviewed:** 2026-08-31

## LAB05-Q05 — A

**Question:** The policy-and-cost governance rollout acceptance criteria require operators to correct existing noncompliant resources after a managed change is assigned. Which service fact supports that requirement?

- **A — Correct.** Modify can correct supported properties and existing resources require a remediation task with an authorized managed identity.
  Modify can correct supported properties and existing resources require a remediation task with an authorized managed identity. This modify and remediation fact resolves the policy-and-cost governance rollout design question about how to correct existing noncompliant resources after a managed change is assigned.
- **B — Incorrect.** An Azure budget tracks actual or forecast cost and sends notifications but does not stop resource consumption.
  An Azure budget tracks actual or forecast cost and sends notifications but does not stop resource consumption. In the policy-and-cost governance rollout, this statement describes budget behavior. The budget behavior statement accurately describes budget behavior; however, policy-and-cost governance rollout needs modify and remediation to correct existing noncompliant resources after a managed change is assigned; budget behavior cannot replace modify and remediation.
- **C — Incorrect.** Azure Advisor analyzes resource use and publishes recommendations; it does not automatically apply cost changes.
  Azure Advisor analyzes resource use and publishes recommendations; it does not automatically apply cost changes. In the policy-and-cost governance rollout, this statement describes Advisor cost recommendations. Selecting Advisor cost recommendations for policy-and-cost governance rollout leaves modify and remediation unanswered in policy-and-cost governance rollout; the policy-and-cost governance rollout lacks a modify and remediation basis to correct existing noncompliant resources after a managed change is assigned.
- **D — Incorrect.** An initiative groups multiple policy definitions so they can be assigned and reported together.
  An initiative groups multiple policy definitions so they can be assigned and reported together. In the policy-and-cost governance rollout, this statement describes policy initiatives. Modify and remediation governs policy-and-cost governance rollout; policy initiatives cannot support modify and remediation when operators must correct existing noncompliant resources after a managed change is assigned.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Remediate noncompliant resources with Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

**Source reviewed:** 2026-08-31

## LAB05-Q06 — B

**Question:** A cost governance reviewer challenges whether the policy-and-cost governance rollout can receive notifications without expecting spending to be stopped automatically. Which response resolves the concern?

- **A — Incorrect.** A forecast threshold warns when projected spend is expected to cross a percentage of the budget.
  A forecast threshold warns when projected spend is expected to cross a percentage of the budget. In the policy-and-cost governance rollout, this statement describes forecast budget alerts. The forecast budget alerts statement accurately describes forecast budget alerts; however, policy-and-cost governance rollout needs budget behavior to receive notifications without expecting spending to be stopped automatically; forecast budget alerts cannot replace budget behavior.
- **B — Correct.** An Azure budget tracks actual or forecast cost and sends notifications but does not stop resource consumption.
  An Azure budget tracks actual or forecast cost and sends notifications but does not stop resource consumption. For policy-and-cost governance rollout, budget behavior supplies the service rule needed to receive notifications without expecting spending to be stopped automatically.
- **C — Incorrect.** A management-group policy assignment affects descendant subscriptions except explicitly excluded scopes.
  A management-group policy assignment affects descendant subscriptions except explicitly excluded scopes. In the policy-and-cost governance rollout, this statement describes governance scope and exclusions. Budget behavior governs policy-and-cost governance rollout; governance scope and exclusions cannot support budget behavior when operators must receive notifications without expecting spending to be stopped automatically.
- **D — Incorrect.** Azure Policy compliance state can lag a change until the next evaluation or an explicit scan completes.
  Azure Policy compliance state can lag a change until the next evaluation or an explicit scan completes. In the policy-and-cost governance rollout, this statement describes policy compliance evaluation. Policy-and-cost governance rollout asks about budget behavior; this policy compliance evaluation choice leaves the budget behavior explanation missing.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q07 — B

**Question:** The policy-and-cost governance rollout handoff omits the cost governance rule needed to notify owners before projected spending reaches the configured limit. Which statement should the team add?

- **A — Incorrect.** Budget notifications require supported contact emails, roles, or action groups at the budget scope.
  Budget notifications require supported contact emails, roles, or action groups at the budget scope. In the policy-and-cost governance rollout, this statement describes budget notification contacts. Selecting budget notification contacts for policy-and-cost governance rollout leaves forecast budget alerts unanswered in policy-and-cost governance rollout; the policy-and-cost governance rollout lacks a forecast budget alerts basis to notify owners before projected spending reaches the configured limit.
- **B — Correct.** A forecast threshold warns when projected spend is expected to cross a percentage of the budget.
  A forecast threshold warns when projected spend is expected to cross a percentage of the budget. In the policy-and-cost governance rollout, this forecast budget alerts rule supports the need to notify owners before projected spending reaches the configured limit.
- **C — Incorrect.** A policy definition expresses a rule, while an assignment applies that rule at a selected scope.
  A policy definition expresses a rule, while an assignment applies that rule at a selected scope. In the policy-and-cost governance rollout, this statement describes policy definitions and assignments. Policy-and-cost governance rollout asks about forecast budget alerts; this policy definitions and assignments choice leaves the forecast budget alerts explanation missing.
- **D — Incorrect.** The deny effect rejects a noncompliant create or update request before the resource provider completes it.
  The deny effect rejects a noncompliant create or update request before the resource provider completes it. In the policy-and-cost governance rollout, this statement describes deny policy effect. The deny policy effect statement accurately describes deny policy effect; however, policy-and-cost governance rollout needs forecast budget alerts to notify owners before projected spending reaches the configured limit; deny policy effect cannot replace forecast budget alerts.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q08 — D

**Question:** A cost governance incident review of the policy-and-cost governance rollout depends on the ability to route cost notifications to the approved recipients. Which platform description is reliable?

- **A — Incorrect.** Azure Advisor analyzes resource use and publishes recommendations; it does not automatically apply cost changes.
  Azure Advisor analyzes resource use and publishes recommendations; it does not automatically apply cost changes. In the policy-and-cost governance rollout, this statement describes Advisor cost recommendations. Budget notification contacts governs policy-and-cost governance rollout; Advisor cost recommendations cannot support budget notification contacts when operators must route cost notifications to the approved recipients.
- **B — Incorrect.** An initiative groups multiple policy definitions so they can be assigned and reported together.
  An initiative groups multiple policy definitions so they can be assigned and reported together. In the policy-and-cost governance rollout, this statement describes policy initiatives. Policy-and-cost governance rollout asks about budget notification contacts; this policy initiatives choice leaves the budget notification contacts explanation missing.
- **C — Incorrect.** Modify can correct supported properties and existing resources require a remediation task with an authorized managed identity.
  Modify can correct supported properties and existing resources require a remediation task with an authorized managed identity. In the policy-and-cost governance rollout, this statement describes modify and remediation. The modify and remediation statement accurately describes modify and remediation; however, policy-and-cost governance rollout needs budget notification contacts to route cost notifications to the approved recipients; modify and remediation cannot replace budget notification contacts.
- **D — Correct.** Budget notifications require supported contact emails, roles, or action groups at the budget scope.
  For the policy-and-cost governance rollout, the rule for budget notification contacts is defined by this statement: budget notifications require supported contact emails, roles, or action groups at the budget scope. It supports the required outcome to route cost notifications to the approved recipients.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q09 — D

**Question:** A cloud governance analyst enforcing standards and controlling spend is updating the cost governance runbook. The requirement is to identify rightsizing or shutdown opportunities from service telemetry. Which statement describes Azure behavior correctly?

- **A — Incorrect.** A management-group policy assignment affects descendant subscriptions except explicitly excluded scopes.
  A management-group policy assignment affects descendant subscriptions except explicitly excluded scopes. In the policy-and-cost governance rollout, this statement describes governance scope and exclusions. Policy-and-cost governance rollout asks about Advisor cost recommendations; this governance scope and exclusions choice leaves the Advisor cost recommendations explanation missing.
- **B — Incorrect.** Azure Policy compliance state can lag a change until the next evaluation or an explicit scan completes.
  Azure Policy compliance state can lag a change until the next evaluation or an explicit scan completes. In the policy-and-cost governance rollout, this statement describes policy compliance evaluation. The policy compliance evaluation statement accurately describes policy compliance evaluation; however, policy-and-cost governance rollout needs Advisor cost recommendations to identify rightsizing or shutdown opportunities from service telemetry; policy compliance evaluation cannot replace Advisor cost recommendations.
- **C — Incorrect.** An Azure budget tracks actual or forecast cost and sends notifications but does not stop resource consumption.
  An Azure budget tracks actual or forecast cost and sends notifications but does not stop resource consumption. In the policy-and-cost governance rollout, this statement describes budget behavior. Selecting budget behavior for policy-and-cost governance rollout leaves Advisor cost recommendations unanswered in policy-and-cost governance rollout; the policy-and-cost governance rollout lacks a Advisor cost recommendations basis to identify rightsizing or shutdown opportunities from service telemetry.
- **D — Correct.** Azure Advisor analyzes resource use and publishes recommendations; it does not automatically apply cost changes.
  Azure Advisor analyzes resource use and publishes recommendations; it does not automatically apply cost changes. The policy-and-cost governance rollout applies that Advisor cost recommendations boundary when operators must identify rightsizing or shutdown opportunities from service telemetry.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Azure Advisor cost recommendations](https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations)

**Source reviewed:** 2026-08-31

## LAB05-Q10 — B

**Question:** A cost governance peer review asks how the policy-and-cost governance rollout should handle this outcome: exclude an approved child scope without weakening governance elsewhere. Which explanation is accurate?

- **A — Incorrect.** A policy definition expresses a rule, while an assignment applies that rule at a selected scope.
  A policy definition expresses a rule, while an assignment applies that rule at a selected scope. In the policy-and-cost governance rollout, this statement describes policy definitions and assignments. The policy definitions and assignments statement accurately describes policy definitions and assignments; however, policy-and-cost governance rollout needs governance scope and exclusions to exclude an approved child scope without weakening governance elsewhere; policy definitions and assignments cannot replace governance scope and exclusions.
- **B — Correct.** A management-group policy assignment affects descendant subscriptions except explicitly excluded scopes.
  The policy-and-cost governance rollout needs governance scope and exclusions to exclude an approved child scope without weakening governance elsewhere; this option states the applicable governance scope and exclusions rule: a management-group policy assignment affects descendant subscriptions except explicitly excluded scopes.
- **C — Incorrect.** The deny effect rejects a noncompliant create or update request before the resource provider completes it.
  The deny effect rejects a noncompliant create or update request before the resource provider completes it. In the policy-and-cost governance rollout, this statement describes deny policy effect. Governance scope and exclusions governs policy-and-cost governance rollout; deny policy effect cannot support governance scope and exclusions when operators must exclude an approved child scope without weakening governance elsewhere.
- **D — Incorrect.** A forecast threshold warns when projected spend is expected to cross a percentage of the budget.
  A forecast threshold warns when projected spend is expected to cross a percentage of the budget. In the policy-and-cost governance rollout, this statement describes forecast budget alerts. Policy-and-cost governance rollout asks about governance scope and exclusions; this forecast budget alerts choice leaves the governance scope and exclusions explanation missing.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Azure Policy assignment scope](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/scope)

**Source reviewed:** 2026-08-31

## LAB05-Q11 — D

**Question:** The cloud governance analyst enforcing standards and controlling spend may change the policy-and-cost governance rollout only to package a governance rule and apply it at the intended scope. Which cost governance action stays within that assignment?

- **A — Incorrect.** Trigger a compliance scan after assignment when the lab needs deterministic validation timing.
  Trigger a compliance scan after assignment when the lab needs deterministic validation timing. In the policy-and-cost governance rollout, this action changes policy compliance evaluation. Policy-and-cost governance rollout approved policy definitions and assignments, not policy compliance evaluation; only the policy definitions and assignments change can package a governance rule and apply it at the intended scope.
- **B — Incorrect.** Create a budget at the intended billing scope with thresholds and notification recipients.
  Create a budget at the intended billing scope with thresholds and notification recipients. In the policy-and-cost governance rollout, this action changes budget behavior. Policy-and-cost governance rollout requires policy definitions and assignments; changing budget behavior leaves policy definitions and assignments absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot package a governance rule and apply it at the intended scope.
- **C — Incorrect.** Retrieve active cost recommendations and review impact before approving any remediation.
  Retrieve active cost recommendations and review impact before approving any remediation. In the policy-and-cost governance rollout, this action changes Advisor cost recommendations. Advisor cost recommendations does not implement policy definitions and assignments for policy-and-cost governance rollout; the policy-and-cost governance rollout still cannot package a governance rule and apply it at the intended scope.
- **D — Correct.** Select or author the definition and then assign it at the narrowest required governance scope.
  Select or author the definition and then assign it at the narrowest required governance scope. It is the least-change policy definitions and assignments path for the policy-and-cost governance rollout requirement to package a governance rule and apply it at the intended scope.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

**Source reviewed:** 2026-08-31

## LAB05-Q12 — D

**Question:** A cost governance dry run shows no policy-and-cost governance rollout command will deploy several related governance rules as one versioned assignment. Which action belongs before execution?

- **A — Incorrect.** Use a deny assignment only after validating its condition and approved exclusions.
  Use a deny assignment only after validating its condition and approved exclusions. In the policy-and-cost governance rollout, this action changes deny policy effect. Policy-and-cost governance rollout requires policy initiatives; changing deny policy effect leaves policy initiatives absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot deploy several related governance rules as one versioned assignment.
- **B — Incorrect.** Add a forecast notification early enough for the owner to correct projected overspend.
  Add a forecast notification early enough for the owner to correct projected overspend. In the policy-and-cost governance rollout, this action changes forecast budget alerts. Forecast budget alerts does not implement policy initiatives for policy-and-cost governance rollout; the policy-and-cost governance rollout still cannot deploy several related governance rules as one versioned assignment.
- **C — Incorrect.** Set notScopes only for approved exceptions and keep the assignment at the shared parent scope.
  Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. In the policy-and-cost governance rollout, this action changes governance scope and exclusions. Policy-and-cost governance rollout instead needs policy initiatives: Use an initiative when one compliance baseline requires several coordinated policy rules. The governance scope and exclusions action omits that policy initiatives work.
- **D — Correct.** Use an initiative when one compliance baseline requires several coordinated policy rules.
  Use an initiative when one compliance baseline requires several coordinated policy rules. In policy-and-cost governance rollout, applying policy initiatives is the scoped way to deploy several related governance rules as one versioned assignment.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Azure Policy initiative definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure)

**Source reviewed:** 2026-08-31

## LAB05-Q13 — C

**Question:** For the policy-and-cost governance rollout, operators need to measure existing resources against an assigned governance rule. Which change realizes that requirement?

- **A — Incorrect.** Assign the modify policy with a managed identity and create remediation for existing resources.
  Assign the modify policy with a managed identity and create remediation for existing resources. In the policy-and-cost governance rollout, this action changes modify and remediation. Modify and remediation does not implement policy compliance evaluation for policy-and-cost governance rollout; the policy-and-cost governance rollout still cannot measure existing resources against an assigned governance rule.
- **B — Incorrect.** Configure an approved notification recipient and verify it is valid at the selected scope.
  Configure an approved notification recipient and verify it is valid at the selected scope. In the policy-and-cost governance rollout, this action changes budget notification contacts. Policy-and-cost governance rollout instead needs policy compliance evaluation: Trigger a compliance scan after assignment when the lab needs deterministic validation timing. The budget notification contacts action omits that policy compliance evaluation work.
- **C — Correct.** Trigger a compliance scan after assignment when the lab needs deterministic validation timing.
  Trigger a compliance scan after assignment when the lab needs deterministic validation timing. The policy-and-cost governance rollout uses this policy compliance evaluation operation to measure existing resources against an assigned governance rule within the approved scope.
- **D — Incorrect.** Select or author the definition and then assign it at the narrowest required governance scope.
  Select or author the definition and then assign it at the narrowest required governance scope. In the policy-and-cost governance rollout, this action changes policy definitions and assignments. Policy-and-cost governance rollout requires policy compliance evaluation; changing policy definitions and assignments leaves policy compliance evaluation absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot measure existing resources against an assigned governance rule.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Get Azure Policy compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data)

**Source reviewed:** 2026-08-31

## LAB05-Q14 — B

**Question:** Operators must automate the policy-and-cost governance rollout change needed to block a noncompliant creation request before the resource is deployed. Which cost governance operation belongs in the runbook?

- **A — Incorrect.** Create a budget at the intended billing scope with thresholds and notification recipients.
  Create a budget at the intended billing scope with thresholds and notification recipients. In the policy-and-cost governance rollout, this action changes budget behavior. Policy-and-cost governance rollout instead needs deny policy effect: Use a deny assignment only after validating its condition and approved exclusions. The budget behavior action omits that deny policy effect work.
- **B — Correct.** Use a deny assignment only after validating its condition and approved exclusions.
  For the policy-and-cost governance rollout, the required deny policy effect action is: use a deny assignment only after validating its condition and approved exclusions. It makes the environment able to block a noncompliant creation request before the resource is deployed.
- **C — Incorrect.** Retrieve active cost recommendations and review impact before approving any remediation.
  Retrieve active cost recommendations and review impact before approving any remediation. In the policy-and-cost governance rollout, this action changes Advisor cost recommendations. Policy-and-cost governance rollout requires deny policy effect; changing Advisor cost recommendations leaves deny policy effect absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot block a noncompliant creation request before the resource is deployed.
- **D — Incorrect.** Use an initiative when one compliance baseline requires several coordinated policy rules.
  Use an initiative when one compliance baseline requires several coordinated policy rules. In the policy-and-cost governance rollout, this action changes policy initiatives. Policy initiatives does not implement deny policy effect for policy-and-cost governance rollout; the policy-and-cost governance rollout still cannot block a noncompliant creation request before the resource is deployed.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Understand Azure Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)

**Source reviewed:** 2026-08-31

## LAB05-Q15 — A

**Question:** A policy-and-cost governance rollout review finds cost governance drift from the need to correct existing noncompliant resources after a managed change is assigned. Which correction addresses that drift?

- **A — Correct.** Assign the modify policy with a managed identity and create remediation for existing resources.
  Assign the modify policy with a managed identity and create remediation for existing resources. This changes modify and remediation in the policy-and-cost governance rollout, supplying the missing state needed to correct existing noncompliant resources after a managed change is assigned.
- **B — Incorrect.** Add a forecast notification early enough for the owner to correct projected overspend.
  Add a forecast notification early enough for the owner to correct projected overspend. In the policy-and-cost governance rollout, this action changes forecast budget alerts. Policy-and-cost governance rollout requires modify and remediation; changing forecast budget alerts leaves modify and remediation absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot correct existing noncompliant resources after a managed change is assigned.
- **C — Incorrect.** Set notScopes only for approved exceptions and keep the assignment at the shared parent scope.
  Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. In the policy-and-cost governance rollout, this action changes governance scope and exclusions. Governance scope and exclusions does not implement modify and remediation for policy-and-cost governance rollout; the policy-and-cost governance rollout still cannot correct existing noncompliant resources after a managed change is assigned.
- **D — Incorrect.** Trigger a compliance scan after assignment when the lab needs deterministic validation timing.
  Trigger a compliance scan after assignment when the lab needs deterministic validation timing. In the policy-and-cost governance rollout, this action changes policy compliance evaluation. Policy-and-cost governance rollout instead needs modify and remediation: Assign the modify policy with a managed identity and create remediation for existing resources. The policy compliance evaluation action omits that modify and remediation work.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Remediate noncompliant resources with Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

**Source reviewed:** 2026-08-31

## LAB05-Q16 — C

**Question:** The policy-and-cost governance rollout window permits only the cost governance change needed to receive notifications without expecting spending to be stopped automatically. Which option respects the boundary?

- **A — Incorrect.** Configure an approved notification recipient and verify it is valid at the selected scope.
  Configure an approved notification recipient and verify it is valid at the selected scope. In the policy-and-cost governance rollout, this action changes budget notification contacts. Policy-and-cost governance rollout requires budget behavior; changing budget notification contacts leaves budget behavior absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot receive notifications without expecting spending to be stopped automatically.
- **B — Incorrect.** Select or author the definition and then assign it at the narrowest required governance scope.
  Select or author the definition and then assign it at the narrowest required governance scope. In the policy-and-cost governance rollout, this action changes policy definitions and assignments. Policy definitions and assignments does not implement budget behavior for policy-and-cost governance rollout; the policy-and-cost governance rollout still cannot receive notifications without expecting spending to be stopped automatically.
- **C — Correct.** Create a budget at the intended billing scope with thresholds and notification recipients.
  The policy-and-cost governance rollout must receive notifications without expecting spending to be stopped automatically; this option performs its direct budget behavior change: create a budget at the intended billing scope with thresholds and notification recipients.
- **D — Incorrect.** Use a deny assignment only after validating its condition and approved exclusions.
  Use a deny assignment only after validating its condition and approved exclusions. In the policy-and-cost governance rollout, this action changes deny policy effect. Policy-and-cost governance rollout approved budget behavior, not deny policy effect; only the budget behavior change can receive notifications without expecting spending to be stopped automatically.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q17 — D

**Question:** The cost governance preflight has passed; the policy-and-cost governance rollout must now notify owners before projected spending reaches the configured limit. Which operation should run?

- **A — Incorrect.** Retrieve active cost recommendations and review impact before approving any remediation.
  Retrieve active cost recommendations and review impact before approving any remediation. In the policy-and-cost governance rollout, this action changes Advisor cost recommendations. Advisor cost recommendations does not implement forecast budget alerts for policy-and-cost governance rollout; the policy-and-cost governance rollout still cannot notify owners before projected spending reaches the configured limit.
- **B — Incorrect.** Use an initiative when one compliance baseline requires several coordinated policy rules.
  Use an initiative when one compliance baseline requires several coordinated policy rules. In the policy-and-cost governance rollout, this action changes policy initiatives. Policy-and-cost governance rollout instead needs forecast budget alerts: Add a forecast notification early enough for the owner to correct projected overspend. The policy initiatives action omits that forecast budget alerts work.
- **C — Incorrect.** Assign the modify policy with a managed identity and create remediation for existing resources.
  Assign the modify policy with a managed identity and create remediation for existing resources. In the policy-and-cost governance rollout, this action changes modify and remediation. Policy-and-cost governance rollout approved forecast budget alerts, not modify and remediation; only the forecast budget alerts change can notify owners before projected spending reaches the configured limit.
- **D — Correct.** Add a forecast notification early enough for the owner to correct projected overspend.
  Add a forecast notification early enough for the owner to correct projected overspend. It is the least-change forecast budget alerts path for the policy-and-cost governance rollout requirement to notify owners before projected spending reaches the configured limit.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q18 — A

**Question:** The policy-and-cost governance rollout plan must route cost notifications to the approved recipients while limiting the mutation scope to cost governance. Which action is appropriate?

- **A — Correct.** Configure an approved notification recipient and verify it is valid at the selected scope.
  Configure an approved notification recipient and verify it is valid at the selected scope. In policy-and-cost governance rollout, applying budget notification contacts is the scoped way to route cost notifications to the approved recipients.
- **B — Incorrect.** Set notScopes only for approved exceptions and keep the assignment at the shared parent scope.
  Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. In the policy-and-cost governance rollout, this action changes governance scope and exclusions. Policy-and-cost governance rollout approved budget notification contacts, not governance scope and exclusions; only the budget notification contacts change can route cost notifications to the approved recipients.
- **C — Incorrect.** Trigger a compliance scan after assignment when the lab needs deterministic validation timing.
  Trigger a compliance scan after assignment when the lab needs deterministic validation timing. In the policy-and-cost governance rollout, this action changes policy compliance evaluation. Policy-and-cost governance rollout requires budget notification contacts; changing policy compliance evaluation leaves budget notification contacts absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot route cost notifications to the approved recipients.
- **D — Incorrect.** Create a budget at the intended billing scope with thresholds and notification recipients.
  Create a budget at the intended billing scope with thresholds and notification recipients. In the policy-and-cost governance rollout, this action changes budget behavior. Budget behavior does not implement budget notification contacts for policy-and-cost governance rollout; the policy-and-cost governance rollout still cannot route cost notifications to the approved recipients.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q19 — C

**Question:** A cost governance ticket in the policy-and-cost governance rollout says to identify rightsizing or shutdown opportunities from service telemetry. Which cost governance action completes the policy-and-cost governance rollout request with minimal change?

- **A — Incorrect.** Select or author the definition and then assign it at the narrowest required governance scope.
  Select or author the definition and then assign it at the narrowest required governance scope. In the policy-and-cost governance rollout, this action changes policy definitions and assignments. Policy-and-cost governance rollout approved Advisor cost recommendations, not policy definitions and assignments; only the Advisor cost recommendations change can identify rightsizing or shutdown opportunities from service telemetry.
- **B — Incorrect.** Use a deny assignment only after validating its condition and approved exclusions.
  Use a deny assignment only after validating its condition and approved exclusions. In the policy-and-cost governance rollout, this action changes deny policy effect. Policy-and-cost governance rollout requires Advisor cost recommendations; changing deny policy effect leaves Advisor cost recommendations absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot identify rightsizing or shutdown opportunities from service telemetry.
- **C — Correct.** Retrieve active cost recommendations and review impact before approving any remediation.
  Retrieve active cost recommendations and review impact before approving any remediation. The policy-and-cost governance rollout uses this Advisor cost recommendations operation to identify rightsizing or shutdown opportunities from service telemetry within the approved scope.
- **D — Incorrect.** Add a forecast notification early enough for the owner to correct projected overspend.
  Add a forecast notification early enough for the owner to correct projected overspend. In the policy-and-cost governance rollout, this action changes forecast budget alerts. Policy-and-cost governance rollout instead needs Advisor cost recommendations: Retrieve active cost recommendations and review impact before approving any remediation. The forecast budget alerts action omits that Advisor cost recommendations work.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Azure Advisor cost recommendations](https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations)

**Source reviewed:** 2026-08-31

## LAB05-Q20 — B

**Question:** The approach for the policy-and-cost governance rollout is approved, but the cost governance environment still cannot exclude an approved child scope without weakening governance elsewhere. Which implementation step closes the gap?

- **A — Incorrect.** Use an initiative when one compliance baseline requires several coordinated policy rules.
  Use an initiative when one compliance baseline requires several coordinated policy rules. In the policy-and-cost governance rollout, this action changes policy initiatives. Policy-and-cost governance rollout requires governance scope and exclusions; changing policy initiatives leaves governance scope and exclusions absent in policy-and-cost governance rollout; policy-and-cost governance rollout cannot exclude an approved child scope without weakening governance elsewhere.
- **B — Correct.** Set notScopes only for approved exceptions and keep the assignment at the shared parent scope.
  For the policy-and-cost governance rollout, the required governance scope and exclusions action is: set notScopes only for approved exceptions and keep the assignment at the shared parent scope. It makes the environment able to exclude an approved child scope without weakening governance elsewhere.
- **C — Incorrect.** Assign the modify policy with a managed identity and create remediation for existing resources.
  Assign the modify policy with a managed identity and create remediation for existing resources. In the policy-and-cost governance rollout, this action changes modify and remediation. Policy-and-cost governance rollout instead needs governance scope and exclusions: Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. The modify and remediation action omits that governance scope and exclusions work.
- **D — Incorrect.** Configure an approved notification recipient and verify it is valid at the selected scope.
  Configure an approved notification recipient and verify it is valid at the selected scope. In the policy-and-cost governance rollout, this action changes budget notification contacts. Policy-and-cost governance rollout approved governance scope and exclusions, not budget notification contacts; only the governance scope and exclusions change can exclude an approved child scope without weakening governance elsewhere.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Azure Policy assignment scope](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/scope)

**Source reviewed:** 2026-08-31

## LAB05-Q21 — A

**Question:** The policy-and-cost governance rollout rejects cost governance exit status as proof it can package a governance rule and apply it at the intended scope. Which policy-and-cost governance rollout result is valid evidence?

- **A — Correct.** Read the assignment's definition ID, scope, parameters, and enforcement mode.
  Read the assignment's definition ID, scope, parameters, and enforcement mode. Because the policy-and-cost governance rollout check observes policy definitions and assignments, it independently verifies the requirement to package a governance rule and apply it at the intended scope.
- **B — Incorrect.** Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
  Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment. In the policy-and-cost governance rollout, this check observes deny policy effect. Deny policy effect success in policy-and-cost governance rollout cannot verify policy definitions and assignments; policy-and-cost governance rollout cannot package a governance rule and apply it at the intended scope until policy definitions and assignments evidence exists.
- **C — Incorrect.** Read the notification operator, threshold, threshold type, and enabled state.
  Read the notification operator, threshold, threshold type, and enabled state. In the policy-and-cost governance rollout, this check observes forecast budget alerts. Policy-and-cost governance rollout reads forecast budget alerts, leaving policy definitions and assignments unproved in policy-and-cost governance rollout; policy-and-cost governance rollout still has no policy definitions and assignments proof.
- **D — Incorrect.** Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.
  Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription. In the policy-and-cost governance rollout, this check observes governance scope and exclusions. Policy-and-cost governance rollout could pass governance scope and exclusions while policy definitions and assignments is wrong; policy-and-cost governance rollout still lacks policy definitions and assignments proof.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

**Source reviewed:** 2026-08-31

## LAB05-Q22 — B

**Question:** The cost governance validator needs one policy-and-cost governance rollout query after the change to deploy several related governance rules as one versioned assignment. Which cost governance property should the policy-and-cost governance rollout validator inspect?

- **A — Incorrect.** Inspect the remediation deployment and query the corrected property on each target resource.
  Inspect the remediation deployment and query the corrected property on each target resource. In the policy-and-cost governance rollout, this check observes modify and remediation. Modify and remediation success in policy-and-cost governance rollout cannot verify policy initiatives; policy-and-cost governance rollout cannot deploy several related governance rules as one versioned assignment until policy initiatives evidence exists.
- **B — Correct.** Query the initiative assignment and enumerate its member definition references.
  The policy-and-cost governance rollout validator needs this policy initiatives result: query the initiative assignment and enumerate its member definition references. It proves the outcome to deploy several related governance rules as one versioned assignment rather than an adjacent checkpoint.
- **C — Incorrect.** Query the notification contact collection and confirm the threshold is enabled.
  Query the notification contact collection and confirm the threshold is enabled. In the policy-and-cost governance rollout, this check observes budget notification contacts. Policy-and-cost governance rollout could pass budget notification contacts while policy initiatives is wrong; policy-and-cost governance rollout still lacks policy initiatives proof.
- **D — Incorrect.** Read the assignment's definition ID, scope, parameters, and enforcement mode.
  Read the assignment's definition ID, scope, parameters, and enforcement mode. In the policy-and-cost governance rollout, this check observes policy definitions and assignments. Policy-and-cost governance rollout output covers policy definitions and assignments, not policy initiatives; the policy initiatives requirement to deploy several related governance rules as one versioned assignment remains unverified.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Azure Policy initiative definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure)

**Source reviewed:** 2026-08-31

## LAB05-Q23 — D

**Question:** The cloud governance analyst enforcing standards and controlling spend must confirm the policy-and-cost governance rollout, without mutation, can measure existing resources against an assigned governance rule. Which cost governance check qualifies?

- **A — Incorrect.** Query the budget amount, time grain, thresholds, and current cost separately.
  Query the budget amount, time grain, thresholds, and current cost separately. In the policy-and-cost governance rollout, this check observes budget behavior. Policy-and-cost governance rollout reads budget behavior, leaving policy compliance evaluation unproved in policy-and-cost governance rollout; policy-and-cost governance rollout still has no policy compliance evaluation proof.
- **B — Incorrect.** Query recommendation category, impact, resource ID, and short description.
  Query recommendation category, impact, resource ID, and short description. In the policy-and-cost governance rollout, this check observes Advisor cost recommendations. Policy-and-cost governance rollout could pass Advisor cost recommendations while policy compliance evaluation is wrong; policy-and-cost governance rollout still lacks policy compliance evaluation proof.
- **C — Incorrect.** Query the initiative assignment and enumerate its member definition references.
  Query the initiative assignment and enumerate its member definition references. In the policy-and-cost governance rollout, this check observes policy initiatives. Policy-and-cost governance rollout output covers policy initiatives, not policy compliance evaluation; the policy compliance evaluation requirement to measure existing resources against an assigned governance rule remains unverified.
- **D — Correct.** Query policy states after evaluation and match the resource ID, assignment ID, and compliance state.
  Query policy states after evaluation and match the resource ID, assignment ID, and compliance state. This is independent policy compliance evaluation evidence for the policy-and-cost governance rollout, even if policy-and-cost governance rollout setup reports success before policy compliance evaluation becomes observable.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Get Azure Policy compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data)

**Source reviewed:** 2026-08-31

## LAB05-Q24 — D

**Question:** The policy-and-cost governance rollout configuration is complete; the cost governance reviewers need evidence it can block a noncompliant creation request before the resource is deployed. Which observation shows success?

- **A — Incorrect.** Read the notification operator, threshold, threshold type, and enabled state.
  Read the notification operator, threshold, threshold type, and enabled state. In the policy-and-cost governance rollout, this check observes forecast budget alerts. Policy-and-cost governance rollout could pass forecast budget alerts while deny policy effect is wrong; policy-and-cost governance rollout still lacks deny policy effect proof.
- **B — Incorrect.** Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.
  Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription. In the policy-and-cost governance rollout, this check observes governance scope and exclusions. Policy-and-cost governance rollout output covers governance scope and exclusions, not deny policy effect; the deny policy effect requirement to block a noncompliant creation request before the resource is deployed remains unverified.
- **C — Incorrect.** Query policy states after evaluation and match the resource ID, assignment ID, and compliance state.
  Query policy states after evaluation and match the resource ID, assignment ID, and compliance state. In the policy-and-cost governance rollout, this check observes policy compliance evaluation. Policy compliance evaluation success in policy-and-cost governance rollout cannot verify deny policy effect; policy-and-cost governance rollout cannot block a noncompliant creation request before the resource is deployed until deny policy effect evidence exists.
- **D — Correct.** Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
  Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment. For policy-and-cost governance rollout, this deny policy effect read confirms the service can block a noncompliant creation request before the resource is deployed.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Understand Azure Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)

**Source reviewed:** 2026-08-31

## LAB05-Q25 — B

**Question:** The cost governance validation asks whether the policy-and-cost governance rollout can correct existing noncompliant resources after a managed change is assigned. Which observable state is strongest?

- **A — Incorrect.** Query the notification contact collection and confirm the threshold is enabled.
  Query the notification contact collection and confirm the threshold is enabled. In the policy-and-cost governance rollout, this check observes budget notification contacts. Policy-and-cost governance rollout output covers budget notification contacts, not modify and remediation; the modify and remediation requirement to correct existing noncompliant resources after a managed change is assigned remains unverified.
- **B — Correct.** Inspect the remediation deployment and query the corrected property on each target resource.
  Inspect the remediation deployment and query the corrected property on each target resource. The policy-and-cost governance rollout reads modify and remediation directly; that modify and remediation result proves the policy-and-cost governance rollout can correct existing noncompliant resources after a managed change is assigned without another mutation.
- **C — Incorrect.** Read the assignment's definition ID, scope, parameters, and enforcement mode.
  Read the assignment's definition ID, scope, parameters, and enforcement mode. In the policy-and-cost governance rollout, this check observes policy definitions and assignments. Policy-and-cost governance rollout reads policy definitions and assignments, leaving modify and remediation unproved in policy-and-cost governance rollout; policy-and-cost governance rollout still has no modify and remediation proof.
- **D — Incorrect.** Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
  Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment. In the policy-and-cost governance rollout, this check observes deny policy effect. Policy-and-cost governance rollout could pass deny policy effect while modify and remediation is wrong; policy-and-cost governance rollout still lacks modify and remediation proof.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Remediate noncompliant resources with Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

**Source reviewed:** 2026-08-31

## LAB05-Q26 — D

**Question:** A policy-and-cost governance rollout review must prove the cost governance ability to receive notifications without expecting spending to be stopped automatically. Which check avoids an adjacent feature?

- **A — Incorrect.** Query recommendation category, impact, resource ID, and short description.
  Query recommendation category, impact, resource ID, and short description. In the policy-and-cost governance rollout, this check observes Advisor cost recommendations. Advisor cost recommendations success in policy-and-cost governance rollout cannot verify budget behavior; policy-and-cost governance rollout cannot receive notifications without expecting spending to be stopped automatically until budget behavior evidence exists.
- **B — Incorrect.** Query the initiative assignment and enumerate its member definition references.
  Query the initiative assignment and enumerate its member definition references. In the policy-and-cost governance rollout, this check observes policy initiatives. Policy-and-cost governance rollout reads policy initiatives, leaving budget behavior unproved in policy-and-cost governance rollout; policy-and-cost governance rollout still has no budget behavior proof.
- **C — Incorrect.** Inspect the remediation deployment and query the corrected property on each target resource.
  Inspect the remediation deployment and query the corrected property on each target resource. In the policy-and-cost governance rollout, this check observes modify and remediation. Policy-and-cost governance rollout could pass modify and remediation while budget behavior is wrong; policy-and-cost governance rollout still lacks budget behavior proof.
- **D — Correct.** Query the budget amount, time grain, thresholds, and current cost separately.
  For the policy-and-cost governance rollout, this budget behavior observation is decisive: query the budget amount, time grain, thresholds, and current cost separately. It is policy-and-cost governance rollout evidence that operators can receive notifications without expecting spending to be stopped automatically.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q27 — D

**Question:** The policy-and-cost governance rollout evidence bundle needs a cost governance result showing it can notify owners before projected spending reaches the configured limit. Which result belongs in the checkpoint?

- **A — Incorrect.** Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.
  Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription. In the policy-and-cost governance rollout, this check observes governance scope and exclusions. Policy-and-cost governance rollout reads governance scope and exclusions, leaving forecast budget alerts unproved in policy-and-cost governance rollout; policy-and-cost governance rollout still has no forecast budget alerts proof.
- **B — Incorrect.** Query policy states after evaluation and match the resource ID, assignment ID, and compliance state.
  Query policy states after evaluation and match the resource ID, assignment ID, and compliance state. In the policy-and-cost governance rollout, this check observes policy compliance evaluation. Policy-and-cost governance rollout could pass policy compliance evaluation while forecast budget alerts is wrong; policy-and-cost governance rollout still lacks forecast budget alerts proof.
- **C — Incorrect.** Query the budget amount, time grain, thresholds, and current cost separately.
  Query the budget amount, time grain, thresholds, and current cost separately. In the policy-and-cost governance rollout, this check observes budget behavior. Policy-and-cost governance rollout output covers budget behavior, not forecast budget alerts; the forecast budget alerts requirement to notify owners before projected spending reaches the configured limit remains unverified.
- **D — Correct.** Read the notification operator, threshold, threshold type, and enabled state.
  Read the notification operator, threshold, threshold type, and enabled state. Because the policy-and-cost governance rollout check observes forecast budget alerts, it independently verifies the requirement to notify owners before projected spending reaches the configured limit.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q28 — B

**Question:** Before policy-and-cost governance rollout cleanup, the cost governance team must reconfirm it can route cost notifications to the approved recipients. Which read-only inspection should run?

- **A — Incorrect.** Read the assignment's definition ID, scope, parameters, and enforcement mode.
  Read the assignment's definition ID, scope, parameters, and enforcement mode. In the policy-and-cost governance rollout, this check observes policy definitions and assignments. Policy-and-cost governance rollout could pass policy definitions and assignments while budget notification contacts is wrong; policy-and-cost governance rollout still lacks budget notification contacts proof.
- **B — Correct.** Query the notification contact collection and confirm the threshold is enabled.
  The policy-and-cost governance rollout validator needs this budget notification contacts result: query the notification contact collection and confirm the threshold is enabled. It proves the outcome to route cost notifications to the approved recipients rather than an adjacent checkpoint.
- **C — Incorrect.** Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
  Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment. In the policy-and-cost governance rollout, this check observes deny policy effect. Deny policy effect success in policy-and-cost governance rollout cannot verify budget notification contacts; policy-and-cost governance rollout cannot route cost notifications to the approved recipients until budget notification contacts evidence exists.
- **D — Incorrect.** Read the notification operator, threshold, threshold type, and enabled state.
  Read the notification operator, threshold, threshold type, and enabled state. In the policy-and-cost governance rollout, this check observes forecast budget alerts. Policy-and-cost governance rollout reads forecast budget alerts, leaving budget notification contacts unproved in policy-and-cost governance rollout; policy-and-cost governance rollout still has no budget notification contacts proof.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q29 — D

**Question:** The policy-and-cost governance rollout setup reports success after the cost governance attempt to identify rightsizing or shutdown opportunities from service telemetry. Which cost governance read-only observation proves the policy-and-cost governance rollout outcome?

- **A — Incorrect.** Query the initiative assignment and enumerate its member definition references.
  Query the initiative assignment and enumerate its member definition references. In the policy-and-cost governance rollout, this check observes policy initiatives. Policy-and-cost governance rollout output covers policy initiatives, not Advisor cost recommendations; the Advisor cost recommendations requirement to identify rightsizing or shutdown opportunities from service telemetry remains unverified.
- **B — Incorrect.** Inspect the remediation deployment and query the corrected property on each target resource.
  Inspect the remediation deployment and query the corrected property on each target resource. In the policy-and-cost governance rollout, this check observes modify and remediation. Modify and remediation success in policy-and-cost governance rollout cannot verify Advisor cost recommendations; policy-and-cost governance rollout cannot identify rightsizing or shutdown opportunities from service telemetry until Advisor cost recommendations evidence exists.
- **C — Incorrect.** Query the notification contact collection and confirm the threshold is enabled.
  Query the notification contact collection and confirm the threshold is enabled. In the policy-and-cost governance rollout, this check observes budget notification contacts. Policy-and-cost governance rollout reads budget notification contacts, leaving Advisor cost recommendations unproved in policy-and-cost governance rollout; policy-and-cost governance rollout still has no Advisor cost recommendations proof.
- **D — Correct.** Query recommendation category, impact, resource ID, and short description.
  Query recommendation category, impact, resource ID, and short description. This is independent Advisor cost recommendations evidence for the policy-and-cost governance rollout, even if policy-and-cost governance rollout setup reports success before Advisor cost recommendations becomes observable.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Azure Advisor cost recommendations](https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations)

**Source reviewed:** 2026-08-31

## LAB05-Q30 — C

**Question:** The cost governance log says the policy-and-cost governance rollout can now exclude an approved child scope without weakening governance elsewhere. Which cost governance state should the policy-and-cost governance rollout acceptance test retain?

- **A — Incorrect.** Query policy states after evaluation and match the resource ID, assignment ID, and compliance state.
  Query policy states after evaluation and match the resource ID, assignment ID, and compliance state. In the policy-and-cost governance rollout, this check observes policy compliance evaluation. Policy compliance evaluation success in policy-and-cost governance rollout cannot verify governance scope and exclusions; policy-and-cost governance rollout cannot exclude an approved child scope without weakening governance elsewhere until governance scope and exclusions evidence exists.
- **B — Incorrect.** Query the budget amount, time grain, thresholds, and current cost separately.
  Query the budget amount, time grain, thresholds, and current cost separately. In the policy-and-cost governance rollout, this check observes budget behavior. Policy-and-cost governance rollout reads budget behavior, leaving governance scope and exclusions unproved in policy-and-cost governance rollout; policy-and-cost governance rollout still has no governance scope and exclusions proof.
- **C — Correct.** Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.
  Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription. For policy-and-cost governance rollout, this governance scope and exclusions read confirms the service can exclude an approved child scope without weakening governance elsewhere.
- **D — Incorrect.** Query recommendation category, impact, resource ID, and short description.
  Query recommendation category, impact, resource ID, and short description. In the policy-and-cost governance rollout, this check observes Advisor cost recommendations. Policy-and-cost governance rollout output covers Advisor cost recommendations, not governance scope and exclusions; the governance scope and exclusions requirement to exclude an approved child scope without weakening governance elsewhere remains unverified.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Azure Policy assignment scope](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/scope)

**Source reviewed:** 2026-08-31

## LAB05-Q31 — C

**Question:** A cost governance break/fix in the policy-and-cost governance rollout fails when operators try to package a governance rule and apply it at the intended scope. Which diagnosis fits?

- **A — Incorrect.** Only one member definition was assigned, leaving the rest of the baseline unapplied.
  Only one member definition was assigned, leaving the rest of the baseline unapplied. The policy-and-cost governance rollout fault concerns policy initiatives. Policy-and-cost governance rollout has policy initiatives impact, but policy definitions and assignments is the policy-and-cost governance rollout failed path; the policy initiatives state cannot produce policy definitions and assignments failure.
- **B — Incorrect.** The design expects reaching the budget threshold to shut down resources automatically.
  The design expects reaching the budget threshold to shut down resources automatically. The policy-and-cost governance rollout fault concerns budget behavior. Policy-and-cost governance rollout could repair budget behavior while policy definitions and assignments stays broken in policy-and-cost governance rollout; the policy-and-cost governance rollout remains unable to package a governance rule and apply it at the intended scope.
- **C — Correct.** The definition exists in the tenant but has never been assigned to the target scope.
  The definition exists in the tenant but has never been assigned to the target scope. This policy-and-cost governance rollout condition breaks policy definitions and assignments, explaining why operators cannot package a governance rule and apply it at the intended scope.
- **D — Incorrect.** The target subscription is listed in notScopes and therefore never receives the policy assignment.
  The target subscription is listed in notScopes and therefore never receives the policy assignment. The policy-and-cost governance rollout fault concerns governance scope and exclusions. Policy-and-cost governance rollout may fix governance scope and exclusions, yet policy definitions and assignments still fails; this policy-and-cost governance rollout diagnosis of governance scope and exclusions is wrong for policy definitions and assignments.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

**Source reviewed:** 2026-08-31

## LAB05-Q32 — A

**Question:** The policy-and-cost governance rollout troubleshooting scope is the cost governance need to deploy several related governance rules as one versioned assignment. Which condition should be corrected first?

- **A — Correct.** Only one member definition was assigned, leaving the rest of the baseline unapplied.
  For the policy-and-cost governance rollout, the policy initiatives failure is causal: only one member definition was assigned, leaving the rest of the baseline unapplied. Correcting it restores the ability to deploy several related governance rules as one versioned assignment.
- **B — Incorrect.** Validation ran immediately after assignment and treated a not-started evaluation as compliant.
  Validation ran immediately after assignment and treated a not-started evaluation as compliant. The policy-and-cost governance rollout fault concerns policy compliance evaluation. Policy-and-cost governance rollout failed on policy initiatives; this policy compliance evaluation finding redirects policy-and-cost governance rollout remediation away from policy initiatives.
- **C — Incorrect.** Only an actual-cost alert exists, so no warning occurs while spend is merely forecast to exceed the limit.
  Only an actual-cost alert exists, so no warning occurs while spend is merely forecast to exceed the limit. The policy-and-cost governance rollout fault concerns forecast budget alerts. Policy-and-cost governance rollout may fix forecast budget alerts, yet policy initiatives still fails; this policy-and-cost governance rollout diagnosis of forecast budget alerts is wrong for policy initiatives.
- **D — Incorrect.** The definition exists in the tenant but has never been assigned to the target scope.
  The definition exists in the tenant but has never been assigned to the target scope. The policy-and-cost governance rollout fault concerns policy definitions and assignments. Policy-and-cost governance rollout has policy definitions and assignments impact, but policy initiatives is the policy-and-cost governance rollout failed path; the policy definitions and assignments state cannot produce policy initiatives failure.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Azure Policy initiative definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure)

**Source reviewed:** 2026-08-31

## LAB05-Q33 — B

**Question:** The policy-and-cost governance rollout result is partial because the cost governance cannot measure existing resources against an assigned governance rule. Which condition accounts for that result?

- **A — Incorrect.** The assignment uses audit, so the noncompliant request succeeds and is only reported.
  The assignment uses audit, so the noncompliant request succeeds and is only reported. The policy-and-cost governance rollout fault concerns deny policy effect. Policy-and-cost governance rollout failed on policy compliance evaluation; this deny policy effect finding redirects policy-and-cost governance rollout remediation away from policy compliance evaluation.
- **B — Correct.** Validation ran immediately after assignment and treated a not-started evaluation as compliant.
  Validation ran immediately after assignment and treated a not-started evaluation as compliant. The finding is specific to policy compliance evaluation in the policy-and-cost governance rollout; repairing policy compliance evaluation restores the policy-and-cost governance rollout ability to measure existing resources against an assigned governance rule.
- **C — Incorrect.** The action group resource ID belongs to a scope that the budget notification cannot resolve.
  The action group resource ID belongs to a scope that the budget notification cannot resolve. The policy-and-cost governance rollout fault concerns budget notification contacts. Policy-and-cost governance rollout has budget notification contacts impact, but policy compliance evaluation is the policy-and-cost governance rollout failed path; the budget notification contacts state cannot produce policy compliance evaluation failure.
- **D — Incorrect.** Only one member definition was assigned, leaving the rest of the baseline unapplied.
  Only one member definition was assigned, leaving the rest of the baseline unapplied. The policy-and-cost governance rollout fault concerns policy initiatives. Policy-and-cost governance rollout could repair policy initiatives while policy compliance evaluation stays broken in policy-and-cost governance rollout; the policy-and-cost governance rollout remains unable to measure existing resources against an assigned governance rule.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Get Azure Policy compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data)

**Source reviewed:** 2026-08-31

## LAB05-Q34 — C

**Question:** The cost governance evidence shows the policy-and-cost governance rollout cannot block a noncompliant creation request before the resource is deployed. Which root cause fits that evidence?

- **A — Incorrect.** The assignment has no managed identity permission to perform its required modification.
  The assignment has no managed identity permission to perform its required modification. The policy-and-cost governance rollout fault concerns modify and remediation. Policy-and-cost governance rollout may fix modify and remediation, yet deny policy effect still fails; this policy-and-cost governance rollout diagnosis of modify and remediation is wrong for deny policy effect.
- **B — Incorrect.** The workflow assumes a cost recommendation has already resized or deleted the resource.
  The workflow assumes a cost recommendation has already resized or deleted the resource. The policy-and-cost governance rollout fault concerns Advisor cost recommendations. Policy-and-cost governance rollout has Advisor cost recommendations impact, but deny policy effect is the policy-and-cost governance rollout failed path; the Advisor cost recommendations state cannot produce deny policy effect failure.
- **C — Correct.** The assignment uses audit, so the noncompliant request succeeds and is only reported.
  The policy-and-cost governance rollout cannot block a noncompliant creation request before the resource is deployed because of this deny policy effect defect: the assignment uses audit, so the noncompliant request succeeds and is only reported. The symptom and repair align.
- **D — Incorrect.** Validation ran immediately after assignment and treated a not-started evaluation as compliant.
  Validation ran immediately after assignment and treated a not-started evaluation as compliant. The policy-and-cost governance rollout fault concerns policy compliance evaluation. Policy-and-cost governance rollout failed on deny policy effect; this policy compliance evaluation finding redirects policy-and-cost governance rollout remediation away from deny policy effect.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Understand Azure Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)

**Source reviewed:** 2026-08-31

## LAB05-Q35 — A

**Question:** Although the policy-and-cost governance rollout is meant to let the cost governance correct existing noncompliant resources after a managed change is assigned, its checkpoint fails. Which cost governance defect explains the failure?

- **A — Correct.** The assignment has no managed identity permission to perform its required modification.
  The assignment has no managed identity permission to perform its required modification. Removing this modify and remediation condition lets the policy-and-cost governance rollout correct existing noncompliant resources after a managed change is assigned while leaving healthy controls unchanged.
- **B — Incorrect.** The design expects reaching the budget threshold to shut down resources automatically.
  The design expects reaching the budget threshold to shut down resources automatically. The policy-and-cost governance rollout fault concerns budget behavior. Policy-and-cost governance rollout could repair budget behavior while modify and remediation stays broken in policy-and-cost governance rollout; the policy-and-cost governance rollout remains unable to correct existing noncompliant resources after a managed change is assigned.
- **C — Incorrect.** The target subscription is listed in notScopes and therefore never receives the policy assignment.
  The target subscription is listed in notScopes and therefore never receives the policy assignment. The policy-and-cost governance rollout fault concerns governance scope and exclusions. Policy-and-cost governance rollout failed on modify and remediation; this governance scope and exclusions finding redirects policy-and-cost governance rollout remediation away from modify and remediation.
- **D — Incorrect.** The assignment uses audit, so the noncompliant request succeeds and is only reported.
  The assignment uses audit, so the noncompliant request succeeds and is only reported. The policy-and-cost governance rollout fault concerns deny policy effect. Policy-and-cost governance rollout may fix deny policy effect, yet modify and remediation still fails; this policy-and-cost governance rollout diagnosis of deny policy effect is wrong for modify and remediation.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Remediate noncompliant resources with Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

**Source reviewed:** 2026-08-31

## LAB05-Q36 — B

**Question:** The cost governance support team isolated the policy-and-cost governance rollout incident to the attempt to receive notifications without expecting spending to be stopped automatically. Which condition prevents success?

- **A — Incorrect.** Only an actual-cost alert exists, so no warning occurs while spend is merely forecast to exceed the limit.
  Only an actual-cost alert exists, so no warning occurs while spend is merely forecast to exceed the limit. The policy-and-cost governance rollout fault concerns forecast budget alerts. Policy-and-cost governance rollout could repair forecast budget alerts while budget behavior stays broken in policy-and-cost governance rollout; the policy-and-cost governance rollout remains unable to receive notifications without expecting spending to be stopped automatically.
- **B — Correct.** The design expects reaching the budget threshold to shut down resources automatically.
  The design expects reaching the budget threshold to shut down resources automatically. In policy-and-cost governance rollout, this budget behavior cause matches the failure to receive notifications without expecting spending to be stopped automatically.
- **C — Incorrect.** The definition exists in the tenant but has never been assigned to the target scope.
  The definition exists in the tenant but has never been assigned to the target scope. The policy-and-cost governance rollout fault concerns policy definitions and assignments. Policy-and-cost governance rollout may fix policy definitions and assignments, yet budget behavior still fails; this policy-and-cost governance rollout diagnosis of policy definitions and assignments is wrong for budget behavior.
- **D — Incorrect.** The assignment has no managed identity permission to perform its required modification.
  The assignment has no managed identity permission to perform its required modification. The policy-and-cost governance rollout fault concerns modify and remediation. Policy-and-cost governance rollout has modify and remediation impact, but budget behavior is the policy-and-cost governance rollout failed path; the modify and remediation state cannot produce budget behavior failure.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q37 — C

**Question:** A policy-and-cost governance rollout query surprises the cloud governance analyst enforcing standards and controlling spend during the cost governance attempt to notify owners before projected spending reaches the configured limit. Which finding explains it?

- **A — Incorrect.** The action group resource ID belongs to a scope that the budget notification cannot resolve.
  The action group resource ID belongs to a scope that the budget notification cannot resolve. The policy-and-cost governance rollout fault concerns budget notification contacts. Policy-and-cost governance rollout failed on forecast budget alerts; this budget notification contacts finding redirects policy-and-cost governance rollout remediation away from forecast budget alerts.
- **B — Incorrect.** Only one member definition was assigned, leaving the rest of the baseline unapplied.
  Only one member definition was assigned, leaving the rest of the baseline unapplied. The policy-and-cost governance rollout fault concerns policy initiatives. Policy-and-cost governance rollout may fix policy initiatives, yet forecast budget alerts still fails; this policy-and-cost governance rollout diagnosis of policy initiatives is wrong for forecast budget alerts.
- **C — Correct.** Only an actual-cost alert exists, so no warning occurs while spend is merely forecast to exceed the limit.
  Only an actual-cost alert exists, so no warning occurs while spend is merely forecast to exceed the limit. This policy-and-cost governance rollout condition breaks forecast budget alerts, explaining why operators cannot notify owners before projected spending reaches the configured limit.
- **D — Incorrect.** The design expects reaching the budget threshold to shut down resources automatically.
  The design expects reaching the budget threshold to shut down resources automatically. The policy-and-cost governance rollout fault concerns budget behavior. Policy-and-cost governance rollout could repair budget behavior while forecast budget alerts stays broken in policy-and-cost governance rollout; the policy-and-cost governance rollout remains unable to notify owners before projected spending reaches the configured limit.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q38 — D

**Question:** Other policy-and-cost governance rollout components are healthy, but the cost governance still cannot route cost notifications to the approved recipients. Which state causes the isolated failure?

- **A — Incorrect.** The workflow assumes a cost recommendation has already resized or deleted the resource.
  The workflow assumes a cost recommendation has already resized or deleted the resource. The policy-and-cost governance rollout fault concerns Advisor cost recommendations. Policy-and-cost governance rollout may fix Advisor cost recommendations, yet budget notification contacts still fails; this policy-and-cost governance rollout diagnosis of Advisor cost recommendations is wrong for budget notification contacts.
- **B — Incorrect.** Validation ran immediately after assignment and treated a not-started evaluation as compliant.
  Validation ran immediately after assignment and treated a not-started evaluation as compliant. The policy-and-cost governance rollout fault concerns policy compliance evaluation. Policy-and-cost governance rollout has policy compliance evaluation impact, but budget notification contacts is the policy-and-cost governance rollout failed path; the policy compliance evaluation state cannot produce budget notification contacts failure.
- **C — Incorrect.** Only an actual-cost alert exists, so no warning occurs while spend is merely forecast to exceed the limit.
  Only an actual-cost alert exists, so no warning occurs while spend is merely forecast to exceed the limit. The policy-and-cost governance rollout fault concerns forecast budget alerts. Policy-and-cost governance rollout could repair forecast budget alerts while budget notification contacts stays broken in policy-and-cost governance rollout; the policy-and-cost governance rollout remains unable to route cost notifications to the approved recipients.
- **D — Correct.** The action group resource ID belongs to a scope that the budget notification cannot resolve.
  For the policy-and-cost governance rollout, the budget notification contacts failure is causal: the action group resource ID belongs to a scope that the budget notification cannot resolve. Correcting it restores the ability to route cost notifications to the approved recipients.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q39 — A

**Question:** During a cost governance fault drill, the policy-and-cost governance rollout does not identify rightsizing or shutdown opportunities from service telemetry. Which finding identifies the defect?

- **A — Correct.** The workflow assumes a cost recommendation has already resized or deleted the resource.
  The workflow assumes a cost recommendation has already resized or deleted the resource. The finding is specific to Advisor cost recommendations in the policy-and-cost governance rollout; repairing Advisor cost recommendations restores the policy-and-cost governance rollout ability to identify rightsizing or shutdown opportunities from service telemetry.
- **B — Incorrect.** The target subscription is listed in notScopes and therefore never receives the policy assignment.
  The target subscription is listed in notScopes and therefore never receives the policy assignment. The policy-and-cost governance rollout fault concerns governance scope and exclusions. Policy-and-cost governance rollout could repair governance scope and exclusions while Advisor cost recommendations stays broken in policy-and-cost governance rollout; the policy-and-cost governance rollout remains unable to identify rightsizing or shutdown opportunities from service telemetry.
- **C — Incorrect.** The assignment uses audit, so the noncompliant request succeeds and is only reported.
  The assignment uses audit, so the noncompliant request succeeds and is only reported. The policy-and-cost governance rollout fault concerns deny policy effect. Policy-and-cost governance rollout failed on Advisor cost recommendations; this deny policy effect finding redirects policy-and-cost governance rollout remediation away from Advisor cost recommendations.
- **D — Incorrect.** The action group resource ID belongs to a scope that the budget notification cannot resolve.
  The action group resource ID belongs to a scope that the budget notification cannot resolve. The policy-and-cost governance rollout fault concerns budget notification contacts. Policy-and-cost governance rollout may fix budget notification contacts, yet Advisor cost recommendations still fails; this policy-and-cost governance rollout diagnosis of budget notification contacts is wrong for Advisor cost recommendations.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Azure Advisor cost recommendations](https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations)

**Source reviewed:** 2026-08-31

## LAB05-Q40 — A

**Question:** The policy-and-cost governance rollout setup finishes, yet the cost governance cannot exclude an approved child scope without weakening governance elsewhere. Which misconfiguration explains the mismatch?

- **A — Correct.** The target subscription is listed in notScopes and therefore never receives the policy assignment.
  The policy-and-cost governance rollout cannot exclude an approved child scope without weakening governance elsewhere because of this governance scope and exclusions defect: the target subscription is listed in notScopes and therefore never receives the policy assignment. The symptom and repair align.
- **B — Incorrect.** The definition exists in the tenant but has never been assigned to the target scope.
  The definition exists in the tenant but has never been assigned to the target scope. The policy-and-cost governance rollout fault concerns policy definitions and assignments. Policy-and-cost governance rollout failed on governance scope and exclusions; this policy definitions and assignments finding redirects policy-and-cost governance rollout remediation away from governance scope and exclusions.
- **C — Incorrect.** The assignment has no managed identity permission to perform its required modification.
  The assignment has no managed identity permission to perform its required modification. The policy-and-cost governance rollout fault concerns modify and remediation. Policy-and-cost governance rollout may fix modify and remediation, yet governance scope and exclusions still fails; this policy-and-cost governance rollout diagnosis of modify and remediation is wrong for governance scope and exclusions.
- **D — Incorrect.** The workflow assumes a cost recommendation has already resized or deleted the resource.
  The workflow assumes a cost recommendation has already resized or deleted the resource. The policy-and-cost governance rollout fault concerns Advisor cost recommendations. Policy-and-cost governance rollout has Advisor cost recommendations impact, but governance scope and exclusions is the policy-and-cost governance rollout failed path; the Advisor cost recommendations state cannot produce governance scope and exclusions failure.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Azure Policy assignment scope](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/scope)

**Source reviewed:** 2026-08-31

## LAB05-Q41 — C

**Question:** The cloud governance analyst enforcing standards and controlling spend needs a safe policy-and-cost governance rollout change to package a governance rule and apply it at the intended scope, followed by cost governance evidence. Which pair merits approval?

- **A — Incorrect.** First, Trigger a compliance scan after assignment when the lab needs deterministic validation timing. Then, Query policy states after evaluation and match the resource ID, assignment ID, and compliance state.
  First, Trigger a compliance scan after assignment when the lab needs deterministic validation timing. Then, Query policy states after evaluation and match the resource ID, assignment ID, and compliance state. This policy-and-cost governance rollout pair serves policy compliance evaluation. Policy compliance evaluation cannot replace policy definitions and assignments in policy-and-cost governance rollout. Use this policy definitions and assignments pair instead: First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode.
- **B — Incorrect.** First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state.
  First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state. This policy-and-cost governance rollout pair serves forecast budget alerts. Policy-and-cost governance rollout proves forecast budget alerts, but policy definitions and assignments lacks implementation in policy-and-cost governance rollout and policy definitions and assignments proof; the policy definitions and assignments outcome to package a governance rule and apply it at the intended scope remains open.
- **C — Correct.** First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode.
  First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode. This ordered policy definitions and assignments workflow lets the policy-and-cost governance rollout package a governance rule and apply it at the intended scope and then verify the resulting state.
- **D — Incorrect.** First, Configure an approved notification recipient and verify it is valid at the selected scope. Then, Query the notification contact collection and confirm the threshold is enabled.
  First, Configure an approved notification recipient and verify it is valid at the selected scope. Then, Query the notification contact collection and confirm the threshold is enabled. This policy-and-cost governance rollout pair serves budget notification contacts. Policy-and-cost governance rollout closes budget notification contacts, not policy definitions and assignments; without the policy definitions and assignments workflow, it cannot package a governance rule and apply it at the intended scope.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

**Source reviewed:** 2026-08-31

## LAB05-Q42 — A

**Question:** The policy-and-cost governance rollout has two cost governance gates: deploy several related governance rules as one versioned assignment, then prove the policy-and-cost governance rollout state. Which cost governance sequence works?

- **A — Correct.** First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references.
  First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references. For policy-and-cost governance rollout, the policy initiatives operation precedes its policy initiatives read-back check, allowing it to deploy several related governance rules as one versioned assignment.
- **B — Incorrect.** First, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
  First, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment. This policy-and-cost governance rollout pair serves deny policy effect. Policy-and-cost governance rollout uses deny policy effect for both steps; policy initiatives remains untouched in policy-and-cost governance rollout, so its policy initiatives gate to deploy several related governance rules as one versioned assignment fails.
- **C — Incorrect.** First, Configure an approved notification recipient and verify it is valid at the selected scope. Then, Query the notification contact collection and confirm the threshold is enabled.
  First, Configure an approved notification recipient and verify it is valid at the selected scope. Then, Query the notification contact collection and confirm the threshold is enabled. This policy-and-cost governance rollout pair serves budget notification contacts. Policy-and-cost governance rollout closes budget notification contacts, not policy initiatives; without the policy initiatives workflow, it cannot deploy several related governance rules as one versioned assignment.
- **D — Incorrect.** First, Retrieve active cost recommendations and review impact before approving any remediation. Then, Query recommendation category, impact, resource ID, and short description.
  First, Retrieve active cost recommendations and review impact before approving any remediation. Then, Query recommendation category, impact, resource ID, and short description. This policy-and-cost governance rollout pair serves Advisor cost recommendations. Advisor cost recommendations cannot replace policy initiatives in policy-and-cost governance rollout. Use this policy initiatives pair instead: First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Azure Policy initiative definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure)

**Source reviewed:** 2026-08-31

## LAB05-Q43 — C

**Question:** Which cost governance path makes the policy-and-cost governance rollout able to measure existing resources against an assigned governance rule, then inspects the defining properties?

- **A — Incorrect.** First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource.
  First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource. This policy-and-cost governance rollout pair serves modify and remediation. Policy-and-cost governance rollout uses modify and remediation for both steps; policy compliance evaluation remains untouched in policy-and-cost governance rollout, so its policy compliance evaluation gate to measure existing resources against an assigned governance rule fails.
- **B — Incorrect.** First, Retrieve active cost recommendations and review impact before approving any remediation. Then, Query recommendation category, impact, resource ID, and short description.
  First, Retrieve active cost recommendations and review impact before approving any remediation. Then, Query recommendation category, impact, resource ID, and short description. This policy-and-cost governance rollout pair serves Advisor cost recommendations. Policy-and-cost governance rollout closes Advisor cost recommendations, not policy compliance evaluation; without the policy compliance evaluation workflow, it cannot measure existing resources against an assigned governance rule.
- **C — Correct.** First, Trigger a compliance scan after assignment when the lab needs deterministic validation timing. Then, Query policy states after evaluation and match the resource ID, assignment ID, and compliance state.
  First, Trigger a compliance scan after assignment when the lab needs deterministic validation timing. Then, Query policy states after evaluation and match the resource ID, assignment ID, and compliance state. In the policy-and-cost governance rollout, the first policy compliance evaluation step runs; the policy-and-cost governance rollout then reads policy compliance evaluation state to prove it can measure existing resources against an assigned governance rule.
- **D — Incorrect.** First, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.
  First, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription. This policy-and-cost governance rollout pair serves governance scope and exclusions. Policy-and-cost governance rollout proves governance scope and exclusions, but policy compliance evaluation lacks implementation in policy-and-cost governance rollout and policy compliance evaluation proof; the policy compliance evaluation outcome to measure existing resources against an assigned governance rule remains open.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Get Azure Policy compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data)

**Source reviewed:** 2026-08-31

## LAB05-Q44 — D

**Question:** At the policy-and-cost governance rollout approval gate, operators must show that the cost governance can block a noncompliant creation request before the resource is deployed. Which cost governance configure-and-check pair is defensible?

- **A — Incorrect.** First, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately.
  First, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately. This policy-and-cost governance rollout pair serves budget behavior. Policy-and-cost governance rollout closes budget behavior, not deny policy effect; without the deny policy effect workflow, it cannot block a noncompliant creation request before the resource is deployed.
- **B — Incorrect.** First, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.
  First, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription. This policy-and-cost governance rollout pair serves governance scope and exclusions. Governance scope and exclusions cannot replace deny policy effect in policy-and-cost governance rollout. Use this deny policy effect pair instead: First, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
- **C — Incorrect.** First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode.
  First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode. This policy-and-cost governance rollout pair serves policy definitions and assignments. Policy-and-cost governance rollout proves policy definitions and assignments, but deny policy effect lacks implementation in policy-and-cost governance rollout and deny policy effect proof; the deny policy effect outcome to block a noncompliant creation request before the resource is deployed remains open.
- **D — Correct.** First, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
  For the policy-and-cost governance rollout, the safe deny policy effect order is: first, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment. The policy-and-cost governance rollout records deny policy effect proof after configuration.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Understand Azure Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)

**Source reviewed:** 2026-08-31

## LAB05-Q45 — C

**Question:** The policy-and-cost governance rollout forbids a partial cost governance result. Operators must first correct existing noncompliant resources after a managed change is assigned and afterward confirm the policy-and-cost governance rollout outcome. Which cost governance sequence is complete?

- **A — Incorrect.** First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state.
  First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state. This policy-and-cost governance rollout pair serves forecast budget alerts. Forecast budget alerts cannot replace modify and remediation in policy-and-cost governance rollout. Use this modify and remediation pair instead: First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource.
- **B — Incorrect.** First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode.
  First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode. This policy-and-cost governance rollout pair serves policy definitions and assignments. Policy-and-cost governance rollout proves policy definitions and assignments, but modify and remediation lacks implementation in policy-and-cost governance rollout and modify and remediation proof; the modify and remediation outcome to correct existing noncompliant resources after a managed change is assigned remains open.
- **C — Correct.** First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource.
  First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource. The policy-and-cost governance rollout uses its modify and remediation mutation gate and modify and remediation verification gate before it can correct existing noncompliant resources after a managed change is assigned.
- **D — Incorrect.** First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references.
  First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references. This policy-and-cost governance rollout pair serves policy initiatives. Policy-and-cost governance rollout closes policy initiatives, not modify and remediation; without the modify and remediation workflow, it cannot correct existing noncompliant resources after a managed change is assigned.

**Objectives:** `IG-GOVERN-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Remediate noncompliant resources with Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

**Source reviewed:** 2026-08-31

## LAB05-Q46 — A

**Question:** Only the policy-and-cost governance rollout change needed to receive notifications without expecting spending to be stopped automatically is allowed, and cost governance proof is mandatory. Which pair fits?

- **A — Correct.** First, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately.
  The policy-and-cost governance rollout gets a complete budget behavior sequence here: first, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately. Read-back evidence follows the change.
- **B — Incorrect.** First, Configure an approved notification recipient and verify it is valid at the selected scope. Then, Query the notification contact collection and confirm the threshold is enabled.
  First, Configure an approved notification recipient and verify it is valid at the selected scope. Then, Query the notification contact collection and confirm the threshold is enabled. This policy-and-cost governance rollout pair serves budget notification contacts. Policy-and-cost governance rollout uses budget notification contacts for both steps; budget behavior remains untouched in policy-and-cost governance rollout, so its budget behavior gate to receive notifications without expecting spending to be stopped automatically fails.
- **C — Incorrect.** First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references.
  First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references. This policy-and-cost governance rollout pair serves policy initiatives. Policy-and-cost governance rollout closes policy initiatives, not budget behavior; without the budget behavior workflow, it cannot receive notifications without expecting spending to be stopped automatically.
- **D — Incorrect.** First, Trigger a compliance scan after assignment when the lab needs deterministic validation timing. Then, Query policy states after evaluation and match the resource ID, assignment ID, and compliance state.
  First, Trigger a compliance scan after assignment when the lab needs deterministic validation timing. Then, Query policy states after evaluation and match the resource ID, assignment ID, and compliance state. This policy-and-cost governance rollout pair serves policy compliance evaluation. Policy compliance evaluation cannot replace budget behavior in policy-and-cost governance rollout. Use this budget behavior pair instead: First, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB05-CP01`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q47 — B

**Question:** The policy-and-cost governance rollout runbook separates cost governance mutation from validation while it must notify owners before projected spending reaches the configured limit. Which sequence proves it cleanly?

- **A — Incorrect.** First, Retrieve active cost recommendations and review impact before approving any remediation. Then, Query recommendation category, impact, resource ID, and short description.
  First, Retrieve active cost recommendations and review impact before approving any remediation. Then, Query recommendation category, impact, resource ID, and short description. This policy-and-cost governance rollout pair serves Advisor cost recommendations. Policy-and-cost governance rollout uses Advisor cost recommendations for both steps; forecast budget alerts remains untouched in policy-and-cost governance rollout, so its forecast budget alerts gate to notify owners before projected spending reaches the configured limit fails.
- **B — Correct.** First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state.
  First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state. This ordered forecast budget alerts workflow lets the policy-and-cost governance rollout notify owners before projected spending reaches the configured limit and then verify the resulting state.
- **C — Incorrect.** First, Trigger a compliance scan after assignment when the lab needs deterministic validation timing. Then, Query policy states after evaluation and match the resource ID, assignment ID, and compliance state.
  First, Trigger a compliance scan after assignment when the lab needs deterministic validation timing. Then, Query policy states after evaluation and match the resource ID, assignment ID, and compliance state. This policy-and-cost governance rollout pair serves policy compliance evaluation. Policy compliance evaluation cannot replace forecast budget alerts in policy-and-cost governance rollout. Use this forecast budget alerts pair instead: First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state.
- **D — Incorrect.** First, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
  First, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment. This policy-and-cost governance rollout pair serves deny policy effect. Policy-and-cost governance rollout proves deny policy effect, but forecast budget alerts lacks implementation in policy-and-cost governance rollout and forecast budget alerts proof; the forecast budget alerts outcome to notify owners before projected spending reaches the configured limit remains open.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB05-CP02`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q48 — B

**Question:** The policy-and-cost governance rollout checkpoint requires both this cost governance outcome—route cost notifications to the approved recipients—and a read-only policy-and-cost governance rollout state check. Which cost governance response is complete?

- **A — Incorrect.** First, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.
  First, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription. This policy-and-cost governance rollout pair serves governance scope and exclusions. Policy-and-cost governance rollout closes governance scope and exclusions, not budget notification contacts; without the budget notification contacts workflow, it cannot route cost notifications to the approved recipients.
- **B — Correct.** First, Configure an approved notification recipient and verify it is valid at the selected scope. Then, Query the notification contact collection and confirm the threshold is enabled.
  First, Configure an approved notification recipient and verify it is valid at the selected scope. Then, Query the notification contact collection and confirm the threshold is enabled. For policy-and-cost governance rollout, the budget notification contacts operation precedes its budget notification contacts read-back check, allowing it to route cost notifications to the approved recipients.
- **C — Incorrect.** First, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment.
  First, Use a deny assignment only after validating its condition and approved exclusions. Then, Attempt a controlled noncompliant deployment and confirm the denial references the expected assignment. This policy-and-cost governance rollout pair serves deny policy effect. Policy-and-cost governance rollout proves deny policy effect, but budget notification contacts lacks implementation in policy-and-cost governance rollout and budget notification contacts proof; the budget notification contacts outcome to route cost notifications to the approved recipients remains open.
- **D — Incorrect.** First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource.
  First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource. This policy-and-cost governance rollout pair serves modify and remediation. Policy-and-cost governance rollout uses modify and remediation for both steps; budget notification contacts remains untouched in policy-and-cost governance rollout, so its budget notification contacts gate to route cost notifications to the approved recipients fails.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB05-CP03`).

**Microsoft Learn sources:**

- [Tutorial for creating Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

**Source reviewed:** 2026-08-31

## LAB05-Q49 — A

**Question:** The policy-and-cost governance rollout runbook must identify rightsizing or shutdown opportunities from service telemetry, then retain cost governance read-back evidence. Which policy-and-cost governance rollout pair completes both duties?

- **A — Correct.** First, Retrieve active cost recommendations and review impact before approving any remediation. Then, Query recommendation category, impact, resource ID, and short description.
  First, Retrieve active cost recommendations and review impact before approving any remediation. Then, Query recommendation category, impact, resource ID, and short description. In the policy-and-cost governance rollout, the first Advisor cost recommendations step runs; the policy-and-cost governance rollout then reads Advisor cost recommendations state to prove it can identify rightsizing or shutdown opportunities from service telemetry.
- **B — Incorrect.** First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode.
  First, Select or author the definition and then assign it at the narrowest required governance scope. Then, Read the assignment's definition ID, scope, parameters, and enforcement mode. This policy-and-cost governance rollout pair serves policy definitions and assignments. Policy-and-cost governance rollout proves policy definitions and assignments, but Advisor cost recommendations lacks implementation in policy-and-cost governance rollout and Advisor cost recommendations proof; the Advisor cost recommendations outcome to identify rightsizing or shutdown opportunities from service telemetry remains open.
- **C — Incorrect.** First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource.
  First, Assign the modify policy with a managed identity and create remediation for existing resources. Then, Inspect the remediation deployment and query the corrected property on each target resource. This policy-and-cost governance rollout pair serves modify and remediation. Policy-and-cost governance rollout uses modify and remediation for both steps; Advisor cost recommendations remains untouched in policy-and-cost governance rollout, so its Advisor cost recommendations gate to identify rightsizing or shutdown opportunities from service telemetry fails.
- **D — Incorrect.** First, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately.
  First, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately. This policy-and-cost governance rollout pair serves budget behavior. Policy-and-cost governance rollout closes budget behavior, not Advisor cost recommendations; without the Advisor cost recommendations workflow, it cannot identify rightsizing or shutdown opportunities from service telemetry.

**Objectives:** `IG-GOVERN-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB05-CP04`).

**Microsoft Learn sources:**

- [Azure Advisor cost recommendations](https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations)

**Source reviewed:** 2026-08-31

## LAB05-Q50 — C

**Question:** To satisfy the cost governance requirement, operators must change the policy-and-cost governance rollout configuration and prove it can exclude an approved child scope without weakening governance elsewhere. Which sequence is coherent?

- **A — Incorrect.** First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references.
  First, Use an initiative when one compliance baseline requires several coordinated policy rules. Then, Query the initiative assignment and enumerate its member definition references. This policy-and-cost governance rollout pair serves policy initiatives. Policy-and-cost governance rollout proves policy initiatives, but governance scope and exclusions lacks implementation in policy-and-cost governance rollout and governance scope and exclusions proof; the governance scope and exclusions outcome to exclude an approved child scope without weakening governance elsewhere remains open.
- **B — Incorrect.** First, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately.
  First, Create a budget at the intended billing scope with thresholds and notification recipients. Then, Query the budget amount, time grain, thresholds, and current cost separately. This policy-and-cost governance rollout pair serves budget behavior. Policy-and-cost governance rollout uses budget behavior for both steps; governance scope and exclusions remains untouched in policy-and-cost governance rollout, so its governance scope and exclusions gate to exclude an approved child scope without weakening governance elsewhere fails.
- **C — Correct.** First, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.
  For the policy-and-cost governance rollout, the safe governance scope and exclusions order is: first, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription. The policy-and-cost governance rollout records governance scope and exclusions proof after configuration.
- **D — Incorrect.** First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state.
  First, Add a forecast notification early enough for the owner to correct projected overspend. Then, Read the notification operator, threshold, threshold type, and enabled state. This policy-and-cost governance rollout pair serves forecast budget alerts. Forecast budget alerts cannot replace governance scope and exclusions in policy-and-cost governance rollout. Use this governance scope and exclusions pair instead: First, Set notScopes only for approved exceptions and keep the assignment at the shared parent scope. Then, Compare the assignment scope, excluded scopes, and compliance records from each descendant subscription.

**Objectives:** `IG-GOVERN-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB05-CP05`).

**Microsoft Learn sources:**

- [Azure Policy assignment scope](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/scope)

**Source reviewed:** 2026-08-31
