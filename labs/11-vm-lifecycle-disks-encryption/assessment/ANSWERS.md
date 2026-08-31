# Lab 11 answer key

Return to [the questions](QUESTIONS.md).

## 1. C (`LAB11-Q01`)

The lab establishes this design principle: VM resize can require deallocation, managed disks have independent lifecycles, and encryption at host depends on subscription registration, region, and VM size support.

Objectives: CP-VM-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli>

## 2. D (`LAB11-Q02`)

The reviewed hands-on action for this objective is: Enable encryption at host only after the subscription feature and selected VM size are confirmed.

Objectives: CP-VM-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm>

## 3. A (`LAB11-Q03`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: CP-VM-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-machines/linux/attach-disk-portal>

## 4. B (`LAB11-Q04`)

The lab's reviewed command path performs this bounded action: Deallocate and resize the VM to a validated alternative SKU, then return it to the intended state.

Objectives: CP-VM-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-machines/disks-enable-host-based-encryption-cli>

## 5. C (`LAB11-Q05`)

The independent validation path must prove Microsoft.Compute/disks for the exact recorded object.

Objectives: CP-VM-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli>

## 6. D (`LAB11-Q06`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: CP-VM-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm>

## 7. A (`LAB11-Q07`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: CP-VM-04, CP-VM-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-machines/linux/attach-disk-portal>

## 8. B (`LAB11-Q08`)

Accepted requests and offline checks do not prove the final live state.

Objectives: CP-VM-05, CP-VM-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-machines/disks-enable-host-based-encryption-cli>
