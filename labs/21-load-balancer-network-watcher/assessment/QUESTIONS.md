# Lab 21 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB21-Q01 — Foundational

A network operations administrator publishing a resilient HTTP backend is updating the backend readiness runbook. The requirement is to expose one ingress IP for incoming balanced traffic. Which statement describes Azure behavior correctly?

- A. A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows.
- B. Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules.
- C. When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows.
- D. A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules.

## LAB21-Q02 — Foundational

A backend readiness peer review asks how the resilient HTTP backend publication should handle this outcome: register every serving network interface as an eligible target. Which explanation is accurate?

- A. A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows.
- B. A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows.
- C. A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress.
- D. Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information.

## LAB21-Q03 — Foundational

For the resilient HTTP backend publication, the backend readiness plan must remove an instance from rotation when its application endpoint is unhealthy. Which statement about backend readiness belongs in the resilient HTTP backend publication record?

- A. A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.
- B. Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence.
- C. A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows.
- D. Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.

## LAB21-Q04 — Foundational

The backend readiness review compares four claims for the resilient HTTP backend publication requirement to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule. Which claim is technically sound?

- A. Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules.
- B. When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows.
- C. A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules.
- D. A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.

## LAB21-Q05 — Foundational

The backend readiness architecture note requires the resilient HTTP backend publication environment to allow the platform probe source while keeping other unsolicited traffic denied. Which statement defines the relevant backend readiness boundary?

- A. Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules.
- B. A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress.
- C. Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information.
- D. A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows.

## LAB21-Q06 — Foundational

A new backend readiness operator must explain why the resilient HTTP backend publication can provide explicit outbound connectivity for a Standard load-balanced backend. Which explanation is accurate?

- A. A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress.
- B. Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence.
- C. Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.
- D. A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows.

## LAB21-Q07 — Foundational

The resilient HTTP backend publication acceptance criteria require operators to keep successive flows from one client on the affinity mode the application expects. Which service fact supports that requirement?

- A. When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows.
- B. A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules.
- C. Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence.
- D. A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.

## LAB21-Q08 — Foundational

A backend readiness reviewer challenges whether the resilient HTTP backend publication can explain why no new client flow is sent when every target fails its probe. Which response resolves the concern?

- A. Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information.
- B. A backend pool identifies the NIC configurations or IP addresses eligible to receive balanced flows.
- C. When every backend probe is unhealthy, the load balancer cannot select a healthy target for new client flows.
- D. Standard Load Balancer health probes use the AzureLoadBalancer service tag and must reach the probed backend port through effective NSG rules.

## LAB21-Q09 — Foundational

The resilient HTTP backend publication handoff omits the backend readiness rule needed to test reachability between two endpoints and return the responsible hop or policy. Which statement should the team add?

- A. Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.
- B. A health probe tests a configured protocol, port, and optional path so unhealthy backends stop receiving new flows.
- C. Connection troubleshoot performs an on-demand path test and reports reachability, latency, and diagnosed failure information.
- D. A Standard Load Balancer needs an explicit outbound design, such as outbound rules or NAT Gateway, for predictable backend egress.

## LAB21-Q10 — Foundational

A backend readiness incident review of the resilient HTTP backend publication depends on the ability to measure connection reachability and latency continuously over time. Which platform description is reliable?

- A. A load-balancer frontend IP configuration is the client-facing address used by load-balancing and inbound NAT rules.
- B. Connection Monitor continuously tests configured source and destination endpoints and records reachability and latency over time.
- C. A load-balancing rule binds a frontend, backend pool, probe, protocol, and port mapping into one traffic path.
- D. Load distribution mode can hash two or three tuple fields to provide none, client IP, or client IP and protocol session persistence.

## LAB21-Q11 — Foundational

A backend readiness ticket in the resilient HTTP backend publication says to expose one ingress IP for incoming balanced traffic. Which backend readiness action completes the resilient HTTP backend publication request with minimal change?

- A. Configure a probe that reflects actual application readiness rather than only host availability.
- B. Configure the approved outbound method and size SNAT capacity for expected concurrency.
- C. Run the diagnostic from the actual source resource to the exact destination and port.
- D. Create a public or internal frontend that matches the approved reachability requirement.

## LAB21-Q12 — Foundational

The approach for the resilient HTTP backend publication is approved, but the backend readiness environment still cannot register every serving network interface as an eligible target. Which implementation step closes the gap?

- A. Create the rule with resource IDs from the intended frontend, backend pool, and health probe.
- B. Choose the distribution mode only when the application requires client affinity.
- C. Create a test group with representative endpoints, protocol, port, frequency, and success thresholds.
- D. Add every intended healthy backend and exclude maintenance instances before production traffic.

## LAB21-Q13 — Foundational

The network operations administrator publishing a resilient HTTP backend may change the resilient HTTP backend publication only to remove an instance from rotation when its application endpoint is unhealthy. Which backend readiness action stays within that assignment?

- A. Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application.
- B. Configure a probe that reflects actual application readiness rather than only host availability.
- C. Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend.
- D. Create a public or internal frontend that matches the approved reachability requirement.

## LAB21-Q14 — Foundational

A backend readiness dry run shows no resilient HTTP backend publication command will connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule. Which action belongs before execution?

- A. Create the rule with resource IDs from the intended frontend, backend pool, and health probe.
- B. Configure the approved outbound method and size SNAT capacity for expected concurrency.
- C. Run the diagnostic from the actual source resource to the exact destination and port.
- D. Add every intended healthy backend and exclude maintenance instances before production traffic.

## LAB21-Q15 — Foundational

For the resilient HTTP backend publication, operators need to allow the platform probe source while keeping other unsolicited traffic denied. Which change realizes that requirement?

- A. Choose the distribution mode only when the application requires client affinity.
- B. Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application.
- C. Create a test group with representative endpoints, protocol, port, frequency, and success thresholds.
- D. Configure a probe that reflects actual application readiness rather than only host availability.

## LAB21-Q16 — Applied

Operators must automate the resilient HTTP backend publication change needed to provide explicit outbound connectivity for a Standard load-balanced backend. Which backend readiness operation belongs in the runbook?

- A. Configure the approved outbound method and size SNAT capacity for expected concurrency.
- B. Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend.
- C. Create a public or internal frontend that matches the approved reachability requirement.
- D. Create the rule with resource IDs from the intended frontend, backend pool, and health probe.

## LAB21-Q17 — Applied

A resilient HTTP backend publication review finds backend readiness drift from the need to keep successive flows from one client on the affinity mode the application expects. Which correction addresses that drift?

- A. Run the diagnostic from the actual source resource to the exact destination and port.
- B. Add every intended healthy backend and exclude maintenance instances before production traffic.
- C. Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application.
- D. Choose the distribution mode only when the application requires client affinity.

## LAB21-Q18 — Applied

The resilient HTTP backend publication window permits only the backend readiness change needed to explain why no new client flow is sent when every target fails its probe. Which option respects the boundary?

- A. Create a test group with representative endpoints, protocol, port, frequency, and success thresholds.
- B. Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend.
- C. Configure a probe that reflects actual application readiness rather than only host availability.
- D. Configure the approved outbound method and size SNAT capacity for expected concurrency.

## LAB21-Q19 — Applied

The backend readiness preflight has passed; the resilient HTTP backend publication must now test reachability between two endpoints and return the responsible hop or policy. Which operation should run?

- A. Create a public or internal frontend that matches the approved reachability requirement.
- B. Run the diagnostic from the actual source resource to the exact destination and port.
- C. Create the rule with resource IDs from the intended frontend, backend pool, and health probe.
- D. Choose the distribution mode only when the application requires client affinity.

## LAB21-Q20 — Applied

The resilient HTTP backend publication plan must measure connection reachability and latency continuously over time while limiting the mutation scope to backend readiness. Which action is appropriate?

- A. Create a test group with representative endpoints, protocol, port, frequency, and success thresholds.
- B. Add every intended healthy backend and exclude maintenance instances before production traffic.
- C. Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application.
- D. Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend.

## LAB21-Q21 — Applied

The resilient HTTP backend publication setup reports success after the backend readiness attempt to expose one ingress IP for incoming balanced traffic. Which backend readiness read-only observation proves the resilient HTTP backend publication outcome?

- A. Query the rule and verify every referenced component and port value.
- B. Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
- C. Query loadDistribution on the rule and test repeated flows from controlled clients.
- D. Query monitor state, test configurations, test groups, and recent reachability results.

## LAB21-Q22 — Applied

The backend readiness log says the resilient HTTP backend publication can now register every serving network interface as an eligible target. Which backend readiness state should the resilient HTTP backend publication acceptance test retain?

- A. Inspect effective NSG rules and probe health for the exact backend NIC and port.
- B. Correlate per-instance health with listener tests and effective security rules.
- C. Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
- D. Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.

## LAB21-Q23 — Applied

The resilient HTTP backend publication rejects backend readiness exit status as proof it can remove an instance from rotation when its application endpoint is unhealthy. Which resilient HTTP backend publication result is valid evidence?

- A. Query outbound rules or NAT Gateway association and test backend egress independently.
- B. Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
- C. Query probe protocol, port, path, interval, threshold, and backend health status.
- D. Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.

## LAB21-Q24 — Applied

The backend readiness validator needs one resilient HTTP backend publication query after the change to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule. Which backend readiness property should the resilient HTTP backend publication validator inspect?

- A. Query loadDistribution on the rule and test repeated flows from controlled clients.
- B. Query monitor state, test configurations, test groups, and recent reachability results.
- C. Query probe protocol, port, path, interval, threshold, and backend health status.
- D. Query the rule and verify every referenced component and port value.

## LAB21-Q25 — Applied

The network operations administrator publishing a resilient HTTP backend must confirm the resilient HTTP backend publication, without mutation, can allow the platform probe source while keeping other unsolicited traffic denied. Which backend readiness check qualifies?

- A. Inspect effective NSG rules and probe health for the exact backend NIC and port.
- B. Correlate per-instance health with listener tests and effective security rules.
- C. Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
- D. Query the rule and verify every referenced component and port value.

## LAB21-Q26 — Applied

The resilient HTTP backend publication configuration is complete; the backend readiness reviewers need evidence it can provide explicit outbound connectivity for a Standard load-balanced backend. Which observation shows success?

- A. Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
- B. Query outbound rules or NAT Gateway association and test backend egress independently.
- C. Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
- D. Inspect effective NSG rules and probe health for the exact backend NIC and port.

## LAB21-Q27 — Applied

The backend readiness validation asks whether the resilient HTTP backend publication can keep successive flows from one client on the affinity mode the application expects. Which observable state is strongest?

- A. Query monitor state, test configurations, test groups, and recent reachability results.
- B. Query probe protocol, port, path, interval, threshold, and backend health status.
- C. Query outbound rules or NAT Gateway association and test backend egress independently.
- D. Query loadDistribution on the rule and test repeated flows from controlled clients.

## LAB21-Q28 — Applied

A resilient HTTP backend publication review must prove the backend readiness ability to explain why no new client flow is sent when every target fails its probe. Which check avoids an adjacent feature?

- A. Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
- B. Query the rule and verify every referenced component and port value.
- C. Query loadDistribution on the rule and test repeated flows from controlled clients.
- D. Correlate per-instance health with listener tests and effective security rules.

## LAB21-Q29 — Applied

The resilient HTTP backend publication evidence bundle needs a backend readiness result showing it can test reachability between two endpoints and return the responsible hop or policy. Which result belongs in the checkpoint?

- A. Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
- B. Inspect effective NSG rules and probe health for the exact backend NIC and port.
- C. Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
- D. Correlate per-instance health with listener tests and effective security rules.

## LAB21-Q30 — Applied

Before resilient HTTP backend publication cleanup, the backend readiness team must reconfirm it can measure connection reachability and latency continuously over time. Which read-only inspection should run?

- A. Query probe protocol, port, path, interval, threshold, and backend health status.
- B. Query outbound rules or NAT Gateway association and test backend egress independently.
- C. Query monitor state, test configurations, test groups, and recent reachability results.
- D. Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.

## LAB21-Q31 — Applied

During a backend readiness fault drill, the resilient HTTP backend publication does not expose one ingress IP for incoming balanced traffic. Which finding identifies the defect?

- A. An internal-only service was assigned a public frontend IP.
- B. The new VM exists but its NIC is not a member of the load balancer backend pool.
- C. Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design.
- D. The monitor has no enabled source endpoint in its test group.

## LAB21-Q32 — Applied

The resilient HTTP backend publication setup finishes, yet the backend readiness cannot register every serving network interface as an eligible target. Which misconfiguration explains the mismatch?

- A. The HTTP probe path returns a failure status even though the application root path works.
- B. The application expects client affinity while the rule uses the default five-tuple distribution.
- C. The new VM exists but its NIC is not a member of the load balancer backend pool.
- D. An internal-only service was assigned a public frontend IP.

## LAB21-Q33 — Applied

A backend readiness break/fix in the resilient HTTP backend publication fails when operators try to remove an instance from rotation when its application endpoint is unhealthy. Which diagnosis fits?

- A. The rule references a probe for a different backend application port.
- B. The HTTP probe path returns a failure status even though the application root path works.
- C. The backend service listens on a different port from the configured probe.
- D. The new VM exists but its NIC is not a member of the load balancer backend pool.

## LAB21-Q34 — Applied

The resilient HTTP backend publication troubleshooting scope is the backend readiness need to connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule. Which condition should be corrected first?

- A. A higher-priority NSG deny blocks the AzureLoadBalancer probe source.
- B. The diagnostic targeted the destination's management port instead of the failing application port.
- C. The HTTP probe path returns a failure status even though the application root path works.
- D. The rule references a probe for a different backend application port.

## LAB21-Q35 — Applied

The resilient HTTP backend publication result is partial because the backend readiness cannot allow the platform probe source while keeping other unsolicited traffic denied. Which condition accounts for that result?

- A. A higher-priority NSG deny blocks the AzureLoadBalancer probe source.
- B. Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design.
- C. The monitor has no enabled source endpoint in its test group.
- D. The rule references a probe for a different backend application port.

## LAB21-Q36 — Applied

The backend readiness evidence shows the resilient HTTP backend publication cannot provide explicit outbound connectivity for a Standard load-balanced backend. Which root cause fits that evidence?

- A. The application expects client affinity while the rule uses the default five-tuple distribution.
- B. An internal-only service was assigned a public frontend IP.
- C. Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design.
- D. A higher-priority NSG deny blocks the AzureLoadBalancer probe source.

## LAB21-Q37 — Applied

Although the resilient HTTP backend publication is meant to let the backend readiness keep successive flows from one client on the affinity mode the application expects, its checkpoint fails. Which backend readiness defect explains the failure?

- A. The backend service listens on a different port from the configured probe.
- B. The new VM exists but its NIC is not a member of the load balancer backend pool.
- C. The application expects client affinity while the rule uses the default five-tuple distribution.
- D. Backends rely on implicit outbound access that is unavailable for the chosen Standard load-balancer design.

## LAB21-Q38 — Applied

The backend readiness support team isolated the resilient HTTP backend publication incident to the attempt to explain why no new client flow is sent when every target fails its probe. Which condition prevents success?

- A. The diagnostic targeted the destination's management port instead of the failing application port.
- B. The backend service listens on a different port from the configured probe.
- C. The HTTP probe path returns a failure status even though the application root path works.
- D. The application expects client affinity while the rule uses the default five-tuple distribution.

## LAB21-Q39 — Applied

A resilient HTTP backend publication query surprises the network operations administrator publishing a resilient HTTP backend during the backend readiness attempt to test reachability between two endpoints and return the responsible hop or policy. Which finding explains it?

- A. The diagnostic targeted the destination's management port instead of the failing application port.
- B. The monitor has no enabled source endpoint in its test group.
- C. The rule references a probe for a different backend application port.
- D. The backend service listens on a different port from the configured probe.

## LAB21-Q40 — Applied

Other resilient HTTP backend publication components are healthy, but the backend readiness still cannot measure connection reachability and latency continuously over time. Which state causes the isolated failure?

- A. An internal-only service was assigned a public frontend IP.
- B. The monitor has no enabled source endpoint in its test group.
- C. A higher-priority NSG deny blocks the AzureLoadBalancer probe source.
- D. The diagnostic targeted the destination's management port instead of the failing application port.

## LAB21-Q41 — Advanced

