# Lab 23 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB23-Q01 — C

**Question:** The actionable alert-routing design acceptance criteria require operators to evaluate a numeric signal against a threshold over a defined window. Which service fact supports that requirement?

- **A — Incorrect.** An alert rule evaluates only the resources included in its configured scopes and supported regional model.
  An alert rule evaluates only the resources included in its configured scopes and supported regional model. In the actionable alert-routing design, this statement describes alert target scopes. Actionable alert-routing design asks about metric alert conditions; this alert target scopes choice leaves the metric alert conditions explanation missing.
- **B — Incorrect.** An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation.
  An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation. In the actionable alert-routing design, this statement describes alert suppression rules. The alert suppression rules statement accurately describes alert suppression rules; however, actionable alert-routing design needs metric alert conditions to evaluate a numeric signal against a threshold over a defined window; alert suppression rules cannot replace metric alert conditions.
- **C — Correct.** A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes.
  A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes. The actionable alert-routing design applies that metric alert conditions boundary when operators must evaluate a numeric signal against a threshold over a defined window.
- **D — Incorrect.** A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.
  A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic. In the actionable alert-routing design, this statement describes stateful metric alerts. Metric alert conditions governs actionable alert-routing design; stateful metric alerts cannot support metric alert conditions when operators must evaluate a numeric signal against a threshold over a defined window.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q02 — C

**Question:** An alert routing reviewer challenges whether the actionable alert-routing design can attach an alert rule to the resource that emits the monitored signal. Which response resolves the concern?

- **A — Incorrect.** An action group defines reusable notification and automation receivers and must be linked to the alert rule to run.
  An action group defines reusable notification and automation receivers and must be linked to the alert rule to run. In the actionable alert-routing design, this statement describes action group association. The action group association statement accurately describes action group association; however, actionable alert-routing design needs alert target scopes to attach an alert rule to the resource that emits the monitored signal; action group association cannot replace alert target scopes.
- **B — Incorrect.** Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied.
  Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied. In the actionable alert-routing design, this statement describes scheduled alert processing. Selecting scheduled alert processing for actionable alert-routing design leaves alert target scopes unanswered in actionable alert-routing design; the actionable alert-routing design lacks a alert target scopes basis to attach an alert rule to the resource that emits the monitored signal.
- **C — Correct.** An alert rule evaluates only the resources included in its configured scopes and supported regional model.
  The actionable alert-routing design needs alert target scopes to attach an alert rule to the resource that emits the monitored signal; this option states the applicable alert target scopes rule: an alert rule evaluates only the resources included in its configured scopes and supported regional model.
- **D — Incorrect.** Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions.
  Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions. In the actionable alert-routing design, this statement describes dynamic thresholds. Actionable alert-routing design asks about alert target scopes; this dynamic thresholds choice leaves the alert target scopes explanation missing.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q03 — B

**Question:** The actionable alert-routing design handoff omits the alert routing rule needed to connect an alert rule to reusable notification and automation actions. Which statement should the team add?

- **A — Incorrect.** Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior.
  Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior. In the actionable alert-routing design, this statement describes action group receivers. Selecting action group receivers for actionable alert-routing design leaves action group association unanswered in actionable alert-routing design; the actionable alert-routing design lacks a action group association basis to connect an alert rule to reusable notification and automation actions.
- **B — Correct.** An action group defines reusable notification and automation receivers and must be linked to the alert rule to run.
  An action group defines reusable notification and automation receivers and must be linked to the alert rule to run. This action group association fact resolves the actionable alert-routing design design question about how to connect an alert rule to reusable notification and automation actions.
- **C — Incorrect.** An activity log alert matches subscription-level control-plane events by category and selected conditions.
  An activity log alert matches subscription-level control-plane events by category and selected conditions. In the actionable alert-routing design, this statement describes activity log alerts. Actionable alert-routing design asks about action group association; this activity log alerts choice leaves the action group association explanation missing.
- **D — Incorrect.** Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself.
  Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself. In the actionable alert-routing design, this statement describes alert severity. The alert severity statement accurately describes alert severity; however, actionable alert-routing design needs action group association to connect an alert rule to reusable notification and automation actions; alert severity cannot replace action group association.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q04 — B

**Question:** An alert routing incident review of the actionable alert-routing design depends on the ability to route a fired alert to the intended email, webhook, or automation endpoint. Which platform description is reliable?

- **A — Incorrect.** An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation.
  An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation. In the actionable alert-routing design, this statement describes alert suppression rules. Action group receivers governs actionable alert-routing design; alert suppression rules cannot support action group receivers when operators must route a fired alert to the intended email, webhook, or automation endpoint.
- **B — Correct.** Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior.
  Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior. For actionable alert-routing design, action group receivers supplies the service rule needed to route a fired alert to the intended email, webhook, or automation endpoint.
- **C — Incorrect.** A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.
  A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic. In the actionable alert-routing design, this statement describes stateful metric alerts. The stateful metric alerts statement accurately describes stateful metric alerts; however, actionable alert-routing design needs action group receivers to route a fired alert to the intended email, webhook, or automation endpoint; stateful metric alerts cannot replace action group receivers.
- **D — Incorrect.** A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes.
  A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes. In the actionable alert-routing design, this statement describes metric alert conditions. Selecting metric alert conditions for actionable alert-routing design leaves action group receivers unanswered in actionable alert-routing design; the actionable alert-routing design lacks a action group receivers basis to route a fired alert to the intended email, webhook, or automation endpoint.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q05 — A

**Question:** A monitoring administrator routing and suppressing actionable alerts is updating the alert routing runbook. The requirement is to change delivery of matching notifications while leaving detection intact. Which statement describes Azure behavior correctly?

- **A — Correct.** An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation.
  An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation. In the actionable alert-routing design, this alert suppression rules rule supports the need to change delivery of matching notifications while leaving detection intact.
- **B — Incorrect.** Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied.
  Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied. In the actionable alert-routing design, this statement describes scheduled alert processing. The scheduled alert processing statement accurately describes scheduled alert processing; however, actionable alert-routing design needs alert suppression rules to change delivery of matching notifications while leaving detection intact; scheduled alert processing cannot replace alert suppression rules.
- **C — Incorrect.** Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions.
  Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions. In the actionable alert-routing design, this statement describes dynamic thresholds. Selecting dynamic thresholds for actionable alert-routing design leaves alert suppression rules unanswered in actionable alert-routing design; the actionable alert-routing design lacks a alert suppression rules basis to change delivery of matching notifications while leaving detection intact.
- **D — Incorrect.** An alert rule evaluates only the resources included in its configured scopes and supported regional model.
  An alert rule evaluates only the resources included in its configured scopes and supported regional model. In the actionable alert-routing design, this statement describes alert target scopes. Alert suppression rules governs actionable alert-routing design; alert target scopes cannot support alert suppression rules when operators must change delivery of matching notifications while leaving detection intact.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q06 — D

**Question:** An alert routing peer review asks how the actionable alert-routing design should handle this outcome: apply alert-routing behavior only during an approved maintenance window. Which explanation is accurate?

- **A — Incorrect.** An activity log alert matches subscription-level control-plane events by category and selected conditions.
  An activity log alert matches subscription-level control-plane events by category and selected conditions. In the actionable alert-routing design, this statement describes activity log alerts. The activity log alerts statement accurately describes activity log alerts; however, actionable alert-routing design needs scheduled alert processing to apply alert-routing behavior only during an approved maintenance window; activity log alerts cannot replace scheduled alert processing.
- **B — Incorrect.** Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself.
  Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself. In the actionable alert-routing design, this statement describes alert severity. Selecting alert severity for actionable alert-routing design leaves scheduled alert processing unanswered in actionable alert-routing design; the actionable alert-routing design lacks a scheduled alert processing basis to apply alert-routing behavior only during an approved maintenance window.
- **C — Incorrect.** An action group defines reusable notification and automation receivers and must be linked to the alert rule to run.
  An action group defines reusable notification and automation receivers and must be linked to the alert rule to run. In the actionable alert-routing design, this statement describes action group association. Scheduled alert processing governs actionable alert-routing design; action group association cannot support scheduled alert processing when operators must apply alert-routing behavior only during an approved maintenance window.
- **D — Correct.** Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied.
  For the actionable alert-routing design, the rule for scheduled alert processing is defined by this statement: alert processing schedules use configured recurrence and time-zone rules to control when actions are applied. It supports the required outcome to apply alert-routing behavior only during an approved maintenance window.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q07 — A

**Question:** For the actionable alert-routing design, the alert routing plan must trigger on a matching Activity Log record. Which statement about alert routing belongs in the actionable alert-routing design record?

- **A — Correct.** An activity log alert matches subscription-level control-plane events by category and selected conditions.
  An activity log alert matches subscription-level control-plane events by category and selected conditions. The actionable alert-routing design applies that activity log alerts boundary when operators must trigger on a matching Activity Log record.
- **B — Incorrect.** A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.
  A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic. In the actionable alert-routing design, this statement describes stateful metric alerts. Activity log alerts governs actionable alert-routing design; stateful metric alerts cannot support activity log alerts when operators must trigger on a matching Activity Log record.
- **C — Incorrect.** A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes.
  A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes. In the actionable alert-routing design, this statement describes metric alert conditions. Actionable alert-routing design asks about activity log alerts; this metric alert conditions choice leaves the activity log alerts explanation missing.
- **D — Incorrect.** Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior.
  Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior. In the actionable alert-routing design, this statement describes action group receivers. The action group receivers statement accurately describes action group receivers; however, actionable alert-routing design needs activity log alerts to trigger on a matching Activity Log record; action group receivers cannot replace activity log alerts.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor activity log alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log)

**Source reviewed:** 2026-08-31

## LAB23-Q08 — D

**Question:** The alert routing review compares four claims for the actionable alert-routing design requirement to keep an alert fired until the measured condition has resolved. Which claim is technically sound?

- **A — Incorrect.** Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions.
  Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions. In the actionable alert-routing design, this statement describes dynamic thresholds. Stateful metric alerts governs actionable alert-routing design; dynamic thresholds cannot support stateful metric alerts when operators must keep an alert fired until the measured condition has resolved.
- **B — Incorrect.** An alert rule evaluates only the resources included in its configured scopes and supported regional model.
  An alert rule evaluates only the resources included in its configured scopes and supported regional model. In the actionable alert-routing design, this statement describes alert target scopes. Actionable alert-routing design asks about stateful metric alerts; this alert target scopes choice leaves the stateful metric alerts explanation missing.
- **C — Incorrect.** An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation.
  An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation. In the actionable alert-routing design, this statement describes alert suppression rules. The alert suppression rules statement accurately describes alert suppression rules; however, actionable alert-routing design needs stateful metric alerts to keep an alert fired until the measured condition has resolved; alert suppression rules cannot replace stateful metric alerts.
- **D — Correct.** A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.
  The actionable alert-routing design needs stateful metric alerts to keep an alert fired until the measured condition has resolved; this option states the applicable stateful metric alerts rule: a stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q09 — D

**Question:** The alert routing architecture note requires the actionable alert-routing design environment to let the service learn a changing baseline instead of using one static threshold. Which statement defines the relevant alert routing boundary?

- **A — Incorrect.** Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself.
  Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself. In the actionable alert-routing design, this statement describes alert severity. Actionable alert-routing design asks about dynamic thresholds; this alert severity choice leaves the dynamic thresholds explanation missing.
- **B — Incorrect.** An action group defines reusable notification and automation receivers and must be linked to the alert rule to run.
  An action group defines reusable notification and automation receivers and must be linked to the alert rule to run. In the actionable alert-routing design, this statement describes action group association. The action group association statement accurately describes action group association; however, actionable alert-routing design needs dynamic thresholds to let the service learn a changing baseline instead of using one static threshold; action group association cannot replace dynamic thresholds.
- **C — Incorrect.** Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied.
  Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied. In the actionable alert-routing design, this statement describes scheduled alert processing. Selecting scheduled alert processing for actionable alert-routing design leaves dynamic thresholds unanswered in actionable alert-routing design; the actionable alert-routing design lacks a dynamic thresholds basis to let the service learn a changing baseline instead of using one static threshold.
- **D — Correct.** Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions.
  Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions. This dynamic thresholds fact resolves the actionable alert-routing design design question about how to let the service learn a changing baseline instead of using one static threshold.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Dynamic thresholds in Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-dynamic-thresholds)

**Source reviewed:** 2026-08-31

## LAB23-Q10 — D

**Question:** A new alert routing operator must explain why the actionable alert-routing design can encode operational urgency independently of whether a rule fires. Which explanation is accurate?

- **A — Incorrect.** A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes.
  A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes. In the actionable alert-routing design, this statement describes metric alert conditions. The metric alert conditions statement accurately describes metric alert conditions; however, actionable alert-routing design needs alert severity to encode operational urgency independently of whether a rule fires; metric alert conditions cannot replace alert severity.
- **B — Incorrect.** Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior.
  Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior. In the actionable alert-routing design, this statement describes action group receivers. Selecting action group receivers for actionable alert-routing design leaves alert severity unanswered in actionable alert-routing design; the actionable alert-routing design lacks a alert severity basis to encode operational urgency independently of whether a rule fires.
- **C — Incorrect.** An activity log alert matches subscription-level control-plane events by category and selected conditions.
  An activity log alert matches subscription-level control-plane events by category and selected conditions. In the actionable alert-routing design, this statement describes activity log alerts. Alert severity governs actionable alert-routing design; activity log alerts cannot support alert severity when operators must encode operational urgency independently of whether a rule fires.
- **D — Correct.** Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself.
  Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself. For actionable alert-routing design, alert severity supplies the service rule needed to encode operational urgency independently of whether a rule fires.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q11 — B

**Question:** An actionable alert-routing design review finds alert routing drift from the need to evaluate a numeric signal against a threshold over a defined window. Which correction addresses that drift?

- **A — Incorrect.** Create the action group and attach its resource ID to the alert rule actions.
  Create the action group and attach its resource ID to the alert rule actions. In the actionable alert-routing design, this action changes action group association. Actionable alert-routing design approved metric alert conditions, not action group association; only the metric alert conditions change can evaluate a numeric signal against a threshold over a defined window.
- **B — Correct.** Define the condition from the incident signal and use a window that avoids meaningless single-sample noise.
  Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. The actionable alert-routing design uses this metric alert conditions operation to evaluate a numeric signal against a threshold over a defined window within the approved scope.
- **C — Incorrect.** Define the maintenance recurrence and time zone explicitly and review its start and end boundaries.
  Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. In the actionable alert-routing design, this action changes scheduled alert processing. Scheduled alert processing does not implement metric alert conditions for actionable alert-routing design; the actionable alert-routing design still cannot evaluate a numeric signal against a threshold over a defined window.
- **D — Incorrect.** Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts.
  Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. In the actionable alert-routing design, this action changes dynamic thresholds. Actionable alert-routing design instead needs metric alert conditions: Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. The dynamic thresholds action omits that metric alert conditions work.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q12 — A

**Question:** The actionable alert-routing design window permits only the alert routing change needed to attach an alert rule to the resource that emits the monitored signal. Which option respects the boundary?

- **A — Correct.** Set scopes to the exact resources or common supported scope that must be monitored.
  For the actionable alert-routing design, the required alert target scopes action is: set scopes to the exact resources or common supported scope that must be monitored. It makes the environment able to attach an alert rule to the resource that emits the monitored signal.
- **B — Incorrect.** Configure only approved receiver types and validate each address without committing secrets.
  Configure only approved receiver types and validate each address without committing secrets. In the actionable alert-routing design, this action changes action group receivers. Action group receivers does not implement alert target scopes for actionable alert-routing design; the actionable alert-routing design still cannot attach an alert rule to the resource that emits the monitored signal.
- **C — Incorrect.** Create conditions for the required operation, status, resource type, or caller and attach an action group.
  Create conditions for the required operation, status, resource type, or caller and attach an action group. In the actionable alert-routing design, this action changes activity log alerts. Actionable alert-routing design instead needs alert target scopes: Set scopes to the exact resources or common supported scope that must be monitored. The activity log alerts action omits that alert target scopes work.
- **D — Incorrect.** Set severity from the organization's impact and response model and route actions accordingly.
  Set severity from the organization's impact and response model and route actions accordingly. In the actionable alert-routing design, this action changes alert severity. Actionable alert-routing design approved alert target scopes, not alert severity; only the alert target scopes change can attach an alert rule to the resource that emits the monitored signal.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q13 — D

**Question:** The alert routing preflight has passed; the actionable alert-routing design must now connect an alert rule to reusable notification and automation actions. Which operation should run?

- **A — Incorrect.** Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled.
  Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. In the actionable alert-routing design, this action changes alert suppression rules. Alert suppression rules does not implement action group association for actionable alert-routing design; the actionable alert-routing design still cannot connect an alert rule to reusable notification and automation actions.
- **B — Incorrect.** Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications.
  Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. In the actionable alert-routing design, this action changes stateful metric alerts. Actionable alert-routing design instead needs action group association: Create the action group and attach its resource ID to the alert rule actions. The stateful metric alerts action omits that action group association work.
- **C — Incorrect.** Define the condition from the incident signal and use a window that avoids meaningless single-sample noise.
  Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. In the actionable alert-routing design, this action changes metric alert conditions. Actionable alert-routing design approved action group association, not metric alert conditions; only the action group association change can connect an alert rule to reusable notification and automation actions.
- **D — Correct.** Create the action group and attach its resource ID to the alert rule actions.
  Create the action group and attach its resource ID to the alert rule actions. This changes action group association in the actionable alert-routing design, supplying the missing state needed to connect an alert rule to reusable notification and automation actions.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q14 — C

**Question:** The actionable alert-routing design plan must route a fired alert to the intended email, webhook, or automation endpoint while limiting the mutation scope to alert routing. Which action is appropriate?

- **A — Incorrect.** Define the maintenance recurrence and time zone explicitly and review its start and end boundaries.
  Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. In the actionable alert-routing design, this action changes scheduled alert processing. Actionable alert-routing design instead needs action group receivers: Configure only approved receiver types and validate each address without committing secrets. The scheduled alert processing action omits that action group receivers work.
- **B — Incorrect.** Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts.
  Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. In the actionable alert-routing design, this action changes dynamic thresholds. Actionable alert-routing design approved action group receivers, not dynamic thresholds; only the action group receivers change can route a fired alert to the intended email, webhook, or automation endpoint.
- **C — Correct.** Configure only approved receiver types and validate each address without committing secrets.
  The actionable alert-routing design must route a fired alert to the intended email, webhook, or automation endpoint; this option performs its direct action group receivers change: configure only approved receiver types and validate each address without committing secrets.
- **D — Incorrect.** Set scopes to the exact resources or common supported scope that must be monitored.
  Set scopes to the exact resources or common supported scope that must be monitored. In the actionable alert-routing design, this action changes alert target scopes. Alert target scopes does not implement action group receivers for actionable alert-routing design; the actionable alert-routing design still cannot route a fired alert to the intended email, webhook, or automation endpoint.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q15 — A

**Question:** An alert routing ticket in the actionable alert-routing design says to change delivery of matching notifications while leaving detection intact. Which alert routing action completes the actionable alert-routing design request with minimal change?

- **A — Correct.** Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled.
  Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. It is the least-change alert suppression rules path for the actionable alert-routing design requirement to change delivery of matching notifications while leaving detection intact.
- **B — Incorrect.** Create conditions for the required operation, status, resource type, or caller and attach an action group.
  Create conditions for the required operation, status, resource type, or caller and attach an action group. In the actionable alert-routing design, this action changes activity log alerts. Actionable alert-routing design requires alert suppression rules; changing activity log alerts leaves alert suppression rules absent in actionable alert-routing design; actionable alert-routing design cannot change delivery of matching notifications while leaving detection intact.
- **C — Incorrect.** Set severity from the organization's impact and response model and route actions accordingly.
  Set severity from the organization's impact and response model and route actions accordingly. In the actionable alert-routing design, this action changes alert severity. Alert severity does not implement alert suppression rules for actionable alert-routing design; the actionable alert-routing design still cannot change delivery of matching notifications while leaving detection intact.
- **D — Incorrect.** Create the action group and attach its resource ID to the alert rule actions.
  Create the action group and attach its resource ID to the alert rule actions. In the actionable alert-routing design, this action changes action group association. Actionable alert-routing design instead needs alert suppression rules: Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. The action group association action omits that alert suppression rules work.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q16 — A

**Question:** The approach for the actionable alert-routing design is approved, but the alert routing environment still cannot apply alert-routing behavior only during an approved maintenance window. Which implementation step closes the gap?

- **A — Correct.** Define the maintenance recurrence and time zone explicitly and review its start and end boundaries.
  Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. In actionable alert-routing design, applying scheduled alert processing is the scoped way to apply alert-routing behavior only during an approved maintenance window.
- **B — Incorrect.** Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications.
  Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. In the actionable alert-routing design, this action changes stateful metric alerts. Stateful metric alerts does not implement scheduled alert processing for actionable alert-routing design; the actionable alert-routing design still cannot apply alert-routing behavior only during an approved maintenance window.
- **C — Incorrect.** Define the condition from the incident signal and use a window that avoids meaningless single-sample noise.
  Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. In the actionable alert-routing design, this action changes metric alert conditions. Actionable alert-routing design instead needs scheduled alert processing: Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. The metric alert conditions action omits that scheduled alert processing work.
- **D — Incorrect.** Configure only approved receiver types and validate each address without committing secrets.
  Configure only approved receiver types and validate each address without committing secrets. In the actionable alert-routing design, this action changes action group receivers. Actionable alert-routing design approved scheduled alert processing, not action group receivers; only the scheduled alert processing change can apply alert-routing behavior only during an approved maintenance window.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q17 — B

**Question:** The monitoring administrator routing and suppressing actionable alerts may change the actionable alert-routing design only to trigger on a matching Activity Log record. Which alert routing action stays within that assignment?

- **A — Incorrect.** Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts.
  Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. In the actionable alert-routing design, this action changes dynamic thresholds. Dynamic thresholds does not implement activity log alerts for actionable alert-routing design; the actionable alert-routing design still cannot trigger on a matching Activity Log record.
- **B — Correct.** Create conditions for the required operation, status, resource type, or caller and attach an action group.
  Create conditions for the required operation, status, resource type, or caller and attach an action group. The actionable alert-routing design uses this activity log alerts operation to trigger on a matching Activity Log record within the approved scope.
- **C — Incorrect.** Set scopes to the exact resources or common supported scope that must be monitored.
  Set scopes to the exact resources or common supported scope that must be monitored. In the actionable alert-routing design, this action changes alert target scopes. Actionable alert-routing design approved activity log alerts, not alert target scopes; only the activity log alerts change can trigger on a matching Activity Log record.
- **D — Incorrect.** Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled.
  Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. In the actionable alert-routing design, this action changes alert suppression rules. Actionable alert-routing design requires activity log alerts; changing alert suppression rules leaves activity log alerts absent in actionable alert-routing design; actionable alert-routing design cannot trigger on a matching Activity Log record.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor activity log alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log)

**Source reviewed:** 2026-08-31

## LAB23-Q18 — D

**Question:** An alert routing dry run shows no actionable alert-routing design command will keep an alert fired until the measured condition has resolved. Which action belongs before execution?

- **A — Incorrect.** Set severity from the organization's impact and response model and route actions accordingly.
  Set severity from the organization's impact and response model and route actions accordingly. In the actionable alert-routing design, this action changes alert severity. Actionable alert-routing design instead needs stateful metric alerts: Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. The alert severity action omits that stateful metric alerts work.
- **B — Incorrect.** Create the action group and attach its resource ID to the alert rule actions.
  Create the action group and attach its resource ID to the alert rule actions. In the actionable alert-routing design, this action changes action group association. Actionable alert-routing design approved stateful metric alerts, not action group association; only the stateful metric alerts change can keep an alert fired until the measured condition has resolved.
- **C — Incorrect.** Define the maintenance recurrence and time zone explicitly and review its start and end boundaries.
  Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. In the actionable alert-routing design, this action changes scheduled alert processing. Actionable alert-routing design requires stateful metric alerts; changing scheduled alert processing leaves stateful metric alerts absent in actionable alert-routing design; actionable alert-routing design cannot keep an alert fired until the measured condition has resolved.
- **D — Correct.** Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications.
  For the actionable alert-routing design, the required stateful metric alerts action is: use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. It makes the environment able to keep an alert fired until the measured condition has resolved.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q19 — B

**Question:** For the actionable alert-routing design, operators need to let the service learn a changing baseline instead of using one static threshold. Which change realizes that requirement?

- **A — Incorrect.** Define the condition from the incident signal and use a window that avoids meaningless single-sample noise.
  Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. In the actionable alert-routing design, this action changes metric alert conditions. Actionable alert-routing design approved dynamic thresholds, not metric alert conditions; only the dynamic thresholds change can let the service learn a changing baseline instead of using one static threshold.
- **B — Correct.** Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts.
  Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. This changes dynamic thresholds in the actionable alert-routing design, supplying the missing state needed to let the service learn a changing baseline instead of using one static threshold.
- **C — Incorrect.** Configure only approved receiver types and validate each address without committing secrets.
  Configure only approved receiver types and validate each address without committing secrets. In the actionable alert-routing design, this action changes action group receivers. Action group receivers does not implement dynamic thresholds for actionable alert-routing design; the actionable alert-routing design still cannot let the service learn a changing baseline instead of using one static threshold.
- **D — Incorrect.** Create conditions for the required operation, status, resource type, or caller and attach an action group.
  Create conditions for the required operation, status, resource type, or caller and attach an action group. In the actionable alert-routing design, this action changes activity log alerts. Actionable alert-routing design instead needs dynamic thresholds: Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. The activity log alerts action omits that dynamic thresholds work.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Dynamic thresholds in Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-dynamic-thresholds)

**Source reviewed:** 2026-08-31

## LAB23-Q20 — C

**Question:** Operators must automate the actionable alert-routing design change needed to encode operational urgency independently of whether a rule fires. Which alert routing operation belongs in the runbook?

- **A — Incorrect.** Set scopes to the exact resources or common supported scope that must be monitored.
  Set scopes to the exact resources or common supported scope that must be monitored. In the actionable alert-routing design, this action changes alert target scopes. Actionable alert-routing design requires alert severity; changing alert target scopes leaves alert severity absent in actionable alert-routing design; actionable alert-routing design cannot encode operational urgency independently of whether a rule fires.
- **B — Incorrect.** Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled.
  Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. In the actionable alert-routing design, this action changes alert suppression rules. Alert suppression rules does not implement alert severity for actionable alert-routing design; the actionable alert-routing design still cannot encode operational urgency independently of whether a rule fires.
- **C — Correct.** Set severity from the organization's impact and response model and route actions accordingly.
  The actionable alert-routing design must encode operational urgency independently of whether a rule fires; this option performs its direct alert severity change: set severity from the organization's impact and response model and route actions accordingly.
- **D — Incorrect.** Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications.
  Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. In the actionable alert-routing design, this action changes stateful metric alerts. Actionable alert-routing design approved alert severity, not stateful metric alerts; only the alert severity change can encode operational urgency independently of whether a rule fires.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q21 — B

**Question:** The alert routing validation asks whether the actionable alert-routing design can evaluate a numeric signal against a threshold over a defined window. Which observable state is strongest?

- **A — Incorrect.** Query receiver collections and perform a controlled action-group test where supported.
  Query receiver collections and perform a controlled action-group test where supported. In the actionable alert-routing design, this check observes action group receivers. Actionable alert-routing design output covers action group receivers, not metric alert conditions; the metric alert conditions requirement to evaluate a numeric signal against a threshold over a defined window remains unverified.
- **B — Correct.** Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
  Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency. This is independent metric alert conditions evidence for the actionable alert-routing design, even if actionable alert-routing design setup reports success before metric alert conditions becomes observable.
- **C — Incorrect.** Query allOf conditions and generate a safe matching control-plane event.
  Query allOf conditions and generate a safe matching control-plane event. In the actionable alert-routing design, this check observes activity log alerts. Actionable alert-routing design reads activity log alerts, leaving metric alert conditions unproved in actionable alert-routing design; actionable alert-routing design still has no metric alert conditions proof.
- **D — Incorrect.** Query severity, enabled state, description, and action groups on the rule.
  Query severity, enabled state, description, and action groups on the rule. In the actionable alert-routing design, this check observes alert severity. Actionable alert-routing design could pass alert severity while metric alert conditions is wrong; actionable alert-routing design still lacks metric alert conditions proof.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q22 — B

**Question:** An actionable alert-routing design review must prove the alert routing ability to attach an alert rule to the resource that emits the monitored signal. Which check avoids an adjacent feature?

- **A — Incorrect.** Query processing-rule scopes, filters, action type, enabled state, and schedule.
  Query processing-rule scopes, filters, action type, enabled state, and schedule. In the actionable alert-routing design, this check observes alert suppression rules. Alert suppression rules success in actionable alert-routing design cannot verify alert target scopes; actionable alert-routing design cannot attach an alert rule to the resource that emits the monitored signal until alert target scopes evidence exists.
- **B — Correct.** Query scopes and confirm each intended resource ID is represented.
  Query scopes and confirm each intended resource ID is represented. For actionable alert-routing design, this alert target scopes read confirms the service can attach an alert rule to the resource that emits the monitored signal.
- **C — Incorrect.** Inspect fired and resolved timestamps and correlate them with the metric series.
  Inspect fired and resolved timestamps and correlate them with the metric series. In the actionable alert-routing design, this check observes stateful metric alerts. Actionable alert-routing design could pass stateful metric alerts while alert target scopes is wrong; actionable alert-routing design still lacks alert target scopes proof.
- **D — Incorrect.** Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
  Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency. In the actionable alert-routing design, this check observes metric alert conditions. Actionable alert-routing design output covers metric alert conditions, not alert target scopes; the alert target scopes requirement to attach an alert rule to the resource that emits the monitored signal remains unverified.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q23 — D

**Question:** The actionable alert-routing design evidence bundle needs an alert routing result showing it can connect an alert rule to reusable notification and automation actions. Which result belongs in the checkpoint?

- **A — Incorrect.** Query schedule recurrence, timeZone, startDateTime, and endDateTime.
  Query schedule recurrence, timeZone, startDateTime, and endDateTime. In the actionable alert-routing design, this check observes scheduled alert processing. Actionable alert-routing design reads scheduled alert processing, leaving action group association unproved in actionable alert-routing design; actionable alert-routing design still has no action group association proof.
- **B — Incorrect.** Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
  Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore. In the actionable alert-routing design, this check observes dynamic thresholds. Actionable alert-routing design could pass dynamic thresholds while action group association is wrong; actionable alert-routing design still lacks action group association proof.
- **C — Incorrect.** Query scopes and confirm each intended resource ID is represented.
  Query scopes and confirm each intended resource ID is represented. In the actionable alert-routing design, this check observes alert target scopes. Actionable alert-routing design output covers alert target scopes, not action group association; the action group association requirement to connect an alert rule to reusable notification and automation actions remains unverified.
- **D — Correct.** Query the alert rule actions and resolve each referenced action group.
  Query the alert rule actions and resolve each referenced action group. The actionable alert-routing design reads action group association directly; that action group association result proves the actionable alert-routing design can connect an alert rule to reusable notification and automation actions without another mutation.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q24 — A

**Question:** Before actionable alert-routing design cleanup, the alert routing team must reconfirm it can route a fired alert to the intended email, webhook, or automation endpoint. Which read-only inspection should run?

- **A — Correct.** Query receiver collections and perform a controlled action-group test where supported.
  For the actionable alert-routing design, this action group receivers observation is decisive: query receiver collections and perform a controlled action-group test where supported. It is actionable alert-routing design evidence that operators can route a fired alert to the intended email, webhook, or automation endpoint.
- **B — Incorrect.** Query allOf conditions and generate a safe matching control-plane event.
  Query allOf conditions and generate a safe matching control-plane event. In the actionable alert-routing design, this check observes activity log alerts. Actionable alert-routing design output covers activity log alerts, not action group receivers; the action group receivers requirement to route a fired alert to the intended email, webhook, or automation endpoint remains unverified.
- **C — Incorrect.** Query severity, enabled state, description, and action groups on the rule.
  Query severity, enabled state, description, and action groups on the rule. In the actionable alert-routing design, this check observes alert severity. Alert severity success in actionable alert-routing design cannot verify action group receivers; actionable alert-routing design cannot route a fired alert to the intended email, webhook, or automation endpoint until action group receivers evidence exists.
- **D — Incorrect.** Query the alert rule actions and resolve each referenced action group.
  Query the alert rule actions and resolve each referenced action group. In the actionable alert-routing design, this check observes action group association. Actionable alert-routing design reads action group association, leaving action group receivers unproved in actionable alert-routing design; actionable alert-routing design still has no action group receivers proof.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q25 — B

**Question:** The actionable alert-routing design setup reports success after the alert routing attempt to change delivery of matching notifications while leaving detection intact. Which alert routing read-only observation proves the actionable alert-routing design outcome?

- **A — Incorrect.** Inspect fired and resolved timestamps and correlate them with the metric series.
  Inspect fired and resolved timestamps and correlate them with the metric series. In the actionable alert-routing design, this check observes stateful metric alerts. Actionable alert-routing design output covers stateful metric alerts, not alert suppression rules; the alert suppression rules requirement to change delivery of matching notifications while leaving detection intact remains unverified.
- **B — Correct.** Query processing-rule scopes, filters, action type, enabled state, and schedule.
  Query processing-rule scopes, filters, action type, enabled state, and schedule. Because the actionable alert-routing design check observes alert suppression rules, it independently verifies the requirement to change delivery of matching notifications while leaving detection intact.
- **C — Incorrect.** Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
  Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency. In the actionable alert-routing design, this check observes metric alert conditions. Actionable alert-routing design reads metric alert conditions, leaving alert suppression rules unproved in actionable alert-routing design; actionable alert-routing design still has no alert suppression rules proof.
- **D — Incorrect.** Query receiver collections and perform a controlled action-group test where supported.
  Query receiver collections and perform a controlled action-group test where supported. In the actionable alert-routing design, this check observes action group receivers. Actionable alert-routing design could pass action group receivers while alert suppression rules is wrong; actionable alert-routing design still lacks alert suppression rules proof.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q26 — C

**Question:** The alert routing log says the actionable alert-routing design can now apply alert-routing behavior only during an approved maintenance window. Which alert routing state should the actionable alert-routing design acceptance test retain?

- **A — Incorrect.** Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
  Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore. In the actionable alert-routing design, this check observes dynamic thresholds. Dynamic thresholds success in actionable alert-routing design cannot verify scheduled alert processing; actionable alert-routing design cannot apply alert-routing behavior only during an approved maintenance window until scheduled alert processing evidence exists.
