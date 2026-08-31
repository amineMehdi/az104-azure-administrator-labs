# Lab 17 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB17-Q01`)

The lab establishes this design principle: VNet peering is non-transitive and requires compatible address spaces and two directional peering objects, while Standard public IPs are secure by default until an NSG permits traffic.

Objectives: NW-VNET-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell>

## 2. B (`LAB17-Q02`)

The reviewed hands-on action for this objective is: Create both sides of VNet peering and interpret Connected, Initiated, and Disconnected states.

Objectives: NW-VNET-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering>

## 3. C (`LAB17-Q03`)

Least privilege requires the documented boundary: Network Contributor on the lab resource group

Objectives: NW-VNET-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses>

## 4. D (`LAB17-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: NW-VNET-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell>

## 5. A (`LAB17-Q05`)

The lab's reviewed command path performs this bounded action: Create hub and spoke address spaces that do not overlap and subdivide them into purpose-specific subnets.

Objectives: NW-VNET-02

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering>

## 6. B (`LAB17-Q06`)

The independent validation path must prove Microsoft.Network/publicIPAddresses for the exact recorded object.

Objectives: NW-VNET-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses>

## 7. C (`LAB17-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: NW-VNET-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell>

## 8. D (`LAB17-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: NW-VNET-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering>

## 9. A (`LAB17-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: NW-VNET-03, NW-VNET-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses>

## 10. B (`LAB17-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: NW-VNET-01, NW-VNET-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell>
