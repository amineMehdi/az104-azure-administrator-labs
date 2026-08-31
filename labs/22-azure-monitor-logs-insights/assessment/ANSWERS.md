# Lab 22 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB22-Q01`)

The lab establishes this design principle: Metrics are numeric time series, logs are queryable records with ingestion delay and cost, and Insights packages add curated collection and interpretation for particular resource types.

Objectives: MR-MONITOR-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/metrics-getting-started>

## 2. B (`LAB22-Q02`)

The reviewed hands-on action for this objective is: Discover diagnostic categories and create settings that send supported logs and metrics to the workspace.

Objectives: MR-MONITOR-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings>

## 3. C (`LAB22-Q03`)

Least privilege requires the documented boundary: Monitoring Contributor and Log Analytics Contributor on the lab resource group

Objectives: MR-MONITOR-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview>

## 4. D (`LAB22-Q04`)

The lab records the exact scope and identity of diagnostic setting before validation and cleanup.

Objectives: MR-MONITOR-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview>

## 5. A (`LAB22-Q05`)

Context, authorization, scope, and gates are separate prerequisites that must be confirmed.

Objectives: MR-MONITOR-06

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview>

## 6. B (`LAB22-Q06`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: MR-MONITOR-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/metrics-getting-started>

## 7. C (`LAB22-Q07`)

The lab's reviewed command path performs this bounded action: Run KQL queries that summarize activity by operation, result, and time range without assuming immediate ingestion.

Objectives: MR-MONITOR-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings>

## 8. D (`LAB22-Q08`)

The independent validation path must prove Microsoft.Insights/diagnosticSettings for the exact recorded object.

Objectives: MR-MONITOR-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview>

## 9. A (`LAB22-Q09`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: MR-MONITOR-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview>

## 10. B (`LAB22-Q10`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: MR-MONITOR-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview>

## 11. C (`LAB22-Q11`)

A bounded negative assertion detects accidental privilege or exposure beyond the intended state.

Objectives: MR-MONITOR-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/metrics-getting-started>

## 12. D (`LAB22-Q12`)

Immutable recorded IDs create a deterministic validation and cleanup boundary.

Objectives: MR-MONITOR-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings>

## 13. A (`LAB22-Q13`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: MR-MONITOR-03, MR-MONITOR-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview>

## 14. B (`LAB22-Q14`)

Accepted requests and offline checks do not prove the final live state.

Objectives: MR-MONITOR-05, MR-MONITOR-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview>

## 15. C (`LAB22-Q15`)

The narrowest evidence-supported correction avoids unrelated changes and excess privilege.

Objectives: MR-MONITOR-06, MR-MONITOR-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview>