- **B — Incorrect.** Query scopes and confirm each intended resource ID is represented.
  Query scopes and confirm each intended resource ID is represented. In the actionable alert-routing design, this check observes alert target scopes. Actionable alert-routing design reads alert target scopes, leaving scheduled alert processing unproved in actionable alert-routing design; actionable alert-routing design still has no scheduled alert processing proof.
- **C — Correct.** Query schedule recurrence, timeZone, startDateTime, and endDateTime.
  The actionable alert-routing design validator needs this scheduled alert processing result: query schedule recurrence, timeZone, startDateTime, and endDateTime. It proves the outcome to apply alert-routing behavior only during an approved maintenance window rather than an adjacent checkpoint.
- **D — Incorrect.** Query processing-rule scopes, filters, action type, enabled state, and schedule.
  Query processing-rule scopes, filters, action type, enabled state, and schedule. In the actionable alert-routing design, this check observes alert suppression rules. Actionable alert-routing design output covers alert suppression rules, not scheduled alert processing; the scheduled alert processing requirement to apply alert-routing behavior only during an approved maintenance window remains unverified.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q27 — D

**Question:** The actionable alert-routing design rejects alert routing exit status as proof it can trigger on a matching Activity Log record. Which actionable alert-routing design result is valid evidence?

- **A — Incorrect.** Query severity, enabled state, description, and action groups on the rule.
  Query severity, enabled state, description, and action groups on the rule. In the actionable alert-routing design, this check observes alert severity. Actionable alert-routing design reads alert severity, leaving activity log alerts unproved in actionable alert-routing design; actionable alert-routing design still has no activity log alerts proof.
- **B — Incorrect.** Query the alert rule actions and resolve each referenced action group.
  Query the alert rule actions and resolve each referenced action group. In the actionable alert-routing design, this check observes action group association. Actionable alert-routing design could pass action group association while activity log alerts is wrong; actionable alert-routing design still lacks activity log alerts proof.
- **C — Incorrect.** Query schedule recurrence, timeZone, startDateTime, and endDateTime.
  Query schedule recurrence, timeZone, startDateTime, and endDateTime. In the actionable alert-routing design, this check observes scheduled alert processing. Actionable alert-routing design output covers scheduled alert processing, not activity log alerts; the activity log alerts requirement to trigger on a matching Activity Log record remains unverified.
- **D — Correct.** Query allOf conditions and generate a safe matching control-plane event.
  Query allOf conditions and generate a safe matching control-plane event. This is independent activity log alerts evidence for the actionable alert-routing design, even if actionable alert-routing design setup reports success before activity log alerts becomes observable.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor activity log alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log)

**Source reviewed:** 2026-08-31

## LAB23-Q28 — A

**Question:** The alert routing validator needs one actionable alert-routing design query after the change to keep an alert fired until the measured condition has resolved. Which alert routing property should the actionable alert-routing design validator inspect?

- **A — Correct.** Inspect fired and resolved timestamps and correlate them with the metric series.
  Inspect fired and resolved timestamps and correlate them with the metric series. For actionable alert-routing design, this stateful metric alerts read confirms the service can keep an alert fired until the measured condition has resolved.
- **B — Incorrect.** Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
  Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency. In the actionable alert-routing design, this check observes metric alert conditions. Actionable alert-routing design output covers metric alert conditions, not stateful metric alerts; the stateful metric alerts requirement to keep an alert fired until the measured condition has resolved remains unverified.
- **C — Incorrect.** Query receiver collections and perform a controlled action-group test where supported.
  Query receiver collections and perform a controlled action-group test where supported. In the actionable alert-routing design, this check observes action group receivers. Action group receivers success in actionable alert-routing design cannot verify stateful metric alerts; actionable alert-routing design cannot keep an alert fired until the measured condition has resolved until stateful metric alerts evidence exists.
- **D — Incorrect.** Query allOf conditions and generate a safe matching control-plane event.
  Query allOf conditions and generate a safe matching control-plane event. In the actionable alert-routing design, this check observes activity log alerts. Actionable alert-routing design reads activity log alerts, leaving stateful metric alerts unproved in actionable alert-routing design; actionable alert-routing design still has no stateful metric alerts proof.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q29 — B

**Question:** The monitoring administrator routing and suppressing actionable alerts must confirm the actionable alert-routing design, without mutation, can let the service learn a changing baseline instead of using one static threshold. Which alert routing check qualifies?

- **A — Incorrect.** Query scopes and confirm each intended resource ID is represented.
  Query scopes and confirm each intended resource ID is represented. In the actionable alert-routing design, this check observes alert target scopes. Actionable alert-routing design output covers alert target scopes, not dynamic thresholds; the dynamic thresholds requirement to let the service learn a changing baseline instead of using one static threshold remains unverified.
- **B — Correct.** Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
  Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore. The actionable alert-routing design reads dynamic thresholds directly; that dynamic thresholds result proves the actionable alert-routing design can let the service learn a changing baseline instead of using one static threshold without another mutation.
- **C — Incorrect.** Query processing-rule scopes, filters, action type, enabled state, and schedule.
  Query processing-rule scopes, filters, action type, enabled state, and schedule. In the actionable alert-routing design, this check observes alert suppression rules. Actionable alert-routing design reads alert suppression rules, leaving dynamic thresholds unproved in actionable alert-routing design; actionable alert-routing design still has no dynamic thresholds proof.
- **D — Incorrect.** Inspect fired and resolved timestamps and correlate them with the metric series.
  Inspect fired and resolved timestamps and correlate them with the metric series. In the actionable alert-routing design, this check observes stateful metric alerts. Actionable alert-routing design could pass stateful metric alerts while dynamic thresholds is wrong; actionable alert-routing design still lacks dynamic thresholds proof.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Dynamic thresholds in Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-dynamic-thresholds)

**Source reviewed:** 2026-08-31

## LAB23-Q30 — B

**Question:** The actionable alert-routing design configuration is complete; the alert routing reviewers need evidence it can encode operational urgency independently of whether a rule fires. Which observation shows success?

- **A — Incorrect.** Query the alert rule actions and resolve each referenced action group.
  Query the alert rule actions and resolve each referenced action group. In the actionable alert-routing design, this check observes action group association. Action group association success in actionable alert-routing design cannot verify alert severity; actionable alert-routing design cannot encode operational urgency independently of whether a rule fires until alert severity evidence exists.
- **B — Correct.** Query severity, enabled state, description, and action groups on the rule.
  For the actionable alert-routing design, this alert severity observation is decisive: query severity, enabled state, description, and action groups on the rule. It is actionable alert-routing design evidence that operators can encode operational urgency independently of whether a rule fires.
- **C — Incorrect.** Query schedule recurrence, timeZone, startDateTime, and endDateTime.
  Query schedule recurrence, timeZone, startDateTime, and endDateTime. In the actionable alert-routing design, this check observes scheduled alert processing. Actionable alert-routing design could pass scheduled alert processing while alert severity is wrong; actionable alert-routing design still lacks alert severity proof.
- **D — Incorrect.** Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
  Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore. In the actionable alert-routing design, this check observes dynamic thresholds. Actionable alert-routing design output covers dynamic thresholds, not alert severity; the alert severity requirement to encode operational urgency independently of whether a rule fires remains unverified.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q31 — C

**Question:** Although the actionable alert-routing design is meant to let the alert routing evaluate a numeric signal against a threshold over a defined window, its checkpoint fails. Which alert routing defect explains the failure?

- **A — Incorrect.** The rule was created in the correct resource group but its scopes point to a different resource.
  The rule was created in the correct resource group but its scopes point to a different resource. The actionable alert-routing design fault concerns alert target scopes. Actionable alert-routing design has alert target scopes impact, but metric alert conditions is the actionable alert-routing design failed path; the alert target scopes state cannot produce metric alert conditions failure.
- **B — Incorrect.** The schedule was authored in UTC while the maintenance window was interpreted as local time.
  The schedule was authored in UTC while the maintenance window was interpreted as local time. The actionable alert-routing design fault concerns scheduled alert processing. Actionable alert-routing design could repair scheduled alert processing while metric alert conditions stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to evaluate a numeric signal against a threshold over a defined window.
- **C — Correct.** The rule uses Average when the requirement is to catch any maximum value above the limit.
  The rule uses Average when the requirement is to catch any maximum value above the limit. The finding is specific to metric alert conditions in the actionable alert-routing design; repairing metric alert conditions restores the actionable alert-routing design ability to evaluate a numeric signal against a threshold over a defined window.
- **D — Incorrect.** The rule's severity conflicts with the incident-routing policy used by its action group.
  The rule's severity conflicts with the incident-routing policy used by its action group. The actionable alert-routing design fault concerns alert severity. Actionable alert-routing design may fix alert severity, yet metric alert conditions still fails; this actionable alert-routing design diagnosis of alert severity is wrong for metric alert conditions.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q32 — D

**Question:** The alert routing support team isolated the actionable alert-routing design incident to the attempt to attach an alert rule to the resource that emits the monitored signal. Which condition prevents success?

- **A — Incorrect.** The action group exists but is not referenced by the enabled alert rule.
  The action group exists but is not referenced by the enabled alert rule. The actionable alert-routing design fault concerns action group association. Actionable alert-routing design could repair action group association while alert target scopes stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to attach an alert rule to the resource that emits the monitored signal.
- **B — Incorrect.** The condition filters on a data-plane operation that does not appear in the Azure Activity Log.
  The condition filters on a data-plane operation that does not appear in the Azure Activity Log. The actionable alert-routing design fault concerns activity log alerts. Actionable alert-routing design failed on alert target scopes; this activity log alerts finding redirects actionable alert-routing design remediation away from alert target scopes.
- **C — Incorrect.** The rule uses Average when the requirement is to catch any maximum value above the limit.
  The rule uses Average when the requirement is to catch any maximum value above the limit. The actionable alert-routing design fault concerns metric alert conditions. Actionable alert-routing design may fix metric alert conditions, yet alert target scopes still fails; this actionable alert-routing design diagnosis of metric alert conditions is wrong for alert target scopes.
- **D — Correct.** The rule was created in the correct resource group but its scopes point to a different resource.
  The actionable alert-routing design cannot attach an alert rule to the resource that emits the monitored signal because of this alert target scopes defect: the rule was created in the correct resource group but its scopes point to a different resource. The symptom and repair align.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q33 — B

**Question:** An actionable alert-routing design query surprises the monitoring administrator routing and suppressing actionable alerts during the alert routing attempt to connect an alert rule to reusable notification and automation actions. Which finding explains it?

- **A — Incorrect.** The email receiver address contains a typographical error.
  The email receiver address contains a typographical error. The actionable alert-routing design fault concerns action group receivers. Actionable alert-routing design failed on action group association; this action group receivers finding redirects actionable alert-routing design remediation away from action group association.
- **B — Correct.** The action group exists but is not referenced by the enabled alert rule.
  The action group exists but is not referenced by the enabled alert rule. Removing this action group association condition lets the actionable alert-routing design connect an alert rule to reusable notification and automation actions while leaving healthy controls unchanged.
- **C — Incorrect.** The team expects a new notification at every evaluation while using a stateful alert.
  The team expects a new notification at every evaluation while using a stateful alert. The actionable alert-routing design fault concerns stateful metric alerts. Actionable alert-routing design has stateful metric alerts impact, but action group association is the actionable alert-routing design failed path; the stateful metric alerts state cannot produce action group association failure.
- **D — Incorrect.** The rule was created in the correct resource group but its scopes point to a different resource.
  The rule was created in the correct resource group but its scopes point to a different resource. The actionable alert-routing design fault concerns alert target scopes. Actionable alert-routing design could repair alert target scopes while action group association stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to connect an alert rule to reusable notification and automation actions.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q34 — C

**Question:** Other actionable alert-routing design components are healthy, but the alert routing still cannot route a fired alert to the intended email, webhook, or automation endpoint. Which state causes the isolated failure?

- **A — Incorrect.** The alert rule itself was disabled, eliminating evaluation evidence during maintenance.
  The alert rule itself was disabled, eliminating evaluation evidence during maintenance. The actionable alert-routing design fault concerns alert suppression rules. Actionable alert-routing design may fix alert suppression rules, yet action group receivers still fails; this actionable alert-routing design diagnosis of alert suppression rules is wrong for action group receivers.
- **B — Incorrect.** The resource has too little historical metric data for the dynamic baseline.
  The resource has too little historical metric data for the dynamic baseline. The actionable alert-routing design fault concerns dynamic thresholds. Actionable alert-routing design has dynamic thresholds impact, but action group receivers is the actionable alert-routing design failed path; the dynamic thresholds state cannot produce action group receivers failure.
- **C — Correct.** The email receiver address contains a typographical error.
  The email receiver address contains a typographical error. In actionable alert-routing design, this action group receivers cause matches the failure to route a fired alert to the intended email, webhook, or automation endpoint.
- **D — Incorrect.** The action group exists but is not referenced by the enabled alert rule.
  The action group exists but is not referenced by the enabled alert rule. The actionable alert-routing design fault concerns action group association. Actionable alert-routing design failed on action group receivers; this action group association finding redirects actionable alert-routing design remediation away from action group receivers.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q35 — C

**Question:** During an alert routing fault drill, the actionable alert-routing design does not change delivery of matching notifications while leaving detection intact. Which finding identifies the defect?

- **A — Incorrect.** The schedule was authored in UTC while the maintenance window was interpreted as local time.
  The schedule was authored in UTC while the maintenance window was interpreted as local time. The actionable alert-routing design fault concerns scheduled alert processing. Actionable alert-routing design has scheduled alert processing impact, but alert suppression rules is the actionable alert-routing design failed path; the scheduled alert processing state cannot produce alert suppression rules failure.
- **B — Incorrect.** The rule's severity conflicts with the incident-routing policy used by its action group.
  The rule's severity conflicts with the incident-routing policy used by its action group. The actionable alert-routing design fault concerns alert severity. Actionable alert-routing design could repair alert severity while alert suppression rules stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to change delivery of matching notifications while leaving detection intact.
- **C — Correct.** The alert rule itself was disabled, eliminating evaluation evidence during maintenance.
  The alert rule itself was disabled, eliminating evaluation evidence during maintenance. This actionable alert-routing design condition breaks alert suppression rules, explaining why operators cannot change delivery of matching notifications while leaving detection intact.
- **D — Incorrect.** The email receiver address contains a typographical error.
  The email receiver address contains a typographical error. The actionable alert-routing design fault concerns action group receivers. Actionable alert-routing design may fix action group receivers, yet alert suppression rules still fails; this actionable alert-routing design diagnosis of action group receivers is wrong for alert suppression rules.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q36 — D

**Question:** The actionable alert-routing design setup finishes, yet the alert routing cannot apply alert-routing behavior only during an approved maintenance window. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The condition filters on a data-plane operation that does not appear in the Azure Activity Log.
  The condition filters on a data-plane operation that does not appear in the Azure Activity Log. The actionable alert-routing design fault concerns activity log alerts. Actionable alert-routing design could repair activity log alerts while scheduled alert processing stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to apply alert-routing behavior only during an approved maintenance window.
- **B — Incorrect.** The rule uses Average when the requirement is to catch any maximum value above the limit.
  The rule uses Average when the requirement is to catch any maximum value above the limit. The actionable alert-routing design fault concerns metric alert conditions. Actionable alert-routing design failed on scheduled alert processing; this metric alert conditions finding redirects actionable alert-routing design remediation away from scheduled alert processing.
- **C — Incorrect.** The alert rule itself was disabled, eliminating evaluation evidence during maintenance.
  The alert rule itself was disabled, eliminating evaluation evidence during maintenance. The actionable alert-routing design fault concerns alert suppression rules. Actionable alert-routing design may fix alert suppression rules, yet scheduled alert processing still fails; this actionable alert-routing design diagnosis of alert suppression rules is wrong for scheduled alert processing.
- **D — Correct.** The schedule was authored in UTC while the maintenance window was interpreted as local time.
  For the actionable alert-routing design, the scheduled alert processing failure is causal: the schedule was authored in UTC while the maintenance window was interpreted as local time. Correcting it restores the ability to apply alert-routing behavior only during an approved maintenance window.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q37 — C

**Question:** An alert routing break/fix in the actionable alert-routing design fails when operators try to trigger on a matching Activity Log record. Which diagnosis fits?

- **A — Incorrect.** The team expects a new notification at every evaluation while using a stateful alert.
  The team expects a new notification at every evaluation while using a stateful alert. The actionable alert-routing design fault concerns stateful metric alerts. Actionable alert-routing design failed on activity log alerts; this stateful metric alerts finding redirects actionable alert-routing design remediation away from activity log alerts.
- **B — Incorrect.** The rule was created in the correct resource group but its scopes point to a different resource.
  The rule was created in the correct resource group but its scopes point to a different resource. The actionable alert-routing design fault concerns alert target scopes. Actionable alert-routing design may fix alert target scopes, yet activity log alerts still fails; this actionable alert-routing design diagnosis of alert target scopes is wrong for activity log alerts.
- **C — Correct.** The condition filters on a data-plane operation that does not appear in the Azure Activity Log.
  The condition filters on a data-plane operation that does not appear in the Azure Activity Log. The finding is specific to activity log alerts in the actionable alert-routing design; repairing activity log alerts restores the actionable alert-routing design ability to trigger on a matching Activity Log record.
