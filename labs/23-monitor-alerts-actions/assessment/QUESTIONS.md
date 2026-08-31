# Lab 23 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB23-Q01 — Foundational

The actionable alert-routing design acceptance criteria require operators to evaluate a numeric signal against a threshold over a defined window. Which service fact supports that requirement?

- A. An alert rule evaluates only the resources included in its configured scopes and supported regional model.
- B. An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation.
- C. A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes.
- D. A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.

## LAB23-Q02 — Foundational

An alert routing reviewer challenges whether the actionable alert-routing design can attach an alert rule to the resource that emits the monitored signal. Which response resolves the concern?

- A. An action group defines reusable notification and automation receivers and must be linked to the alert rule to run.
- B. Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied.
- C. An alert rule evaluates only the resources included in its configured scopes and supported regional model.
- D. Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions.

## LAB23-Q03 — Foundational

The actionable alert-routing design handoff omits the alert routing rule needed to connect an alert rule to reusable notification and automation actions. Which statement should the team add?

- A. Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior.
- B. An action group defines reusable notification and automation receivers and must be linked to the alert rule to run.
- C. An activity log alert matches subscription-level control-plane events by category and selected conditions.
- D. Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself.

## LAB23-Q04 — Foundational

An alert routing incident review of the actionable alert-routing design depends on the ability to route a fired alert to the intended email, webhook, or automation endpoint. Which platform description is reliable?

- A. An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation.
- B. Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior.
- C. A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.
- D. A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes.

## LAB23-Q05 — Foundational

A monitoring administrator routing and suppressing actionable alerts is updating the alert routing runbook. The requirement is to change delivery of matching notifications while leaving detection intact. Which statement describes Azure behavior correctly?

- A. An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation.
- B. Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied.
- C. Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions.
- D. An alert rule evaluates only the resources included in its configured scopes and supported regional model.

## LAB23-Q06 — Foundational

An alert routing peer review asks how the actionable alert-routing design should handle this outcome: apply alert-routing behavior only during an approved maintenance window. Which explanation is accurate?

- A. An activity log alert matches subscription-level control-plane events by category and selected conditions.
- B. Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself.
- C. An action group defines reusable notification and automation receivers and must be linked to the alert rule to run.
- D. Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied.

## LAB23-Q07 — Foundational

For the actionable alert-routing design, the alert routing plan must trigger on a matching Activity Log record. Which statement about alert routing belongs in the actionable alert-routing design record?

- A. An activity log alert matches subscription-level control-plane events by category and selected conditions.
- B. A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.
- C. A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes.
- D. Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior.

## LAB23-Q08 — Foundational

The alert routing review compares four claims for the actionable alert-routing design requirement to keep an alert fired until the measured condition has resolved. Which claim is technically sound?

- A. Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions.
- B. An alert rule evaluates only the resources included in its configured scopes and supported regional model.
- C. An alert processing rule can suppress actions for matching fired alerts without disabling alert evaluation.
- D. A stateful metric alert fires when its condition is met and resolves after the signal no longer meets the rule's resolution logic.

## LAB23-Q09 — Foundational

The alert routing architecture note requires the actionable alert-routing design environment to let the service learn a changing baseline instead of using one static threshold. Which statement defines the relevant alert routing boundary?

- A. Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself.
- B. An action group defines reusable notification and automation receivers and must be linked to the alert rule to run.
- C. Alert processing schedules use configured recurrence and time-zone rules to control when actions are applied.
- D. Dynamic-threshold metric alerts learn historical behavior and require enough suitable data before producing meaningful anomaly decisions.

## LAB23-Q10 — Foundational

A new alert routing operator must explain why the actionable alert-routing design can encode operational urgency independently of whether a rule fires. Which explanation is accurate?

- A. A metric alert evaluates a metric, aggregation, operator, threshold, window, and frequency against one or more scopes.
- B. Each action-group receiver type has its own address, authentication, regional, and rate-limit behavior.
- C. An activity log alert matches subscription-level control-plane events by category and selected conditions.
- D. Azure Monitor severity is operator-defined classification from Sev0 through Sev4 and does not change the measured condition itself.

## LAB23-Q11 — Foundational

An actionable alert-routing design review finds alert routing drift from the need to evaluate a numeric signal against a threshold over a defined window. Which correction addresses that drift?

