# Lab 21 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB21-Q01 — D

**Question:** A network operations administrator publishing a resilient HTTP backend is updating the backend readiness runbook. The requirement is to expose one ingress IP for incoming balanced traffic. Which statement describes Azure behavior correctly?

- **A — Incorrect.** A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows.
  A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows. In the resilient HTTP backend publication, this statement describes backend address pools. Resilient HTTP backend publication asks about load balancer frontends; this backend address pools choice leaves the load balancer frontends explanation missing.
- **B — Incorrect.** Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules.
  Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules. In the resilient HTTP backend publication, this statement describes health probe NSG traffic. The health probe NSG traffic statement accurately describes health probe NSG traffic; however, resilient HTTP backend publication needs load balancer frontends to expose one ingress IP for incoming balanced traffic; health probe NSG traffic cannot replace load balancer frontends.
- **C — Incorrect.** When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows.
  When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows. In the resilient HTTP backend publication, this statement describes all-backend probe failure. Selecting all-backend probe failure for resilient HTTP backend publication leaves load balancer frontends unanswered in resilient HTTP backend publication; the resilient HTTP backend publication lacks a load balancer frontends basis to expose one ingress IP for incoming balanced traffic.
- **D — Correct.** A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules.
  A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules. In the resilient HTTP backend publication, this load balancer frontends rule supports the need to expose one ingress IP for incoming balanced traffic.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q02 — B

**Question:** A backend readiness peer review asks how the resilient HTTP backend publication should handle this outcome: register every serving network interface as an eligible target. Which explanation is accurate?

- **A — Incorrect.** A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows.
  A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows. In the resilient HTTP backend publication, this statement describes health probes. The health probes statement accurately describes health probes; however, resilient HTTP backend publication needs backend address pools to register every serving network interface as an eligible target; health probes cannot replace backend address pools.
- **B — Correct.** A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows.
  For the resilient HTTP backend publication, the rule for backend address pools is defined by this statement: a backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows. It supports the required outcome to register every serving network interface as an eligible target.
- **C — Incorrect.** A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress.
  A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress. In the resilient HTTP backend publication, this statement describes outbound connectivity. Backend address pools governs resilient HTTP backend publication; outbound connectivity cannot support backend address pools when operators must register every serving network interface as an eligible target.
- **D — Incorrect.** Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information.
  Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information. In the resilient HTTP backend publication, this statement describes connection troubleshoot. Resilient HTTP backend publication asks about backend address pools; this connection troubleshoot choice leaves the backend address pools explanation missing.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q03 — C

**Question:** For the resilient HTTP backend publication, the backend readiness plan must remove an instance from rotation when its application endpoint is unhealthy. Which statement about backend readiness belongs in the resilient HTTP backend publication record?

- **A — Incorrect.** A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.
  A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path. In the resilient HTTP backend publication, this statement describes load-balancing rules. Selecting load-balancing rules for resilient HTTP backend publication leaves health probes unanswered in resilient HTTP backend publication; the resilient HTTP backend publication lacks a health probes basis to remove an instance from rotation when its application endpoint is unhealthy.
- **B — Incorrect.** Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence.
  Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence. In the resilient HTTP backend publication, this statement describes session persistence. Health probes governs resilient HTTP backend publication; session persistence cannot support health probes when operators must remove an instance from rotation when its application endpoint is unhealthy.
- **C — Correct.** A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows.
  A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows. The resilient HTTP backend publication applies that health probes boundary when operators must remove an instance from rotation when its application endpoint is unhealthy.
- **D — Incorrect.** Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.
  Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time. In the resilient HTTP backend publication, this statement describes Connection Monitor. The Connection Monitor statement accurately describes Connection Monitor; however, resilient HTTP backend publication needs health probes to remove an instance from rotation when its application endpoint is unhealthy; Connection Monitor cannot replace health probes.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q04 — D

**Question:** The backend readiness review compares four claims for the resilient HTTP backend publication requirement to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule. Which claim is technically sound?

- **A — Incorrect.** Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules.
  Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules. In the resilient HTTP backend publication, this statement describes health probe NSG traffic. Load-balancing rules governs resilient HTTP backend publication; health probe NSG traffic cannot support load-balancing rules when operators must connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule.
- **B — Incorrect.** When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows.
  When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows. In the resilient HTTP backend publication, this statement describes all-backend probe failure. Resilient HTTP backend publication asks about load-balancing rules; this all-backend probe failure choice leaves the load-balancing rules explanation missing.
- **C — Incorrect.** A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules.
  A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules. In the resilient HTTP backend publication, this statement describes load balancer frontends. The load balancer frontends statement accurately describes load balancer frontends; however, resilient HTTP backend publication needs load-balancing rules to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule; load balancer frontends cannot replace load-balancing rules.
- **D — Correct.** A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.
  The resilient HTTP backend publication needs load-balancing rules to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule; this option states the applicable load-balancing rules rule: a load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q05 — A

**Question:** The backend readiness architecture note requires the resilient HTTP backend publication environment to allow the platform probe source while keeping other unsolicited traffic denied. Which statement defines the relevant backend readiness boundary?

- **A — Correct.** Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules.
  Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules. This health probe NSG traffic fact resolves the resilient HTTP backend publication design question about how to allow the platform probe source while keeping other unsolicited traffic denied.
- **B — Incorrect.** A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress.
  A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress. In the resilient HTTP backend publication, this statement describes outbound connectivity. The outbound connectivity statement accurately describes outbound connectivity; however, resilient HTTP backend publication needs health probe NSG traffic to allow the platform probe source while keeping other unsolicited traffic denied; outbound connectivity cannot replace health probe NSG traffic.
- **C — Incorrect.** Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information.
  Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information. In the resilient HTTP backend publication, this statement describes connection troubleshoot. Selecting connection troubleshoot for resilient HTTP backend publication leaves health probe NSG traffic unanswered in resilient HTTP backend publication; the resilient HTTP backend publication lacks a health probe NSG traffic basis to allow the platform probe source while keeping other unsolicited traffic denied.
- **D — Incorrect.** A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows.
  A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows. In the resilient HTTP backend publication, this statement describes backend address pools. Health probe NSG traffic governs resilient HTTP backend publication; backend address pools cannot support health probe NSG traffic when operators must allow the platform probe source while keeping other unsolicited traffic denied.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q06 — A

**Question:** A new backend readiness operator must explain why the resilient HTTP backend publication can provide explicit outbound connectivity for a Standard load-balanced backend. Which explanation is accurate?

- **A — Correct.** A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress.
  A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress. For resilient HTTP backend publication, outbound connectivity supplies the service rule needed to provide explicit outbound connectivity for a Standard load-balanced backend.
- **B — Incorrect.** Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence.
  Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence. In the resilient HTTP backend publication, this statement describes session persistence. Selecting session persistence for resilient HTTP backend publication leaves outbound connectivity unanswered in resilient HTTP backend publication; the resilient HTTP backend publication lacks a outbound connectivity basis to provide explicit outbound connectivity for a Standard load-balanced backend.
- **C — Incorrect.** Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.
  Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time. In the resilient HTTP backend publication, this statement describes Connection Monitor. Outbound connectivity governs resilient HTTP backend publication; Connection Monitor cannot support outbound connectivity when operators must provide explicit outbound connectivity for a Standard load-balanced backend.
- **D — Incorrect.** A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows.
  A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows. In the resilient HTTP backend publication, this statement describes health probes. Resilient HTTP backend publication asks about outbound connectivity; this health probes choice leaves the outbound connectivity explanation missing.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Outbound rules for Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/outbound-rules)

**Source reviewed:** 2026-08-31

## LAB21-Q07 — C

**Question:** The resilient HTTP backend publication acceptance criteria require operators to keep successive flows from one client on the affinity mode the application expects. Which service fact supports that requirement?

- **A — Incorrect.** When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows.
  When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows. In the resilient HTTP backend publication, this statement describes all-backend probe failure. Selecting all-backend probe failure for resilient HTTP backend publication leaves session persistence unanswered in resilient HTTP backend publication; the resilient HTTP backend publication lacks a session persistence basis to keep successive flows from one client on the affinity mode the application expects.
- **B — Incorrect.** A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules.
  A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules. In the resilient HTTP backend publication, this statement describes load balancer frontends. Session persistence governs resilient HTTP backend publication; load balancer frontends cannot support session persistence when operators must keep successive flows from one client on the affinity mode the application expects.
- **C — Correct.** Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence.
  Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence. In the resilient HTTP backend publication, this session persistence rule supports the need to keep successive flows from one client on the affinity mode the application expects.
- **D — Incorrect.** A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.
  A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path. In the resilient HTTP backend publication, this statement describes load-balancing rules. The load-balancing rules statement accurately describes load-balancing rules; however, resilient HTTP backend publication needs session persistence to keep successive flows from one client on the affinity mode the application expects; load-balancing rules cannot replace session persistence.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Load Balancer distribution mode](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-distribution-mode)

**Source reviewed:** 2026-08-31

