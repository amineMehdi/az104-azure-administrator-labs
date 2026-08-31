# Lab 25 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB25-Q01 — Foundational

For the Azure-to-Azure disaster-recovery pilot, the failover pilot plan must replicate supported virtual-machine disks from one region to recovery resources in another. Which statement about failover pilot belongs in the Azure-to-Azure disaster-recovery pilot record?

- A. The Recovery Services vault for Azure-to-Azure replication is placed outside the source VM's failure region according to scenario guidance.
- B. Recovery settings map protected machines to target virtual networks, subnets, and optional target IP configuration.
- C. A planned failover coordinates shutdown and final synchronization when the source is available to minimize data loss.
- D. Azure-to-Azure Site Recovery replicates supported VM disks from a source region into configured target-region resources.

## LAB25-Q02 — Foundational

The failover pilot review compares four claims for the Azure-to-Azure disaster-recovery pilot requirement to place recovery orchestration outside the failure boundary it must survive. Which claim is technically sound?

- A. A Site Recovery replication policy defines settings such as recovery-point retention and app-consistent snapshot frequency.
- B. The Recovery Services vault for Azure-to-Azure replication is placed outside the source VM's failure region according to scenario guidance.
- C. A protected item must complete initial replication and reach a healthy protected state before it can meet recovery expectations.
- D. An unplanned failover recovers from an unavailable source using a selected available recovery point and may have data loss.

## LAB25-Q03 — Foundational

The failover pilot architecture note requires the Azure-to-Azure disaster-recovery pilot environment to configure retention plus the cadence for application-aware recovery points. Which statement defines the relevant failover pilot boundary?

- A. Azure-to-Azure replication uses a supported cache storage account in the source region for outgoing replication data.
- B. A Site Recovery replication policy defines settings such as recovery-point retention and app-consistent snapshot frequency.
- C. A test failover validates recovery without changing production replication and should use an isolated recovery network.
- D. Commit finalizes the selected recovery point; reprotect reverses replication direction before a later failback.

## LAB25-Q04 — Foundational

A new failover pilot operator must explain why the Azure-to-Azure disaster-recovery pilot can buffer replication changes in a supported source-region storage account. Which explanation is accurate?

- A. Recovery settings map protected machines to target virtual networks, subnets, and optional target IP configuration.
- B. A planned failover coordinates shutdown and final synchronization when the source is available to minimize data loss.
- C. Azure-to-Azure Site Recovery replicates supported VM disks from a source region into configured target-region resources.
- D. Azure-to-Azure replication uses a supported cache storage account in the source region for outgoing replication data.

## LAB25-Q05 — Foundational

The Azure-to-Azure disaster-recovery pilot acceptance criteria require operators to connect recovered machines to the intended target network and subnet. Which service fact supports that requirement?

- A. Recovery settings map protected machines to target virtual networks, subnets, and optional target IP configuration.
- B. A protected item must complete initial replication and reach a healthy protected state before it can meet recovery expectations.
- C. An unplanned failover recovers from an unavailable source using a selected available recovery point and may have data loss.
- D. The Recovery Services vault for Azure-to-Azure replication is placed outside the source VM's failure region according to scenario guidance.

## LAB25-Q06 — Foundational

A failover pilot reviewer challenges whether the Azure-to-Azure disaster-recovery pilot can wait until initial synchronization completes and protection reports normal. Which response resolves the concern?

- A. A protected item must complete initial replication and reach a healthy protected state before it can meet recovery expectations.
- B. A test failover validates recovery without changing production replication and should use an isolated recovery network.
- C. Commit finalizes the selected recovery point; reprotect reverses replication direction before a later failback.
- D. A Site Recovery replication policy defines settings such as recovery-point retention and app-consistent snapshot frequency.

## LAB25-Q07 — Foundational

The Azure-to-Azure disaster-recovery pilot handoff omits the failover pilot rule needed to exercise recovery on an isolated network without disrupting production replication. Which statement should the team add?

- A. A planned failover coordinates shutdown and final synchronization when the source is available to minimize data loss.
- B. A test failover validates recovery without changing production replication and should use an isolated recovery network.
- C. Azure-to-Azure Site Recovery replicates supported VM disks from a source region into configured target-region resources.
- D. Azure-to-Azure replication uses a supported cache storage account in the source region for outgoing replication data.

## LAB25-Q08 — Foundational

A failover pilot incident review of the Azure-to-Azure disaster-recovery pilot depends on the ability to shut down the source and capture its latest changes for low-loss recovery. Which platform description is reliable?

- A. A planned failover coordinates shutdown and final synchronization when the source is available to minimize data loss.
- B. An unplanned failover recovers from an unavailable source using a selected available recovery point and may have data loss.
- C. The Recovery Services vault for Azure-to-Azure replication is placed outside the source VM's failure region according to scenario guidance.
- D. Recovery settings map protected machines to target virtual networks, subnets, and optional target IP configuration.

## LAB25-Q09 — Foundational

A disaster-recovery administrator piloting Azure-to-Azure replication is updating the failover pilot runbook. The requirement is to start outage recovery from the most appropriate stored point. Which statement describes Azure behavior correctly?

- A. Commit finalizes the selected recovery point; reprotect reverses replication direction before a later failback.
- B. A Site Recovery replication policy defines settings such as recovery-point retention and app-consistent snapshot frequency.
- C. A protected item must complete initial replication and reach a healthy protected state before it can meet recovery expectations.
- D. An unplanned failover recovers from an unavailable source using a selected available recovery point and may have data loss.

## LAB25-Q10 — Foundational

A failover pilot peer review asks how the Azure-to-Azure disaster-recovery pilot should handle this outcome: finalize recovery, reverse protection direction, and return service to the original region. Which explanation is accurate?

- A. Azure-to-Azure Site Recovery replicates supported VM disks from a source region into configured target-region resources.
- B. Azure-to-Azure replication uses a supported cache storage account in the source region for outgoing replication data.
- C. A test failover validates recovery without changing production replication and should use an isolated recovery network.
- D. Commit finalizes the selected recovery point; reprotect reverses replication direction before a later failback.

## LAB25-Q11 — Foundational

The disaster-recovery administrator piloting Azure-to-Azure replication may change the Azure-to-Azure disaster-recovery pilot only to replicate supported virtual-machine disks from one region to recovery resources in another. Which failover pilot action stays within that assignment?

- A. Choose a supported target region and validate VM, disk, network, quota, and feature compatibility.
- B. Create or select a policy whose recovery-point objectives match the application requirements.
- C. Monitor initial replication and resolve warnings or errors before scheduling the drill.
- D. Choose the most suitable recovery point, start failover, and validate the application before commit.

## LAB25-Q12 — Foundational

A failover pilot dry run shows no Azure-to-Azure disaster-recovery pilot command will place recovery orchestration outside the failure boundary it must survive. Which action belongs before execution?

- A. Select a compatible cache account in the source region and avoid unsupported firewall or performance constraints.
- B. Start test failover to an isolated target VNet and validate the recovered application before cleanup.
- C. Validate recovery, commit deliberately, reprotect to the original region, and plan failback as a separate controlled change.
- D. Create or select the vault in the approved recovery region before enabling replication.

## LAB25-Q13 — Foundational

For the Azure-to-Azure disaster-recovery pilot, operators need to configure retention plus the cadence for application-aware recovery points. Which change realizes that requirement?

- A. Prepare nonoverlapping target networking and map every protected NIC before failover.
- B. Use planned failover for an intentional migration or outage when source coordination is possible.
- C. Choose a supported target region and validate VM, disk, network, quota, and feature compatibility.
- D. Create or select a policy whose recovery-point objectives match the application requirements.

## LAB25-Q14 — Foundational

Operators must automate the Azure-to-Azure disaster-recovery pilot change needed to buffer replication changes in a supported source-region storage account. Which failover pilot operation belongs in the runbook?

- A. Monitor initial replication and resolve warnings or errors before scheduling the drill.
- B. Select a compatible cache account in the source region and avoid unsupported firewall or performance constraints.
- C. Choose the most suitable recovery point, start failover, and validate the application before commit.
- D. Create or select the vault in the approved recovery region before enabling replication.

## LAB25-Q15 — Foundational

An Azure-to-Azure disaster-recovery pilot review finds failover pilot drift from the need to connect recovered machines to the intended target network and subnet. Which correction addresses that drift?

- A. Start test failover to an isolated target VNet and validate the recovered application before cleanup.
- B. Prepare nonoverlapping target networking and map every protected NIC before failover.
- C. Validate recovery, commit deliberately, reprotect to the original region, and plan failback as a separate controlled change.
- D. Create or select a policy whose recovery-point objectives match the application requirements.

## LAB25-Q16 — Applied

