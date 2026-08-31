# Lab 12 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB12-Q01 — Foundational

The compute resilience review compares four claims for the resilient compute capacity design requirement to place instances in separate datacenter fault boundaries within one region. Which claim is technically sound?

- A. Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope.
- B. Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region.
- C. Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
- D. A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination.

## LAB12-Q02 — Foundational

The compute resilience architecture note requires the resilient compute capacity design environment to spread virtual machines across fault and update domains in one datacenter. Which statement defines the relevant compute resilience boundary?

- A. Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement.
- B. Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope.
- C. A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations.
- D. Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move.

## LAB12-Q03 — Foundational

A new compute resilience operator must explain why the resilient compute capacity design can manage individually configurable virtual machines as one scalable group. Which explanation is accurate?

- A. Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit.
- B. Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships.
- C. Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement.
- D. Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data.

## LAB12-Q04 — Foundational

The resilient compute capacity design acceptance criteria require operators to make every instance follow one centrally maintained definition. Which service fact supports that requirement?

- A. Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
- B. A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination.
- C. Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit.
- D. Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region.

## LAB12-Q05 — Foundational

A compute resilience reviewer challenges whether the resilient compute capacity design can adjust instance count from a metric without manual intervention. Which response resolves the concern?

- A. Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
- B. A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations.
- C. Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move.
- D. Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope.

## LAB12-Q06 — Foundational

The resilient compute capacity design handoff omits the compute resilience rule needed to confirm regional SKU availability and subscription capacity before deployment. Which statement should the team add?

- A. Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships.
- B. Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data.
- C. A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations.
- D. Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement.

## LAB12-Q07 — Foundational

A compute resilience incident review of the resilient compute capacity design depends on the ability to relocate a supported virtual machine and its dependencies to another resource group. Which platform description is reliable?

- A. A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination.
- B. Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships.
- C. Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region.
- D. Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit.

## LAB12-Q08 — Foundational

A reliability administrator designing resilient compute is updating the compute resilience runbook. The requirement is to relocate a supported virtual machine across subscription boundaries. Which statement describes Azure behavior correctly?

- A. Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move.
- B. Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope.
- C. Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
- D. A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination.

## LAB12-Q09 — Foundational

A compute resilience peer review asks how the resilient compute capacity design should handle this outcome: recreate supported workload resources in a different Azure region through an orchestrated move. Which explanation is accurate?

- A. Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data.
- B. Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move.
- C. Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement.
- D. A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations.

## LAB12-Q10 — Foundational

For the resilient compute capacity design, the compute resilience plan must prove that the chosen placement model survives its intended failure boundary. Which statement about compute resilience belongs in the resilient compute capacity design record?

- A. Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data.
- B. Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region.
- C. Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit.
- D. Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships.

## LAB12-Q11 — Foundational

A compute resilience dry run shows no resilient compute capacity design command will place instances in separate datacenter fault boundaries within one region. Which action belongs before execution?

- A. Create a flexible scale set with the approved orchestration, zone, and fault-domain settings.
- B. Check SKU restrictions and regional quota before selecting the VM or scale-set size.
- C. Place redundant instances in separate supported zones and design the data tier for the same failure boundary.
- D. Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover.

## LAB12-Q12 — Foundational

For the resilient compute capacity design, operators need to spread virtual machines across fault and update domains in one datacenter. Which change realizes that requirement?

- A. Create the availability set before its VMs and attach each VM during creation.
- B. Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload.
- C. Validate the move set containing the VM, NIC, disks, and other required dependencies.
- D. Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone.

## LAB12-Q13 — Foundational

Operators must automate the resilient compute capacity design change needed to manage individually configurable virtual machines as one scalable group. Which compute resilience operation belongs in the runbook?

- A. Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds.
- B. Validate source and destination subscriptions and move all required dependencies together.
- C. Place redundant instances in separate supported zones and design the data tier for the same failure boundary.
- D. Create a flexible scale set with the approved orchestration, zone, and fault-domain settings.

## LAB12-Q14 — Foundational

A resilient compute capacity design review finds compute resilience drift from the need to make every instance follow one centrally maintained definition. Which correction addresses that drift?

- A. Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload.
- B. Check SKU restrictions and regional quota before selecting the VM or scale-set size.
- C. Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover.
- D. Create the availability set before its VMs and attach each VM during creation.

## LAB12-Q15 — Foundational

The resilient compute capacity design window permits only the compute resilience change needed to adjust instance count from a metric without manual intervention. Which option respects the boundary?

- A. Validate the move set containing the VM, NIC, disks, and other required dependencies.
- B. Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone.
- C. Create a flexible scale set with the approved orchestration, zone, and fault-domain settings.
- D. Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds.

