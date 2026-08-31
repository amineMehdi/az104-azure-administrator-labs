# Lab 24 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB24-Q01 — Foundational

A restore rehearsal incident review of the test-VM protection and restore drill depends on the ability to store supported Azure VM protection metadata in the correct vault type. Which platform description is reliable?

- A. A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.
- B. An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date.
- C. A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery.
- D. Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.

## LAB24-Q02 — Foundational

A recovery administrator protecting and restoring a test VM is updating the restore rehearsal runbook. The requirement is to use the vault type designed for newer data-source protection workloads. Which statement describes Azure behavior correctly?

- A. A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained.
- B. A restore operation must select a successful recovery point compatible with the desired restore type.
- C. Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion.
- D. A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.

## LAB24-Q03 — Foundational

A restore rehearsal peer review asks how the test-VM protection and restore drill should handle this outcome: define how often recovery points are created and how long they remain. Which explanation is accurate?

- A. A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained.
- B. A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource.
- C. Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM.
- D. Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures.

## LAB24-Q04 — Foundational

For the test-VM protection and restore drill, the restore rehearsal plan must associate the intended protection schedule with the test workload. Which statement about restore rehearsal belongs in the test-VM protection and restore drill record?

- A. An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date.
- B. A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource.
- C. Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.
- D. A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery.

## LAB24-Q05 — Foundational

The restore rehearsal review compares four claims for the test-VM protection and restore drill requirement to create an extra recovery point before a risky maintenance window. Which claim is technically sound?

- A. A restore operation must select a successful recovery point compatible with the desired restore type.
- B. Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion.
- C. A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.
- D. An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date.

## LAB24-Q06 — Foundational

The restore rehearsal architecture note requires the test-VM protection and restore drill environment to select a recovery point that meets the required recovery time. Which statement defines the relevant restore rehearsal boundary?

- A. Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM.
- B. Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures.
- C. A restore operation must select a successful recovery point compatible with the desired restore type.
- D. A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained.

## LAB24-Q07 — Foundational

A new restore rehearsal operator must explain why the test-VM protection and restore drill can recover selected files without replacing the complete virtual machine. Which explanation is accurate?

- A. Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM.
- B. Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.
- C. A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery.
- D. A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource.

## LAB24-Q08 — Foundational

The test-VM protection and restore drill acceptance criteria require operators to choose between creating a restored machine and restoring disks for controlled assembly. Which service fact supports that requirement?

- A. Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion.
- B. A Backup vault is the newer management entity used by Azure Data Protection for supported datasource types.
- C. Azure VM restore can create a new VM, restore disks, or replace disks depending on workload and recovery requirements.
- D. An on-demand backup creates a recovery point outside the normal schedule and can use an allowed retention date.

## LAB24-Q09 — Foundational

A restore rehearsal reviewer challenges whether the test-VM protection and restore drill can hold erased recovery data temporarily so accidental removal can be reversed. Which response resolves the concern?

- A. Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures.
- B. A backup policy defines when recovery points are created and how long daily, weekly, monthly, or yearly points are retained.
- C. Backup soft delete retains deleted backup data for a recovery period and may require explicit handling before vault deletion.
- D. A restore operation must select a successful recovery point compatible with the desired restore type.

## LAB24-Q10 — Foundational

The test-VM protection and restore drill handoff omits the restore rehearsal rule needed to detect failed protection jobs and route them to operators. Which statement should the team add?

- A. A Recovery Services vault stores management data and recovery points for supported workloads such as Azure VM backup and Site Recovery.
- B. Backup Center, jobs, built-in alerts, Azure Monitor, and reports expose protection health and operational failures.
- C. A backup policy has no effect on a workload until a backup instance or protected item associates that policy with the datasource.
- D. Azure VM file recovery mounts or exposes a recovery point so selected files can be copied without restoring the entire VM.

## LAB24-Q11 — Foundational

The test-VM protection and restore drill plan must store supported Azure VM protection metadata in the correct vault type while limiting the mutation scope to restore rehearsal. Which action is appropriate?

- A. Create the vault in the approved region and resource group before protecting the VM.
- B. Configure frequency, time zone, and retention ranges from the recovery objectives.
- C. List recovery points and choose one captured before the simulated data loss.
- D. Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup.

## LAB24-Q12 — Foundational

A restore rehearsal ticket in the test-VM protection and restore drill says to use the vault type designed for newer data-source protection workloads. Which restore rehearsal action completes the test-VM protection and restore drill request with minimal change?

- A. Enable protection for the exact datasource using the approved policy ID.
- B. Use file recovery when only a small set of guest files must be recovered.
- C. Enable the required monitoring path and route actionable backup failures to an approved receiver.
- D. Choose a Backup vault only for a workload supported by its data-protection model.

## LAB24-Q13 — Foundational

The approach for the test-VM protection and restore drill is approved, but the restore rehearsal environment still cannot define how often recovery points are created and how long they remain. Which implementation step closes the gap?

- A. Configure frequency, time zone, and retention ranges from the recovery objectives.
- B. Trigger an on-demand backup before the destructive test and persist its job ID.
- C. Choose restore disks for controlled validation before deciding whether to replace production resources.
- D. Create the vault in the approved region and resource group before protecting the VM.

## LAB24-Q14 — Foundational

The recovery administrator protecting and restoring a test VM may change the test-VM protection and restore drill only to associate the intended protection schedule with the test workload. Which restore rehearsal action stays within that assignment?

- A. Enable protection for the exact datasource using the approved policy ID.
- B. List recovery points and choose one captured before the simulated data loss.
- C. Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup.
- D. Choose a Backup vault only for a workload supported by its data-protection model.

## LAB24-Q15 — Foundational

A restore rehearsal dry run shows no test-VM protection and restore drill command will create an extra recovery point before a risky maintenance window. Which action belongs before execution?

- A. Use file recovery when only a small set of guest files must be recovered.
- B. Enable the required monitoring path and route actionable backup failures to an approved receiver.
- C. Configure frequency, time zone, and retention ranges from the recovery objectives.
- D. Trigger an on-demand backup before the destructive test and persist its job ID.

## LAB24-Q16 — Applied

For the test-VM protection and restore drill, operators need to select a recovery point that meets the required recovery time. Which change realizes that requirement?

- A. List recovery points and choose one captured before the simulated data loss.
- B. Choose restore disks for controlled validation before deciding whether to replace production resources.
- C. Create the vault in the approved region and resource group before protecting the VM.
- D. Enable protection for the exact datasource using the approved policy ID.

## LAB24-Q17 — Applied

Operators must automate the test-VM protection and restore drill change needed to recover selected files without replacing the complete virtual machine. Which restore rehearsal operation belongs in the runbook?

- A. Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup.
- B. Choose a Backup vault only for a workload supported by its data-protection model.
- C. Trigger an on-demand backup before the destructive test and persist its job ID.
- D. Use file recovery when only a small set of guest files must be recovered.

## LAB24-Q18 — Applied

A test-VM protection and restore drill review finds restore rehearsal drift from the need to choose between creating a restored machine and restoring disks for controlled assembly. Which correction addresses that drift?

- A. Enable the required monitoring path and route actionable backup failures to an approved receiver.
- B. Configure frequency, time zone, and retention ranges from the recovery objectives.
- C. List recovery points and choose one captured before the simulated data loss.
- D. Choose restore disks for controlled validation before deciding whether to replace production resources.

## LAB24-Q19 — Applied

The test-VM protection and restore drill window permits only the restore rehearsal change needed to hold erased recovery data temporarily so accidental removal can be reversed. Which option respects the boundary?

- A. Create the vault in the approved region and resource group before protecting the VM.
- B. Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup.
- C. Enable protection for the exact datasource using the approved policy ID.
- D. Use file recovery when only a small set of guest files must be recovered.

## LAB24-Q20 — Applied

The restore rehearsal preflight has passed; the test-VM protection and restore drill must now detect failed protection jobs and route them to operators. Which operation should run?

- A. Enable the required monitoring path and route actionable backup failures to an approved receiver.
- B. Choose a Backup vault only for a workload supported by its data-protection model.
- C. Trigger an on-demand backup before the destructive test and persist its job ID.
- D. Choose restore disks for controlled validation before deciding whether to replace production resources.

## LAB24-Q21 — Applied

Before test-VM protection and restore drill cleanup, the restore rehearsal team must reconfirm it can store supported Azure VM protection metadata in the correct vault type. Which read-only inspection should run?

- A. Query the protected item and match policy ID, protection state, health, and datasource ID.
- B. Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
- C. Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
- D. Query vault type, location, provisioningState, storage model, and protected-item count.

## LAB24-Q22 — Applied

The test-VM protection and restore drill setup reports success after the restore rehearsal attempt to use the vault type designed for newer data-source protection workloads. Which restore rehearsal read-only observation proves the test-VM protection and restore drill outcome?

- A. Track the backup job to completion and list the resulting recovery point timestamp.
- B. Query the restore job output and resolve every created disk, template, or VM resource ID.
- C. Query vault type, location, provisioningState, storage model, and protected-item count.
- D. Query the vault's storage settings, identity, provisioning state, and backup instances.

## LAB24-Q23 — Applied

The restore rehearsal log says the test-VM protection and restore drill can now define how often recovery points are created and how long they remain. Which restore rehearsal state should the test-VM protection and restore drill acceptance test retain?

- A. Compare recovery-point time, type, consistency, and expiry with the incident timeline.
- B. Query soft-delete state and list soft-deleted backup items in the cleanup report.
- C. Read the policy schedule and retention rules and calculate the oldest expected recovery point.
- D. Query the vault's storage settings, identity, provisioning state, and backup instances.

## LAB24-Q24 — Applied

The test-VM protection and restore drill rejects restore rehearsal exit status as proof it can associate the intended protection schedule with the test workload. Which test-VM protection and restore drill result is valid evidence?

- A. Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
- B. Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
- C. Query the protected item and match policy ID, protection state, health, and datasource ID.
- D. Read the policy schedule and retention rules and calculate the oldest expected recovery point.

## LAB24-Q25 — Applied

The restore rehearsal validator needs one test-VM protection and restore drill query after the change to create an extra recovery point before a risky maintenance window. Which restore rehearsal property should the test-VM protection and restore drill validator inspect?

- A. Query the restore job output and resolve every created disk, template, or VM resource ID.
- B. Track the backup job to completion and list the resulting recovery point timestamp.
- C. Query vault type, location, provisioningState, storage model, and protected-item count.
- D. Query the protected item and match policy ID, protection state, health, and datasource ID.

## LAB24-Q26 — Applied

The recovery administrator protecting and restoring a test VM must confirm the test-VM protection and restore drill, without mutation, can select a recovery point that meets the required recovery time. Which restore rehearsal check qualifies?

- A. Compare recovery-point time, type, consistency, and expiry with the incident timeline.
- B. Query soft-delete state and list soft-deleted backup items in the cleanup report.
- C. Query the vault's storage settings, identity, provisioning state, and backup instances.
- D. Track the backup job to completion and list the resulting recovery point timestamp.

## LAB24-Q27 — Applied

The test-VM protection and restore drill configuration is complete; the restore rehearsal reviewers need evidence it can recover selected files without replacing the complete virtual machine. Which observation shows success?

- A. Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
- B. Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
- C. Read the policy schedule and retention rules and calculate the oldest expected recovery point.
- D. Compare recovery-point time, type, consistency, and expiry with the incident timeline.

## LAB24-Q28 — Applied

The restore rehearsal validation asks whether the test-VM protection and restore drill can choose between creating a restored machine and restoring disks for controlled assembly. Which observable state is strongest?

- A. Query vault type, location, provisioningState, storage model, and protected-item count.
- B. Query the protected item and match policy ID, protection state, health, and datasource ID.
- C. Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
- D. Query the restore job output and resolve every created disk, template, or VM resource ID.

## LAB24-Q29 — Applied

A test-VM protection and restore drill review must prove the restore rehearsal ability to hold erased recovery data temporarily so accidental removal can be reversed. Which check avoids an adjacent feature?

- A. Query soft-delete state and list soft-deleted backup items in the cleanup report.
- B. Query the vault's storage settings, identity, provisioning state, and backup instances.
- C. Track the backup job to completion and list the resulting recovery point timestamp.
- D. Query the restore job output and resolve every created disk, template, or VM resource ID.

## LAB24-Q30 — Applied

The test-VM protection and restore drill evidence bundle needs a restore rehearsal result showing it can detect failed protection jobs and route them to operators. Which result belongs in the checkpoint?

- A. Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
- B. Read the policy schedule and retention rules and calculate the oldest expected recovery point.
- C. Compare recovery-point time, type, consistency, and expiry with the incident timeline.
- D. Query soft-delete state and list soft-deleted backup items in the cleanup report.

## LAB24-Q31 — Applied

Other test-VM protection and restore drill components are healthy, but the restore rehearsal still cannot store supported Azure VM protection metadata in the correct vault type. Which state causes the isolated failure?

- A. The runbook attempts to configure classic Azure VM backup in an incompatible vault type.
- B. The selected recovery point was created after the unwanted change.
- C. The vault is in a region that cannot protect the selected VM with the required scenario.
- D. The backup failed, but no alert route covers the vault or datasource scope.

## LAB24-Q32 — Applied

During a restore rehearsal fault drill, the test-VM protection and restore drill does not use the vault type designed for newer data-source protection workloads. Which finding identifies the defect?

- A. Daily recovery points expire sooner than the required recovery window.
- B. The recovery session was left mounted after the files were copied.
- C. The runbook attempts to configure classic Azure VM backup in an incompatible vault type.
- D. The vault is in a region that cannot protect the selected VM with the required scenario.

## LAB24-Q33 — Applied

The test-VM protection and restore drill setup finishes, yet the restore rehearsal cannot define how often recovery points are created and how long they remain. Which misconfiguration explains the mismatch?

- A. Daily recovery points expire sooner than the required recovery window.
- B. The policy exists, but the VM has never been registered as a protected item.
- C. The runbook selects replace disks without first validating application recovery impact.
- D. The runbook attempts to configure classic Azure VM backup in an incompatible vault type.

## LAB24-Q34 — Applied

A restore rehearsal break/fix in the test-VM protection and restore drill fails when operators try to associate the intended protection schedule with the test workload. Which diagnosis fits?

- A. The lab starts its break/fix change before the backup job finishes.
- B. The policy exists, but the VM has never been registered as a protected item.
- C. Cleanup reports success while a soft-deleted protected item remains undocumented.
- D. Daily recovery points expire sooner than the required recovery window.

## LAB24-Q35 — Applied

The test-VM protection and restore drill troubleshooting scope is the restore rehearsal need to create an extra recovery point before a risky maintenance window. Which condition should be corrected first?

- A. The selected recovery point was created after the unwanted change.
- B. The backup failed, but no alert route covers the vault or datasource scope.
- C. The lab starts its break/fix change before the backup job finishes.
- D. The policy exists, but the VM has never been registered as a protected item.

## LAB24-Q36 — Applied

The test-VM protection and restore drill result is partial because the restore rehearsal cannot select a recovery point that meets the required recovery time. Which condition accounts for that result?

- A. The recovery session was left mounted after the files were copied.
- B. The vault is in a region that cannot protect the selected VM with the required scenario.
- C. The selected recovery point was created after the unwanted change.
- D. The lab starts its break/fix change before the backup job finishes.

## LAB24-Q37 — Applied

The restore rehearsal evidence shows the test-VM protection and restore drill cannot recover selected files without replacing the complete virtual machine. Which root cause fits that evidence?

- A. The runbook selects replace disks without first validating application recovery impact.
- B. The recovery session was left mounted after the files were copied.
- C. The runbook attempts to configure classic Azure VM backup in an incompatible vault type.
- D. The selected recovery point was created after the unwanted change.

## LAB24-Q38 — Applied

Although the test-VM protection and restore drill is meant to let the restore rehearsal choose between creating a restored machine and restoring disks for controlled assembly, its checkpoint fails. Which restore rehearsal defect explains the failure?

- A. Cleanup reports success while a soft-deleted protected item remains undocumented.
- B. Daily recovery points expire sooner than the required recovery window.
- C. The recovery session was left mounted after the files were copied.
- D. The runbook selects replace disks without first validating application recovery impact.

## LAB24-Q39 — Applied

The restore rehearsal support team isolated the test-VM protection and restore drill incident to the attempt to hold erased recovery data temporarily so accidental removal can be reversed. Which condition prevents success?

- A. The backup failed, but no alert route covers the vault or datasource scope.
- B. Cleanup reports success while a soft-deleted protected item remains undocumented.
- C. The policy exists, but the VM has never been registered as a protected item.
- D. The runbook selects replace disks without first validating application recovery impact.

## LAB24-Q40 — Applied

A test-VM protection and restore drill query surprises the recovery administrator protecting and restoring a test VM during the restore rehearsal attempt to detect failed protection jobs and route them to operators. Which finding explains it?

- A. The vault is in a region that cannot protect the selected VM with the required scenario.
- B. The lab starts its break/fix change before the backup job finishes.
- C. The backup failed, but no alert route covers the vault or datasource scope.
- D. Cleanup reports success while a soft-deleted protected item remains undocumented.

## LAB24-Q41 — Advanced

The test-VM protection and restore drill checkpoint requires both this restore rehearsal outcome—store supported Azure VM protection metadata in the correct vault type—and a read-only test-VM protection and restore drill state check. Which restore rehearsal response is complete?

- A. First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.
- B. First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.
- C. First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
- D. First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID.

## LAB24-Q42 — Advanced

The test-VM protection and restore drill runbook must use the vault type designed for newer data-source protection workloads, then retain restore rehearsal read-back evidence. Which test-VM protection and restore drill pair completes both duties?

- A. First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.
- B. First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.
- C. First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID.
- D. First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.

## LAB24-Q43 — Advanced

To satisfy the restore rehearsal requirement, operators must change the test-VM protection and restore drill configuration and prove it can define how often recovery points are created and how long they remain. Which sequence is coherent?

- A. First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.
- B. First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.
- C. First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.
- D. First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.

## LAB24-Q44 — Advanced

The recovery administrator protecting and restoring a test VM needs a safe test-VM protection and restore drill change to associate the intended protection schedule with the test workload, followed by restore rehearsal evidence. Which pair merits approval?

- A. First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.
- B. First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
- C. First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.
- D. First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.

## LAB24-Q45 — Advanced

The test-VM protection and restore drill has two restore rehearsal gates: create an extra recovery point before a risky maintenance window, then prove the test-VM protection and restore drill state. Which restore rehearsal sequence works?

- A. First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
- B. First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.
- C. First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.
- D. First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.

## LAB24-Q46 — Advanced

Which restore rehearsal path makes the test-VM protection and restore drill able to select a recovery point that meets the required recovery time, then inspects the defining properties?

- A. First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.
- B. First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID.
- C. First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.
- D. First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.

## LAB24-Q47 — Advanced

At the test-VM protection and restore drill approval gate, operators must show that the restore rehearsal can recover selected files without replacing the complete virtual machine. Which restore rehearsal configure-and-check pair is defensible?

- A. First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.
- B. First, Configure frequency, time zone, and retention ranges from the recovery objectives. Then, Read the policy schedule and retention rules and calculate the oldest expected recovery point.
- C. First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.
- D. First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.

## LAB24-Q48 — Advanced

The test-VM protection and restore drill forbids a partial restore rehearsal result. Operators must first choose between creating a restored machine and restoring disks for controlled assembly and afterward confirm the test-VM protection and restore drill outcome. Which restore rehearsal sequence is complete?

- A. First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
- B. First, Choose restore disks for controlled validation before deciding whether to replace production resources. Then, Query the restore job output and resolve every created disk, template, or VM resource ID.
- C. First, Enable protection for the exact datasource using the approved policy ID. Then, Query the protected item and match policy ID, protection state, health, and datasource ID.
- D. First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.

## LAB24-Q49 — Advanced

Only the test-VM protection and restore drill change needed to hold erased recovery data temporarily so accidental removal can be reversed is allowed, and restore rehearsal proof is mandatory. Which pair fits?

- A. First, Create the vault in the approved region and resource group before protecting the VM. Then, Query vault type, location, provisioningState, storage model, and protected-item count.
- B. First, Trigger an on-demand backup before the destructive test and persist its job ID. Then, Track the backup job to completion and list the resulting recovery point timestamp.
- C. First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.
- D. First, Keep soft delete enabled and document retained items rather than attempting irreversible purge in routine cleanup. Then, Query soft-delete state and list soft-deleted backup items in the cleanup report.

## LAB24-Q50 — Advanced

The test-VM protection and restore drill runbook separates restore rehearsal mutation from validation while it must detect failed protection jobs and route them to operators. Which sequence proves it cleanly?

- A. First, Choose a Backup vault only for a workload supported by its data-protection model. Then, Query the vault's storage settings, identity, provisioning state, and backup instances.
- B. First, Enable the required monitoring path and route actionable backup failures to an approved receiver. Then, Query failed jobs, protection health, alert state, and diagnostic or reporting configuration.
- C. First, List recovery points and choose one captured before the simulated data loss. Then, Compare recovery-point time, type, consistency, and expiry with the incident timeline.
- D. First, Use file recovery when only a small set of guest files must be recovered. Then, Verify the selected recovery point is mounted, copy the target file, and unmount the recovery session.

[Open the answer key](./ANSWERS.md)