The Azure-to-Azure disaster-recovery pilot window permits only the failover pilot change needed to wait until initial synchronization completes and protection reports normal. Which option respects the boundary?

- A. Use planned failover for an intentional migration or outage when source coordination is possible.
- B. Monitor initial replication and resolve warnings or errors before scheduling the drill.
- C. Choose a supported target region and validate VM, disk, network, quota, and feature compatibility.
- D. Select a compatible cache account in the source region and avoid unsupported firewall or performance constraints.

## LAB25-Q17 — Applied

The failover pilot preflight has passed; the Azure-to-Azure disaster-recovery pilot must now exercise recovery on an isolated network without disrupting production replication. Which operation should run?

- A. Choose the most suitable recovery point, start failover, and validate the application before commit.
- B. Create or select the vault in the approved recovery region before enabling replication.
- C. Prepare nonoverlapping target networking and map every protected NIC before failover.
- D. Start test failover to an isolated target VNet and validate the recovered application before cleanup.

## LAB25-Q18 — Applied

The Azure-to-Azure disaster-recovery pilot plan must shut down the source and capture its latest changes for low-loss recovery while limiting the mutation scope to failover pilot. Which action is appropriate?

- A. Validate recovery, commit deliberately, reprotect to the original region, and plan failback as a separate controlled change.
- B. Create or select a policy whose recovery-point objectives match the application requirements.
- C. Use planned failover for an intentional migration or outage when source coordination is possible.
- D. Monitor initial replication and resolve warnings or errors before scheduling the drill.

## LAB25-Q19 — Applied

A failover pilot ticket in the Azure-to-Azure disaster-recovery pilot says to start outage recovery from the most appropriate stored point. Which failover pilot action completes the Azure-to-Azure disaster-recovery pilot request with minimal change?

- A. Choose a supported target region and validate VM, disk, network, quota, and feature compatibility.
- B. Choose the most suitable recovery point, start failover, and validate the application before commit.
- C. Select a compatible cache account in the source region and avoid unsupported firewall or performance constraints.
- D. Start test failover to an isolated target VNet and validate the recovered application before cleanup.

## LAB25-Q20 — Applied

The approach for the Azure-to-Azure disaster-recovery pilot is approved, but the failover pilot environment still cannot finalize recovery, reverse protection direction, and return service to the original region. Which implementation step closes the gap?

- A. Validate recovery, commit deliberately, reprotect to the original region, and plan failback as a separate controlled change.
- B. Create or select the vault in the approved recovery region before enabling replication.
- C. Prepare nonoverlapping target networking and map every protected NIC before failover.
- D. Use planned failover for an intentional migration or outage when source coordination is possible.

## LAB25-Q21 — Applied

The Azure-to-Azure disaster-recovery pilot rejects failover pilot exit status as proof it can replicate supported virtual-machine disks from one region to recovery resources in another. Which Azure-to-Azure disaster-recovery pilot result is valid evidence?

- A. Query the protected disk's cache storage account ID and confirm region, kind, and network reachability.
- B. Track the test-failover job, recovered VM network, application checks, and cleanup job.
- C. Query activeLocation, allowedOperations, protectionState, and reverse-replication health after each phase.
- D. Query the protected item's source and target fabric, region, and replication health.

## LAB25-Q22 — Applied

The failover pilot validator needs one Azure-to-Azure disaster-recovery pilot query after the change to place recovery orchestration outside the failure boundary it must survive. Which failover pilot property should the Azure-to-Azure disaster-recovery pilot validator inspect?

- A. Query target network and subnet IDs for each replicated NIC and validate DNS and security dependencies.
- B. Query vault location and confirm it differs from the protected workload's source region.
- C. Track shutdown, synchronization, failover job completion, active location, and recovery point.
- D. Query the protected item's source and target fabric, region, and replication health.

## LAB25-Q23 — Applied

The disaster-recovery administrator piloting Azure-to-Azure replication must confirm the Azure-to-Azure disaster-recovery pilot, without mutation, can configure retention plus the cadence for application-aware recovery points. Which failover pilot check qualifies?

- A. Query protectionState, replicationHealth, activeLocation, and latest recovery points.
- B. Query recoveryPointRetentionInHours and appConsistentFrequencyInHours on the active policy.
- C. Query recovery-point type, job state, active location, and target VM health.
- D. Query vault location and confirm it differs from the protected workload's source region.

## LAB25-Q24 — Applied

The Azure-to-Azure disaster-recovery pilot configuration is complete; the failover pilot reviewers need evidence it can buffer replication changes in a supported source-region storage account. Which observation shows success?

- A. Track the test-failover job, recovered VM network, application checks, and cleanup job.
- B. Query activeLocation, allowedOperations, protectionState, and reverse-replication health after each phase.
- C. Query the protected disk's cache storage account ID and confirm region, kind, and network reachability.
- D. Query recoveryPointRetentionInHours and appConsistentFrequencyInHours on the active policy.

## LAB25-Q25 — Applied

The failover pilot validation asks whether the Azure-to-Azure disaster-recovery pilot can connect recovered machines to the intended target network and subnet. Which observable state is strongest?

- A. Track shutdown, synchronization, failover job completion, active location, and recovery point.
- B. Query the protected item's source and target fabric, region, and replication health.
- C. Query target network and subnet IDs for each replicated NIC and validate DNS and security dependencies.
- D. Query the protected disk's cache storage account ID and confirm region, kind, and network reachability.

## LAB25-Q26 — Applied

An Azure-to-Azure disaster-recovery pilot review must prove the failover pilot ability to wait until initial synchronization completes and protection reports normal. Which check avoids an adjacent feature?

- A. Query recovery-point type, job state, active location, and target VM health.
- B. Query protectionState, replicationHealth, activeLocation, and latest recovery points.
- C. Query vault location and confirm it differs from the protected workload's source region.
- D. Query target network and subnet IDs for each replicated NIC and validate DNS and security dependencies.

## LAB25-Q27 — Applied

The Azure-to-Azure disaster-recovery pilot evidence bundle needs a failover pilot result showing it can exercise recovery on an isolated network without disrupting production replication. Which result belongs in the checkpoint?

- A. Query activeLocation, allowedOperations, protectionState, and reverse-replication health after each phase.
- B. Query recoveryPointRetentionInHours and appConsistentFrequencyInHours on the active policy.
- C. Query protectionState, replicationHealth, activeLocation, and latest recovery points.
- D. Track the test-failover job, recovered VM network, application checks, and cleanup job.

## LAB25-Q28 — Applied

Before Azure-to-Azure disaster-recovery pilot cleanup, the failover pilot team must reconfirm it can shut down the source and capture its latest changes for low-loss recovery. Which read-only inspection should run?

- A. Track shutdown, synchronization, failover job completion, active location, and recovery point.
- B. Query the protected item's source and target fabric, region, and replication health.
- C. Query the protected disk's cache storage account ID and confirm region, kind, and network reachability.
- D. Track the test-failover job, recovered VM network, application checks, and cleanup job.

## LAB25-Q29 — Applied

The Azure-to-Azure disaster-recovery pilot setup reports success after the failover pilot attempt to start outage recovery from the most appropriate stored point. Which failover pilot read-only observation proves the Azure-to-Azure disaster-recovery pilot outcome?

- A. Query vault location and confirm it differs from the protected workload's source region.
- B. Query recovery-point type, job state, active location, and target VM health.
- C. Query target network and subnet IDs for each replicated NIC and validate DNS and security dependencies.
- D. Track shutdown, synchronization, failover job completion, active location, and recovery point.

## LAB25-Q30 — Applied

The failover pilot log says the Azure-to-Azure disaster-recovery pilot can now finalize recovery, reverse protection direction, and return service to the original region. Which failover pilot state should the Azure-to-Azure disaster-recovery pilot acceptance test retain?

- A. Query recoveryPointRetentionInHours and appConsistentFrequencyInHours on the active policy.
- B. Query protectionState, replicationHealth, activeLocation, and latest recovery points.
- C. Query activeLocation, allowedOperations, protectionState, and reverse-replication health after each phase.
- D. Query recovery-point type, job state, active location, and target VM health.

## LAB25-Q31 — Applied

A failover pilot break/fix in the Azure-to-Azure disaster-recovery pilot fails when operators try to replicate supported virtual-machine disks from one region to recovery resources in another. Which diagnosis fits?

- A. The vault was created in the same region as the source VM it must orchestrate during regional recovery.
- B. The target region does not support one of the source VM's required features.
- C. Initial replication is still in progress when the test failover is started.
- D. The failover was committed before application owners validated the recovered workload.

## LAB25-Q32 — Applied

The Azure-to-Azure disaster-recovery pilot troubleshooting scope is the failover pilot need to place recovery orchestration outside the failure boundary it must survive. Which condition should be corrected first?

- A. The application requires app-consistent points more frequently than the policy creates them.
- B. The test VM connects to the production target network and creates duplicate service identities.
- C. The vault was created in the same region as the source VM it must orchestrate during regional recovery.
- D. The target region does not support one of the source VM's required features.

## LAB25-Q33 — Applied

The Azure-to-Azure disaster-recovery pilot result is partial because the failover pilot cannot configure retention plus the cadence for application-aware recovery points. Which condition accounts for that result?

- A. The application requires app-consistent points more frequently than the policy creates them.
- B. The chosen cache storage account is in the target region instead of the source region.
- C. The source VM cannot be reached, so final planned synchronization cannot complete.
- D. The vault was created in the same region as the source VM it must orchestrate during regional recovery.

## LAB25-Q34 — Applied

The failover pilot evidence shows the Azure-to-Azure disaster-recovery pilot cannot buffer replication changes in a supported source-region storage account. Which root cause fits that evidence?

- A. The chosen cache storage account is in the target region instead of the source region.
- B. The mapped target subnet does not exist in the recovery virtual network.
- C. The latest processed recovery point does not meet the application's consistency requirement.
- D. The application requires app-consistent points more frequently than the policy creates them.

## LAB25-Q35 — Applied

Although the Azure-to-Azure disaster-recovery pilot is meant to let the failover pilot connect recovered machines to the intended target network and subnet, its checkpoint fails. Which failover pilot defect explains the failure?

- A. Initial replication is still in progress when the test failover is started.
- B. The failover was committed before application owners validated the recovered workload.
- C. The chosen cache storage account is in the target region instead of the source region.
- D. The mapped target subnet does not exist in the recovery virtual network.

## LAB25-Q36 — Applied

The failover pilot support team isolated the Azure-to-Azure disaster-recovery pilot incident to the attempt to wait until initial synchronization completes and protection reports normal. Which condition prevents success?

- A. The test VM connects to the production target network and creates duplicate service identities.
- B. The target region does not support one of the source VM's required features.
- C. The mapped target subnet does not exist in the recovery virtual network.
- D. Initial replication is still in progress when the test failover is started.

## LAB25-Q37 — Applied

An Azure-to-Azure disaster-recovery pilot query surprises the disaster-recovery administrator piloting Azure-to-Azure replication during the failover pilot attempt to exercise recovery on an isolated network without disrupting production replication. Which finding explains it?

- A. The test VM connects to the production target network and creates duplicate service identities.
- B. The source VM cannot be reached, so final planned synchronization cannot complete.
- C. The vault was created in the same region as the source VM it must orchestrate during regional recovery.
- D. Initial replication is still in progress when the test failover is started.

## LAB25-Q38 — Applied

Other Azure-to-Azure disaster-recovery pilot components are healthy, but the failover pilot still cannot shut down the source and capture its latest changes for low-loss recovery. Which state causes the isolated failure?

- A. The latest processed recovery point does not meet the application's consistency requirement.
- B. The application requires app-consistent points more frequently than the policy creates them.
- C. The source VM cannot be reached, so final planned synchronization cannot complete.
- D. The test VM connects to the production target network and creates duplicate service identities.

## LAB25-Q39 — Applied

During a failover pilot fault drill, the Azure-to-Azure disaster-recovery pilot does not start outage recovery from the most appropriate stored point. Which finding identifies the defect?

- A. The failover was committed before application owners validated the recovered workload.
- B. The chosen cache storage account is in the target region instead of the source region.
- C. The latest processed recovery point does not meet the application's consistency requirement.
- D. The source VM cannot be reached, so final planned synchronization cannot complete.

## LAB25-Q40 — Applied

The Azure-to-Azure disaster-recovery pilot setup finishes, yet the failover pilot cannot finalize recovery, reverse protection direction, and return service to the original region. Which misconfiguration explains the mismatch?

- A. The failover was committed before application owners validated the recovered workload.
- B. The target region does not support one of the source VM's required features.
- C. The mapped target subnet does not exist in the recovery virtual network.
- D. The latest processed recovery point does not meet the application's consistency requirement.

## LAB25-Q41 — Advanced

The disaster-recovery administrator piloting Azure-to-Azure replication needs a safe Azure-to-Azure disaster-recovery pilot change to replicate supported virtual-machine disks from one region to recovery resources in another, followed by failover pilot evidence. Which pair merits approval?

- A. First, Create or select a policy whose recovery-point objectives match the application requirements. Then, Query recoveryPointRetentionInHours and appConsistentFrequencyInHours on the active policy.
- B. First, Start test failover to an isolated target VNet and validate the recovered application before cleanup. Then, Track the test-failover job, recovered VM network, application checks, and cleanup job.
- C. First, Choose a supported target region and validate VM, disk, network, quota, and feature compatibility. Then, Query the protected item's source and target fabric, region, and replication health.
- D. First, Use planned failover for an intentional migration or outage when source coordination is possible. Then, Track shutdown, synchronization, failover job completion, active location, and recovery point.

## LAB25-Q42 — Advanced

The Azure-to-Azure disaster-recovery pilot has two failover pilot gates: place recovery orchestration outside the failure boundary it must survive, then prove the Azure-to-Azure disaster-recovery pilot state. Which failover pilot sequence works?

- A. First, Select a compatible cache account in the source region and avoid unsupported firewall or performance constraints. Then, Query the protected disk's cache storage account ID and confirm region, kind, and network reachability.
- B. First, Use planned failover for an intentional migration or outage when source coordination is possible. Then, Track shutdown, synchronization, failover job completion, active location, and recovery point.
- C. First, Create or select the vault in the approved recovery region before enabling replication. Then, Query vault location and confirm it differs from the protected workload's source region.
- D. First, Choose the most suitable recovery point, start failover, and validate the application before commit. Then, Query recovery-point type, job state, active location, and target VM health.

## LAB25-Q43 — Advanced

Which failover pilot path makes the Azure-to-Azure disaster-recovery pilot able to configure retention plus the cadence for application-aware recovery points, then inspects the defining properties?

- A. First, Prepare nonoverlapping target networking and map every protected NIC before failover. Then, Query target network and subnet IDs for each replicated NIC and validate DNS and security dependencies.
- B. First, Choose the most suitable recovery point, start failover, and validate the application before commit. Then, Query recovery-point type, job state, active location, and target VM health.
- C. First, Create or select a policy whose recovery-point objectives match the application requirements. Then, Query recoveryPointRetentionInHours and appConsistentFrequencyInHours on the active policy.
- D. First, Validate recovery, commit deliberately, reprotect to the original region, and plan failback as a separate controlled change. Then, Query activeLocation, allowedOperations, protectionState, and reverse-replication health after each phase.

## LAB25-Q44 — Advanced

At the Azure-to-Azure disaster-recovery pilot approval gate, operators must show that the failover pilot can buffer replication changes in a supported source-region storage account. Which failover pilot configure-and-check pair is defensible?

- A. First, Select a compatible cache account in the source region and avoid unsupported firewall or performance constraints. Then, Query the protected disk's cache storage account ID and confirm region, kind, and network reachability.
- B. First, Monitor initial replication and resolve warnings or errors before scheduling the drill. Then, Query protectionState, replicationHealth, activeLocation, and latest recovery points.
- C. First, Validate recovery, commit deliberately, reprotect to the original region, and plan failback as a separate controlled change. Then, Query activeLocation, allowedOperations, protectionState, and reverse-replication health after each phase.
- D. First, Choose a supported target region and validate VM, disk, network, quota, and feature compatibility. Then, Query the protected item's source and target fabric, region, and replication health.

## LAB25-Q45 — Advanced

The Azure-to-Azure disaster-recovery pilot forbids a partial failover pilot result. Operators must first connect recovered machines to the intended target network and subnet and afterward confirm the Azure-to-Azure disaster-recovery pilot outcome. Which failover pilot sequence is complete?

- A. First, Start test failover to an isolated target VNet and validate the recovered application before cleanup. Then, Track the test-failover job, recovered VM network, application checks, and cleanup job.
- B. First, Choose a supported target region and validate VM, disk, network, quota, and feature compatibility. Then, Query the protected item's source and target fabric, region, and replication health.
- C. First, Prepare nonoverlapping target networking and map every protected NIC before failover. Then, Query target network and subnet IDs for each replicated NIC and validate DNS and security dependencies.
- D. First, Create or select the vault in the approved recovery region before enabling replication. Then, Query vault location and confirm it differs from the protected workload's source region.

## LAB25-Q46 — Advanced

Only the Azure-to-Azure disaster-recovery pilot change needed to wait until initial synchronization completes and protection reports normal is allowed, and failover pilot proof is mandatory. Which pair fits?

- A. First, Use planned failover for an intentional migration or outage when source coordination is possible. Then, Track shutdown, synchronization, failover job completion, active location, and recovery point.
- B. First, Create or select the vault in the approved recovery region before enabling replication. Then, Query vault location and confirm it differs from the protected workload's source region.
- C. First, Monitor initial replication and resolve warnings or errors before scheduling the drill. Then, Query protectionState, replicationHealth, activeLocation, and latest recovery points.
- D. First, Create or select a policy whose recovery-point objectives match the application requirements. Then, Query recoveryPointRetentionInHours and appConsistentFrequencyInHours on the active policy.

## LAB25-Q47 — Advanced

The Azure-to-Azure disaster-recovery pilot runbook separates failover pilot mutation from validation while it must exercise recovery on an isolated network without disrupting production replication. Which sequence proves it cleanly?

- A. First, Choose the most suitable recovery point, start failover, and validate the application before commit. Then, Query recovery-point type, job state, active location, and target VM health.
- B. First, Create or select a policy whose recovery-point objectives match the application requirements. Then, Query recoveryPointRetentionInHours and appConsistentFrequencyInHours on the active policy.
- C. First, Select a compatible cache account in the source region and avoid unsupported firewall or performance constraints. Then, Query the protected disk's cache storage account ID and confirm region, kind, and network reachability.
- D. First, Start test failover to an isolated target VNet and validate the recovered application before cleanup. Then, Track the test-failover job, recovered VM network, application checks, and cleanup job.

## LAB25-Q48 — Advanced

The Azure-to-Azure disaster-recovery pilot checkpoint requires both this failover pilot outcome—shut down the source and capture its latest changes for low-loss recovery—and a read-only Azure-to-Azure disaster-recovery pilot state check. Which failover pilot response is complete?

- A. First, Use planned failover for an intentional migration or outage when source coordination is possible. Then, Track shutdown, synchronization, failover job completion, active location, and recovery point.
- B. First, Validate recovery, commit deliberately, reprotect to the original region, and plan failback as a separate controlled change. Then, Query activeLocation, allowedOperations, protectionState, and reverse-replication health after each phase.
- C. First, Select a compatible cache account in the source region and avoid unsupported firewall or performance constraints. Then, Query the protected disk's cache storage account ID and confirm region, kind, and network reachability.
- D. First, Prepare nonoverlapping target networking and map every protected NIC before failover. Then, Query target network and subnet IDs for each replicated NIC and validate DNS and security dependencies.

## LAB25-Q49 — Advanced

The Azure-to-Azure disaster-recovery pilot runbook must start outage recovery from the most appropriate stored point, then retain failover pilot read-back evidence. Which Azure-to-Azure disaster-recovery pilot pair completes both duties?

- A. First, Choose a supported target region and validate VM, disk, network, quota, and feature compatibility. Then, Query the protected item's source and target fabric, region, and replication health.
- B. First, Choose the most suitable recovery point, start failover, and validate the application before commit. Then, Query recovery-point type, job state, active location, and target VM health.
- C. First, Prepare nonoverlapping target networking and map every protected NIC before failover. Then, Query target network and subnet IDs for each replicated NIC and validate DNS and security dependencies.
- D. First, Monitor initial replication and resolve warnings or errors before scheduling the drill. Then, Query protectionState, replicationHealth, activeLocation, and latest recovery points.

## LAB25-Q50 — Advanced

To satisfy the failover pilot requirement, operators must change the Azure-to-Azure disaster-recovery pilot configuration and prove it can finalize recovery, reverse protection direction, and return service to the original region. Which sequence is coherent?

- A. First, Create or select the vault in the approved recovery region before enabling replication. Then, Query vault location and confirm it differs from the protected workload's source region.
- B. First, Monitor initial replication and resolve warnings or errors before scheduling the drill. Then, Query protectionState, replicationHealth, activeLocation, and latest recovery points.
- C. First, Start test failover to an isolated target VNet and validate the recovered application before cleanup. Then, Track the test-failover job, recovered VM network, application checks, and cleanup job.
- D. First, Validate recovery, commit deliberately, reprotect to the original region, and plan failback as a separate controlled change. Then, Query activeLocation, allowedOperations, protectionState, and reverse-replication health after each phase.

[Open the answer key](./ANSWERS.md)
