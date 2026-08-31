# Lab 24 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB24-Q01 — C

**Question:** A restore rehearsal incident review of the test-VM protection and restore drill depends on the ability to store supported Azure VM protection metadata in the correct vault type. Which platform description is reliable?

- **A — Incorrect.** A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.
  A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types. In the test-VM protection and restore drill, this statement describes Backup vaults. Test-VM protection and restore drill asks about Recovery Services vaults; this Backup vaults choice leaves the Recovery Services vaults explanation missing.
- **B — Incorrect.** An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date.
  An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date. In the test-VM protection and restore drill, this statement describes on-demand backups. The on-demand backups statement accurately describes on-demand backups; however, test-VM protection and restore drill needs Recovery Services vaults to store supported Azure VM protection metadata in the correct vault type; on-demand backups cannot replace Recovery Services vaults.
- **C — Correct.** A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery.
  A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery. The test-VM protection and restore drill applies that Recovery Services vaults boundary when operators must store supported Azure VM protection metadata in the correct vault type.
- **D — Incorrect.** Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.
  Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements. In the test-VM protection and restore drill, this statement describes VM restore choices. Recovery Services vaults governs test-VM protection and restore drill; VM restore choices cannot support Recovery Services vaults when operators must store supported Azure VM protection metadata in the correct vault type.

**Objectives:** `MR-RECOVERY-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Create a Recovery Services vault](https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q02 — D

**Question:** A recovery administrator protecting and restoring a test VM is updating the restore rehearsal runbook. The requirement is to use the vault type designed for newer data-source protection workloads. Which statement describes Azure behavior correctly?

- **A — Incorrect.** A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained.
  A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained. In the test-VM protection and restore drill, this statement describes backup frequency and retention. The backup frequency and retention statement accurately describes backup frequency and retention; however, test-VM protection and restore drill needs Backup vaults to use the vault type designed for newer data-source protection workloads; backup frequency and retention cannot replace Backup vaults.
- **B — Incorrect.** A restore operation must select a successful recovery point compatible with the desired restore type.
  A restore operation must select a successful recovery point compatible with the desired restore type. In the test-VM protection and restore drill, this statement describes recovery-point selection. Selecting recovery-point selection for test-VM protection and restore drill leaves Backup vaults unanswered in test-VM protection and restore drill; the test-VM protection and restore drill lacks a Backup vaults basis to use the vault type designed for newer data-source protection workloads.
- **C — Incorrect.** Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion.
  Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion. In the test-VM protection and restore drill, this statement describes backup soft delete. Backup vaults governs test-VM protection and restore drill; backup soft delete cannot support Backup vaults when operators must use the vault type designed for newer data-source protection workloads.
- **D — Correct.** A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.
  The test-VM protection and restore drill needs Backup vaults to use the vault type designed for newer data-source protection workloads; this option states the applicable Backup vaults rule: a Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.

**Objectives:** `MR-RECOVERY-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Create and manage an Azure Backup vault](https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q03 — A

**Question:** A restore rehearsal peer review asks how the test-VM protection and restore drill should handle this outcome: define how often recovery points are created and how long they remain. Which explanation is accurate?

- **A — Correct.** A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained.
  A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained. This backup frequency and retention fact resolves the test-VM protection and restore drill design question about how to define how often recovery points are created and how long they remain.
- **B — Incorrect.** A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource.
  A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource. In the test-VM protection and restore drill, this statement describes policy association. Backup frequency and retention governs test-VM protection and restore drill; policy association cannot support backup frequency and retention when operators must define how often recovery points are created and how long they remain.
- **C — Incorrect.** Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM.
  Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM. In the test-VM protection and restore drill, this statement describes file-level recovery. Test-VM protection and restore drill asks about backup frequency and retention; this file-level recovery choice leaves the backup frequency and retention explanation missing.
- **D — Incorrect.** Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures.
  Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures. In the test-VM protection and restore drill, this statement describes backup monitoring and alerts. The backup monitoring and alerts statement accurately describes backup monitoring and alerts; however, test-VM protection and restore drill needs backup frequency and retention to define how often recovery points are created and how long they remain; backup monitoring and alerts cannot replace backup frequency and retention.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Azure Backup policy fundamentals](https://learn.microsoft.com/en-us/azure/backup/backup-architecture)

**Source reviewed:** 2026-08-31

## LAB24-Q04 — B

**Question:** For the test-VM protection and restore drill, the restore rehearsal plan must associate the intended protection schedule with the test workload. Which statement about restore rehearsal belongs in the test-VM protection and restore drill record?

- **A — Incorrect.** An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date.
  An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date. In the test-VM protection and restore drill, this statement describes on-demand backups. Policy association governs test-VM protection and restore drill; on-demand backups cannot support policy association when operators must associate the intended protection schedule with the test workload.
- **B — Correct.** A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource.
  A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource. For test-VM protection and restore drill, policy association supplies the service rule needed to associate the intended protection schedule with the test workload.
- **C — Incorrect.** Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.
  Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements. In the test-VM protection and restore drill, this statement describes VM restore choices. The VM restore choices statement accurately describes VM restore choices; however, test-VM protection and restore drill needs policy association to associate the intended protection schedule with the test workload; VM restore choices cannot replace policy association.
- **D — Incorrect.** A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery.
  A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery. In the test-VM protection and restore drill, this statement describes Recovery Services vaults. Selecting Recovery Services vaults for test-VM protection and restore drill leaves policy association unanswered in test-VM protection and restore drill; the test-VM protection and restore drill lacks a policy association basis to associate the intended protection schedule with the test workload.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q05 — D

**Question:** The restore rehearsal review compares four claims for the test-VM protection and restore drill requirement to create an extra recovery point before a risky maintenance window. Which claim is technically sound?

- **A — Incorrect.** A restore operation must select a successful recovery point compatible with the desired restore type.
  A restore operation must select a successful recovery point compatible with the desired restore type. In the test-VM protection and restore drill, this statement describes recovery-point selection. Test-VM protection and restore drill asks about on-demand backups; this recovery-point selection choice leaves the on-demand backups explanation missing.
- **B — Incorrect.** Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion.
  Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion. In the test-VM protection and restore drill, this statement describes backup soft delete. The backup soft delete statement accurately describes backup soft delete; however, test-VM protection and restore drill needs on-demand backups to create an extra recovery point before a risky maintenance window; backup soft delete cannot replace on-demand backups.
- **C — Incorrect.** A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.
  A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types. In the test-VM protection and restore drill, this statement describes Backup vaults. Selecting Backup vaults for test-VM protection and restore drill leaves on-demand backups unanswered in test-VM protection and restore drill; the test-VM protection and restore drill lacks a on-demand backups basis to create an extra recovery point before a risky maintenance window.
- **D — Correct.** An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date.
  An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date. In the test-VM protection and restore drill, this on-demand backups rule supports the need to create an extra recovery point before a risky maintenance window.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q06 — C

**Question:** The restore rehearsal architecture note requires the test-VM protection and restore drill environment to select a recovery point that meets the required recovery time. Which statement defines the relevant restore rehearsal boundary?

- **A — Incorrect.** Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM.
  Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM. In the test-VM protection and restore drill, this statement describes file-level recovery. The file-level recovery statement accurately describes file-level recovery; however, test-VM protection and restore drill needs recovery-point selection to select a recovery point that meets the required recovery time; file-level recovery cannot replace recovery-point selection.
- **B — Incorrect.** Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures.
  Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures. In the test-VM protection and restore drill, this statement describes backup monitoring and alerts. Selecting backup monitoring and alerts for test-VM protection and restore drill leaves recovery-point selection unanswered in test-VM protection and restore drill; the test-VM protection and restore drill lacks a recovery-point selection basis to select a recovery point that meets the required recovery time.
- **C — Correct.** A restore operation must select a successful recovery point compatible with the desired restore type.
  For the test-VM protection and restore drill, the rule for recovery-point selection is defined by this statement: a restore operation must select a successful recovery point compatible with the desired restore type. It supports the required outcome to select a recovery point that meets the required recovery time.
- **D — Incorrect.** A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained.
  A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained. In the test-VM protection and restore drill, this statement describes backup frequency and retention. Test-VM protection and restore drill asks about recovery-point selection; this backup frequency and retention choice leaves the recovery-point selection explanation missing.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q07 — A

**Question:** A new restore rehearsal operator must explain why the test-VM protection and restore drill can recover selected files without replacing the complete virtual machine. Which explanation is accurate?

- **A — Correct.** Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM.
  Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM. The test-VM protection and restore drill applies that file-level recovery boundary when operators must recover selected files without replacing the complete virtual machine.
- **B — Incorrect.** Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.
  Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements. In the test-VM protection and restore drill, this statement describes VM restore choices. File-level recovery governs test-VM protection and restore drill; VM restore choices cannot support file-level recovery when operators must recover selected files without replacing the complete virtual machine.
- **C — Incorrect.** A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery.
  A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery. In the test-VM protection and restore drill, this statement describes Recovery Services vaults. Test-VM protection and restore drill asks about file-level recovery; this Recovery Services vaults choice leaves the file-level recovery explanation missing.
- **D — Incorrect.** A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource.
  A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource. In the test-VM protection and restore drill, this statement describes policy association. The policy association statement accurately describes policy association; however, test-VM protection and restore drill needs file-level recovery to recover selected files without replacing the complete virtual machine; policy association cannot replace file-level recovery.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Recover files from an Azure virtual machine backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm)

**Source reviewed:** 2026-08-31

## LAB24-Q08 — C

**Question:** The test-VM protection and restore drill acceptance criteria require operators to choose between creating a restored machine and restoring disks for controlled assembly. Which service fact supports that requirement?

