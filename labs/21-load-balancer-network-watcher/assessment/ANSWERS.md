# Lab 21 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB21-Q01`)

The lab's central distinction is: A load-balancing rule depends on a healthy probe and reachable backend, while Network Watcher distinguishes DNS, routing, NSG, guest firewall, and application-listener failures.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-powershell>

## 2. B (`LAB21-Q02`)

The first implementation checkpoint is: Create two backend NICs/VMs in an NSG-protected subnet without individual public IPs.

Objectives: NW-DNSLB-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status>

## 3. C (`LAB21-Q03`)

The documented permission boundary is Network Contributor and Virtual Machine Contributor on the lab resource group

Objectives: NW-DNSLB-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview>

## 4. D (`LAB21-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: MR-MONITOR-06

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview>

## 5. A (`LAB21-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-powershell>

## 6. B (`LAB21-Q06`)

The live-only gate is explicit and must not be guessed: None beyond the declared role and a disposable subscription.

Objectives: NW-DNSLB-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status>

## 7. C (`LAB21-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: NW-DNSLB-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview>

## 8. D (`LAB21-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: MR-MONITOR-06, NW-VNET-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview>

## 9. A (`LAB21-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: NW-VNET-05, NW-DNSLB-02

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-powershell>

## 10. B (`LAB21-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: NW-DNSLB-02, NW-DNSLB-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status>
