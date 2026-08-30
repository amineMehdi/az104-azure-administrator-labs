# Lab 25 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB25-Q01`)

The lab's central distinction is: Test failover validates recovery without committing production direction, while planned/unplanned failover, commit, reprotect, and failback are separate state transitions with cost and data-loss implications.

Objectives: MR-RECOVERY-05

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-powershell

## 2. B (`LAB25-Q02`)

The first implementation checkpoint is: Create non-overlapping source and recovery VNets in the configured primary and secondary regions.

Objectives: MR-RECOVERY-06

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill

## 3. C (`LAB25-Q03`)

The documented permission boundary is Site Recovery Contributor, Virtual Machine Contributor, and Network Contributor on both region scopes

Objectives: MR-RECOVERY-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-failover-failback

## 4. D (`LAB25-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: MR-RECOVERY-06

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-manage-registration-and-protection

## 5. A (`LAB25-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: MR-RECOVERY-05

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-powershell

## 6. B (`LAB25-Q06`)

The live-only gate is explicit and must not be guessed: This elevated lab requires two approved regions and explicit cost review before live execution; test failover must use an isolated network.

Objectives: MR-RECOVERY-06

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill

## 7. C (`LAB25-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: MR-RECOVERY-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-failover-failback

## 8. D (`LAB25-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: MR-RECOVERY-06, MR-RECOVERY-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-manage-registration-and-protection

## 9. A (`LAB25-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: MR-RECOVERY-05, MR-RECOVERY-06

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-powershell

## 10. B (`LAB25-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: MR-RECOVERY-06, MR-RECOVERY-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill
