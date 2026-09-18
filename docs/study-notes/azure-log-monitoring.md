# Azure Monitor: AZ-104 Study Note

This note focuses on the current AZ-104 objective **Monitor resources in Azure**. It covers the concepts worth prioritizing for the exam:

- metrics
- logs and Log Analytics
- queries and Kusto Query Language (KQL)
- Azure Monitor Insights
- alerts, action groups, and alert processing rules

Detailed Data Collection Endpoint, Data Collection Rule, Azure Monitor Agent, and IIS-file collection procedures are intentionally outside this note's main scope. They are implementation details rather than the core emphasis of the current published AZ-104 objectives.

## The big picture

Azure Monitor answers two different operational questions:

1. **What is happening now?** Usually answer this with metrics.
2. **What happened, why did it happen, and which resource was involved?** Usually answer this with logs and queries.

A simplified monitoring flow is:

```text
Azure resource
   ├── platform metrics ──> Azure Monitor Metrics ──> charts/metric alerts
   └── activity/resource logs ──> Log Analytics workspace ──> KQL queries/log alerts

Metric or log alert
   └──> action group ──> email, webhook, notification, or automation
```

Monitoring is useful only when you connect the signal to a decision: investigate, notify someone, scale, repair, or ignore a known condition.

## 1. Metrics

A **metric** is a numeric measurement recorded over time. Examples include:

- virtual machine percentage CPU
- storage account capacity
- App Service HTTP 5xx count
- load balancer health probe status
- network bytes sent

Metrics are usually best for fast, numeric questions such as:

> Has CPU been above 80% for the last 15 minutes?

A metric has a time series, a value, and often dimensions such as resource name, operation, or status. You view metrics in Azure Monitor and can plot them over a selected time range.

### Example

To investigate a slow web application, start with:

```text
CPU        -> Is the VM overloaded?
Memory     -> Is available memory falling?
Requests   -> Did traffic increase?
HTTP 5xx   -> Did server errors increase?
```

A metric is not the same as a log record. `CPU = 82%` is a measurement. A log record might say that a particular request returned HTTP 500 or that a deployment changed a setting.

## 2. Logs and Log Analytics

A **log** is a record of an event, state change, operation, or observation. Examples include:

- a virtual machine starting or stopping;
- a failed sign-in or authorization event;
- a resource configuration change;
- a web request returning an error;
- a backup operation succeeding or failing.

A **Log Analytics workspace** is the Azure resource where supported Azure Monitor logs are stored and queried. It is not simply a dashboard. It is a central log store with tables, retention settings, access controls, and a query experience.

Different kinds of logs have different origins:

| Log type | Example | Typical use |
|---|---|---|
| Activity log | A VM was deleted | Investigate Azure control-plane operations |
| Resource log | A storage request was denied | Investigate service-level operations |
| Guest/application log | An application wrote an error | Investigate software inside a VM or application |

The important boundary is:

- **Azure Monitor Metrics** stores and displays numeric measurements.
- **Log Analytics** stores supported log records for analysis with KQL.

Logs can be more detailed than metrics, but they require deliberate collection and configuration. A resource existing in Azure does not mean every possible log is automatically in a workspace.

## 3. Queries and KQL

**Kusto Query Language (KQL)** is used to query and analyze logs in a Log Analytics workspace.

A basic query reads from a table:

```kusto
AzureActivity
| take 20
```

This means: read the `AzureActivity` table and return 20 records.

A useful investigation query might group activity by operation:

```kusto
AzureActivity
| summarize Operations=count() by OperationNameValue
| order by Operations desc
```

A time filter makes the investigation more meaningful:

```kusto
AzureActivity
| where TimeGenerated > ago(1h)
| summarize Count=count() by ResourceGroup
| order by Count desc
```

### Core KQL operators to recognize

| Operator | Purpose |
|---|---|
| `where` | Filter records |
| `project` | Select columns |
| `summarize` | Aggregate records |
| `count()` | Count records |
| `bin()` | Group time into intervals |
| `order by` | Sort results |
| `take` | Return a limited sample |
| `render` | Request a chart suitable for the result |

Example: count events by 5-minute interval:

```kusto
AzureActivity
| where TimeGenerated > ago(1h)
| summarize Events=count() by bin(TimeGenerated, 5m)
| render timechart
```

When a question says **query and analyze logs**, think in this order:

1. Identify the correct workspace.
2. Identify the likely table.
3. Filter by time and relevant resource.
4. Select the columns or aggregate the records.
5. Interpret the result and decide what to do next.

## 4. Azure Monitor Insights

**Insights** are curated monitoring experiences for particular Azure resource types. They combine relevant metrics, logs, charts, health information, and sometimes topology or dependency information into a service-specific view.

For AZ-104, know the idea rather than memorizing every screen:

- VM Insights helps interpret virtual machine health and performance.
- Storage Insights helps examine storage account behavior and capacity.
- Network Insights helps provide monitoring views for network resources.

Insights do not replace metrics or Log Analytics. They organize and present monitoring data so that an administrator can investigate a resource more quickly.

```text
Raw signals -> metrics/logs -> resource-specific Insights experience
```

A practical distinction:

- Use a normal metric chart when you already know which measurement you need.
- Use Logs and KQL when you need detailed records, filtering, correlation, or historical investigation.
- Use Insights when you want a guided, resource-specific overview.

## 5. Alerts

An **alert rule** evaluates a condition and creates an alert when the condition is met.

Common alert types include:

- metric alerts, such as CPU above 80%;
- log search alerts, such as more than five failed operations in 10 minutes;
- activity log alerts, such as a resource being deleted;
- service-health or resource-health alerts, where applicable.

### Metric alert example

```text
Condition: VM CPU > 80%
Evaluation: average over 15 minutes
Action: notify the operations team
```

### Log alert example

```kusto
AzureActivity
| where TimeGenerated > ago(10m)
| where OperationNameValue contains "delete"
| summarize Deletes=count()
```

A log alert evaluates the query result according to the alert rule's condition. The query alone does not notify anyone.

## 6. Action groups and alert processing rules

An **action group** defines what to do when an alert fires. Actions can include:

- email or SMS notifications;
- push notifications;
- webhook calls;
- Azure Automation or Functions integration;
- other supported automated actions.

An alert rule decides **when** there is a problem. The action group decides **who or what is contacted**.

An **alert processing rule** modifies how alerts are handled after they are generated. It can, for example:

- suppress notifications during a maintenance window;
- add or remove action groups;
- apply handling to a defined scope;
- reduce duplicate or unwanted notifications.

The relationship is:

```text
Signal
  -> alert rule evaluates a condition
  -> alert is generated
  -> action group performs notification/automation
  -> alert processing rule can modify that handling
```

Do not confuse an alert rule with an action group:

| Resource | Main question answered |
|---|---|
| Alert rule | When should an alert be created? |
| Action group | What should happen when it fires? |
| Alert processing rule | Should that handling be changed for this scope or time? |

## 7. A complete practical scenario

Requirement:

> Notify the administrator when a production web VM has sustained high CPU, and investigate whether the increase came from a traffic spike.

A sensible monitoring design is:

1. Create a **metric alert** for average CPU above 80% for 15 minutes.
2. Attach an **action group** that emails the administrator.
3. When it fires, inspect VM and application metrics.
4. Use Log Analytics and KQL to investigate request or error records.
5. Use the relevant VM or application **Insights** view for a guided overview.
6. If the alert fired during planned maintenance, use an **alert processing rule** to suppress the expected notification window.

This demonstrates why metrics and logs complement one another:

```text
Metric: CPU increased at 14:05
Logs: requests/errors increased at 14:05
Conclusion: likely traffic or application load
```

## 8. What to prioritize for AZ-104

### High priority

- Metrics versus logs
- Log Analytics workspaces
- Activity logs versus resource/application logs
- Basic KQL filtering and aggregation
- Azure Monitor Insights at a conceptual level
- Metric alerts versus log alerts
- Alert rules, action groups, and alert processing rules
- Choosing the right signal for an operational question

### Lower priority for this objective

- Detailed Azure Monitor Agent internals
- IIS-specific file collection
- Data Collection Endpoint regional topology
- Private-link collection architecture
- Every field and option in a Data Collection Rule

Those topics may matter in real Azure administration, but they are not the first study investment for the current published AZ-104 objectives.

## Exam reasoning checklist

When reading a monitoring question, ask:

1. Is the question about a number over time? Use **metrics**.
2. Is it about detailed events or history? Use **logs**.
3. Does it require KQL? Use a **Log Analytics workspace**.
4. Does it ask for a guided view for a VM, storage account, or network? Think **Insights**.
5. Does it ask when to trigger? Think **alert rule**.
6. Does it ask who gets notified or what automation runs? Think **action group**.
7. Does it ask to suppress or modify notifications for a time/scope? Think **alert processing rule**.

## Retrieval check

Explain this scenario without looking at the note:

> CPU on a VM has been above 80% for 15 minutes. The administrator wants an email, then wants to determine whether failed requests increased at the same time.

A complete answer should identify:

- a metric alert for the CPU threshold;
- an action group for the email;
- Log Analytics and a KQL query for detailed failed-request records;
- Insights as an optional guided investigation view;
- an alert processing rule if notifications must be suppressed during maintenance.

## Official references

- [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/overview)
- [Azure Monitor logs overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs)
- [Log Analytics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)
- [Kusto Query Language overview](https://learn.microsoft.com/en-us/kusto/query/)
- [Azure Monitor alerts overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
- [Azure Monitor Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview)