- A. Create the action group and attach its resource ID to the alert rule actions.
- B. Define the condition from the incident signal and use a window that avoids meaningless single-sample noise.
- C. Define the maintenance recurrence and time zone explicitly and review its start and end boundaries.
- D. Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts.

## LAB23-Q12 — Foundational

The actionable alert-routing design window permits only the alert routing change needed to attach an alert rule to the resource that emits the monitored signal. Which option respects the boundary?

- A. Set scopes to the exact resources or common supported scope that must be monitored.
- B. Configure only approved receiver types and validate each address without committing secrets.
- C. Create conditions for the required operation, status, resource type, or caller and attach an action group.
- D. Set severity from the organization's impact and response model and route actions accordingly.

## LAB23-Q13 — Foundational

The alert routing preflight has passed; the actionable alert-routing design must now connect an alert rule to reusable notification and automation actions. Which operation should run?

- A. Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled.
- B. Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications.
- C. Define the condition from the incident signal and use a window that avoids meaningless single-sample noise.
- D. Create the action group and attach its resource ID to the alert rule actions.

## LAB23-Q14 — Foundational

The actionable alert-routing design plan must route a fired alert to the intended email, webhook, or automation endpoint while limiting the mutation scope to alert routing. Which action is appropriate?

- A. Define the maintenance recurrence and time zone explicitly and review its start and end boundaries.
- B. Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts.
- C. Configure only approved receiver types and validate each address without committing secrets.
- D. Set scopes to the exact resources or common supported scope that must be monitored.

## LAB23-Q15 — Foundational

An alert routing ticket in the actionable alert-routing design says to change delivery of matching notifications while leaving detection intact. Which alert routing action completes the actionable alert-routing design request with minimal change?

- A. Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled.
- B. Create conditions for the required operation, status, resource type, or caller and attach an action group.
- C. Set severity from the organization's impact and response model and route actions accordingly.
- D. Create the action group and attach its resource ID to the alert rule actions.

## LAB23-Q16 — Applied

The approach for the actionable alert-routing design is approved, but the alert routing environment still cannot apply alert-routing behavior only during an approved maintenance window. Which implementation step closes the gap?

- A. Define the maintenance recurrence and time zone explicitly and review its start and end boundaries.
- B. Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications.
- C. Define the condition from the incident signal and use a window that avoids meaningless single-sample noise.
- D. Configure only approved receiver types and validate each address without committing secrets.

## LAB23-Q17 — Applied

The monitoring administrator routing and suppressing actionable alerts may change the actionable alert-routing design only to trigger on a matching Activity Log record. Which alert routing action stays within that assignment?

- A. Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts.
- B. Create conditions for the required operation, status, resource type, or caller and attach an action group.
- C. Set scopes to the exact resources or common supported scope that must be monitored.
- D. Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled.

## LAB23-Q18 — Applied

An alert routing dry run shows no actionable alert-routing design command will keep an alert fired until the measured condition has resolved. Which action belongs before execution?

- A. Set severity from the organization's impact and response model and route actions accordingly.
- B. Create the action group and attach its resource ID to the alert rule actions.
- C. Define the maintenance recurrence and time zone explicitly and review its start and end boundaries.
- D. Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications.

## LAB23-Q19 — Applied

For the actionable alert-routing design, operators need to let the service learn a changing baseline instead of using one static threshold. Which change realizes that requirement?

- A. Define the condition from the incident signal and use a window that avoids meaningless single-sample noise.
- B. Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts.
- C. Configure only approved receiver types and validate each address without committing secrets.
- D. Create conditions for the required operation, status, resource type, or caller and attach an action group.

## LAB23-Q20 — Applied

Operators must automate the actionable alert-routing design change needed to encode operational urgency independently of whether a rule fires. Which alert routing operation belongs in the runbook?

- A. Set scopes to the exact resources or common supported scope that must be monitored.
- B. Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled.
- C. Set severity from the organization's impact and response model and route actions accordingly.
- D. Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications.

## LAB23-Q21 — Applied

The alert routing validation asks whether the actionable alert-routing design can evaluate a numeric signal against a threshold over a defined window. Which observable state is strongest?

- A. Query receiver collections and perform a controlled action-group test where supported.
- B. Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
- C. Query allOf conditions and generate a safe matching control-plane event.
- D. Query severity, enabled state, description, and action groups on the rule.