- **A — Incorrect.** Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion.
  Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion. In the test-VM protection and restore drill, this statement describes backup soft delete. VM restore choices governs test-VM protection and restore drill; backup soft delete cannot support VM restore choices when operators must choose between creating a restored machine and restoring disks for controlled assembly.
- **B — Incorrect.** A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.
  A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types. In the test-VM protection and restore drill, this statement describes Backup vaults. Test-VM protection and restore drill asks about VM restore choices; this Backup vaults choice leaves the VM restore choices explanation missing.
- **C — Correct.** Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.
  The test-VM protection and restore drill needs VM restore choices to choose between creating a restored machine and restoring disks for controlled assembly; this option states the applicable VM restore choices rule: Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.
- **D — Incorrect.** An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date.
  An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date. In the test-VM protection and restore drill, this statement describes on-demand backups. Selecting on-demand backups for test-VM protection and restore drill leaves VM restore choices unanswered in test-VM protection and restore drill; the test-VM protection and restore drill lacks a VM restore choices basis to choose between creating a restored machine and restoring disks for controlled assembly.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q09 — C

**Question:** A restore rehearsal reviewer challenges whether the test-VM protection and restore drill can hold erased recovery data temporarily so accidental removal can be reversed. Which response resolves the concern?

- **A — Incorrect.** Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures.
  Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures. In the test-VM protection and restore drill, this statement describes backup monitoring and alerts. Test-VM protection and restore drill asks about backup soft delete; this backup monitoring and alerts choice leaves the backup soft delete explanation missing.
- **B — Incorrect.** A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained.
  A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained. In the test-VM protection and restore drill, this statement describes backup frequency and retention. The backup frequency and retention statement accurately describes backup frequency and retention; however, test-VM protection and restore drill needs backup soft delete to hold erased recovery data temporarily so accidental removal can be reversed; backup frequency and retention cannot replace backup soft delete.
- **C — Correct.** Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion.
  Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion. This backup soft delete fact resolves the test-VM protection and restore drill design question about how to hold erased recovery data temporarily so accidental removal can be reversed.
- **D — Incorrect.** A restore operation must select a successful recovery point compatible with the desired restore type.
  A restore operation must select a successful recovery point compatible with the desired restore type. In the test-VM protection and restore drill, this statement describes recovery-point selection. Backup soft delete governs test-VM protection and restore drill; recovery-point selection cannot support backup soft delete when operators must hold erased recovery data temporarily so accidental removal can be reversed.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Soft delete for Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-security-feature-cloud)

**Source reviewed:** 2026-08-31

## LAB24-Q10 — B

**Question:** The test-VM protection and restore drill handoff omits the restore rehearsal rule needed to detect failed protection jobs and route them to operators. Which statement should the team add?

- **A — Incorrect.** A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery.
  A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery. In the test-VM protection and restore drill, this statement describes Recovery Services vaults. The Recovery Services vaults statement accurately describes Recovery Services vaults; however, test-VM protection and restore drill needs backup monitoring and alerts to detect failed protection jobs and route them to operators; Recovery Services vaults cannot replace backup monitoring and alerts.
- **B — Correct.** Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures.
  Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures. For test-VM protection and restore drill, backup monitoring and alerts supplies the service rule needed to detect failed protection jobs and route them to operators.
- **C — Incorrect.** A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource.
  A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource. In the test-VM protection and restore drill, this statement describes policy association. Backup monitoring and alerts governs test-VM protection and restore drill; policy association cannot support backup monitoring and alerts when operators must detect failed protection jobs and route them to operators.
- **D — Incorrect.** Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM.
  Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM. In the test-VM protection and restore drill, this statement describes file-level recovery. Test-VM protection and restore drill asks about backup monitoring and alerts; this file-level recovery choice leaves the backup monitoring and alerts explanation missing.

**Objectives:** `MR-RECOVERY-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Monitor Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor)

**Source reviewed:** 2026-08-31

## LAB24-Q11 — A

**Question:** The test-VM protection and restore drill plan must store supported Azure VM protection metadata in the correct vault type while limiting the mutation scope to restore rehearsal. Which action is appropriate?

- **A — Correct.** Create the vault in the approved region and resource group before protecting the VM.
  Create the vault in the approved region and resource group before protecting the VM. The test-VM protection and restore drill uses this Recovery Services vaults operation to store supported Azure VM protection metadata in the correct vault type within the approved scope.
- **B — Incorrect.** Configure frequency, time zone, and retention ranges from the recovery objectives.
  Configure frequency, time zone, and retention ranges from the recovery objectives. In the test-VM protection and restore drill, this action changes backup frequency and retention. Test-VM protection and restore drill requires Recovery Services vaults; changing backup frequency and retention leaves Recovery Services vaults absent in test-VM protection and restore drill; test-VM protection and restore drill cannot store supported Azure VM protection metadata in the correct vault type.
- **C — Incorrect.** List recovery points and choose one captured before the simulated data loss.
  List recovery points and choose one captured before the simulated data loss. In the test-VM protection and restore drill, this action changes recovery-point selection. Recovery-point selection does not implement Recovery Services vaults for test-VM protection and restore drill; the test-VM protection and restore drill still cannot store supported Azure VM protection metadata in the correct vault type.
- **D — Incorrect.** Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup.
  Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. In the test-VM protection and restore drill, this action changes backup soft delete. Test-VM protection and restore drill instead needs Recovery Services vaults: Create the vault in the approved region and resource group before protecting the VM. The backup soft delete action omits that Recovery Services vaults work.

**Objectives:** `MR-RECOVERY-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Create a Recovery Services vault](https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q12 — D

**Question:** A restore rehearsal ticket in the test-VM protection and restore drill says to use the vault type designed for newer data-source protection workloads. Which restore rehearsal action completes the test-VM protection and restore drill request with minimal change?

- **A — Incorrect.** Enable protection for the exact datasource using the approved policy ID.
  Enable protection for the exact datasource using the approved policy ID. In the test-VM protection and restore drill, this action changes policy association. Test-VM protection and restore drill requires Backup vaults; changing policy association leaves Backup vaults absent in test-VM protection and restore drill; test-VM protection and restore drill cannot use the vault type designed for newer data-source protection workloads.
- **B — Incorrect.** Use file recovery when only a small set of guest files must be recovered.
  Use file recovery when only a small set of guest files must be recovered. In the test-VM protection and restore drill, this action changes file-level recovery. File-level recovery does not implement Backup vaults for test-VM protection and restore drill; the test-VM protection and restore drill still cannot use the vault type designed for newer data-source protection workloads.
- **C — Incorrect.** Enable the required monitoring path and route actionable backup failures to an approved receiver.
  Enable the required monitoring path and route actionable backup failures to an approved receiver. In the test-VM protection and restore drill, this action changes backup monitoring and alerts. Test-VM protection and restore drill instead needs Backup vaults: Choose a Backup vault only for a workload supported by its data-protection model. The backup monitoring and alerts action omits that Backup vaults work.
- **D — Correct.** Choose a Backup vault only for a workload supported by its data-protection model.
  For the test-VM protection and restore drill, the required Backup vaults action is: choose a Backup vault only for a workload supported by its data-protection model. It makes the environment able to use the vault type designed for newer data-source protection workloads.

**Objectives:** `MR-RECOVERY-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Create and manage an Azure Backup vault](https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q13 — A

**Question:** The approach for the test-VM protection and restore drill is approved, but the restore rehearsal environment still cannot define how often recovery points are created and how long they remain. Which implementation step closes the gap?

- **A — Correct.** Configure frequency, time zone, and retention ranges from the recovery objectives.
  Configure frequency, time zone, and retention ranges from the recovery objectives. This changes backup frequency and retention in the test-VM protection and restore drill, supplying the missing state needed to define how often recovery points are created and how long they remain.
- **B — Incorrect.** Trigger an on-demand backup before the destructive test and persist its job ID.
  Trigger an on-demand backup before the destructive test and persist its job ID. In the test-VM protection and restore drill, this action changes on-demand backups. Test-VM protection and restore drill instead needs backup frequency and retention: Configure frequency, time zone, and retention ranges from the recovery objectives. The on-demand backups action omits that backup frequency and retention work.
- **C — Incorrect.** Choose restore disks for controlled validation before deciding whether to replace production resources.
  Choose restore disks for controlled validation before deciding whether to replace production resources. In the test-VM protection and restore drill, this action changes VM restore choices. Test-VM protection and restore drill approved backup frequency and retention, not VM restore choices; only the backup frequency and retention change can define how often recovery points are created and how long they remain.
- **D — Incorrect.** Create the vault in the approved region and resource group before protecting the VM.
  Create the vault in the approved region and resource group before protecting the VM. In the test-VM protection and restore drill, this action changes Recovery Services vaults. Test-VM protection and restore drill requires backup frequency and retention; changing Recovery Services vaults leaves backup frequency and retention absent in test-VM protection and restore drill; test-VM protection and restore drill cannot define how often recovery points are created and how long they remain.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Azure Backup policy fundamentals](https://learn.microsoft.com/en-us/azure/backup/backup-architecture)

**Source reviewed:** 2026-08-31

## LAB24-Q14 — A

**Question:** The recovery administrator protecting and restoring a test VM may change the test-VM protection and restore drill only to associate the intended protection schedule with the test workload. Which restore rehearsal action stays within that assignment?

- **A — Correct.** Enable protection for the exact datasource using the approved policy ID.
  The test-VM protection and restore drill must associate the intended protection schedule with the test workload; this option performs its direct policy association change: enable protection for the exact datasource using the approved policy ID.
- **B — Incorrect.** List recovery points and choose one captured before the simulated data loss.
  List recovery points and choose one captured before the simulated data loss. In the test-VM protection and restore drill, this action changes recovery-point selection. Test-VM protection and restore drill approved policy association, not recovery-point selection; only the policy association change can associate the intended protection schedule with the test workload.
- **C — Incorrect.** Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup.
  Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. In the test-VM protection and restore drill, this action changes backup soft delete. Test-VM protection and restore drill requires policy association; changing backup soft delete leaves policy association absent in test-VM protection and restore drill; test-VM protection and restore drill cannot associate the intended protection schedule with the test workload.
- **D — Incorrect.** Choose a Backup vault only for a workload supported by its data-protection model.
  Choose a Backup vault only for a workload supported by its data-protection model. In the test-VM protection and restore drill, this action changes Backup vaults. Backup vaults does not implement policy association for test-VM protection and restore drill; the test-VM protection and restore drill still cannot associate the intended protection schedule with the test workload.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q15 — D

**Question:** A restore rehearsal dry run shows no test-VM protection and restore drill command will create an extra recovery point before a risky maintenance window. Which action belongs before execution?

- **A — Incorrect.** Use file recovery when only a small set of guest files must be recovered.
  Use file recovery when only a small set of guest files must be recovered. In the test-VM protection and restore drill, this action changes file-level recovery. Test-VM protection and restore drill approved on-demand backups, not file-level recovery; only the on-demand backups change can create an extra recovery point before a risky maintenance window.
- **B — Incorrect.** Enable the required monitoring path and route actionable backup failures to an approved receiver.
  Enable the required monitoring path and route actionable backup failures to an approved receiver. In the test-VM protection and restore drill, this action changes backup monitoring and alerts. Test-VM protection and restore drill requires on-demand backups; changing backup monitoring and alerts leaves on-demand backups absent in test-VM protection and restore drill; test-VM protection and restore drill cannot create an extra recovery point before a risky maintenance window.
- **C — Incorrect.** Configure frequency, time zone, and retention ranges from the recovery objectives.
  Configure frequency, time zone, and retention ranges from the recovery objectives. In the test-VM protection and restore drill, this action changes backup frequency and retention. Backup frequency and retention does not implement on-demand backups for test-VM protection and restore drill; the test-VM protection and restore drill still cannot create an extra recovery point before a risky maintenance window.
- **D — Correct.** Trigger an on-demand backup before the destructive test and persist its job ID.
  Trigger an on-demand backup before the destructive test and persist its job ID. It is the least-change on-demand backups path for the test-VM protection and restore drill requirement to create an extra recovery point before a risky maintenance window.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q16 — A

**Question:** For the test-VM protection and restore drill, operators need to select a recovery point that meets the required recovery time. Which change realizes that requirement?

- **A — Correct.** List recovery points and choose one captured before the simulated data loss.
  List recovery points and choose one captured before the simulated data loss. In test-VM protection and restore drill, applying recovery-point selection is the scoped way to select a recovery point that meets the required recovery time.
- **B — Incorrect.** Choose restore disks for controlled validation before deciding whether to replace production resources.
  Choose restore disks for controlled validation before deciding whether to replace production resources. In the test-VM protection and restore drill, this action changes VM restore choices. VM restore choices does not implement recovery-point selection for test-VM protection and restore drill; the test-VM protection and restore drill still cannot select a recovery point that meets the required recovery time.
- **C — Incorrect.** Create the vault in the approved region and resource group before protecting the VM.
  Create the vault in the approved region and resource group before protecting the VM. In the test-VM protection and restore drill, this action changes Recovery Services vaults. Test-VM protection and restore drill instead needs recovery-point selection: List recovery points and choose one captured before the simulated data loss. The Recovery Services vaults action omits that recovery-point selection work.
- **D — Incorrect.** Enable protection for the exact datasource using the approved policy ID.
  Enable protection for the exact datasource using the approved policy ID. In the test-VM protection and restore drill, this action changes policy association. Test-VM protection and restore drill approved recovery-point selection, not policy association; only the recovery-point selection change can select a recovery point that meets the required recovery time.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q17 — D

**Question:** Operators must automate the test-VM protection and restore drill change needed to recover selected files without replacing the complete virtual machine. Which restore rehearsal operation belongs in the runbook?

- **A — Incorrect.** Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup.
  Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. In the test-VM protection and restore drill, this action changes backup soft delete. Backup soft delete does not implement file-level recovery for test-VM protection and restore drill; the test-VM protection and restore drill still cannot recover selected files without replacing the complete virtual machine.
- **B — Incorrect.** Choose a Backup vault only for a workload supported by its data-protection model.
  Choose a Backup vault only for a workload supported by its data-protection model. In the test-VM protection and restore drill, this action changes Backup vaults. Test-VM protection and restore drill instead needs file-level recovery: Use file recovery when only a small set of guest files must be recovered. The Backup vaults action omits that file-level recovery work.
- **C — Incorrect.** Trigger an on-demand backup before the destructive test and persist its job ID.
  Trigger an on-demand backup before the destructive test and persist its job ID. In the test-VM protection and restore drill, this action changes on-demand backups. Test-VM protection and restore drill approved file-level recovery, not on-demand backups; only the file-level recovery change can recover selected files without replacing the complete virtual machine.
- **D — Correct.** Use file recovery when only a small set of guest files must be recovered.
  Use file recovery when only a small set of guest files must be recovered. The test-VM protection and restore drill uses this file-level recovery operation to recover selected files without replacing the complete virtual machine within the approved scope.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Recover files from an Azure virtual machine backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm)

**Source reviewed:** 2026-08-31

## LAB24-Q18 — D

**Question:** A test-VM protection and restore drill review finds restore rehearsal drift from the need to choose between creating a restored machine and restoring disks for controlled assembly. Which correction addresses that drift?

- **A — Incorrect.** Enable the required monitoring path and route actionable backup failures to an approved receiver.
  Enable the required monitoring path and route actionable backup failures to an approved receiver. In the test-VM protection and restore drill, this action changes backup monitoring and alerts. Test-VM protection and restore drill instead needs VM restore choices: Choose restore disks for controlled validation before deciding whether to replace production resources. The backup monitoring and alerts action omits that VM restore choices work.
- **B — Incorrect.** Configure frequency, time zone, and retention ranges from the recovery objectives.
  Configure frequency, time zone, and retention ranges from the recovery objectives. In the test-VM protection and restore drill, this action changes backup frequency and retention. Test-VM protection and restore drill approved VM restore choices, not backup frequency and retention; only the VM restore choices change can choose between creating a restored machine and restoring disks for controlled assembly.
- **C — Incorrect.** List recovery points and choose one captured before the simulated data loss.
  List recovery points and choose one captured before the simulated data loss. In the test-VM protection and restore drill, this action changes recovery-point selection. Test-VM protection and restore drill requires VM restore choices; changing recovery-point selection leaves VM restore choices absent in test-VM protection and restore drill; test-VM protection and restore drill cannot choose between creating a restored machine and restoring disks for controlled assembly.
- **D — Correct.** Choose restore disks for controlled validation before deciding whether to replace production resources.
  For the test-VM protection and restore drill, the required VM restore choices action is: choose restore disks for controlled validation before deciding whether to replace production resources. It makes the environment able to choose between creating a restored machine and restoring disks for controlled assembly.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q19 — B

**Question:** The test-VM protection and restore drill window permits only the restore rehearsal change needed to hold erased recovery data temporarily so accidental removal can be reversed. Which option respects the boundary?

- **A — Incorrect.** Create the vault in the approved region and resource group before protecting the VM.
  Create the vault in the approved region and resource group before protecting the VM. In the test-VM protection and restore drill, this action changes Recovery Services vaults. Test-VM protection and restore drill approved backup soft delete, not Recovery Services vaults; only the backup soft delete change can hold erased recovery data temporarily so accidental removal can be reversed.
- **B — Correct.** Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup.
  Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. This changes backup soft delete in the test-VM protection and restore drill, supplying the missing state needed to hold erased recovery data temporarily so accidental removal can be reversed.
- **C — Incorrect.** Enable protection for the exact datasource using the approved policy ID.
  Enable protection for the exact datasource using the approved policy ID. In the test-VM protection and restore drill, this action changes policy association. Policy association does not implement backup soft delete for test-VM protection and restore drill; the test-VM protection and restore drill still cannot hold erased recovery data temporarily so accidental removal can be reversed.
- **D — Incorrect.** Use file recovery when only a small set of guest files must be recovered.
  Use file recovery when only a small set of guest files must be recovered. In the test-VM protection and restore drill, this action changes file-level recovery. Test-VM protection and restore drill instead needs backup soft delete: Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. The file-level recovery action omits that backup soft delete work.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Soft delete for Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-security-feature-cloud)

**Source reviewed:** 2026-08-31

## LAB24-Q20 — A

**Question:** The restore rehearsal preflight has passed; the test-VM protection and restore drill must now detect failed protection jobs and route them to operators. Which operation should run?

- **A — Correct.** Enable the required monitoring path and route actionable backup failures to an approved receiver.
  The test-VM protection and restore drill must detect failed protection jobs and route them to operators; this option performs its direct backup monitoring and alerts change: enable the required monitoring path and route actionable backup failures to an approved receiver.
- **B — Incorrect.** Choose a Backup vault only for a workload supported by its data-protection model.
  Choose a Backup vault only for a workload supported by its data-protection model. In the test-VM protection and restore drill, this action changes Backup vaults. Backup vaults does not implement backup monitoring and alerts for test-VM protection and restore drill; the test-VM protection and restore drill still cannot detect failed protection jobs and route them to operators.
- **C — Incorrect.** Trigger an on-demand backup before the destructive test and persist its job ID.
  Trigger an on-demand backup before the destructive test and persist its job ID. In the test-VM protection and restore drill, this action changes on-demand backups. Test-VM protection and restore drill instead needs backup monitoring and alerts: Enable the required monitoring path and route actionable backup failures to an approved receiver. The on-demand backups action omits that backup monitoring and alerts work.
- **D — Incorrect.** Choose restore disks for controlled validation before deciding whether to replace production resources.
  Choose restore disks for controlled validation before deciding whether to replace production resources. In the test-VM protection and restore drill, this action changes VM restore choices. Test-VM protection and restore drill approved backup monitoring and alerts, not VM restore choices; only the backup monitoring and alerts change can detect failed protection jobs and route them to operators.

**Objectives:** `MR-RECOVERY-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Monitor Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor)

