# Lab 11 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB11-Q01 — A

**Question:** A compute administrator maintaining a secured Linux VM is updating the VM maintenance runbook. The requirement is to choose a regionally available Marketplace image reference. Which statement describes Azure behavior correctly?

- **A — Correct.** A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms.
  A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms. The secured Linux VM maintenance window applies that virtual machine image selection boundary when operators must choose a regionally available Marketplace image reference.
- **B — Incorrect.** A VM network interface must reference a valid subnet and satisfy regional and attachment constraints.
  A VM network interface must reference a valid subnet and satisfy regional and attachment constraints. In the secured Linux VM maintenance window, this statement describes network interface dependency. The network interface dependency statement accurately describes network interface dependency; however, secured Linux VM maintenance window needs virtual machine image selection to choose a regionally available Marketplace image reference; network interface dependency cannot replace virtual machine image selection.
- **C — Incorrect.** Managed disk type and size determine supported performance, cost, and workload characteristics.
  Managed disk type and size determine supported performance, cost, and workload characteristics. In the secured Linux VM maintenance window, this statement describes managed disk performance tiers. Selecting managed disk performance tiers for secured Linux VM maintenance window leaves virtual machine image selection unanswered in secured Linux VM maintenance window; the secured Linux VM maintenance window lacks a virtual machine image selection basis to choose a regionally available Marketplace image reference.
- **D — Incorrect.** Some VM resizes require deallocation when the target size is unavailable on the current cluster.
  Some VM resizes require deallocation when the target size is unavailable on the current cluster. In the secured Linux VM maintenance window, this statement describes resize deallocation. Virtual machine image selection governs secured Linux VM maintenance window; resize deallocation cannot support virtual machine image selection when operators must choose a regionally available Marketplace image reference.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Find Azure Marketplace image information with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage)

**Source reviewed:** 2026-08-31

## LAB11-Q02 — A

**Question:** A VM maintenance peer review asks how the secured Linux VM maintenance window should handle this outcome: attach the virtual machine to the intended subnet through its network interface. Which explanation is accurate?

- **A — Correct.** A VM network interface must reference a valid subnet and satisfy regional and attachment constraints.
  The secured Linux VM maintenance window needs network interface dependency to attach the virtual machine to the intended subnet through its network interface; this option states the applicable network interface dependency rule: a VM network interface must reference a valid subnet and satisfy regional and attachment constraints.
- **B — Incorrect.** Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption.
  Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption. In the secured Linux VM maintenance window, this statement describes encryption at host. Selecting encryption at host for secured Linux VM maintenance window leaves network interface dependency unanswered in secured Linux VM maintenance window; the secured Linux VM maintenance window lacks a network interface dependency basis to attach the virtual machine to the intended subnet through its network interface.
- **C — Incorrect.** A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest.
  A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest. In the secured Linux VM maintenance window, this statement describes attaching data disks. Network interface dependency governs secured Linux VM maintenance window; attaching data disks cannot support network interface dependency when operators must attach the virtual machine to the intended subnet through its network interface.
- **D — Incorrect.** A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation.
  A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation. In the secured Linux VM maintenance window, this statement describes stopped and deallocated states. Secured Linux VM maintenance window asks about network interface dependency; this stopped and deallocated states choice leaves the network interface dependency explanation missing.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Create a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q03 — C

**Question:** For the secured Linux VM maintenance window, the VM maintenance plan must encrypt supported host caches and temporary storage at the compute host. Which statement about VM maintenance belongs in the secured Linux VM maintenance window record?

- **A — Incorrect.** A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss.
  A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss. In the secured Linux VM maintenance window, this statement describes temporary disks. Selecting temporary disks for secured Linux VM maintenance window leaves encryption at host unanswered in secured Linux VM maintenance window; the secured Linux VM maintenance window lacks a encryption at host basis to encrypt supported host caches and temporary storage at the compute host.
- **B — Incorrect.** Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity.
  Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity. In the secured Linux VM maintenance window, this statement describes VM size availability. Encryption at host governs secured Linux VM maintenance window; VM size availability cannot support encryption at host when operators must encrypt supported host caches and temporary storage at the compute host.
- **C — Correct.** Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption.
  Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption. This encryption at host fact resolves the secured Linux VM maintenance window design question about how to encrypt supported host caches and temporary storage at the compute host.
- **D — Incorrect.** A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs.
  A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs. In the secured Linux VM maintenance window, this statement describes managed disk snapshots. The managed disk snapshots statement accurately describes managed disk snapshots; however, secured Linux VM maintenance window needs encryption at host to encrypt supported host caches and temporary storage at the compute host; managed disk snapshots cannot replace encryption at host.