The resilient HTTP backend publication runbook must expose one ingress IP for incoming balanced traffic, then retain backend readiness read-back evidence. Which resilient HTTP backend publication pair completes both duties?

- A. First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
- B. First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
- C. First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.
- D. First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.

## LAB21-Q42 — Advanced

To satisfy the backend readiness requirement, operators must change the resilient HTTP backend publication configuration and prove it can register every serving network interface as an eligible target. Which sequence is coherent?

- A. First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.
- B. First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.
- C. First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
- D. First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.

## LAB21-Q43 — Advanced

The network operations administrator publishing a resilient HTTP backend needs a safe resilient HTTP backend publication change to remove an instance from rotation when its application endpoint is unhealthy, followed by backend readiness evidence. Which pair merits approval?

- A. First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
- B. First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.
- C. First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
- D. First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.

## LAB21-Q44 — Advanced

The resilient HTTP backend publication has two backend readiness gates: connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule, then prove the resilient HTTP backend publication state. Which backend readiness sequence works?

- A. First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.
- B. First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently.
- C. First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.
- D. First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.

## LAB21-Q45 — Advanced

Which backend readiness path makes the resilient HTTP backend publication able to allow the platform probe source while keeping other unsolicited traffic denied, then inspects the defining properties?

- A. First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.
- B. First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
- C. First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.
- D. First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.

## LAB21-Q46 — Advanced

At the resilient HTTP backend publication approval gate, operators must show that the backend readiness can provide explicit outbound connectivity for a Standard load-balanced backend. Which backend readiness configure-and-check pair is defensible?

- A. First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.
- B. First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
- C. First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
- D. First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently.

## LAB21-Q47 — Advanced

The resilient HTTP backend publication forbids a partial backend readiness result. Operators must first keep successive flows from one client on the affinity mode the application expects and afterward confirm the resilient HTTP backend publication outcome. Which backend readiness sequence is complete?

- A. First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.
- B. First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.
- C. First, Configure a probe that reflects actual application readiness rather than only host availability. Then, Query probe protocol, port, path, interval, threshold, and backend health status.
- D. First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.

## LAB21-Q48 — Advanced

Only the resilient HTTP backend publication change needed to explain why no new client flow is sent when every target fails its probe is allowed, and backend readiness proof is mandatory. Which pair fits?

- A. First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.
- B. First, Create the rule with resource IDs from the intended frontend, backend pool, and health probe. Then, Query the rule and verify every referenced component and port value.
- C. First, Investigate application listener, probe configuration, guest firewall, and NSG path before changing the frontend. Then, Correlate per-instance health with listener tests and effective security rules.
- D. First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.

## LAB21-Q49 — Advanced

The resilient HTTP backend publication runbook separates backend readiness mutation from validation while it must test reachability between two endpoints and return the responsible hop or policy. Which sequence proves it cleanly?

- A. First, Create a public or internal frontend that matches the approved reachability requirement. Then, Query frontendIPConfigurations and confirm public IP or subnet, private allocation, and zone settings.
- B. First, Allow the AzureLoadBalancer service tag to the probe port without broadly exposing the application. Then, Inspect effective NSG rules and probe health for the exact backend NIC and port.
- C. First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently.
- D. First, Run the diagnostic from the actual source resource to the exact destination and port. Then, Capture connectionStatus, probesSent, probesFailed, averageLatencyInMs, and diagnostic messages.

## LAB21-Q50 — Advanced

The resilient HTTP backend publication checkpoint requires both this backend readiness outcome—measure connection reachability and latency continuously over time—and a read-only resilient HTTP backend publication state check. Which backend readiness response is complete?

- A. First, Add every intended healthy backend and exclude maintenance instances before production traffic. Then, Query backendAddressPools and resolve each backend membership to the expected VM NIC or IP.
- B. First, Configure the approved outbound method and size SNAT capacity for expected concurrency. Then, Query outbound rules or NAT Gateway association and test backend egress independently.
- C. First, Create a test group with representative endpoints, protocol, port, frequency, and success thresholds. Then, Query monitor state, test configurations, test groups, and recent reachability results.
- D. First, Choose the distribution mode only when the application requires client affinity. Then, Query loadDistribution on the rule and test repeated flows from controlled clients.

[Open the answer key](./ANSWERS.md)