## LAB21-Q08 — C

**Question:** A backend readiness reviewer challenges whether the resilient HTTP backend publication can explain why no new client flow is sent when every target fails its probe. Which response resolves the concern?

- **A — Incorrect.** Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information.
  Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information. In the resilient HTTP backend publication, this statement describes connection troubleshoot. All-backend probe failure governs resilient HTTP backend publication; connection troubleshoot cannot support all-backend probe failure when operators must explain why no new client flow is sent when every target fails its probe.
- **B — Incorrect.** A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows.
  A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows. In the resilient HTTP backend publication, this statement describes backend address pools. Resilient HTTP backend publication asks about all-backend probe failure; this backend address pools choice leaves the all-backend probe failure explanation missing.
- **C — Correct.** When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows.
  For the resilient HTTP backend publication, the rule for all-backend probe failure is defined by this statement: when every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows. It supports the required outcome to explain why no new client flow is sent when every target fails its probe.
- **D — Incorrect.** Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules.
  Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules. In the resilient HTTP backend publication, this statement describes health probe NSG traffic. Selecting health probe NSG traffic for resilient HTTP backend publication leaves all-backend probe failure unanswered in resilient HTTP backend publication; the resilient HTTP backend publication lacks a all-backend probe failure basis to explain why no new client flow is sent when every target fails its probe.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q09 — C

**Question:** The resilient HTTP backend publication handoff omits the backend readiness rule needed to test reachability between two endpoints and return the responsible hop or policy. Which statement should the team add?

- **A — Incorrect.** Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.
  Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time. In the resilient HTTP backend publication, this statement describes Connection Monitor. Resilient HTTP backend publication asks about connection troubleshoot; this Connection Monitor choice leaves the connection troubleshoot explanation missing.
- **B — Incorrect.** A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows.
  A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows. In the resilient HTTP backend publication, this statement describes health probes. The health probes statement accurately describes health probes; however, resilient HTTP backend publication needs connection troubleshoot to test reachability between two endpoints and return the responsible hop or policy; health probes cannot replace connection troubleshoot.
- **C — Correct.** Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information.
  Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information. The resilient HTTP backend publication applies that connection troubleshoot boundary when operators must test reachability between two endpoints and return the responsible hop or policy.
- **D — Incorrect.** A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress.
  A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress. In the resilient HTTP backend publication, this statement describes outbound connectivity. Connection troubleshoot governs resilient HTTP backend publication; outbound connectivity cannot support connection troubleshoot when operators must test reachability between two endpoints and return the responsible hop or policy.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Network Watcher connection troubleshoot](https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q10 — B

**Question:** A backend readiness incident review of the resilient HTTP backend publication depends on the ability to measure connection reachability and latency continuously over time. Which platform description is reliable?

- **A — Incorrect.** A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules.
  A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules. In the resilient HTTP backend publication, this statement describes load balancer frontends. The load balancer frontends statement accurately describes load balancer frontends; however, resilient HTTP backend publication needs Connection Monitor to measure connection reachability and latency continuously over time; load balancer frontends cannot replace Connection Monitor.
- **B — Correct.** Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.
  The resilient HTTP backend publication needs Connection Monitor to measure connection reachability and latency continuously over time; this option states the applicable Connection Monitor rule: connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.
- **C — Incorrect.** A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.
  A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path. In the resilient HTTP backend publication, this statement describes load-balancing rules. Connection Monitor governs resilient HTTP backend publication; load-balancing rules cannot support Connection Monitor when operators must measure connection reachability and latency continuously over time.
- **D — Incorrect.** Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence.
  Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence. In the resilient HTTP backend publication, this statement describes session persistence. Resilient HTTP backend publication asks about Connection Monitor; this session persistence choice leaves the Connection Monitor explanation missing.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q11 — D

**Question:** A backend readiness ticket in the resilient HTTP backend publication says to expose one ingress IP for incoming balanced traffic. Which backend readiness action completes the resilient HTTP backend publication request with minimal change?

- **A — Incorrect.** Configure a probe that reflects actual application readiness rather than only host availability.
  Configure a probe that reflects actual application readiness rather than only host availability. In the resilient HTTP backend publication, this action changes health probes. Resilient HTTP backend publication approved load balancer frontends, not health probes; only the load balancer frontends change can expose one ingress IP for incoming balanced traffic.
- **B — Incorrect.** Configure the approved outbound method and size SNAT capacity for expected concurrency.
  Configure the approved outbound method and size SNAT capacity for expected concurrency. In the resilient HTTP backend publication, this action changes outbound connectivity. Resilient HTTP backend publication requires load balancer frontends; changing outbound connectivity leaves load balancer frontends absent in resilient HTTP backend publication; resilient HTTP backend publication cannot expose one ingress IP for incoming balanced traffic.
- **C — Incorrect.** Run the diagnostic from the actual source resource to the exact destination and port.
  Run the diagnostic from the actual source resource to the exact destination and port. In the resilient HTTP backend publication, this action changes connection troubleshoot. Connection troubleshoot does not implement load balancer frontends for resilient HTTP backend publication; the resilient HTTP backend publication still cannot expose one ingress IP for incoming balanced traffic.
- **D — Correct.** Create a public or internal frontend that matches the approved reachability requirement.
  Create a public or internal frontend that matches the approved reachability requirement. It is the least-change load balancer frontends path for the resilient HTTP backend publication requirement to expose one ingress IP for incoming balanced traffic.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q12 — D

**Question:** The approach for the resilient HTTP backend publication is approved, but the backend readiness environment still cannot register every serving network interface as an eligible target. Which implementation step closes the gap?

- **A — Incorrect.** Create the rule with resource IDs from the intended frontend, backend pool, and health probe.
  Create the rule with resource IDs from the intended frontend, backend pool, and health probe. In the resilient HTTP backend publication, this action changes load-balancing rules. Resilient HTTP backend publication requires backend address pools; changing load-balancing rules leaves backend address pools absent in resilient HTTP backend publication; resilient HTTP backend publication cannot register every serving network interface as an eligible target.
- **B — Incorrect.** Choose the distribution mode only when the application requires client affinity.
  Choose the distribution mode only when the application requires client affinity. In the resilient HTTP backend publication, this action changes session persistence. Session persistence does not implement backend address pools for resilient HTTP backend publication; the resilient HTTP backend publication still cannot register every serving network interface as an eligible target.
- **C — Incorrect.** Create a test group with representative endpoints, protocol, port, frequency, and success thresholds.
  Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. In the resilient HTTP backend publication, this action changes Connection Monitor. Resilient HTTP backend publication instead needs backend address pools: Add every intended healthy backend and exclude maintenance instances before production traffic. The Connection Monitor action omits that backend address pools work.
- **D — Correct.** Add every intended healthy backend and exclude maintenance instances before production traffic.
  Add every intended healthy backend and exclude maintenance instances before production traffic. In resilient HTTP backend publication, applying backend address pools is the scoped way to register every serving network interface as an eligible target.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q13 — B

**Question:** The network operations administrator publishing a resilient HTTP backend may change the resilient HTTP backend publication only to remove an instance from rotation when its application endpoint is unhealthy. Which backend readiness action stays within that assignment?

- **A — Incorrect.** Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application.
  Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. In the resilient HTTP backend publication, this action changes health probe NSG traffic. Health probe NSG traffic does not implement health probes for resilient HTTP backend publication; the resilient HTTP backend publication still cannot remove an instance from rotation when its application endpoint is unhealthy.
- **B — Correct.** Configure a probe that reflects actual application readiness rather than only host availability.
  Configure a probe that reflects actual application readiness rather than only host availability. The resilient HTTP backend publication uses this health probes operation to remove an instance from rotation when its application endpoint is unhealthy within the approved scope.
- **C — Incorrect.** Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend.
  Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. In the resilient HTTP backend publication, this action changes all-backend probe failure. Resilient HTTP backend publication approved health probes, not all-backend probe failure; only the health probes change can remove an instance from rotation when its application endpoint is unhealthy.
- **D — Incorrect.** Create a public or internal frontend that matches the approved reachability requirement.
  Create a public or internal frontend that matches the approved reachability requirement. In the resilient HTTP backend publication, this action changes load balancer frontends. Resilient HTTP backend publication requires health probes; changing load balancer frontends leaves health probes absent in resilient HTTP backend publication; resilient HTTP backend publication cannot remove an instance from rotation when its application endpoint is unhealthy.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q14 — A

**Question:** A backend readiness dry run shows no resilient HTTP backend publication command will connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule. Which action belongs before execution?

- **A — Correct.** Create the rule with resource IDs from the intended frontend, backend pool, and health probe.
  For the resilient HTTP backend publication, the required load-balancing rules action is: create the rule with resource IDs from the intended frontend, backend pool, and health probe. It makes the environment able to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule.
- **B — Incorrect.** Configure the approved outbound method and size SNAT capacity for expected concurrency.
  Configure the approved outbound method and size SNAT capacity for expected concurrency. In the resilient HTTP backend publication, this action changes outbound connectivity. Resilient HTTP backend publication approved load-balancing rules, not outbound connectivity; only the load-balancing rules change can connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule.
- **C — Incorrect.** Run the diagnostic from the actual source resource to the exact destination and port.
  Run the diagnostic from the actual source resource to the exact destination and port. In the resilient HTTP backend publication, this action changes connection troubleshoot. Resilient HTTP backend publication requires load-balancing rules; changing connection troubleshoot leaves load-balancing rules absent in resilient HTTP backend publication; resilient HTTP backend publication cannot connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule.
- **D — Incorrect.** Add every intended healthy backend and exclude maintenance instances before production traffic.
  Add every intended healthy backend and exclude maintenance instances before production traffic. In the resilient HTTP backend publication, this action changes backend address pools. Backend address pools does not implement load-balancing rules for resilient HTTP backend publication; the resilient HTTP backend publication still cannot connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q15 — B

**Question:** For the resilient HTTP backend publication, operators need to allow the platform probe source while keeping other unsolicited traffic denied. Which change realizes that requirement?

- **A — Incorrect.** Choose the distribution mode only when the application requires client affinity.
  Choose the distribution mode only when the application requires client affinity. In the resilient HTTP backend publication, this action changes session persistence. Resilient HTTP backend publication approved health probe NSG traffic, not session persistence; only the health probe NSG traffic change can allow the platform probe source while keeping other unsolicited traffic denied.
- **B — Correct.** Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application.
  Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. This changes health probe NSG traffic in the resilient HTTP backend publication, supplying the missing state needed to allow the platform probe source while keeping other unsolicited traffic denied.
- **C — Incorrect.** Create a test group with representative endpoints, protocol, port, frequency, and success thresholds.
  Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. In the resilient HTTP backend publication, this action changes Connection Monitor. Connection Monitor does not implement health probe NSG traffic for resilient HTTP backend publication; the resilient HTTP backend publication still cannot allow the platform probe source while keeping other unsolicited traffic denied.
- **D — Incorrect.** Configure a probe that reflects actual application readiness rather than only host availability.
  Configure a probe that reflects actual application readiness rather than only host availability. In the resilient HTTP backend publication, this action changes health probes. Resilient HTTP backend publication instead needs health probe NSG traffic: Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. The health probes action omits that health probe NSG traffic work.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q16 — A

**Question:** Operators must automate the resilient HTTP backend publication change needed to provide explicit outbound connectivity for a Standard load-balanced backend. Which backend readiness operation belongs in the runbook?

- **A — Correct.** Configure the approved outbound method and size SNAT capacity for expected concurrency.
  The resilient HTTP backend publication must provide explicit outbound connectivity for a Standard load-balanced backend; this option performs its direct outbound connectivity change: configure the approved outbound method and size SNAT capacity for expected concurrency.
- **B — Incorrect.** Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend.
  Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. In the resilient HTTP backend publication, this action changes all-backend probe failure. All-backend probe failure does not implement outbound connectivity for resilient HTTP backend publication; the resilient HTTP backend publication still cannot provide explicit outbound connectivity for a Standard load-balanced backend.
- **C — Incorrect.** Create a public or internal frontend that matches the approved reachability requirement.
  Create a public or internal frontend that matches the approved reachability requirement. In the resilient HTTP backend publication, this action changes load balancer frontends. Resilient HTTP backend publication instead needs outbound connectivity: Configure the approved outbound method and size SNAT capacity for expected concurrency. The load balancer frontends action omits that outbound connectivity work.
- **D — Incorrect.** Create the rule with resource IDs from the intended frontend, backend pool, and health probe.
  Create the rule with resource IDs from the intended frontend, backend pool, and health probe. In the resilient HTTP backend publication, this action changes load-balancing rules. Resilient HTTP backend publication approved outbound connectivity, not load-balancing rules; only the outbound connectivity change can provide explicit outbound connectivity for a Standard load-balanced backend.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Outbound rules for Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/outbound-rules)

**Source reviewed:** 2026-08-31

## LAB21-Q17 — D

**Question:** A resilient HTTP backend publication review finds backend readiness drift from the need to keep successive flows from one client on the affinity mode the application expects. Which correction addresses that drift?

- **A — Incorrect.** Run the diagnostic from the actual source resource to the exact destination and port.
  Run the diagnostic from the actual source resource to the exact destination and port. In the resilient HTTP backend publication, this action changes connection troubleshoot. Connection troubleshoot does not implement session persistence for resilient HTTP backend publication; the resilient HTTP backend publication still cannot keep successive flows from one client on the affinity mode the application expects.
- **B — Incorrect.** Add every intended healthy backend and exclude maintenance instances before production traffic.
  Add every intended healthy backend and exclude maintenance instances before production traffic. In the resilient HTTP backend publication, this action changes backend address pools. Resilient HTTP backend publication instead needs session persistence: Choose the distribution mode only when the application requires client affinity. The backend address pools action omits that session persistence work.
- **C — Incorrect.** Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application.
  Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. In the resilient HTTP backend publication, this action changes health probe NSG traffic. Resilient HTTP backend publication approved session persistence, not health probe NSG traffic; only the session persistence change can keep successive flows from one client on the affinity mode the application expects.
- **D — Correct.** Choose the distribution mode only when the application requires client affinity.
  Choose the distribution mode only when the application requires client affinity. It is the least-change session persistence path for the resilient HTTP backend publication requirement to keep successive flows from one client on the affinity mode the application expects.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Load Balancer distribution mode](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-distribution-mode)

**Source reviewed:** 2026-08-31

## LAB21-Q18 — B

**Question:** The resilient HTTP backend publication window permits only the backend readiness change needed to explain why no new client flow is sent when every target fails its probe. Which option respects the boundary?

- **A — Incorrect.** Create a test group with representative endpoints, protocol, port, frequency, and success thresholds.
  Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. In the resilient HTTP backend publication, this action changes Connection Monitor. Resilient HTTP backend publication instead needs all-backend probe failure: Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. The Connection Monitor action omits that all-backend probe failure work.
- **B — Correct.** Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend.
  Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. In resilient HTTP backend publication, applying all-backend probe failure is the scoped way to explain why no new client flow is sent when every target fails its probe.
- **C — Incorrect.** Configure a probe that reflects actual application readiness rather than only host availability.
  Configure a probe that reflects actual application readiness rather than only host availability. In the resilient HTTP backend publication, this action changes health probes. Resilient HTTP backend publication requires all-backend probe failure; changing health probes leaves all-backend probe failure absent in resilient HTTP backend publication; resilient HTTP backend publication cannot explain why no new client flow is sent when every target fails its probe.
- **D — Incorrect.** Configure the approved outbound method and size SNAT capacity for expected concurrency.
  Configure the approved outbound method and size SNAT capacity for expected concurrency. In the resilient HTTP backend publication, this action changes outbound connectivity. Outbound connectivity does not implement all-backend probe failure for resilient HTTP backend publication; the resilient HTTP backend publication still cannot explain why no new client flow is sent when every target fails its probe.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q19 — B

**Question:** The backend readiness preflight has passed; the resilient HTTP backend publication must now test reachability between two endpoints and return the responsible hop or policy. Which operation should run?

- **A — Incorrect.** Create a public or internal frontend that matches the approved reachability requirement.
  Create a public or internal frontend that matches the approved reachability requirement. In the resilient HTTP backend publication, this action changes load balancer frontends. Resilient HTTP backend publication approved connection troubleshoot, not load balancer frontends; only the connection troubleshoot change can test reachability between two endpoints and return the responsible hop or policy.
- **B — Correct.** Run the diagnostic from the actual source resource to the exact destination and port.
  Run the diagnostic from the actual source resource to the exact destination and port. The resilient HTTP backend publication uses this connection troubleshoot operation to test reachability between two endpoints and return the responsible hop or policy within the approved scope.
- **C — Incorrect.** Create the rule with resource IDs from the intended frontend, backend pool, and health probe.
  Create the rule with resource IDs from the intended frontend, backend pool, and health probe. In the resilient HTTP backend publication, this action changes load-balancing rules. Load-balancing rules does not implement connection troubleshoot for resilient HTTP backend publication; the resilient HTTP backend publication still cannot test reachability between two endpoints and return the responsible hop or policy.