## LAB23-Q22 — Applied

An actionable alert-routing design review must prove the alert routing ability to attach an alert rule to the resource that emits the monitored signal. Which check avoids an adjacent feature?

- A. Query processing-rule scopes, filters, action type, enabled state, and schedule.
- B. Query scopes and confirm each intended resource ID is represented.
- C. Inspect fired and resolved timestamps and correlate them with the metric series.
- D. Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.

## LAB23-Q23 — Applied

The actionable alert-routing design evidence bundle needs an alert routing result showing it can connect an alert rule to reusable notification and automation actions. Which result belongs in the checkpoint?

- A. Query schedule recurrence, timeZone, startDateTime, and endDateTime.
- B. Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
- C. Query scopes and confirm each intended resource ID is represented.
- D. Query the alert rule actions and resolve each referenced action group.

## LAB23-Q24 — Applied

Before actionable alert-routing design cleanup, the alert routing team must reconfirm it can route a fired alert to the intended email, webhook, or automation endpoint. Which read-only inspection should run?

- A. Query receiver collections and perform a controlled action-group test where supported.
- B. Query allOf conditions and generate a safe matching control-plane event.
- C. Query severity, enabled state, description, and action groups on the rule.
- D. Query the alert rule actions and resolve each referenced action group.

## LAB23-Q25 — Applied

The actionable alert-routing design setup reports success after the alert routing attempt to change delivery of matching notifications while leaving detection intact. Which alert routing read-only observation proves the actionable alert-routing design outcome?

- A. Inspect fired and resolved timestamps and correlate them with the metric series.
- B. Query processing-rule scopes, filters, action type, enabled state, and schedule.
- C. Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
- D. Query receiver collections and perform a controlled action-group test where supported.

## LAB23-Q26 — Applied

The alert routing log says the actionable alert-routing design can now apply alert-routing behavior only during an approved maintenance window. Which alert routing state should the actionable alert-routing design acceptance test retain?

- A. Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
- B. Query scopes and confirm each intended resource ID is represented.
- C. Query schedule recurrence, timeZone, startDateTime, and endDateTime.
- D. Query processing-rule scopes, filters, action type, enabled state, and schedule.

## LAB23-Q27 — Applied

The actionable alert-routing design rejects alert routing exit status as proof it can trigger on a matching Activity Log record. Which actionable alert-routing design result is valid evidence?

- A. Query severity, enabled state, description, and action groups on the rule.
- B. Query the alert rule actions and resolve each referenced action group.
- C. Query schedule recurrence, timeZone, startDateTime, and endDateTime.
- D. Query allOf conditions and generate a safe matching control-plane event.

## LAB23-Q28 — Applied

The alert routing validator needs one actionable alert-routing design query after the change to keep an alert fired until the measured condition has resolved. Which alert routing property should the actionable alert-routing design validator inspect?

- A. Inspect fired and resolved timestamps and correlate them with the metric series.
- B. Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
- C. Query receiver collections and perform a controlled action-group test where supported.
- D. Query allOf conditions and generate a safe matching control-plane event.

## LAB23-Q29 — Applied

The monitoring administrator routing and suppressing actionable alerts must confirm the actionable alert-routing design, without mutation, can let the service learn a changing baseline instead of using one static threshold. Which alert routing check qualifies?

- A. Query scopes and confirm each intended resource ID is represented.
- B. Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
- C. Query processing-rule scopes, filters, action type, enabled state, and schedule.
- D. Inspect fired and resolved timestamps and correlate them with the metric series.

## LAB23-Q30 — Applied

The actionable alert-routing design configuration is complete; the alert routing reviewers need evidence it can encode operational urgency independently of whether a rule fires. Which observation shows success?

- A. Query the alert rule actions and resolve each referenced action group.
- B. Query severity, enabled state, description, and action groups on the rule.
- C. Query schedule recurrence, timeZone, startDateTime, and endDateTime.
- D. Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.

## LAB23-Q31 — Applied

Although the actionable alert-routing design is meant to let the alert routing evaluate a numeric signal against a threshold over a defined window, its checkpoint fails. Which alert routing defect explains the failure?

- A. The rule was created in the correct resource group but its scopes point to a different resource.
- B. The schedule was authored in UTC while the maintenance window was interpreted as local time.
- C. The rule uses Average when the requirement is to catch any maximum value above the limit.
- D. The rule's severity conflicts with the incident-routing policy used by its action group.

