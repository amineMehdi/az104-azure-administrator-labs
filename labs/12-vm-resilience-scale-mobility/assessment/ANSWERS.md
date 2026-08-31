# Lab 12 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB12-Q01 — B

**Question:** The compute resilience review compares four claims for the resilient compute capacity design requirement to place instances in separate datacenter fault boundaries within one region. Which claim is technically sound?

- **A — Incorrect.** Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope.
  Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope. In the resilient compute capacity design, this statement describes availability sets. Resilient compute capacity design asks about availability zones; this availability sets choice leaves the availability zones explanation missing.
- **B — Correct.** Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region.
  Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region. For resilient compute capacity design, availability zones supplies the service rule needed to place instances in separate datacenter fault boundaries within one region.
- **C — Incorrect.** Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
  Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values. In the resilient compute capacity design, this statement describes VM scale-set autoscale. Selecting VM scale-set autoscale for resilient compute capacity design leaves availability zones unanswered in resilient compute capacity design; the resilient compute capacity design lacks a availability zones basis to place instances in separate datacenter fault boundaries within one region.
- **D — Incorrect.** A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination.
  A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination. In the resilient compute capacity design, this statement describes cross-subscription VM moves. Availability zones governs resilient compute capacity design; cross-subscription VM moves cannot support availability zones when operators must place instances in separate datacenter fault boundaries within one region.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Azure availability zones overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q02 — B

**Question:** The compute resilience architecture note requires the resilient compute capacity design environment to spread virtual machines across fault and update domains in one datacenter. Which statement defines the relevant compute resilience boundary?

- **A — Incorrect.** Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement.
  Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement. In the resilient compute capacity design, this statement describes flexible scale sets. The flexible scale sets statement accurately describes flexible scale sets; however, resilient compute capacity design needs availability sets to spread virtual machines across fault and update domains in one datacenter; flexible scale sets cannot replace availability sets.
- **B — Correct.** Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope.
  Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope. In the resilient compute capacity design, this availability sets rule supports the need to spread virtual machines across fault and update domains in one datacenter.
- **C — Incorrect.** A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations.
  A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations. In the resilient compute capacity design, this statement describes regional size and quota checks. Availability sets governs resilient compute capacity design; regional size and quota checks cannot support availability sets when operators must spread virtual machines across fault and update domains in one datacenter.
- **D — Incorrect.** Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move.
  Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move. In the resilient compute capacity design, this statement describes cross-region VM movement. Resilient compute capacity design asks about availability sets; this cross-region VM movement choice leaves the availability sets explanation missing.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Azure virtual machine availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q03 — C

**Question:** A new compute resilience operator must explain why the resilient compute capacity design can manage individually configurable virtual machines as one scalable group. Which explanation is accurate?

- **A — Incorrect.** Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit.
  Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit. In the resilient compute capacity design, this statement describes uniform scale sets. Selecting uniform scale sets for resilient compute capacity design leaves flexible scale sets unanswered in resilient compute capacity design; the resilient compute capacity design lacks a flexible scale sets basis to manage individually configurable virtual machines as one scalable group.
- **B — Incorrect.** Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships.
  Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships. In the resilient compute capacity design, this statement describes resource-group VM moves. Flexible scale sets governs resilient compute capacity design; resource-group VM moves cannot support flexible scale sets when operators must manage individually configurable virtual machines as one scalable group.
- **C — Correct.** Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement.
  For the resilient compute capacity design, the rule for flexible scale sets is defined by this statement: flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement. It supports the required outcome to manage individually configurable virtual machines as one scalable group.
- **D — Incorrect.** Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data.
  Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data. In the resilient compute capacity design, this statement describes resilience validation. The resilience validation statement accurately describes resilience validation; however, resilient compute capacity design needs flexible scale sets to manage individually configurable virtual machines as one scalable group; resilience validation cannot replace flexible scale sets.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Flexible orchestration for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets)

**Source reviewed:** 2026-08-31

## LAB12-Q04 — C

**Question:** The resilient compute capacity design acceptance criteria require operators to make every instance follow one centrally maintained definition. Which service fact supports that requirement?

- **A — Incorrect.** Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
  Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values. In the resilient compute capacity design, this statement describes VM scale-set autoscale. Uniform scale sets governs resilient compute capacity design; VM scale-set autoscale cannot support uniform scale sets when operators must make every instance follow one centrally maintained definition.
- **B — Incorrect.** A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination.
  A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination. In the resilient compute capacity design, this statement describes cross-subscription VM moves. Resilient compute capacity design asks about uniform scale sets; this cross-subscription VM moves choice leaves the uniform scale sets explanation missing.
- **C — Correct.** Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit.
  Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit. The resilient compute capacity design applies that uniform scale sets boundary when operators must make every instance follow one centrally maintained definition.
- **D — Incorrect.** Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region.
  Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region. In the resilient compute capacity design, this statement describes availability zones. Selecting availability zones for resilient compute capacity design leaves uniform scale sets unanswered in resilient compute capacity design; the resilient compute capacity design lacks a uniform scale sets basis to make every instance follow one centrally maintained definition.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Orchestration modes for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes)

**Source reviewed:** 2026-08-31

## LAB12-Q05 — A

**Question:** A compute resilience reviewer challenges whether the resilient compute capacity design can adjust instance count from a metric without manual intervention. Which response resolves the concern?

- **A — Correct.** Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
  The resilient compute capacity design needs VM scale-set autoscale to adjust instance count from a metric without manual intervention; this option states the applicable VM scale-set autoscale rule: autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
- **B — Incorrect.** A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations.
  A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations. In the resilient compute capacity design, this statement describes regional size and quota checks. The regional size and quota checks statement accurately describes regional size and quota checks; however, resilient compute capacity design needs VM scale-set autoscale to adjust instance count from a metric without manual intervention; regional size and quota checks cannot replace VM scale-set autoscale.
- **C — Incorrect.** Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move.
  Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move. In the resilient compute capacity design, this statement describes cross-region VM movement. Selecting cross-region VM movement for resilient compute capacity design leaves VM scale-set autoscale unanswered in resilient compute capacity design; the resilient compute capacity design lacks a VM scale-set autoscale basis to adjust instance count from a metric without manual intervention.
- **D — Incorrect.** Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope.
  Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope. In the resilient compute capacity design, this statement describes availability sets. VM scale-set autoscale governs resilient compute capacity design; availability sets cannot support VM scale-set autoscale when operators must adjust instance count from a metric without manual intervention.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Autoscale a Virtual Machine Scale Set](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q06 — C

**Question:** The resilient compute capacity design handoff omits the compute resilience rule needed to confirm regional SKU availability and subscription capacity before deployment. Which statement should the team add?

- **A — Incorrect.** Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships.
  Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships. In the resilient compute capacity design, this statement describes resource-group VM moves. The resource-group VM moves statement accurately describes resource-group VM moves; however, resilient compute capacity design needs regional size and quota checks to confirm regional SKU availability and subscription capacity before deployment; resource-group VM moves cannot replace regional size and quota checks.
- **B — Incorrect.** Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data.
  Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data. In the resilient compute capacity design, this statement describes resilience validation. Selecting resilience validation for resilient compute capacity design leaves regional size and quota checks unanswered in resilient compute capacity design; the resilient compute capacity design lacks a regional size and quota checks basis to confirm regional SKU availability and subscription capacity before deployment.
- **C — Correct.** A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations.
  A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations. This regional size and quota checks fact resolves the resilient compute capacity design design question about how to confirm regional SKU availability and subscription capacity before deployment.
- **D — Incorrect.** Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement.
  Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement. In the resilient compute capacity design, this statement describes flexible scale sets. Resilient compute capacity design asks about regional size and quota checks; this flexible scale sets choice leaves the regional size and quota checks explanation missing.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Check virtual machine vCPU quotas](https://learn.microsoft.com/en-us/azure/quotas/per-vm-quota-requests)

**Source reviewed:** 2026-08-31

## LAB12-Q07 — B

**Question:** A compute resilience incident review of the resilient compute capacity design depends on the ability to relocate a supported virtual machine and its dependencies to another resource group. Which platform description is reliable?

- **A — Incorrect.** A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination.
  A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination. In the resilient compute capacity design, this statement describes cross-subscription VM moves. Selecting cross-subscription VM moves for resilient compute capacity design leaves resource-group VM moves unanswered in resilient compute capacity design; the resilient compute capacity design lacks a resource-group VM moves basis to relocate a supported virtual machine and its dependencies to another resource group.
- **B — Correct.** Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships.
  Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships. For resilient compute capacity design, resource-group VM moves supplies the service rule needed to relocate a supported virtual machine and its dependencies to another resource group.
- **C — Incorrect.** Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region.
  Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region. In the resilient compute capacity design, this statement describes availability zones. Resilient compute capacity design asks about resource-group VM moves; this availability zones choice leaves the resource-group VM moves explanation missing.
- **D — Incorrect.** Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit.
  Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit. In the resilient compute capacity design, this statement describes uniform scale sets. The uniform scale sets statement accurately describes uniform scale sets; however, resilient compute capacity design needs resource-group VM moves to relocate a supported virtual machine and its dependencies to another resource group; uniform scale sets cannot replace resource-group VM moves.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q08 — D

**Question:** A reliability administrator designing resilient compute is updating the compute resilience runbook. The requirement is to relocate a supported virtual machine across subscription boundaries. Which statement describes Azure behavior correctly?

- **A — Incorrect.** Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move.
  Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move. In the resilient compute capacity design, this statement describes cross-region VM movement. Cross-subscription VM moves governs resilient compute capacity design; cross-region VM movement cannot support cross-subscription VM moves when operators must relocate a supported virtual machine across subscription boundaries.
- **B — Incorrect.** Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope.
  Availability sets distribute classic VM deployments across fault and update domains within one datacenter scope. In the resilient compute capacity design, this statement describes availability sets. Resilient compute capacity design asks about cross-subscription VM moves; this availability sets choice leaves the cross-subscription VM moves explanation missing.
- **C — Incorrect.** Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values.
  Autoscale changes scale-set capacity from metric rules while respecting configured minimum, maximum, and default values. In the resilient compute capacity design, this statement describes VM scale-set autoscale. The VM scale-set autoscale statement accurately describes VM scale-set autoscale; however, resilient compute capacity design needs cross-subscription VM moves to relocate a supported virtual machine across subscription boundaries; VM scale-set autoscale cannot replace cross-subscription VM moves.
- **D — Correct.** A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination.
  A cross-subscription move requires compatible tenants, providers, quotas, and dependent-resource support in the destination. In the resilient compute capacity design, this cross-subscription VM moves rule supports the need to relocate a supported virtual machine across subscription boundaries.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q09 — B

**Question:** A compute resilience peer review asks how the resilient compute capacity design should handle this outcome: recreate supported workload resources in a different Azure region through an orchestrated move. Which explanation is accurate?

- **A — Incorrect.** Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data.
  Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data. In the resilient compute capacity design, this statement describes resilience validation. Resilient compute capacity design asks about cross-region VM movement; this resilience validation choice leaves the cross-region VM movement explanation missing.
- **B — Correct.** Moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move.
  For the resilient compute capacity design, the rule for cross-region VM movement is defined by this statement: moving a VM to another region is a replication-and-cutover workflow rather than a resource-group metadata move. It supports the required outcome to recreate supported workload resources in a different Azure region through an orchestrated move.
- **C — Incorrect.** Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement.
  Flexible orchestration supports VM profiles and individually managed instances across specified fault-domain or zone placement. In the resilient compute capacity design, this statement describes flexible scale sets. Selecting flexible scale sets for resilient compute capacity design leaves cross-region VM movement unanswered in resilient compute capacity design; the resilient compute capacity design lacks a cross-region VM movement basis to recreate supported workload resources in a different Azure region through an orchestrated move.
- **D — Incorrect.** A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations.
  A target size must be supported in the region and have sufficient subscription vCPU quota before scale or resize operations. In the resilient compute capacity design, this statement describes regional size and quota checks. Cross-region VM movement governs resilient compute capacity design; regional size and quota checks cannot support cross-region VM movement when operators must recreate supported workload resources in a different Azure region through an orchestrated move.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to another region](https://learn.microsoft.com/en-us/azure/resource-mover/overview)

**Source reviewed:** 2026-08-31

## LAB12-Q10 — A

**Question:** For the resilient compute capacity design, the compute resilience plan must prove that the chosen placement model survives its intended failure boundary. Which statement about compute resilience belongs in the resilient compute capacity design record?

- **A — Correct.** Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data.
  Resilience requires independent failure domains plus healthy traffic distribution and recoverable application data. The resilient compute capacity design applies that resilience validation boundary when operators must prove that the chosen placement model survives its intended failure boundary.
- **B — Incorrect.** Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region.
  Deploying VM instances across distinct availability zones protects against a datacenter-level failure within a supported region. In the resilient compute capacity design, this statement describes availability zones. Selecting availability zones for resilient compute capacity design leaves resilience validation unanswered in resilient compute capacity design; the resilient compute capacity design lacks a resilience validation basis to prove that the chosen placement model survives its intended failure boundary.
- **C — Incorrect.** Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit.
  Uniform orchestration creates instances from a shared model and manages them as a homogeneous scale unit. In the resilient compute capacity design, this statement describes uniform scale sets. Resilience validation governs resilient compute capacity design; uniform scale sets cannot support resilience validation when operators must prove that the chosen placement model survives its intended failure boundary.
- **D — Incorrect.** Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships.
  Moving a VM between resource groups requires including move-dependent resources and preserving supported relationships. In the resilient compute capacity design, this statement describes resource-group VM moves. Resilient compute capacity design asks about resilience validation; this resource-group VM moves choice leaves the resilience validation explanation missing.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Reliability in Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/reliability/reliability-virtual-machines)

**Source reviewed:** 2026-08-31

## LAB12-Q11 — C

**Question:** A compute resilience dry run shows no resilient compute capacity design command will place instances in separate datacenter fault boundaries within one region. Which action belongs before execution?

- **A — Incorrect.** Create a flexible scale set with the approved orchestration, zone, and fault-domain settings.
  Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. In the resilient compute capacity design, this action changes flexible scale sets. Resilient compute capacity design approved availability zones, not flexible scale sets; only the availability zones change can place instances in separate datacenter fault boundaries within one region.
- **B — Incorrect.** Check SKU restrictions and regional quota before selecting the VM or scale-set size.
  Check SKU restrictions and regional quota before selecting the VM or scale-set size. In the resilient compute capacity design, this action changes regional size and quota checks. Resilient compute capacity design requires availability zones; changing regional size and quota checks leaves availability zones absent in resilient compute capacity design; resilient compute capacity design cannot place instances in separate datacenter fault boundaries within one region.
- **C — Correct.** Place redundant instances in separate supported zones and design the data tier for the same failure boundary.
  The resilient compute capacity design must place instances in separate datacenter fault boundaries within one region; this option performs its direct availability zones change: place redundant instances in separate supported zones and design the data tier for the same failure boundary.
- **D — Incorrect.** Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover.
  Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. In the resilient compute capacity design, this action changes cross-region VM movement. Resilient compute capacity design instead needs availability zones: Place redundant instances in separate supported zones and design the data tier for the same failure boundary. The cross-region VM movement action omits that availability zones work.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Azure availability zones overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q12 — A

**Question:** For the resilient compute capacity design, operators need to spread virtual machines across fault and update domains in one datacenter. Which change realizes that requirement?

- **A — Correct.** Create the availability set before its VMs and attach each VM during creation.
  Create the availability set before its VMs and attach each VM during creation. It is the least-change availability sets path for the resilient compute capacity design requirement to spread virtual machines across fault and update domains in one datacenter.
- **B — Incorrect.** Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload.
  Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. In the resilient compute capacity design, this action changes uniform scale sets. Uniform scale sets does not implement availability sets for resilient compute capacity design; the resilient compute capacity design still cannot spread virtual machines across fault and update domains in one datacenter.
- **C — Incorrect.** Validate the move set containing the VM, NIC, disks, and other required dependencies.
  Validate the move set containing the VM, NIC, disks, and other required dependencies. In the resilient compute capacity design, this action changes resource-group VM moves. Resilient compute capacity design instead needs availability sets: Create the availability set before its VMs and attach each VM during creation. The resource-group VM moves action omits that availability sets work.
- **D — Incorrect.** Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone.
  Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. In the resilient compute capacity design, this action changes resilience validation. Resilient compute capacity design approved availability sets, not resilience validation; only the availability sets change can spread virtual machines across fault and update domains in one datacenter.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Azure virtual machine availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q13 — D

**Question:** Operators must automate the resilient compute capacity design change needed to manage individually configurable virtual machines as one scalable group. Which compute resilience operation belongs in the runbook?

- **A — Incorrect.** Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds.
  Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. In the resilient compute capacity design, this action changes VM scale-set autoscale. VM scale-set autoscale does not implement flexible scale sets for resilient compute capacity design; the resilient compute capacity design still cannot manage individually configurable virtual machines as one scalable group.
- **B — Incorrect.** Validate source and destination subscriptions and move all required dependencies together.
  Validate source and destination subscriptions and move all required dependencies together. In the resilient compute capacity design, this action changes cross-subscription VM moves. Resilient compute capacity design instead needs flexible scale sets: Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. The cross-subscription VM moves action omits that flexible scale sets work.
- **C — Incorrect.** Place redundant instances in separate supported zones and design the data tier for the same failure boundary.
  Place redundant instances in separate supported zones and design the data tier for the same failure boundary. In the resilient compute capacity design, this action changes availability zones. Resilient compute capacity design approved flexible scale sets, not availability zones; only the flexible scale sets change can manage individually configurable virtual machines as one scalable group.
- **D — Correct.** Create a flexible scale set with the approved orchestration, zone, and fault-domain settings.
  Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. In resilient compute capacity design, applying flexible scale sets is the scoped way to manage individually configurable virtual machines as one scalable group.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Flexible orchestration for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets)

**Source reviewed:** 2026-08-31

## LAB12-Q14 — A

**Question:** A resilient compute capacity design review finds compute resilience drift from the need to make every instance follow one centrally maintained definition. Which correction addresses that drift?

- **A — Correct.** Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload.
  Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. The resilient compute capacity design uses this uniform scale sets operation to make every instance follow one centrally maintained definition within the approved scope.
- **B — Incorrect.** Check SKU restrictions and regional quota before selecting the VM or scale-set size.
  Check SKU restrictions and regional quota before selecting the VM or scale-set size. In the resilient compute capacity design, this action changes regional size and quota checks. Resilient compute capacity design approved uniform scale sets, not regional size and quota checks; only the uniform scale sets change can make every instance follow one centrally maintained definition.
- **C — Incorrect.** Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover.
  Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. In the resilient compute capacity design, this action changes cross-region VM movement. Resilient compute capacity design requires uniform scale sets; changing cross-region VM movement leaves uniform scale sets absent in resilient compute capacity design; resilient compute capacity design cannot make every instance follow one centrally maintained definition.
- **D — Incorrect.** Create the availability set before its VMs and attach each VM during creation.
  Create the availability set before its VMs and attach each VM during creation. In the resilient compute capacity design, this action changes availability sets. Availability sets does not implement uniform scale sets for resilient compute capacity design; the resilient compute capacity design still cannot make every instance follow one centrally maintained definition.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Orchestration modes for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes)

**Source reviewed:** 2026-08-31

## LAB12-Q15 — D

**Question:** The resilient compute capacity design window permits only the compute resilience change needed to adjust instance count from a metric without manual intervention. Which option respects the boundary?

- **A — Incorrect.** Validate the move set containing the VM, NIC, disks, and other required dependencies.
  Validate the move set containing the VM, NIC, disks, and other required dependencies. In the resilient compute capacity design, this action changes resource-group VM moves. Resilient compute capacity design approved VM scale-set autoscale, not resource-group VM moves; only the VM scale-set autoscale change can adjust instance count from a metric without manual intervention.
- **B — Incorrect.** Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone.
  Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. In the resilient compute capacity design, this action changes resilience validation. Resilient compute capacity design requires VM scale-set autoscale; changing resilience validation leaves VM scale-set autoscale absent in resilient compute capacity design; resilient compute capacity design cannot adjust instance count from a metric without manual intervention.
- **C — Incorrect.** Create a flexible scale set with the approved orchestration, zone, and fault-domain settings.
  Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. In the resilient compute capacity design, this action changes flexible scale sets. Flexible scale sets does not implement VM scale-set autoscale for resilient compute capacity design; the resilient compute capacity design still cannot adjust instance count from a metric without manual intervention.
- **D — Correct.** Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds.
  For the resilient compute capacity design, the required VM scale-set autoscale action is: create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. It makes the environment able to adjust instance count from a metric without manual intervention.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Autoscale a Virtual Machine Scale Set](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q16 — C

**Question:** The compute resilience preflight has passed; the resilient compute capacity design must now confirm regional SKU availability and subscription capacity before deployment. Which operation should run?

- **A — Incorrect.** Validate source and destination subscriptions and move all required dependencies together.
  Validate source and destination subscriptions and move all required dependencies together. In the resilient compute capacity design, this action changes cross-subscription VM moves. Resilient compute capacity design requires regional size and quota checks; changing cross-subscription VM moves leaves regional size and quota checks absent in resilient compute capacity design; resilient compute capacity design cannot confirm regional SKU availability and subscription capacity before deployment.
- **B — Incorrect.** Place redundant instances in separate supported zones and design the data tier for the same failure boundary.
  Place redundant instances in separate supported zones and design the data tier for the same failure boundary. In the resilient compute capacity design, this action changes availability zones. Availability zones does not implement regional size and quota checks for resilient compute capacity design; the resilient compute capacity design still cannot confirm regional SKU availability and subscription capacity before deployment.
- **C — Correct.** Check SKU restrictions and regional quota before selecting the VM or scale-set size.
  Check SKU restrictions and regional quota before selecting the VM or scale-set size. This changes regional size and quota checks in the resilient compute capacity design, supplying the missing state needed to confirm regional SKU availability and subscription capacity before deployment.
- **D — Incorrect.** Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload.
  Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. In the resilient compute capacity design, this action changes uniform scale sets. Resilient compute capacity design approved regional size and quota checks, not uniform scale sets; only the regional size and quota checks change can confirm regional SKU availability and subscription capacity before deployment.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Check virtual machine vCPU quotas](https://learn.microsoft.com/en-us/azure/quotas/per-vm-quota-requests)

**Source reviewed:** 2026-08-31

## LAB12-Q17 — A

**Question:** The resilient compute capacity design plan must relocate a supported virtual machine and its dependencies to another resource group while limiting the mutation scope to compute resilience. Which action is appropriate?

- **A — Correct.** Validate the move set containing the VM, NIC, disks, and other required dependencies.
  The resilient compute capacity design must relocate a supported virtual machine and its dependencies to another resource group; this option performs its direct resource-group VM moves change: validate the move set containing the VM, NIC, disks, and other required dependencies.
- **B — Incorrect.** Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover.
  Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. In the resilient compute capacity design, this action changes cross-region VM movement. Resilient compute capacity design instead needs resource-group VM moves: Validate the move set containing the VM, NIC, disks, and other required dependencies. The cross-region VM movement action omits that resource-group VM moves work.
- **C — Incorrect.** Create the availability set before its VMs and attach each VM during creation.
  Create the availability set before its VMs and attach each VM during creation. In the resilient compute capacity design, this action changes availability sets. Resilient compute capacity design approved resource-group VM moves, not availability sets; only the resource-group VM moves change can relocate a supported virtual machine and its dependencies to another resource group.
- **D — Incorrect.** Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds.
  Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. In the resilient compute capacity design, this action changes VM scale-set autoscale. Resilient compute capacity design requires resource-group VM moves; changing VM scale-set autoscale leaves resource-group VM moves absent in resilient compute capacity design; resilient compute capacity design cannot relocate a supported virtual machine and its dependencies to another resource group.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q18 — C

**Question:** A compute resilience ticket in the resilient compute capacity design says to relocate a supported virtual machine across subscription boundaries. Which compute resilience action completes the resilient compute capacity design request with minimal change?

- **A — Incorrect.** Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone.
  Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. In the resilient compute capacity design, this action changes resilience validation. Resilient compute capacity design instead needs cross-subscription VM moves: Validate source and destination subscriptions and move all required dependencies together. The resilience validation action omits that cross-subscription VM moves work.
- **B — Incorrect.** Create a flexible scale set with the approved orchestration, zone, and fault-domain settings.
  Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. In the resilient compute capacity design, this action changes flexible scale sets. Resilient compute capacity design approved cross-subscription VM moves, not flexible scale sets; only the cross-subscription VM moves change can relocate a supported virtual machine across subscription boundaries.
- **C — Correct.** Validate source and destination subscriptions and move all required dependencies together.
  Validate source and destination subscriptions and move all required dependencies together. It is the least-change cross-subscription VM moves path for the resilient compute capacity design requirement to relocate a supported virtual machine across subscription boundaries.
- **D — Incorrect.** Check SKU restrictions and regional quota before selecting the VM or scale-set size.
  Check SKU restrictions and regional quota before selecting the VM or scale-set size. In the resilient compute capacity design, this action changes regional size and quota checks. Regional size and quota checks does not implement cross-subscription VM moves for resilient compute capacity design; the resilient compute capacity design still cannot relocate a supported virtual machine across subscription boundaries.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q19 — D

**Question:** The approach for the resilient compute capacity design is approved, but the compute resilience environment still cannot recreate supported workload resources in a different Azure region through an orchestrated move. Which implementation step closes the gap?

- **A — Incorrect.** Place redundant instances in separate supported zones and design the data tier for the same failure boundary.
  Place redundant instances in separate supported zones and design the data tier for the same failure boundary. In the resilient compute capacity design, this action changes availability zones. Resilient compute capacity design approved cross-region VM movement, not availability zones; only the cross-region VM movement change can recreate supported workload resources in a different Azure region through an orchestrated move.
- **B — Incorrect.** Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload.
  Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. In the resilient compute capacity design, this action changes uniform scale sets. Resilient compute capacity design requires cross-region VM movement; changing uniform scale sets leaves cross-region VM movement absent in resilient compute capacity design; resilient compute capacity design cannot recreate supported workload resources in a different Azure region through an orchestrated move.
- **C — Incorrect.** Validate the move set containing the VM, NIC, disks, and other required dependencies.
  Validate the move set containing the VM, NIC, disks, and other required dependencies. In the resilient compute capacity design, this action changes resource-group VM moves. Resource-group VM moves does not implement cross-region VM movement for resilient compute capacity design; the resilient compute capacity design still cannot recreate supported workload resources in a different Azure region through an orchestrated move.
- **D — Correct.** Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover.
  Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. In resilient compute capacity design, applying cross-region VM movement is the scoped way to recreate supported workload resources in a different Azure region through an orchestrated move.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to another region](https://learn.microsoft.com/en-us/azure/resource-mover/overview)

**Source reviewed:** 2026-08-31

## LAB12-Q20 — A

**Question:** The reliability administrator designing resilient compute may change the resilient compute capacity design only to prove that the chosen placement model survives its intended failure boundary. Which compute resilience action stays within that assignment?

- **A — Correct.** Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone.
  Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. The resilient compute capacity design uses this resilience validation operation to prove that the chosen placement model survives its intended failure boundary within the approved scope.
- **B — Incorrect.** Create the availability set before its VMs and attach each VM during creation.
  Create the availability set before its VMs and attach each VM during creation. In the resilient compute capacity design, this action changes availability sets. Availability sets does not implement resilience validation for resilient compute capacity design; the resilient compute capacity design still cannot prove that the chosen placement model survives its intended failure boundary.
- **C — Incorrect.** Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds.
  Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. In the resilient compute capacity design, this action changes VM scale-set autoscale. Resilient compute capacity design instead needs resilience validation: Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. The VM scale-set autoscale action omits that resilience validation work.
- **D — Incorrect.** Validate source and destination subscriptions and move all required dependencies together.
  Validate source and destination subscriptions and move all required dependencies together. In the resilient compute capacity design, this action changes cross-subscription VM moves. Resilient compute capacity design approved resilience validation, not cross-subscription VM moves; only the resilience validation change can prove that the chosen placement model survives its intended failure boundary.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Reliability in Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/reliability/reliability-virtual-machines)

**Source reviewed:** 2026-08-31

## LAB12-Q21 — A

**Question:** The compute resilience validator needs one resilient compute capacity design query after the change to place instances in separate datacenter fault boundaries within one region. Which compute resilience property should the resilient compute capacity design validator inspect?

- **A — Correct.** Query each VM's zones array and confirm the instances occupy different zone numbers.
  For the resilient compute capacity design, this availability zones observation is decisive: query each VM's zones array and confirm the instances occupy different zone numbers. It is resilient compute capacity design evidence that operators can place instances in separate datacenter fault boundaries within one region.
- **B — Incorrect.** Query orchestrationMode and compare every instance's latest-model status.
  Query orchestrationMode and compare every instance's latest-model status. In the resilient compute capacity design, this check observes uniform scale sets. Uniform scale sets success in resilient compute capacity design cannot verify availability zones; resilient compute capacity design cannot place instances in separate datacenter fault boundaries within one region until availability zones evidence exists.
- **C — Incorrect.** Run move validation and confirm each resource appears under the destination resource group afterward.
  Run move validation and confirm each resource appears under the destination resource group afterward. In the resilient compute capacity design, this check observes resource-group VM moves. Resilient compute capacity design reads resource-group VM moves, leaving availability zones unproved in resilient compute capacity design; resilient compute capacity design still has no availability zones proof.
- **D — Incorrect.** Query zone or fault-domain placement and perform a controlled single-instance availability test.
  Query zone or fault-domain placement and perform a controlled single-instance availability test. In the resilient compute capacity design, this check observes resilience validation. Resilient compute capacity design could pass resilience validation while availability zones is wrong; resilient compute capacity design still lacks availability zones proof.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Azure availability zones overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q22 — A

**Question:** The reliability administrator designing resilient compute must confirm the resilient compute capacity design, without mutation, can spread virtual machines across fault and update domains in one datacenter. Which compute resilience check qualifies?

- **A — Correct.** Query platformFaultDomain and platformUpdateDomain values for every instance.
  Query platformFaultDomain and platformUpdateDomain values for every instance. Because the resilient compute capacity design check observes availability sets, it independently verifies the requirement to spread virtual machines across fault and update domains in one datacenter.
- **B — Incorrect.** Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
  Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric. In the resilient compute capacity design, this check observes VM scale-set autoscale. Resilient compute capacity design reads VM scale-set autoscale, leaving availability sets unproved in resilient compute capacity design; resilient compute capacity design still has no availability sets proof.
- **C — Incorrect.** Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
  Confirm the destination subscription in each moved resource ID and recheck role assignments separately. In the resilient compute capacity design, this check observes cross-subscription VM moves. Resilient compute capacity design could pass cross-subscription VM moves while availability sets is wrong; resilient compute capacity design still lacks availability sets proof.
- **D — Incorrect.** Query each VM's zones array and confirm the instances occupy different zone numbers.
  Query each VM's zones array and confirm the instances occupy different zone numbers. In the resilient compute capacity design, this check observes availability zones. Resilient compute capacity design output covers availability zones, not availability sets; the availability sets requirement to spread virtual machines across fault and update domains in one datacenter remains unverified.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Azure virtual machine availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q23 — B

**Question:** The resilient compute capacity design configuration is complete; the compute resilience reviewers need evidence it can manage individually configurable virtual machines as one scalable group. Which observation shows success?

- **A — Incorrect.** Query SKU restrictions and current regional vCPU usage for the target family.
  Query SKU restrictions and current regional vCPU usage for the target family. In the resilient compute capacity design, this check observes regional size and quota checks. Resilient compute capacity design reads regional size and quota checks, leaving flexible scale sets unproved in resilient compute capacity design; resilient compute capacity design still has no flexible scale sets proof.
- **B — Correct.** Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
  The resilient compute capacity design validator needs this flexible scale sets result: query orchestrationMode, zones, platformFaultDomainCount, and instance membership. It proves the outcome to manage individually configurable virtual machines as one scalable group rather than an adjacent checkpoint.
- **C — Incorrect.** Track prepare, initiate move, commit, and source cleanup states for every dependency.
  Track prepare, initiate move, commit, and source cleanup states for every dependency. In the resilient compute capacity design, this check observes cross-region VM movement. Resilient compute capacity design output covers cross-region VM movement, not flexible scale sets; the flexible scale sets requirement to manage individually configurable virtual machines as one scalable group remains unverified.
- **D — Incorrect.** Query platformFaultDomain and platformUpdateDomain values for every instance.
  Query platformFaultDomain and platformUpdateDomain values for every instance. In the resilient compute capacity design, this check observes availability sets. Availability sets success in resilient compute capacity design cannot verify flexible scale sets; resilient compute capacity design cannot manage individually configurable virtual machines as one scalable group until flexible scale sets evidence exists.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Flexible orchestration for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets)

**Source reviewed:** 2026-08-31

## LAB12-Q24 — B

**Question:** The compute resilience validation asks whether the resilient compute capacity design can make every instance follow one centrally maintained definition. Which observable state is strongest?

- **A — Incorrect.** Run move validation and confirm each resource appears under the destination resource group afterward.
  Run move validation and confirm each resource appears under the destination resource group afterward. In the resilient compute capacity design, this check observes resource-group VM moves. Resilient compute capacity design could pass resource-group VM moves while uniform scale sets is wrong; resilient compute capacity design still lacks uniform scale sets proof.
- **B — Correct.** Query orchestrationMode and compare every instance's latest-model status.
  Query orchestrationMode and compare every instance's latest-model status. This is independent uniform scale sets evidence for the resilient compute capacity design, even if resilient compute capacity design setup reports success before uniform scale sets becomes observable.
- **C — Incorrect.** Query zone or fault-domain placement and perform a controlled single-instance availability test.
  Query zone or fault-domain placement and perform a controlled single-instance availability test. In the resilient compute capacity design, this check observes resilience validation. Resilience validation success in resilient compute capacity design cannot verify uniform scale sets; resilient compute capacity design cannot make every instance follow one centrally maintained definition until uniform scale sets evidence exists.
- **D — Incorrect.** Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
  Query orchestrationMode, zones, platformFaultDomainCount, and instance membership. In the resilient compute capacity design, this check observes flexible scale sets. Resilient compute capacity design reads flexible scale sets, leaving uniform scale sets unproved in resilient compute capacity design; resilient compute capacity design still has no uniform scale sets proof.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Orchestration modes for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes)

**Source reviewed:** 2026-08-31

## LAB12-Q25 — D

**Question:** A resilient compute capacity design review must prove the compute resilience ability to adjust instance count from a metric without manual intervention. Which check avoids an adjacent feature?

- **A — Incorrect.** Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
  Confirm the destination subscription in each moved resource ID and recheck role assignments separately. In the resilient compute capacity design, this check observes cross-subscription VM moves. Resilient compute capacity design output covers cross-subscription VM moves, not VM scale-set autoscale; the VM scale-set autoscale requirement to adjust instance count from a metric without manual intervention remains unverified.
- **B — Incorrect.** Query each VM's zones array and confirm the instances occupy different zone numbers.
  Query each VM's zones array and confirm the instances occupy different zone numbers. In the resilient compute capacity design, this check observes availability zones. Availability zones success in resilient compute capacity design cannot verify VM scale-set autoscale; resilient compute capacity design cannot adjust instance count from a metric without manual intervention until VM scale-set autoscale evidence exists.
- **C — Incorrect.** Query orchestrationMode and compare every instance's latest-model status.
  Query orchestrationMode and compare every instance's latest-model status. In the resilient compute capacity design, this check observes uniform scale sets. Resilient compute capacity design reads uniform scale sets, leaving VM scale-set autoscale unproved in resilient compute capacity design; resilient compute capacity design still has no VM scale-set autoscale proof.
- **D — Correct.** Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
  Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric. For resilient compute capacity design, this VM scale-set autoscale read confirms the service can adjust instance count from a metric without manual intervention.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Autoscale a Virtual Machine Scale Set](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q26 — C

**Question:** The resilient compute capacity design evidence bundle needs a compute resilience result showing it can confirm regional SKU availability and subscription capacity before deployment. Which result belongs in the checkpoint?

- **A — Incorrect.** Track prepare, initiate move, commit, and source cleanup states for every dependency.
  Track prepare, initiate move, commit, and source cleanup states for every dependency. In the resilient compute capacity design, this check observes cross-region VM movement. Cross-region VM movement success in resilient compute capacity design cannot verify regional size and quota checks; resilient compute capacity design cannot confirm regional SKU availability and subscription capacity before deployment until regional size and quota checks evidence exists.
- **B — Incorrect.** Query platformFaultDomain and platformUpdateDomain values for every instance.
  Query platformFaultDomain and platformUpdateDomain values for every instance. In the resilient compute capacity design, this check observes availability sets. Resilient compute capacity design reads availability sets, leaving regional size and quota checks unproved in resilient compute capacity design; resilient compute capacity design still has no regional size and quota checks proof.
- **C — Correct.** Query SKU restrictions and current regional vCPU usage for the target family.
  Query SKU restrictions and current regional vCPU usage for the target family. The resilient compute capacity design reads regional size and quota checks directly; that regional size and quota checks result proves the resilient compute capacity design can confirm regional SKU availability and subscription capacity before deployment without another mutation.
- **D — Incorrect.** Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
  Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric. In the resilient compute capacity design, this check observes VM scale-set autoscale. Resilient compute capacity design output covers VM scale-set autoscale, not regional size and quota checks; the regional size and quota checks requirement to confirm regional SKU availability and subscription capacity before deployment remains unverified.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Check virtual machine vCPU quotas](https://learn.microsoft.com/en-us/azure/quotas/per-vm-quota-requests)

**Source reviewed:** 2026-08-31

## LAB12-Q27 — C

**Question:** Before resilient compute capacity design cleanup, the compute resilience team must reconfirm it can relocate a supported virtual machine and its dependencies to another resource group. Which read-only inspection should run?

- **A — Incorrect.** Query zone or fault-domain placement and perform a controlled single-instance availability test.
  Query zone or fault-domain placement and perform a controlled single-instance availability test. In the resilient compute capacity design, this check observes resilience validation. Resilient compute capacity design reads resilience validation, leaving resource-group VM moves unproved in resilient compute capacity design; resilient compute capacity design still has no resource-group VM moves proof.
- **B — Incorrect.** Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
  Query orchestrationMode, zones, platformFaultDomainCount, and instance membership. In the resilient compute capacity design, this check observes flexible scale sets. Resilient compute capacity design could pass flexible scale sets while resource-group VM moves is wrong; resilient compute capacity design still lacks resource-group VM moves proof.
- **C — Correct.** Run move validation and confirm each resource appears under the destination resource group afterward.
  For the resilient compute capacity design, this resource-group VM moves observation is decisive: run move validation and confirm each resource appears under the destination resource group afterward. It is resilient compute capacity design evidence that operators can relocate a supported virtual machine and its dependencies to another resource group.
- **D — Incorrect.** Query SKU restrictions and current regional vCPU usage for the target family.
  Query SKU restrictions and current regional vCPU usage for the target family. In the resilient compute capacity design, this check observes regional size and quota checks. Regional size and quota checks success in resilient compute capacity design cannot verify resource-group VM moves; resilient compute capacity design cannot relocate a supported virtual machine and its dependencies to another resource group until resource-group VM moves evidence exists.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q28 — D

**Question:** The resilient compute capacity design setup reports success after the compute resilience attempt to relocate a supported virtual machine across subscription boundaries. Which compute resilience read-only observation proves the resilient compute capacity design outcome?

- **A — Incorrect.** Query each VM's zones array and confirm the instances occupy different zone numbers.
  Query each VM's zones array and confirm the instances occupy different zone numbers. In the resilient compute capacity design, this check observes availability zones. Resilient compute capacity design could pass availability zones while cross-subscription VM moves is wrong; resilient compute capacity design still lacks cross-subscription VM moves proof.
- **B — Incorrect.** Query orchestrationMode and compare every instance's latest-model status.
  Query orchestrationMode and compare every instance's latest-model status. In the resilient compute capacity design, this check observes uniform scale sets. Resilient compute capacity design output covers uniform scale sets, not cross-subscription VM moves; the cross-subscription VM moves requirement to relocate a supported virtual machine across subscription boundaries remains unverified.
- **C — Incorrect.** Run move validation and confirm each resource appears under the destination resource group afterward.
  Run move validation and confirm each resource appears under the destination resource group afterward. In the resilient compute capacity design, this check observes resource-group VM moves. Resource-group VM moves success in resilient compute capacity design cannot verify cross-subscription VM moves; resilient compute capacity design cannot relocate a supported virtual machine across subscription boundaries until cross-subscription VM moves evidence exists.
- **D — Correct.** Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
  Confirm the destination subscription in each moved resource ID and recheck role assignments separately. Because the resilient compute capacity design check observes cross-subscription VM moves, it independently verifies the requirement to relocate a supported virtual machine across subscription boundaries.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q29 — B

**Question:** The compute resilience log says the resilient compute capacity design can now recreate supported workload resources in a different Azure region through an orchestrated move. Which compute resilience state should the resilient compute capacity design acceptance test retain?

- **A — Incorrect.** Query platformFaultDomain and platformUpdateDomain values for every instance.
  Query platformFaultDomain and platformUpdateDomain values for every instance. In the resilient compute capacity design, this check observes availability sets. Resilient compute capacity design output covers availability sets, not cross-region VM movement; the cross-region VM movement requirement to recreate supported workload resources in a different Azure region through an orchestrated move remains unverified.
- **B — Correct.** Track prepare, initiate move, commit, and source cleanup states for every dependency.
  The resilient compute capacity design validator needs this cross-region VM movement result: track prepare, initiate move, commit, and source cleanup states for every dependency. It proves the outcome to recreate supported workload resources in a different Azure region through an orchestrated move rather than an adjacent checkpoint.
- **C — Incorrect.** Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
  Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric. In the resilient compute capacity design, this check observes VM scale-set autoscale. Resilient compute capacity design reads VM scale-set autoscale, leaving cross-region VM movement unproved in resilient compute capacity design; resilient compute capacity design still has no cross-region VM movement proof.
- **D — Incorrect.** Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
  Confirm the destination subscription in each moved resource ID and recheck role assignments separately. In the resilient compute capacity design, this check observes cross-subscription VM moves. Resilient compute capacity design could pass cross-subscription VM moves while cross-region VM movement is wrong; resilient compute capacity design still lacks cross-region VM movement proof.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to another region](https://learn.microsoft.com/en-us/azure/resource-mover/overview)

**Source reviewed:** 2026-08-31

## LAB12-Q30 — A

**Question:** The resilient compute capacity design rejects compute resilience exit status as proof it can prove that the chosen placement model survives its intended failure boundary. Which resilient compute capacity design result is valid evidence?

- **A — Correct.** Query zone or fault-domain placement and perform a controlled single-instance availability test.
  Query zone or fault-domain placement and perform a controlled single-instance availability test. This is independent resilience validation evidence for the resilient compute capacity design, even if resilient compute capacity design setup reports success before resilience validation becomes observable.
- **B — Incorrect.** Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
  Query orchestrationMode, zones, platformFaultDomainCount, and instance membership. In the resilient compute capacity design, this check observes flexible scale sets. Resilient compute capacity design reads flexible scale sets, leaving resilience validation unproved in resilient compute capacity design; resilient compute capacity design still has no resilience validation proof.
- **C — Incorrect.** Query SKU restrictions and current regional vCPU usage for the target family.
  Query SKU restrictions and current regional vCPU usage for the target family. In the resilient compute capacity design, this check observes regional size and quota checks. Resilient compute capacity design could pass regional size and quota checks while resilience validation is wrong; resilient compute capacity design still lacks resilience validation proof.
- **D — Incorrect.** Track prepare, initiate move, commit, and source cleanup states for every dependency.
  Track prepare, initiate move, commit, and source cleanup states for every dependency. In the resilient compute capacity design, this check observes cross-region VM movement. Resilient compute capacity design output covers cross-region VM movement, not resilience validation; the resilience validation requirement to prove that the chosen placement model survives its intended failure boundary remains unverified.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Reliability in Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/reliability/reliability-virtual-machines)

**Source reviewed:** 2026-08-31

## LAB12-Q31 — B

**Question:** The resilient compute capacity design troubleshooting scope is the compute resilience need to place instances in separate datacenter fault boundaries within one region. Which condition should be corrected first?

- **A — Incorrect.** A VM was created first and cannot be added to the availability set in place.
  A VM was created first and cannot be added to the availability set in place. The resilient compute capacity design fault concerns availability sets. Resilient compute capacity design has availability sets impact, but availability zones is the resilient compute capacity design failed path; the availability sets state cannot produce availability zones failure.
- **B — Correct.** Both redundant instances were deployed into the same availability zone.
  Both redundant instances were deployed into the same availability zone. In resilient compute capacity design, this availability zones cause matches the failure to place instances in separate datacenter fault boundaries within one region.
- **C — Incorrect.** The VM family quota cannot accommodate the requested instance count.
  The VM family quota cannot accommodate the requested instance count. The resilient compute capacity design fault concerns regional size and quota checks. Resilient compute capacity design failed on availability zones; this regional size and quota checks finding redirects resilient compute capacity design remediation away from availability zones.
- **D — Incorrect.** Multiple instances exist, but all share one failure domain and one data copy.
  Multiple instances exist, but all share one failure domain and one data copy. The resilient compute capacity design fault concerns resilience validation. Resilient compute capacity design may fix resilience validation, yet availability zones still fails; this resilient compute capacity design diagnosis of resilience validation is wrong for availability zones.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Azure availability zones overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q32 — A

**Question:** The resilient compute capacity design result is partial because the compute resilience cannot spread virtual machines across fault and update domains in one datacenter. Which condition accounts for that result?

- **A — Correct.** A VM was created first and cannot be added to the availability set in place.
  A VM was created first and cannot be added to the availability set in place. This resilient compute capacity design condition breaks availability sets, explaining why operators cannot spread virtual machines across fault and update domains in one datacenter.
- **B — Incorrect.** The deployment assumes uniform-only upgrade behavior on a flexible scale set.
  The deployment assumes uniform-only upgrade behavior on a flexible scale set. The resilient compute capacity design fault concerns flexible scale sets. Resilient compute capacity design failed on availability sets; this flexible scale sets finding redirects resilient compute capacity design remediation away from availability sets.
- **C — Incorrect.** The move request omitted a dependent network interface.
  The move request omitted a dependent network interface. The resilient compute capacity design fault concerns resource-group VM moves. Resilient compute capacity design may fix resource-group VM moves, yet availability sets still fails; this resilient compute capacity design diagnosis of resource-group VM moves is wrong for availability sets.
- **D — Incorrect.** Both redundant instances were deployed into the same availability zone.
  Both redundant instances were deployed into the same availability zone. The resilient compute capacity design fault concerns availability zones. Resilient compute capacity design has availability zones impact, but availability sets is the resilient compute capacity design failed path; the availability zones state cannot produce availability sets failure.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Azure virtual machine availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q33 — A