- **D — Incorrect.** The schedule was authored in UTC while the maintenance window was interpreted as local time.
  The schedule was authored in UTC while the maintenance window was interpreted as local time. The actionable alert-routing design fault concerns scheduled alert processing. Actionable alert-routing design could repair scheduled alert processing while activity log alerts stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to trigger on a matching Activity Log record.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor activity log alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log)

**Source reviewed:** 2026-08-31

## LAB23-Q38 — A

**Question:** The actionable alert-routing design troubleshooting scope is the alert routing need to keep an alert fired until the measured condition has resolved. Which condition should be corrected first?

- **A — Correct.** The team expects a new notification at every evaluation while using a stateful alert.
  The actionable alert-routing design cannot keep an alert fired until the measured condition has resolved because of this stateful metric alerts defect: the team expects a new notification at every evaluation while using a stateful alert. The symptom and repair align.
- **B — Incorrect.** The resource has too little historical metric data for the dynamic baseline.
  The resource has too little historical metric data for the dynamic baseline. The actionable alert-routing design fault concerns dynamic thresholds. Actionable alert-routing design has dynamic thresholds impact, but stateful metric alerts is the actionable alert-routing design failed path; the dynamic thresholds state cannot produce stateful metric alerts failure.
- **C — Incorrect.** The action group exists but is not referenced by the enabled alert rule.
  The action group exists but is not referenced by the enabled alert rule. The actionable alert-routing design fault concerns action group association. Actionable alert-routing design could repair action group association while stateful metric alerts stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to keep an alert fired until the measured condition has resolved.
- **D — Incorrect.** The condition filters on a data-plane operation that does not appear in the Azure Activity Log.
  The condition filters on a data-plane operation that does not appear in the Azure Activity Log. The actionable alert-routing design fault concerns activity log alerts. Actionable alert-routing design failed on stateful metric alerts; this activity log alerts finding redirects actionable alert-routing design remediation away from stateful metric alerts.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q39 — D

**Question:** The actionable alert-routing design result is partial because the alert routing cannot let the service learn a changing baseline instead of using one static threshold. Which condition accounts for that result?

- **A — Incorrect.** The rule's severity conflicts with the incident-routing policy used by its action group.
  The rule's severity conflicts with the incident-routing policy used by its action group. The actionable alert-routing design fault concerns alert severity. Actionable alert-routing design has alert severity impact, but dynamic thresholds is the actionable alert-routing design failed path; the alert severity state cannot produce dynamic thresholds failure.
- **B — Incorrect.** The email receiver address contains a typographical error.
  The email receiver address contains a typographical error. The actionable alert-routing design fault concerns action group receivers. Actionable alert-routing design could repair action group receivers while dynamic thresholds stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to let the service learn a changing baseline instead of using one static threshold.
- **C — Incorrect.** The team expects a new notification at every evaluation while using a stateful alert.
  The team expects a new notification at every evaluation while using a stateful alert. The actionable alert-routing design fault concerns stateful metric alerts. Actionable alert-routing design failed on dynamic thresholds; this stateful metric alerts finding redirects actionable alert-routing design remediation away from dynamic thresholds.
- **D — Correct.** The resource has too little historical metric data for the dynamic baseline.
  The resource has too little historical metric data for the dynamic baseline. Removing this dynamic thresholds condition lets the actionable alert-routing design let the service learn a changing baseline instead of using one static threshold while leaving healthy controls unchanged.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Dynamic thresholds in Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-dynamic-thresholds)

**Source reviewed:** 2026-08-31

## LAB23-Q40 — B

**Question:** The alert routing evidence shows the actionable alert-routing design cannot encode operational urgency independently of whether a rule fires. Which root cause fits that evidence?

- **A — Incorrect.** The rule uses Average when the requirement is to catch any maximum value above the limit.
  The rule uses Average when the requirement is to catch any maximum value above the limit. The actionable alert-routing design fault concerns metric alert conditions. Actionable alert-routing design could repair metric alert conditions while alert severity stays broken in actionable alert-routing design; the actionable alert-routing design remains unable to encode operational urgency independently of whether a rule fires.
- **B — Correct.** The rule's severity conflicts with the incident-routing policy used by its action group.
  The rule's severity conflicts with the incident-routing policy used by its action group. In actionable alert-routing design, this alert severity cause matches the failure to encode operational urgency independently of whether a rule fires.
- **C — Incorrect.** The alert rule itself was disabled, eliminating evaluation evidence during maintenance.
  The alert rule itself was disabled, eliminating evaluation evidence during maintenance. The actionable alert-routing design fault concerns alert suppression rules. Actionable alert-routing design may fix alert suppression rules, yet alert severity still fails; this actionable alert-routing design diagnosis of alert suppression rules is wrong for alert severity.
- **D — Incorrect.** The resource has too little historical metric data for the dynamic baseline.
  The resource has too little historical metric data for the dynamic baseline. The actionable alert-routing design fault concerns dynamic thresholds. Actionable alert-routing design has dynamic thresholds impact, but alert severity is the actionable alert-routing design failed path; the dynamic thresholds state cannot produce alert severity failure.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q41 — C

**Question:** The actionable alert-routing design forbids a partial alert routing result. Operators must first evaluate a numeric signal against a threshold over a defined window and afterward confirm the actionable alert-routing design outcome. Which alert routing sequence is complete?

- **A — Incorrect.** First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.
  First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group. This actionable alert-routing design pair serves action group association. Action group association cannot replace metric alert conditions in actionable alert-routing design. Use this metric alert conditions pair instead: First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
- **B — Incorrect.** First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.
  First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event. This actionable alert-routing design pair serves activity log alerts. Actionable alert-routing design proves activity log alerts, but metric alert conditions lacks implementation in actionable alert-routing design and metric alert conditions proof; the metric alert conditions outcome to evaluate a numeric signal against a threshold over a defined window remains open.
- **C — Correct.** First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
  First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency. In the actionable alert-routing design, the first metric alert conditions step runs; the actionable alert-routing design then reads metric alert conditions state to prove it can evaluate a numeric signal against a threshold over a defined window.
- **D — Incorrect.** First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.
  First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series. This actionable alert-routing design pair serves stateful metric alerts. Actionable alert-routing design closes stateful metric alerts, not metric alert conditions; without the metric alert conditions workflow, it cannot evaluate a numeric signal against a threshold over a defined window.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q42 — D

**Question:** Only the actionable alert-routing design change needed to attach an alert rule to the resource that emits the monitored signal is allowed, and alert routing proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.
  First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported. This actionable alert-routing design pair serves action group receivers. Actionable alert-routing design proves action group receivers, but alert target scopes lacks implementation in actionable alert-routing design and alert target scopes proof; the alert target scopes outcome to attach an alert rule to the resource that emits the monitored signal remains open.
- **B — Incorrect.** First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.
  First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series. This actionable alert-routing design pair serves stateful metric alerts. Actionable alert-routing design uses stateful metric alerts for both steps; alert target scopes remains untouched in actionable alert-routing design, so its alert target scopes gate to attach an alert rule to the resource that emits the monitored signal fails.
- **C — Incorrect.** First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
  First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore. This actionable alert-routing design pair serves dynamic thresholds. Actionable alert-routing design closes dynamic thresholds, not alert target scopes; without the alert target scopes workflow, it cannot attach an alert rule to the resource that emits the monitored signal.
- **D — Correct.** First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented.
  For the actionable alert-routing design, the safe alert target scopes order is: first, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented. The actionable alert-routing design records alert target scopes proof after configuration.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q43 — A

**Question:** The actionable alert-routing design runbook separates alert routing mutation from validation while it must connect an alert rule to reusable notification and automation actions. Which sequence proves it cleanly?

- **A — Correct.** First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.
  First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group. The actionable alert-routing design uses its action group association mutation gate and action group association verification gate before it can connect an alert rule to reusable notification and automation actions.
- **B — Incorrect.** First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule.
  First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule. This actionable alert-routing design pair serves alert suppression rules. Actionable alert-routing design closes alert suppression rules, not action group association; without the action group association workflow, it cannot connect an alert rule to reusable notification and automation actions.
- **C — Incorrect.** First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
  First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore. This actionable alert-routing design pair serves dynamic thresholds. Dynamic thresholds cannot replace action group association in actionable alert-routing design. Use this action group association pair instead: First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.
- **D — Incorrect.** First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.
  First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule. This actionable alert-routing design pair serves alert severity. Actionable alert-routing design proves alert severity, but action group association lacks implementation in actionable alert-routing design and action group association proof; the action group association outcome to connect an alert rule to reusable notification and automation actions remains open.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q44 — D

**Question:** The actionable alert-routing design checkpoint requires both this alert routing outcome—route a fired alert to the intended email, webhook, or automation endpoint—and a read-only actionable alert-routing design state check. Which alert routing response is complete?

