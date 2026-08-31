# Lab 22 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB22-Q01 — B

**Question:** The telemetry assessment review compares four claims for the evidence-based monitoring workspace requirement to decide whether a measurement belongs in metrics or queryable events. Which claim is technically sound?

- **A — Incorrect.** A metric chart or query combines samples using an aggregation over a selected time grain and interval.
  A metric chart or query combines samples using an aggregation over a selected time grain and interval. In the evidence-based monitoring workspace, this statement describes metric aggregation and time grain. Evidence-based monitoring workspace asks about metrics and logs; this metric aggregation and time grain choice leaves the metrics and logs explanation missing.
- **B — Correct.** Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
  The evidence-based monitoring workspace needs metrics and logs to decide whether a measurement belongs in metrics or queryable events; this option states the applicable metrics and logs rule: metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
- **C — Incorrect.** A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior.
  A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior. In the evidence-based monitoring workspace, this statement describes Log Analytics workspaces. Selecting Log Analytics workspaces for evidence-based monitoring workspace leaves metrics and logs unanswered in evidence-based monitoring workspace; the evidence-based monitoring workspace lacks a metrics and logs basis to decide whether a measurement belongs in metrics or queryable events.
- **D — Incorrect.** Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types.
  Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types. In the evidence-based monitoring workspace, this statement describes Azure Monitor Insights. Metrics and logs governs evidence-based monitoring workspace; Azure Monitor Insights cannot support metrics and logs when operators must decide whether a measurement belongs in metrics or queryable events.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor data platform](https://learn.microsoft.com/en-us/azure/azure-monitor/data-platform)

**Source reviewed:** 2026-08-31

## LAB22-Q02 — D

**Question:** The telemetry assessment architecture note requires the evidence-based monitoring workspace environment to interpret a chart only after checking its aggregation and time grain. Which statement defines the relevant telemetry assessment boundary?

- **A — Incorrect.** A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs.
  A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs. In the evidence-based monitoring workspace, this statement describes diagnostic setting destinations. The diagnostic setting destinations statement accurately describes diagnostic setting destinations; however, evidence-based monitoring workspace needs metric aggregation and time grain to interpret a chart only after checking its aggregation and time grain; diagnostic setting destinations cannot replace metric aggregation and time grain.
- **B — Incorrect.** KQL operators such as where, project, summarize, and order by shape records into focused operational evidence.
  KQL operators such as where, project, summarize, and order by shape records into focused operational evidence. In the evidence-based monitoring workspace, this statement describes KQL filtering and summarization. Selecting KQL filtering and summarization for evidence-based monitoring workspace leaves metric aggregation and time grain unanswered in evidence-based monitoring workspace; the evidence-based monitoring workspace lacks a metric aggregation and time grain basis to interpret a chart only after checking its aggregation and time grain.
- **C — Incorrect.** Connection Monitor records recurring network reachability and latency tests between configured endpoints.
  Connection Monitor records recurring network reachability and latency tests between configured endpoints. In the evidence-based monitoring workspace, this statement describes Connection Monitor telemetry. Metric aggregation and time grain governs evidence-based monitoring workspace; Connection Monitor telemetry cannot support metric aggregation and time grain when operators must interpret a chart only after checking its aggregation and time grain.
- **D — Correct.** A metric chart or query combines samples using an aggregation over a selected time grain and interval.
  A metric chart or query combines samples using an aggregation over a selected time grain and interval. This metric aggregation and time grain fact resolves the evidence-based monitoring workspace design question about how to interpret a chart only after checking its aggregation and time grain.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metrics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/data-platform-metrics)

**Source reviewed:** 2026-08-31

## LAB22-Q03 — A

**Question:** A new telemetry assessment operator must explain why the evidence-based monitoring workspace can send supported resource telemetry to an approved destination. Which explanation is accurate?

- **A — Correct.** A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs.
  A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs. For evidence-based monitoring workspace, diagnostic setting destinations supplies the service rule needed to send supported resource telemetry to an approved destination.
- **B — Incorrect.** Available diagnostic log categories differ by resource provider and resource type.
  Available diagnostic log categories differ by resource provider and resource type. In the evidence-based monitoring workspace, this statement describes resource-specific log categories. Diagnostic setting destinations governs evidence-based monitoring workspace; resource-specific log categories cannot support diagnostic setting destinations when operators must send supported resource telemetry to an approved destination.
- **C — Incorrect.** Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.
  Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration. In the evidence-based monitoring workspace, this statement describes log ingestion latency. Evidence-based monitoring workspace asks about diagnostic setting destinations; this log ingestion latency choice leaves the diagnostic setting destinations explanation missing.
- **D — Incorrect.** Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost.
  Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost. In the evidence-based monitoring workspace, this statement describes monitoring retention and cost. The monitoring retention and cost statement accurately describes monitoring retention and cost; however, evidence-based monitoring workspace needs diagnostic setting destinations to send supported resource telemetry to an approved destination; monitoring retention and cost cannot replace diagnostic setting destinations.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q04 — D

**Question:** The evidence-based monitoring workspace acceptance criteria require operators to enable the service-specific log categories required by the query. Which service fact supports that requirement?

- **A — Incorrect.** A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior.
  A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior. In the evidence-based monitoring workspace, this statement describes Log Analytics workspaces. Resource-specific log categories governs evidence-based monitoring workspace; Log Analytics workspaces cannot support resource-specific log categories when operators must enable the service-specific log categories required by the query.
- **B — Incorrect.** Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types.
  Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types. In the evidence-based monitoring workspace, this statement describes Azure Monitor Insights. Evidence-based monitoring workspace asks about resource-specific log categories; this Azure Monitor Insights choice leaves the resource-specific log categories explanation missing.
- **C — Incorrect.** Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
  Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying. In the evidence-based monitoring workspace, this statement describes metrics and logs. The metrics and logs statement accurately describes metrics and logs; however, evidence-based monitoring workspace needs resource-specific log categories to enable the service-specific log categories required by the query; metrics and logs cannot replace resource-specific log categories.
- **D — Correct.** Available diagnostic log categories differ by resource provider and resource type.
  Available diagnostic log categories differ by resource provider and resource type. In the evidence-based monitoring workspace, this resource-specific log categories rule supports the need to enable the service-specific log categories required by the query.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q05 — D

**Question:** A telemetry assessment reviewer challenges whether the evidence-based monitoring workspace can store and query records from several monitored resources in one boundary. Which response resolves the concern?

- **A — Incorrect.** KQL operators such as where, project, summarize, and order by shape records into focused operational evidence.
  KQL operators such as where, project, summarize, and order by shape records into focused operational evidence. In the evidence-based monitoring workspace, this statement describes KQL filtering and summarization. Evidence-based monitoring workspace asks about Log Analytics workspaces; this KQL filtering and summarization choice leaves the Log Analytics workspaces explanation missing.
- **B — Incorrect.** Connection Monitor records recurring network reachability and latency tests between configured endpoints.
  Connection Monitor records recurring network reachability and latency tests between configured endpoints. In the evidence-based monitoring workspace, this statement describes Connection Monitor telemetry. The Connection Monitor telemetry statement accurately describes Connection Monitor telemetry; however, evidence-based monitoring workspace needs Log Analytics workspaces to store and query records from several monitored resources in one boundary; Connection Monitor telemetry cannot replace Log Analytics workspaces.
- **C — Incorrect.** A metric chart or query combines samples using an aggregation over a selected time grain and interval.
  A metric chart or query combines samples using an aggregation over a selected time grain and interval. In the evidence-based monitoring workspace, this statement describes metric aggregation and time grain. Selecting metric aggregation and time grain for evidence-based monitoring workspace leaves Log Analytics workspaces unanswered in evidence-based monitoring workspace; the evidence-based monitoring workspace lacks a Log Analytics workspaces basis to store and query records from several monitored resources in one boundary.
- **D — Correct.** A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior.
  For the evidence-based monitoring workspace, the rule for Log Analytics workspaces is defined by this statement: a Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior. It supports the required outcome to store and query records from several monitored resources in one boundary.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Log Analytics workspace overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q06 — D

**Question:** The evidence-based monitoring workspace handoff omits the telemetry assessment rule needed to filter records and calculate a grouped summary with KQL. Which statement should the team add?

- **A — Incorrect.** Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.
  Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration. In the evidence-based monitoring workspace, this statement describes log ingestion latency. The log ingestion latency statement accurately describes log ingestion latency; however, evidence-based monitoring workspace needs KQL filtering and summarization to filter records and calculate a grouped summary with KQL; log ingestion latency cannot replace KQL filtering and summarization.
- **B — Incorrect.** Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost.
  Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost. In the evidence-based monitoring workspace, this statement describes monitoring retention and cost. Selecting monitoring retention and cost for evidence-based monitoring workspace leaves KQL filtering and summarization unanswered in evidence-based monitoring workspace; the evidence-based monitoring workspace lacks a KQL filtering and summarization basis to filter records and calculate a grouped summary with KQL.
- **C — Incorrect.** A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs.
  A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs. In the evidence-based monitoring workspace, this statement describes diagnostic setting destinations. KQL filtering and summarization governs evidence-based monitoring workspace; diagnostic setting destinations cannot support KQL filtering and summarization when operators must filter records and calculate a grouped summary with KQL.
- **D — Correct.** KQL operators such as where, project, summarize, and order by shape records into focused operational evidence.
  KQL operators such as where, project, summarize, and order by shape records into focused operational evidence. The evidence-based monitoring workspace applies that KQL filtering and summarization boundary when operators must filter records and calculate a grouped summary with KQL.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Log queries in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q07 — C

**Question:** A telemetry assessment incident review of the evidence-based monitoring workspace depends on the ability to allow for collection and processing delay before declaring telemetry missing. Which platform description is reliable?

- **A — Incorrect.** Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types.
  Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types. In the evidence-based monitoring workspace, this statement describes Azure Monitor Insights. Selecting Azure Monitor Insights for evidence-based monitoring workspace leaves log ingestion latency unanswered in evidence-based monitoring workspace; the evidence-based monitoring workspace lacks a log ingestion latency basis to allow for collection and processing delay before declaring telemetry missing.
- **B — Incorrect.** Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
  Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying. In the evidence-based monitoring workspace, this statement describes metrics and logs. Log ingestion latency governs evidence-based monitoring workspace; metrics and logs cannot support log ingestion latency when operators must allow for collection and processing delay before declaring telemetry missing.
- **C — Correct.** Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.
  The evidence-based monitoring workspace needs log ingestion latency to allow for collection and processing delay before declaring telemetry missing; this option states the applicable log ingestion latency rule: diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.
- **D — Incorrect.** Available diagnostic log categories differ by resource provider and resource type.
  Available diagnostic log categories differ by resource provider and resource type. In the evidence-based monitoring workspace, this statement describes resource-specific log categories. The resource-specific log categories statement accurately describes resource-specific log categories; however, evidence-based monitoring workspace needs log ingestion latency to allow for collection and processing delay before declaring telemetry missing; resource-specific log categories cannot replace log ingestion latency.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Log data ingestion time in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-ingestion-time)

**Source reviewed:** 2026-08-31

## LAB22-Q08 — C

**Question:** A monitoring administrator building an evidence-based service view is updating the telemetry assessment runbook. The requirement is to use a curated service view backed by the required monitoring data. Which statement describes Azure behavior correctly?

- **A — Incorrect.** Connection Monitor records recurring network reachability and latency tests between configured endpoints.
  Connection Monitor records recurring network reachability and latency tests between configured endpoints. In the evidence-based monitoring workspace, this statement describes Connection Monitor telemetry. Azure Monitor Insights governs evidence-based monitoring workspace; Connection Monitor telemetry cannot support Azure Monitor Insights when operators must use a curated service view backed by the required monitoring data.
- **B — Incorrect.** A metric chart or query combines samples using an aggregation over a selected time grain and interval.
  A metric chart or query combines samples using an aggregation over a selected time grain and interval. In the evidence-based monitoring workspace, this statement describes metric aggregation and time grain. Evidence-based monitoring workspace asks about Azure Monitor Insights; this metric aggregation and time grain choice leaves the Azure Monitor Insights explanation missing.
- **C — Correct.** Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types.
  Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types. This Azure Monitor Insights fact resolves the evidence-based monitoring workspace design question about how to use a curated service view backed by the required monitoring data.
- **D — Incorrect.** A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior.
  A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior. In the evidence-based monitoring workspace, this statement describes Log Analytics workspaces. Selecting Log Analytics workspaces for evidence-based monitoring workspace leaves Azure Monitor Insights unanswered in evidence-based monitoring workspace; the evidence-based monitoring workspace lacks a Azure Monitor Insights basis to use a curated service view backed by the required monitoring data.

**Objectives:** `MR-MONITOR-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Insights and curated visualizations in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q09 — A

**Question:** A telemetry assessment peer review asks how the evidence-based monitoring workspace should handle this outcome: bring continuous network-test telemetry into the monitoring workflow. Which explanation is accurate?

- **A — Correct.** Connection Monitor records recurring network reachability and latency tests between configured endpoints.
  Connection Monitor records recurring network reachability and latency tests between configured endpoints. For evidence-based monitoring workspace, Connection Monitor telemetry supplies the service rule needed to bring continuous network-test telemetry into the monitoring workflow.
- **B — Incorrect.** Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost.
  Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost. In the evidence-based monitoring workspace, this statement describes monitoring retention and cost. The monitoring retention and cost statement accurately describes monitoring retention and cost; however, evidence-based monitoring workspace needs Connection Monitor telemetry to bring continuous network-test telemetry into the monitoring workflow; monitoring retention and cost cannot replace Connection Monitor telemetry.
- **C — Incorrect.** A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs.
  A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs. In the evidence-based monitoring workspace, this statement describes diagnostic setting destinations. Selecting diagnostic setting destinations for evidence-based monitoring workspace leaves Connection Monitor telemetry unanswered in evidence-based monitoring workspace; the evidence-based monitoring workspace lacks a Connection Monitor telemetry basis to bring continuous network-test telemetry into the monitoring workflow.
- **D — Incorrect.** KQL operators such as where, project, summarize, and order by shape records into focused operational evidence.
  KQL operators such as where, project, summarize, and order by shape records into focused operational evidence. In the evidence-based monitoring workspace, this statement describes KQL filtering and summarization. Connection Monitor telemetry governs evidence-based monitoring workspace; KQL filtering and summarization cannot support Connection Monitor telemetry when operators must bring continuous network-test telemetry into the monitoring workflow.

**Objectives:** `MR-MONITOR-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q10 — A

**Question:** For the evidence-based monitoring workspace, the telemetry assessment plan must control retention and ingestion volume before monitoring cost grows unexpectedly. Which statement about telemetry assessment belongs in the evidence-based monitoring workspace record?

- **A — Correct.** Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost.
  Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost. In the evidence-based monitoring workspace, this monitoring retention and cost rule supports the need to control retention and ingestion volume before monitoring cost grows unexpectedly.
- **B — Incorrect.** Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
  Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying. In the evidence-based monitoring workspace, this statement describes metrics and logs. Selecting metrics and logs for evidence-based monitoring workspace leaves monitoring retention and cost unanswered in evidence-based monitoring workspace; the evidence-based monitoring workspace lacks a monitoring retention and cost basis to control retention and ingestion volume before monitoring cost grows unexpectedly.
- **C — Incorrect.** Available diagnostic log categories differ by resource provider and resource type.
  Available diagnostic log categories differ by resource provider and resource type. In the evidence-based monitoring workspace, this statement describes resource-specific log categories. Monitoring retention and cost governs evidence-based monitoring workspace; resource-specific log categories cannot support monitoring retention and cost when operators must control retention and ingestion volume before monitoring cost grows unexpectedly.
- **D — Incorrect.** Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.
  Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration. In the evidence-based monitoring workspace, this statement describes log ingestion latency. Evidence-based monitoring workspace asks about monitoring retention and cost; this log ingestion latency choice leaves the monitoring retention and cost explanation missing.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor Logs cost calculations and options](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs)

**Source reviewed:** 2026-08-31

## LAB22-Q11 — C

**Question:** A telemetry assessment dry run shows no evidence-based monitoring workspace command will decide whether a measurement belongs in metrics or queryable events. Which action belongs before execution?

- **A — Incorrect.** Select only required categories and send them to the approved destination resources.
  Select only required categories and send them to the approved destination resources. In the evidence-based monitoring workspace, this action changes diagnostic setting destinations. Evidence-based monitoring workspace approved metrics and logs, not diagnostic setting destinations; only the metrics and logs change can decide whether a measurement belongs in metrics or queryable events.
- **B — Incorrect.** Filter early by resource and time, then summarize only the dimensions required by the question.
  Filter early by resource and time, then summarize only the dimensions required by the question. In the evidence-based monitoring workspace, this action changes KQL filtering and summarization. Evidence-based monitoring workspace requires metrics and logs; changing KQL filtering and summarization leaves metrics and logs absent in evidence-based monitoring workspace; evidence-based monitoring workspace cannot decide whether a measurement belongs in metrics or queryable events.
- **C — Correct.** Use a metric for fast numeric trends and logs when the question requires record-level context.
  For the evidence-based monitoring workspace, the required metrics and logs action is: use a metric for fast numeric trends and logs when the question requires record-level context. It makes the environment able to decide whether a measurement belongs in metrics or queryable events.
- **D — Incorrect.** Configure representative endpoints and a test frequency that can reveal intermittent failures.
  Configure representative endpoints and a test frequency that can reveal intermittent failures. In the evidence-based monitoring workspace, this action changes Connection Monitor telemetry. Evidence-based monitoring workspace instead needs metrics and logs: Use a metric for fast numeric trends and logs when the question requires record-level context. The Connection Monitor telemetry action omits that metrics and logs work.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor data platform](https://learn.microsoft.com/en-us/azure/azure-monitor/data-platform)

**Source reviewed:** 2026-08-31

## LAB22-Q12 — C

**Question:** For the evidence-based monitoring workspace, operators need to interpret a chart only after checking its aggregation and time grain. Which change realizes that requirement?

- **A — Incorrect.** List categories on the exact resource before creating the diagnostic setting.
  List categories on the exact resource before creating the diagnostic setting. In the evidence-based monitoring workspace, this action changes resource-specific log categories. Evidence-based monitoring workspace requires metric aggregation and time grain; changing resource-specific log categories leaves metric aggregation and time grain absent in evidence-based monitoring workspace; evidence-based monitoring workspace cannot interpret a chart only after checking its aggregation and time grain.
- **B — Incorrect.** Poll with a bounded timeout while separately verifying the diagnostic setting and generated event.
  Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. In the evidence-based monitoring workspace, this action changes log ingestion latency. Log ingestion latency does not implement metric aggregation and time grain for evidence-based monitoring workspace; the evidence-based monitoring workspace still cannot interpret a chart only after checking its aggregation and time grain.
- **C — Correct.** Choose aggregation and granularity that match the operational question and signal semantics.
  Choose aggregation and granularity that match the operational question and signal semantics. This changes metric aggregation and time grain in the evidence-based monitoring workspace, supplying the missing state needed to interpret a chart only after checking its aggregation and time grain.
- **D — Incorrect.** Collect signals tied to operational requirements and set an approved workspace retention period.
  Collect signals tied to operational requirements and set an approved workspace retention period. In the evidence-based monitoring workspace, this action changes monitoring retention and cost. Evidence-based monitoring workspace approved metric aggregation and time grain, not monitoring retention and cost; only the metric aggregation and time grain change can interpret a chart only after checking its aggregation and time grain.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metrics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/data-platform-metrics)

**Source reviewed:** 2026-08-31

## LAB22-Q13 — D

**Question:** Operators must automate the evidence-based monitoring workspace change needed to send supported resource telemetry to an approved destination. Which telemetry assessment operation belongs in the runbook?

- **A — Incorrect.** Route diagnostic data to the intended workspace and record its immutable resource and customer IDs.
  Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. In the evidence-based monitoring workspace, this action changes Log Analytics workspaces. Log Analytics workspaces does not implement diagnostic setting destinations for evidence-based monitoring workspace; the evidence-based monitoring workspace still cannot send supported resource telemetry to an approved destination.
- **B — Incorrect.** Enable the prerequisites for the resource-specific insight and allow time for data collection.
  Enable the prerequisites for the resource-specific insight and allow time for data collection. In the evidence-based monitoring workspace, this action changes Azure Monitor Insights. Evidence-based monitoring workspace instead needs diagnostic setting destinations: Select only required categories and send them to the approved destination resources. The Azure Monitor Insights action omits that diagnostic setting destinations work.
- **C — Incorrect.** Use a metric for fast numeric trends and logs when the question requires record-level context.
  Use a metric for fast numeric trends and logs when the question requires record-level context. In the evidence-based monitoring workspace, this action changes metrics and logs. Evidence-based monitoring workspace approved diagnostic setting destinations, not metrics and logs; only the diagnostic setting destinations change can send supported resource telemetry to an approved destination.
- **D — Correct.** Select only required categories and send them to the approved destination resources.
  The evidence-based monitoring workspace must send supported resource telemetry to an approved destination; this option performs its direct diagnostic setting destinations change: select only required categories and send them to the approved destination resources.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q14 — D

**Question:** An evidence-based monitoring workspace review finds telemetry assessment drift from the need to enable the service-specific log categories required by the query. Which correction addresses that drift?

- **A — Incorrect.** Filter early by resource and time, then summarize only the dimensions required by the question.
  Filter early by resource and time, then summarize only the dimensions required by the question. In the evidence-based monitoring workspace, this action changes KQL filtering and summarization. Evidence-based monitoring workspace instead needs resource-specific log categories: List categories on the exact resource before creating the diagnostic setting. The KQL filtering and summarization action omits that resource-specific log categories work.
- **B — Incorrect.** Configure representative endpoints and a test frequency that can reveal intermittent failures.
  Configure representative endpoints and a test frequency that can reveal intermittent failures. In the evidence-based monitoring workspace, this action changes Connection Monitor telemetry. Evidence-based monitoring workspace approved resource-specific log categories, not Connection Monitor telemetry; only the resource-specific log categories change can enable the service-specific log categories required by the query.
- **C — Incorrect.** Choose aggregation and granularity that match the operational question and signal semantics.
  Choose aggregation and granularity that match the operational question and signal semantics. In the evidence-based monitoring workspace, this action changes metric aggregation and time grain. Evidence-based monitoring workspace requires resource-specific log categories; changing metric aggregation and time grain leaves resource-specific log categories absent in evidence-based monitoring workspace; evidence-based monitoring workspace cannot enable the service-specific log categories required by the query.
- **D — Correct.** List categories on the exact resource before creating the diagnostic setting.
  List categories on the exact resource before creating the diagnostic setting. It is the least-change resource-specific log categories path for the evidence-based monitoring workspace requirement to enable the service-specific log categories required by the query.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q15 — B

**Question:** The evidence-based monitoring workspace window permits only the telemetry assessment change needed to store and query records from several monitored resources in one boundary. Which option respects the boundary?

- **A — Incorrect.** Poll with a bounded timeout while separately verifying the diagnostic setting and generated event.
  Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. In the evidence-based monitoring workspace, this action changes log ingestion latency. Evidence-based monitoring workspace approved Log Analytics workspaces, not log ingestion latency; only the Log Analytics workspaces change can store and query records from several monitored resources in one boundary.
- **B — Correct.** Route diagnostic data to the intended workspace and record its immutable resource and customer IDs.
  Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. In evidence-based monitoring workspace, applying Log Analytics workspaces is the scoped way to store and query records from several monitored resources in one boundary.
- **C — Incorrect.** Collect signals tied to operational requirements and set an approved workspace retention period.
  Collect signals tied to operational requirements and set an approved workspace retention period. In the evidence-based monitoring workspace, this action changes monitoring retention and cost. Monitoring retention and cost does not implement Log Analytics workspaces for evidence-based monitoring workspace; the evidence-based monitoring workspace still cannot store and query records from several monitored resources in one boundary.
- **D — Incorrect.** Select only required categories and send them to the approved destination resources.
  Select only required categories and send them to the approved destination resources. In the evidence-based monitoring workspace, this action changes diagnostic setting destinations. Evidence-based monitoring workspace instead needs Log Analytics workspaces: Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. The diagnostic setting destinations action omits that Log Analytics workspaces work.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Log Analytics workspace overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q16 — A

**Question:** The telemetry assessment preflight has passed; the evidence-based monitoring workspace must now filter records and calculate a grouped summary with KQL. Which operation should run?

- **A — Correct.** Filter early by resource and time, then summarize only the dimensions required by the question.
  Filter early by resource and time, then summarize only the dimensions required by the question. The evidence-based monitoring workspace uses this KQL filtering and summarization operation to filter records and calculate a grouped summary with KQL within the approved scope.
- **B — Incorrect.** Enable the prerequisites for the resource-specific insight and allow time for data collection.
  Enable the prerequisites for the resource-specific insight and allow time for data collection. In the evidence-based monitoring workspace, this action changes Azure Monitor Insights. Azure Monitor Insights does not implement KQL filtering and summarization for evidence-based monitoring workspace; the evidence-based monitoring workspace still cannot filter records and calculate a grouped summary with KQL.
- **C — Incorrect.** Use a metric for fast numeric trends and logs when the question requires record-level context.
  Use a metric for fast numeric trends and logs when the question requires record-level context. In the evidence-based monitoring workspace, this action changes metrics and logs. Evidence-based monitoring workspace instead needs KQL filtering and summarization: Filter early by resource and time, then summarize only the dimensions required by the question. The metrics and logs action omits that KQL filtering and summarization work.
- **D — Incorrect.** List categories on the exact resource before creating the diagnostic setting.
  List categories on the exact resource before creating the diagnostic setting. In the evidence-based monitoring workspace, this action changes resource-specific log categories. Evidence-based monitoring workspace approved KQL filtering and summarization, not resource-specific log categories; only the KQL filtering and summarization change can filter records and calculate a grouped summary with KQL.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Log queries in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q17 — C

**Question:** The evidence-based monitoring workspace plan must allow for collection and processing delay before declaring telemetry missing while limiting the mutation scope to telemetry assessment. Which action is appropriate?

- **A — Incorrect.** Configure representative endpoints and a test frequency that can reveal intermittent failures.
  Configure representative endpoints and a test frequency that can reveal intermittent failures. In the evidence-based monitoring workspace, this action changes Connection Monitor telemetry. Connection Monitor telemetry does not implement log ingestion latency for evidence-based monitoring workspace; the evidence-based monitoring workspace still cannot allow for collection and processing delay before declaring telemetry missing.
- **B — Incorrect.** Choose aggregation and granularity that match the operational question and signal semantics.
  Choose aggregation and granularity that match the operational question and signal semantics. In the evidence-based monitoring workspace, this action changes metric aggregation and time grain. Evidence-based monitoring workspace instead needs log ingestion latency: Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. The metric aggregation and time grain action omits that log ingestion latency work.
- **C — Correct.** Poll with a bounded timeout while separately verifying the diagnostic setting and generated event.
  For the evidence-based monitoring workspace, the required log ingestion latency action is: poll with a bounded timeout while separately verifying the diagnostic setting and generated event. It makes the environment able to allow for collection and processing delay before declaring telemetry missing.
- **D — Incorrect.** Route diagnostic data to the intended workspace and record its immutable resource and customer IDs.
  Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. In the evidence-based monitoring workspace, this action changes Log Analytics workspaces. Evidence-based monitoring workspace requires log ingestion latency; changing Log Analytics workspaces leaves log ingestion latency absent in evidence-based monitoring workspace; evidence-based monitoring workspace cannot allow for collection and processing delay before declaring telemetry missing.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Log data ingestion time in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-ingestion-time)

**Source reviewed:** 2026-08-31

## LAB22-Q18 — B

**Question:** A telemetry assessment ticket in the evidence-based monitoring workspace says to use a curated service view backed by the required monitoring data. Which telemetry assessment action completes the evidence-based monitoring workspace request with minimal change?

- **A — Incorrect.** Collect signals tied to operational requirements and set an approved workspace retention period.
  Collect signals tied to operational requirements and set an approved workspace retention period. In the evidence-based monitoring workspace, this action changes monitoring retention and cost. Evidence-based monitoring workspace instead needs Azure Monitor Insights: Enable the prerequisites for the resource-specific insight and allow time for data collection. The monitoring retention and cost action omits that Azure Monitor Insights work.
- **B — Correct.** Enable the prerequisites for the resource-specific insight and allow time for data collection.
  Enable the prerequisites for the resource-specific insight and allow time for data collection. This changes Azure Monitor Insights in the evidence-based monitoring workspace, supplying the missing state needed to use a curated service view backed by the required monitoring data.
- **C — Incorrect.** Select only required categories and send them to the approved destination resources.
  Select only required categories and send them to the approved destination resources. In the evidence-based monitoring workspace, this action changes diagnostic setting destinations. Evidence-based monitoring workspace requires Azure Monitor Insights; changing diagnostic setting destinations leaves Azure Monitor Insights absent in evidence-based monitoring workspace; evidence-based monitoring workspace cannot use a curated service view backed by the required monitoring data.
- **D — Incorrect.** Filter early by resource and time, then summarize only the dimensions required by the question.
  Filter early by resource and time, then summarize only the dimensions required by the question. In the evidence-based monitoring workspace, this action changes KQL filtering and summarization. KQL filtering and summarization does not implement Azure Monitor Insights for evidence-based monitoring workspace; the evidence-based monitoring workspace still cannot use a curated service view backed by the required monitoring data.

**Objectives:** `MR-MONITOR-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Insights and curated visualizations in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q19 — B

**Question:** The approach for the evidence-based monitoring workspace is approved, but the telemetry assessment environment still cannot bring continuous network-test telemetry into the monitoring workflow. Which implementation step closes the gap?

- **A — Incorrect.** Use a metric for fast numeric trends and logs when the question requires record-level context.
  Use a metric for fast numeric trends and logs when the question requires record-level context. In the evidence-based monitoring workspace, this action changes metrics and logs. Evidence-based monitoring workspace approved Connection Monitor telemetry, not metrics and logs; only the Connection Monitor telemetry change can bring continuous network-test telemetry into the monitoring workflow.
- **B — Correct.** Configure representative endpoints and a test frequency that can reveal intermittent failures.
  The evidence-based monitoring workspace must bring continuous network-test telemetry into the monitoring workflow; this option performs its direct Connection Monitor telemetry change: configure representative endpoints and a test frequency that can reveal intermittent failures.
- **C — Incorrect.** List categories on the exact resource before creating the diagnostic setting.
  List categories on the exact resource before creating the diagnostic setting. In the evidence-based monitoring workspace, this action changes resource-specific log categories. Resource-specific log categories does not implement Connection Monitor telemetry for evidence-based monitoring workspace; the evidence-based monitoring workspace still cannot bring continuous network-test telemetry into the monitoring workflow.
- **D — Incorrect.** Poll with a bounded timeout while separately verifying the diagnostic setting and generated event.
  Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. In the evidence-based monitoring workspace, this action changes log ingestion latency. Evidence-based monitoring workspace instead needs Connection Monitor telemetry: Configure representative endpoints and a test frequency that can reveal intermittent failures. The log ingestion latency action omits that Connection Monitor telemetry work.

**Objectives:** `MR-MONITOR-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q20 — B

**Question:** The monitoring administrator building an evidence-based service view may change the evidence-based monitoring workspace only to control retention and ingestion volume before monitoring cost grows unexpectedly. Which telemetry assessment action stays within that assignment?

- **A — Incorrect.** Choose aggregation and granularity that match the operational question and signal semantics.
  Choose aggregation and granularity that match the operational question and signal semantics. In the evidence-based monitoring workspace, this action changes metric aggregation and time grain. Evidence-based monitoring workspace requires monitoring retention and cost; changing metric aggregation and time grain leaves monitoring retention and cost absent in evidence-based monitoring workspace; evidence-based monitoring workspace cannot control retention and ingestion volume before monitoring cost grows unexpectedly.
- **B — Correct.** Collect signals tied to operational requirements and set an approved workspace retention period.
  Collect signals tied to operational requirements and set an approved workspace retention period. It is the least-change monitoring retention and cost path for the evidence-based monitoring workspace requirement to control retention and ingestion volume before monitoring cost grows unexpectedly.
- **C — Incorrect.** Route diagnostic data to the intended workspace and record its immutable resource and customer IDs.
  Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. In the evidence-based monitoring workspace, this action changes Log Analytics workspaces. Evidence-based monitoring workspace instead needs monitoring retention and cost: Collect signals tied to operational requirements and set an approved workspace retention period. The Log Analytics workspaces action omits that monitoring retention and cost work.
- **D — Incorrect.** Enable the prerequisites for the resource-specific insight and allow time for data collection.
  Enable the prerequisites for the resource-specific insight and allow time for data collection. In the evidence-based monitoring workspace, this action changes Azure Monitor Insights. Evidence-based monitoring workspace approved monitoring retention and cost, not Azure Monitor Insights; only the monitoring retention and cost change can control retention and ingestion volume before monitoring cost grows unexpectedly.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor Logs cost calculations and options](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs)

**Source reviewed:** 2026-08-31

## LAB22-Q21 — C

**Question:** The telemetry assessment validator needs one evidence-based monitoring workspace query after the change to decide whether a measurement belongs in metrics or queryable events. Which telemetry assessment property should the evidence-based monitoring workspace validator inspect?

- **A — Incorrect.** Query diagnostic-settings categories and match configured categories against the returned list.
  Query diagnostic-settings categories and match configured categories against the returned list. In the evidence-based monitoring workspace, this check observes resource-specific log categories. Evidence-based monitoring workspace output covers resource-specific log categories, not metrics and logs; the metrics and logs requirement to decide whether a measurement belongs in metrics or queryable events remains unverified.
- **B — Incorrect.** Record query time range, retries, and the first matching TimeGenerated value.
  Record query time range, retries, and the first matching TimeGenerated value. In the evidence-based monitoring workspace, this check observes log ingestion latency. Log ingestion latency success in evidence-based monitoring workspace cannot verify metrics and logs; evidence-based monitoring workspace cannot decide whether a measurement belongs in metrics or queryable events until metrics and logs evidence exists.
- **C — Correct.** Query the metric namespace and separately confirm expected records reach the Log Analytics table.
  Query the metric namespace and separately confirm expected records reach the Log Analytics table. For evidence-based monitoring workspace, this metrics and logs read confirms the service can decide whether a measurement belongs in metrics or queryable events.
- **D — Incorrect.** Query daily ingestion, table retention, and enabled categories before and after the change.
  Query daily ingestion, table retention, and enabled categories before and after the change. In the evidence-based monitoring workspace, this check observes monitoring retention and cost. Evidence-based monitoring workspace could pass monitoring retention and cost while metrics and logs is wrong; evidence-based monitoring workspace still lacks metrics and logs proof.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor data platform](https://learn.microsoft.com/en-us/azure/azure-monitor/data-platform)

**Source reviewed:** 2026-08-31

## LAB22-Q22 — B

**Question:** The monitoring administrator building an evidence-based service view must confirm the evidence-based monitoring workspace, without mutation, can interpret a chart only after checking its aggregation and time grain. Which telemetry assessment check qualifies?

- **A — Incorrect.** Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
  Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings. In the evidence-based monitoring workspace, this check observes Log Analytics workspaces. Log Analytics workspaces success in evidence-based monitoring workspace cannot verify metric aggregation and time grain; evidence-based monitoring workspace cannot interpret a chart only after checking its aggregation and time grain until metric aggregation and time grain evidence exists.
- **B — Correct.** Read the metric definition's supported aggregations and compare results at two time grains.
  Read the metric definition's supported aggregations and compare results at two time grains. The evidence-based monitoring workspace reads metric aggregation and time grain directly; that metric aggregation and time grain result proves the evidence-based monitoring workspace can interpret a chart only after checking its aggregation and time grain without another mutation.
- **C — Incorrect.** Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
  Query required agents or settings and verify the insight's underlying metrics or log tables contain data. In the evidence-based monitoring workspace, this check observes Azure Monitor Insights. Evidence-based monitoring workspace could pass Azure Monitor Insights while metric aggregation and time grain is wrong; evidence-based monitoring workspace still lacks metric aggregation and time grain proof.
- **D — Incorrect.** Query the metric namespace and separately confirm expected records reach the Log Analytics table.
  Query the metric namespace and separately confirm expected records reach the Log Analytics table. In the evidence-based monitoring workspace, this check observes metrics and logs. Evidence-based monitoring workspace output covers metrics and logs, not metric aggregation and time grain; the metric aggregation and time grain requirement to interpret a chart only after checking its aggregation and time grain remains unverified.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metrics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/data-platform-metrics)

**Source reviewed:** 2026-08-31

## LAB22-Q23 — A

**Question:** The evidence-based monitoring workspace configuration is complete; the telemetry assessment reviewers need evidence it can send supported resource telemetry to an approved destination. Which observation shows success?

- **A — Correct.** Query logs and metrics selections, destination IDs, and enabled states on the setting.
  For the evidence-based monitoring workspace, this diagnostic setting destinations observation is decisive: query logs and metrics selections, destination IDs, and enabled states on the setting. It is evidence-based monitoring workspace evidence that operators can send supported resource telemetry to an approved destination.
- **B — Incorrect.** Run the query over a known time range and confirm projected columns, grouping, and result count.
  Run the query over a known time range and confirm projected columns, grouping, and result count. In the evidence-based monitoring workspace, this check observes KQL filtering and summarization. Evidence-based monitoring workspace could pass KQL filtering and summarization while diagnostic setting destinations is wrong; evidence-based monitoring workspace still lacks diagnostic setting destinations proof.
- **C — Incorrect.** Query monitor test results and correlate failed checks with network configuration changes.
  Query monitor test results and correlate failed checks with network configuration changes. In the evidence-based monitoring workspace, this check observes Connection Monitor telemetry. Evidence-based monitoring workspace output covers Connection Monitor telemetry, not diagnostic setting destinations; the diagnostic setting destinations requirement to send supported resource telemetry to an approved destination remains unverified.
- **D — Incorrect.** Read the metric definition's supported aggregations and compare results at two time grains.
  Read the metric definition's supported aggregations and compare results at two time grains. In the evidence-based monitoring workspace, this check observes metric aggregation and time grain. Metric aggregation and time grain success in evidence-based monitoring workspace cannot verify diagnostic setting destinations; evidence-based monitoring workspace cannot send supported resource telemetry to an approved destination until diagnostic setting destinations evidence exists.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q24 — D

**Question:** The telemetry assessment validation asks whether the evidence-based monitoring workspace can enable the service-specific log categories required by the query. Which observable state is strongest?

- **A — Incorrect.** Record query time range, retries, and the first matching TimeGenerated value.
  Record query time range, retries, and the first matching TimeGenerated value. In the evidence-based monitoring workspace, this check observes log ingestion latency. Evidence-based monitoring workspace could pass log ingestion latency while resource-specific log categories is wrong; evidence-based monitoring workspace still lacks resource-specific log categories proof.
- **B — Incorrect.** Query daily ingestion, table retention, and enabled categories before and after the change.
  Query daily ingestion, table retention, and enabled categories before and after the change. In the evidence-based monitoring workspace, this check observes monitoring retention and cost. Evidence-based monitoring workspace output covers monitoring retention and cost, not resource-specific log categories; the resource-specific log categories requirement to enable the service-specific log categories required by the query remains unverified.
- **C — Incorrect.** Query logs and metrics selections, destination IDs, and enabled states on the setting.
  Query logs and metrics selections, destination IDs, and enabled states on the setting. In the evidence-based monitoring workspace, this check observes diagnostic setting destinations. Diagnostic setting destinations success in evidence-based monitoring workspace cannot verify resource-specific log categories; evidence-based monitoring workspace cannot enable the service-specific log categories required by the query until resource-specific log categories evidence exists.
- **D — Correct.** Query diagnostic-settings categories and match configured categories against the returned list.
  Query diagnostic-settings categories and match configured categories against the returned list. Because the evidence-based monitoring workspace check observes resource-specific log categories, it independently verifies the requirement to enable the service-specific log categories required by the query.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q25 — D

**Question:** An evidence-based monitoring workspace review must prove the telemetry assessment ability to store and query records from several monitored resources in one boundary. Which check avoids an adjacent feature?

- **A — Incorrect.** Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
  Query required agents or settings and verify the insight's underlying metrics or log tables contain data. In the evidence-based monitoring workspace, this check observes Azure Monitor Insights. Evidence-based monitoring workspace output covers Azure Monitor Insights, not Log Analytics workspaces; the Log Analytics workspaces requirement to store and query records from several monitored resources in one boundary remains unverified.
- **B — Incorrect.** Query the metric namespace and separately confirm expected records reach the Log Analytics table.
  Query the metric namespace and separately confirm expected records reach the Log Analytics table. In the evidence-based monitoring workspace, this check observes metrics and logs. Metrics and logs success in evidence-based monitoring workspace cannot verify Log Analytics workspaces; evidence-based monitoring workspace cannot store and query records from several monitored resources in one boundary until Log Analytics workspaces evidence exists.
- **C — Incorrect.** Query diagnostic-settings categories and match configured categories against the returned list.
  Query diagnostic-settings categories and match configured categories against the returned list. In the evidence-based monitoring workspace, this check observes resource-specific log categories. Evidence-based monitoring workspace reads resource-specific log categories, leaving Log Analytics workspaces unproved in evidence-based monitoring workspace; evidence-based monitoring workspace still has no Log Analytics workspaces proof.
- **D — Correct.** Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
  The evidence-based monitoring workspace validator needs this Log Analytics workspaces result: query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings. It proves the outcome to store and query records from several monitored resources in one boundary rather than an adjacent checkpoint.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Log Analytics workspace overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q26 — B

**Question:** The evidence-based monitoring workspace evidence bundle needs a telemetry assessment result showing it can filter records and calculate a grouped summary with KQL. Which result belongs in the checkpoint?

- **A — Incorrect.** Query monitor test results and correlate failed checks with network configuration changes.
  Query monitor test results and correlate failed checks with network configuration changes. In the evidence-based monitoring workspace, this check observes Connection Monitor telemetry. Connection Monitor telemetry success in evidence-based monitoring workspace cannot verify KQL filtering and summarization; evidence-based monitoring workspace cannot filter records and calculate a grouped summary with KQL until KQL filtering and summarization evidence exists.
- **B — Correct.** Run the query over a known time range and confirm projected columns, grouping, and result count.
  Run the query over a known time range and confirm projected columns, grouping, and result count. This is independent KQL filtering and summarization evidence for the evidence-based monitoring workspace, even if evidence-based monitoring workspace setup reports success before KQL filtering and summarization becomes observable.
- **C — Incorrect.** Read the metric definition's supported aggregations and compare results at two time grains.
  Read the metric definition's supported aggregations and compare results at two time grains. In the evidence-based monitoring workspace, this check observes metric aggregation and time grain. Evidence-based monitoring workspace could pass metric aggregation and time grain while KQL filtering and summarization is wrong; evidence-based monitoring workspace still lacks KQL filtering and summarization proof.
- **D — Incorrect.** Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
  Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings. In the evidence-based monitoring workspace, this check observes Log Analytics workspaces. Evidence-based monitoring workspace output covers Log Analytics workspaces, not KQL filtering and summarization; the KQL filtering and summarization requirement to filter records and calculate a grouped summary with KQL remains unverified.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Log queries in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q27 — A

**Question:** Before evidence-based monitoring workspace cleanup, the telemetry assessment team must reconfirm it can allow for collection and processing delay before declaring telemetry missing. Which read-only inspection should run?

- **A — Correct.** Record query time range, retries, and the first matching TimeGenerated value.
  Record query time range, retries, and the first matching TimeGenerated value. For evidence-based monitoring workspace, this log ingestion latency read confirms the service can allow for collection and processing delay before declaring telemetry missing.
- **B — Incorrect.** Query daily ingestion, table retention, and enabled categories before and after the change.
  Query daily ingestion, table retention, and enabled categories before and after the change. In the evidence-based monitoring workspace, this check observes monitoring retention and cost. Evidence-based monitoring workspace could pass monitoring retention and cost while log ingestion latency is wrong; evidence-based monitoring workspace still lacks log ingestion latency proof.
- **C — Incorrect.** Query logs and metrics selections, destination IDs, and enabled states on the setting.
  Query logs and metrics selections, destination IDs, and enabled states on the setting. In the evidence-based monitoring workspace, this check observes diagnostic setting destinations. Evidence-based monitoring workspace output covers diagnostic setting destinations, not log ingestion latency; the log ingestion latency requirement to allow for collection and processing delay before declaring telemetry missing remains unverified.
- **D — Incorrect.** Run the query over a known time range and confirm projected columns, grouping, and result count.
  Run the query over a known time range and confirm projected columns, grouping, and result count. In the evidence-based monitoring workspace, this check observes KQL filtering and summarization. KQL filtering and summarization success in evidence-based monitoring workspace cannot verify log ingestion latency; evidence-based monitoring workspace cannot allow for collection and processing delay before declaring telemetry missing until log ingestion latency evidence exists.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Log data ingestion time in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-ingestion-time)

**Source reviewed:** 2026-08-31

## LAB22-Q28 — C

**Question:** The evidence-based monitoring workspace setup reports success after the telemetry assessment attempt to use a curated service view backed by the required monitoring data. Which telemetry assessment read-only observation proves the evidence-based monitoring workspace outcome?

- **A — Incorrect.** Query the metric namespace and separately confirm expected records reach the Log Analytics table.
  Query the metric namespace and separately confirm expected records reach the Log Analytics table. In the evidence-based monitoring workspace, this check observes metrics and logs. Evidence-based monitoring workspace could pass metrics and logs while Azure Monitor Insights is wrong; evidence-based monitoring workspace still lacks Azure Monitor Insights proof.
- **B — Incorrect.** Query diagnostic-settings categories and match configured categories against the returned list.
  Query diagnostic-settings categories and match configured categories against the returned list. In the evidence-based monitoring workspace, this check observes resource-specific log categories. Evidence-based monitoring workspace output covers resource-specific log categories, not Azure Monitor Insights; the Azure Monitor Insights requirement to use a curated service view backed by the required monitoring data remains unverified.
- **C — Correct.** Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
  Query required agents or settings and verify the insight's underlying metrics or log tables contain data. The evidence-based monitoring workspace reads Azure Monitor Insights directly; that Azure Monitor Insights result proves the evidence-based monitoring workspace can use a curated service view backed by the required monitoring data without another mutation.
- **D — Incorrect.** Record query time range, retries, and the first matching TimeGenerated value.
  Record query time range, retries, and the first matching TimeGenerated value. In the evidence-based monitoring workspace, this check observes log ingestion latency. Evidence-based monitoring workspace reads log ingestion latency, leaving Azure Monitor Insights unproved in evidence-based monitoring workspace; evidence-based monitoring workspace still has no Azure Monitor Insights proof.

**Objectives:** `MR-MONITOR-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Insights and curated visualizations in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q29 — D

**Question:** The telemetry assessment log says the evidence-based monitoring workspace can now bring continuous network-test telemetry into the monitoring workflow. Which telemetry assessment state should the evidence-based monitoring workspace acceptance test retain?

- **A — Incorrect.** Read the metric definition's supported aggregations and compare results at two time grains.
  Read the metric definition's supported aggregations and compare results at two time grains. In the evidence-based monitoring workspace, this check observes metric aggregation and time grain. Evidence-based monitoring workspace output covers metric aggregation and time grain, not Connection Monitor telemetry; the Connection Monitor telemetry requirement to bring continuous network-test telemetry into the monitoring workflow remains unverified.
- **B — Incorrect.** Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
  Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings. In the evidence-based monitoring workspace, this check observes Log Analytics workspaces. Log Analytics workspaces success in evidence-based monitoring workspace cannot verify Connection Monitor telemetry; evidence-based monitoring workspace cannot bring continuous network-test telemetry into the monitoring workflow until Connection Monitor telemetry evidence exists.
- **C — Incorrect.** Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
  Query required agents or settings and verify the insight's underlying metrics or log tables contain data. In the evidence-based monitoring workspace, this check observes Azure Monitor Insights. Evidence-based monitoring workspace reads Azure Monitor Insights, leaving Connection Monitor telemetry unproved in evidence-based monitoring workspace; evidence-based monitoring workspace still has no Connection Monitor telemetry proof.
- **D — Correct.** Query monitor test results and correlate failed checks with network configuration changes.
  For the evidence-based monitoring workspace, this Connection Monitor telemetry observation is decisive: query monitor test results and correlate failed checks with network configuration changes. It is evidence-based monitoring workspace evidence that operators can bring continuous network-test telemetry into the monitoring workflow.

**Objectives:** `MR-MONITOR-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q30 — B

**Question:** The evidence-based monitoring workspace rejects telemetry assessment exit status as proof it can control retention and ingestion volume before monitoring cost grows unexpectedly. Which evidence-based monitoring workspace result is valid evidence?

- **A — Incorrect.** Query logs and metrics selections, destination IDs, and enabled states on the setting.
  Query logs and metrics selections, destination IDs, and enabled states on the setting. In the evidence-based monitoring workspace, this check observes diagnostic setting destinations. Diagnostic setting destinations success in evidence-based monitoring workspace cannot verify monitoring retention and cost; evidence-based monitoring workspace cannot control retention and ingestion volume before monitoring cost grows unexpectedly until monitoring retention and cost evidence exists.
- **B — Correct.** Query daily ingestion, table retention, and enabled categories before and after the change.
  Query daily ingestion, table retention, and enabled categories before and after the change. Because the evidence-based monitoring workspace check observes monitoring retention and cost, it independently verifies the requirement to control retention and ingestion volume before monitoring cost grows unexpectedly.
- **C — Incorrect.** Run the query over a known time range and confirm projected columns, grouping, and result count.
  Run the query over a known time range and confirm projected columns, grouping, and result count. In the evidence-based monitoring workspace, this check observes KQL filtering and summarization. Evidence-based monitoring workspace could pass KQL filtering and summarization while monitoring retention and cost is wrong; evidence-based monitoring workspace still lacks monitoring retention and cost proof.
- **D — Incorrect.** Query monitor test results and correlate failed checks with network configuration changes.
  Query monitor test results and correlate failed checks with network configuration changes. In the evidence-based monitoring workspace, this check observes Connection Monitor telemetry. Evidence-based monitoring workspace output covers Connection Monitor telemetry, not monitoring retention and cost; the monitoring retention and cost requirement to control retention and ingestion volume before monitoring cost grows unexpectedly remains unverified.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor Logs cost calculations and options](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs)

**Source reviewed:** 2026-08-31

## LAB22-Q31 — A

**Question:** The evidence-based monitoring workspace troubleshooting scope is the telemetry assessment need to decide whether a measurement belongs in metrics or queryable events. Which condition should be corrected first?

- **A — Correct.** The runbook expects a platform metric query to return individual activity-log records.
  The evidence-based monitoring workspace cannot decide whether a measurement belongs in metrics or queryable events because of this metrics and logs defect: the runbook expects a platform metric query to return individual activity-log records. The symptom and repair align.
- **B — Incorrect.** An average aggregation hides a short maximum spike that triggered the incident.
  An average aggregation hides a short maximum spike that triggered the incident. The evidence-based monitoring workspace fault concerns metric aggregation and time grain. Evidence-based monitoring workspace could repair metric aggregation and time grain while metrics and logs stays broken in evidence-based monitoring workspace; the evidence-based monitoring workspace remains unable to decide whether a measurement belongs in metrics or queryable events.
- **C — Incorrect.** The time filter excludes the interval when the test event occurred.
  The time filter excludes the interval when the test event occurred. The evidence-based monitoring workspace fault concerns KQL filtering and summarization. Evidence-based monitoring workspace failed on metrics and logs; this KQL filtering and summarization finding redirects evidence-based monitoring workspace remediation away from metrics and logs.
- **D — Incorrect.** Verbose categories were enabled globally without a retention or cost review.
  Verbose categories were enabled globally without a retention or cost review. The evidence-based monitoring workspace fault concerns monitoring retention and cost. Evidence-based monitoring workspace may fix monitoring retention and cost, yet metrics and logs still fails; this evidence-based monitoring workspace diagnosis of monitoring retention and cost is wrong for metrics and logs.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor data platform](https://learn.microsoft.com/en-us/azure/azure-monitor/data-platform)

**Source reviewed:** 2026-08-31

## LAB22-Q32 — B

**Question:** The evidence-based monitoring workspace result is partial because the telemetry assessment cannot interpret a chart only after checking its aggregation and time grain. Which condition accounts for that result?

- **A — Incorrect.** The setting exists but no resource-log category is enabled.
  The setting exists but no resource-log category is enabled. The evidence-based monitoring workspace fault concerns diagnostic setting destinations. Evidence-based monitoring workspace could repair diagnostic setting destinations while metric aggregation and time grain stays broken in evidence-based monitoring workspace; the evidence-based monitoring workspace remains unable to interpret a chart only after checking its aggregation and time grain.
- **B — Correct.** An average aggregation hides a short maximum spike that triggered the incident.
  An average aggregation hides a short maximum spike that triggered the incident. Removing this metric aggregation and time grain condition lets the evidence-based monitoring workspace interpret a chart only after checking its aggregation and time grain while leaving healthy controls unchanged.
- **C — Incorrect.** Validation queried only once before the test record completed ingestion.
  Validation queried only once before the test record completed ingestion. The evidence-based monitoring workspace fault concerns log ingestion latency. Evidence-based monitoring workspace may fix log ingestion latency, yet metric aggregation and time grain still fails; this evidence-based monitoring workspace diagnosis of log ingestion latency is wrong for metric aggregation and time grain.
- **D — Incorrect.** The runbook expects a platform metric query to return individual activity-log records.
  The runbook expects a platform metric query to return individual activity-log records. The evidence-based monitoring workspace fault concerns metrics and logs. Evidence-based monitoring workspace has metrics and logs impact, but metric aggregation and time grain is the evidence-based monitoring workspace failed path; the metrics and logs state cannot produce metric aggregation and time grain failure.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metrics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/data-platform-metrics)

**Source reviewed:** 2026-08-31

## LAB22-Q33 — C

**Question:** The telemetry assessment evidence shows the evidence-based monitoring workspace cannot send supported resource telemetry to an approved destination. Which root cause fits that evidence?

- **A — Incorrect.** The template specifies a category name that the target resource does not expose.
  The template specifies a category name that the target resource does not expose. The evidence-based monitoring workspace fault concerns resource-specific log categories. Evidence-based monitoring workspace failed on diagnostic setting destinations; this resource-specific log categories finding redirects evidence-based monitoring workspace remediation away from diagnostic setting destinations.
- **B — Incorrect.** The insight is opened before its required monitoring agent or data collection rule is associated.
  The insight is opened before its required monitoring agent or data collection rule is associated. The evidence-based monitoring workspace fault concerns Azure Monitor Insights. Evidence-based monitoring workspace may fix Azure Monitor Insights, yet diagnostic setting destinations still fails; this evidence-based monitoring workspace diagnosis of Azure Monitor Insights is wrong for diagnostic setting destinations.
- **C — Correct.** The setting exists but no resource-log category is enabled.
  The setting exists but no resource-log category is enabled. In evidence-based monitoring workspace, this diagnostic setting destinations cause matches the failure to send supported resource telemetry to an approved destination.
- **D — Incorrect.** An average aggregation hides a short maximum spike that triggered the incident.
  An average aggregation hides a short maximum spike that triggered the incident. The evidence-based monitoring workspace fault concerns metric aggregation and time grain. Evidence-based monitoring workspace could repair metric aggregation and time grain while diagnostic setting destinations stays broken in evidence-based monitoring workspace; the evidence-based monitoring workspace remains unable to send supported resource telemetry to an approved destination.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q34 — C

**Question:** Although the evidence-based monitoring workspace is meant to let the telemetry assessment enable the service-specific log categories required by the query, its checkpoint fails. Which telemetry assessment defect explains the failure?

- **A — Incorrect.** The diagnostic setting sends data to a different workspace than the one queried during validation.
  The diagnostic setting sends data to a different workspace than the one queried during validation. The evidence-based monitoring workspace fault concerns Log Analytics workspaces. Evidence-based monitoring workspace may fix Log Analytics workspaces, yet resource-specific log categories still fails; this evidence-based monitoring workspace diagnosis of Log Analytics workspaces is wrong for resource-specific log categories.
- **B — Incorrect.** The chosen source endpoint cannot run the configured connection test.
  The chosen source endpoint cannot run the configured connection test. The evidence-based monitoring workspace fault concerns Connection Monitor telemetry. Evidence-based monitoring workspace has Connection Monitor telemetry impact, but resource-specific log categories is the evidence-based monitoring workspace failed path; the Connection Monitor telemetry state cannot produce resource-specific log categories failure.
- **C — Correct.** The template specifies a category name that the target resource does not expose.
  The template specifies a category name that the target resource does not expose. This evidence-based monitoring workspace condition breaks resource-specific log categories, explaining why operators cannot enable the service-specific log categories required by the query.
- **D — Incorrect.** The setting exists but no resource-log category is enabled.
  The setting exists but no resource-log category is enabled. The evidence-based monitoring workspace fault concerns diagnostic setting destinations. Evidence-based monitoring workspace failed on resource-specific log categories; this diagnostic setting destinations finding redirects evidence-based monitoring workspace remediation away from resource-specific log categories.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q35 — A

**Question:** The telemetry assessment support team isolated the evidence-based monitoring workspace incident to the attempt to store and query records from several monitored resources in one boundary. Which condition prevents success?

- **A — Correct.** The diagnostic setting sends data to a different workspace than the one queried during validation.
  For the evidence-based monitoring workspace, the Log Analytics workspaces failure is causal: the diagnostic setting sends data to a different workspace than the one queried during validation. Correcting it restores the ability to store and query records from several monitored resources in one boundary.
- **B — Incorrect.** The time filter excludes the interval when the test event occurred.
  The time filter excludes the interval when the test event occurred. The evidence-based monitoring workspace fault concerns KQL filtering and summarization. Evidence-based monitoring workspace could repair KQL filtering and summarization while Log Analytics workspaces stays broken in evidence-based monitoring workspace; the evidence-based monitoring workspace remains unable to store and query records from several monitored resources in one boundary.
- **C — Incorrect.** Verbose categories were enabled globally without a retention or cost review.
  Verbose categories were enabled globally without a retention or cost review. The evidence-based monitoring workspace fault concerns monitoring retention and cost. Evidence-based monitoring workspace failed on Log Analytics workspaces; this monitoring retention and cost finding redirects evidence-based monitoring workspace remediation away from Log Analytics workspaces.
- **D — Incorrect.** The template specifies a category name that the target resource does not expose.
  The template specifies a category name that the target resource does not expose. The evidence-based monitoring workspace fault concerns resource-specific log categories. Evidence-based monitoring workspace may fix resource-specific log categories, yet Log Analytics workspaces still fails; this evidence-based monitoring workspace diagnosis of resource-specific log categories is wrong for Log Analytics workspaces.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Log Analytics workspace overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q36 — A

**Question:** An evidence-based monitoring workspace query surprises the monitoring administrator building an evidence-based service view during the telemetry assessment attempt to filter records and calculate a grouped summary with KQL. Which finding explains it?

- **A — Correct.** The time filter excludes the interval when the test event occurred.
  The time filter excludes the interval when the test event occurred. The finding is specific to KQL filtering and summarization in the evidence-based monitoring workspace; repairing KQL filtering and summarization restores the evidence-based monitoring workspace ability to filter records and calculate a grouped summary with KQL.
- **B — Incorrect.** Validation queried only once before the test record completed ingestion.
  Validation queried only once before the test record completed ingestion. The evidence-based monitoring workspace fault concerns log ingestion latency. Evidence-based monitoring workspace failed on KQL filtering and summarization; this log ingestion latency finding redirects evidence-based monitoring workspace remediation away from KQL filtering and summarization.
- **C — Incorrect.** The runbook expects a platform metric query to return individual activity-log records.
  The runbook expects a platform metric query to return individual activity-log records. The evidence-based monitoring workspace fault concerns metrics and logs. Evidence-based monitoring workspace may fix metrics and logs, yet KQL filtering and summarization still fails; this evidence-based monitoring workspace diagnosis of metrics and logs is wrong for KQL filtering and summarization.
- **D — Incorrect.** The diagnostic setting sends data to a different workspace than the one queried during validation.
  The diagnostic setting sends data to a different workspace than the one queried during validation. The evidence-based monitoring workspace fault concerns Log Analytics workspaces. Evidence-based monitoring workspace has Log Analytics workspaces impact, but KQL filtering and summarization is the evidence-based monitoring workspace failed path; the Log Analytics workspaces state cannot produce KQL filtering and summarization failure.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Log queries in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q37 — B

**Question:** Other evidence-based monitoring workspace components are healthy, but the telemetry assessment still cannot allow for collection and processing delay before declaring telemetry missing. Which state causes the isolated failure?

- **A — Incorrect.** The insight is opened before its required monitoring agent or data collection rule is associated.
  The insight is opened before its required monitoring agent or data collection rule is associated. The evidence-based monitoring workspace fault concerns Azure Monitor Insights. Evidence-based monitoring workspace failed on log ingestion latency; this Azure Monitor Insights finding redirects evidence-based monitoring workspace remediation away from log ingestion latency.
- **B — Correct.** Validation queried only once before the test record completed ingestion.
  The evidence-based monitoring workspace cannot allow for collection and processing delay before declaring telemetry missing because of this log ingestion latency defect: validation queried only once before the test record completed ingestion. The symptom and repair align.
- **C — Incorrect.** An average aggregation hides a short maximum spike that triggered the incident.
  An average aggregation hides a short maximum spike that triggered the incident. The evidence-based monitoring workspace fault concerns metric aggregation and time grain. Evidence-based monitoring workspace has metric aggregation and time grain impact, but log ingestion latency is the evidence-based monitoring workspace failed path; the metric aggregation and time grain state cannot produce log ingestion latency failure.
- **D — Incorrect.** The time filter excludes the interval when the test event occurred.
  The time filter excludes the interval when the test event occurred. The evidence-based monitoring workspace fault concerns KQL filtering and summarization. Evidence-based monitoring workspace could repair KQL filtering and summarization while log ingestion latency stays broken in evidence-based monitoring workspace; the evidence-based monitoring workspace remains unable to allow for collection and processing delay before declaring telemetry missing.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Log data ingestion time in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-ingestion-time)

**Source reviewed:** 2026-08-31

## LAB22-Q38 — A

**Question:** During a telemetry assessment fault drill, the evidence-based monitoring workspace does not use a curated service view backed by the required monitoring data. Which finding identifies the defect?

- **A — Correct.** The insight is opened before its required monitoring agent or data collection rule is associated.
  The insight is opened before its required monitoring agent or data collection rule is associated. Removing this Azure Monitor Insights condition lets the evidence-based monitoring workspace use a curated service view backed by the required monitoring data while leaving healthy controls unchanged.
- **B — Incorrect.** The chosen source endpoint cannot run the configured connection test.
  The chosen source endpoint cannot run the configured connection test. The evidence-based monitoring workspace fault concerns Connection Monitor telemetry. Evidence-based monitoring workspace has Connection Monitor telemetry impact, but Azure Monitor Insights is the evidence-based monitoring workspace failed path; the Connection Monitor telemetry state cannot produce Azure Monitor Insights failure.
- **C — Incorrect.** The setting exists but no resource-log category is enabled.
  The setting exists but no resource-log category is enabled. The evidence-based monitoring workspace fault concerns diagnostic setting destinations. Evidence-based monitoring workspace could repair diagnostic setting destinations while Azure Monitor Insights stays broken in evidence-based monitoring workspace; the evidence-based monitoring workspace remains unable to use a curated service view backed by the required monitoring data.
- **D — Incorrect.** Validation queried only once before the test record completed ingestion.
  Validation queried only once before the test record completed ingestion. The evidence-based monitoring workspace fault concerns log ingestion latency. Evidence-based monitoring workspace failed on Azure Monitor Insights; this log ingestion latency finding redirects evidence-based monitoring workspace remediation away from Azure Monitor Insights.

**Objectives:** `MR-MONITOR-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Insights and curated visualizations in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q39 — A

**Question:** The evidence-based monitoring workspace setup finishes, yet the telemetry assessment cannot bring continuous network-test telemetry into the monitoring workflow. Which misconfiguration explains the mismatch?

- **A — Correct.** The chosen source endpoint cannot run the configured connection test.
  The chosen source endpoint cannot run the configured connection test. In evidence-based monitoring workspace, this Connection Monitor telemetry cause matches the failure to bring continuous network-test telemetry into the monitoring workflow.
- **B — Incorrect.** Verbose categories were enabled globally without a retention or cost review.
  Verbose categories were enabled globally without a retention or cost review. The evidence-based monitoring workspace fault concerns monitoring retention and cost. Evidence-based monitoring workspace could repair monitoring retention and cost while Connection Monitor telemetry stays broken in evidence-based monitoring workspace; the evidence-based monitoring workspace remains unable to bring continuous network-test telemetry into the monitoring workflow.
- **C — Incorrect.** The template specifies a category name that the target resource does not expose.
  The template specifies a category name that the target resource does not expose. The evidence-based monitoring workspace fault concerns resource-specific log categories. Evidence-based monitoring workspace failed on Connection Monitor telemetry; this resource-specific log categories finding redirects evidence-based monitoring workspace remediation away from Connection Monitor telemetry.
- **D — Incorrect.** The insight is opened before its required monitoring agent or data collection rule is associated.
  The insight is opened before its required monitoring agent or data collection rule is associated. The evidence-based monitoring workspace fault concerns Azure Monitor Insights. Evidence-based monitoring workspace may fix Azure Monitor Insights, yet Connection Monitor telemetry still fails; this evidence-based monitoring workspace diagnosis of Azure Monitor Insights is wrong for Connection Monitor telemetry.

**Objectives:** `MR-MONITOR-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q40 — B

**Question:** A telemetry assessment break/fix in the evidence-based monitoring workspace fails when operators try to control retention and ingestion volume before monitoring cost grows unexpectedly. Which diagnosis fits?

- **A — Incorrect.** The runbook expects a platform metric query to return individual activity-log records.
  The runbook expects a platform metric query to return individual activity-log records. The evidence-based monitoring workspace fault concerns metrics and logs. Evidence-based monitoring workspace could repair metrics and logs while monitoring retention and cost stays broken in evidence-based monitoring workspace; the evidence-based monitoring workspace remains unable to control retention and ingestion volume before monitoring cost grows unexpectedly.
- **B — Correct.** Verbose categories were enabled globally without a retention or cost review.
  Verbose categories were enabled globally without a retention or cost review. This evidence-based monitoring workspace condition breaks monitoring retention and cost, explaining why operators cannot control retention and ingestion volume before monitoring cost grows unexpectedly.
- **C — Incorrect.** The diagnostic setting sends data to a different workspace than the one queried during validation.
  The diagnostic setting sends data to a different workspace than the one queried during validation. The evidence-based monitoring workspace fault concerns Log Analytics workspaces. Evidence-based monitoring workspace may fix Log Analytics workspaces, yet monitoring retention and cost still fails; this evidence-based monitoring workspace diagnosis of Log Analytics workspaces is wrong for monitoring retention and cost.
- **D — Incorrect.** The chosen source endpoint cannot run the configured connection test.
  The chosen source endpoint cannot run the configured connection test. The evidence-based monitoring workspace fault concerns Connection Monitor telemetry. Evidence-based monitoring workspace has Connection Monitor telemetry impact, but monitoring retention and cost is the evidence-based monitoring workspace failed path; the Connection Monitor telemetry state cannot produce monitoring retention and cost failure.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor Logs cost calculations and options](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs)

**Source reviewed:** 2026-08-31

## LAB22-Q41 — D

**Question:** The evidence-based monitoring workspace has two telemetry assessment gates: decide whether a measurement belongs in metrics or queryable events, then prove the evidence-based monitoring workspace state. Which telemetry assessment sequence works?

- **A — Incorrect.** First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.
  First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting. This evidence-based monitoring workspace pair serves diagnostic setting destinations. Diagnostic setting destinations cannot replace metrics and logs in evidence-based monitoring workspace. Use this metrics and logs pair instead: First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.
- **B — Incorrect.** First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
  First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value. This evidence-based monitoring workspace pair serves log ingestion latency. Evidence-based monitoring workspace proves log ingestion latency, but metrics and logs lacks implementation in evidence-based monitoring workspace and metrics and logs proof; the metrics and logs outcome to decide whether a measurement belongs in metrics or queryable events remains open.
- **C — Incorrect.** First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
  First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data. This evidence-based monitoring workspace pair serves Azure Monitor Insights. Evidence-based monitoring workspace uses Azure Monitor Insights for both steps; metrics and logs remains untouched in evidence-based monitoring workspace, so its metrics and logs gate to decide whether a measurement belongs in metrics or queryable events fails.
- **D — Correct.** First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.
  For the evidence-based monitoring workspace, the safe metrics and logs order is: first, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table. The evidence-based monitoring workspace records metrics and logs proof after configuration.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Azure Monitor data platform](https://learn.microsoft.com/en-us/azure/azure-monitor/data-platform)

**Source reviewed:** 2026-08-31

## LAB22-Q42 — C

**Question:** Which telemetry assessment path makes the evidence-based monitoring workspace able to interpret a chart only after checking its aggregation and time grain, then inspects the defining properties?

- **A — Incorrect.** First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list.
  First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list. This evidence-based monitoring workspace pair serves resource-specific log categories. Evidence-based monitoring workspace proves resource-specific log categories, but metric aggregation and time grain lacks implementation in evidence-based monitoring workspace and metric aggregation and time grain proof; the metric aggregation and time grain outcome to interpret a chart only after checking its aggregation and time grain remains open.
- **B — Incorrect.** First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
  First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data. This evidence-based monitoring workspace pair serves Azure Monitor Insights. Evidence-based monitoring workspace uses Azure Monitor Insights for both steps; metric aggregation and time grain remains untouched in evidence-based monitoring workspace, so its metric aggregation and time grain gate to interpret a chart only after checking its aggregation and time grain fails.
- **C — Correct.** First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.
  First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains. The evidence-based monitoring workspace uses its metric aggregation and time grain mutation gate and metric aggregation and time grain verification gate before it can interpret a chart only after checking its aggregation and time grain.
- **D — Incorrect.** First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.
  First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes. This evidence-based monitoring workspace pair serves Connection Monitor telemetry. Connection Monitor telemetry cannot replace metric aggregation and time grain in evidence-based monitoring workspace. Use this metric aggregation and time grain pair instead: First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.

**Objectives:** `MR-MONITOR-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Azure Monitor metrics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/data-platform-metrics)

**Source reviewed:** 2026-08-31

## LAB22-Q43 — A

**Question:** At the evidence-based monitoring workspace approval gate, operators must show that the telemetry assessment can send supported resource telemetry to an approved destination. Which telemetry assessment configure-and-check pair is defensible?

- **A — Correct.** First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.
  The evidence-based monitoring workspace gets a complete diagnostic setting destinations sequence here: first, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting. Read-back evidence follows the change.
- **B — Incorrect.** First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
  First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings. This evidence-based monitoring workspace pair serves Log Analytics workspaces. Evidence-based monitoring workspace closes Log Analytics workspaces, not diagnostic setting destinations; without the diagnostic setting destinations workflow, it cannot send supported resource telemetry to an approved destination.
- **C — Incorrect.** First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.
  First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes. This evidence-based monitoring workspace pair serves Connection Monitor telemetry. Connection Monitor telemetry cannot replace diagnostic setting destinations in evidence-based monitoring workspace. Use this diagnostic setting destinations pair instead: First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.
- **D — Incorrect.** First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change.
  First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change. This evidence-based monitoring workspace pair serves monitoring retention and cost. Evidence-based monitoring workspace proves monitoring retention and cost, but diagnostic setting destinations lacks implementation in evidence-based monitoring workspace and diagnostic setting destinations proof; the diagnostic setting destinations outcome to send supported resource telemetry to an approved destination remains open.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q44 — B

**Question:** The evidence-based monitoring workspace forbids a partial telemetry assessment result. Operators must first enable the service-specific log categories required by the query and afterward confirm the evidence-based monitoring workspace outcome. Which telemetry assessment sequence is complete?

- **A — Incorrect.** First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.
  First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count. This evidence-based monitoring workspace pair serves KQL filtering and summarization. Evidence-based monitoring workspace closes KQL filtering and summarization, not resource-specific log categories; without the resource-specific log categories workflow, it cannot enable the service-specific log categories required by the query.
- **B — Correct.** First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list.
  First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list. This ordered resource-specific log categories workflow lets the evidence-based monitoring workspace enable the service-specific log categories required by the query and then verify the resulting state.
- **C — Incorrect.** First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change.
  First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change. This evidence-based monitoring workspace pair serves monitoring retention and cost. Evidence-based monitoring workspace proves monitoring retention and cost, but resource-specific log categories lacks implementation in evidence-based monitoring workspace and resource-specific log categories proof; the resource-specific log categories outcome to enable the service-specific log categories required by the query remains open.
- **D — Incorrect.** First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.
  First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table. This evidence-based monitoring workspace pair serves metrics and logs. Evidence-based monitoring workspace uses metrics and logs for both steps; resource-specific log categories remains untouched in evidence-based monitoring workspace, so its resource-specific log categories gate to enable the service-specific log categories required by the query fails.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)

**Source reviewed:** 2026-08-31

## LAB22-Q45 — D

**Question:** Only the evidence-based monitoring workspace change needed to store and query records from several monitored resources in one boundary is allowed, and telemetry assessment proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
  First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value. This evidence-based monitoring workspace pair serves log ingestion latency. Log ingestion latency cannot replace Log Analytics workspaces in evidence-based monitoring workspace. Use this Log Analytics workspaces pair instead: First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
- **B — Incorrect.** First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.
  First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table. This evidence-based monitoring workspace pair serves metrics and logs. Evidence-based monitoring workspace proves metrics and logs, but Log Analytics workspaces lacks implementation in evidence-based monitoring workspace and Log Analytics workspaces proof; the Log Analytics workspaces outcome to store and query records from several monitored resources in one boundary remains open.
- **C — Incorrect.** First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.
  First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains. This evidence-based monitoring workspace pair serves metric aggregation and time grain. Evidence-based monitoring workspace uses metric aggregation and time grain for both steps; Log Analytics workspaces remains untouched in evidence-based monitoring workspace, so its Log Analytics workspaces gate to store and query records from several monitored resources in one boundary fails.
- **D — Correct.** First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
  First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings. For evidence-based monitoring workspace, the Log Analytics workspaces operation precedes its Log Analytics workspaces read-back check, allowing it to store and query records from several monitored resources in one boundary.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Log Analytics workspace overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q46 — C

**Question:** The evidence-based monitoring workspace runbook separates telemetry assessment mutation from validation while it must filter records and calculate a grouped summary with KQL. Which sequence proves it cleanly?

- **A — Incorrect.** First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
  First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data. This evidence-based monitoring workspace pair serves Azure Monitor Insights. Evidence-based monitoring workspace proves Azure Monitor Insights, but KQL filtering and summarization lacks implementation in evidence-based monitoring workspace and KQL filtering and summarization proof; the KQL filtering and summarization outcome to filter records and calculate a grouped summary with KQL remains open.
- **B — Incorrect.** First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.
  First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains. This evidence-based monitoring workspace pair serves metric aggregation and time grain. Evidence-based monitoring workspace uses metric aggregation and time grain for both steps; KQL filtering and summarization remains untouched in evidence-based monitoring workspace, so its KQL filtering and summarization gate to filter records and calculate a grouped summary with KQL fails.
- **C — Correct.** First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.
  First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count. In the evidence-based monitoring workspace, the first KQL filtering and summarization step runs; the evidence-based monitoring workspace then reads KQL filtering and summarization state to prove it can filter records and calculate a grouped summary with KQL.
- **D — Incorrect.** First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.
  First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting. This evidence-based monitoring workspace pair serves diagnostic setting destinations. Diagnostic setting destinations cannot replace KQL filtering and summarization in evidence-based monitoring workspace. Use this KQL filtering and summarization pair instead: First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB22-CP01`).

**Microsoft Learn sources:**

- [Log queries in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q47 — A

**Question:** The evidence-based monitoring workspace checkpoint requires both this telemetry assessment outcome—allow for collection and processing delay before declaring telemetry missing—and a read-only evidence-based monitoring workspace state check. Which telemetry assessment response is complete?

- **A — Correct.** First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
  For the evidence-based monitoring workspace, the safe log ingestion latency order is: first, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value. The evidence-based monitoring workspace records log ingestion latency proof after configuration.
- **B — Incorrect.** First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.
  First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes. This evidence-based monitoring workspace pair serves Connection Monitor telemetry. Evidence-based monitoring workspace closes Connection Monitor telemetry, not log ingestion latency; without the log ingestion latency workflow, it cannot allow for collection and processing delay before declaring telemetry missing.
- **C — Incorrect.** First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.
  First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting. This evidence-based monitoring workspace pair serves diagnostic setting destinations. Diagnostic setting destinations cannot replace log ingestion latency in evidence-based monitoring workspace. Use this log ingestion latency pair instead: First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
- **D — Incorrect.** First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list.
  First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list. This evidence-based monitoring workspace pair serves resource-specific log categories. Evidence-based monitoring workspace proves resource-specific log categories, but log ingestion latency lacks implementation in evidence-based monitoring workspace and log ingestion latency proof; the log ingestion latency outcome to allow for collection and processing delay before declaring telemetry missing remains open.

**Objectives:** `MR-MONITOR-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB22-CP02`).

**Microsoft Learn sources:**

- [Log data ingestion time in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-ingestion-time)

**Source reviewed:** 2026-08-31

## LAB22-Q48 — B

**Question:** The evidence-based monitoring workspace runbook must use a curated service view backed by the required monitoring data, then retain telemetry assessment read-back evidence. Which evidence-based monitoring workspace pair completes both duties?

- **A — Incorrect.** First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change.
  First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change. This evidence-based monitoring workspace pair serves monitoring retention and cost. Evidence-based monitoring workspace closes monitoring retention and cost, not Azure Monitor Insights; without the Azure Monitor Insights workflow, it cannot use a curated service view backed by the required monitoring data.
- **B — Correct.** First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
  First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data. The evidence-based monitoring workspace uses its Azure Monitor Insights mutation gate and Azure Monitor Insights verification gate before it can use a curated service view backed by the required monitoring data.
- **C — Incorrect.** First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list.
  First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list. This evidence-based monitoring workspace pair serves resource-specific log categories. Evidence-based monitoring workspace proves resource-specific log categories, but Azure Monitor Insights lacks implementation in evidence-based monitoring workspace and Azure Monitor Insights proof; the Azure Monitor Insights outcome to use a curated service view backed by the required monitoring data remains open.
- **D — Incorrect.** First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
  First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings. This evidence-based monitoring workspace pair serves Log Analytics workspaces. Evidence-based monitoring workspace uses Log Analytics workspaces for both steps; Azure Monitor Insights remains untouched in evidence-based monitoring workspace, so its Azure Monitor Insights gate to use a curated service view backed by the required monitoring data fails.

**Objectives:** `MR-MONITOR-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB22-CP03`).

**Microsoft Learn sources:**

- [Insights and curated visualizations in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q49 — C

**Question:** To satisfy the telemetry assessment requirement, operators must change the evidence-based monitoring workspace configuration and prove it can bring continuous network-test telemetry into the monitoring workflow. Which sequence is coherent?

- **A — Incorrect.** First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.
  First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table. This evidence-based monitoring workspace pair serves metrics and logs. Metrics and logs cannot replace Connection Monitor telemetry in evidence-based monitoring workspace. Use this Connection Monitor telemetry pair instead: First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.
- **B — Incorrect.** First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
  First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings. This evidence-based monitoring workspace pair serves Log Analytics workspaces. Evidence-based monitoring workspace proves Log Analytics workspaces, but Connection Monitor telemetry lacks implementation in evidence-based monitoring workspace and Connection Monitor telemetry proof; the Connection Monitor telemetry outcome to bring continuous network-test telemetry into the monitoring workflow remains open.
- **C — Correct.** First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.
  The evidence-based monitoring workspace gets a complete Connection Monitor telemetry sequence here: first, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes. Read-back evidence follows the change.
- **D — Incorrect.** First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.
  First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count. This evidence-based monitoring workspace pair serves KQL filtering and summarization. Evidence-based monitoring workspace closes KQL filtering and summarization, not Connection Monitor telemetry; without the Connection Monitor telemetry workflow, it cannot bring continuous network-test telemetry into the monitoring workflow.

**Objectives:** `MR-MONITOR-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB22-CP04`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB22-Q50 — D

**Question:** The monitoring administrator building an evidence-based service view needs a safe evidence-based monitoring workspace change to control retention and ingestion volume before monitoring cost grows unexpectedly, followed by telemetry assessment evidence. Which pair merits approval?

- **A — Incorrect.** First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.
  First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains. This evidence-based monitoring workspace pair serves metric aggregation and time grain. Evidence-based monitoring workspace proves metric aggregation and time grain, but monitoring retention and cost lacks implementation in evidence-based monitoring workspace and monitoring retention and cost proof; the monitoring retention and cost outcome to control retention and ingestion volume before monitoring cost grows unexpectedly remains open.
- **B — Incorrect.** First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.
  First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count. This evidence-based monitoring workspace pair serves KQL filtering and summarization. Evidence-based monitoring workspace uses KQL filtering and summarization for both steps; monitoring retention and cost remains untouched in evidence-based monitoring workspace, so its monitoring retention and cost gate to control retention and ingestion volume before monitoring cost grows unexpectedly fails.
- **C — Incorrect.** First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
  First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value. This evidence-based monitoring workspace pair serves log ingestion latency. Evidence-based monitoring workspace closes log ingestion latency, not monitoring retention and cost; without the monitoring retention and cost workflow, it cannot control retention and ingestion volume before monitoring cost grows unexpectedly.
- **D — Correct.** First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change.
  First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change. This ordered monitoring retention and cost workflow lets the evidence-based monitoring workspace control retention and ingestion volume before monitoring cost grows unexpectedly and then verify the resulting state.

**Objectives:** `MR-MONITOR-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB22-CP05`).

**Microsoft Learn sources:**

- [Azure Monitor Logs cost calculations and options](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs)

**Source reviewed:** 2026-08-31