**Question:** The compute resilience evidence shows the resilient compute capacity design cannot manage individually configurable virtual machines as one scalable group. Which root cause fits that evidence?

- **A — Correct.** The deployment assumes uniform-only upgrade behavior on a flexible scale set.
  For the resilient compute capacity design, the flexible scale sets failure is causal: the deployment assumes uniform-only upgrade behavior on a flexible scale set. Correcting it restores the ability to manage individually configurable virtual machines as one scalable group.
- **B — Incorrect.** Manual instance customization creates drift from the uniform scale-set model.
  Manual instance customization creates drift from the uniform scale-set model. The resilient compute capacity design fault concerns uniform scale sets. Resilient compute capacity design may fix uniform scale sets, yet flexible scale sets still fails; this resilient compute capacity design diagnosis of uniform scale sets is wrong for flexible scale sets.
- **C — Incorrect.** The destination subscription lacks registration for a required resource provider.
  The destination subscription lacks registration for a required resource provider. The resilient compute capacity design fault concerns cross-subscription VM moves. Resilient compute capacity design has cross-subscription VM moves impact, but flexible scale sets is the resilient compute capacity design failed path; the cross-subscription VM moves state cannot produce flexible scale sets failure.
- **D — Incorrect.** A VM was created first and cannot be added to the availability set in place.
  A VM was created first and cannot be added to the availability set in place. The resilient compute capacity design fault concerns availability sets. Resilient compute capacity design could repair availability sets while flexible scale sets stays broken in resilient compute capacity design; the resilient compute capacity design remains unable to manage individually configurable virtual machines as one scalable group.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Flexible orchestration for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets)

**Source reviewed:** 2026-08-31

## LAB12-Q34 — B

**Question:** Although the resilient compute capacity design is meant to let the compute resilience make every instance follow one centrally maintained definition, its checkpoint fails. Which compute resilience defect explains the failure?

- **A — Incorrect.** The scale-out threshold is reachable, but maximum capacity equals current capacity.
  The scale-out threshold is reachable, but maximum capacity equals current capacity. The resilient compute capacity design fault concerns VM scale-set autoscale. Resilient compute capacity design may fix VM scale-set autoscale, yet uniform scale sets still fails; this resilient compute capacity design diagnosis of VM scale-set autoscale is wrong for uniform scale sets.
- **B — Correct.** Manual instance customization creates drift from the uniform scale-set model.
  Manual instance customization creates drift from the uniform scale-set model. The finding is specific to uniform scale sets in the resilient compute capacity design; repairing uniform scale sets restores the resilient compute capacity design ability to make every instance follow one centrally maintained definition.
- **C — Incorrect.** The runbook invokes a resource-group move and expects the VM's physical region to change.
  The runbook invokes a resource-group move and expects the VM's physical region to change. The resilient compute capacity design fault concerns cross-region VM movement. Resilient compute capacity design could repair cross-region VM movement while uniform scale sets stays broken in resilient compute capacity design; the resilient compute capacity design remains unable to make every instance follow one centrally maintained definition.
- **D — Incorrect.** The deployment assumes uniform-only upgrade behavior on a flexible scale set.
  The deployment assumes uniform-only upgrade behavior on a flexible scale set. The resilient compute capacity design fault concerns flexible scale sets. Resilient compute capacity design failed on uniform scale sets; this flexible scale sets finding redirects resilient compute capacity design remediation away from uniform scale sets.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Orchestration modes for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes)

**Source reviewed:** 2026-08-31

## LAB12-Q35 — C

**Question:** The compute resilience support team isolated the resilient compute capacity design incident to the attempt to adjust instance count from a metric without manual intervention. Which condition prevents success?

- **A — Incorrect.** The VM family quota cannot accommodate the requested instance count.
  The VM family quota cannot accommodate the requested instance count. The resilient compute capacity design fault concerns regional size and quota checks. Resilient compute capacity design has regional size and quota checks impact, but VM scale-set autoscale is the resilient compute capacity design failed path; the regional size and quota checks state cannot produce VM scale-set autoscale failure.
- **B — Incorrect.** Multiple instances exist, but all share one failure domain and one data copy.
  Multiple instances exist, but all share one failure domain and one data copy. The resilient compute capacity design fault concerns resilience validation. Resilient compute capacity design could repair resilience validation while VM scale-set autoscale stays broken in resilient compute capacity design; the resilient compute capacity design remains unable to adjust instance count from a metric without manual intervention.
- **C — Correct.** The scale-out threshold is reachable, but maximum capacity equals current capacity.
  The resilient compute capacity design cannot adjust instance count from a metric without manual intervention because of this VM scale-set autoscale defect: the scale-out threshold is reachable, but maximum capacity equals current capacity. The symptom and repair align.
- **D — Incorrect.** Manual instance customization creates drift from the uniform scale-set model.
  Manual instance customization creates drift from the uniform scale-set model. The resilient compute capacity design fault concerns uniform scale sets. Resilient compute capacity design may fix uniform scale sets, yet VM scale-set autoscale still fails; this resilient compute capacity design diagnosis of uniform scale sets is wrong for VM scale-set autoscale.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Autoscale a Virtual Machine Scale Set](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q36 — D

**Question:** A resilient compute capacity design query surprises the reliability administrator designing resilient compute during the compute resilience attempt to confirm regional SKU availability and subscription capacity before deployment. Which finding explains it?

- **A — Incorrect.** The move request omitted a dependent network interface.
  The move request omitted a dependent network interface. The resilient compute capacity design fault concerns resource-group VM moves. Resilient compute capacity design could repair resource-group VM moves while regional size and quota checks stays broken in resilient compute capacity design; the resilient compute capacity design remains unable to confirm regional SKU availability and subscription capacity before deployment.
- **B — Incorrect.** Both redundant instances were deployed into the same availability zone.
  Both redundant instances were deployed into the same availability zone. The resilient compute capacity design fault concerns availability zones. Resilient compute capacity design failed on regional size and quota checks; this availability zones finding redirects resilient compute capacity design remediation away from regional size and quota checks.
- **C — Incorrect.** The scale-out threshold is reachable, but maximum capacity equals current capacity.
  The scale-out threshold is reachable, but maximum capacity equals current capacity. The resilient compute capacity design fault concerns VM scale-set autoscale. Resilient compute capacity design may fix VM scale-set autoscale, yet regional size and quota checks still fails; this resilient compute capacity design diagnosis of VM scale-set autoscale is wrong for regional size and quota checks.
- **D — Correct.** The VM family quota cannot accommodate the requested instance count.
  The VM family quota cannot accommodate the requested instance count. Removing this regional size and quota checks condition lets the resilient compute capacity design confirm regional SKU availability and subscription capacity before deployment while leaving healthy controls unchanged.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Check virtual machine vCPU quotas](https://learn.microsoft.com/en-us/azure/quotas/per-vm-quota-requests)

**Source reviewed:** 2026-08-31

## LAB12-Q37 — A

**Question:** Other resilient compute capacity design components are healthy, but the compute resilience still cannot relocate a supported virtual machine and its dependencies to another resource group. Which state causes the isolated failure?

- **A — Correct.** The move request omitted a dependent network interface.
  The move request omitted a dependent network interface. In resilient compute capacity design, this resource-group VM moves cause matches the failure to relocate a supported virtual machine and its dependencies to another resource group.
- **B — Incorrect.** The destination subscription lacks registration for a required resource provider.
  The destination subscription lacks registration for a required resource provider. The resilient compute capacity design fault concerns cross-subscription VM moves. Resilient compute capacity design may fix cross-subscription VM moves, yet resource-group VM moves still fails; this resilient compute capacity design diagnosis of cross-subscription VM moves is wrong for resource-group VM moves.
- **C — Incorrect.** A VM was created first and cannot be added to the availability set in place.
  A VM was created first and cannot be added to the availability set in place. The resilient compute capacity design fault concerns availability sets. Resilient compute capacity design has availability sets impact, but resource-group VM moves is the resilient compute capacity design failed path; the availability sets state cannot produce resource-group VM moves failure.
- **D — Incorrect.** The VM family quota cannot accommodate the requested instance count.
  The VM family quota cannot accommodate the requested instance count. The resilient compute capacity design fault concerns regional size and quota checks. Resilient compute capacity design could repair regional size and quota checks while resource-group VM moves stays broken in resilient compute capacity design; the resilient compute capacity design remains unable to relocate a supported virtual machine and its dependencies to another resource group.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q38 — D

**Question:** During a compute resilience fault drill, the resilient compute capacity design does not relocate a supported virtual machine across subscription boundaries. Which finding identifies the defect?

- **A — Incorrect.** The runbook invokes a resource-group move and expects the VM's physical region to change.
  The runbook invokes a resource-group move and expects the VM's physical region to change. The resilient compute capacity design fault concerns cross-region VM movement. Resilient compute capacity design may fix cross-region VM movement, yet cross-subscription VM moves still fails; this resilient compute capacity design diagnosis of cross-region VM movement is wrong for cross-subscription VM moves.
- **B — Incorrect.** The deployment assumes uniform-only upgrade behavior on a flexible scale set.
  The deployment assumes uniform-only upgrade behavior on a flexible scale set. The resilient compute capacity design fault concerns flexible scale sets. Resilient compute capacity design has flexible scale sets impact, but cross-subscription VM moves is the resilient compute capacity design failed path; the flexible scale sets state cannot produce cross-subscription VM moves failure.
- **C — Incorrect.** The move request omitted a dependent network interface.
  The move request omitted a dependent network interface. The resilient compute capacity design fault concerns resource-group VM moves. Resilient compute capacity design could repair resource-group VM moves while cross-subscription VM moves stays broken in resilient compute capacity design; the resilient compute capacity design remains unable to relocate a supported virtual machine across subscription boundaries.
- **D — Correct.** The destination subscription lacks registration for a required resource provider.
  The destination subscription lacks registration for a required resource provider. This resilient compute capacity design condition breaks cross-subscription VM moves, explaining why operators cannot relocate a supported virtual machine across subscription boundaries.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q39 — C

**Question:** The resilient compute capacity design setup finishes, yet the compute resilience cannot recreate supported workload resources in a different Azure region through an orchestrated move. Which misconfiguration explains the mismatch?

- **A — Incorrect.** Multiple instances exist, but all share one failure domain and one data copy.
  Multiple instances exist, but all share one failure domain and one data copy. The resilient compute capacity design fault concerns resilience validation. Resilient compute capacity design has resilience validation impact, but cross-region VM movement is the resilient compute capacity design failed path; the resilience validation state cannot produce cross-region VM movement failure.
- **B — Incorrect.** Manual instance customization creates drift from the uniform scale-set model.
  Manual instance customization creates drift from the uniform scale-set model. The resilient compute capacity design fault concerns uniform scale sets. Resilient compute capacity design could repair uniform scale sets while cross-region VM movement stays broken in resilient compute capacity design; the resilient compute capacity design remains unable to recreate supported workload resources in a different Azure region through an orchestrated move.
- **C — Correct.** The runbook invokes a resource-group move and expects the VM's physical region to change.
  For the resilient compute capacity design, the cross-region VM movement failure is causal: the runbook invokes a resource-group move and expects the VM's physical region to change. Correcting it restores the ability to recreate supported workload resources in a different Azure region through an orchestrated move.
- **D — Incorrect.** The destination subscription lacks registration for a required resource provider.
  The destination subscription lacks registration for a required resource provider. The resilient compute capacity design fault concerns cross-subscription VM moves. Resilient compute capacity design may fix cross-subscription VM moves, yet cross-region VM movement still fails; this resilient compute capacity design diagnosis of cross-subscription VM moves is wrong for cross-region VM movement.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to another region](https://learn.microsoft.com/en-us/azure/resource-mover/overview)

**Source reviewed:** 2026-08-31

## LAB12-Q40 — D

**Question:** A compute resilience break/fix in the resilient compute capacity design fails when operators try to prove that the chosen placement model survives its intended failure boundary. Which diagnosis fits?

- **A — Incorrect.** Both redundant instances were deployed into the same availability zone.
  Both redundant instances were deployed into the same availability zone. The resilient compute capacity design fault concerns availability zones. Resilient compute capacity design could repair availability zones while resilience validation stays broken in resilient compute capacity design; the resilient compute capacity design remains unable to prove that the chosen placement model survives its intended failure boundary.
- **B — Incorrect.** The scale-out threshold is reachable, but maximum capacity equals current capacity.
  The scale-out threshold is reachable, but maximum capacity equals current capacity. The resilient compute capacity design fault concerns VM scale-set autoscale. Resilient compute capacity design failed on resilience validation; this VM scale-set autoscale finding redirects resilient compute capacity design remediation away from resilience validation.
- **C — Incorrect.** The runbook invokes a resource-group move and expects the VM's physical region to change.
  The runbook invokes a resource-group move and expects the VM's physical region to change. The resilient compute capacity design fault concerns cross-region VM movement. Resilient compute capacity design may fix cross-region VM movement, yet resilience validation still fails; this resilient compute capacity design diagnosis of cross-region VM movement is wrong for resilience validation.
- **D — Correct.** Multiple instances exist, but all share one failure domain and one data copy.
  Multiple instances exist, but all share one failure domain and one data copy. The finding is specific to resilience validation in the resilient compute capacity design; repairing resilience validation restores the resilient compute capacity design ability to prove that the chosen placement model survives its intended failure boundary.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Reliability in Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/reliability/reliability-virtual-machines)

**Source reviewed:** 2026-08-31

## LAB12-Q41 — A

**Question:** The resilient compute capacity design has two compute resilience gates: place instances in separate datacenter fault boundaries within one region, then prove the resilient compute capacity design state. Which compute resilience sequence works?

- **A — Correct.** First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers.
  The resilient compute capacity design gets a complete availability zones sequence here: first, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers. Read-back evidence follows the change.
- **B — Incorrect.** First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
  First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership. This resilient compute capacity design pair serves flexible scale sets. Resilient compute capacity design proves flexible scale sets, but availability zones lacks implementation in resilient compute capacity design and availability zones proof; the availability zones outcome to place instances in separate datacenter fault boundaries within one region remains open.
- **C — Incorrect.** First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.
  First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward. This resilient compute capacity design pair serves resource-group VM moves. Resilient compute capacity design uses resource-group VM moves for both steps; availability zones remains untouched in resilient compute capacity design, so its availability zones gate to place instances in separate datacenter fault boundaries within one region fails.
- **D — Incorrect.** First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
  First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately. This resilient compute capacity design pair serves cross-subscription VM moves. Resilient compute capacity design closes cross-subscription VM moves, not availability zones; without the availability zones workflow, it cannot place instances in separate datacenter fault boundaries within one region.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Azure availability zones overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q42 — D

**Question:** Which compute resilience path makes the resilient compute capacity design able to spread virtual machines across fault and update domains in one datacenter, then inspects the defining properties?

- **A — Incorrect.** First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
  First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status. This resilient compute capacity design pair serves uniform scale sets. Resilient compute capacity design proves uniform scale sets, but availability sets lacks implementation in resilient compute capacity design and availability sets proof; the availability sets outcome to spread virtual machines across fault and update domains in one datacenter remains open.
- **B — Incorrect.** First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
  First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately. This resilient compute capacity design pair serves cross-subscription VM moves. Resilient compute capacity design uses cross-subscription VM moves for both steps; availability sets remains untouched in resilient compute capacity design, so its availability sets gate to spread virtual machines across fault and update domains in one datacenter fails.
- **C — Incorrect.** First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.
  First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency. This resilient compute capacity design pair serves cross-region VM movement. Resilient compute capacity design closes cross-region VM movement, not availability sets; without the availability sets workflow, it cannot spread virtual machines across fault and update domains in one datacenter.
- **D — Correct.** First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance.
  First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance. This ordered availability sets workflow lets the resilient compute capacity design spread virtual machines across fault and update domains in one datacenter and then verify the resulting state.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Azure virtual machine availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q43 — C

**Question:** At the resilient compute capacity design approval gate, operators must show that the compute resilience can manage individually configurable virtual machines as one scalable group. Which compute resilience configure-and-check pair is defensible?

- **A — Incorrect.** First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
  First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric. This resilient compute capacity design pair serves VM scale-set autoscale. Resilient compute capacity design uses VM scale-set autoscale for both steps; flexible scale sets remains untouched in resilient compute capacity design, so its flexible scale sets gate to manage individually configurable virtual machines as one scalable group fails.
- **B — Incorrect.** First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.
  First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency. This resilient compute capacity design pair serves cross-region VM movement. Resilient compute capacity design closes cross-region VM movement, not flexible scale sets; without the flexible scale sets workflow, it cannot manage individually configurable virtual machines as one scalable group.
- **C — Correct.** First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
  First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership. For resilient compute capacity design, the flexible scale sets operation precedes its flexible scale sets read-back check, allowing it to manage individually configurable virtual machines as one scalable group.
- **D — Incorrect.** First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.
  First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test. This resilient compute capacity design pair serves resilience validation. Resilient compute capacity design proves resilience validation, but flexible scale sets lacks implementation in resilient compute capacity design and flexible scale sets proof; the flexible scale sets outcome to manage individually configurable virtual machines as one scalable group remains open.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Flexible orchestration for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets)

**Source reviewed:** 2026-08-31

## LAB12-Q44 — C

**Question:** The resilient compute capacity design forbids a partial compute resilience result. Operators must first make every instance follow one centrally maintained definition and afterward confirm the resilient compute capacity design outcome. Which compute resilience sequence is complete?

- **A — Incorrect.** First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.
  First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family. This resilient compute capacity design pair serves regional size and quota checks. Resilient compute capacity design closes regional size and quota checks, not uniform scale sets; without the uniform scale sets workflow, it cannot make every instance follow one centrally maintained definition.
- **B — Incorrect.** First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.
  First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test. This resilient compute capacity design pair serves resilience validation. Resilience validation cannot replace uniform scale sets in resilient compute capacity design. Use this uniform scale sets pair instead: First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
- **C — Correct.** First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
  First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status. In the resilient compute capacity design, the first uniform scale sets step runs; the resilient compute capacity design then reads uniform scale sets state to prove it can make every instance follow one centrally maintained definition.
- **D — Incorrect.** First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers.
  First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers. This resilient compute capacity design pair serves availability zones. Resilient compute capacity design uses availability zones for both steps; uniform scale sets remains untouched in resilient compute capacity design, so its uniform scale sets gate to make every instance follow one centrally maintained definition fails.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Orchestration modes for Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes)

**Source reviewed:** 2026-08-31

## LAB12-Q45 — B

**Question:** Only the resilient compute capacity design change needed to adjust instance count from a metric without manual intervention is allowed, and compute resilience proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.
  First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward. This resilient compute capacity design pair serves resource-group VM moves. Resource-group VM moves cannot replace VM scale-set autoscale in resilient compute capacity design. Use this VM scale-set autoscale pair instead: First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
