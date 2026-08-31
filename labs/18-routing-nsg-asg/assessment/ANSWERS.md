# Lab 18 answer key

Return to [the questions](QUESTIONS.md).

## 1. C (`LAB18-Q01`)

The lab establishes this design principle: NSG evaluation uses priority and direction, ASGs replace hard-coded IP membership, and route selection uses longest-prefix matching before connectivity diagnostics explain the result.

Objectives: NW-VNET-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group>

## 2. D (`LAB18-Q02`)

The reviewed hands-on action for this objective is: Create ordered NSG rules that allow only the intended application flow and preserve default deny behavior.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups>

## 3. A (`LAB18-Q03`)

Least privilege requires the documented boundary: Network Contributor on the lab resource group

Objectives: NW-SECURE-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-route-table>

## 4. B (`LAB18-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: NW-SECURE-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview>

## 5. C (`LAB18-Q05`)

The lab's reviewed command path performs this bounded action: Create frontend and backend ASGs and associate test NIC configurations.

Objectives: NW-VNET-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group>

## 6. D (`LAB18-Q06`)

The independent validation path must prove Microsoft.Network/applicationSecurityGroups for the exact recorded object.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups>

## 7. A (`LAB18-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: NW-SECURE-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-route-table>

## 8. B (`LAB18-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: NW-SECURE-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview>

## 9. C (`LAB18-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: NW-VNET-04, NW-VNET-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group>

## 10. D (`LAB18-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: NW-VNET-05, NW-SECURE-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups>
