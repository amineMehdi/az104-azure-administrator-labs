# Azure Monitoring and Observability: AZ-104 Distinction Note

Azure has many things that appear to “monitor” resources. They are not all doing the same job.

The reliable way to distinguish them is to ask:

1. **What signal is being collected?**
2. **Where does that signal come from?**
3. **What resource or scope does it watch?**
4. **Is it collecting, storing, analyzing, presenting, or responding?**

The phrase to remember is:

> **Identify the signal before choosing the monitoring tool.**

## The one-page mental model

```text
A resource produces a signal
        ↓
A collector or platform feature captures it
        ↓
A store holds it, if it is historical data
        ↓
A query, chart, or Insights view helps you understand it
        ↓
An alert rule decides whether it matters
        ↓
An action group notifies or automates a response
```

Different Azure services occupy different parts of this flow.

## The monitoring map

| Thing | What it watches | What it produces or does | Think of it as |
|---|---|---|---|
| Azure Monitor | Broad Azure and hybrid telemetry | Unified monitoring platform | Umbrella |
| Metrics | Numeric measurements over time | CPU, capacity, requests, latency | Gauge |
| Activity Log | Azure control-plane operations | Create, update, delete, deployment events | Audit trail |
| Resource logs | Data-plane/service operations | Storage requests, Key Vault access, firewall events | Service event records |
| Diagnostic settings | Azure resource log routing | Sends selected resource logs to destinations | Routing configuration |
| Log Analytics workspace | Logs and traces sent to it | Tables queried with KQL | Log store/query engine |
| Azure Monitor Agent | Guest OS/application data | Events, files, counters, guest telemetry | VM worker |
| DCR | AMA collection instructions | Defines data sources, transformations, destinations | Collection rule |
| DCE | Certain agent/network endpoints | Configuration and ingestion endpoints | Collection network endpoint |
| Application Insights | Application execution | Requests, dependencies, exceptions, traces | Application observer |
| Insights | A resource-specific monitoring experience | Curated charts, health, topology, metrics, logs | Guided dashboard |
| NSG/VNet flow logs | Network flow metadata | Source/destination IPs, ports, protocol, allow/deny | Network traffic evidence |
| Network Watcher | Network diagnostics | Next hop, packet capture, IP flow verify, connectivity tools | Network toolbox |
| Connection Monitor | Reachability between endpoints | Connectivity, latency, failed checks | Active probe |
| Service Health | Azure-wide incidents and planned maintenance | Service issues affecting Azure customers | Azure platform status |
| Resource Health | Health of your specific resource | Available, unavailable, degraded, unknown | Resource availability status |
| Alert rule | A condition over a signal | Creates an alert | Decision |
| Action group | What happens after an alert | Email, webhook, automation, SMS | Response |
| Alert processing rule | How alert handling changes | Suppression or action-group changes | Notification policy |

The same Azure Monitor umbrella contains many of these, but the signal and job are different.

## 1. Azure Monitor: the umbrella, not one collector

The most important correction is:

> **Azure Monitor is the platform and monitoring experience. It is not one specific kind of log.**

Azure Monitor brings together:

- metrics;
- logs and traces;
- activity events;
- application telemetry;
- resource health;
- Insights experiences;
- alerts and responses.

When an exam question says “configure Azure Monitor,” do not immediately choose a DCR, workspace, or agent. First identify what Azure Monitor is supposed to observe.

```text
Azure Monitor
  ├── Metrics Explorer
  ├── Azure Monitor Logs / Log Analytics
  ├── Insights
  ├── Alerts
  ├── Activity Log integration
  └── Network monitoring integration
```

## 2. Metrics: numeric measurements

A metric is a number measured over time.

Examples:

```text
VM CPU percentage:             82%
Storage capacity:              450 GB
App Service HTTP 5xx count:    12
Load balancer health probes:   2 failed
Network bytes sent:            1.4 GB
```

Metrics answer:

> How much? How often? Is the value above or below a threshold?

Use metrics when the requirement says:

- CPU exceeds 80%;
- storage capacity is nearly full;
- latency is above a threshold;
- requests per minute increased;
- a resource metric should trigger an alert.

```text
Metric: VM CPU > 80% for 15 minutes
        ↓
Metric alert
        ↓
Action group sends email
```

Metrics are not detailed event records. `CPU = 82%` does not tell you which process caused the load. Logs or application telemetry may help explain it.

## 3. Activity Log: Azure control-plane operations

The **Activity Log** records management operations performed on Azure resources.

Examples:

```text
A VM was created
A storage account was deleted
An NSG rule was changed
A deployment failed
A role assignment was created
```

These are **control-plane** events: changes to Azure resources and configuration.

Use the Activity Log when the question is:

> Who changed the Azure configuration, what changed, or when did a deployment fail?

The Activity Log is collected automatically at subscription scope. It is not the same as logs generated inside a VM or by requests sent to a storage account.

Example distinction:

```text
Create a storage account                 -> Activity Log
Read a blob from that storage account   -> Resource log
```

The Activity Log is retained for a limited default period. Use a diagnostic setting to route it to Log Analytics, Storage, or Event Hubs when you need longer retention or centralized analysis.

## 4. Resource logs: operations inside a service

**Resource logs** record operations performed within a resource, often called data-plane operations.

Examples:

```text
A blob read request was denied
A Key Vault secret was accessed
A firewall blocked a request
A database query failed
```

Resource logs are different from the Activity Log:

| Question | Correct signal |
|---|---|
| Who deleted the storage account? | Activity Log |
| Who read a blob? | Storage resource log |
| Who changed a Key Vault policy? | Activity Log |
| Who accessed a secret? | Key Vault resource log |

Resource logs usually require explicit configuration. The resource existing does not mean every resource log category is automatically stored in a workspace.

## 5. Diagnostic settings: routing, not analysis

A **diagnostic setting** tells an Azure resource which platform logs and metrics to send to a destination.

Conceptually:

```text
Storage account resource logs
        ↓ diagnostic setting
        ├── Log Analytics workspace
        ├── Storage account
        └── Event Hub
```

A diagnostic setting does not itself explain or visualize the data. It is the delivery configuration.

Use it when the question says:

- send resource logs to a Log Analytics workspace;
- archive logs to a Storage account;
- stream logs to Event Hubs;
- configure which categories are exported.

This is different from a DCR:

```text
Diagnostic setting -> routes Azure resource/platform logs
DCR + AMA          -> configures collection from a VM guest or other DCR source
```

## 6. Log Analytics workspace: storage and KQL analysis

A **Log Analytics workspace** stores logs and traces in tables and lets you query them with Kusto Query Language (KQL).

It is not automatically the collector.

```text
Signal source -> collection/routing configuration -> Log Analytics workspace -> KQL
```

For example:

```text
Storage resource logs
    -> diagnostic setting
    -> Workspace1
    -> KQL query
```

The workspace answers:

> Where do historical log records live, and where can I query them?

A workspace can contain data from many sources. The table name tells you more about the source than the workspace name does.

Example KQL:

```kusto
AzureActivity
| where TimeGenerated > ago(1h)
| summarize Operations=count() by OperationNameValue
```

```kusto
AzureDiagnostics
| where TimeGenerated > ago(1h)
| summarize Records=count() by ResourceType
```

Do not choose a workspace merely because the word “logs” appears. Determine what signal must first be collected and how it reaches the workspace.

### Log Analytics workspace versus Azure Monitor workspace

These names are similar but refer to different workspace types:

```text
Log Analytics workspace
    -> logs and traces
    -> KQL

Azure Monitor workspace
    -> Prometheus and OpenTelemetry metrics
    -> PromQL or metrics-specific tools
```

For the current AZ-104 monitoring objectives, most workspace-and-KQL questions refer to a **Log Analytics workspace**. Do not choose an Azure Monitor workspace merely because the product name is Azure Monitor.

The practical question is:

```text
Am I storing/querying log records, or storing/querying metrics?
```


## 7. Azure Monitor Agent, DCR, and DCE: guest data collection

These are most relevant when collecting data from inside a VM or server.

### Azure Monitor Agent

The **Azure Monitor Agent (AMA)** is the worker installed on a VM or connected server.

It can collect data such as:

- Windows Event Logs;
- Syslog;
- performance counters;
- IIS logs;
- custom text logs.

```text
Data inside VM guest OS -> AMA
```

### Data Collection Rule

A **Data Collection Rule (DCR)** provides the instructions:

```text
Read Windows Security events
Read a custom log file
Collect selected performance counters
Send the result to Workspace1
```

### Data Collection Endpoint

A **Data Collection Endpoint (DCE)** provides certain configuration or ingestion endpoints for collection architectures, especially private or network-isolated designs. It is not the general answer for every log-collection question.

The distinction is:

```text
Guest-OS/application log problem -> AMA + DCR
Agent communication endpoint problem -> DCE
NSG network-flow problem        -> NSG/VNet flow logs
```

This is the same signal-first rule that prevents confusing DCE with flow logs.

## 8. Application Insights: application behavior

**Application Insights** monitors application execution. It is an Azure Monitor application-performance monitoring experience.

It can help answer:

- Are requests slow?
- Which dependency is failing?
- Are exceptions increasing?
- Which endpoint returns HTTP 500?
- What is the request rate and duration?
- How does a request flow through application dependencies?

```text
Application code
  -> requests, dependencies, exceptions, traces
  -> Application Insights
  -> charts, correlation, investigation, alerts
```

Application Insights watches the **application**, not the NSG and not Azure Resource Manager changes.

Contrast:

```text
VM CPU is high                 -> VM metrics / VM Insights
HTTP requests are slow         -> Application Insights
NSG is denying TCP 3389        -> NSG flow logs
VM was resized                 -> Activity Log
```

Application Insights is especially useful when infrastructure appears healthy but the application is failing.

## 9. Insights: curated views, not a separate universal collector

**Insights** are resource-specific monitoring experiences that organize existing telemetry.

Examples:

- VM Insights: VM health, performance, processes, and related data;
- Storage Insights: storage capacity, transactions, and service behavior;
- Network Insights: network resource topology, health, metrics, traffic, and diagnostics.

Insights answer:

> Give me a guided view of this kind of resource and its relevant signals.

They do not all collect the same data, and they do not replace the underlying telemetry sources.

```text
Raw signal -> metric/log store -> resource-specific Insights view
```

Think of Insights as a curated dashboard and investigation experience, not as “another kind of log.”

## 10. Network Watcher, flow logs, and Connection Monitor

These are often confused because they all appear in network monitoring.

### Network Watcher

**Network Watcher** is a collection of network diagnostic tools. It helps troubleshoot a network path or inspect network behavior.

Examples include:

- IP flow verify: would this flow be allowed or denied?
- next hop: which route would traffic take?
- connection troubleshoot;
- packet capture;
- topology and network diagnostics;
- Connection Monitor integration;
- flow-log integration.

Think:

> Network Watcher is the network toolbox.

### NSG or VNet flow logs

Flow logs are passive records of network traffic metadata.

They answer:

```text
Who connected to whom?
Which port and protocol were used?
Was the flow allowed or denied?
How much traffic occurred?
```

They do not inspect application payloads.

```text
Network traffic -> NSG/VNet flow logging -> traffic analysis
```

For current Azure designs, Microsoft is retiring NSG flow logs and recommends VNet flow logs. Older exam questions may still use “NSG flow logs” as the expected answer.

### Connection Monitor

Connection Monitor actively tests reachability between endpoints.

Example:

```text
VM01 -> sql01.database.windows.net:1433
```

It can help answer:

- Is the destination reachable?
- Is latency increasing?
- Which hop or check is failing?

The contrast is:

```text
Flow logs:       observe actual traffic that occurred
Connection Monitor: actively test whether a path works
```

## 11. Service Health and Resource Health

These are about **availability and platform health**, not application logs.

### Service Health

Service Health tells you about Azure platform conditions relevant to you, such as:

- service issues;
- planned maintenance;
- health advisories;
- security advisories.

It answers:

> Is Microsoft reporting an Azure service problem that may affect my subscription or resources?

### Resource Health

Resource Health reports the health of a specific resource:

```text
VM01: Available
Database01: Degraded
Storage01: Unavailable
```

It can show platform or resource availability events and health history.

Contrast:

```text
Resource Health: Is the Azure resource available?
Application Insights: Is the application behaving correctly?
Metrics: Is CPU/latency/capacity abnormal?
```

A VM can be `Available` while its application is returning HTTP 500 errors. Resource Health and application monitoring answer different questions.

## 12. Alerts and responses: the last layer

Alerts are not the original telemetry source.

An **alert rule** evaluates a signal:

```text
Metric alert:       CPU > 80%
Log alert:          five failed operations in ten minutes
Activity alert:     a resource was deleted
Resource health:    VM becomes unavailable
```

An **action group** defines what happens:

```text
Email
SMS
Webhook
Logic App
Automation
Function
```

An **alert processing rule** modifies alert handling, such as suppressing notifications during maintenance.

```text
Signal source
  -> alert rule
  -> alert
  -> action group
  -> notification or automation
```

Use this distinction:

| Requirement | Resource or feature |
|---|---|
| Capture the signal | Metric/log/flow/agent/diagnostic feature |
| Store historical logs | Log Analytics workspace or another destination |
| Explore a resource | Insights or portal experience |
| Decide whether a condition matters | Alert rule |
| Notify or automate | Action group |
| Suppress or modify notification handling | Alert processing rule |

## 13. One incident, many tools, each with a different job

Requirement:

> Users report that a web application is slow and some requests fail.

Do not choose one generic “monitoring” tool. Decompose the incident:

```text
1. Is the VM CPU or disk under pressure?
   -> VM metrics / VM Insights

2. Are HTTP requests slow or returning exceptions?
   -> Application Insights

3. Is the VM reachable from the load balancer?
   -> Connection Monitor / Network Watcher

4. Are NSG rules denying required traffic?
   -> IP flow verify / flow logs

5. Did someone recently change an NSG or VM setting?
   -> Activity Log

6. Is Azure reporting a platform problem?
   -> Service Health / Resource Health

7. Should the team be notified automatically?
   -> Alert rule + action group
```

The tools overlap in the portal, but the signals do not overlap completely.

## 14. The exam decision tree

When an AZ-104 question mentions monitoring, ask:

### What is the signal?

```text
Number over time                     -> Metric
Azure management operation           -> Activity Log
Operation inside a PaaS resource    -> Resource log
File/event/counter inside a VM      -> AMA + DCR
Application request/exception       -> Application Insights
IP flow through NSG/VNet            -> Flow logs
Reachability between endpoints      -> Connection Monitor
Azure platform incident             -> Service Health
Specific resource availability      -> Resource Health
```

### What is the requested job?

```text
Collect/route data       -> diagnostic setting, AMA/DCR, flow logging
Store/query logs         -> Log Analytics workspace + KQL
View a curated resource  -> Insights
Test a path              -> Network Watcher / Connection Monitor
Trigger a condition      -> Alert rule
Notify or automate       -> Action group
Suppress notifications   -> Alert processing rule
```

## 15. The simplest mental model

Remember three axes:

### Axis 1: What is being watched?

```text
Azure configuration -> Activity Log
PaaS operations     -> Resource logs
VM guest            -> AMA/DCR
Application         -> Application Insights
Network traffic     -> Flow logs
Connectivity path   -> Connection Monitor
Platform health     -> Service Health / Resource Health
```

### Axis 2: What does the tool do?

```text
Collect     -> AMA, DCR, diagnostic settings, flow logs
Store       -> Log Analytics workspace, Storage, Event Hubs
Analyze     -> KQL, Metrics Explorer, Traffic Analytics
Present     -> Insights, workbooks, dashboards
Respond     -> Alert rules, action groups, processing rules
Diagnose    -> Network Watcher
```

### Axis 3: Where does it attach?

```text
Subscription/resource management -> Activity Log
Azure resource                 -> diagnostic setting, metrics, resource logs
VM guest                        -> AMA/DCR
Application code                -> Application Insights
NSG or VNet                     -> flow logging
Network path                    -> Connection Monitor
Alert scope                     -> alert rule/action group
```

The phrase to use when you are stuck is:

> **This is a [signal type] problem, not a [different signal type] problem.**

Examples:

```text
This is a network-flow problem, not a guest-OS log problem.
This is a control-plane audit problem, not a storage data-plane problem.
This is an application-performance problem, not a VM-health problem.
This is a reachability problem, not a historical traffic problem.
This is a notification problem, not a telemetry-collection problem.
```

## What to prioritize for AZ-104

The current objectives emphasize:

- interpreting metrics in Azure Monitor;
- configuring log settings;
- querying and analyzing logs;
- alert rules, action groups, and alert processing rules;
- Azure Monitor Insights for VMs, storage accounts, and networks;
- Network Watcher and Connection Monitor.

Prioritize the signal boundaries and resource relationships before memorizing every agent or diagnostic option. The exam may include related implementation details, but the reusable skill is choosing the correct tool from the signal and operational question.

## Retrieval check

Classify each requirement before naming a tool:

1. “A VM's CPU has stayed above 80% for 15 minutes.”
2. “Who deleted the storage account?”
3. “Which client IPs attempted RDP against the VM?”
4. “The application returns slow HTTP responses.”
5. “Can VM01 reach SQL Database on port 1433?”
6. “Azure is performing maintenance in this region.”
7. “Email the administrator when the condition is detected.”

Expected signal/tool families:

```text
1. VM metric -> metric alert
2. Activity Log
3. NSG/VNet flow logs
4. Application Insights
5. Connection Monitor / Network Watcher
6. Service Health
7. Action group attached to an alert rule
```

## Official references

- [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview)
- [Azure Activity Log](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log)
- [Azure Monitor resource logs](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/resource-logs)
- [Azure Monitor diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings)
- [Log Analytics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)
- [Application Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
- [Network Insights](https://learn.microsoft.com/en-us/azure/network-watcher/network-insights-overview)
- [NSG flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-overview)
- [Virtual Network flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/vnet-flow-logs-overview)
- [Traffic Analytics](https://learn.microsoft.com/en-us/azure/network-watcher/traffic-analytics)
- [Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)
- [Resource Health](https://learn.microsoft.com/en-us/azure/service-health/resource-health-overview)
- [Azure Service Health](https://learn.microsoft.com/en-us/azure/service-health/overview)