- **B — Correct.** First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
  For the resilient compute capacity design, the safe VM scale-set autoscale order is: first, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric. The resilient compute capacity design records VM scale-set autoscale proof after configuration.
- **C — Incorrect.** First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers.
  First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers. This resilient compute capacity design pair serves availability zones. Resilient compute capacity design uses availability zones for both steps; VM scale-set autoscale remains untouched in resilient compute capacity design, so its VM scale-set autoscale gate to adjust instance count from a metric without manual intervention fails.
- **D — Incorrect.** First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance.
  First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance. This resilient compute capacity design pair serves availability sets. Resilient compute capacity design closes availability sets, not VM scale-set autoscale; without the VM scale-set autoscale workflow, it cannot adjust instance count from a metric without manual intervention.

**Objectives:** `CP-VM-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Autoscale a Virtual Machine Scale Set](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-overview)

**Source reviewed:** 2026-08-31

## LAB12-Q46 — B

**Question:** The resilient compute capacity design runbook separates compute resilience mutation from validation while it must confirm regional SKU availability and subscription capacity before deployment. Which sequence proves it cleanly?

- **A — Incorrect.** First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
  First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately. This resilient compute capacity design pair serves cross-subscription VM moves. Resilient compute capacity design proves cross-subscription VM moves, but regional size and quota checks lacks implementation in resilient compute capacity design and regional size and quota checks proof; the regional size and quota checks outcome to confirm regional SKU availability and subscription capacity before deployment remains open.
- **B — Correct.** First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.
  First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family. The resilient compute capacity design uses its regional size and quota checks mutation gate and regional size and quota checks verification gate before it can confirm regional SKU availability and subscription capacity before deployment.
- **C — Incorrect.** First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance.
  First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance. This resilient compute capacity design pair serves availability sets. Resilient compute capacity design closes availability sets, not regional size and quota checks; without the regional size and quota checks workflow, it cannot confirm regional SKU availability and subscription capacity before deployment.
- **D — Incorrect.** First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
  First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership. This resilient compute capacity design pair serves flexible scale sets. Flexible scale sets cannot replace regional size and quota checks in resilient compute capacity design. Use this regional size and quota checks pair instead: First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB12-CP01`).

**Microsoft Learn sources:**

- [Check virtual machine vCPU quotas](https://learn.microsoft.com/en-us/azure/quotas/per-vm-quota-requests)

**Source reviewed:** 2026-08-31

## LAB12-Q47 — D

**Question:** The resilient compute capacity design checkpoint requires both this compute resilience outcome—relocate a supported virtual machine and its dependencies to another resource group—and a read-only resilient compute capacity design state check. Which compute resilience response is complete?

- **A — Incorrect.** First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.
  First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency. This resilient compute capacity design pair serves cross-region VM movement. Resilient compute capacity design uses cross-region VM movement for both steps; resource-group VM moves remains untouched in resilient compute capacity design, so its resource-group VM moves gate to relocate a supported virtual machine and its dependencies to another resource group fails.
- **B — Incorrect.** First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership.
  First, Create a flexible scale set with the approved orchestration, zone, and fault-domain settings. Then, Query orchestrationMode, zones, platformFaultDomainCount, and instance membership. This resilient compute capacity design pair serves flexible scale sets. Resilient compute capacity design closes flexible scale sets, not resource-group VM moves; without the resource-group VM moves workflow, it cannot relocate a supported virtual machine and its dependencies to another resource group.
- **C — Incorrect.** First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
  First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status. This resilient compute capacity design pair serves uniform scale sets. Uniform scale sets cannot replace resource-group VM moves in resilient compute capacity design. Use this resource-group VM moves pair instead: First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.
- **D — Correct.** First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.
  The resilient compute capacity design gets a complete resource-group VM moves sequence here: first, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward. Read-back evidence follows the change.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB12-CP02`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q48 — C

**Question:** The resilient compute capacity design runbook must relocate a supported virtual machine across subscription boundaries, then retain compute resilience read-back evidence. Which resilient compute capacity design pair completes both duties?

- **A — Incorrect.** First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.
  First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test. This resilient compute capacity design pair serves resilience validation. Resilient compute capacity design closes resilience validation, not cross-subscription VM moves; without the cross-subscription VM moves workflow, it cannot relocate a supported virtual machine across subscription boundaries.
- **B — Incorrect.** First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status.
  First, Use uniform orchestration when identical instance configuration and scale-set-managed lifecycle fit the workload. Then, Query orchestrationMode and compare every instance's latest-model status. This resilient compute capacity design pair serves uniform scale sets. Uniform scale sets cannot replace cross-subscription VM moves in resilient compute capacity design. Use this cross-subscription VM moves pair instead: First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
- **C — Correct.** First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately.
  First, Validate source and destination subscriptions and move all required dependencies together. Then, Confirm the destination subscription in each moved resource ID and recheck role assignments separately. This ordered cross-subscription VM moves workflow lets the resilient compute capacity design relocate a supported virtual machine across subscription boundaries and then verify the resulting state.
- **D — Incorrect.** First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
  First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric. This resilient compute capacity design pair serves VM scale-set autoscale. Resilient compute capacity design uses VM scale-set autoscale for both steps; cross-subscription VM moves remains untouched in resilient compute capacity design, so its cross-subscription VM moves gate to relocate a supported virtual machine across subscription boundaries fails.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB12-CP03`).

**Microsoft Learn sources:**

- [Move guidance for virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations)

**Source reviewed:** 2026-08-31

## LAB12-Q49 — D

**Question:** To satisfy the compute resilience requirement, operators must change the resilient compute capacity design configuration and prove it can recreate supported workload resources in a different Azure region through an orchestrated move. Which sequence is coherent?

- **A — Incorrect.** First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers.
  First, Place redundant instances in separate supported zones and design the data tier for the same failure boundary. Then, Query each VM's zones array and confirm the instances occupy different zone numbers. This resilient compute capacity design pair serves availability zones. Availability zones cannot replace cross-region VM movement in resilient compute capacity design. Use this cross-region VM movement pair instead: First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.
- **B — Incorrect.** First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric.
  First, Create scale-out and scale-in rules with safe thresholds, aggregation windows, cooldowns, and capacity bounds. Then, Query autoscale profiles and confirm capacity bounds and paired rules reference the intended resource metric. This resilient compute capacity design pair serves VM scale-set autoscale. Resilient compute capacity design proves VM scale-set autoscale, but cross-region VM movement lacks implementation in resilient compute capacity design and cross-region VM movement proof; the cross-region VM movement outcome to recreate supported workload resources in a different Azure region through an orchestrated move remains open.
- **C — Incorrect.** First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.
  First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family. This resilient compute capacity design pair serves regional size and quota checks. Resilient compute capacity design uses regional size and quota checks for both steps; cross-region VM movement remains untouched in resilient compute capacity design, so its cross-region VM movement gate to recreate supported workload resources in a different Azure region through an orchestrated move fails.
- **D — Correct.** First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency.
  First, Use Azure Resource Mover or another supported replication workflow and validate dependencies before cutover. Then, Track prepare, initiate move, commit, and source cleanup states for every dependency. For resilient compute capacity design, the cross-region VM movement operation precedes its cross-region VM movement read-back check, allowing it to recreate supported workload resources in a different Azure region through an orchestrated move.

**Objectives:** `CP-VM-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB12-CP04`).

**Microsoft Learn sources:**

- [Move Azure resources to another region](https://learn.microsoft.com/en-us/azure/resource-mover/overview)

**Source reviewed:** 2026-08-31

## LAB12-Q50 — B

**Question:** The reliability administrator designing resilient compute needs a safe resilient compute capacity design change to prove that the chosen placement model survives its intended failure boundary, followed by compute resilience evidence. Which pair merits approval?

- **A — Incorrect.** First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance.
  First, Create the availability set before its VMs and attach each VM during creation. Then, Query platformFaultDomain and platformUpdateDomain values for every instance. This resilient compute capacity design pair serves availability sets. Resilient compute capacity design proves availability sets, but resilience validation lacks implementation in resilient compute capacity design and resilience validation proof; the resilience validation outcome to prove that the chosen placement model survives its intended failure boundary remains open.
- **B — Correct.** First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.
  First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test. In the resilient compute capacity design, the first resilience validation step runs; the resilient compute capacity design then reads resilience validation state to prove it can prove that the chosen placement model survives its intended failure boundary.
- **C — Incorrect.** First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family.
  First, Check SKU restrictions and regional quota before selecting the VM or scale-set size. Then, Query SKU restrictions and current regional vCPU usage for the target family. This resilient compute capacity design pair serves regional size and quota checks. Resilient compute capacity design closes regional size and quota checks, not resilience validation; without the resilience validation workflow, it cannot prove that the chosen placement model survives its intended failure boundary.
- **D — Incorrect.** First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward.
  First, Validate the move set containing the VM, NIC, disks, and other required dependencies. Then, Run move validation and confirm each resource appears under the destination resource group afterward. This resilient compute capacity design pair serves resource-group VM moves. Resource-group VM moves cannot replace resilience validation in resilient compute capacity design. Use this resilience validation pair instead: First, Validate placement, health, load-balancing, and data recovery instead of relying on instance count alone. Then, Query zone or fault-domain placement and perform a controlled single-instance availability test.

**Objectives:** `CP-VM-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB12-CP05`).

**Microsoft Learn sources:**

- [Reliability in Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/reliability/reliability-virtual-machines)

**Source reviewed:** 2026-08-31
