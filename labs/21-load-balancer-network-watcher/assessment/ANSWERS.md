# Lab 21 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB21-Q01`)

The lab establishes this design principle: A load-balancing rule depends on a healthy probe and reachable backend, while Network Watcher distinguishes DNS, routing, NSG, guest firewall, and application-listener failures.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-powershell>

## 2. B (`LAB21-Q02`)

The reviewed hands-on action for this objective is: Create a Standard public load balancer, backend pool, TCP probe, and frontend rule.

Objectives: NW-DNSLB-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status>

## 3. C (`LAB21-Q03`)

Least privilege requires the documented boundary: Network Contributor and Virtual Machine Contributor on the lab resource group

Objectives: NW-DNSLB-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview>

## 4. D (`LAB21-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview>

## 5. A (`LAB21-Q05`)

The lab's reviewed command path performs this bounded action: Create two backend NICs/VMs in an NSG-protected subnet without individual public IPs.

Objectives: NW-DNSLB-02

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-powershell>

## 6. B (`LAB21-Q06`)

The independent validation path must prove Microsoft.Network/networkWatchers for the exact recorded object.

Objectives: NW-DNSLB-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status>

## 7. C (`LAB21-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview>

## 8. D (`LAB21-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: NW-DNSLB-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview>

## 9. A (`LAB21-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: NW-DNSLB-03, NW-VNET-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-powershell>

## 10. B (`LAB21-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: NW-VNET-05, NW-DNSLB-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status>
