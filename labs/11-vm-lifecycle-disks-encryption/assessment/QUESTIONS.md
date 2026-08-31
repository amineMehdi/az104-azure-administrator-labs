# Lab 11 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB11-Q01 — Foundational

A compute administrator maintaining a secured Linux VM is updating the VM maintenance runbook. The requirement is to choose a regionally available Marketplace image reference. Which statement describes Azure behavior correctly?

- A. A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms.
- B. A VM network interface must reference a valid subnet and satisfy regional and attachment constraints.
- C. Managed disk type and size determine supported performance, cost, and workload characteristics.
- D. Some VM resizes require deallocation when the target size is unavailable on the current cluster.

## LAB11-Q02 — Foundational

A VM maintenance peer review asks how the secured Linux VM maintenance window should handle this outcome: attach the virtual machine to the intended subnet through its network interface. Which explanation is accurate?

- A. A VM network interface must reference a valid subnet and satisfy regional and attachment constraints.
- B. Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption.
- C. A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest.
- D. A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation.

## LAB11-Q03 — Foundational

For the secured Linux VM maintenance window, the VM maintenance plan must encrypt supported host caches and temporary storage at the compute host. Which statement about VM maintenance belongs in the secured Linux VM maintenance window record?

- A. A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss.
- B. Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity.
- C. Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption.
- D. A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs.

## LAB11-Q04 — Foundational

The VM maintenance review compares four claims for the secured Linux VM maintenance window requirement to keep durable workload data off the host-local scratch disk. Which claim is technically sound?

- A. Managed disk type and size determine supported performance, cost, and workload characteristics.
- B. A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss.
- C. Some VM resizes require deallocation when the target size is unavailable on the current cluster.
- D. A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms.

## LAB11-Q05 — Foundational

The VM maintenance architecture note requires the secured Linux VM maintenance window environment to choose a managed disk tier that meets the workload's performance requirement. Which statement defines the relevant VM maintenance boundary?

- A. Managed disk type and size determine supported performance, cost, and workload characteristics.
- B. A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest.
- C. A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation.
- D. A VM network interface must reference a valid subnet and satisfy regional and attachment constraints.

## LAB11-Q06 — Foundational

A new VM maintenance operator must explain why the secured Linux VM maintenance window can add persistent capacity without replacing the operating-system disk. Which explanation is accurate?

- A. Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity.
- B. A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest.
- C. A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs.
- D. Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption.

## LAB11-Q07 — Foundational

The secured Linux VM maintenance window acceptance criteria require operators to confirm that the requested compute shape is offered in the deployment region. Which service fact supports that requirement?

- A. Some VM resizes require deallocation when the target size is unavailable on the current cluster.
- B. Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity.
- C. A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms.
- D. A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss.

## LAB11-Q08 — Foundational

A VM maintenance reviewer challenges whether the secured Linux VM maintenance window can change compute size when the destination cluster cannot resize the running machine in place. Which response resolves the concern?

- A. A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation.
- B. A VM network interface must reference a valid subnet and satisfy regional and attachment constraints.
- C. Managed disk type and size determine supported performance, cost, and workload characteristics.
- D. Some VM resizes require deallocation when the target size is unavailable on the current cluster.

## LAB11-Q09 — Foundational

The secured Linux VM maintenance window handoff omits the VM maintenance rule needed to end compute charges rather than only powering off inside the machine. Which statement should the team add?

- A. A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs.
- B. Encryption at host encrypts supported VM host caches and temporary disks in addition to managed disk server-side encryption.
- C. A stopped VM can remain allocated and billed for compute, while a deallocated VM releases compute allocation.
- D. A managed data disk must be attached at a unique LUN and then initialized and mounted inside the guest.

## LAB11-Q10 — Foundational

A VM maintenance incident review of the secured Linux VM maintenance window depends on the ability to capture a point-in-time copy of a managed disk. Which platform description is reliable?

- A. A VM image determines the operating-system publisher, offer, SKU, version, and applicable purchase terms.
- B. A managed disk snapshot is a point-in-time copy used to create another disk and should be coordinated with application consistency needs.
- C. A VM temporary disk is local ephemeral storage and must not hold data that must survive maintenance, redeployment, or host loss.
- D. Available VM sizes depend on region, zone, subscription quota, hardware cluster, and current allocation capacity.

## LAB11-Q11 — Foundational

A VM maintenance ticket in the secured Linux VM maintenance window says to choose a regionally available Marketplace image reference. Which VM maintenance action completes the secured Linux VM maintenance window request with minimal change?

- A. Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile.
- B. Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS.
- C. Use deallocate when the lab must release compute billing and no workload state depends on host allocation.
- D. Resolve an approved image URN and accept marketplace terms when the selected image requires them.

## LAB11-Q12 — Foundational

The approach for the secured Linux VM maintenance window is approved, but the VM maintenance environment still cannot attach the virtual machine to the intended subnet through its network interface. Which implementation step closes the gap?

- A. Place durable application data on managed data disks or an external storage service.
- B. List available sizes for the VM and region before choosing the target SKU.
- C. Create the subnet and NIC before attaching that NIC to the VM deployment.
- D. Quiesce the workload when required and create a snapshot from the intended managed disk ID.

## LAB11-Q13 — Foundational

The compute administrator maintaining a secured Linux VM may change the secured Linux VM maintenance window only to encrypt supported host caches and temporary storage at the compute host. Which VM maintenance action stays within that assignment?

- A. Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile.
- B. Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs.
- C. Plan downtime and deallocate the VM when an online resize path is not available.
- D. Resolve an approved image URN and accept marketplace terms when the selected image requires them.

## LAB11-Q14 — Foundational

A VM maintenance dry run shows no secured Linux VM maintenance window command will keep durable workload data off the host-local scratch disk. Which action belongs before execution?

- A. Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS.
- B. Place durable application data on managed data disks or an external storage service.
- C. Use deallocate when the lab must release compute billing and no workload state depends on host allocation.
- D. Create the subnet and NIC before attaching that NIC to the VM deployment.

## LAB11-Q15 — Foundational

For the secured Linux VM maintenance window, operators need to choose a managed disk tier that meets the workload's performance requirement. Which change realizes that requirement?

- A. Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs.
- B. List available sizes for the VM and region before choosing the target SKU.
- C. Quiesce the workload when required and create a snapshot from the intended managed disk ID.
- D. Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile.

## LAB11-Q16 — Applied

Operators must automate the secured Linux VM maintenance window change needed to add persistent capacity without replacing the operating-system disk. Which VM maintenance operation belongs in the runbook?

- A. Plan downtime and deallocate the VM when an online resize path is not available.
- B. Resolve an approved image URN and accept marketplace terms when the selected image requires them.
- C. Place durable application data on managed data disks or an external storage service.
- D. Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS.

## LAB11-Q17 — Applied

A secured Linux VM maintenance window review finds VM maintenance drift from the need to confirm that the requested compute shape is offered in the deployment region. Which correction addresses that drift?

- A. Use deallocate when the lab must release compute billing and no workload state depends on host allocation.
- B. Create the subnet and NIC before attaching that NIC to the VM deployment.
- C. List available sizes for the VM and region before choosing the target SKU.
- D. Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs.

## LAB11-Q18 — Applied

The secured Linux VM maintenance window window permits only the VM maintenance change needed to change compute size when the destination cluster cannot resize the running machine in place. Which option respects the boundary?

- A. Quiesce the workload when required and create a snapshot from the intended managed disk ID.
- B. Plan downtime and deallocate the VM when an online resize path is not available.
- C. Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile.
- D. Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS.

## LAB11-Q19 — Applied

The VM maintenance preflight has passed; the secured Linux VM maintenance window must now end compute charges rather than only powering off inside the machine. Which operation should run?

- A. Use deallocate when the lab must release compute billing and no workload state depends on host allocation.
- B. Resolve an approved image URN and accept marketplace terms when the selected image requires them.
- C. Place durable application data on managed data disks or an external storage service.
- D. List available sizes for the VM and region before choosing the target SKU.

## LAB11-Q20 — Applied

The secured Linux VM maintenance window plan must capture a point-in-time copy of a managed disk while limiting the mutation scope to VM maintenance. Which action is appropriate?

- A. Create the subnet and NIC before attaching that NIC to the VM deployment.
- B. Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs.
- C. Quiesce the workload when required and create a snapshot from the intended managed disk ID.
- D. Plan downtime and deallocate the VM when an online resize path is not available.