**Objectives:** `CP-VM-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Encryption at host for Azure virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disks-enable-host-based-encryption-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q04 — B

**Question:** The VM maintenance review compares four claims for the secured Linux VM maintenance window requirement to keep durable workload data off the host-local scratch disk. Which claim is technically sound?

- **A — Incorrect.** Managed disk type and size determine supported performance, cost, and workload characteristics.
  Managed disk type and size determine supported performance, cost, and workload characteristics. In the secured Linux VM maintenance window, this statement describes managed disk performance tiers. Temporary disks governs secured Linux VM maintenance window; managed disk performance tiers cannot support temporary disks when operators must keep durable workload data off the host-local scratch disk.
- **B — Correct.** A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss.
  A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss. For secured Linux VM maintenance window, temporary disks supplies the service rule needed to keep durable workload data off the host-local scratch disk.
- **C — Incorrect.** Some VM resizes require deallocation when the target size is unavailable on the current cluster.
  Some VM resizes require deallocation when the target size is unavailable on the current cluster. In the secured Linux VM maintenance window, this statement describes resize deallocation. The resize deallocation statement accurately describes resize deallocation; however, secured Linux VM maintenance window needs temporary disks to keep durable workload data off the host-local scratch disk; resize deallocation cannot replace temporary disks.
- **D — Incorrect.** A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms.
  A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms. In the secured Linux VM maintenance window, this statement describes virtual machine image selection. Selecting virtual machine image selection for secured Linux VM maintenance window leaves temporary disks unanswered in secured Linux VM maintenance window; the secured Linux VM maintenance window lacks a temporary disks basis to keep durable workload data off the host-local scratch disk.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Managed disks overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)

**Source reviewed:** 2026-08-31

## LAB11-Q05 — A

**Question:** The VM maintenance architecture note requires the secured Linux VM maintenance window environment to choose a managed disk tier that meets the workload's performance requirement. Which statement defines the relevant VM maintenance boundary?

- **A — Correct.** Managed disk type and size determine supported performance, cost, and workload characteristics.
  Managed disk type and size determine supported performance, cost, and workload characteristics. In the secured Linux VM maintenance window, this managed disk performance tiers rule supports the need to choose a managed disk tier that meets the workload's performance requirement.
- **B — Incorrect.** A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest.
  A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest. In the secured Linux VM maintenance window, this statement describes attaching data disks. The attaching data disks statement accurately describes attaching data disks; however, secured Linux VM maintenance window needs managed disk performance tiers to choose a managed disk tier that meets the workload's performance requirement; attaching data disks cannot replace managed disk performance tiers.
- **C — Incorrect.** A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation.
  A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation. In the secured Linux VM maintenance window, this statement describes stopped and deallocated states. Selecting stopped and deallocated states for secured Linux VM maintenance window leaves managed disk performance tiers unanswered in secured Linux VM maintenance window; the secured Linux VM maintenance window lacks a managed disk performance tiers basis to choose a managed disk tier that meets the workload's performance requirement.
- **D — Incorrect.** A VM network interface must reference a valid subnet and satisfy regional and attachment constraints.
  A VM network interface must reference a valid subnet and satisfy regional and attachment constraints. In the secured Linux VM maintenance window, this statement describes network interface dependency. Managed disk performance tiers governs secured Linux VM maintenance window; network interface dependency cannot support managed disk performance tiers when operators must choose a managed disk tier that meets the workload's performance requirement.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Azure managed disk types](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

**Source reviewed:** 2026-08-31

## LAB11-Q06 — B

**Question:** A new VM maintenance operator must explain why the secured Linux VM maintenance window can add persistent capacity without replacing the operating-system disk. Which explanation is accurate?

- **A — Incorrect.** Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity.
  Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity. In the secured Linux VM maintenance window, this statement describes VM size availability. The VM size availability statement accurately describes VM size availability; however, secured Linux VM maintenance window needs attaching data disks to add persistent capacity without replacing the operating-system disk; VM size availability cannot replace attaching data disks.
- **B — Correct.** A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest.
  For the secured Linux VM maintenance window, the rule for attaching data disks is defined by this statement: a managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest. It supports the required outcome to add persistent capacity without replacing the operating-system disk.
- **C — Incorrect.** A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs.
  A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs. In the secured Linux VM maintenance window, this statement describes managed disk snapshots. Attaching data disks governs secured Linux VM maintenance window; managed disk snapshots cannot support attaching data disks when operators must add persistent capacity without replacing the operating-system disk.
- **D — Incorrect.** Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption.
  Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption. In the secured Linux VM maintenance window, this statement describes encryption at host. Secured Linux VM maintenance window asks about attaching data disks; this encryption at host choice leaves the attaching data disks explanation missing.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Add a data disk to a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/add-disk)

**Source reviewed:** 2026-08-31

## LAB11-Q07 — B

**Question:** The secured Linux VM maintenance window acceptance criteria require operators to confirm that the requested compute shape is offered in the deployment region. Which service fact supports that requirement?

- **A — Incorrect.** Some VM resizes require deallocation when the target size is unavailable on the current cluster.
  Some VM resizes require deallocation when the target size is unavailable on the current cluster. In the secured Linux VM maintenance window, this statement describes resize deallocation. Selecting resize deallocation for secured Linux VM maintenance window leaves VM size availability unanswered in secured Linux VM maintenance window; the secured Linux VM maintenance window lacks a VM size availability basis to confirm that the requested compute shape is offered in the deployment region.
- **B — Correct.** Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity.
  Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity. The secured Linux VM maintenance window applies that VM size availability boundary when operators must confirm that the requested compute shape is offered in the deployment region.
- **C — Incorrect.** A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms.
  A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms. In the secured Linux VM maintenance window, this statement describes virtual machine image selection. Secured Linux VM maintenance window asks about VM size availability; this virtual machine image selection choice leaves the VM size availability explanation missing.
- **D — Incorrect.** A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss.
  A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss. In the secured Linux VM maintenance window, this statement describes temporary disks. The temporary disks statement accurately describes temporary disks; however, secured Linux VM maintenance window needs VM size availability to confirm that the requested compute shape is offered in the deployment region; temporary disks cannot replace VM size availability.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Virtual machine sizes in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)

**Source reviewed:** 2026-08-31

## LAB11-Q08 — D

**Question:** A VM maintenance reviewer challenges whether the secured Linux VM maintenance window can change compute size when the destination cluster cannot resize the running machine in place. Which response resolves the concern?

- **A — Incorrect.** A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation.
  A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation. In the secured Linux VM maintenance window, this statement describes stopped and deallocated states. Resize deallocation governs secured Linux VM maintenance window; stopped and deallocated states cannot support resize deallocation when operators must change compute size when the destination cluster cannot resize the running machine in place.
- **B — Incorrect.** A VM network interface must reference a valid subnet and satisfy regional and attachment constraints.
  A VM network interface must reference a valid subnet and satisfy regional and attachment constraints. In the secured Linux VM maintenance window, this statement describes network interface dependency. Secured Linux VM maintenance window asks about resize deallocation; this network interface dependency choice leaves the resize deallocation explanation missing.
- **C — Incorrect.** Managed disk type and size determine supported performance, cost, and workload characteristics.
  Managed disk type and size determine supported performance, cost, and workload characteristics. In the secured Linux VM maintenance window, this statement describes managed disk performance tiers. The managed disk performance tiers statement accurately describes managed disk performance tiers; however, secured Linux VM maintenance window needs resize deallocation to change compute size when the destination cluster cannot resize the running machine in place; managed disk performance tiers cannot replace resize deallocation.
- **D — Correct.** Some VM resizes require deallocation when the target size is unavailable on the current cluster.
  The secured Linux VM maintenance window needs resize deallocation to change compute size when the destination cluster cannot resize the running machine in place; this option states the applicable resize deallocation rule: some VM resizes require deallocation when the target size is unavailable on the current cluster.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Resize an Azure virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm)

**Source reviewed:** 2026-08-31

## LAB11-Q09 — C

**Question:** The secured Linux VM maintenance window handoff omits the VM maintenance rule needed to end compute charges rather than only powering off inside the machine. Which statement should the team add?

- **A — Incorrect.** A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs.
  A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs. In the secured Linux VM maintenance window, this statement describes managed disk snapshots. Secured Linux VM maintenance window asks about stopped and deallocated states; this managed disk snapshots choice leaves the stopped and deallocated states explanation missing.
- **B — Incorrect.** Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption.
  Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption. In the secured Linux VM maintenance window, this statement describes encryption at host. The encryption at host statement accurately describes encryption at host; however, secured Linux VM maintenance window needs stopped and deallocated states to end compute charges rather than only powering off inside the machine; encryption at host cannot replace stopped and deallocated states.
- **C — Correct.** A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation.
  A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation. This stopped and deallocated states fact resolves the secured Linux VM maintenance window design question about how to end compute charges rather than only powering off inside the machine.
- **D — Incorrect.** A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest.
  A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest. In the secured Linux VM maintenance window, this statement describes attaching data disks. Stopped and deallocated states governs secured Linux VM maintenance window; attaching data disks cannot support stopped and deallocated states when operators must end compute charges rather than only powering off inside the machine.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Azure virtual machine states and billing status](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)

**Source reviewed:** 2026-08-31

## LAB11-Q10 — B

**Question:** A VM maintenance incident review of the secured Linux VM maintenance window depends on the ability to capture a point-in-time copy of a managed disk. Which platform description is reliable?

- **A — Incorrect.** A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms.
  A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms. In the secured Linux VM maintenance window, this statement describes virtual machine image selection. The virtual machine image selection statement accurately describes virtual machine image selection; however, secured Linux VM maintenance window needs managed disk snapshots to capture a point-in-time copy of a managed disk; virtual machine image selection cannot replace managed disk snapshots.
- **B — Correct.** A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs.
  A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs. For secured Linux VM maintenance window, managed disk snapshots supplies the service rule needed to capture a point-in-time copy of a managed disk.
- **C — Incorrect.** A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss.
  A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss. In the secured Linux VM maintenance window, this statement describes temporary disks. Managed disk snapshots governs secured Linux VM maintenance window; temporary disks cannot support managed disk snapshots when operators must capture a point-in-time copy of a managed disk.
- **D — Incorrect.** Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity.
  Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity. In the secured Linux VM maintenance window, this statement describes VM size availability. Secured Linux VM maintenance window asks about managed disk snapshots; this VM size availability choice leaves the managed disk snapshots explanation missing.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Tutorial - Manage Azure disks with the Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-disks)

**Source reviewed:** 2026-08-31

## LAB11-Q11 — D

**Question:** A VM maintenance ticket in the secured Linux VM maintenance window says to choose a regionally available Marketplace image reference. Which VM maintenance action completes the secured Linux VM maintenance window request with minimal change?

- **A — Incorrect.** Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile.
  Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. In the secured Linux VM maintenance window, this action changes encryption at host. Secured Linux VM maintenance window approved virtual machine image selection, not encryption at host; only the virtual machine image selection change can choose a regionally available Marketplace image reference.
- **B — Incorrect.** Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS.
  Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. In the secured Linux VM maintenance window, this action changes attaching data disks. Secured Linux VM maintenance window requires virtual machine image selection; changing attaching data disks leaves virtual machine image selection absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot choose a regionally available Marketplace image reference.
- **C — Incorrect.** Use deallocate when the lab must release compute billing and no workload state depends on host allocation.
  Use deallocate when the lab must release compute billing and no workload state depends on host allocation. In the secured Linux VM maintenance window, this action changes stopped and deallocated states. Stopped and deallocated states does not implement virtual machine image selection for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot choose a regionally available Marketplace image reference.
- **D — Correct.** Resolve an approved image URN and accept marketplace terms when the selected image requires them.
  Resolve an approved image URN and accept marketplace terms when the selected image requires them. The secured Linux VM maintenance window uses this virtual machine image selection operation to choose a regionally available Marketplace image reference within the approved scope.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Find Azure Marketplace image information with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage)

**Source reviewed:** 2026-08-31

## LAB11-Q12 — C

**Question:** The approach for the secured Linux VM maintenance window is approved, but the VM maintenance environment still cannot attach the virtual machine to the intended subnet through its network interface. Which implementation step closes the gap?

- **A — Incorrect.** Place durable application data on managed data disks or an external storage service.
  Place durable application data on managed data disks or an external storage service. In the secured Linux VM maintenance window, this action changes temporary disks. Secured Linux VM maintenance window requires network interface dependency; changing temporary disks leaves network interface dependency absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot attach the virtual machine to the intended subnet through its network interface.
- **B — Incorrect.** List available sizes for the VM and region before choosing the target SKU.
  List available sizes for the VM and region before choosing the target SKU. In the secured Linux VM maintenance window, this action changes VM size availability. VM size availability does not implement network interface dependency for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot attach the virtual machine to the intended subnet through its network interface.
- **C — Correct.** Create the subnet and NIC before attaching that NIC to the VM deployment.
  For the secured Linux VM maintenance window, the required network interface dependency action is: create the subnet and NIC before attaching that NIC to the VM deployment. It makes the environment able to attach the virtual machine to the intended subnet through its network interface.
- **D — Incorrect.** Quiesce the workload when required and create a snapshot from the intended managed disk ID.
  Quiesce the workload when required and create a snapshot from the intended managed disk ID. In the secured Linux VM maintenance window, this action changes managed disk snapshots. Secured Linux VM maintenance window approved network interface dependency, not managed disk snapshots; only the network interface dependency change can attach the virtual machine to the intended subnet through its network interface.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Create a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q13 — A

**Question:** The compute administrator maintaining a secured Linux VM may change the secured Linux VM maintenance window only to encrypt supported host caches and temporary storage at the compute host. Which VM maintenance action stays within that assignment?

- **A — Correct.** Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile.
  Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. This changes encryption at host in the secured Linux VM maintenance window, supplying the missing state needed to encrypt supported host caches and temporary storage at the compute host.
- **B — Incorrect.** Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs.
  Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. In the secured Linux VM maintenance window, this action changes managed disk performance tiers. Secured Linux VM maintenance window instead needs encryption at host: Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. The managed disk performance tiers action omits that encryption at host work.
- **C — Incorrect.** Plan downtime and deallocate the VM when an online resize path is not available.
  Plan downtime and deallocate the VM when an online resize path is not available. In the secured Linux VM maintenance window, this action changes resize deallocation. Secured Linux VM maintenance window approved encryption at host, not resize deallocation; only the encryption at host change can encrypt supported host caches and temporary storage at the compute host.
- **D — Incorrect.** Resolve an approved image URN and accept marketplace terms when the selected image requires them.
  Resolve an approved image URN and accept marketplace terms when the selected image requires them. In the secured Linux VM maintenance window, this action changes virtual machine image selection. Secured Linux VM maintenance window requires encryption at host; changing virtual machine image selection leaves encryption at host absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot encrypt supported host caches and temporary storage at the compute host.

**Objectives:** `CP-VM-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Encryption at host for Azure virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disks-enable-host-based-encryption-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q14 — B

**Question:** A VM maintenance dry run shows no secured Linux VM maintenance window command will keep durable workload data off the host-local scratch disk. Which action belongs before execution?

- **A — Incorrect.** Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS.
  Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. In the secured Linux VM maintenance window, this action changes attaching data disks. Secured Linux VM maintenance window instead needs temporary disks: Place durable application data on managed data disks or an external storage service. The attaching data disks action omits that temporary disks work.
- **B — Correct.** Place durable application data on managed data disks or an external storage service.
  The secured Linux VM maintenance window must keep durable workload data off the host-local scratch disk; this option performs its direct temporary disks change: place durable application data on managed data disks or an external storage service.
- **C — Incorrect.** Use deallocate when the lab must release compute billing and no workload state depends on host allocation.
  Use deallocate when the lab must release compute billing and no workload state depends on host allocation. In the secured Linux VM maintenance window, this action changes stopped and deallocated states. Secured Linux VM maintenance window requires temporary disks; changing stopped and deallocated states leaves temporary disks absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot keep durable workload data off the host-local scratch disk.
- **D — Incorrect.** Create the subnet and NIC before attaching that NIC to the VM deployment.
  Create the subnet and NIC before attaching that NIC to the VM deployment. In the secured Linux VM maintenance window, this action changes network interface dependency. Network interface dependency does not implement temporary disks for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot keep durable workload data off the host-local scratch disk.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Managed disks overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)

**Source reviewed:** 2026-08-31

## LAB11-Q15 — A

**Question:** For the secured Linux VM maintenance window, operators need to choose a managed disk tier that meets the workload's performance requirement. Which change realizes that requirement?

- **A — Correct.** Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs.
  Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. It is the least-change managed disk performance tiers path for the secured Linux VM maintenance window requirement to choose a managed disk tier that meets the workload's performance requirement.
- **B — Incorrect.** List available sizes for the VM and region before choosing the target SKU.
  List available sizes for the VM and region before choosing the target SKU. In the secured Linux VM maintenance window, this action changes VM size availability. Secured Linux VM maintenance window requires managed disk performance tiers; changing VM size availability leaves managed disk performance tiers absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot choose a managed disk tier that meets the workload's performance requirement.
- **C — Incorrect.** Quiesce the workload when required and create a snapshot from the intended managed disk ID.
  Quiesce the workload when required and create a snapshot from the intended managed disk ID. In the secured Linux VM maintenance window, this action changes managed disk snapshots. Managed disk snapshots does not implement managed disk performance tiers for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot choose a managed disk tier that meets the workload's performance requirement.
- **D — Incorrect.** Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile.
  Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. In the secured Linux VM maintenance window, this action changes encryption at host. Secured Linux VM maintenance window instead needs managed disk performance tiers: Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. The encryption at host action omits that managed disk performance tiers work.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Azure managed disk types](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

**Source reviewed:** 2026-08-31

## LAB11-Q16 — D

**Question:** Operators must automate the secured Linux VM maintenance window change needed to add persistent capacity without replacing the operating-system disk. Which VM maintenance operation belongs in the runbook?

- **A — Incorrect.** Plan downtime and deallocate the VM when an online resize path is not available.
  Plan downtime and deallocate the VM when an online resize path is not available. In the secured Linux VM maintenance window, this action changes resize deallocation. Secured Linux VM maintenance window requires attaching data disks; changing resize deallocation leaves attaching data disks absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot add persistent capacity without replacing the operating-system disk.
- **B — Incorrect.** Resolve an approved image URN and accept marketplace terms when the selected image requires them.
  Resolve an approved image URN and accept marketplace terms when the selected image requires them. In the secured Linux VM maintenance window, this action changes virtual machine image selection. Virtual machine image selection does not implement attaching data disks for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot add persistent capacity without replacing the operating-system disk.
- **C — Incorrect.** Place durable application data on managed data disks or an external storage service.
  Place durable application data on managed data disks or an external storage service. In the secured Linux VM maintenance window, this action changes temporary disks. Secured Linux VM maintenance window instead needs attaching data disks: Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. The temporary disks action omits that attaching data disks work.
- **D — Correct.** Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS.
  Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. In secured Linux VM maintenance window, applying attaching data disks is the scoped way to add persistent capacity without replacing the operating-system disk.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Add a data disk to a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/add-disk)

**Source reviewed:** 2026-08-31

## LAB11-Q17 — C

**Question:** A secured Linux VM maintenance window review finds VM maintenance drift from the need to confirm that the requested compute shape is offered in the deployment region. Which correction addresses that drift?

- **A — Incorrect.** Use deallocate when the lab must release compute billing and no workload state depends on host allocation.
  Use deallocate when the lab must release compute billing and no workload state depends on host allocation. In the secured Linux VM maintenance window, this action changes stopped and deallocated states. Stopped and deallocated states does not implement VM size availability for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot confirm that the requested compute shape is offered in the deployment region.
- **B — Incorrect.** Create the subnet and NIC before attaching that NIC to the VM deployment.
  Create the subnet and NIC before attaching that NIC to the VM deployment. In the secured Linux VM maintenance window, this action changes network interface dependency. Secured Linux VM maintenance window instead needs VM size availability: List available sizes for the VM and region before choosing the target SKU. The network interface dependency action omits that VM size availability work.
- **C — Correct.** List available sizes for the VM and region before choosing the target SKU.
  List available sizes for the VM and region before choosing the target SKU. The secured Linux VM maintenance window uses this VM size availability operation to confirm that the requested compute shape is offered in the deployment region within the approved scope.
- **D — Incorrect.** Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs.
  Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. In the secured Linux VM maintenance window, this action changes managed disk performance tiers. Secured Linux VM maintenance window requires VM size availability; changing managed disk performance tiers leaves VM size availability absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot confirm that the requested compute shape is offered in the deployment region.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Virtual machine sizes in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)

**Source reviewed:** 2026-08-31

## LAB11-Q18 — B

**Question:** The secured Linux VM maintenance window window permits only the VM maintenance change needed to change compute size when the destination cluster cannot resize the running machine in place. Which option respects the boundary?

- **A — Incorrect.** Quiesce the workload when required and create a snapshot from the intended managed disk ID.
  Quiesce the workload when required and create a snapshot from the intended managed disk ID. In the secured Linux VM maintenance window, this action changes managed disk snapshots. Secured Linux VM maintenance window instead needs resize deallocation: Plan downtime and deallocate the VM when an online resize path is not available. The managed disk snapshots action omits that resize deallocation work.
- **B — Correct.** Plan downtime and deallocate the VM when an online resize path is not available.
  For the secured Linux VM maintenance window, the required resize deallocation action is: plan downtime and deallocate the VM when an online resize path is not available. It makes the environment able to change compute size when the destination cluster cannot resize the running machine in place.
- **C — Incorrect.** Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile.
  Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. In the secured Linux VM maintenance window, this action changes encryption at host. Secured Linux VM maintenance window requires resize deallocation; changing encryption at host leaves resize deallocation absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot change compute size when the destination cluster cannot resize the running machine in place.
- **D — Incorrect.** Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS.
  Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. In the secured Linux VM maintenance window, this action changes attaching data disks. Attaching data disks does not implement resize deallocation for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot change compute size when the destination cluster cannot resize the running machine in place.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Resize an Azure virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm)

**Source reviewed:** 2026-08-31

## LAB11-Q19 — A

**Question:** The VM maintenance preflight has passed; the secured Linux VM maintenance window must now end compute charges rather than only powering off inside the machine. Which operation should run?

- **A — Correct.** Use deallocate when the lab must release compute billing and no workload state depends on host allocation.
  Use deallocate when the lab must release compute billing and no workload state depends on host allocation. This changes stopped and deallocated states in the secured Linux VM maintenance window, supplying the missing state needed to end compute charges rather than only powering off inside the machine.
- **B — Incorrect.** Resolve an approved image URN and accept marketplace terms when the selected image requires them.
  Resolve an approved image URN and accept marketplace terms when the selected image requires them. In the secured Linux VM maintenance window, this action changes virtual machine image selection. Secured Linux VM maintenance window requires stopped and deallocated states; changing virtual machine image selection leaves stopped and deallocated states absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot end compute charges rather than only powering off inside the machine.
- **C — Incorrect.** Place durable application data on managed data disks or an external storage service.
  Place durable application data on managed data disks or an external storage service. In the secured Linux VM maintenance window, this action changes temporary disks. Temporary disks does not implement stopped and deallocated states for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot end compute charges rather than only powering off inside the machine.
- **D — Incorrect.** List available sizes for the VM and region before choosing the target SKU.
  List available sizes for the VM and region before choosing the target SKU. In the secured Linux VM maintenance window, this action changes VM size availability. Secured Linux VM maintenance window instead needs stopped and deallocated states: Use deallocate when the lab must release compute billing and no workload state depends on host allocation. The VM size availability action omits that stopped and deallocated states work.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Azure virtual machine states and billing status](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)

**Source reviewed:** 2026-08-31

## LAB11-Q20 — C

**Question:** The secured Linux VM maintenance window plan must capture a point-in-time copy of a managed disk while limiting the mutation scope to VM maintenance. Which action is appropriate?

- **A — Incorrect.** Create the subnet and NIC before attaching that NIC to the VM deployment.
  Create the subnet and NIC before attaching that NIC to the VM deployment. In the secured Linux VM maintenance window, this action changes network interface dependency. Secured Linux VM maintenance window requires managed disk snapshots; changing network interface dependency leaves managed disk snapshots absent in secured Linux VM maintenance window; secured Linux VM maintenance window cannot capture a point-in-time copy of a managed disk.
- **B — Incorrect.** Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs.
  Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. In the secured Linux VM maintenance window, this action changes managed disk performance tiers. Managed disk performance tiers does not implement managed disk snapshots for secured Linux VM maintenance window; the secured Linux VM maintenance window still cannot capture a point-in-time copy of a managed disk.
- **C — Correct.** Quiesce the workload when required and create a snapshot from the intended managed disk ID.
  The secured Linux VM maintenance window must capture a point-in-time copy of a managed disk; this option performs its direct managed disk snapshots change: quiesce the workload when required and create a snapshot from the intended managed disk ID.
- **D — Incorrect.** Plan downtime and deallocate the VM when an online resize path is not available.
  Plan downtime and deallocate the VM when an online resize path is not available. In the secured Linux VM maintenance window, this action changes resize deallocation. Secured Linux VM maintenance window approved managed disk snapshots, not resize deallocation; only the managed disk snapshots change can capture a point-in-time copy of a managed disk.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Tutorial - Manage Azure disks with the Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-disks)

**Source reviewed:** 2026-08-31

## LAB11-Q21 — B

**Question:** The secured Linux VM maintenance window setup reports success after the VM maintenance attempt to choose a regionally available Marketplace image reference. Which VM maintenance read-only observation proves the secured Linux VM maintenance window outcome?

- **A — Incorrect.** Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
  Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks. In the secured Linux VM maintenance window, this check observes temporary disks. Secured Linux VM maintenance window output covers temporary disks, not virtual machine image selection; the virtual machine image selection requirement to choose a regionally available Marketplace image reference remains unverified.
- **B — Correct.** Query storageProfile.imageReference and confirm every image component matches the approved baseline.
  Query storageProfile.imageReference and confirm every image component matches the approved baseline. This is independent virtual machine image selection evidence for the secured Linux VM maintenance window, even if secured Linux VM maintenance window setup reports success before virtual machine image selection becomes observable.
- **C — Incorrect.** Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
  Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU. In the secured Linux VM maintenance window, this check observes VM size availability. Secured Linux VM maintenance window reads VM size availability, leaving virtual machine image selection unproved in secured Linux VM maintenance window; secured Linux VM maintenance window still has no virtual machine image selection proof.
- **D — Incorrect.** Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
  Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState. In the secured Linux VM maintenance window, this check observes managed disk snapshots. Secured Linux VM maintenance window could pass managed disk snapshots while virtual machine image selection is wrong; secured Linux VM maintenance window still lacks virtual machine image selection proof.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Find Azure Marketplace image information with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage)

**Source reviewed:** 2026-08-31

## LAB11-Q22 — A

**Question:** The VM maintenance log says the secured Linux VM maintenance window can now attach the virtual machine to the intended subnet through its network interface. Which VM maintenance state should the secured Linux VM maintenance window acceptance test retain?

- **A — Correct.** Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
  Query the VM networkProfile and resolve its NIC and IP configuration resource IDs. For secured Linux VM maintenance window, this network interface dependency read confirms the service can attach the virtual machine to the intended subnet through its network interface.
- **B — Incorrect.** Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
  Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values. In the secured Linux VM maintenance window, this check observes managed disk performance tiers. Secured Linux VM maintenance window reads managed disk performance tiers, leaving network interface dependency unproved in secured Linux VM maintenance window; secured Linux VM maintenance window still has no network interface dependency proof.
- **C — Incorrect.** Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
  Read powerState and hardwareProfile.vmSize after the resize and restart sequence. In the secured Linux VM maintenance window, this check observes resize deallocation. Secured Linux VM maintenance window could pass resize deallocation while network interface dependency is wrong; secured Linux VM maintenance window still lacks network interface dependency proof.
- **D — Incorrect.** Query storageProfile.imageReference and confirm every image component matches the approved baseline.
  Query storageProfile.imageReference and confirm every image component matches the approved baseline. In the secured Linux VM maintenance window, this check observes virtual machine image selection. Secured Linux VM maintenance window output covers virtual machine image selection, not network interface dependency; the network interface dependency requirement to attach the virtual machine to the intended subnet through its network interface remains unverified.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Create a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q23 — C

**Question:** The secured Linux VM maintenance window rejects VM maintenance exit status as proof it can encrypt supported host caches and temporary storage at the compute host. Which secured Linux VM maintenance window result is valid evidence?

- **A — Incorrect.** Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
  Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state. In the secured Linux VM maintenance window, this check observes attaching data disks. Secured Linux VM maintenance window reads attaching data disks, leaving encryption at host unproved in secured Linux VM maintenance window; secured Linux VM maintenance window still has no encryption at host proof.
- **B — Incorrect.** Query instanceView power state and confirm it reports VM deallocated.
  Query instanceView power state and confirm it reports VM deallocated. In the secured Linux VM maintenance window, this check observes stopped and deallocated states. Secured Linux VM maintenance window could pass stopped and deallocated states while encryption at host is wrong; secured Linux VM maintenance window still lacks encryption at host proof.
- **C — Correct.** Query securityProfile.encryptionAtHost and verify it is true on the running VM.
  Query securityProfile.encryptionAtHost and verify it is true on the running VM. The secured Linux VM maintenance window reads encryption at host directly; that encryption at host result proves the secured Linux VM maintenance window can encrypt supported host caches and temporary storage at the compute host without another mutation.
- **D — Incorrect.** Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
  Query the VM networkProfile and resolve its NIC and IP configuration resource IDs. In the secured Linux VM maintenance window, this check observes network interface dependency. Network interface dependency success in secured Linux VM maintenance window cannot verify encryption at host; secured Linux VM maintenance window cannot encrypt supported host caches and temporary storage at the compute host until encryption at host evidence exists.

**Objectives:** `CP-VM-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Encryption at host for Azure virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disks-enable-host-based-encryption-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q24 — A

**Question:** The VM maintenance validator needs one secured Linux VM maintenance window query after the change to keep durable workload data off the host-local scratch disk. Which VM maintenance property should the secured Linux VM maintenance window validator inspect?

- **A — Correct.** Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
  For the secured Linux VM maintenance window, this temporary disks observation is decisive: inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks. It is secured Linux VM maintenance window evidence that operators can keep durable workload data off the host-local scratch disk.
- **B — Incorrect.** Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
  Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU. In the secured Linux VM maintenance window, this check observes VM size availability. Secured Linux VM maintenance window output covers VM size availability, not temporary disks; the temporary disks requirement to keep durable workload data off the host-local scratch disk remains unverified.
- **C — Incorrect.** Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
  Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState. In the secured Linux VM maintenance window, this check observes managed disk snapshots. Managed disk snapshots success in secured Linux VM maintenance window cannot verify temporary disks; secured Linux VM maintenance window cannot keep durable workload data off the host-local scratch disk until temporary disks evidence exists.
- **D — Incorrect.** Query securityProfile.encryptionAtHost and verify it is true on the running VM.
  Query securityProfile.encryptionAtHost and verify it is true on the running VM. In the secured Linux VM maintenance window, this check observes encryption at host. Secured Linux VM maintenance window reads encryption at host, leaving temporary disks unproved in secured Linux VM maintenance window; secured Linux VM maintenance window still has no temporary disks proof.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Managed disks overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)

**Source reviewed:** 2026-08-31

## LAB11-Q25 — C

**Question:** The compute administrator maintaining a secured Linux VM must confirm the secured Linux VM maintenance window, without mutation, can choose a managed disk tier that meets the workload's performance requirement. Which VM maintenance check qualifies?

- **A — Incorrect.** Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
  Read powerState and hardwareProfile.vmSize after the resize and restart sequence. In the secured Linux VM maintenance window, this check observes resize deallocation. Secured Linux VM maintenance window output covers resize deallocation, not managed disk performance tiers; the managed disk performance tiers requirement to choose a managed disk tier that meets the workload's performance requirement remains unverified.
- **B — Incorrect.** Query storageProfile.imageReference and confirm every image component matches the approved baseline.
  Query storageProfile.imageReference and confirm every image component matches the approved baseline. In the secured Linux VM maintenance window, this check observes virtual machine image selection. Virtual machine image selection success in secured Linux VM maintenance window cannot verify managed disk performance tiers; secured Linux VM maintenance window cannot choose a managed disk tier that meets the workload's performance requirement until managed disk performance tiers evidence exists.
- **C — Correct.** Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
  Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values. Because the secured Linux VM maintenance window check observes managed disk performance tiers, it independently verifies the requirement to choose a managed disk tier that meets the workload's performance requirement.
- **D — Incorrect.** Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
  Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks. In the secured Linux VM maintenance window, this check observes temporary disks. Secured Linux VM maintenance window could pass temporary disks while managed disk performance tiers is wrong; secured Linux VM maintenance window still lacks managed disk performance tiers proof.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Azure managed disk types](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

**Source reviewed:** 2026-08-31

## LAB11-Q26 — C

**Question:** The secured Linux VM maintenance window configuration is complete; the VM maintenance reviewers need evidence it can add persistent capacity without replacing the operating-system disk. Which observation shows success?

- **A — Incorrect.** Query instanceView power state and confirm it reports VM deallocated.
  Query instanceView power state and confirm it reports VM deallocated. In the secured Linux VM maintenance window, this check observes stopped and deallocated states. Stopped and deallocated states success in secured Linux VM maintenance window cannot verify attaching data disks; secured Linux VM maintenance window cannot add persistent capacity without replacing the operating-system disk until attaching data disks evidence exists.
- **B — Incorrect.** Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
  Query the VM networkProfile and resolve its NIC and IP configuration resource IDs. In the secured Linux VM maintenance window, this check observes network interface dependency. Secured Linux VM maintenance window reads network interface dependency, leaving attaching data disks unproved in secured Linux VM maintenance window; secured Linux VM maintenance window still has no attaching data disks proof.
- **C — Correct.** Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
  The secured Linux VM maintenance window validator needs this attaching data disks result: query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state. It proves the outcome to add persistent capacity without replacing the operating-system disk rather than an adjacent checkpoint.
- **D — Incorrect.** Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
  Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values. In the secured Linux VM maintenance window, this check observes managed disk performance tiers. Secured Linux VM maintenance window output covers managed disk performance tiers, not attaching data disks; the attaching data disks requirement to add persistent capacity without replacing the operating-system disk remains unverified.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Add a data disk to a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/add-disk)

**Source reviewed:** 2026-08-31

## LAB11-Q27 — B

**Question:** The VM maintenance validation asks whether the secured Linux VM maintenance window can confirm that the requested compute shape is offered in the deployment region. Which observable state is strongest?

- **A — Incorrect.** Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
  Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState. In the secured Linux VM maintenance window, this check observes managed disk snapshots. Secured Linux VM maintenance window reads managed disk snapshots, leaving VM size availability unproved in secured Linux VM maintenance window; secured Linux VM maintenance window still has no VM size availability proof.
- **B — Correct.** Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
  Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU. This is independent VM size availability evidence for the secured Linux VM maintenance window, even if secured Linux VM maintenance window setup reports success before VM size availability becomes observable.
- **C — Incorrect.** Query securityProfile.encryptionAtHost and verify it is true on the running VM.
  Query securityProfile.encryptionAtHost and verify it is true on the running VM. In the secured Linux VM maintenance window, this check observes encryption at host. Secured Linux VM maintenance window output covers encryption at host, not VM size availability; the VM size availability requirement to confirm that the requested compute shape is offered in the deployment region remains unverified.
- **D — Incorrect.** Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
  Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state. In the secured Linux VM maintenance window, this check observes attaching data disks. Attaching data disks success in secured Linux VM maintenance window cannot verify VM size availability; secured Linux VM maintenance window cannot confirm that the requested compute shape is offered in the deployment region until VM size availability evidence exists.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Virtual machine sizes in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)

**Source reviewed:** 2026-08-31

## LAB11-Q28 — C

**Question:** A secured Linux VM maintenance window review must prove the VM maintenance ability to change compute size when the destination cluster cannot resize the running machine in place. Which check avoids an adjacent feature?

- **A — Incorrect.** Query storageProfile.imageReference and confirm every image component matches the approved baseline.
  Query storageProfile.imageReference and confirm every image component matches the approved baseline. In the secured Linux VM maintenance window, this check observes virtual machine image selection. Secured Linux VM maintenance window could pass virtual machine image selection while resize deallocation is wrong; secured Linux VM maintenance window still lacks resize deallocation proof.
- **B — Incorrect.** Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
  Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks. In the secured Linux VM maintenance window, this check observes temporary disks. Secured Linux VM maintenance window output covers temporary disks, not resize deallocation; the resize deallocation requirement to change compute size when the destination cluster cannot resize the running machine in place remains unverified.
- **C — Correct.** Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
  Read powerState and hardwareProfile.vmSize after the resize and restart sequence. For secured Linux VM maintenance window, this resize deallocation read confirms the service can change compute size when the destination cluster cannot resize the running machine in place.
- **D — Incorrect.** Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
  Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU. In the secured Linux VM maintenance window, this check observes VM size availability. Secured Linux VM maintenance window reads VM size availability, leaving resize deallocation unproved in secured Linux VM maintenance window; secured Linux VM maintenance window still has no resize deallocation proof.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Resize an Azure virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm)

**Source reviewed:** 2026-08-31

## LAB11-Q29 — C

**Question:** The secured Linux VM maintenance window evidence bundle needs a VM maintenance result showing it can end compute charges rather than only powering off inside the machine. Which result belongs in the checkpoint?

- **A — Incorrect.** Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
  Query the VM networkProfile and resolve its NIC and IP configuration resource IDs. In the secured Linux VM maintenance window, this check observes network interface dependency. Secured Linux VM maintenance window output covers network interface dependency, not stopped and deallocated states; the stopped and deallocated states requirement to end compute charges rather than only powering off inside the machine remains unverified.
- **B — Incorrect.** Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
  Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values. In the secured Linux VM maintenance window, this check observes managed disk performance tiers. Managed disk performance tiers success in secured Linux VM maintenance window cannot verify stopped and deallocated states; secured Linux VM maintenance window cannot end compute charges rather than only powering off inside the machine until stopped and deallocated states evidence exists.
- **C — Correct.** Query instanceView power state and confirm it reports VM deallocated.
  Query instanceView power state and confirm it reports VM deallocated. The secured Linux VM maintenance window reads stopped and deallocated states directly; that stopped and deallocated states result proves the secured Linux VM maintenance window can end compute charges rather than only powering off inside the machine without another mutation.
- **D — Incorrect.** Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
  Read powerState and hardwareProfile.vmSize after the resize and restart sequence. In the secured Linux VM maintenance window, this check observes resize deallocation. Secured Linux VM maintenance window could pass resize deallocation while stopped and deallocated states is wrong; secured Linux VM maintenance window still lacks stopped and deallocated states proof.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Azure virtual machine states and billing status](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)

**Source reviewed:** 2026-08-31

## LAB11-Q30 — B

**Question:** Before secured Linux VM maintenance window cleanup, the VM maintenance team must reconfirm it can capture a point-in-time copy of a managed disk. Which read-only inspection should run?

- **A — Incorrect.** Query securityProfile.encryptionAtHost and verify it is true on the running VM.
  Query securityProfile.encryptionAtHost and verify it is true on the running VM. In the secured Linux VM maintenance window, this check observes encryption at host. Encryption at host success in secured Linux VM maintenance window cannot verify managed disk snapshots; secured Linux VM maintenance window cannot capture a point-in-time copy of a managed disk until managed disk snapshots evidence exists.
- **B — Correct.** Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
  For the secured Linux VM maintenance window, this managed disk snapshots observation is decisive: query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState. It is secured Linux VM maintenance window evidence that operators can capture a point-in-time copy of a managed disk.
- **C — Incorrect.** Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
  Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state. In the secured Linux VM maintenance window, this check observes attaching data disks. Secured Linux VM maintenance window could pass attaching data disks while managed disk snapshots is wrong; secured Linux VM maintenance window still lacks managed disk snapshots proof.
- **D — Incorrect.** Query instanceView power state and confirm it reports VM deallocated.
  Query instanceView power state and confirm it reports VM deallocated. In the secured Linux VM maintenance window, this check observes stopped and deallocated states. Secured Linux VM maintenance window output covers stopped and deallocated states, not managed disk snapshots; the managed disk snapshots requirement to capture a point-in-time copy of a managed disk remains unverified.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Tutorial - Manage Azure disks with the Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-disks)

**Source reviewed:** 2026-08-31

## LAB11-Q31 — D

**Question:** During a VM maintenance fault drill, the secured Linux VM maintenance window does not choose a regionally available Marketplace image reference. Which finding identifies the defect?

- **A — Incorrect.** The NIC resides in a different region from the virtual machine.
  The NIC resides in a different region from the virtual machine. The secured Linux VM maintenance window fault concerns network interface dependency. Secured Linux VM maintenance window has network interface dependency impact, but virtual machine image selection is the secured Linux VM maintenance window failed path; the network interface dependency state cannot produce virtual machine image selection failure.
- **B — Incorrect.** Two requested data disks use the same LUN on one virtual machine.
  Two requested data disks use the same LUN on one virtual machine. The secured Linux VM maintenance window fault concerns attaching data disks. Secured Linux VM maintenance window could repair attaching data disks while virtual machine image selection stays broken in secured Linux VM maintenance window; the secured Linux VM maintenance window remains unable to choose a regionally available Marketplace image reference.
- **C — Incorrect.** The snapshot source ID points to the OS disk instead of the intended data disk.
  The snapshot source ID points to the OS disk instead of the intended data disk. The secured Linux VM maintenance window fault concerns managed disk snapshots. Secured Linux VM maintenance window failed on virtual machine image selection; this managed disk snapshots finding redirects secured Linux VM maintenance window remediation away from virtual machine image selection.
- **D — Correct.** The selected marketplace image requires plan information that the deployment omitted.
  The selected marketplace image requires plan information that the deployment omitted. The finding is specific to virtual machine image selection in the secured Linux VM maintenance window; repairing virtual machine image selection restores the secured Linux VM maintenance window ability to choose a regionally available Marketplace image reference.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Find Azure Marketplace image information with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage)

**Source reviewed:** 2026-08-31

## LAB11-Q32 — D

**Question:** The secured Linux VM maintenance window setup finishes, yet the VM maintenance cannot attach the virtual machine to the intended subnet through its network interface. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The selected VM size or subscription is not enabled for encryption at host.
  The selected VM size or subscription is not enabled for encryption at host. The secured Linux VM maintenance window fault concerns encryption at host. Secured Linux VM maintenance window could repair encryption at host while network interface dependency stays broken in secured Linux VM maintenance window; the secured Linux VM maintenance window remains unable to attach the virtual machine to the intended subnet through its network interface.
- **B — Incorrect.** The requested size is not available on the current hardware cluster.
  The requested size is not available on the current hardware cluster. The secured Linux VM maintenance window fault concerns VM size availability. Secured Linux VM maintenance window failed on network interface dependency; this VM size availability finding redirects secured Linux VM maintenance window remediation away from network interface dependency.
- **C — Incorrect.** The selected marketplace image requires plan information that the deployment omitted.
  The selected marketplace image requires plan information that the deployment omitted. The secured Linux VM maintenance window fault concerns virtual machine image selection. Secured Linux VM maintenance window may fix virtual machine image selection, yet network interface dependency still fails; this secured Linux VM maintenance window diagnosis of virtual machine image selection is wrong for network interface dependency.
- **D — Correct.** The NIC resides in a different region from the virtual machine.
  The secured Linux VM maintenance window cannot attach the virtual machine to the intended subnet through its network interface because of this network interface dependency defect: the NIC resides in a different region from the virtual machine. The symptom and repair align.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Create a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q33 — C

**Question:** A VM maintenance break/fix in the secured Linux VM maintenance window fails when operators try to encrypt supported host caches and temporary storage at the compute host. Which diagnosis fits?

- **A — Incorrect.** The application wrote its only database copy to the temporary disk.
  The application wrote its only database copy to the temporary disk. The secured Linux VM maintenance window fault concerns temporary disks. Secured Linux VM maintenance window failed on encryption at host; this temporary disks finding redirects secured Linux VM maintenance window remediation away from encryption at host.
- **B — Incorrect.** The runbook attempts an online resize to a SKU unavailable on the VM's current cluster.
  The runbook attempts an online resize to a SKU unavailable on the VM's current cluster. The secured Linux VM maintenance window fault concerns resize deallocation. Secured Linux VM maintenance window may fix resize deallocation, yet encryption at host still fails; this secured Linux VM maintenance window diagnosis of resize deallocation is wrong for encryption at host.
- **C — Correct.** The selected VM size or subscription is not enabled for encryption at host.
  The selected VM size or subscription is not enabled for encryption at host. Removing this encryption at host condition lets the secured Linux VM maintenance window encrypt supported host caches and temporary storage at the compute host while leaving healthy controls unchanged.
- **D — Incorrect.** The NIC resides in a different region from the virtual machine.
  The NIC resides in a different region from the virtual machine. The secured Linux VM maintenance window fault concerns network interface dependency. Secured Linux VM maintenance window could repair network interface dependency while encryption at host stays broken in secured Linux VM maintenance window; the secured Linux VM maintenance window remains unable to encrypt supported host caches and temporary storage at the compute host.

**Objectives:** `CP-VM-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Encryption at host for Azure virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disks-enable-host-based-encryption-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q34 — C

**Question:** The secured Linux VM maintenance window troubleshooting scope is the VM maintenance need to keep durable workload data off the host-local scratch disk. Which condition should be corrected first?

- **A — Incorrect.** The disk SKU cannot deliver the required IOPS for the workload.
  The disk SKU cannot deliver the required IOPS for the workload. The secured Linux VM maintenance window fault concerns managed disk performance tiers. Secured Linux VM maintenance window may fix managed disk performance tiers, yet temporary disks still fails; this secured Linux VM maintenance window diagnosis of managed disk performance tiers is wrong for temporary disks.
- **B — Incorrect.** The guest operating system shut down, but Azure still reports the VM as allocated.
  The guest operating system shut down, but Azure still reports the VM as allocated. The secured Linux VM maintenance window fault concerns stopped and deallocated states. Secured Linux VM maintenance window has stopped and deallocated states impact, but temporary disks is the secured Linux VM maintenance window failed path; the stopped and deallocated states state cannot produce temporary disks failure.
- **C — Correct.** The application wrote its only database copy to the temporary disk.
  The application wrote its only database copy to the temporary disk. In secured Linux VM maintenance window, this temporary disks cause matches the failure to keep durable workload data off the host-local scratch disk.
- **D — Incorrect.** The selected VM size or subscription is not enabled for encryption at host.
  The selected VM size or subscription is not enabled for encryption at host. The secured Linux VM maintenance window fault concerns encryption at host. Secured Linux VM maintenance window failed on temporary disks; this encryption at host finding redirects secured Linux VM maintenance window remediation away from temporary disks.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Managed disks overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)

**Source reviewed:** 2026-08-31

## LAB11-Q35 — A

**Question:** The secured Linux VM maintenance window result is partial because the VM maintenance cannot choose a managed disk tier that meets the workload's performance requirement. Which condition accounts for that result?

- **A — Correct.** The disk SKU cannot deliver the required IOPS for the workload.
  The disk SKU cannot deliver the required IOPS for the workload. This secured Linux VM maintenance window condition breaks managed disk performance tiers, explaining why operators cannot choose a managed disk tier that meets the workload's performance requirement.
- **B — Incorrect.** Two requested data disks use the same LUN on one virtual machine.
  Two requested data disks use the same LUN on one virtual machine. The secured Linux VM maintenance window fault concerns attaching data disks. Secured Linux VM maintenance window could repair attaching data disks while managed disk performance tiers stays broken in secured Linux VM maintenance window; the secured Linux VM maintenance window remains unable to choose a managed disk tier that meets the workload's performance requirement.
- **C — Incorrect.** The snapshot source ID points to the OS disk instead of the intended data disk.
  The snapshot source ID points to the OS disk instead of the intended data disk. The secured Linux VM maintenance window fault concerns managed disk snapshots. Secured Linux VM maintenance window failed on managed disk performance tiers; this managed disk snapshots finding redirects secured Linux VM maintenance window remediation away from managed disk performance tiers.
- **D — Incorrect.** The application wrote its only database copy to the temporary disk.
  The application wrote its only database copy to the temporary disk. The secured Linux VM maintenance window fault concerns temporary disks. Secured Linux VM maintenance window may fix temporary disks, yet managed disk performance tiers still fails; this secured Linux VM maintenance window diagnosis of temporary disks is wrong for managed disk performance tiers.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Azure managed disk types](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

**Source reviewed:** 2026-08-31

## LAB11-Q36 — D

**Question:** The VM maintenance evidence shows the secured Linux VM maintenance window cannot add persistent capacity without replacing the operating-system disk. Which root cause fits that evidence?

- **A — Incorrect.** The requested size is not available on the current hardware cluster.
  The requested size is not available on the current hardware cluster. The secured Linux VM maintenance window fault concerns VM size availability. Secured Linux VM maintenance window could repair VM size availability while attaching data disks stays broken in secured Linux VM maintenance window; the secured Linux VM maintenance window remains unable to add persistent capacity without replacing the operating-system disk.
- **B — Incorrect.** The selected marketplace image requires plan information that the deployment omitted.
  The selected marketplace image requires plan information that the deployment omitted. The secured Linux VM maintenance window fault concerns virtual machine image selection. Secured Linux VM maintenance window failed on attaching data disks; this virtual machine image selection finding redirects secured Linux VM maintenance window remediation away from attaching data disks.
- **C — Incorrect.** The disk SKU cannot deliver the required IOPS for the workload.
  The disk SKU cannot deliver the required IOPS for the workload. The secured Linux VM maintenance window fault concerns managed disk performance tiers. Secured Linux VM maintenance window may fix managed disk performance tiers, yet attaching data disks still fails; this secured Linux VM maintenance window diagnosis of managed disk performance tiers is wrong for attaching data disks.
- **D — Correct.** Two requested data disks use the same LUN on one virtual machine.
  For the secured Linux VM maintenance window, the attaching data disks failure is causal: two requested data disks use the same LUN on one virtual machine. Correcting it restores the ability to add persistent capacity without replacing the operating-system disk.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Add a data disk to a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/add-disk)

**Source reviewed:** 2026-08-31

## LAB11-Q37 — A

**Question:** Although the secured Linux VM maintenance window is meant to let the VM maintenance confirm that the requested compute shape is offered in the deployment region, its checkpoint fails. Which VM maintenance defect explains the failure?

- **A — Correct.** The requested size is not available on the current hardware cluster.
  The requested size is not available on the current hardware cluster. The finding is specific to VM size availability in the secured Linux VM maintenance window; repairing VM size availability restores the secured Linux VM maintenance window ability to confirm that the requested compute shape is offered in the deployment region.
- **B — Incorrect.** The runbook attempts an online resize to a SKU unavailable on the VM's current cluster.
  The runbook attempts an online resize to a SKU unavailable on the VM's current cluster. The secured Linux VM maintenance window fault concerns resize deallocation. Secured Linux VM maintenance window may fix resize deallocation, yet VM size availability still fails; this secured Linux VM maintenance window diagnosis of resize deallocation is wrong for VM size availability.
- **C — Incorrect.** The NIC resides in a different region from the virtual machine.
  The NIC resides in a different region from the virtual machine. The secured Linux VM maintenance window fault concerns network interface dependency. Secured Linux VM maintenance window has network interface dependency impact, but VM size availability is the secured Linux VM maintenance window failed path; the network interface dependency state cannot produce VM size availability failure.
- **D — Incorrect.** Two requested data disks use the same LUN on one virtual machine.
  Two requested data disks use the same LUN on one virtual machine. The secured Linux VM maintenance window fault concerns attaching data disks. Secured Linux VM maintenance window could repair attaching data disks while VM size availability stays broken in secured Linux VM maintenance window; the secured Linux VM maintenance window remains unable to confirm that the requested compute shape is offered in the deployment region.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Virtual machine sizes in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)

**Source reviewed:** 2026-08-31

## LAB11-Q38 — D

**Question:** The VM maintenance support team isolated the secured Linux VM maintenance window incident to the attempt to change compute size when the destination cluster cannot resize the running machine in place. Which condition prevents success?

- **A — Incorrect.** The guest operating system shut down, but Azure still reports the VM as allocated.
  The guest operating system shut down, but Azure still reports the VM as allocated. The secured Linux VM maintenance window fault concerns stopped and deallocated states. Secured Linux VM maintenance window may fix stopped and deallocated states, yet resize deallocation still fails; this secured Linux VM maintenance window diagnosis of stopped and deallocated states is wrong for resize deallocation.
- **B — Incorrect.** The selected VM size or subscription is not enabled for encryption at host.
  The selected VM size or subscription is not enabled for encryption at host. The secured Linux VM maintenance window fault concerns encryption at host. Secured Linux VM maintenance window has encryption at host impact, but resize deallocation is the secured Linux VM maintenance window failed path; the encryption at host state cannot produce resize deallocation failure.
- **C — Incorrect.** The requested size is not available on the current hardware cluster.
  The requested size is not available on the current hardware cluster. The secured Linux VM maintenance window fault concerns VM size availability. Secured Linux VM maintenance window could repair VM size availability while resize deallocation stays broken in secured Linux VM maintenance window; the secured Linux VM maintenance window remains unable to change compute size when the destination cluster cannot resize the running machine in place.
- **D — Correct.** The runbook attempts an online resize to a SKU unavailable on the VM's current cluster.
  The secured Linux VM maintenance window cannot change compute size when the destination cluster cannot resize the running machine in place because of this resize deallocation defect: the runbook attempts an online resize to a SKU unavailable on the VM's current cluster. The symptom and repair align.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Resize an Azure virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm)

**Source reviewed:** 2026-08-31

## LAB11-Q39 — D

**Question:** A secured Linux VM maintenance window query surprises the compute administrator maintaining a secured Linux VM during the VM maintenance attempt to end compute charges rather than only powering off inside the machine. Which finding explains it?

- **A — Incorrect.** The snapshot source ID points to the OS disk instead of the intended data disk.
  The snapshot source ID points to the OS disk instead of the intended data disk. The secured Linux VM maintenance window fault concerns managed disk snapshots. Secured Linux VM maintenance window has managed disk snapshots impact, but stopped and deallocated states is the secured Linux VM maintenance window failed path; the managed disk snapshots state cannot produce stopped and deallocated states failure.
- **B — Incorrect.** The application wrote its only database copy to the temporary disk.
  The application wrote its only database copy to the temporary disk. The secured Linux VM maintenance window fault concerns temporary disks. Secured Linux VM maintenance window could repair temporary disks while stopped and deallocated states stays broken in secured Linux VM maintenance window; the secured Linux VM maintenance window remains unable to end compute charges rather than only powering off inside the machine.
- **C — Incorrect.** The runbook attempts an online resize to a SKU unavailable on the VM's current cluster.
  The runbook attempts an online resize to a SKU unavailable on the VM's current cluster. The secured Linux VM maintenance window fault concerns resize deallocation. Secured Linux VM maintenance window failed on stopped and deallocated states; this resize deallocation finding redirects secured Linux VM maintenance window remediation away from stopped and deallocated states.
- **D — Correct.** The guest operating system shut down, but Azure still reports the VM as allocated.
  The guest operating system shut down, but Azure still reports the VM as allocated. Removing this stopped and deallocated states condition lets the secured Linux VM maintenance window end compute charges rather than only powering off inside the machine while leaving healthy controls unchanged.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Azure virtual machine states and billing status](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)

**Source reviewed:** 2026-08-31

## LAB11-Q40 — A

**Question:** Other secured Linux VM maintenance window components are healthy, but the VM maintenance still cannot capture a point-in-time copy of a managed disk. Which state causes the isolated failure?

- **A — Correct.** The snapshot source ID points to the OS disk instead of the intended data disk.
  The snapshot source ID points to the OS disk instead of the intended data disk. In secured Linux VM maintenance window, this managed disk snapshots cause matches the failure to capture a point-in-time copy of a managed disk.
- **B — Incorrect.** The selected marketplace image requires plan information that the deployment omitted.
  The selected marketplace image requires plan information that the deployment omitted. The secured Linux VM maintenance window fault concerns virtual machine image selection. Secured Linux VM maintenance window failed on managed disk snapshots; this virtual machine image selection finding redirects secured Linux VM maintenance window remediation away from managed disk snapshots.
- **C — Incorrect.** The disk SKU cannot deliver the required IOPS for the workload.
  The disk SKU cannot deliver the required IOPS for the workload. The secured Linux VM maintenance window fault concerns managed disk performance tiers. Secured Linux VM maintenance window may fix managed disk performance tiers, yet managed disk snapshots still fails; this secured Linux VM maintenance window diagnosis of managed disk performance tiers is wrong for managed disk snapshots.
- **D — Incorrect.** The guest operating system shut down, but Azure still reports the VM as allocated.
  The guest operating system shut down, but Azure still reports the VM as allocated. The secured Linux VM maintenance window fault concerns stopped and deallocated states. Secured Linux VM maintenance window has stopped and deallocated states impact, but managed disk snapshots is the secured Linux VM maintenance window failed path; the stopped and deallocated states state cannot produce managed disk snapshots failure.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Tutorial - Manage Azure disks with the Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-disks)

**Source reviewed:** 2026-08-31

## LAB11-Q41 — B

**Question:** The secured Linux VM maintenance window runbook must choose a regionally available Marketplace image reference, then retain VM maintenance read-back evidence. Which secured Linux VM maintenance window pair completes both duties?

- **A — Incorrect.** First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.
  First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM. This secured Linux VM maintenance window pair serves encryption at host. Encryption at host cannot replace virtual machine image selection in secured Linux VM maintenance window. Use this virtual machine image selection pair instead: First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.
- **B — Correct.** First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.
  First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline. In the secured Linux VM maintenance window, the first virtual machine image selection step runs; the secured Linux VM maintenance window then reads virtual machine image selection state to prove it can choose a regionally available Marketplace image reference.
- **C — Incorrect.** First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
  First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU. This secured Linux VM maintenance window pair serves VM size availability. Secured Linux VM maintenance window uses VM size availability for both steps; virtual machine image selection remains untouched in secured Linux VM maintenance window, so its virtual machine image selection gate to choose a regionally available Marketplace image reference fails.
- **D — Incorrect.** First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
  First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence. This secured Linux VM maintenance window pair serves resize deallocation. Secured Linux VM maintenance window closes resize deallocation, not virtual machine image selection; without the virtual machine image selection workflow, it cannot choose a regionally available Marketplace image reference.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Find Azure Marketplace image information with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage)

**Source reviewed:** 2026-08-31

## LAB11-Q42 — D

**Question:** To satisfy the VM maintenance requirement, operators must change the secured Linux VM maintenance window configuration and prove it can attach the virtual machine to the intended subnet through its network interface. Which sequence is coherent?

- **A — Incorrect.** First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
  First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks. This secured Linux VM maintenance window pair serves temporary disks. Secured Linux VM maintenance window proves temporary disks, but network interface dependency lacks implementation in secured Linux VM maintenance window and network interface dependency proof; the network interface dependency outcome to attach the virtual machine to the intended subnet through its network interface remains open.
- **B — Incorrect.** First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
  First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence. This secured Linux VM maintenance window pair serves resize deallocation. Secured Linux VM maintenance window uses resize deallocation for both steps; network interface dependency remains untouched in secured Linux VM maintenance window, so its network interface dependency gate to attach the virtual machine to the intended subnet through its network interface fails.
- **C — Incorrect.** First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.
  First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated. This secured Linux VM maintenance window pair serves stopped and deallocated states. Secured Linux VM maintenance window closes stopped and deallocated states, not network interface dependency; without the network interface dependency workflow, it cannot attach the virtual machine to the intended subnet through its network interface.
- **D — Correct.** First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
  For the secured Linux VM maintenance window, the safe network interface dependency order is: first, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs. The secured Linux VM maintenance window records network interface dependency proof after configuration.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Create a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q43 — D

**Question:** The compute administrator maintaining a secured Linux VM needs a safe secured Linux VM maintenance window change to encrypt supported host caches and temporary storage at the compute host, followed by VM maintenance evidence. Which pair merits approval?

- **A — Incorrect.** First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
  First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values. This secured Linux VM maintenance window pair serves managed disk performance tiers. Secured Linux VM maintenance window uses managed disk performance tiers for both steps; encryption at host remains untouched in secured Linux VM maintenance window, so its encryption at host gate to encrypt supported host caches and temporary storage at the compute host fails.
- **B — Incorrect.** First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.
  First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated. This secured Linux VM maintenance window pair serves stopped and deallocated states. Secured Linux VM maintenance window closes stopped and deallocated states, not encryption at host; without the encryption at host workflow, it cannot encrypt supported host caches and temporary storage at the compute host.
- **C — Incorrect.** First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
  First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState. This secured Linux VM maintenance window pair serves managed disk snapshots. Managed disk snapshots cannot replace encryption at host in secured Linux VM maintenance window. Use this encryption at host pair instead: First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.
- **D — Correct.** First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.
  First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM. The secured Linux VM maintenance window uses its encryption at host mutation gate and encryption at host verification gate before it can encrypt supported host caches and temporary storage at the compute host.

**Objectives:** `CP-VM-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Encryption at host for Azure virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disks-enable-host-based-encryption-cli)

**Source reviewed:** 2026-08-31

## LAB11-Q44 — B

**Question:** The secured Linux VM maintenance window has two VM maintenance gates: keep durable workload data off the host-local scratch disk, then prove the secured Linux VM maintenance window state. Which VM maintenance sequence works?

- **A — Incorrect.** First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
  First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state. This secured Linux VM maintenance window pair serves attaching data disks. Secured Linux VM maintenance window closes attaching data disks, not temporary disks; without the temporary disks workflow, it cannot keep durable workload data off the host-local scratch disk.
- **B — Correct.** First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
  The secured Linux VM maintenance window gets a complete temporary disks sequence here: first, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks. Read-back evidence follows the change.
- **C — Incorrect.** First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
  First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState. This secured Linux VM maintenance window pair serves managed disk snapshots. Secured Linux VM maintenance window proves managed disk snapshots, but temporary disks lacks implementation in secured Linux VM maintenance window and temporary disks proof; the temporary disks outcome to keep durable workload data off the host-local scratch disk remains open.
- **D — Incorrect.** First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.
  First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline. This secured Linux VM maintenance window pair serves virtual machine image selection. Secured Linux VM maintenance window uses virtual machine image selection for both steps; temporary disks remains untouched in secured Linux VM maintenance window, so its temporary disks gate to keep durable workload data off the host-local scratch disk fails.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Managed disks overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)

**Source reviewed:** 2026-08-31

## LAB11-Q45 — B

**Question:** Which VM maintenance path makes the secured Linux VM maintenance window able to choose a managed disk tier that meets the workload's performance requirement, then inspects the defining properties?

- **A — Incorrect.** First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
  First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU. This secured Linux VM maintenance window pair serves VM size availability. VM size availability cannot replace managed disk performance tiers in secured Linux VM maintenance window. Use this managed disk performance tiers pair instead: First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
- **B — Correct.** First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
  First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values. This ordered managed disk performance tiers workflow lets the secured Linux VM maintenance window choose a managed disk tier that meets the workload's performance requirement and then verify the resulting state.
- **C — Incorrect.** First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.
  First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline. This secured Linux VM maintenance window pair serves virtual machine image selection. Secured Linux VM maintenance window uses virtual machine image selection for both steps; managed disk performance tiers remains untouched in secured Linux VM maintenance window, so its managed disk performance tiers gate to choose a managed disk tier that meets the workload's performance requirement fails.
- **D — Incorrect.** First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
  First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs. This secured Linux VM maintenance window pair serves network interface dependency. Secured Linux VM maintenance window closes network interface dependency, not managed disk performance tiers; without the managed disk performance tiers workflow, it cannot choose a managed disk tier that meets the workload's performance requirement.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Azure managed disk types](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

**Source reviewed:** 2026-08-31

## LAB11-Q46 — D

**Question:** At the secured Linux VM maintenance window approval gate, operators must show that the VM maintenance can add persistent capacity without replacing the operating-system disk. Which VM maintenance configure-and-check pair is defensible?

- **A — Incorrect.** First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
  First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence. This secured Linux VM maintenance window pair serves resize deallocation. Secured Linux VM maintenance window proves resize deallocation, but attaching data disks lacks implementation in secured Linux VM maintenance window and attaching data disks proof; the attaching data disks outcome to add persistent capacity without replacing the operating-system disk remains open.
- **B — Incorrect.** First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
  First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs. This secured Linux VM maintenance window pair serves network interface dependency. Secured Linux VM maintenance window uses network interface dependency for both steps; attaching data disks remains untouched in secured Linux VM maintenance window, so its attaching data disks gate to add persistent capacity without replacing the operating-system disk fails.
- **C — Incorrect.** First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.
  First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM. This secured Linux VM maintenance window pair serves encryption at host. Secured Linux VM maintenance window closes encryption at host, not attaching data disks; without the attaching data disks workflow, it cannot add persistent capacity without replacing the operating-system disk.
- **D — Correct.** First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
  First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state. For secured Linux VM maintenance window, the attaching data disks operation precedes its attaching data disks read-back check, allowing it to add persistent capacity without replacing the operating-system disk.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB11-CP01`).

**Microsoft Learn sources:**

- [Add a data disk to a Linux virtual machine with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/add-disk)

**Source reviewed:** 2026-08-31

## LAB11-Q47 — B

**Question:** The secured Linux VM maintenance window forbids a partial VM maintenance result. Operators must first confirm that the requested compute shape is offered in the deployment region and afterward confirm the secured Linux VM maintenance window outcome. Which VM maintenance sequence is complete?

- **A — Incorrect.** First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.
  First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated. This secured Linux VM maintenance window pair serves stopped and deallocated states. Secured Linux VM maintenance window uses stopped and deallocated states for both steps; VM size availability remains untouched in secured Linux VM maintenance window, so its VM size availability gate to confirm that the requested compute shape is offered in the deployment region fails.
- **B — Correct.** First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
  First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU. In the secured Linux VM maintenance window, the first VM size availability step runs; the secured Linux VM maintenance window then reads VM size availability state to prove it can confirm that the requested compute shape is offered in the deployment region.
- **C — Incorrect.** First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.
  First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM. This secured Linux VM maintenance window pair serves encryption at host. Encryption at host cannot replace VM size availability in secured Linux VM maintenance window. Use this VM size availability pair instead: First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
- **D — Incorrect.** First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
  First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks. This secured Linux VM maintenance window pair serves temporary disks. Secured Linux VM maintenance window proves temporary disks, but VM size availability lacks implementation in secured Linux VM maintenance window and VM size availability proof; the VM size availability outcome to confirm that the requested compute shape is offered in the deployment region remains open.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB11-CP02`).

**Microsoft Learn sources:**

- [Virtual machine sizes in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)

**Source reviewed:** 2026-08-31

## LAB11-Q48 — A

**Question:** Only the secured Linux VM maintenance window change needed to change compute size when the destination cluster cannot resize the running machine in place is allowed, and VM maintenance proof is mandatory. Which pair fits?

- **A — Correct.** First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
  For the secured Linux VM maintenance window, the safe resize deallocation order is: first, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence. The secured Linux VM maintenance window records resize deallocation proof after configuration.
- **B — Incorrect.** First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
  First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState. This secured Linux VM maintenance window pair serves managed disk snapshots. Managed disk snapshots cannot replace resize deallocation in secured Linux VM maintenance window. Use this resize deallocation pair instead: First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
- **C — Incorrect.** First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
  First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks. This secured Linux VM maintenance window pair serves temporary disks. Secured Linux VM maintenance window proves temporary disks, but resize deallocation lacks implementation in secured Linux VM maintenance window and resize deallocation proof; the resize deallocation outcome to change compute size when the destination cluster cannot resize the running machine in place remains open.
- **D — Incorrect.** First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
  First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values. This secured Linux VM maintenance window pair serves managed disk performance tiers. Secured Linux VM maintenance window uses managed disk performance tiers for both steps; resize deallocation remains untouched in secured Linux VM maintenance window, so its resize deallocation gate to change compute size when the destination cluster cannot resize the running machine in place fails.

**Objectives:** `CP-VM-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB11-CP03`).

**Microsoft Learn sources:**

- [Resize an Azure virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm)

**Source reviewed:** 2026-08-31

## LAB11-Q49 — D

**Question:** The secured Linux VM maintenance window runbook separates VM maintenance mutation from validation while it must end compute charges rather than only powering off inside the machine. Which sequence proves it cleanly?

- **A — Incorrect.** First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.
  First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline. This secured Linux VM maintenance window pair serves virtual machine image selection. Virtual machine image selection cannot replace stopped and deallocated states in secured Linux VM maintenance window. Use this stopped and deallocated states pair instead: First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.
- **B — Incorrect.** First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
  First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values. This secured Linux VM maintenance window pair serves managed disk performance tiers. Secured Linux VM maintenance window proves managed disk performance tiers, but stopped and deallocated states lacks implementation in secured Linux VM maintenance window and stopped and deallocated states proof; the stopped and deallocated states outcome to end compute charges rather than only powering off inside the machine remains open.
- **C — Incorrect.** First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
  First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state. This secured Linux VM maintenance window pair serves attaching data disks. Secured Linux VM maintenance window uses attaching data disks for both steps; stopped and deallocated states remains untouched in secured Linux VM maintenance window, so its stopped and deallocated states gate to end compute charges rather than only powering off inside the machine fails.
- **D — Correct.** First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.
  First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated. The secured Linux VM maintenance window uses its stopped and deallocated states mutation gate and stopped and deallocated states verification gate before it can end compute charges rather than only powering off inside the machine.

**Objectives:** `CP-VM-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB11-CP04`).

**Microsoft Learn sources:**

- [Azure virtual machine states and billing status](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)

**Source reviewed:** 2026-08-31

## LAB11-Q50 — A

**Question:** The secured Linux VM maintenance window checkpoint requires both this VM maintenance outcome—capture a point-in-time copy of a managed disk—and a read-only secured Linux VM maintenance window state check. Which VM maintenance response is complete?

- **A — Correct.** First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
  The secured Linux VM maintenance window gets a complete managed disk snapshots sequence here: first, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState. Read-back evidence follows the change.
- **B — Incorrect.** First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
  First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs. This secured Linux VM maintenance window pair serves network interface dependency. Secured Linux VM maintenance window uses network interface dependency for both steps; managed disk snapshots remains untouched in secured Linux VM maintenance window, so its managed disk snapshots gate to capture a point-in-time copy of a managed disk fails.
- **C — Incorrect.** First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
  First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state. This secured Linux VM maintenance window pair serves attaching data disks. Secured Linux VM maintenance window closes attaching data disks, not managed disk snapshots; without the managed disk snapshots workflow, it cannot capture a point-in-time copy of a managed disk.
- **D — Incorrect.** First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
  First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU. This secured Linux VM maintenance window pair serves VM size availability. VM size availability cannot replace managed disk snapshots in secured Linux VM maintenance window. Use this managed disk snapshots pair instead: First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.

**Objectives:** `CP-VM-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB11-CP05`).

**Microsoft Learn sources:**

- [Tutorial - Manage Azure disks with the Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-disks)

**Source reviewed:** 2026-08-31
