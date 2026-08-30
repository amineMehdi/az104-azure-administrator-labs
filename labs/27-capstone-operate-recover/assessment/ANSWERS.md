# Lab 27 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB27-Q01`)

The lab's central distinction is: Operations should follow evidence: establish baseline, detect and scope the fault, repair the smallest cause, validate service state, then prove backup or recovery objectives before cleanup.

Objectives: IG-ACCESS-03

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview

## 2. B (`LAB27-Q02`)

The first implementation checkpoint is: Inventory the workload, interpret direct/inherited access, policy compliance, tags, locks, and current health before changing anything.

Objectives: IG-GOVERN-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview

## 3. C (`LAB27-Q03`)

The documented permission boundary is Contributor, Monitoring Contributor, Backup Contributor, and Network Contributor on the capstone resource group

Objectives: IG-GOVERN-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview

## 4. D (`LAB27-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: IG-GOVERN-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction

## 5. A (`LAB27-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: IG-GOVERN-06

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access

## 6. B (`LAB27-Q06`)

The live-only gate is explicit and must not be guessed: The live recovery drill requires cost review and an isolated workload; production failover or irreversible deletion is never inferred from this capstone.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview

## 7. C (`LAB27-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: NW-SECURE-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview

## 8. D (`LAB27-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: NW-DNSLB-03, MR-MONITOR-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview

## 9. A (`LAB27-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: MR-MONITOR-03, MR-MONITOR-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction

## 10. B (`LAB27-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: MR-MONITOR-04, MR-MONITOR-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access
