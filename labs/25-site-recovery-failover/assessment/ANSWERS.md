# Lab 25 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB25-Q01`)

The lab establishes this design principle: Test failover validates recovery without committing production direction, while planned/unplanned failover, commit, reprotect, and failback are separate state transitions with cost and data-loss implications.

Objectives: MR-RECOVERY-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-powershell>

## 2. B (`LAB25-Q02`)

The reviewed hands-on action for this objective is: Create a source VM and Recovery Services vault, then configure Azure-to-Azure fabric, container, policy, and network mappings.

Objectives: MR-RECOVERY-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill>

## 3. C (`LAB25-Q03`)

Least privilege requires the documented boundary: Site Recovery Contributor, Virtual Machine Contributor, and Network Contributor on both region scopes

Objectives: MR-RECOVERY-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-failover-failback>

## 4. D (`LAB25-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: MR-RECOVERY-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-manage-registration-and-protection>

## 5. A (`LAB25-Q05`)

The lab's reviewed command path performs this bounded action: Create non-overlapping source and recovery VNets in the configured primary and secondary regions.

Objectives: MR-RECOVERY-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-powershell>

## 6. B (`LAB25-Q06`)

The independent validation path must prove Microsoft.Network/virtualNetworks for the exact recorded object.

Objectives: MR-RECOVERY-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill>

## 7. C (`LAB25-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: This elevated lab requires two approved regions and explicit cost review before live execution; test failover must use an isolated network.

Objectives: MR-RECOVERY-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-failover-failback>

## 8. D (`LAB25-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: MR-RECOVERY-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-manage-registration-and-protection>

## 9. A (`LAB25-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: MR-RECOVERY-05, MR-RECOVERY-06

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-powershell>

## 10. B (`LAB25-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: MR-RECOVERY-06, MR-RECOVERY-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill>