## LAB12-Q16 — Applied

The compute resilience preflight has passed; the resilient compute capacity design must now confirm regional SKU availability and subscription capacity before deployment. Which operation should run?

- A. Validate source and destination subscriptions and move all required dependencies together.
- B. Place redundant instances in separate supported zones and design the data tier for the same failure boundary.
- C. Check SKU restrictions and regional quota before selecting the VM or scale-set size.
- D. Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload.

## LAB12-Q17 — Applied

The resilient compute capacity design plan must relocate a supported virtual machine and its dependencies to another resource group while limiting the mutation scope to compute resilience. Which action is appropriate?

- A. Validate the move set containing the VM, NIC, disks, and other required dependencies.
- B. Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover.
- C. Create the availability set before its VMs and attach each VM during creation.
- D. Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds.

## LAB12-Q18 — Applied

A compute resilience ticket in the resilient compute capacity design says to relocate a supported virtual machine across subscription boundaries. Which compute resilience action completes the resilient compute capacity design request with minimal change?

- A. Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone.
- B. Create a flexible scale set with the approved orchestration, zone, and fault-domain settings.
- C. Validate source and destination subscriptions and move all required dependencies together.
- D. Check SKU restrictions and regional quota before selecting the VM or scale-set size.

## LAB12-Q19 — Applied

The approach for the resilient compute capacity design is approved, but the compute resilience environment still cannot recreate supported workload resources in a different Azure region through an orchestrated move. Which implementation step closes the gap?

- A. Place redundant instances in separate supported zones and design the data tier for the same failure boundary.
- B. Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload.
- C. Validate the move set containing the VM, NIC, disks, and other required dependencies.
- D. Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover.

## LAB12-Q20 — Applied

The reliability administrator designing resilient compute may change the resilient compute capacity design only to prove that the chosen placement model survives its intended failure boundary. Which compute resilience action stays within that assignment?

- A. Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone.
- B. Create the availability set before its VMs and attach each VM during creation.
- C. Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds.
- D. Validate source and destination subscriptions and move all required dependencies together.

## LAB12-Q21 — Applied

The compute resilience validator needs one resilient compute capacity design query after the change to place instances in separate datacenter fault boundaries within one region. Which compute resilience property should the resilient compute capacity design validator inspect?

- A. Query each VM's zones array and confirm the instances occupy different zone numbers.
- B. Query orchestrationMode and compare every instance's latest-model status.
- C. Run move validation and confirm each resource appears under the destination resource group afterward.
- D. Query zone or fault-domain placement and perform a controlled single-instance availability test.

## LAB12-Q22 — Applied

The reliability administrator designing resilient compute must confirm the resilient compute capacity design, without mutation, can spread virtual machines across fault and update domains in one datacenter. Which compute resilience check qualifies?

- A. Query platformFaultDomain and platformUpdateDomain values for every instance.
- B. Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
- C. Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
- D. Query each VM's zones array and confirm the instances occupy different zone numbers.

## LAB12-Q23 — Applied

The resilient compute capacity design configuration is complete; the compute resilience reviewers need evidence it can manage individually configurable virtual machines as one scalable group. Which observation shows success?

- A. Query SKU restrictions and current regional vCPU usage for the target family.
- B. Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
- C. Track prepare, initiate move, commit, and source cleanup states for every dependency.
- D. Query platformFaultDomain and platformUpdateDomain values for every instance.

## LAB12-Q24 — Applied

The compute resilience validation asks whether the resilient compute capacity design can make every instance follow one centrally maintained definition. Which observable state is strongest?

- A. Run move validation and confirm each resource appears under the destination resource group afterward.
- B. Query orchestrationMode and compare every instance's latest-model status.
- C. Query zone or fault-domain placement and perform a controlled single-instance availability test.
- D. Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.

## LAB12-Q25 — Applied

A resilient compute capacity design review must prove the compute resilience ability to adjust instance count from a metric without manual intervention. Which check avoids an adjacent feature?

- A. Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
- B. Query each VM's zones array and confirm the instances occupy different zone numbers.
- C. Query orchestrationMode and compare every instance's latest-model status.
- D. Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.

## LAB12-Q26 — Applied

The resilient compute capacity design evidence bundle needs a compute resilience result showing it can confirm regional SKU availability and subscription capacity before deployment. Which result belongs in the checkpoint?

- A. Track prepare, initiate move, commit, and source cleanup states for every dependency.
- B. Query platformFaultDomain and platformUpdateDomain values for every instance.
- C. Query SKU restrictions and current regional vCPU usage for the target family.
- D. Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.

## LAB12-Q27 — Applied

Before resilient compute capacity design cleanup, the compute resilience team must reconfirm it can relocate a supported virtual machine and its dependencies to another resource group. Which read-only inspection should run?

- A. Query zone or fault-domain placement and perform a controlled single-instance availability test.
- B. Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
- C. Run move validation and confirm each resource appears under the destination resource group afterward.
- D. Query SKU restrictions and current regional vCPU usage for the target family.

## LAB12-Q28 — Applied

The resilient compute capacity design setup reports success after the compute resilience attempt to relocate a supported virtual machine across subscription boundaries. Which compute resilience read-only observation proves the resilient compute capacity design outcome?

- A. Query each VM's zones array and confirm the instances occupy different zone numbers.
- B. Query orchestrationMode and compare every instance's latest-model status.
- C. Run move validation and confirm each resource appears under the destination resource group afterward.
- D. Confirm the destination subscription in each moved resource ID and recheck role assignments separately.

## LAB12-Q29 — Applied

The compute resilience log says the resilient compute capacity design can now recreate supported workload resources in a different Azure region through an orchestrated move. Which compute resilience state should the resilient compute capacity design acceptance test retain?

- A. Query platformFaultDomain and platformUpdateDomain values for every instance.
- B. Track prepare, initiate move, commit, and source cleanup states for every dependency.
- C. Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
- D. Confirm the destination subscription in each moved resource ID and recheck role assignments separately.

## LAB12-Q30 — Applied

The resilient compute capacity design rejects compute resilience exit status as proof it can prove that the chosen placement model survives its intended failure boundary. Which resilient compute capacity design result is valid evidence?

- A. Query zone or fault-domain placement and perform a controlled single-instance availability test.
- B. Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
- C. Query SKU restrictions and current regional vCPU usage for the target family.
- D. Track prepare, initiate move, commit, and source cleanup states for every dependency.

## LAB12-Q31 — Applied

The resilient compute capacity design troubleshooting scope is the compute resilience need to place instances in separate datacenter fault boundaries within one region. Which condition should be corrected first?

- A. A VM was created first and cannot be added to the availability set in place.
- B. Both redundant instances were deployed into the same availability zone.
- C. The VM family quota cannot accommodate the requested instance count.
- D. Multiple instances exist, but all share one failure domain and one data copy.

## LAB12-Q32 — Applied

The resilient compute capacity design result is partial because the compute resilience cannot spread virtual machines across fault and update domains in one datacenter. Which condition accounts for that result?

- A. A VM was created first and cannot be added to the availability set in place.
- B. The deployment assumes uniform-only upgrade behavior on a flexible scale set.
- C. The move request omitted a dependent network interface.
- D. Both redundant instances were deployed into the same availability zone.

## LAB12-Q33 — Applied

The compute resilience evidence shows the resilient compute capacity design cannot manage individually configurable virtual machines as one scalable group. Which root cause fits that evidence?

- A. The deployment assumes uniform-only upgrade behavior on a flexible scale set.
- B. Manual instance customization creates drift from the uniform scale-set model.
- C. The destination subscription lacks registration for a required resource provider.
- D. A VM was created first and cannot be added to the availability set in place.

## LAB12-Q34 — Applied

Although the resilient compute capacity design is meant to let the compute resilience make every instance follow one centrally maintained definition, its checkpoint fails. Which compute resilience defect explains the failure?

- A. The scale-out threshold is reachable, but maximum capacity equals current capacity.
- B. Manual instance customization creates drift from the uniform scale-set model.
- C. The runbook invokes a resource-group move and expects the VM's physical region to change.
- D. The deployment assumes uniform-only upgrade behavior on a flexible scale set.

## LAB12-Q35 — Applied

The compute resilience support team isolated the resilient compute capacity design incident to the attempt to adjust instance count from a metric without manual intervention. Which condition prevents success?

- A. The VM family quota cannot accommodate the requested instance count.
- B. Multiple instances exist, but all share one failure domain and one data copy.
- C. The scale-out threshold is reachable, but maximum capacity equals current capacity.
- D. Manual instance customization creates drift from the uniform scale-set model.

## LAB12-Q36 — Applied

A resilient compute capacity design query surprises the reliability administrator designing resilient compute during the compute resilience attempt to confirm regional SKU availability and subscription capacity before deployment. Which finding explains it?

- A. The move request omitted a dependent network interface.
- B. Both redundant instances were deployed into the same availability zone.
- C. The scale-out threshold is reachable, but maximum capacity equals current capacity.
- D. The VM family quota cannot accommodate the requested instance count.

## LAB12-Q37 — Applied