## LAB11-Q21 — Applied

The secured Linux VM maintenance window setup reports success after the VM maintenance attempt to choose a regionally available Marketplace image reference. Which VM maintenance read-only observation proves the secured Linux VM maintenance window outcome?

- A. Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
- B. Query storageProfile.imageReference and confirm every image component matches the approved baseline.
- C. Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
- D. Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.

## LAB11-Q22 — Applied

The VM maintenance log says the secured Linux VM maintenance window can now attach the virtual machine to the intended subnet through its network interface. Which VM maintenance state should the secured Linux VM maintenance window acceptance test retain?

- A. Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
- B. Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
- C. Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
- D. Query storageProfile.imageReference and confirm every image component matches the approved baseline.

## LAB11-Q23 — Applied

The secured Linux VM maintenance window rejects VM maintenance exit status as proof it can encrypt supported host caches and temporary storage at the compute host. Which secured Linux VM maintenance window result is valid evidence?

- A. Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
- B. Query instanceView power state and confirm it reports VM deallocated.
- C. Query securityProfile.encryptionAtHost and verify it is true on the running VM.
- D. Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.

## LAB11-Q24 — Applied

The VM maintenance validator needs one secured Linux VM maintenance window query after the change to keep durable workload data off the host-local scratch disk. Which VM maintenance property should the secured Linux VM maintenance window validator inspect?

- A. Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
- B. Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
- C. Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
- D. Query securityProfile.encryptionAtHost and verify it is true on the running VM.

## LAB11-Q25 — Applied

The compute administrator maintaining a secured Linux VM must confirm the secured Linux VM maintenance window, without mutation, can choose a managed disk tier that meets the workload's performance requirement. Which VM maintenance check qualifies?

- A. Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
- B. Query storageProfile.imageReference and confirm every image component matches the approved baseline.
- C. Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
- D. Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.

## LAB11-Q26 — Applied

The secured Linux VM maintenance window configuration is complete; the VM maintenance reviewers need evidence it can add persistent capacity without replacing the operating-system disk. Which observation shows success?

- A. Query instanceView power state and confirm it reports VM deallocated.
- B. Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
- C. Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
- D. Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.

## LAB11-Q27 — Applied

The VM maintenance validation asks whether the secured Linux VM maintenance window can confirm that the requested compute shape is offered in the deployment region. Which observable state is strongest?

- A. Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
- B. Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
- C. Query securityProfile.encryptionAtHost and verify it is true on the running VM.
- D. Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.

## LAB11-Q28 — Applied

A secured Linux VM maintenance window review must prove the VM maintenance ability to change compute size when the destination cluster cannot resize the running machine in place. Which check avoids an adjacent feature?

- A. Query storageProfile.imageReference and confirm every image component matches the approved baseline.
- B. Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
- C. Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
- D. Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.

## LAB11-Q29 — Applied

The secured Linux VM maintenance window evidence bundle needs a VM maintenance result showing it can end compute charges rather than only powering off inside the machine. Which result belongs in the checkpoint?

- A. Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
- B. Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
- C. Query instanceView power state and confirm it reports VM deallocated.
- D. Read powerState and hardwareProfile.vmSize after the resize and restart sequence.

## LAB11-Q30 — Applied

Before secured Linux VM maintenance window cleanup, the VM maintenance team must reconfirm it can capture a point-in-time copy of a managed disk. Which read-only inspection should run?

- A. Query securityProfile.encryptionAtHost and verify it is true on the running VM.
- B. Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
- C. Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
- D. Query instanceView power state and confirm it reports VM deallocated.

## LAB11-Q31 — Applied

During a VM maintenance fault drill, the secured Linux VM maintenance window does not choose a regionally available Marketplace image reference. Which finding identifies the defect?

- A. The NIC resides in a different region from the virtual machine.
- B. Two requested data disks use the same LUN on one virtual machine.
- C. The snapshot source ID points to the OS disk instead of the intended data disk.
- D. The selected marketplace image requires plan information that the deployment omitted.

## LAB11-Q32 — Applied

The secured Linux VM maintenance window setup finishes, yet the VM maintenance cannot attach the virtual machine to the intended subnet through its network interface. Which misconfiguration explains the mismatch?