- **D — Incorrect.** Choose the distribution mode only when the application requires client affinity.
  Choose the distribution mode only when the application requires client affinity. In the resilient HTTP backend publication, this action changes session persistence. Resilient HTTP backend publication instead needs connection troubleshoot: Run the diagnostic from the actual source resource to the exact destination and port. The session persistence action omits that connection troubleshoot work.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Network Watcher connection troubleshoot](https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q20 — A

**Question:** The resilient HTTP backend publication plan must measure connection reachability and latency continuously over time while limiting the mutation scope to backend readiness. Which action is appropriate?

- **A — Correct.** Create a test group with representative endpoints, protocol, port, frequency, and success thresholds.
  For the resilient HTTP backend publication, the required Connection Monitor action is: create a test group with representative endpoints, protocol, port, frequency, and success thresholds. It makes the environment able to measure connection reachability and latency continuously over time.
- **B — Incorrect.** Add every intended healthy backend and exclude maintenance instances before production traffic.
  Add every intended healthy backend and exclude maintenance instances before production traffic. In the resilient HTTP backend publication, this action changes backend address pools. Backend address pools does not implement Connection Monitor for resilient HTTP backend publication; the resilient HTTP backend publication still cannot measure connection reachability and latency continuously over time.
- **C — Incorrect.** Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application.
  Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. In the resilient HTTP backend publication, this action changes health probe NSG traffic. Resilient HTTP backend publication instead needs Connection Monitor: Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. The health probe NSG traffic action omits that Connection Monitor work.
- **D — Incorrect.** Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend.
  Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. In the resilient HTTP backend publication, this action changes all-backend probe failure. Resilient HTTP backend publication approved Connection Monitor, not all-backend probe failure; only the Connection Monitor change can measure connection reachability and latency continuously over time.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q21 — B

**Question:** The resilient HTTP backend publication setup reports success after the backend readiness attempt to expose one ingress IP for incoming balanced traffic. Which backend readiness read-only observation proves the resilient HTTP backend publication outcome?

- **A — Incorrect.** Query the rule and verify every referenced component and port value.
  Query the rule and verify every referenced component and port value. In the resilient HTTP backend publication, this check observes load-balancing rules. Resilient HTTP backend publication output covers load-balancing rules, not load balancer frontends; the load balancer frontends requirement to expose one ingress IP for incoming balanced traffic remains unverified.
- **B — Correct.** Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
  Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings. Because the resilient HTTP backend publication check observes load balancer frontends, it independently verifies the requirement to expose one ingress IP for incoming balanced traffic.
- **C — Incorrect.** Query loadDistribution on the rule and test repeated flows from controlled clients.
  Query loadDistribution on the rule and test repeated flows from controlled clients. In the resilient HTTP backend publication, this check observes session persistence. Resilient HTTP backend publication reads session persistence, leaving load balancer frontends unproved in resilient HTTP backend publication; resilient HTTP backend publication still has no load balancer frontends proof.
- **D — Incorrect.** Query monitor state, test configurations, test groups, and recent reachability results.
  Query monitor state, test configurations, test groups, and recent reachability results. In the resilient HTTP backend publication, this check observes Connection Monitor. Resilient HTTP backend publication could pass Connection Monitor while load balancer frontends is wrong; resilient HTTP backend publication still lacks load balancer frontends proof.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q22 — D

**Question:** The backend readiness log says the resilient HTTP backend publication can now register every serving network interface as an eligible target. Which backend readiness state should the resilient HTTP backend publication acceptance test retain?

- **A — Incorrect.** Inspect effective NSG rules and probe health for the exact backend NIC and port.
  Inspect effective NSG rules and probe health for the exact backend NIC and port. In the resilient HTTP backend publication, this check observes health probe NSG traffic. Health probe NSG traffic success in resilient HTTP backend publication cannot verify backend address pools; resilient HTTP backend publication cannot register every serving network interface as an eligible target until backend address pools evidence exists.
- **B — Incorrect.** Correlate per-instance health with listener tests and effective security rules.
  Correlate per-instance health with listener tests and effective security rules. In the resilient HTTP backend publication, this check observes all-backend probe failure. Resilient HTTP backend publication reads all-backend probe failure, leaving backend address pools unproved in resilient HTTP backend publication; resilient HTTP backend publication still has no backend address pools proof.
- **C — Incorrect.** Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
  Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings. In the resilient HTTP backend publication, this check observes load balancer frontends. Resilient HTTP backend publication could pass load balancer frontends while backend address pools is wrong; resilient HTTP backend publication still lacks backend address pools proof.
- **D — Correct.** Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
  The resilient HTTP backend publication validator needs this backend address pools result: query backendAddressPools and resolve each backend membership to the expected VM NIC or IP. It proves the outcome to register every serving network interface as an eligible target rather than an adjacent checkpoint.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q23 — C

**Question:** The resilient HTTP backend publication rejects backend readiness exit status as proof it can remove an instance from rotation when its application endpoint is unhealthy. Which resilient HTTP backend publication result is valid evidence?

- **A — Incorrect.** Query outbound rules or NAT Gateway association and test backend egress independently.
  Query outbound rules or NAT Gateway association and test backend egress independently. In the resilient HTTP backend publication, this check observes outbound connectivity. Resilient HTTP backend publication reads outbound connectivity, leaving health probes unproved in resilient HTTP backend publication; resilient HTTP backend publication still has no health probes proof.
- **B — Incorrect.** Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
  Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages. In the resilient HTTP backend publication, this check observes connection troubleshoot. Resilient HTTP backend publication could pass connection troubleshoot while health probes is wrong; resilient HTTP backend publication still lacks health probes proof.
- **C — Correct.** Query probe protocol, port, path, interval, threshold, and backend health status.
  Query probe protocol, port, path, interval, threshold, and backend health status. This is independent health probes evidence for the resilient HTTP backend publication, even if resilient HTTP backend publication setup reports success before health probes becomes observable.
- **D — Incorrect.** Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
  Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP. In the resilient HTTP backend publication, this check observes backend address pools. Backend address pools success in resilient HTTP backend publication cannot verify health probes; resilient HTTP backend publication cannot remove an instance from rotation when its application endpoint is unhealthy until health probes evidence exists.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q24 — D

**Question:** The backend readiness validator needs one resilient HTTP backend publication query after the change to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule. Which backend readiness property should the resilient HTTP backend publication validator inspect?

- **A — Incorrect.** Query loadDistribution on the rule and test repeated flows from controlled clients.
  Query loadDistribution on the rule and test repeated flows from controlled clients. In the resilient HTTP backend publication, this check observes session persistence. Resilient HTTP backend publication could pass session persistence while load-balancing rules is wrong; resilient HTTP backend publication still lacks load-balancing rules proof.
- **B — Incorrect.** Query monitor state, test configurations, test groups, and recent reachability results.
  Query monitor state, test configurations, test groups, and recent reachability results. In the resilient HTTP backend publication, this check observes Connection Monitor. Resilient HTTP backend publication output covers Connection Monitor, not load-balancing rules; the load-balancing rules requirement to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule remains unverified.
- **C — Incorrect.** Query probe protocol, port, path, interval, threshold, and backend health status.
  Query probe protocol, port, path, interval, threshold, and backend health status. In the resilient HTTP backend publication, this check observes health probes. Health probes success in resilient HTTP backend publication cannot verify load-balancing rules; resilient HTTP backend publication cannot connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule until load-balancing rules evidence exists.
- **D — Correct.** Query the rule and verify every referenced component and port value.
  Query the rule and verify every referenced component and port value. For resilient HTTP backend publication, this load-balancing rules read confirms the service can connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q25 — A

**Question:** The network operations administrator publishing a resilient HTTP backend must confirm the resilient HTTP backend publication, without mutation, can allow the platform probe source while keeping other unsolicited traffic denied. Which backend readiness check qualifies?

- **A — Correct.** Inspect effective NSG rules and probe health for the exact backend NIC and port.
  Inspect effective NSG rules and probe health for the exact backend NIC and port. The resilient HTTP backend publication reads health probe NSG traffic directly; that health probe NSG traffic result proves the resilient HTTP backend publication can allow the platform probe source while keeping other unsolicited traffic denied without another mutation.
- **B — Incorrect.** Correlate per-instance health with listener tests and effective security rules.
  Correlate per-instance health with listener tests and effective security rules. In the resilient HTTP backend publication, this check observes all-backend probe failure. All-backend probe failure success in resilient HTTP backend publication cannot verify health probe NSG traffic; resilient HTTP backend publication cannot allow the platform probe source while keeping other unsolicited traffic denied until health probe NSG traffic evidence exists.
- **C — Incorrect.** Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
  Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings. In the resilient HTTP backend publication, this check observes load balancer frontends. Resilient HTTP backend publication reads load balancer frontends, leaving health probe NSG traffic unproved in resilient HTTP backend publication; resilient HTTP backend publication still has no health probe NSG traffic proof.
- **D — Incorrect.** Query the rule and verify every referenced component and port value.
  Query the rule and verify every referenced component and port value. In the resilient HTTP backend publication, this check observes load-balancing rules. Resilient HTTP backend publication could pass load-balancing rules while health probe NSG traffic is wrong; resilient HTTP backend publication still lacks health probe NSG traffic proof.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q26 — B

**Question:** The resilient HTTP backend publication configuration is complete; the backend readiness reviewers need evidence it can provide explicit outbound connectivity for a Standard load-balanced backend. Which observation shows success?

- **A — Incorrect.** Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
  Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages. In the resilient HTTP backend publication, this check observes connection troubleshoot. Connection troubleshoot success in resilient HTTP backend publication cannot verify outbound connectivity; resilient HTTP backend publication cannot provide explicit outbound connectivity for a Standard load-balanced backend until outbound connectivity evidence exists.
- **B — Correct.** Query outbound rules or NAT Gateway association and test backend egress independently.
  For the resilient HTTP backend publication, this outbound connectivity observation is decisive: query outbound rules or NAT Gateway association and test backend egress independently. It is resilient HTTP backend publication evidence that operators can provide explicit outbound connectivity for a Standard load-balanced backend.
- **C — Incorrect.** Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
  Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP. In the resilient HTTP backend publication, this check observes backend address pools. Resilient HTTP backend publication could pass backend address pools while outbound connectivity is wrong; resilient HTTP backend publication still lacks outbound connectivity proof.
- **D — Incorrect.** Inspect effective NSG rules and probe health for the exact backend NIC and port.
  Inspect effective NSG rules and probe health for the exact backend NIC and port. In the resilient HTTP backend publication, this check observes health probe NSG traffic. Resilient HTTP backend publication output covers health probe NSG traffic, not outbound connectivity; the outbound connectivity requirement to provide explicit outbound connectivity for a Standard load-balanced backend remains unverified.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Outbound rules for Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/outbound-rules)

