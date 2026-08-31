# Lab 23 answer key

Return to [the questions](QUESTIONS.md).

## 1. D (`LAB23-Q01`)

The lab establishes this design principle: Alert rules evaluate signals, action groups deliver notifications or automation, and processing rules change action behavior without disabling signal evaluation.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups>

## 2. A (`LAB23-Q02`)

The reviewed hands-on action for this objective is: Create a metric alert with explicit scope, aggregation, threshold, frequency, and window.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule>

## 3. B (`LAB23-Q03`)

Least privilege requires the documented boundary: Monitoring Contributor on the lab resource group

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log>

## 4. C (`LAB23-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules>

## 5. D (`LAB23-Q05`)

The lab's reviewed command path performs this bounded action: Create an action group with a test email receiver only when AZ104_ALERT_EMAIL is supplied.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups>

## 6. A (`LAB23-Q06`)

The independent validation path must prove Microsoft.Insights/metricAlerts for the exact recorded object.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule>

## 7. B (`LAB23-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: Email delivery and action-group testing require AZ104_ALERT_EMAIL; otherwise a receiver-free action group is used for configuration practice.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log>

## 8. C (`LAB23-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules>

## 9. D (`LAB23-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups>

## 10. A (`LAB23-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule>