Other resilient compute capacity design components are healthy, but the compute resilience still cannot relocate a supported virtual machine and its dependencies to another resource group. Which state causes the isolated failure?

- A. The move request omitted a dependent network interface.
- B. The destination subscription lacks registration for a required resource provider.
- C. A VM was created first and cannot be added to the availability set in place.
- D. The VM family quota cannot accommodate the requested instance count.

## LAB12-Q38 — Applied

During a compute resilience fault drill, the resilient compute capacity design does not relocate a supported virtual machine across subscription boundaries. Which finding identifies the defect?

- A. The runbook invokes a resource-group move and expects the VM's physical region to change.
- B. The deployment assumes uniform-only upgrade behavior on a flexible scale set.
- C. The move request omitted a dependent network interface.
- D. The destination subscription lacks registration for a required resource provider.

## LAB12-Q39 — Applied

The resilient compute capacity design setup finishes, yet the compute resilience cannot recreate supported workload resources in a different Azure region through an orchestrated move. Which misconfiguration explains the mismatch?

- A. Multiple instances exist, but all share one failure domain and one data copy.
- B. Manual instance customization creates drift from the uniform scale-set model.
- C. The runbook invokes a resource-group move and expects the VM's physical region to change.
- D. The destination subscription lacks registration for a required resource provider.

## LAB12-Q40 — Applied

A compute resilience break/fix in the resilient compute capacity design fails when operators try to prove that the chosen placement model survives its intended failure boundary. Which diagnosis fits?

- A. Both redundant instances were deployed into the same availability zone.
- B. The scale-out threshold is reachable, but maximum capacity equals current capacity.
- C. The runbook invokes a resource-group move and expects the VM's physical region to change.
- D. Multiple instances exist, but all share one failure domain and one data copy.

## LAB12-Q41 — Advanced

The resilient compute capacity design has two compute resilience gates: place instances in separate datacenter fault boundaries within one region, then prove the resilient compute capacity design state. Which compute resilience sequence works?

- A. First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers.
- B. First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
- C. First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.
- D. First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.

## LAB12-Q42 — Advanced

Which compute resilience path makes the resilient compute capacity design able to spread virtual machines across fault and update domains in one datacenter, then inspects the defining properties?

- A. First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
- B. First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
- C. First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.
- D. First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance.

## LAB12-Q43 — Advanced

At the resilient compute capacity design approval gate, operators must show that the compute resilience can manage individually configurable virtual machines as one scalable group. Which compute resilience configure-and-check pair is defensible?

- A. First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
- B. First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.
- C. First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
- D. First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.

## LAB12-Q44 — Advanced

The resilient compute capacity design forbids a partial compute resilience result. Operators must first make every instance follow one centrally maintained definition and afterward confirm the resilient compute capacity design outcome. Which compute resilience sequence is complete?

- A. First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.
- B. First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.
- C. First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
- D. First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers.

## LAB12-Q45 — Advanced

Only the resilient compute capacity design change needed to adjust instance count from a metric without manual intervention is allowed, and compute resilience proof is mandatory. Which pair fits?

- A. First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.
- B. First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
- C. First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers.
- D. First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance.

## LAB12-Q46 — Advanced

The resilient compute capacity design runbook separates compute resilience mutation from validation while it must confirm regional SKU availability and subscription capacity before deployment. Which sequence proves it cleanly?

- A. First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
- B. First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.
- C. First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance.
- D. First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.

## LAB12-Q47 — Advanced

The resilient compute capacity design checkpoint requires both this compute resilience outcome—relocate a supported virtual machine and its dependencies to another resource group—and a read-only resilient compute capacity design state check. Which compute resilience response is complete?

- A. First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.
- B. First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
- C. First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
- D. First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.

## LAB12-Q48 — Advanced

The resilient compute capacity design runbook must relocate a supported virtual machine across subscription boundaries, then retain compute resilience read-back evidence. Which resilient compute capacity design pair completes both duties?

- A. First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.
- B. First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
- C. First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
- D. First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.

## LAB12-Q49 — Advanced

To satisfy the compute resilience requirement, operators must change the resilient compute capacity design configuration and prove it can recreate supported workload resources in a different Azure region through an orchestrated move. Which sequence is coherent?

- A. First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers.
- B. First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
- C. First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.
- D. First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.

## LAB12-Q50 — Advanced

The reliability administrator designing resilient compute needs a safe resilient compute capacity design change to prove that the chosen placement model survives its intended failure boundary, followed by compute resilience evidence. Which pair merits approval?

- A. First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance.
- B. First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.
- C. First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.
- D. First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.

[Open the answer key](./ANSWERS.md)