**Source reviewed:** 2026-08-31

## LAB21-Q27 — D

**Question:** The backend readiness validation asks whether the resilient HTTP backend publication can keep successive flows from one client on the affinity mode the application expects. Which observable state is strongest?

- **A — Incorrect.** Query monitor state, test configurations, test groups, and recent reachability results.
  Query monitor state, test configurations, test groups, and recent reachability results. In the resilient HTTP backend publication, this check observes Connection Monitor. Resilient HTTP backend publication reads Connection Monitor, leaving session persistence unproved in resilient HTTP backend publication; resilient HTTP backend publication still has no session persistence proof.
- **B — Incorrect.** Query probe protocol, port, path, interval, threshold, and backend health status.
  Query probe protocol, port, path, interval, threshold, and backend health status. In the resilient HTTP backend publication, this check observes health probes. Resilient HTTP backend publication could pass health probes while session persistence is wrong; resilient HTTP backend publication still lacks session persistence proof.
- **C — Incorrect.** Query outbound rules or NAT Gateway association and test backend egress independently.
  Query outbound rules or NAT Gateway association and test backend egress independently. In the resilient HTTP backend publication, this check observes outbound connectivity. Resilient HTTP backend publication output covers outbound connectivity, not session persistence; the session persistence requirement to keep successive flows from one client on the affinity mode the application expects remains unverified.
- **D — Correct.** Query loadDistribution on the rule and test repeated flows from controlled clients.
  Query loadDistribution on the rule and test repeated flows from controlled clients. Because the resilient HTTP backend publication check observes session persistence, it independently verifies the requirement to keep successive flows from one client on the affinity mode the application expects.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Load Balancer distribution mode](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-distribution-mode)

**Source reviewed:** 2026-08-31

## LAB21-Q28 — D

**Question:** A resilient HTTP backend publication review must prove the backend readiness ability to explain why no new client flow is sent when every target fails its probe. Which check avoids an adjacent feature?

- **A — Incorrect.** Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
  Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings. In the resilient HTTP backend publication, this check observes load balancer frontends. Resilient HTTP backend publication could pass load balancer frontends while all-backend probe failure is wrong; resilient HTTP backend publication still lacks all-backend probe failure proof.
- **B — Incorrect.** Query the rule and verify every referenced component and port value.
  Query the rule and verify every referenced component and port value. In the resilient HTTP backend publication, this check observes load-balancing rules. Resilient HTTP backend publication output covers load-balancing rules, not all-backend probe failure; the all-backend probe failure requirement to explain why no new client flow is sent when every target fails its probe remains unverified.
- **C — Incorrect.** Query loadDistribution on the rule and test repeated flows from controlled clients.
  Query loadDistribution on the rule and test repeated flows from controlled clients. In the resilient HTTP backend publication, this check observes session persistence. Session persistence success in resilient HTTP backend publication cannot verify all-backend probe failure; resilient HTTP backend publication cannot explain why no new client flow is sent when every target fails its probe until all-backend probe failure evidence exists.
- **D — Correct.** Correlate per-instance health with listener tests and effective security rules.
  The resilient HTTP backend publication validator needs this all-backend probe failure result: correlate per-instance health with listener tests and effective security rules. It proves the outcome to explain why no new client flow is sent when every target fails its probe rather than an adjacent checkpoint.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q29 — C

**Question:** The resilient HTTP backend publication evidence bundle needs a backend readiness result showing it can test reachability between two endpoints and return the responsible hop or policy. Which result belongs in the checkpoint?

- **A — Incorrect.** Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
  Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP. In the resilient HTTP backend publication, this check observes backend address pools. Resilient HTTP backend publication output covers backend address pools, not connection troubleshoot; the connection troubleshoot requirement to test reachability between two endpoints and return the responsible hop or policy remains unverified.
- **B — Incorrect.** Inspect effective NSG rules and probe health for the exact backend NIC and port.
  Inspect effective NSG rules and probe health for the exact backend NIC and port. In the resilient HTTP backend publication, this check observes health probe NSG traffic. Health probe NSG traffic success in resilient HTTP backend publication cannot verify connection troubleshoot; resilient HTTP backend publication cannot test reachability between two endpoints and return the responsible hop or policy until connection troubleshoot evidence exists.
- **C — Correct.** Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
  Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages. This is independent connection troubleshoot evidence for the resilient HTTP backend publication, even if resilient HTTP backend publication setup reports success before connection troubleshoot becomes observable.
