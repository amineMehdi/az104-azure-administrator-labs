# Azure Monitor: the telemetry loop

Azure Monitor is easiest to understand as Azure's **telemetry and operational loop**: collect signals, store and analyze them, detect problems, then notify or trigger a response. It is not one dashboard, one agent, or one storage account. The many Monitor tools occupy different places in that loop.

```text
Azure resources, operating systems, and applications
                         │ signals
                         ▼
             collection and routing
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
     Metrics data stores       Log Analytics workspace
             │                       │
             └───────────┬───────────┘
                         ▼
           explore, query, and visualize
                         │
              alert rules evaluate signals
                         │
                 action groups respond
```

This is a reasoning map, not a claim that all telemetry lands in one database. Azure Monitor uses different stores and query tools for different signal types.

## Start with the operational problem

Suppose `vm-api-01` in production is responding slowly. An administrator needs to answer a sequence of questions:

1. **What is happening?** Is CPU high? Are requests slow? Are errors increasing?
2. **When did it begin, and what else happened then?** Did a guest OS event or deployment coincide with the slowdown?
3. **When should someone be notified?** Is the signal serious and persistent enough to require action?
4. **What should happen next?** Notify an operator, create an incident, or run an approved automation?

Azure Monitor provides a common system for gathering evidence and connecting it to investigation and response. It does not automatically know which signals matter to your service; administrators configure collection, queries, thresholds, and responses.

## The mental model: signals move through a loop

### 1. Resources produce signals

A signal is evidence about system behavior. The practical categories are:

- **Metrics:** numeric measurements over time, such as CPU percentage, request count, or latency. They are useful for trends and thresholds.
- **Logs:** timestamped records of events or observations, such as an operating-system event or a failed request. They are useful for detailed investigation and filtering.
- **Traces:** related events that follow one operation across components, such as one web request passing through an API and a database.

Do not assume every useful signal is collected automatically. Azure platform metrics are often available directly from a resource. Guest operating-system and application data may need an agent or application instrumentation. Resource logs may need diagnostic settings to route them to a destination.

### 2. Collection determines what evidence exists

Collection configuration is the “what should we gather, and where should it go?” part of the design.

- **Azure Monitor Agent (AMA)** can collect guest data from VMs and servers.
- **Data collection rules (DCRs)** specify what data to collect and can define destinations for supported collection scenarios.
- **Diagnostic settings** route supported Azure resource logs and metrics to configured destinations, such as a Log Analytics workspace or storage account.
- **Application instrumentation**, commonly using OpenTelemetry, sends application telemetry for analysis with Application Insights.

These mechanisms have different attachment points and responsibilities. For example, installing AMA alone does not mean that every log is being collected; the relevant rule and destination must also be configured. Similarly, being able to see a platform metric does not imply that guest memory data is available.

### 3. Stores and query tools match the signal

Azure Monitor uses different data stores for different kinds of telemetry:

| Data | Typical place to inspect it | Useful question |
|---|---|---|
| Platform or guest metrics | Metrics Explorer and the metrics platform | “Did CPU stay high, and when?” |
| Logs and traces | Log Analytics workspace, queried with Kusto Query Language (KQL) | “Which errors happened during that period?” |
| Prometheus or OpenTelemetry metrics in supported scenarios | Azure Monitor workspace and Prometheus-compatible tools | “Which service or workload is emitting this metric pattern?” |

A **Log Analytics workspace** is an Azure resource that stores log data for querying; it is not another name for Azure Monitor itself. An **Azure Monitor workspace** is a different resource type used for Prometheus metrics. Similar names do not mean they are interchangeable.

### 4. Analysis turns data into understanding

Use the analysis tool that matches the question:

- Use **Metrics Explorer** to compare metric values and trends over time.
- Use **Log Analytics** and KQL to filter, aggregate, and correlate records.
- Use **Application Insights** to investigate application performance, failures, and request flows. It is an application-performance-monitoring capability within Azure Monitor, not a replacement for all VM or Azure resource monitoring.
- Use **Azure Monitor Insights** when a resource type has a curated monitoring experience. Insights organize relevant signals and views; they do not replace the underlying signals or collection configuration.
- Use **Workbooks** to combine queries, visualizations, and explanatory text into an operational view.

A dashboard or insight can only show useful evidence if that evidence is being produced and collected. A polished view cannot compensate for missing telemetry.

### 5. Detection and response are separate steps

An **alert rule** evaluates a signal against a condition. For example: “CPU is above 85% for ten minutes.” When the condition is met, an alert fires.