- **A — Incorrect.** First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.
  First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime. This actionable alert-routing design pair serves scheduled alert processing. Actionable alert-routing design closes scheduled alert processing, not action group receivers; without the action group receivers workflow, it cannot route a fired alert to the intended email, webhook, or automation endpoint.
- **B — Incorrect.** First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.
  First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule. This actionable alert-routing design pair serves alert severity. Alert severity cannot replace action group receivers in actionable alert-routing design. Use this action group receivers pair instead: First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.
- **C — Incorrect.** First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
  First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency. This actionable alert-routing design pair serves metric alert conditions. Actionable alert-routing design proves metric alert conditions, but action group receivers lacks implementation in actionable alert-routing design and action group receivers proof; the action group receivers outcome to route a fired alert to the intended email, webhook, or automation endpoint remains open.
- **D — Correct.** First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.
  The actionable alert-routing design gets a complete action group receivers sequence here: first, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported. Read-back evidence follows the change.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Azure Monitor action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

**Source reviewed:** 2026-08-31

## LAB23-Q45 — A

**Question:** The actionable alert-routing design runbook must change delivery of matching notifications while leaving detection intact, then retain alert routing read-back evidence. Which actionable alert-routing design pair completes both duties?

- **A — Correct.** First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule.
  First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule. This ordered alert suppression rules workflow lets the actionable alert-routing design change delivery of matching notifications while leaving detection intact and then verify the resulting state.
- **B — Incorrect.** First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.
  First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event. This actionable alert-routing design pair serves activity log alerts. Actionable alert-routing design proves activity log alerts, but alert suppression rules lacks implementation in actionable alert-routing design and alert suppression rules proof; the alert suppression rules outcome to change delivery of matching notifications while leaving detection intact remains open.
- **C — Incorrect.** First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
  First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency. This actionable alert-routing design pair serves metric alert conditions. Actionable alert-routing design uses metric alert conditions for both steps; alert suppression rules remains untouched in actionable alert-routing design, so its alert suppression rules gate to change delivery of matching notifications while leaving detection intact fails.
- **D — Incorrect.** First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented.
  First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented. This actionable alert-routing design pair serves alert target scopes. Actionable alert-routing design closes alert target scopes, not alert suppression rules; without the alert suppression rules workflow, it cannot change delivery of matching notifications while leaving detection intact.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q46 — A

**Question:** To satisfy the alert routing requirement, operators must change the actionable alert-routing design configuration and prove it can apply alert-routing behavior only during an approved maintenance window. Which sequence is coherent?

- **A — Correct.** First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.
  First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime. For actionable alert-routing design, the scheduled alert processing operation precedes its scheduled alert processing read-back check, allowing it to apply alert-routing behavior only during an approved maintenance window.
- **B — Incorrect.** First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.
  First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series. This actionable alert-routing design pair serves stateful metric alerts. Actionable alert-routing design uses stateful metric alerts for both steps; scheduled alert processing remains untouched in actionable alert-routing design, so its scheduled alert processing gate to apply alert-routing behavior only during an approved maintenance window fails.
- **C — Incorrect.** First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented.
  First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented. This actionable alert-routing design pair serves alert target scopes. Actionable alert-routing design closes alert target scopes, not scheduled alert processing; without the scheduled alert processing workflow, it cannot apply alert-routing behavior only during an approved maintenance window.
- **D — Incorrect.** First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.
  First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group. This actionable alert-routing design pair serves action group association. Action group association cannot replace scheduled alert processing in actionable alert-routing design. Use this scheduled alert processing pair instead: First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB23-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)

**Source reviewed:** 2026-08-31

## LAB23-Q47 — A

**Question:** The monitoring administrator routing and suppressing actionable alerts needs a safe actionable alert-routing design change to trigger on a matching Activity Log record, followed by alert routing evidence. Which pair merits approval?

- **A — Correct.** First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.
  First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event. In the actionable alert-routing design, the first activity log alerts step runs; the actionable alert-routing design then reads activity log alerts state to prove it can trigger on a matching Activity Log record.
- **B — Incorrect.** First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
  First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore. This actionable alert-routing design pair serves dynamic thresholds. Actionable alert-routing design closes dynamic thresholds, not activity log alerts; without the activity log alerts workflow, it cannot trigger on a matching Activity Log record.
- **C — Incorrect.** First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.
  First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group. This actionable alert-routing design pair serves action group association. Action group association cannot replace activity log alerts in actionable alert-routing design. Use this activity log alerts pair instead: First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.
- **D — Incorrect.** First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.
  First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported. This actionable alert-routing design pair serves action group receivers. Actionable alert-routing design proves action group receivers, but activity log alerts lacks implementation in actionable alert-routing design and activity log alerts proof; the activity log alerts outcome to trigger on a matching Activity Log record remains open.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB23-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor activity log alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log)

**Source reviewed:** 2026-08-31

## LAB23-Q48 — C

**Question:** The actionable alert-routing design has two alert routing gates: keep an alert fired until the measured condition has resolved, then prove the actionable alert-routing design state. Which alert routing sequence works?

- **A — Incorrect.** First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.
  First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule. This actionable alert-routing design pair serves alert severity. Actionable alert-routing design closes alert severity, not stateful metric alerts; without the stateful metric alerts workflow, it cannot keep an alert fired until the measured condition has resolved.
- **B — Incorrect.** First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.
  First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported. This actionable alert-routing design pair serves action group receivers. Action group receivers cannot replace stateful metric alerts in actionable alert-routing design. Use this stateful metric alerts pair instead: First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.
- **C — Correct.** First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.
  For the actionable alert-routing design, the safe stateful metric alerts order is: first, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series. The actionable alert-routing design records stateful metric alerts proof after configuration.
- **D — Incorrect.** First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule.
  First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule. This actionable alert-routing design pair serves alert suppression rules. Actionable alert-routing design uses alert suppression rules for both steps; stateful metric alerts remains untouched in actionable alert-routing design, so its stateful metric alerts gate to keep an alert fired until the measured condition has resolved fails.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB23-CP03`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31

## LAB23-Q49 — C

**Question:** Which alert routing path makes the actionable alert-routing design able to let the service learn a changing baseline instead of using one static threshold, then inspects the defining properties?

- **A — Incorrect.** First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
  First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency. This actionable alert-routing design pair serves metric alert conditions. Metric alert conditions cannot replace dynamic thresholds in actionable alert-routing design. Use this dynamic thresholds pair instead: First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
- **B — Incorrect.** First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule.
  First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule. This actionable alert-routing design pair serves alert suppression rules. Actionable alert-routing design proves alert suppression rules, but dynamic thresholds lacks implementation in actionable alert-routing design and dynamic thresholds proof; the dynamic thresholds outcome to let the service learn a changing baseline instead of using one static threshold remains open.
- **C — Correct.** First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
  First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore. The actionable alert-routing design uses its dynamic thresholds mutation gate and dynamic thresholds verification gate before it can let the service learn a changing baseline instead of using one static threshold.
- **D — Incorrect.** First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.
  First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime. This actionable alert-routing design pair serves scheduled alert processing. Actionable alert-routing design closes scheduled alert processing, not dynamic thresholds; without the dynamic thresholds workflow, it cannot let the service learn a changing baseline instead of using one static threshold.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB23-CP04`).

**Microsoft Learn sources:**

- [Dynamic thresholds in Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-dynamic-thresholds)

**Source reviewed:** 2026-08-31

## LAB23-Q50 — C

**Question:** At the actionable alert-routing design approval gate, operators must show that the alert routing can encode operational urgency independently of whether a rule fires. Which alert routing configure-and-check pair is defensible?

- **A — Incorrect.** First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented.
  First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented. This actionable alert-routing design pair serves alert target scopes. Actionable alert-routing design proves alert target scopes, but alert severity lacks implementation in actionable alert-routing design and alert severity proof; the alert severity outcome to encode operational urgency independently of whether a rule fires remains open.
- **B — Incorrect.** First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.
  First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime. This actionable alert-routing design pair serves scheduled alert processing. Actionable alert-routing design uses scheduled alert processing for both steps; alert severity remains untouched in actionable alert-routing design, so its alert severity gate to encode operational urgency independently of whether a rule fires fails.
- **C — Correct.** First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.
  The actionable alert-routing design gets a complete alert severity sequence here: first, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule. Read-back evidence follows the change.
- **D — Incorrect.** First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.
  First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event. This actionable alert-routing design pair serves activity log alerts. Activity log alerts cannot replace alert severity in actionable alert-routing design. Use this alert severity pair instead: First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.

**Objectives:** `MR-MONITOR-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB23-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor metric alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Source reviewed:** 2026-08-31