**Source reviewed:** 2026-08-31

## LAB24-Q21 — D

**Question:** Before test-VM protection and restore drill cleanup, the restore rehearsal team must reconfirm it can store supported Azure VM protection metadata in the correct vault type. Which read-only inspection should run?

- **A — Incorrect.** Query the protected item and match policy ID, protection state, health, and datasource ID.
  Query the protected item and match policy ID, protection state, health, and datasource ID. In the test-VM protection and restore drill, this check observes policy association. Test-VM protection and restore drill output covers policy association, not Recovery Services vaults; the Recovery Services vaults requirement to store supported Azure VM protection metadata in the correct vault type remains unverified.
- **B — Incorrect.** Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
  Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session. In the test-VM protection and restore drill, this check observes file-level recovery. File-level recovery success in test-VM protection and restore drill cannot verify Recovery Services vaults; test-VM protection and restore drill cannot store supported Azure VM protection metadata in the correct vault type until Recovery Services vaults evidence exists.
- **C — Incorrect.** Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
  Query failed jobs, protection health, alert state, and diagnostic or reporting configuration. In the test-VM protection and restore drill, this check observes backup monitoring and alerts. Test-VM protection and restore drill reads backup monitoring and alerts, leaving Recovery Services vaults unproved in test-VM protection and restore drill; test-VM protection and restore drill still has no Recovery Services vaults proof.
- **D — Correct.** Query vault type, location, provisioningState, storage model, and protected-item count.
  Query vault type, location, provisioningState, storage model, and protected-item count. This is independent Recovery Services vaults evidence for the test-VM protection and restore drill, even if test-VM protection and restore drill setup reports success before Recovery Services vaults becomes observable.

**Objectives:** `MR-RECOVERY-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Create a Recovery Services vault](https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q22 — D

**Question:** The test-VM protection and restore drill setup reports success after the restore rehearsal attempt to use the vault type designed for newer data-source protection workloads. Which restore rehearsal read-only observation proves the test-VM protection and restore drill outcome?

- **A — Incorrect.** Track the backup job to completion and list the resulting recovery point timestamp.
  Track the backup job to completion and list the resulting recovery point timestamp. In the test-VM protection and restore drill, this check observes on-demand backups. On-demand backups success in test-VM protection and restore drill cannot verify Backup vaults; test-VM protection and restore drill cannot use the vault type designed for newer data-source protection workloads until Backup vaults evidence exists.
- **B — Incorrect.** Query the restore job output and resolve every created disk, template, or VM resource ID.
  Query the restore job output and resolve every created disk, template, or VM resource ID. In the test-VM protection and restore drill, this check observes VM restore choices. Test-VM protection and restore drill reads VM restore choices, leaving Backup vaults unproved in test-VM protection and restore drill; test-VM protection and restore drill still has no Backup vaults proof.
- **C — Incorrect.** Query vault type, location, provisioningState, storage model, and protected-item count.
  Query vault type, location, provisioningState, storage model, and protected-item count. In the test-VM protection and restore drill, this check observes Recovery Services vaults. Test-VM protection and restore drill could pass Recovery Services vaults while Backup vaults is wrong; test-VM protection and restore drill still lacks Backup vaults proof.
- **D — Correct.** Query the vault's storage settings, identity, provisioning state, and backup instances.
  Query the vault's storage settings, identity, provisioning state, and backup instances. For test-VM protection and restore drill, this Backup vaults read confirms the service can use the vault type designed for newer data-source protection workloads.

**Objectives:** `MR-RECOVERY-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Create and manage an Azure Backup vault](https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q23 — C

**Question:** The restore rehearsal log says the test-VM protection and restore drill can now define how often recovery points are created and how long they remain. Which restore rehearsal state should the test-VM protection and restore drill acceptance test retain?

- **A — Incorrect.** Compare recovery-point time, type, consistency, and expiry with the incident timeline.
  Compare recovery-point time, type, consistency, and expiry with the incident timeline. In the test-VM protection and restore drill, this check observes recovery-point selection. Test-VM protection and restore drill reads recovery-point selection, leaving backup frequency and retention unproved in test-VM protection and restore drill; test-VM protection and restore drill still has no backup frequency and retention proof.
- **B — Incorrect.** Query soft-delete state and list soft-deleted backup items in the cleanup report.
  Query soft-delete state and list soft-deleted backup items in the cleanup report. In the test-VM protection and restore drill, this check observes backup soft delete. Test-VM protection and restore drill could pass backup soft delete while backup frequency and retention is wrong; test-VM protection and restore drill still lacks backup frequency and retention proof.
- **C — Correct.** Read the policy schedule and retention rules and calculate the oldest expected recovery point.
  Read the policy schedule and retention rules and calculate the oldest expected recovery point. The test-VM protection and restore drill reads backup frequency and retention directly; that backup frequency and retention result proves the test-VM protection and restore drill can define how often recovery points are created and how long they remain without another mutation.
- **D — Incorrect.** Query the vault's storage settings, identity, provisioning state, and backup instances.
  Query the vault's storage settings, identity, provisioning state, and backup instances. In the test-VM protection and restore drill, this check observes Backup vaults. Backup vaults success in test-VM protection and restore drill cannot verify backup frequency and retention; test-VM protection and restore drill cannot define how often recovery points are created and how long they remain until backup frequency and retention evidence exists.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Azure Backup policy fundamentals](https://learn.microsoft.com/en-us/azure/backup/backup-architecture)

**Source reviewed:** 2026-08-31

## LAB24-Q24 — C

**Question:** The test-VM protection and restore drill rejects restore rehearsal exit status as proof it can associate the intended protection schedule with the test workload. Which test-VM protection and restore drill result is valid evidence?

- **A — Incorrect.** Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
  Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session. In the test-VM protection and restore drill, this check observes file-level recovery. Test-VM protection and restore drill could pass file-level recovery while policy association is wrong; test-VM protection and restore drill still lacks policy association proof.
- **B — Incorrect.** Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
  Query failed jobs, protection health, alert state, and diagnostic or reporting configuration. In the test-VM protection and restore drill, this check observes backup monitoring and alerts. Test-VM protection and restore drill output covers backup monitoring and alerts, not policy association; the policy association requirement to associate the intended protection schedule with the test workload remains unverified.
- **C — Correct.** Query the protected item and match policy ID, protection state, health, and datasource ID.
  For the test-VM protection and restore drill, this policy association observation is decisive: query the protected item and match policy ID, protection state, health, and datasource ID. It is test-VM protection and restore drill evidence that operators can associate the intended protection schedule with the test workload.
- **D — Incorrect.** Read the policy schedule and retention rules and calculate the oldest expected recovery point.
  Read the policy schedule and retention rules and calculate the oldest expected recovery point. In the test-VM protection and restore drill, this check observes backup frequency and retention. Test-VM protection and restore drill reads backup frequency and retention, leaving policy association unproved in test-VM protection and restore drill; test-VM protection and restore drill still has no policy association proof.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q25 — B

**Question:** The restore rehearsal validator needs one test-VM protection and restore drill query after the change to create an extra recovery point before a risky maintenance window. Which restore rehearsal property should the test-VM protection and restore drill validator inspect?

- **A — Incorrect.** Query the restore job output and resolve every created disk, template, or VM resource ID.
  Query the restore job output and resolve every created disk, template, or VM resource ID. In the test-VM protection and restore drill, this check observes VM restore choices. Test-VM protection and restore drill output covers VM restore choices, not on-demand backups; the on-demand backups requirement to create an extra recovery point before a risky maintenance window remains unverified.
- **B — Correct.** Track the backup job to completion and list the resulting recovery point timestamp.
  Track the backup job to completion and list the resulting recovery point timestamp. Because the test-VM protection and restore drill check observes on-demand backups, it independently verifies the requirement to create an extra recovery point before a risky maintenance window.
- **C — Incorrect.** Query vault type, location, provisioningState, storage model, and protected-item count.
  Query vault type, location, provisioningState, storage model, and protected-item count. In the test-VM protection and restore drill, this check observes Recovery Services vaults. Test-VM protection and restore drill reads Recovery Services vaults, leaving on-demand backups unproved in test-VM protection and restore drill; test-VM protection and restore drill still has no on-demand backups proof.
- **D — Incorrect.** Query the protected item and match policy ID, protection state, health, and datasource ID.
  Query the protected item and match policy ID, protection state, health, and datasource ID. In the test-VM protection and restore drill, this check observes policy association. Test-VM protection and restore drill could pass policy association while on-demand backups is wrong; test-VM protection and restore drill still lacks on-demand backups proof.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q26 — A

**Question:** The recovery administrator protecting and restoring a test VM must confirm the test-VM protection and restore drill, without mutation, can select a recovery point that meets the required recovery time. Which restore rehearsal check qualifies?

- **A — Correct.** Compare recovery-point time, type, consistency, and expiry with the incident timeline.
  The test-VM protection and restore drill validator needs this recovery-point selection result: compare recovery-point time, type, consistency, and expiry with the incident timeline. It proves the outcome to select a recovery point that meets the required recovery time rather than an adjacent checkpoint.
- **B — Incorrect.** Query soft-delete state and list soft-deleted backup items in the cleanup report.
  Query soft-delete state and list soft-deleted backup items in the cleanup report. In the test-VM protection and restore drill, this check observes backup soft delete. Test-VM protection and restore drill reads backup soft delete, leaving recovery-point selection unproved in test-VM protection and restore drill; test-VM protection and restore drill still has no recovery-point selection proof.
- **C — Incorrect.** Query the vault's storage settings, identity, provisioning state, and backup instances.
  Query the vault's storage settings, identity, provisioning state, and backup instances. In the test-VM protection and restore drill, this check observes Backup vaults. Test-VM protection and restore drill could pass Backup vaults while recovery-point selection is wrong; test-VM protection and restore drill still lacks recovery-point selection proof.
- **D — Incorrect.** Track the backup job to completion and list the resulting recovery point timestamp.
  Track the backup job to completion and list the resulting recovery point timestamp. In the test-VM protection and restore drill, this check observes on-demand backups. Test-VM protection and restore drill output covers on-demand backups, not recovery-point selection; the recovery-point selection requirement to select a recovery point that meets the required recovery time remains unverified.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q27 — A

**Question:** The test-VM protection and restore drill configuration is complete; the restore rehearsal reviewers need evidence it can recover selected files without replacing the complete virtual machine. Which observation shows success?

- **A — Correct.** Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
  Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session. This is independent file-level recovery evidence for the test-VM protection and restore drill, even if test-VM protection and restore drill setup reports success before file-level recovery becomes observable.
- **B — Incorrect.** Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
  Query failed jobs, protection health, alert state, and diagnostic or reporting configuration. In the test-VM protection and restore drill, this check observes backup monitoring and alerts. Test-VM protection and restore drill could pass backup monitoring and alerts while file-level recovery is wrong; test-VM protection and restore drill still lacks file-level recovery proof.
- **C — Incorrect.** Read the policy schedule and retention rules and calculate the oldest expected recovery point.
  Read the policy schedule and retention rules and calculate the oldest expected recovery point. In the test-VM protection and restore drill, this check observes backup frequency and retention. Test-VM protection and restore drill output covers backup frequency and retention, not file-level recovery; the file-level recovery requirement to recover selected files without replacing the complete virtual machine remains unverified.
- **D — Incorrect.** Compare recovery-point time, type, consistency, and expiry with the incident timeline.
  Compare recovery-point time, type, consistency, and expiry with the incident timeline. In the test-VM protection and restore drill, this check observes recovery-point selection. Recovery-point selection success in test-VM protection and restore drill cannot verify file-level recovery; test-VM protection and restore drill cannot recover selected files without replacing the complete virtual machine until file-level recovery evidence exists.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Recover files from an Azure virtual machine backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm)

**Source reviewed:** 2026-08-31

## LAB24-Q28 — D

**Question:** The restore rehearsal validation asks whether the test-VM protection and restore drill can choose between creating a restored machine and restoring disks for controlled assembly. Which observable state is strongest?

- **A — Incorrect.** Query vault type, location, provisioningState, storage model, and protected-item count.
  Query vault type, location, provisioningState, storage model, and protected-item count. In the test-VM protection and restore drill, this check observes Recovery Services vaults. Test-VM protection and restore drill could pass Recovery Services vaults while VM restore choices is wrong; test-VM protection and restore drill still lacks VM restore choices proof.
- **B — Incorrect.** Query the protected item and match policy ID, protection state, health, and datasource ID.
  Query the protected item and match policy ID, protection state, health, and datasource ID. In the test-VM protection and restore drill, this check observes policy association. Test-VM protection and restore drill output covers policy association, not VM restore choices; the VM restore choices requirement to choose between creating a restored machine and restoring disks for controlled assembly remains unverified.
- **C — Incorrect.** Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
  Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session. In the test-VM protection and restore drill, this check observes file-level recovery. File-level recovery success in test-VM protection and restore drill cannot verify VM restore choices; test-VM protection and restore drill cannot choose between creating a restored machine and restoring disks for controlled assembly until VM restore choices evidence exists.
- **D — Correct.** Query the restore job output and resolve every created disk, template, or VM resource ID.
  Query the restore job output and resolve every created disk, template, or VM resource ID. For test-VM protection and restore drill, this VM restore choices read confirms the service can choose between creating a restored machine and restoring disks for controlled assembly.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q29 — A

**Question:** A test-VM protection and restore drill review must prove the restore rehearsal ability to hold erased recovery data temporarily so accidental removal can be reversed. Which check avoids an adjacent feature?

- **A — Correct.** Query soft-delete state and list soft-deleted backup items in the cleanup report.
  Query soft-delete state and list soft-deleted backup items in the cleanup report. The test-VM protection and restore drill reads backup soft delete directly; that backup soft delete result proves the test-VM protection and restore drill can hold erased recovery data temporarily so accidental removal can be reversed without another mutation.
- **B — Incorrect.** Query the vault's storage settings, identity, provisioning state, and backup instances.
  Query the vault's storage settings, identity, provisioning state, and backup instances. In the test-VM protection and restore drill, this check observes Backup vaults. Backup vaults success in test-VM protection and restore drill cannot verify backup soft delete; test-VM protection and restore drill cannot hold erased recovery data temporarily so accidental removal can be reversed until backup soft delete evidence exists.
- **C — Incorrect.** Track the backup job to completion and list the resulting recovery point timestamp.
  Track the backup job to completion and list the resulting recovery point timestamp. In the test-VM protection and restore drill, this check observes on-demand backups. Test-VM protection and restore drill reads on-demand backups, leaving backup soft delete unproved in test-VM protection and restore drill; test-VM protection and restore drill still has no backup soft delete proof.
- **D — Incorrect.** Query the restore job output and resolve every created disk, template, or VM resource ID.
  Query the restore job output and resolve every created disk, template, or VM resource ID. In the test-VM protection and restore drill, this check observes VM restore choices. Test-VM protection and restore drill could pass VM restore choices while backup soft delete is wrong; test-VM protection and restore drill still lacks backup soft delete proof.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Soft delete for Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-security-feature-cloud)

**Source reviewed:** 2026-08-31

## LAB24-Q30 — A

**Question:** The test-VM protection and restore drill evidence bundle needs a restore rehearsal result showing it can detect failed protection jobs and route them to operators. Which result belongs in the checkpoint?

- **A — Correct.** Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
  For the test-VM protection and restore drill, this backup monitoring and alerts observation is decisive: query failed jobs, protection health, alert state, and diagnostic or reporting configuration. It is test-VM protection and restore drill evidence that operators can detect failed protection jobs and route them to operators.
- **B — Incorrect.** Read the policy schedule and retention rules and calculate the oldest expected recovery point.
  Read the policy schedule and retention rules and calculate the oldest expected recovery point. In the test-VM protection and restore drill, this check observes backup frequency and retention. Test-VM protection and restore drill reads backup frequency and retention, leaving backup monitoring and alerts unproved in test-VM protection and restore drill; test-VM protection and restore drill still has no backup monitoring and alerts proof.
- **C — Incorrect.** Compare recovery-point time, type, consistency, and expiry with the incident timeline.
  Compare recovery-point time, type, consistency, and expiry with the incident timeline. In the test-VM protection and restore drill, this check observes recovery-point selection. Test-VM protection and restore drill could pass recovery-point selection while backup monitoring and alerts is wrong; test-VM protection and restore drill still lacks backup monitoring and alerts proof.
- **D — Incorrect.** Query soft-delete state and list soft-deleted backup items in the cleanup report.
  Query soft-delete state and list soft-deleted backup items in the cleanup report. In the test-VM protection and restore drill, this check observes backup soft delete. Test-VM protection and restore drill output covers backup soft delete, not backup monitoring and alerts; the backup monitoring and alerts requirement to detect failed protection jobs and route them to operators remains unverified.

**Objectives:** `MR-RECOVERY-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Monitor Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor)

**Source reviewed:** 2026-08-31

## LAB24-Q31 — C

**Question:** Other test-VM protection and restore drill components are healthy, but the restore rehearsal still cannot store supported Azure VM protection metadata in the correct vault type. Which state causes the isolated failure?

- **A — Incorrect.** The runbook attempts to configure classic Azure VM backup in an incompatible vault type.
  The runbook attempts to configure classic Azure VM backup in an incompatible vault type. The test-VM protection and restore drill fault concerns Backup vaults. Test-VM protection and restore drill has Backup vaults impact, but Recovery Services vaults is the test-VM protection and restore drill failed path; the Backup vaults state cannot produce Recovery Services vaults failure.
- **B — Incorrect.** The selected recovery point was created after the unwanted change.
  The selected recovery point was created after the unwanted change. The test-VM protection and restore drill fault concerns recovery-point selection. Test-VM protection and restore drill could repair recovery-point selection while Recovery Services vaults stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to store supported Azure VM protection metadata in the correct vault type.
- **C — Correct.** The vault is in a region that cannot protect the selected VM with the required scenario.
  The vault is in a region that cannot protect the selected VM with the required scenario. The finding is specific to Recovery Services vaults in the test-VM protection and restore drill; repairing Recovery Services vaults restores the test-VM protection and restore drill ability to store supported Azure VM protection metadata in the correct vault type.
- **D — Incorrect.** The backup failed, but no alert route covers the vault or datasource scope.
  The backup failed, but no alert route covers the vault or datasource scope. The test-VM protection and restore drill fault concerns backup monitoring and alerts. Test-VM protection and restore drill may fix backup monitoring and alerts, yet Recovery Services vaults still fails; this test-VM protection and restore drill diagnosis of backup monitoring and alerts is wrong for Recovery Services vaults.

**Objectives:** `MR-RECOVERY-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Create a Recovery Services vault](https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q32 — C

**Question:** During a restore rehearsal fault drill, the test-VM protection and restore drill does not use the vault type designed for newer data-source protection workloads. Which finding identifies the defect?

- **A — Incorrect.** Daily recovery points expire sooner than the required recovery window.
  Daily recovery points expire sooner than the required recovery window. The test-VM protection and restore drill fault concerns backup frequency and retention. Test-VM protection and restore drill could repair backup frequency and retention while Backup vaults stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to use the vault type designed for newer data-source protection workloads.
- **B — Incorrect.** The recovery session was left mounted after the files were copied.
  The recovery session was left mounted after the files were copied. The test-VM protection and restore drill fault concerns file-level recovery. Test-VM protection and restore drill failed on Backup vaults; this file-level recovery finding redirects test-VM protection and restore drill remediation away from Backup vaults.
- **C — Correct.** The runbook attempts to configure classic Azure VM backup in an incompatible vault type.
  The test-VM protection and restore drill cannot use the vault type designed for newer data-source protection workloads because of this Backup vaults defect: the runbook attempts to configure classic Azure VM backup in an incompatible vault type. The symptom and repair align.
- **D — Incorrect.** The vault is in a region that cannot protect the selected VM with the required scenario.
  The vault is in a region that cannot protect the selected VM with the required scenario. The test-VM protection and restore drill fault concerns Recovery Services vaults. Test-VM protection and restore drill has Recovery Services vaults impact, but Backup vaults is the test-VM protection and restore drill failed path; the Recovery Services vaults state cannot produce Backup vaults failure.

**Objectives:** `MR-RECOVERY-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Create and manage an Azure Backup vault](https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q33 — A

**Question:** The test-VM protection and restore drill setup finishes, yet the restore rehearsal cannot define how often recovery points are created and how long they remain. Which misconfiguration explains the mismatch?

- **A — Correct.** Daily recovery points expire sooner than the required recovery window.
  Daily recovery points expire sooner than the required recovery window. Removing this backup frequency and retention condition lets the test-VM protection and restore drill define how often recovery points are created and how long they remain while leaving healthy controls unchanged.
- **B — Incorrect.** The policy exists, but the VM has never been registered as a protected item.
  The policy exists, but the VM has never been registered as a protected item. The test-VM protection and restore drill fault concerns policy association. Test-VM protection and restore drill may fix policy association, yet backup frequency and retention still fails; this test-VM protection and restore drill diagnosis of policy association is wrong for backup frequency and retention.
- **C — Incorrect.** The runbook selects replace disks without first validating application recovery impact.
  The runbook selects replace disks without first validating application recovery impact. The test-VM protection and restore drill fault concerns VM restore choices. Test-VM protection and restore drill has VM restore choices impact, but backup frequency and retention is the test-VM protection and restore drill failed path; the VM restore choices state cannot produce backup frequency and retention failure.
- **D — Incorrect.** The runbook attempts to configure classic Azure VM backup in an incompatible vault type.
  The runbook attempts to configure classic Azure VM backup in an incompatible vault type. The test-VM protection and restore drill fault concerns Backup vaults. Test-VM protection and restore drill could repair Backup vaults while backup frequency and retention stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to define how often recovery points are created and how long they remain.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Azure Backup policy fundamentals](https://learn.microsoft.com/en-us/azure/backup/backup-architecture)

**Source reviewed:** 2026-08-31

## LAB24-Q34 — B

**Question:** A restore rehearsal break/fix in the test-VM protection and restore drill fails when operators try to associate the intended protection schedule with the test workload. Which diagnosis fits?

- **A — Incorrect.** The lab starts its break/fix change before the backup job finishes.
  The lab starts its break/fix change before the backup job finishes. The test-VM protection and restore drill fault concerns on-demand backups. Test-VM protection and restore drill may fix on-demand backups, yet policy association still fails; this test-VM protection and restore drill diagnosis of on-demand backups is wrong for policy association.
- **B — Correct.** The policy exists, but the VM has never been registered as a protected item.
  The policy exists, but the VM has never been registered as a protected item. In test-VM protection and restore drill, this policy association cause matches the failure to associate the intended protection schedule with the test workload.
- **C — Incorrect.** Cleanup reports success while a soft-deleted protected item remains undocumented.
  Cleanup reports success while a soft-deleted protected item remains undocumented. The test-VM protection and restore drill fault concerns backup soft delete. Test-VM protection and restore drill could repair backup soft delete while policy association stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to associate the intended protection schedule with the test workload.
- **D — Incorrect.** Daily recovery points expire sooner than the required recovery window.
  Daily recovery points expire sooner than the required recovery window. The test-VM protection and restore drill fault concerns backup frequency and retention. Test-VM protection and restore drill failed on policy association; this backup frequency and retention finding redirects test-VM protection and restore drill remediation away from policy association.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q35 — C

**Question:** The test-VM protection and restore drill troubleshooting scope is the restore rehearsal need to create an extra recovery point before a risky maintenance window. Which condition should be corrected first?

- **A — Incorrect.** The selected recovery point was created after the unwanted change.
  The selected recovery point was created after the unwanted change. The test-VM protection and restore drill fault concerns recovery-point selection. Test-VM protection and restore drill has recovery-point selection impact, but on-demand backups is the test-VM protection and restore drill failed path; the recovery-point selection state cannot produce on-demand backups failure.
- **B — Incorrect.** The backup failed, but no alert route covers the vault or datasource scope.
  The backup failed, but no alert route covers the vault or datasource scope. The test-VM protection and restore drill fault concerns backup monitoring and alerts. Test-VM protection and restore drill could repair backup monitoring and alerts while on-demand backups stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to create an extra recovery point before a risky maintenance window.
- **C — Correct.** The lab starts its break/fix change before the backup job finishes.
  The lab starts its break/fix change before the backup job finishes. This test-VM protection and restore drill condition breaks on-demand backups, explaining why operators cannot create an extra recovery point before a risky maintenance window.
- **D — Incorrect.** The policy exists, but the VM has never been registered as a protected item.
  The policy exists, but the VM has never been registered as a protected item. The test-VM protection and restore drill fault concerns policy association. Test-VM protection and restore drill may fix policy association, yet on-demand backups still fails; this test-VM protection and restore drill diagnosis of policy association is wrong for on-demand backups.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q36 — C

**Question:** The test-VM protection and restore drill result is partial because the restore rehearsal cannot select a recovery point that meets the required recovery time. Which condition accounts for that result?

- **A — Incorrect.** The recovery session was left mounted after the files were copied.
  The recovery session was left mounted after the files were copied. The test-VM protection and restore drill fault concerns file-level recovery. Test-VM protection and restore drill could repair file-level recovery while recovery-point selection stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to select a recovery point that meets the required recovery time.
- **B — Incorrect.** The vault is in a region that cannot protect the selected VM with the required scenario.
  The vault is in a region that cannot protect the selected VM with the required scenario. The test-VM protection and restore drill fault concerns Recovery Services vaults. Test-VM protection and restore drill failed on recovery-point selection; this Recovery Services vaults finding redirects test-VM protection and restore drill remediation away from recovery-point selection.
- **C — Correct.** The selected recovery point was created after the unwanted change.
  For the test-VM protection and restore drill, the recovery-point selection failure is causal: the selected recovery point was created after the unwanted change. Correcting it restores the ability to select a recovery point that meets the required recovery time.
- **D — Incorrect.** The lab starts its break/fix change before the backup job finishes.
  The lab starts its break/fix change before the backup job finishes. The test-VM protection and restore drill fault concerns on-demand backups. Test-VM protection and restore drill has on-demand backups impact, but recovery-point selection is the test-VM protection and restore drill failed path; the on-demand backups state cannot produce recovery-point selection failure.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q37 — B

**Question:** The restore rehearsal evidence shows the test-VM protection and restore drill cannot recover selected files without replacing the complete virtual machine. Which root cause fits that evidence?

- **A — Incorrect.** The runbook selects replace disks without first validating application recovery impact.
  The runbook selects replace disks without first validating application recovery impact. The test-VM protection and restore drill fault concerns VM restore choices. Test-VM protection and restore drill failed on file-level recovery; this VM restore choices finding redirects test-VM protection and restore drill remediation away from file-level recovery.
- **B — Correct.** The recovery session was left mounted after the files were copied.
  The recovery session was left mounted after the files were copied. The finding is specific to file-level recovery in the test-VM protection and restore drill; repairing file-level recovery restores the test-VM protection and restore drill ability to recover selected files without replacing the complete virtual machine.
- **C — Incorrect.** The runbook attempts to configure classic Azure VM backup in an incompatible vault type.
  The runbook attempts to configure classic Azure VM backup in an incompatible vault type. The test-VM protection and restore drill fault concerns Backup vaults. Test-VM protection and restore drill has Backup vaults impact, but file-level recovery is the test-VM protection and restore drill failed path; the Backup vaults state cannot produce file-level recovery failure.
- **D — Incorrect.** The selected recovery point was created after the unwanted change.
  The selected recovery point was created after the unwanted change. The test-VM protection and restore drill fault concerns recovery-point selection. Test-VM protection and restore drill could repair recovery-point selection while file-level recovery stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to recover selected files without replacing the complete virtual machine.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Recover files from an Azure virtual machine backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm)

**Source reviewed:** 2026-08-31

## LAB24-Q38 — D

**Question:** Although the test-VM protection and restore drill is meant to let the restore rehearsal choose between creating a restored machine and restoring disks for controlled assembly, its checkpoint fails. Which restore rehearsal defect explains the failure?

- **A — Incorrect.** Cleanup reports success while a soft-deleted protected item remains undocumented.
  Cleanup reports success while a soft-deleted protected item remains undocumented. The test-VM protection and restore drill fault concerns backup soft delete. Test-VM protection and restore drill may fix backup soft delete, yet VM restore choices still fails; this test-VM protection and restore drill diagnosis of backup soft delete is wrong for VM restore choices.
- **B — Incorrect.** Daily recovery points expire sooner than the required recovery window.
  Daily recovery points expire sooner than the required recovery window. The test-VM protection and restore drill fault concerns backup frequency and retention. Test-VM protection and restore drill has backup frequency and retention impact, but VM restore choices is the test-VM protection and restore drill failed path; the backup frequency and retention state cannot produce VM restore choices failure.
- **C — Incorrect.** The recovery session was left mounted after the files were copied.
  The recovery session was left mounted after the files were copied. The test-VM protection and restore drill fault concerns file-level recovery. Test-VM protection and restore drill could repair file-level recovery while VM restore choices stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to choose between creating a restored machine and restoring disks for controlled assembly.
- **D — Correct.** The runbook selects replace disks without first validating application recovery impact.
  The test-VM protection and restore drill cannot choose between creating a restored machine and restoring disks for controlled assembly because of this VM restore choices defect: the runbook selects replace disks without first validating application recovery impact. The symptom and repair align.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q39 — B

**Question:** The restore rehearsal support team isolated the test-VM protection and restore drill incident to the attempt to hold erased recovery data temporarily so accidental removal can be reversed. Which condition prevents success?

- **A — Incorrect.** The backup failed, but no alert route covers the vault or datasource scope.
  The backup failed, but no alert route covers the vault or datasource scope. The test-VM protection and restore drill fault concerns backup monitoring and alerts. Test-VM protection and restore drill has backup monitoring and alerts impact, but backup soft delete is the test-VM protection and restore drill failed path; the backup monitoring and alerts state cannot produce backup soft delete failure.
- **B — Correct.** Cleanup reports success while a soft-deleted protected item remains undocumented.
  Cleanup reports success while a soft-deleted protected item remains undocumented. Removing this backup soft delete condition lets the test-VM protection and restore drill hold erased recovery data temporarily so accidental removal can be reversed while leaving healthy controls unchanged.
- **C — Incorrect.** The policy exists, but the VM has never been registered as a protected item.
  The policy exists, but the VM has never been registered as a protected item. The test-VM protection and restore drill fault concerns policy association. Test-VM protection and restore drill failed on backup soft delete; this policy association finding redirects test-VM protection and restore drill remediation away from backup soft delete.
- **D — Incorrect.** The runbook selects replace disks without first validating application recovery impact.
  The runbook selects replace disks without first validating application recovery impact. The test-VM protection and restore drill fault concerns VM restore choices. Test-VM protection and restore drill may fix VM restore choices, yet backup soft delete still fails; this test-VM protection and restore drill diagnosis of VM restore choices is wrong for backup soft delete.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Soft delete for Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-security-feature-cloud)

**Source reviewed:** 2026-08-31

## LAB24-Q40 — C

**Question:** A test-VM protection and restore drill query surprises the recovery administrator protecting and restoring a test VM during the restore rehearsal attempt to detect failed protection jobs and route them to operators. Which finding explains it?

- **A — Incorrect.** The vault is in a region that cannot protect the selected VM with the required scenario.
  The vault is in a region that cannot protect the selected VM with the required scenario. The test-VM protection and restore drill fault concerns Recovery Services vaults. Test-VM protection and restore drill could repair Recovery Services vaults while backup monitoring and alerts stays broken in test-VM protection and restore drill; the test-VM protection and restore drill remains unable to detect failed protection jobs and route them to operators.
- **B — Incorrect.** The lab starts its break/fix change before the backup job finishes.
  The lab starts its break/fix change before the backup job finishes. The test-VM protection and restore drill fault concerns on-demand backups. Test-VM protection and restore drill failed on backup monitoring and alerts; this on-demand backups finding redirects test-VM protection and restore drill remediation away from backup monitoring and alerts.
- **C — Correct.** The backup failed, but no alert route covers the vault or datasource scope.
  The backup failed, but no alert route covers the vault or datasource scope. In test-VM protection and restore drill, this backup monitoring and alerts cause matches the failure to detect failed protection jobs and route them to operators.
- **D — Incorrect.** Cleanup reports success while a soft-deleted protected item remains undocumented.
  Cleanup reports success while a soft-deleted protected item remains undocumented. The test-VM protection and restore drill fault concerns backup soft delete. Test-VM protection and restore drill has backup soft delete impact, but backup monitoring and alerts is the test-VM protection and restore drill failed path; the backup soft delete state cannot produce backup monitoring and alerts failure.

**Objectives:** `MR-RECOVERY-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Monitor Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor)

**Source reviewed:** 2026-08-31

## LAB24-Q41 — B

**Question:** The test-VM protection and restore drill checkpoint requires both this restore rehearsal outcome—store supported Azure VM protection metadata in the correct vault type—and a read-only test-VM protection and restore drill state check. Which restore rehearsal response is complete?

- **A — Incorrect.** First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.
  First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point. This test-VM protection and restore drill pair serves backup frequency and retention. Backup frequency and retention cannot replace Recovery Services vaults in test-VM protection and restore drill. Use this Recovery Services vaults pair instead: First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.
- **B — Correct.** First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.
  First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count. In the test-VM protection and restore drill, the first Recovery Services vaults step runs; the test-VM protection and restore drill then reads Recovery Services vaults state to prove it can store supported Azure VM protection metadata in the correct vault type.
- **C — Incorrect.** First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
  First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session. This test-VM protection and restore drill pair serves file-level recovery. Test-VM protection and restore drill uses file-level recovery for both steps; Recovery Services vaults remains untouched in test-VM protection and restore drill, so its Recovery Services vaults gate to store supported Azure VM protection metadata in the correct vault type fails.
- **D — Incorrect.** First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID.
  First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID. This test-VM protection and restore drill pair serves VM restore choices. Test-VM protection and restore drill closes VM restore choices, not Recovery Services vaults; without the Recovery Services vaults workflow, it cannot store supported Azure VM protection metadata in the correct vault type.

**Objectives:** `MR-RECOVERY-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Create a Recovery Services vault](https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q42 — B

**Question:** The test-VM protection and restore drill runbook must use the vault type designed for newer data-source protection workloads, then retain restore rehearsal read-back evidence. Which test-VM protection and restore drill pair completes both duties?

- **A — Incorrect.** First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.
  First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID. This test-VM protection and restore drill pair serves policy association. Test-VM protection and restore drill proves policy association, but Backup vaults lacks implementation in test-VM protection and restore drill and Backup vaults proof; the Backup vaults outcome to use the vault type designed for newer data-source protection workloads remains open.
- **B — Correct.** First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.
  For the test-VM protection and restore drill, the safe Backup vaults order is: first, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances. The test-VM protection and restore drill records Backup vaults proof after configuration.
- **C — Incorrect.** First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID.
  First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID. This test-VM protection and restore drill pair serves VM restore choices. Test-VM protection and restore drill closes VM restore choices, not Backup vaults; without the Backup vaults workflow, it cannot use the vault type designed for newer data-source protection workloads.
- **D — Incorrect.** First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.
  First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report. This test-VM protection and restore drill pair serves backup soft delete. Backup soft delete cannot replace Backup vaults in test-VM protection and restore drill. Use this Backup vaults pair instead: First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.

**Objectives:** `MR-RECOVERY-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Create and manage an Azure Backup vault](https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault)

**Source reviewed:** 2026-08-31

## LAB24-Q43 — B

**Question:** To satisfy the restore rehearsal requirement, operators must change the test-VM protection and restore drill configuration and prove it can define how often recovery points are created and how long they remain. Which sequence is coherent?

- **A — Incorrect.** First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.
  First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp. This test-VM protection and restore drill pair serves on-demand backups. Test-VM protection and restore drill uses on-demand backups for both steps; backup frequency and retention remains untouched in test-VM protection and restore drill, so its backup frequency and retention gate to define how often recovery points are created and how long they remain fails.
- **B — Correct.** First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.
  First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point. The test-VM protection and restore drill uses its backup frequency and retention mutation gate and backup frequency and retention verification gate before it can define how often recovery points are created and how long they remain.
- **C — Incorrect.** First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.
  First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report. This test-VM protection and restore drill pair serves backup soft delete. Backup soft delete cannot replace backup frequency and retention in test-VM protection and restore drill. Use this backup frequency and retention pair instead: First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.
- **D — Incorrect.** First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
  First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration. This test-VM protection and restore drill pair serves backup monitoring and alerts. Test-VM protection and restore drill proves backup monitoring and alerts, but backup frequency and retention lacks implementation in test-VM protection and restore drill and backup frequency and retention proof; the backup frequency and retention outcome to define how often recovery points are created and how long they remain remains open.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Azure Backup policy fundamentals](https://learn.microsoft.com/en-us/azure/backup/backup-architecture)

**Source reviewed:** 2026-08-31

## LAB24-Q44 — C

**Question:** The recovery administrator protecting and restoring a test VM needs a safe test-VM protection and restore drill change to associate the intended protection schedule with the test workload, followed by restore rehearsal evidence. Which pair merits approval?

- **A — Incorrect.** First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.
  First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline. This test-VM protection and restore drill pair serves recovery-point selection. Test-VM protection and restore drill closes recovery-point selection, not policy association; without the policy association workflow, it cannot associate the intended protection schedule with the test workload.
- **B — Incorrect.** First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
  First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration. This test-VM protection and restore drill pair serves backup monitoring and alerts. Backup monitoring and alerts cannot replace policy association in test-VM protection and restore drill. Use this policy association pair instead: First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.
- **C — Correct.** First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.
  The test-VM protection and restore drill gets a complete policy association sequence here: first, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID. Read-back evidence follows the change.
- **D — Incorrect.** First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.
  First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count. This test-VM protection and restore drill pair serves Recovery Services vaults. Test-VM protection and restore drill uses Recovery Services vaults for both steps; policy association remains untouched in test-VM protection and restore drill, so its policy association gate to associate the intended protection schedule with the test workload fails.

**Objectives:** `MR-RECOVERY-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q45 — D

**Question:** The test-VM protection and restore drill has two restore rehearsal gates: create an extra recovery point before a risky maintenance window, then prove the test-VM protection and restore drill state. Which restore rehearsal sequence works?

- **A — Incorrect.** First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
  First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session. This test-VM protection and restore drill pair serves file-level recovery. File-level recovery cannot replace on-demand backups in test-VM protection and restore drill. Use this on-demand backups pair instead: First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.
- **B — Incorrect.** First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.
  First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count. This test-VM protection and restore drill pair serves Recovery Services vaults. Test-VM protection and restore drill proves Recovery Services vaults, but on-demand backups lacks implementation in test-VM protection and restore drill and on-demand backups proof; the on-demand backups outcome to create an extra recovery point before a risky maintenance window remains open.
- **C — Incorrect.** First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.
  First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances. This test-VM protection and restore drill pair serves Backup vaults. Test-VM protection and restore drill uses Backup vaults for both steps; on-demand backups remains untouched in test-VM protection and restore drill, so its on-demand backups gate to create an extra recovery point before a risky maintenance window fails.
- **D — Correct.** First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.
  First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp. This ordered on-demand backups workflow lets the test-VM protection and restore drill create an extra recovery point before a risky maintenance window and then verify the resulting state.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Back up Azure virtual machines with Azure CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli)

**Source reviewed:** 2026-08-31

## LAB24-Q46 — A

**Question:** Which restore rehearsal path makes the test-VM protection and restore drill able to select a recovery point that meets the required recovery time, then inspects the defining properties?

- **A — Correct.** First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.
  First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline. For test-VM protection and restore drill, the recovery-point selection operation precedes its recovery-point selection read-back check, allowing it to select a recovery point that meets the required recovery time.
- **B — Incorrect.** First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID.
  First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID. This test-VM protection and restore drill pair serves VM restore choices. Test-VM protection and restore drill uses VM restore choices for both steps; recovery-point selection remains untouched in test-VM protection and restore drill, so its recovery-point selection gate to select a recovery point that meets the required recovery time fails.
- **C — Incorrect.** First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.
  First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances. This test-VM protection and restore drill pair serves Backup vaults. Test-VM protection and restore drill closes Backup vaults, not recovery-point selection; without the recovery-point selection workflow, it cannot select a recovery point that meets the required recovery time.
- **D — Incorrect.** First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.
  First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point. This test-VM protection and restore drill pair serves backup frequency and retention. Backup frequency and retention cannot replace recovery-point selection in test-VM protection and restore drill. Use this recovery-point selection pair instead: First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB24-CP01`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q47 — C

**Question:** At the test-VM protection and restore drill approval gate, operators must show that the restore rehearsal can recover selected files without replacing the complete virtual machine. Which restore rehearsal configure-and-check pair is defensible?

- **A — Incorrect.** First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.
  First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report. This test-VM protection and restore drill pair serves backup soft delete. Test-VM protection and restore drill uses backup soft delete for both steps; file-level recovery remains untouched in test-VM protection and restore drill, so its file-level recovery gate to recover selected files without replacing the complete virtual machine fails.
- **B — Incorrect.** First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.
  First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point. This test-VM protection and restore drill pair serves backup frequency and retention. Test-VM protection and restore drill closes backup frequency and retention, not file-level recovery; without the file-level recovery workflow, it cannot recover selected files without replacing the complete virtual machine.
- **C — Correct.** First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
  First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session. In the test-VM protection and restore drill, the first file-level recovery step runs; the test-VM protection and restore drill then reads file-level recovery state to prove it can recover selected files without replacing the complete virtual machine.
- **D — Incorrect.** First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.
  First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID. This test-VM protection and restore drill pair serves policy association. Test-VM protection and restore drill proves policy association, but file-level recovery lacks implementation in test-VM protection and restore drill and file-level recovery proof; the file-level recovery outcome to recover selected files without replacing the complete virtual machine remains open.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB24-CP02`).

**Microsoft Learn sources:**

- [Recover files from an Azure virtual machine backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm)

**Source reviewed:** 2026-08-31

## LAB24-Q48 — B

**Question:** The test-VM protection and restore drill forbids a partial restore rehearsal result. Operators must first choose between creating a restored machine and restoring disks for controlled assembly and afterward confirm the test-VM protection and restore drill outcome. Which restore rehearsal sequence is complete?

- **A — Incorrect.** First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
  First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration. This test-VM protection and restore drill pair serves backup monitoring and alerts. Test-VM protection and restore drill closes backup monitoring and alerts, not VM restore choices; without the VM restore choices workflow, it cannot choose between creating a restored machine and restoring disks for controlled assembly.
- **B — Correct.** First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID.
  For the test-VM protection and restore drill, the safe VM restore choices order is: first, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID. The test-VM protection and restore drill records VM restore choices proof after configuration.
- **C — Incorrect.** First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.
  First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID. This test-VM protection and restore drill pair serves policy association. Test-VM protection and restore drill proves policy association, but VM restore choices lacks implementation in test-VM protection and restore drill and VM restore choices proof; the VM restore choices outcome to choose between creating a restored machine and restoring disks for controlled assembly remains open.
- **D — Incorrect.** First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.
  First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp. This test-VM protection and restore drill pair serves on-demand backups. Test-VM protection and restore drill uses on-demand backups for both steps; VM restore choices remains untouched in test-VM protection and restore drill, so its VM restore choices gate to choose between creating a restored machine and restoring disks for controlled assembly fails.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB24-CP03`).

**Microsoft Learn sources:**

- [Restore Azure virtual machines](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)

**Source reviewed:** 2026-08-31

## LAB24-Q49 — D

**Question:** Only the test-VM protection and restore drill change needed to hold erased recovery data temporarily so accidental removal can be reversed is allowed, and restore rehearsal proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.
  First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count. This test-VM protection and restore drill pair serves Recovery Services vaults. Recovery Services vaults cannot replace backup soft delete in test-VM protection and restore drill. Use this backup soft delete pair instead: First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.
- **B — Incorrect.** First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.
  First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp. This test-VM protection and restore drill pair serves on-demand backups. Test-VM protection and restore drill proves on-demand backups, but backup soft delete lacks implementation in test-VM protection and restore drill and backup soft delete proof; the backup soft delete outcome to hold erased recovery data temporarily so accidental removal can be reversed remains open.
- **C — Incorrect.** First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.
  First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline. This test-VM protection and restore drill pair serves recovery-point selection. Test-VM protection and restore drill uses recovery-point selection for both steps; backup soft delete remains untouched in test-VM protection and restore drill, so its backup soft delete gate to hold erased recovery data temporarily so accidental removal can be reversed fails.
- **D — Correct.** First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.
  First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report. The test-VM protection and restore drill uses its backup soft delete mutation gate and backup soft delete verification gate before it can hold erased recovery data temporarily so accidental removal can be reversed.

**Objectives:** `MR-RECOVERY-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB24-CP04`).

**Microsoft Learn sources:**

- [Soft delete for Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-security-feature-cloud)

**Source reviewed:** 2026-08-31

## LAB24-Q50 — B

**Question:** The test-VM protection and restore drill runbook separates restore rehearsal mutation from validation while it must detect failed protection jobs and route them to operators. Which sequence proves it cleanly?

- **A — Incorrect.** First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.
  First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances. This test-VM protection and restore drill pair serves Backup vaults. Test-VM protection and restore drill proves Backup vaults, but backup monitoring and alerts lacks implementation in test-VM protection and restore drill and backup monitoring and alerts proof; the backup monitoring and alerts outcome to detect failed protection jobs and route them to operators remains open.
- **B — Correct.** First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
  The test-VM protection and restore drill gets a complete backup monitoring and alerts sequence here: first, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration. Read-back evidence follows the change.
- **C — Incorrect.** First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.
  First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline. This test-VM protection and restore drill pair serves recovery-point selection. Test-VM protection and restore drill closes recovery-point selection, not backup monitoring and alerts; without the backup monitoring and alerts workflow, it cannot detect failed protection jobs and route them to operators.
- **D — Incorrect.** First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
  First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session. This test-VM protection and restore drill pair serves file-level recovery. File-level recovery cannot replace backup monitoring and alerts in test-VM protection and restore drill. Use this backup monitoring and alerts pair instead: First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.

**Objectives:** `MR-RECOVERY-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB24-CP05`).

**Microsoft Learn sources:**

- [Monitor Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor)

**Source reviewed:** 2026-08-31