An **action group** defines how to respond, such as sending email or starting an automation workflow. The rule decides *when*; the action group determines *what response to initiate*. An action group can start a remediation, but it is not the signal, the rule, or the monitoring store.

For `vm-api-01`, the flow might be:

```text
CPU readings → alert rule sees >85% for 10 minutes → alert fires
             → action group emails the on-call team
             → operator investigates metrics and VM logs
             → operator or approved automation fixes the cause
```

Azure Monitor helps observe and respond; it is not, by itself, a general-purpose configuration enforcement system. An alert does not prove a root cause, and a notification does not prove that the issue was fixed.

## Two alert states that sound alike

An alert has two distinct state concepts:

| State | Example values | What it answers | Who changes it? |
|---|---|---|---|
| **Alert condition** | Fired, Resolved | “Does the monitored condition still hold?” | Azure Monitor evaluates the condition. |
| **User response** | New, Acknowledged, Closed | “Has an operator handled this alert?” | A user changes the response. |

If an action group remediation lowers CPU, Azure Monitor may later mark the alert **condition** resolved. That does not itself mark the **user response** Closed. Conversely, an administrator can close the user response while the underlying condition is still fired. “Resolved” describes the monitored condition; “Closed” describes an operator's response.

## Choose by the question you need to answer

| Operational question | Start with | Why |
|---|---|---|
| “Is CPU or request latency rising?” | Metrics Explorer | The question is about a numeric trend over time. |
| “Which errors or OS events occurred during the slowdown?” | Log Analytics / KQL | The question needs detailed records and filtering. |
| “Which application request failed, and where did it spend time?” | Application Insights | The question follows application performance and request behavior. |
| “When should the team be notified?” | Alert rule | The question is about evaluating a condition. |
| “Who or what should be contacted when it fires?” | Action group | The question is about the response destination or workflow. |
| “Give me a resource-focused monitoring view.” | Azure Monitor Insights | The question is about a curated view over relevant monitoring data. |

The discriminating axis is the **verb**: collect, route, query, visualize, evaluate, or respond. Two tools may both display information, but that shared feature does not make them responsible for the same step.

## Common failure patterns

- **No guest data:** a VM exists and Azure platform metrics are visible, but expected memory or OS records are missing because guest collection was not configured correctly.
- **No resource logs at the destination:** the resource emits logs, but diagnostic settings do not route them to the workspace being queried.
- **A query returns no useful evidence:** the wrong workspace, resource, time range, or data type was selected—or the data was never collected.
- **An alert never fires:** the relevant signal is missing, the condition is wrong for the metric's dimensions or aggregation, or the threshold was not reached.
- **An alert fires but nobody is notified:** the alert rule fired, but the action group or its notification configuration does not reach the intended responder.
- **An alert is resolved but still appears open to an operator:** the condition and the user response are separate states; the response may still need to be changed.

Troubleshoot from the source forward: verify the signal exists, verify collection and destination, inspect the data, then check the rule condition and response path. This avoids trying to repair a notification when the real problem is missing telemetry.

## Small thought experiment

For `vm-api-01`, imagine CPU is above 85% from 10:00 to 10:15 and the application returns errors at 10:07. The CPU metric helps establish *when and how much* the machine was busy. Application or guest logs help investigate *what happened*. The alert rule detects the configured CPU condition. The action group notifies the team. None of those facts alone proves that high CPU caused the application errors; correlate the evidence before choosing a fix.

## AZ-104 objective anchors

This mental model supports the **Monitor and maintain Azure resources** domain, especially:

- **MR-MONITOR-01:** Interpret metrics in Azure Monitor.
- **MR-MONITOR-02:** Configure log settings in Azure Monitor.
- **MR-MONITOR-03:** Query and analyze logs in Azure Monitor.
- **MR-MONITOR-04:** Set up alert rules, action groups, and alert processing rules in Azure Monitor.
- **MR-MONITOR-05:** Configure and interpret monitoring of virtual machines, storage accounts, and networks by using Azure Monitor Insights.

These are exam objectives; AMA, DCRs, diagnostic settings, and a particular workspace are implementation details used to make the desired evidence available.

## Official references

- [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview)
- [Azure Monitor data platform](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/data-platform)
- [Azure Monitor data sources and collection methods](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/data-sources)
- [Azure Monitor alerts overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
- [Manage alert instances](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-manage-alert-instances)
- [Application Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

## Retrieval check

A VM shows CPU metrics, but no guest memory readings appear in the monitoring view. Before changing the alert threshold, what would you check in the signal-collection path—and why?