## LAB23-Q32 — Applied

The alert routing support team isolated the actionable alert-routing design incident to the attempt to attach an alert rule to the resource that emits the monitored signal. Which condition prevents success?

- A. The action group exists but is not referenced by the enabled alert rule.
- B. The condition filters on a data-plane operation that does not appear in the Azure Activity Log.
- C. The rule uses Average when the requirement is to catch any maximum value above the limit.
- D. The rule was created in the correct resource group but its scopes point to a different resource.

## LAB23-Q33 — Applied

An actionable alert-routing design query surprises the monitoring administrator routing and suppressing actionable alerts during the alert routing attempt to connect an alert rule to reusable notification and automation actions. Which finding explains it?

- A. The email receiver address contains a typographical error.
- B. The action group exists but is not referenced by the enabled alert rule.
- C. The team expects a new notification at every evaluation while using a stateful alert.
- D. The rule was created in the correct resource group but its scopes point to a different resource.

## LAB23-Q34 — Applied

Other actionable alert-routing design components are healthy, but the alert routing still cannot route a fired alert to the intended email, webhook, or automation endpoint. Which state causes the isolated failure?

- A. The alert rule itself was disabled, eliminating evaluation evidence during maintenance.
- B. The resource has too little historical metric data for the dynamic baseline.
- C. The email receiver address contains a typographical error.
- D. The action group exists but is not referenced by the enabled alert rule.

## LAB23-Q35 — Applied

During an alert routing fault drill, the actionable alert-routing design does not change delivery of matching notifications while leaving detection intact. Which finding identifies the defect?

- A. The schedule was authored in UTC while the maintenance window was interpreted as local time.
- B. The rule's severity conflicts with the incident-routing policy used by its action group.
- C. The alert rule itself was disabled, eliminating evaluation evidence during maintenance.
- D. The email receiver address contains a typographical error.

## LAB23-Q36 — Applied

The actionable alert-routing design setup finishes, yet the alert routing cannot apply alert-routing behavior only during an approved maintenance window. Which misconfiguration explains the mismatch?

- A. The condition filters on a data-plane operation that does not appear in the Azure Activity Log.
- B. The rule uses Average when the requirement is to catch any maximum value above the limit.
- C. The alert rule itself was disabled, eliminating evaluation evidence during maintenance.
- D. The schedule was authored in UTC while the maintenance window was interpreted as local time.

## LAB23-Q37 — Applied

An alert routing break/fix in the actionable alert-routing design fails when operators try to trigger on a matching Activity Log record. Which diagnosis fits?

- A. The team expects a new notification at every evaluation while using a stateful alert.
- B. The rule was created in the correct resource group but its scopes point to a different resource.
- C. The condition filters on a data-plane operation that does not appear in the Azure Activity Log.
- D. The schedule was authored in UTC while the maintenance window was interpreted as local time.

## LAB23-Q38 — Applied

The actionable alert-routing design troubleshooting scope is the alert routing need to keep an alert fired until the measured condition has resolved. Which condition should be corrected first?

- A. The team expects a new notification at every evaluation while using a stateful alert.
- B. The resource has too little historical metric data for the dynamic baseline.
- C. The action group exists but is not referenced by the enabled alert rule.
- D. The condition filters on a data-plane operation that does not appear in the Azure Activity Log.

## LAB23-Q39 — Applied

The actionable alert-routing design result is partial because the alert routing cannot let the service learn a changing baseline instead of using one static threshold. Which condition accounts for that result?

- A. The rule's severity conflicts with the incident-routing policy used by its action group.
- B. The email receiver address contains a typographical error.
- C. The team expects a new notification at every evaluation while using a stateful alert.
- D. The resource has too little historical metric data for the dynamic baseline.

## LAB23-Q40 — Applied

The alert routing evidence shows the actionable alert-routing design cannot encode operational urgency independently of whether a rule fires. Which root cause fits that evidence?

- A. The rule uses Average when the requirement is to catch any maximum value above the limit.
- B. The rule's severity conflicts with the incident-routing policy used by its action group.
- C. The alert rule itself was disabled, eliminating evaluation evidence during maintenance.
- D. The resource has too little historical metric data for the dynamic baseline.

## LAB23-Q41 — Advanced

The actionable alert-routing design forbids a partial alert routing result. Operators must first evaluate a numeric signal against a threshold over a defined window and afterward confirm the actionable alert-routing design outcome. Which alert routing sequence is complete?

- A. First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.
- B. First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.
- C. First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
- D. First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.

## LAB23-Q42 — Advanced

Only the actionable alert-routing design change needed to attach an alert rule to the resource that emits the monitored signal is allowed, and alert routing proof is mandatory. Which pair fits?

- A. First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.
- B. First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.
- C. First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
- D. First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented.

## LAB23-Q43 — Advanced

The actionable alert-routing design runbook separates alert routing mutation from validation while it must connect an alert rule to reusable notification and automation actions. Which sequence proves it cleanly?

- A. First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.
- B. First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule.
- C. First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
- D. First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.

## LAB23-Q44 — Advanced

The actionable alert-routing design checkpoint requires both this alert routing outcome—route a fired alert to the intended email, webhook, or automation endpoint—and a read-only actionable alert-routing design state check. Which alert routing response is complete?

- A. First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.
- B. First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.
- C. First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
- D. First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.

## LAB23-Q45 — Advanced

The actionable alert-routing design runbook must change delivery of matching notifications while leaving detection intact, then retain alert routing read-back evidence. Which actionable alert-routing design pair completes both duties?

- A. First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule.
- B. First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.
- C. First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
- D. First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented.

## LAB23-Q46 — Advanced

To satisfy the alert routing requirement, operators must change the actionable alert-routing design configuration and prove it can apply alert-routing behavior only during an approved maintenance window. Which sequence is coherent?

- A. First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.
- B. First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.
- C. First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented.
- D. First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.

## LAB23-Q47 — Advanced

The monitoring administrator routing and suppressing actionable alerts needs a safe actionable alert-routing design change to trigger on a matching Activity Log record, followed by alert routing evidence. Which pair merits approval?

- A. First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.
- B. First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
- C. First, Create the action group and attach its resource ID to the alert rule actions. Then, Query the alert rule actions and resolve each referenced action group.
- D. First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.

## LAB23-Q48 — Advanced

The actionable alert-routing design has two alert routing gates: keep an alert fired until the measured condition has resolved, then prove the actionable alert-routing design state. Which alert routing sequence works?

- A. First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.
- B. First, Configure only approved receiver types and validate each address without committing secrets. Then, Query receiver collections and perform a controlled action-group test where supported.
- C. First, Use stateful behavior when operators need one incident lifecycle rather than repeated stateless notifications. Then, Inspect fired and resolved timestamps and correlate them with the metric series.
- D. First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule.

## LAB23-Q49 — Advanced

Which alert routing path makes the actionable alert-routing design able to let the service learn a changing baseline instead of using one static threshold, then inspects the defining properties?

- A. First, Define the condition from the incident signal and use a window that avoids meaningless single-sample noise. Then, Query criteria metricName, timeAggregation, operator, threshold, windowSize, and evaluationFrequency.
- B. First, Create a suppression rule scoped to the maintenance targets and leave the alert rule enabled. Then, Query processing-rule scopes, filters, action type, enabled state, and schedule.
- C. First, Choose dynamic thresholds for seasonal signals with sufficient history and configure sensitivity and violation counts. Then, Query criterionType, alertSensitivity, failingPeriods, and ignoreDataBefore.
- D. First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.

## LAB23-Q50 — Advanced

At the actionable alert-routing design approval gate, operators must show that the alert routing can encode operational urgency independently of whether a rule fires. Which alert routing configure-and-check pair is defensible?

- A. First, Set scopes to the exact resources or common supported scope that must be monitored. Then, Query scopes and confirm each intended resource ID is represented.
- B. First, Define the maintenance recurrence and time zone explicitly and review its start and end boundaries. Then, Query schedule recurrence, timeZone, startDateTime, and endDateTime.
- C. First, Set severity from the organization's impact and response model and route actions accordingly. Then, Query severity, enabled state, description, and action groups on the rule.
- D. First, Create conditions for the required operation, status, resource type, or caller and attach an action group. Then, Query allOf conditions and generate a safe matching control-plane event.

[Open the answer key](./ANSWERS.md)