- A. The selected VM size or subscription is not enabled for encryption at host.
- B. The requested size is not available on the current hardware cluster.
- C. The selected marketplace image requires plan information that the deployment omitted.
- D. The NIC resides in a different region from the virtual machine.

## LAB11-Q33 — Applied

A VM maintenance break/fix in the secured Linux VM maintenance window fails when operators try to encrypt supported host caches and temporary storage at the compute host. Which diagnosis fits?

- A. The application wrote its only database copy to the temporary disk.
- B. The runbook attempts an online resize to a SKU unavailable on the VM's current cluster.
- C. The selected VM size or subscription is not enabled for encryption at host.
- D. The NIC resides in a different region from the virtual machine.

## LAB11-Q34 — Applied

The secured Linux VM maintenance window troubleshooting scope is the VM maintenance need to keep durable workload data off the host-local scratch disk. Which condition should be corrected first?

- A. The disk SKU cannot deliver the required IOPS for the workload.
- B. The guest operating system shut down, but Azure still reports the VM as allocated.
- C. The application wrote its only database copy to the temporary disk.
- D. The selected VM size or subscription is not enabled for encryption at host.

## LAB11-Q35 — Applied

The secured Linux VM maintenance window result is partial because the VM maintenance cannot choose a managed disk tier that meets the workload's performance requirement. Which condition accounts for that result?

- A. The disk SKU cannot deliver the required IOPS for the workload.
- B. Two requested data disks use the same LUN on one virtual machine.
- C. The snapshot source ID points to the OS disk instead of the intended data disk.
- D. The application wrote its only database copy to the temporary disk.

## LAB11-Q36 — Applied

The VM maintenance evidence shows the secured Linux VM maintenance window cannot add persistent capacity without replacing the operating-system disk. Which root cause fits that evidence?

- A. The requested size is not available on the current hardware cluster.
- B. The selected marketplace image requires plan information that the deployment omitted.
- C. The disk SKU cannot deliver the required IOPS for the workload.
- D. Two requested data disks use the same LUN on one virtual machine.

## LAB11-Q37 — Applied

Although the secured Linux VM maintenance window is meant to let the VM maintenance confirm that the requested compute shape is offered in the deployment region, its checkpoint fails. Which VM maintenance defect explains the failure?

- A. The requested size is not available on the current hardware cluster.
- B. The runbook attempts an online resize to a SKU unavailable on the VM's current cluster.
- C. The NIC resides in a different region from the virtual machine.
- D. Two requested data disks use the same LUN on one virtual machine.

## LAB11-Q38 — Applied

The VM maintenance support team isolated the secured Linux VM maintenance window incident to the attempt to change compute size when the destination cluster cannot resize the running machine in place. Which condition prevents success?

- A. The guest operating system shut down, but Azure still reports the VM as allocated.
- B. The selected VM size or subscription is not enabled for encryption at host.
- C. The requested size is not available on the current hardware cluster.
- D. The runbook attempts an online resize to a SKU unavailable on the VM's current cluster.

## LAB11-Q39 — Applied

A secured Linux VM maintenance window query surprises the compute administrator maintaining a secured Linux VM during the VM maintenance attempt to end compute charges rather than only powering off inside the machine. Which finding explains it?

- A. The snapshot source ID points to the OS disk instead of the intended data disk.
- B. The application wrote its only database copy to the temporary disk.
- C. The runbook attempts an online resize to a SKU unavailable on the VM's current cluster.
- D. The guest operating system shut down, but Azure still reports the VM as allocated.

## LAB11-Q40 — Applied

Other secured Linux VM maintenance window components are healthy, but the VM maintenance still cannot capture a point-in-time copy of a managed disk. Which state causes the isolated failure?

- A. The snapshot source ID points to the OS disk instead of the intended data disk.
- B. The selected marketplace image requires plan information that the deployment omitted.
- C. The disk SKU cannot deliver the required IOPS for the workload.
- D. The guest operating system shut down, but Azure still reports the VM as allocated.

## LAB11-Q41 — Advanced

The secured Linux VM maintenance window runbook must choose a regionally available Marketplace image reference, then retain VM maintenance read-back evidence. Which secured Linux VM maintenance window pair completes both duties?

- A. First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.
- B. First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.
- C. First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
- D. First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.

## LAB11-Q42 — Advanced

To satisfy the VM maintenance requirement, operators must change the secured Linux VM maintenance window configuration and prove it can attach the virtual machine to the intended subnet through its network interface. Which sequence is coherent?

- A. First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
- B. First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
- C. First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.
- D. First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.

## LAB11-Q43 — Advanced

The compute administrator maintaining a secured Linux VM needs a safe secured Linux VM maintenance window change to encrypt supported host caches and temporary storage at the compute host, followed by VM maintenance evidence. Which pair merits approval?

- A. First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
- B. First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.
- C. First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
- D. First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.

## LAB11-Q44 — Advanced

The secured Linux VM maintenance window has two VM maintenance gates: keep durable workload data off the host-local scratch disk, then prove the secured Linux VM maintenance window state. Which VM maintenance sequence works?

- A. First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
- B. First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
- C. First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
- D. First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.

## LAB11-Q45 — Advanced

Which VM maintenance path makes the secured Linux VM maintenance window able to choose a managed disk tier that meets the workload's performance requirement, then inspects the defining properties?

- A. First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
- B. First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
- C. First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.
- D. First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.

## LAB11-Q46 — Advanced

At the secured Linux VM maintenance window approval gate, operators must show that the VM maintenance can add persistent capacity without replacing the operating-system disk. Which VM maintenance configure-and-check pair is defensible?

- A. First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
- B. First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
- C. First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.
- D. First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.

## LAB11-Q47 — Advanced

The secured Linux VM maintenance window forbids a partial VM maintenance result. Operators must first confirm that the requested compute shape is offered in the deployment region and afterward confirm the secured Linux VM maintenance window outcome. Which VM maintenance sequence is complete?

- A. First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.
- B. First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.
- C. First, Confirm subscription and VM-size support, then enable encryptionAtHost on the VM security profile. Then, Query securityProfile.encryptionAtHost and verify it is true on the running VM.
- D. First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.

## LAB11-Q48 — Advanced

Only the secured Linux VM maintenance window change needed to change compute size when the destination cluster cannot resize the running machine in place is allowed, and VM maintenance proof is mandatory. Which pair fits?

- A. First, Plan downtime and deallocate the VM when an online resize path is not available. Then, Read powerState and hardwareProfile.vmSize after the resize and restart sequence.
- B. First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
- C. First, Place durable application data on managed data disks or an external storage service. Then, Inspect the VM size's temporary-disk capability and confirm durable paths map to managed disks.
- D. First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.

## LAB11-Q49 — Advanced

The secured Linux VM maintenance window runbook separates VM maintenance mutation from validation while it must end compute charges rather than only powering off inside the machine. Which sequence proves it cleanly?

- A. First, Resolve an approved image URN and accept marketplace terms when the selected image requires them. Then, Query storageProfile.imageReference and confirm every image component matches the approved baseline.
- B. First, Choose Standard HDD, Standard SSD, Premium SSD, or another supported type from measured workload needs. Then, Query each disk's sku, diskSizeGb, diskIOPSReadWrite, and diskMBpsReadWrite values.
- C. First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
- D. First, Use deallocate when the lab must release compute billing and no workload state depends on host allocation. Then, Query instanceView power state and confirm it reports VM deallocated.

## LAB11-Q50 — Advanced

The secured Linux VM maintenance window checkpoint requires both this VM maintenance outcome—capture a point-in-time copy of a managed disk—and a read-only secured Linux VM maintenance window state check. Which VM maintenance response is complete?

- A. First, Quiesce the workload when required and create a snapshot from the intended managed disk ID. Then, Query snapshot creationData.sourceResourceId, diskSizeGb, and provisioningState.
- B. First, Create the subnet and NIC before attaching that NIC to the VM deployment. Then, Query the VM networkProfile and resolve its NIC and IP configuration resource IDs.
- C. First, Create or select the managed disk, attach it with a free LUN, and initialize it in the guest OS. Then, Query storageProfile.dataDisks and confirm disk ID, LUN, caching, and attachment state.
- D. First, List available sizes for the VM and region before choosing the target SKU. Then, Query the final hardwareProfile.vmSize and verify quota and zone support for that SKU.

[Open the answer key](./ANSWERS.md)
