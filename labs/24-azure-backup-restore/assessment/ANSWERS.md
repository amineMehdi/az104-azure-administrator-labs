# Lab 24 answer key

Return to [the questions](QUESTIONS.md).

## 1. B (`LAB24-Q01`)

The lab establishes this design principle: Vault type must match the workload, protection creates retained recovery points, and vault deletion requires ordered removal of protected items, soft-delete state, and dependencies.

Objectives: MR-RECOVERY-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault>

## 2. C (`LAB24-Q02`)

The reviewed hands-on action for this objective is: Create a bounded-retention VM backup policy and enable protection for the test VM.

Objectives: MR-RECOVERY-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault>

## 3. D (`LAB24-Q03`)

Least privilege requires the documented boundary: Backup Contributor and Virtual Machine Contributor on the lab resource group

Objectives: MR-RECOVERY-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-powershell>

## 4. A (`LAB24-Q04`)

The lab records the exact scope and identity of backup policy before validation and cleanup.

Objectives: MR-RECOVERY-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm>

## 5. B (`LAB24-Q05`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: MR-RECOVERY-07

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/configure-reports>

## 6. C (`LAB24-Q06`)

The lab's reviewed command path performs this bounded action: Create a bounded-retention VM backup policy and enable protection for the test VM.

Objectives: MR-RECOVERY-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor>

## 7. D (`LAB24-Q07`)

The independent validation path must prove Microsoft.RecoveryServices/vaults for the exact recorded object.

Objectives: MR-RECOVERY-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault>

## 8. A (`LAB24-Q08`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: MR-RECOVERY-03

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault>

## 9. B (`LAB24-Q09`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: MR-RECOVERY-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-powershell>

## 10. C (`LAB24-Q10`)

A bounded negative assertion detects accidental privilege or exposure beyond the intended state.

Objectives: MR-RECOVERY-07

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm>

## 11. D (`LAB24-Q11`)

Immutable recorded IDs create a deterministic validation and cleanup boundary.

Objectives: MR-RECOVERY-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/configure-reports>

## 12. A (`LAB24-Q12`)

Cleanup must use the exact recorded boundary and a separate execution confirmation.

Objectives: MR-RECOVERY-02

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor>

## 13. B (`LAB24-Q13`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: MR-RECOVERY-03, MR-RECOVERY-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault>

## 14. C (`LAB24-Q14`)

Accepted requests and offline checks do not prove the final live state.

Objectives: MR-RECOVERY-04, MR-RECOVERY-07

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault>

## 15. D (`LAB24-Q15`)

The narrowest evidence-supported correction avoids unrelated changes and excess privilege.

Objectives: MR-RECOVERY-07, MR-RECOVERY-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-powershell>