- **D — Incorrect.** Correlate per-instance health with listener tests and effective security rules.
  Correlate per-instance health with listener tests and effective security rules. In the resilient HTTP backend publication, this check observes all-backend probe failure. Resilient HTTP backend publication could pass all-backend probe failure while connection troubleshoot is wrong; resilient HTTP backend publication still lacks connection troubleshoot proof.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Network Watcher connection troubleshoot](https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q30 — C

**Question:** Before resilient HTTP backend publication cleanup, the backend readiness team must reconfirm it can measure connection reachability and latency continuously over time. Which read-only inspection should run?

- **A — Incorrect.** Query probe protocol, port, path, interval, threshold, and backend health status.
  Query probe protocol, port, path, interval, threshold, and backend health status. In the resilient HTTP backend publication, this check observes health probes. Health probes success in resilient HTTP backend publication cannot verify Connection Monitor; resilient HTTP backend publication cannot measure connection reachability and latency continuously over time until Connection Monitor evidence exists.
- **B — Incorrect.** Query outbound rules or NAT Gateway association and test backend egress independently.
  Query outbound rules or NAT Gateway association and test backend egress independently. In the resilient HTTP backend publication, this check observes outbound connectivity. Resilient HTTP backend publication reads outbound connectivity, leaving Connection Monitor unproved in resilient HTTP backend publication; resilient HTTP backend publication still has no Connection Monitor proof.
- **C — Correct.** Query monitor state, test configurations, test groups, and recent reachability results.
  Query monitor state, test configurations, test groups, and recent reachability results. For resilient HTTP backend publication, this Connection Monitor read confirms the service can measure connection reachability and latency continuously over time.
- **D — Incorrect.** Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
  Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages. In the resilient HTTP backend publication, this check observes connection troubleshoot. Resilient HTTP backend publication output covers connection troubleshoot, not Connection Monitor; the Connection Monitor requirement to measure connection reachability and latency continuously over time remains unverified.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q31 — A

**Question:** During a backend readiness fault drill, the resilient HTTP backend publication does not expose one ingress IP for incoming balanced traffic. Which finding identifies the defect?

- **A — Correct.** An internal-only service was assigned a public frontend IP.
  An internal-only service was assigned a public frontend IP. This resilient HTTP backend publication condition breaks load balancer frontends, explaining why operators cannot expose one ingress IP for incoming balanced traffic.
- **B — Incorrect.** The new VM exists but its NIC is not a member of the load balancer backend pool.
  The new VM exists but its NIC is not a member of the load balancer backend pool. The resilient HTTP backend publication fault concerns backend address pools. Resilient HTTP backend publication could repair backend address pools while load balancer frontends stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to expose one ingress IP for incoming balanced traffic.
- **C — Incorrect.** Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design.
  Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design. The resilient HTTP backend publication fault concerns outbound connectivity. Resilient HTTP backend publication failed on load balancer frontends; this outbound connectivity finding redirects resilient HTTP backend publication remediation away from load balancer frontends.
- **D — Incorrect.** The monitor has no enabled source endpoint in its test group.
  The monitor has no enabled source endpoint in its test group. The resilient HTTP backend publication fault concerns Connection Monitor. Resilient HTTP backend publication may fix Connection Monitor, yet load balancer frontends still fails; this resilient HTTP backend publication diagnosis of Connection Monitor is wrong for load balancer frontends.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q32 — C

**Question:** The resilient HTTP backend publication setup finishes, yet the backend readiness cannot register every serving network interface as an eligible target. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The HTTP probe path returns a failure status even though the application root path works.
  The HTTP probe path returns a failure status even though the application root path works. The resilient HTTP backend publication fault concerns health probes. Resilient HTTP backend publication could repair health probes while backend address pools stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to register every serving network interface as an eligible target.
- **B — Incorrect.** The application expects client affinity while the rule uses the default five-tuple distribution.
  The application expects client affinity while the rule uses the default five-tuple distribution. The resilient HTTP backend publication fault concerns session persistence. Resilient HTTP backend publication failed on backend address pools; this session persistence finding redirects resilient HTTP backend publication remediation away from backend address pools.
- **C — Correct.** The new VM exists but its NIC is not a member of the load balancer backend pool.
  For the resilient HTTP backend publication, the backend address pools failure is causal: the new VM exists but its NIC is not a member of the load balancer backend pool. Correcting it restores the ability to register every serving network interface as an eligible target.
- **D — Incorrect.** An internal-only service was assigned a public frontend IP.
  An internal-only service was assigned a public frontend IP. The resilient HTTP backend publication fault concerns load balancer frontends. Resilient HTTP backend publication has load balancer frontends impact, but backend address pools is the resilient HTTP backend publication failed path; the load balancer frontends state cannot produce backend address pools failure.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q33 — B

**Question:** A backend readiness break/fix in the resilient HTTP backend publication fails when operators try to remove an instance from rotation when its application endpoint is unhealthy. Which diagnosis fits?

- **A — Incorrect.** The rule references a probe for a different backend application port.
  The rule references a probe for a different backend application port. The resilient HTTP backend publication fault concerns load-balancing rules. Resilient HTTP backend publication failed on health probes; this load-balancing rules finding redirects resilient HTTP backend publication remediation away from health probes.
- **B — Correct.** The HTTP probe path returns a failure status even though the application root path works.
  The HTTP probe path returns a failure status even though the application root path works. The finding is specific to health probes in the resilient HTTP backend publication; repairing health probes restores the resilient HTTP backend publication ability to remove an instance from rotation when its application endpoint is unhealthy.
- **C — Incorrect.** The backend service listens on a different port from the configured probe.
  The backend service listens on a different port from the configured probe. The resilient HTTP backend publication fault concerns all-backend probe failure. Resilient HTTP backend publication has all-backend probe failure impact, but health probes is the resilient HTTP backend publication failed path; the all-backend probe failure state cannot produce health probes failure.
- **D — Incorrect.** The new VM exists but its NIC is not a member of the load balancer backend pool.
  The new VM exists but its NIC is not a member of the load balancer backend pool. The resilient HTTP backend publication fault concerns backend address pools. Resilient HTTP backend publication could repair backend address pools while health probes stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to remove an instance from rotation when its application endpoint is unhealthy.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q34 — D

**Question:** The resilient HTTP backend publication troubleshooting scope is the backend readiness need to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule. Which condition should be corrected first?

- **A — Incorrect.** A higher-priority NSG deny blocks the AzureLoadBalancer probe source.
  A higher-priority NSG deny blocks the AzureLoadBalancer probe source. The resilient HTTP backend publication fault concerns health probe NSG traffic. Resilient HTTP backend publication may fix health probe NSG traffic, yet load-balancing rules still fails; this resilient HTTP backend publication diagnosis of health probe NSG traffic is wrong for load-balancing rules.
- **B — Incorrect.** The diagnostic targeted the destination's management port instead of the failing application port.
  The diagnostic targeted the destination's management port instead of the failing application port. The resilient HTTP backend publication fault concerns connection troubleshoot. Resilient HTTP backend publication has connection troubleshoot impact, but load-balancing rules is the resilient HTTP backend publication failed path; the connection troubleshoot state cannot produce load-balancing rules failure.
- **C — Incorrect.** The HTTP probe path returns a failure status even though the application root path works.
  The HTTP probe path returns a failure status even though the application root path works. The resilient HTTP backend publication fault concerns health probes. Resilient HTTP backend publication could repair health probes while load-balancing rules stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule.
- **D — Correct.** The rule references a probe for a different backend application port.
  The resilient HTTP backend publication cannot connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule because of this load-balancing rules defect: the rule references a probe for a different backend application port. The symptom and repair align.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q35 — A

**Question:** The resilient HTTP backend publication result is partial because the backend readiness cannot allow the platform probe source while keeping other unsolicited traffic denied. Which condition accounts for that result?

- **A — Correct.** A higher-priority NSG deny blocks the AzureLoadBalancer probe source.
  A higher-priority NSG deny blocks the AzureLoadBalancer probe source. Removing this health probe NSG traffic condition lets the resilient HTTP backend publication allow the platform probe source while keeping other unsolicited traffic denied while leaving healthy controls unchanged.
- **B — Incorrect.** Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design.
  Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design. The resilient HTTP backend publication fault concerns outbound connectivity. Resilient HTTP backend publication could repair outbound connectivity while health probe NSG traffic stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to allow the platform probe source while keeping other unsolicited traffic denied.
- **C — Incorrect.** The monitor has no enabled source endpoint in its test group.
  The monitor has no enabled source endpoint in its test group. The resilient HTTP backend publication fault concerns Connection Monitor. Resilient HTTP backend publication failed on health probe NSG traffic; this Connection Monitor finding redirects resilient HTTP backend publication remediation away from health probe NSG traffic.
- **D — Incorrect.** The rule references a probe for a different backend application port.
  The rule references a probe for a different backend application port. The resilient HTTP backend publication fault concerns load-balancing rules. Resilient HTTP backend publication may fix load-balancing rules, yet health probe NSG traffic still fails; this resilient HTTP backend publication diagnosis of load-balancing rules is wrong for health probe NSG traffic.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q36 — C

**Question:** The backend readiness evidence shows the resilient HTTP backend publication cannot provide explicit outbound connectivity for a Standard load-balanced backend. Which root cause fits that evidence?

- **A — Incorrect.** The application expects client affinity while the rule uses the default five-tuple distribution.
  The application expects client affinity while the rule uses the default five-tuple distribution. The resilient HTTP backend publication fault concerns session persistence. Resilient HTTP backend publication could repair session persistence while outbound connectivity stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to provide explicit outbound connectivity for a Standard load-balanced backend.
- **B — Incorrect.** An internal-only service was assigned a public frontend IP.
  An internal-only service was assigned a public frontend IP. The resilient HTTP backend publication fault concerns load balancer frontends. Resilient HTTP backend publication failed on outbound connectivity; this load balancer frontends finding redirects resilient HTTP backend publication remediation away from outbound connectivity.
- **C — Correct.** Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design.
  Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design. In resilient HTTP backend publication, this outbound connectivity cause matches the failure to provide explicit outbound connectivity for a Standard load-balanced backend.
- **D — Incorrect.** A higher-priority NSG deny blocks the AzureLoadBalancer probe source.
  A higher-priority NSG deny blocks the AzureLoadBalancer probe source. The resilient HTTP backend publication fault concerns health probe NSG traffic. Resilient HTTP backend publication has health probe NSG traffic impact, but outbound connectivity is the resilient HTTP backend publication failed path; the health probe NSG traffic state cannot produce outbound connectivity failure.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Outbound rules for Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/outbound-rules)

**Source reviewed:** 2026-08-31

## LAB21-Q37 — C

**Question:** Although the resilient HTTP backend publication is meant to let the backend readiness keep successive flows from one client on the affinity mode the application expects, its checkpoint fails. Which backend readiness defect explains the failure?

- **A — Incorrect.** The backend service listens on a different port from the configured probe.
  The backend service listens on a different port from the configured probe. The resilient HTTP backend publication fault concerns all-backend probe failure. Resilient HTTP backend publication failed on session persistence; this all-backend probe failure finding redirects resilient HTTP backend publication remediation away from session persistence.
- **B — Incorrect.** The new VM exists but its NIC is not a member of the load balancer backend pool.
  The new VM exists but its NIC is not a member of the load balancer backend pool. The resilient HTTP backend publication fault concerns backend address pools. Resilient HTTP backend publication may fix backend address pools, yet session persistence still fails; this resilient HTTP backend publication diagnosis of backend address pools is wrong for session persistence.
- **C — Correct.** The application expects client affinity while the rule uses the default five-tuple distribution.
  The application expects client affinity while the rule uses the default five-tuple distribution. This resilient HTTP backend publication condition breaks session persistence, explaining why operators cannot keep successive flows from one client on the affinity mode the application expects.
- **D — Incorrect.** Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design.
  Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design. The resilient HTTP backend publication fault concerns outbound connectivity. Resilient HTTP backend publication could repair outbound connectivity while session persistence stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to keep successive flows from one client on the affinity mode the application expects.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Load Balancer distribution mode](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-distribution-mode)

**Source reviewed:** 2026-08-31

## LAB21-Q38 — B

**Question:** The backend readiness support team isolated the resilient HTTP backend publication incident to the attempt to explain why no new client flow is sent when every target fails its probe. Which condition prevents success?

- **A — Incorrect.** The diagnostic targeted the destination's management port instead of the failing application port.
  The diagnostic targeted the destination's management port instead of the failing application port. The resilient HTTP backend publication fault concerns connection troubleshoot. Resilient HTTP backend publication may fix connection troubleshoot, yet all-backend probe failure still fails; this resilient HTTP backend publication diagnosis of connection troubleshoot is wrong for all-backend probe failure.
- **B — Correct.** The backend service listens on a different port from the configured probe.
  For the resilient HTTP backend publication, the all-backend probe failure failure is causal: the backend service listens on a different port from the configured probe. Correcting it restores the ability to explain why no new client flow is sent when every target fails its probe.
- **C — Incorrect.** The HTTP probe path returns a failure status even though the application root path works.
  The HTTP probe path returns a failure status even though the application root path works. The resilient HTTP backend publication fault concerns health probes. Resilient HTTP backend publication could repair health probes while all-backend probe failure stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to explain why no new client flow is sent when every target fails its probe.
- **D — Incorrect.** The application expects client affinity while the rule uses the default five-tuple distribution.
  The application expects client affinity while the rule uses the default five-tuple distribution. The resilient HTTP backend publication fault concerns session persistence. Resilient HTTP backend publication failed on all-backend probe failure; this session persistence finding redirects resilient HTTP backend publication remediation away from all-backend probe failure.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q39 — A

**Question:** A resilient HTTP backend publication query surprises the network operations administrator publishing a resilient HTTP backend during the backend readiness attempt to test reachability between two endpoints and return the responsible hop or policy. Which finding explains it?

- **A — Correct.** The diagnostic targeted the destination's management port instead of the failing application port.
  The diagnostic targeted the destination's management port instead of the failing application port. The finding is specific to connection troubleshoot in the resilient HTTP backend publication; repairing connection troubleshoot restores the resilient HTTP backend publication ability to test reachability between two endpoints and return the responsible hop or policy.
- **B — Incorrect.** The monitor has no enabled source endpoint in its test group.
  The monitor has no enabled source endpoint in its test group. The resilient HTTP backend publication fault concerns Connection Monitor. Resilient HTTP backend publication could repair Connection Monitor while connection troubleshoot stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to test reachability between two endpoints and return the responsible hop or policy.
- **C — Incorrect.** The rule references a probe for a different backend application port.
  The rule references a probe for a different backend application port. The resilient HTTP backend publication fault concerns load-balancing rules. Resilient HTTP backend publication failed on connection troubleshoot; this load-balancing rules finding redirects resilient HTTP backend publication remediation away from connection troubleshoot.
- **D — Incorrect.** The backend service listens on a different port from the configured probe.
  The backend service listens on a different port from the configured probe. The resilient HTTP backend publication fault concerns all-backend probe failure. Resilient HTTP backend publication may fix all-backend probe failure, yet connection troubleshoot still fails; this resilient HTTP backend publication diagnosis of all-backend probe failure is wrong for connection troubleshoot.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Network Watcher connection troubleshoot](https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q40 — B

**Question:** Other resilient HTTP backend publication components are healthy, but the backend readiness still cannot measure connection reachability and latency continuously over time. Which state causes the isolated failure?

- **A — Incorrect.** An internal-only service was assigned a public frontend IP.
  An internal-only service was assigned a public frontend IP. The resilient HTTP backend publication fault concerns load balancer frontends. Resilient HTTP backend publication could repair load balancer frontends while Connection Monitor stays broken in resilient HTTP backend publication; the resilient HTTP backend publication remains unable to measure connection reachability and latency continuously over time.
- **B — Correct.** The monitor has no enabled source endpoint in its test group.
  The resilient HTTP backend publication cannot measure connection reachability and latency continuously over time because of this Connection Monitor defect: the monitor has no enabled source endpoint in its test group. The symptom and repair align.
- **C — Incorrect.** A higher-priority NSG deny blocks the AzureLoadBalancer probe source.
  A higher-priority NSG deny blocks the AzureLoadBalancer probe source. The resilient HTTP backend publication fault concerns health probe NSG traffic. Resilient HTTP backend publication may fix health probe NSG traffic, yet Connection Monitor still fails; this resilient HTTP backend publication diagnosis of health probe NSG traffic is wrong for Connection Monitor.
- **D — Incorrect.** The diagnostic targeted the destination's management port instead of the failing application port.
  The diagnostic targeted the destination's management port instead of the failing application port. The resilient HTTP backend publication fault concerns connection troubleshoot. Resilient HTTP backend publication has connection troubleshoot impact, but Connection Monitor is the resilient HTTP backend publication failed path; the connection troubleshoot state cannot produce Connection Monitor failure.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q41 — A

**Question:** The resilient HTTP backend publication runbook must expose one ingress IP for incoming balanced traffic, then retain backend readiness read-back evidence. Which resilient HTTP backend publication pair completes both duties?

- **A — Correct.** First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
  First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings. This ordered load balancer frontends workflow lets the resilient HTTP backend publication expose one ingress IP for incoming balanced traffic and then verify the resulting state.
- **B — Incorrect.** First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
  First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status. This resilient HTTP backend publication pair serves health probes. Resilient HTTP backend publication proves health probes, but load balancer frontends lacks implementation in resilient HTTP backend publication and load balancer frontends proof; the load balancer frontends outcome to expose one ingress IP for incoming balanced traffic remains open.
- **C — Incorrect.** First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.
  First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients. This resilient HTTP backend publication pair serves session persistence. Resilient HTTP backend publication uses session persistence for both steps; load balancer frontends remains untouched in resilient HTTP backend publication, so its load balancer frontends gate to expose one ingress IP for incoming balanced traffic fails.
- **D — Incorrect.** First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.
  First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules. This resilient HTTP backend publication pair serves all-backend probe failure. Resilient HTTP backend publication closes all-backend probe failure, not load balancer frontends; without the load balancer frontends workflow, it cannot expose one ingress IP for incoming balanced traffic.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q42 — D

**Question:** To satisfy the backend readiness requirement, operators must change the resilient HTTP backend publication configuration and prove it can register every serving network interface as an eligible target. Which sequence is coherent?

- **A — Incorrect.** First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.
  First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value. This resilient HTTP backend publication pair serves load-balancing rules. Resilient HTTP backend publication proves load-balancing rules, but backend address pools lacks implementation in resilient HTTP backend publication and backend address pools proof; the backend address pools outcome to register every serving network interface as an eligible target remains open.
- **B — Incorrect.** First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.
  First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules. This resilient HTTP backend publication pair serves all-backend probe failure. Resilient HTTP backend publication uses all-backend probe failure for both steps; backend address pools remains untouched in resilient HTTP backend publication, so its backend address pools gate to register every serving network interface as an eligible target fails.
- **C — Incorrect.** First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
  First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages. This resilient HTTP backend publication pair serves connection troubleshoot. Resilient HTTP backend publication closes connection troubleshoot, not backend address pools; without the backend address pools workflow, it cannot register every serving network interface as an eligible target.
- **D — Correct.** First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
  First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP. For resilient HTTP backend publication, the backend address pools operation precedes its backend address pools read-back check, allowing it to register every serving network interface as an eligible target.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q43 — A

**Question:** The network operations administrator publishing a resilient HTTP backend needs a safe resilient HTTP backend publication change to remove an instance from rotation when its application endpoint is unhealthy, followed by backend readiness evidence. Which pair merits approval?

- **A — Correct.** First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
  First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status. In the resilient HTTP backend publication, the first health probes step runs; the resilient HTTP backend publication then reads health probes state to prove it can remove an instance from rotation when its application endpoint is unhealthy.
- **B — Incorrect.** First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.
  First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port. This resilient HTTP backend publication pair serves health probe NSG traffic. Resilient HTTP backend publication closes health probe NSG traffic, not health probes; without the health probes workflow, it cannot remove an instance from rotation when its application endpoint is unhealthy.
- **C — Incorrect.** First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
  First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages. This resilient HTTP backend publication pair serves connection troubleshoot. Connection troubleshoot cannot replace health probes in resilient HTTP backend publication. Use this health probes pair instead: First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
- **D — Incorrect.** First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.
  First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results. This resilient HTTP backend publication pair serves Connection Monitor. Resilient HTTP backend publication proves Connection Monitor, but health probes lacks implementation in resilient HTTP backend publication and health probes proof; the health probes outcome to remove an instance from rotation when its application endpoint is unhealthy remains open.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q44 — A

**Question:** The resilient HTTP backend publication has two backend readiness gates: connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule, then prove the resilient HTTP backend publication state. Which backend readiness sequence works?

- **A — Correct.** First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.
  For the resilient HTTP backend publication, the safe load-balancing rules order is: first, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value. The resilient HTTP backend publication records load-balancing rules proof after configuration.
- **B — Incorrect.** First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently.
  First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently. This resilient HTTP backend publication pair serves outbound connectivity. Outbound connectivity cannot replace load-balancing rules in resilient HTTP backend publication. Use this load-balancing rules pair instead: First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.
- **C — Incorrect.** First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.
  First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results. This resilient HTTP backend publication pair serves Connection Monitor. Resilient HTTP backend publication proves Connection Monitor, but load-balancing rules lacks implementation in resilient HTTP backend publication and load-balancing rules proof; the load-balancing rules outcome to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule remains open.
- **D — Incorrect.** First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
  First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings. This resilient HTTP backend publication pair serves load balancer frontends. Resilient HTTP backend publication uses load balancer frontends for both steps; load-balancing rules remains untouched in resilient HTTP backend publication, so its load-balancing rules gate to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule fails.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Azure Load Balancer components](https://learn.microsoft.com/en-us/azure/load-balancer/components)

**Source reviewed:** 2026-08-31

## LAB21-Q45 — C

**Question:** Which backend readiness path makes the resilient HTTP backend publication able to allow the platform probe source while keeping other unsolicited traffic denied, then inspects the defining properties?

- **A — Incorrect.** First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.
  First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients. This resilient HTTP backend publication pair serves session persistence. Session persistence cannot replace health probe NSG traffic in resilient HTTP backend publication. Use this health probe NSG traffic pair instead: First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.
- **B — Incorrect.** First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
  First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings. This resilient HTTP backend publication pair serves load balancer frontends. Resilient HTTP backend publication proves load balancer frontends, but health probe NSG traffic lacks implementation in resilient HTTP backend publication and health probe NSG traffic proof; the health probe NSG traffic outcome to allow the platform probe source while keeping other unsolicited traffic denied remains open.
- **C — Correct.** First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.
  First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port. The resilient HTTP backend publication uses its health probe NSG traffic mutation gate and health probe NSG traffic verification gate before it can allow the platform probe source while keeping other unsolicited traffic denied.
- **D — Incorrect.** First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
  First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP. This resilient HTTP backend publication pair serves backend address pools. Resilient HTTP backend publication closes backend address pools, not health probe NSG traffic; without the health probe NSG traffic workflow, it cannot allow the platform probe source while keeping other unsolicited traffic denied.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q46 — D

**Question:** At the resilient HTTP backend publication approval gate, operators must show that the backend readiness can provide explicit outbound connectivity for a Standard load-balanced backend. Which backend readiness configure-and-check pair is defensible?

- **A — Incorrect.** First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.
  First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules. This resilient HTTP backend publication pair serves all-backend probe failure. Resilient HTTP backend publication proves all-backend probe failure, but outbound connectivity lacks implementation in resilient HTTP backend publication and outbound connectivity proof; the outbound connectivity outcome to provide explicit outbound connectivity for a Standard load-balanced backend remains open.
- **B — Incorrect.** First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
  First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP. This resilient HTTP backend publication pair serves backend address pools. Resilient HTTP backend publication uses backend address pools for both steps; outbound connectivity remains untouched in resilient HTTP backend publication, so its outbound connectivity gate to provide explicit outbound connectivity for a Standard load-balanced backend fails.
- **C — Incorrect.** First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
  First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status. This resilient HTTP backend publication pair serves health probes. Resilient HTTP backend publication closes health probes, not outbound connectivity; without the outbound connectivity workflow, it cannot provide explicit outbound connectivity for a Standard load-balanced backend.
- **D — Correct.** First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently.
  The resilient HTTP backend publication gets a complete outbound connectivity sequence here: first, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently. Read-back evidence follows the change.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB21-CP01`).

**Microsoft Learn sources:**

- [Outbound rules for Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/outbound-rules)

**Source reviewed:** 2026-08-31

## LAB21-Q47 — B

**Question:** The resilient HTTP backend publication forbids a partial backend readiness result. Operators must first keep successive flows from one client on the affinity mode the application expects and afterward confirm the resilient HTTP backend publication outcome. Which backend readiness sequence is complete?

- **A — Incorrect.** First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
  First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages. This resilient HTTP backend publication pair serves connection troubleshoot. Resilient HTTP backend publication uses connection troubleshoot for both steps; session persistence remains untouched in resilient HTTP backend publication, so its session persistence gate to keep successive flows from one client on the affinity mode the application expects fails.
- **B — Correct.** First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.
  First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients. This ordered session persistence workflow lets the resilient HTTP backend publication keep successive flows from one client on the affinity mode the application expects and then verify the resulting state.
- **C — Incorrect.** First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
  First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status. This resilient HTTP backend publication pair serves health probes. Health probes cannot replace session persistence in resilient HTTP backend publication. Use this session persistence pair instead: First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.
- **D — Incorrect.** First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.
  First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value. This resilient HTTP backend publication pair serves load-balancing rules. Resilient HTTP backend publication proves load-balancing rules, but session persistence lacks implementation in resilient HTTP backend publication and session persistence proof; the session persistence outcome to keep successive flows from one client on the affinity mode the application expects remains open.

**Objectives:** `NW-DNSLB-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB21-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Load Balancer distribution mode](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-distribution-mode)

**Source reviewed:** 2026-08-31

## LAB21-Q48 — C

**Question:** Only the resilient HTTP backend publication change needed to explain why no new client flow is sent when every target fails its probe is allowed, and backend readiness proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.
  First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results. This resilient HTTP backend publication pair serves Connection Monitor. Resilient HTTP backend publication closes Connection Monitor, not all-backend probe failure; without the all-backend probe failure workflow, it cannot explain why no new client flow is sent when every target fails its probe.
- **B — Incorrect.** First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.
  First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value. This resilient HTTP backend publication pair serves load-balancing rules. Load-balancing rules cannot replace all-backend probe failure in resilient HTTP backend publication. Use this all-backend probe failure pair instead: First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.
- **C — Correct.** First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.
  First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules. For resilient HTTP backend publication, the all-backend probe failure operation precedes its all-backend probe failure read-back check, allowing it to explain why no new client flow is sent when every target fails its probe.
- **D — Incorrect.** First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.
  First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port. This resilient HTTP backend publication pair serves health probe NSG traffic. Resilient HTTP backend publication uses health probe NSG traffic for both steps; all-backend probe failure remains untouched in resilient HTTP backend publication, so its all-backend probe failure gate to explain why no new client flow is sent when every target fails its probe fails.

**Objectives:** `NW-DNSLB-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB21-CP03`).

**Microsoft Learn sources:**

- [Troubleshoot Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status)

**Source reviewed:** 2026-08-31

## LAB21-Q49 — D

**Question:** The resilient HTTP backend publication runbook separates backend readiness mutation from validation while it must test reachability between two endpoints and return the responsible hop or policy. Which sequence proves it cleanly?

- **A — Incorrect.** First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
  First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings. This resilient HTTP backend publication pair serves load balancer frontends. Load balancer frontends cannot replace connection troubleshoot in resilient HTTP backend publication. Use this connection troubleshoot pair instead: First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
- **B — Incorrect.** First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.
  First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port. This resilient HTTP backend publication pair serves health probe NSG traffic. Resilient HTTP backend publication proves health probe NSG traffic, but connection troubleshoot lacks implementation in resilient HTTP backend publication and connection troubleshoot proof; the connection troubleshoot outcome to test reachability between two endpoints and return the responsible hop or policy remains open.
- **C — Incorrect.** First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently.
  First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently. This resilient HTTP backend publication pair serves outbound connectivity. Resilient HTTP backend publication uses outbound connectivity for both steps; connection troubleshoot remains untouched in resilient HTTP backend publication, so its connection troubleshoot gate to test reachability between two endpoints and return the responsible hop or policy fails.
- **D — Correct.** First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
  First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages. In the resilient HTTP backend publication, the first connection troubleshoot step runs; the resilient HTTP backend publication then reads connection troubleshoot state to prove it can test reachability between two endpoints and return the responsible hop or policy.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB21-CP04`).

**Microsoft Learn sources:**

- [Network Watcher connection troubleshoot](https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview)

**Source reviewed:** 2026-08-31

## LAB21-Q50 — C

**Question:** The resilient HTTP backend publication checkpoint requires both this backend readiness outcome—measure connection reachability and latency continuously over time—and a read-only resilient HTTP backend publication state check. Which backend readiness response is complete?

- **A — Incorrect.** First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
  First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP. This resilient HTTP backend publication pair serves backend address pools. Resilient HTTP backend publication proves backend address pools, but Connection Monitor lacks implementation in resilient HTTP backend publication and Connection Monitor proof; the Connection Monitor outcome to measure connection reachability and latency continuously over time remains open.
- **B — Incorrect.** First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently.
  First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently. This resilient HTTP backend publication pair serves outbound connectivity. Resilient HTTP backend publication uses outbound connectivity for both steps; Connection Monitor remains untouched in resilient HTTP backend publication, so its Connection Monitor gate to measure connection reachability and latency continuously over time fails.
- **C — Correct.** First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.
  For the resilient HTTP backend publication, the safe Connection Monitor order is: first, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results. The resilient HTTP backend publication records Connection Monitor proof after configuration.
- **D — Incorrect.** First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.
  First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients. This resilient HTTP backend publication pair serves session persistence. Session persistence cannot replace Connection Monitor in resilient HTTP backend publication. Use this Connection Monitor pair instead: First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB21-CP05`).

**Microsoft Learn sources:**

- [Network Watcher Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

**Source reviewed:** 2026-08-31
