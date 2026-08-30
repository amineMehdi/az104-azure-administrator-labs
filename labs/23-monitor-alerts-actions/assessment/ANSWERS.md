# Lab 23 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB23-Q01`)

The lab's central distinction is: Alert rules evaluate signals, action groups deliver notifications or automation, and processing rules change action behavior without disabling signal evaluation.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups

## 2. B (`LAB23-Q02`)

The first implementation checkpoint is: Create an action group with a test email receiver only when AZ104_ALERT_EMAIL is supplied.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule

## 3. C (`LAB23-Q03`)

The documented permission boundary is Monitoring Contributor on the lab resource group

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log

## 4. D (`LAB23-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules

## 5. A (`LAB23-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups

## 6. B (`LAB23-Q06`)

The live-only gate is explicit and must not be guessed: Email delivery and action-group testing require AZ104_ALERT_EMAIL; otherwise a receiver-free action group is used for configuration practice.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule

## 7. C (`LAB23-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log

## 8. D (`LAB23-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules

## 9. A (`LAB23-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups

## 10. B (`LAB23-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: MR-MONITOR-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule
