# Lab 22 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB22-Q01 — Foundational

The telemetry assessment review compares four claims for the evidence-based monitoring workspace requirement to decide whether a measurement belongs in metrics or queryable events. Which claim is technically sound?

- A. A metric chart or query combines samples using an aggregation over a selected time grain and interval.
- B. Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
- C. A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior.
- D. Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types.

## LAB22-Q02 — Foundational

The telemetry assessment architecture note requires the evidence-based monitoring workspace environment to interpret a chart only after checking its aggregation and time grain. Which statement defines the relevant telemetry assessment boundary?

- A. A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs.
- B. KQL operators such as where, project, summarize, and order by shape records into focused operational evidence.
- C. Connection Monitor records recurring network reachability and latency tests between configured endpoints.
- D. A metric chart or query combines samples using an aggregation over a selected time grain and interval.

## LAB22-Q03 — Foundational

A new telemetry assessment operator must explain why the evidence-based monitoring workspace can send supported resource telemetry to an approved destination. Which explanation is accurate?

- A. A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs.
- B. Available diagnostic log categories differ by resource provider and resource type.
- C. Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.
- D. Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost.

## LAB22-Q04 — Foundational

The evidence-based monitoring workspace acceptance criteria require operators to enable the service-specific log categories required by the query. Which service fact supports that requirement?

- A. A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior.
- B. Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types.
- C. Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
- D. Available diagnostic log categories differ by resource provider and resource type.

## LAB22-Q05 — Foundational

A telemetry assessment reviewer challenges whether the evidence-based monitoring workspace can store and query records from several monitored resources in one boundary. Which response resolves the concern?

- A. KQL operators such as where, project, summarize, and order by shape records into focused operational evidence.
- B. Connection Monitor records recurring network reachability and latency tests between configured endpoints.
- C. A metric chart or query combines samples using an aggregation over a selected time grain and interval.
- D. A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior.

## LAB22-Q06 — Foundational

The evidence-based monitoring workspace handoff omits the telemetry assessment rule needed to filter records and calculate a grouped summary with KQL. Which statement should the team add?

- A. Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.
- B. Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost.
- C. A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs.
- D. KQL operators such as where, project, summarize, and order by shape records into focused operational evidence.

## LAB22-Q07 — Foundational

A telemetry assessment incident review of the evidence-based monitoring workspace depends on the ability to allow for collection and processing delay before declaring telemetry missing. Which platform description is reliable?

- A. Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types.
- B. Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
- C. Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.
- D. Available diagnostic log categories differ by resource provider and resource type.

## LAB22-Q08 — Foundational

A monitoring administrator building an evidence-based service view is updating the telemetry assessment runbook. The requirement is to use a curated service view backed by the required monitoring data. Which statement describes Azure behavior correctly?

- A. Connection Monitor records recurring network reachability and latency tests between configured endpoints.
- B. A metric chart or query combines samples using an aggregation over a selected time grain and interval.
- C. Azure Monitor Insights packages curated workbooks, metrics, logs, and configuration for supported resource types.
- D. A Log Analytics workspace stores Azure Monitor Logs data with workspace configuration for access, retention, and cost behavior.

## LAB22-Q09 — Foundational

A telemetry assessment peer review asks how the evidence-based monitoring workspace should handle this outcome: bring continuous network-test telemetry into the monitoring workflow. Which explanation is accurate?

- A. Connection Monitor records recurring network reachability and latency tests between configured endpoints.
- B. Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost.
- C. A diagnostic setting routes selected resource log categories and metrics to supported destinations such as Log Analytics, Storage, or Event Hubs.
- D. KQL operators such as where, project, summarize, and order by shape records into focused operational evidence.

## LAB22-Q10 — Foundational

For the evidence-based monitoring workspace, the telemetry assessment plan must control retention and ingestion volume before monitoring cost grows unexpectedly. Which statement about telemetry assessment belongs in the evidence-based monitoring workspace record?

- A. Collecting more diagnostic categories and retaining logs longer can increase ingestion and retention cost.
- B. Metrics are numeric time-series values, while logs contain timestamped records that support richer correlation and querying.
- C. Available diagnostic log categories differ by resource provider and resource type.
- D. Diagnostic events can take time to reach a Log Analytics workspace, so an immediate empty query is not proof of misconfiguration.

## LAB22-Q11 — Foundational

A telemetry assessment dry run shows no evidence-based monitoring workspace command will decide whether a measurement belongs in metrics or queryable events. Which action belongs before execution?

- A. Select only required categories and send them to the approved destination resources.
- B. Filter early by resource and time, then summarize only the dimensions required by the question.
- C. Use a metric for fast numeric trends and logs when the question requires record-level context.
- D. Configure representative endpoints and a test frequency that can reveal intermittent failures.

## LAB22-Q12 — Foundational

For the evidence-based monitoring workspace, operators need to interpret a chart only after checking its aggregation and time grain. Which change realizes that requirement?

- A. List categories on the exact resource before creating the diagnostic setting.
- B. Poll with a bounded timeout while separately verifying the diagnostic setting and generated event.
- C. Choose aggregation and granularity that match the operational question and signal semantics.
- D. Collect signals tied to operational requirements and set an approved workspace retention period.

## LAB22-Q13 — Foundational

Operators must automate the evidence-based monitoring workspace change needed to send supported resource telemetry to an approved destination. Which telemetry assessment operation belongs in the runbook?

- A. Route diagnostic data to the intended workspace and record its immutable resource and customer IDs.
- B. Enable the prerequisites for the resource-specific insight and allow time for data collection.
- C. Use a metric for fast numeric trends and logs when the question requires record-level context.
- D. Select only required categories and send them to the approved destination resources.

## LAB22-Q14 — Foundational

An evidence-based monitoring workspace review finds telemetry assessment drift from the need to enable the service-specific log categories required by the query. Which correction addresses that drift?

- A. Filter early by resource and time, then summarize only the dimensions required by the question.
- B. Configure representative endpoints and a test frequency that can reveal intermittent failures.
- C. Choose aggregation and granularity that match the operational question and signal semantics.
- D. List categories on the exact resource before creating the diagnostic setting.

## LAB22-Q15 — Foundational

The evidence-based monitoring workspace window permits only the telemetry assessment change needed to store and query records from several monitored resources in one boundary. Which option respects the boundary?

- A. Poll with a bounded timeout while separately verifying the diagnostic setting and generated event.
- B. Route diagnostic data to the intended workspace and record its immutable resource and customer IDs.
- C. Collect signals tied to operational requirements and set an approved workspace retention period.
- D. Select only required categories and send them to the approved destination resources.

## LAB22-Q16 — Applied

The telemetry assessment preflight has passed; the evidence-based monitoring workspace must now filter records and calculate a grouped summary with KQL. Which operation should run?

- A. Filter early by resource and time, then summarize only the dimensions required by the question.
- B. Enable the prerequisites for the resource-specific insight and allow time for data collection.
- C. Use a metric for fast numeric trends and logs when the question requires record-level context.
- D. List categories on the exact resource before creating the diagnostic setting.

## LAB22-Q17 — Applied

The evidence-based monitoring workspace plan must allow for collection and processing delay before declaring telemetry missing while limiting the mutation scope to telemetry assessment. Which action is appropriate?

- A. Configure representative endpoints and a test frequency that can reveal intermittent failures.
- B. Choose aggregation and granularity that match the operational question and signal semantics.
- C. Poll with a bounded timeout while separately verifying the diagnostic setting and generated event.
- D. Route diagnostic data to the intended workspace and record its immutable resource and customer IDs.

## LAB22-Q18 — Applied

A telemetry assessment ticket in the evidence-based monitoring workspace says to use a curated service view backed by the required monitoring data. Which telemetry assessment action completes the evidence-based monitoring workspace request with minimal change?

- A. Collect signals tied to operational requirements and set an approved workspace retention period.
- B. Enable the prerequisites for the resource-specific insight and allow time for data collection.
- C. Select only required categories and send them to the approved destination resources.
- D. Filter early by resource and time, then summarize only the dimensions required by the question.

## LAB22-Q19 — Applied

The approach for the evidence-based monitoring workspace is approved, but the telemetry assessment environment still cannot bring continuous network-test telemetry into the monitoring workflow. Which implementation step closes the gap?

- A. Use a metric for fast numeric trends and logs when the question requires record-level context.
- B. Configure representative endpoints and a test frequency that can reveal intermittent failures.
- C. List categories on the exact resource before creating the diagnostic setting.
- D. Poll with a bounded timeout while separately verifying the diagnostic setting and generated event.

## LAB22-Q20 — Applied

The monitoring administrator building an evidence-based service view may change the evidence-based monitoring workspace only to control retention and ingestion volume before monitoring cost grows unexpectedly. Which telemetry assessment action stays within that assignment?

- A. Choose aggregation and granularity that match the operational question and signal semantics.
- B. Collect signals tied to operational requirements and set an approved workspace retention period.
- C. Route diagnostic data to the intended workspace and record its immutable resource and customer IDs.
- D. Enable the prerequisites for the resource-specific insight and allow time for data collection.

## LAB22-Q21 — Applied

The telemetry assessment validator needs one evidence-based monitoring workspace query after the change to decide whether a measurement belongs in metrics or queryable events. Which telemetry assessment property should the evidence-based monitoring workspace validator inspect?

- A. Query diagnostic-settings categories and match configured categories against the returned list.
- B. Record query time range, retries, and the first matching TimeGenerated value.
- C. Query the metric namespace and separately confirm expected records reach the Log Analytics table.
- D. Query daily ingestion, table retention, and enabled categories before and after the change.

## LAB22-Q22 — Applied

The monitoring administrator building an evidence-based service view must confirm the evidence-based monitoring workspace, without mutation, can interpret a chart only after checking its aggregation and time grain. Which telemetry assessment check qualifies?

- A. Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
- B. Read the metric definition's supported aggregations and compare results at two time grains.
- C. Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
- D. Query the metric namespace and separately confirm expected records reach the Log Analytics table.

## LAB22-Q23 — Applied

The evidence-based monitoring workspace configuration is complete; the telemetry assessment reviewers need evidence it can send supported resource telemetry to an approved destination. Which observation shows success?

- A. Query logs and metrics selections, destination IDs, and enabled states on the setting.
- B. Run the query over a known time range and confirm projected columns, grouping, and result count.
- C. Query monitor test results and correlate failed checks with network configuration changes.
- D. Read the metric definition's supported aggregations and compare results at two time grains.

## LAB22-Q24 — Applied

The telemetry assessment validation asks whether the evidence-based monitoring workspace can enable the service-specific log categories required by the query. Which observable state is strongest?

- A. Record query time range, retries, and the first matching TimeGenerated value.
- B. Query daily ingestion, table retention, and enabled categories before and after the change.
- C. Query logs and metrics selections, destination IDs, and enabled states on the setting.
- D. Query diagnostic-settings categories and match configured categories against the returned list.

## LAB22-Q25 — Applied

An evidence-based monitoring workspace review must prove the telemetry assessment ability to store and query records from several monitored resources in one boundary. Which check avoids an adjacent feature?

- A. Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
- B. Query the metric namespace and separately confirm expected records reach the Log Analytics table.
- C. Query diagnostic-settings categories and match configured categories against the returned list.
- D. Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.

## LAB22-Q26 — Applied

The evidence-based monitoring workspace evidence bundle needs a telemetry assessment result showing it can filter records and calculate a grouped summary with KQL. Which result belongs in the checkpoint?

- A. Query monitor test results and correlate failed checks with network configuration changes.
- B. Run the query over a known time range and confirm projected columns, grouping, and result count.
- C. Read the metric definition's supported aggregations and compare results at two time grains.
- D. Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.

## LAB22-Q27 — Applied

Before evidence-based monitoring workspace cleanup, the telemetry assessment team must reconfirm it can allow for collection and processing delay before declaring telemetry missing. Which read-only inspection should run?

- A. Record query time range, retries, and the first matching TimeGenerated value.
- B. Query daily ingestion, table retention, and enabled categories before and after the change.
- C. Query logs and metrics selections, destination IDs, and enabled states on the setting.
- D. Run the query over a known time range and confirm projected columns, grouping, and result count.

## LAB22-Q28 — Applied

The evidence-based monitoring workspace setup reports success after the telemetry assessment attempt to use a curated service view backed by the required monitoring data. Which telemetry assessment read-only observation proves the evidence-based monitoring workspace outcome?

- A. Query the metric namespace and separately confirm expected records reach the Log Analytics table.
- B. Query diagnostic-settings categories and match configured categories against the returned list.
- C. Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
- D. Record query time range, retries, and the first matching TimeGenerated value.

## LAB22-Q29 — Applied

The telemetry assessment log says the evidence-based monitoring workspace can now bring continuous network-test telemetry into the monitoring workflow. Which telemetry assessment state should the evidence-based monitoring workspace acceptance test retain?

- A. Read the metric definition's supported aggregations and compare results at two time grains.
- B. Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
- C. Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
- D. Query monitor test results and correlate failed checks with network configuration changes.

## LAB22-Q30 — Applied

The evidence-based monitoring workspace rejects telemetry assessment exit status as proof it can control retention and ingestion volume before monitoring cost grows unexpectedly. Which evidence-based monitoring workspace result is valid evidence?

- A. Query logs and metrics selections, destination IDs, and enabled states on the setting.
- B. Query daily ingestion, table retention, and enabled categories before and after the change.
- C. Run the query over a known time range and confirm projected columns, grouping, and result count.
- D. Query monitor test results and correlate failed checks with network configuration changes.

## LAB22-Q31 — Applied

The evidence-based monitoring workspace troubleshooting scope is the telemetry assessment need to decide whether a measurement belongs in metrics or queryable events. Which condition should be corrected first?

- A. The runbook expects a platform metric query to return individual activity-log records.
- B. An average aggregation hides a short maximum spike that triggered the incident.
- C. The time filter excludes the interval when the test event occurred.
- D. Verbose categories were enabled globally without a retention or cost review.

## LAB22-Q32 — Applied

The evidence-based monitoring workspace result is partial because the telemetry assessment cannot interpret a chart only after checking its aggregation and time grain. Which condition accounts for that result?

- A. The setting exists but no resource-log category is enabled.
- B. An average aggregation hides a short maximum spike that triggered the incident.
- C. Validation queried only once before the test record completed ingestion.
- D. The runbook expects a platform metric query to return individual activity-log records.

## LAB22-Q33 — Applied

The telemetry assessment evidence shows the evidence-based monitoring workspace cannot send supported resource telemetry to an approved destination. Which root cause fits that evidence?

- A. The template specifies a category name that the target resource does not expose.
- B. The insight is opened before its required monitoring agent or data collection rule is associated.
- C. The setting exists but no resource-log category is enabled.
- D. An average aggregation hides a short maximum spike that triggered the incident.

## LAB22-Q34 — Applied

Although the evidence-based monitoring workspace is meant to let the telemetry assessment enable the service-specific log categories required by the query, its checkpoint fails. Which telemetry assessment defect explains the failure?

- A. The diagnostic setting sends data to a different workspace than the one queried during validation.
- B. The chosen source endpoint cannot run the configured connection test.
- C. The template specifies a category name that the target resource does not expose.
- D. The setting exists but no resource-log category is enabled.

## LAB22-Q35 — Applied

The telemetry assessment support team isolated the evidence-based monitoring workspace incident to the attempt to store and query records from several monitored resources in one boundary. Which condition prevents success?

- A. The diagnostic setting sends data to a different workspace than the one queried during validation.
- B. The time filter excludes the interval when the test event occurred.
- C. Verbose categories were enabled globally without a retention or cost review.
- D. The template specifies a category name that the target resource does not expose.

## LAB22-Q36 — Applied

An evidence-based monitoring workspace query surprises the monitoring administrator building an evidence-based service view during the telemetry assessment attempt to filter records and calculate a grouped summary with KQL. Which finding explains it?

- A. The time filter excludes the interval when the test event occurred.
- B. Validation queried only once before the test record completed ingestion.
- C. The runbook expects a platform metric query to return individual activity-log records.
- D. The diagnostic setting sends data to a different workspace than the one queried during validation.

## LAB22-Q37 — Applied

Other evidence-based monitoring workspace components are healthy, but the telemetry assessment still cannot allow for collection and processing delay before declaring telemetry missing. Which state causes the isolated failure?

- A. The insight is opened before its required monitoring agent or data collection rule is associated.
- B. Validation queried only once before the test record completed ingestion.
- C. An average aggregation hides a short maximum spike that triggered the incident.
- D. The time filter excludes the interval when the test event occurred.

## LAB22-Q38 — Applied

During a telemetry assessment fault drill, the evidence-based monitoring workspace does not use a curated service view backed by the required monitoring data. Which finding identifies the defect?

- A. The insight is opened before its required monitoring agent or data collection rule is associated.
- B. The chosen source endpoint cannot run the configured connection test.
- C. The setting exists but no resource-log category is enabled.
- D. Validation queried only once before the test record completed ingestion.

## LAB22-Q39 — Applied

The evidence-based monitoring workspace setup finishes, yet the telemetry assessment cannot bring continuous network-test telemetry into the monitoring workflow. Which misconfiguration explains the mismatch?

- A. The chosen source endpoint cannot run the configured connection test.
- B. Verbose categories were enabled globally without a retention or cost review.
- C. The template specifies a category name that the target resource does not expose.
- D. The insight is opened before its required monitoring agent or data collection rule is associated.

## LAB22-Q40 — Applied

A telemetry assessment break/fix in the evidence-based monitoring workspace fails when operators try to control retention and ingestion volume before monitoring cost grows unexpectedly. Which diagnosis fits?

- A. The runbook expects a platform metric query to return individual activity-log records.
- B. Verbose categories were enabled globally without a retention or cost review.
- C. The diagnostic setting sends data to a different workspace than the one queried during validation.
- D. The chosen source endpoint cannot run the configured connection test.

## LAB22-Q41 — Advanced

The evidence-based monitoring workspace has two telemetry assessment gates: decide whether a measurement belongs in metrics or queryable events, then prove the evidence-based monitoring workspace state. Which telemetry assessment sequence works?

- A. First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.
- B. First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
- C. First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
- D. First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.

## LAB22-Q42 — Advanced

Which telemetry assessment path makes the evidence-based monitoring workspace able to interpret a chart only after checking its aggregation and time grain, then inspects the defining properties?

- A. First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list.
- B. First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
- C. First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.
- D. First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.

## LAB22-Q43 — Advanced

At the evidence-based monitoring workspace approval gate, operators must show that the telemetry assessment can send supported resource telemetry to an approved destination. Which telemetry assessment configure-and-check pair is defensible?

- A. First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.
- B. First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
- C. First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.
- D. First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change.

## LAB22-Q44 — Advanced

The evidence-based monitoring workspace forbids a partial telemetry assessment result. Operators must first enable the service-specific log categories required by the query and afterward confirm the evidence-based monitoring workspace outcome. Which telemetry assessment sequence is complete?

- A. First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.
- B. First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list.
- C. First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change.
- D. First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.

## LAB22-Q45 — Advanced

Only the evidence-based monitoring workspace change needed to store and query records from several monitored resources in one boundary is allowed, and telemetry assessment proof is mandatory. Which pair fits?

- A. First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
- B. First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.
- C. First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.
- D. First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.

## LAB22-Q46 — Advanced

The evidence-based monitoring workspace runbook separates telemetry assessment mutation from validation while it must filter records and calculate a grouped summary with KQL. Which sequence proves it cleanly?

- A. First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
- B. First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.
- C. First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.
- D. First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.

## LAB22-Q47 — Advanced

The evidence-based monitoring workspace checkpoint requires both this telemetry assessment outcome—allow for collection and processing delay before declaring telemetry missing—and a read-only evidence-based monitoring workspace state check. Which telemetry assessment response is complete?

- A. First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
- B. First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.
- C. First, Select only required categories and send them to the approved destination resources. Then, Query logs and metrics selections, destination IDs, and enabled states on the setting.
- D. First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list.

## LAB22-Q48 — Advanced

The evidence-based monitoring workspace runbook must use a curated service view backed by the required monitoring data, then retain telemetry assessment read-back evidence. Which evidence-based monitoring workspace pair completes both duties?

- A. First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change.
- B. First, Enable the prerequisites for the resource-specific insight and allow time for data collection. Then, Query required agents or settings and verify the insight's underlying metrics or log tables contain data.
- C. First, List categories on the exact resource before creating the diagnostic setting. Then, Query diagnostic-settings categories and match configured categories against the returned list.
- D. First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.

## LAB22-Q49 — Advanced

To satisfy the telemetry assessment requirement, operators must change the evidence-based monitoring workspace configuration and prove it can bring continuous network-test telemetry into the monitoring workflow. Which sequence is coherent?

- A. First, Use a metric for fast numeric trends and logs when the question requires record-level context. Then, Query the metric namespace and separately confirm expected records reach the Log Analytics table.
- B. First, Route diagnostic data to the intended workspace and record its immutable resource and customer IDs. Then, Query workspace provisioning state, retentionInDays, sku, and connected diagnostic settings.
- C. First, Configure representative endpoints and a test frequency that can reveal intermittent failures. Then, Query monitor test results and correlate failed checks with network configuration changes.
- D. First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.

## LAB22-Q50 — Advanced

The monitoring administrator building an evidence-based service view needs a safe evidence-based monitoring workspace change to control retention and ingestion volume before monitoring cost grows unexpectedly, followed by telemetry assessment evidence. Which pair merits approval?

- A. First, Choose aggregation and granularity that match the operational question and signal semantics. Then, Read the metric definition's supported aggregations and compare results at two time grains.
- B. First, Filter early by resource and time, then summarize only the dimensions required by the question. Then, Run the query over a known time range and confirm projected columns, grouping, and result count.
- C. First, Poll with a bounded timeout while separately verifying the diagnostic setting and generated event. Then, Record query time range, retries, and the first matching TimeGenerated value.
- D. First, Collect signals tied to operational requirements and set an approved workspace retention period. Then, Query daily ingestion, table retention, and enabled categories before and after the change.

[Open the answer key](./ANSWERS.md)
