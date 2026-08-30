# Lab 22 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB22-Q01`)

The lab's central distinction is: Metrics are numeric time series, logs are queryable records with ingestion delay and cost, and Insights packages add curated collection and interpretation for particular resource types.

Objectives: MR-MONITOR-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/metrics-getting-started

## 2. B (`LAB22-Q02`)

The first implementation checkpoint is: Create a Log Analytics workspace with bounded retention and a monitored storage account.

Objectives: MR-MONITOR-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings

## 3. C (`LAB22-Q03`)

The documented permission boundary is Monitoring Contributor and Log Analytics Contributor on the lab resource group

Objectives: MR-MONITOR-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview

## 4. D (`LAB22-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: MR-MONITOR-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview

## 5. A (`LAB22-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: MR-MONITOR-06

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview

## 6. B (`LAB22-Q06`)

The live-only gate is explicit and must not be guessed: None beyond the declared role and a disposable subscription.

Objectives: MR-MONITOR-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/metrics-getting-started

## 7. C (`LAB22-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: MR-MONITOR-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings

## 8. D (`LAB22-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: MR-MONITOR-03, MR-MONITOR-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview

## 9. A (`LAB22-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: MR-MONITOR-05, MR-MONITOR-06

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview

## 10. B (`LAB22-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: MR-MONITOR-06, MR-MONITOR-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview
