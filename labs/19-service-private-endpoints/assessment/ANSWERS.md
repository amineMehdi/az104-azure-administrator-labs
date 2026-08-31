# Lab 19 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB19-Q01`)

The lab establishes this design principle: Service endpoints keep the service's public endpoint while adding subnet identity, whereas private endpoints place a private NIC in the VNet and depend on correct private DNS resolution.

Objectives: NW-SECURE-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview>

## 2. B (`LAB19-Q02`)

The reviewed hands-on action for this objective is: Enable Microsoft.Storage service endpoints and add a storage virtual-network rule.

Objectives: NW-SECURE-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview>

## 3. C (`LAB19-Q03`)

Least privilege requires the documented boundary: Network Contributor and Storage Account Contributor on the lab resource group

Objectives: NW-SECURE-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints>

## 4. D (`LAB19-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: NW-SECURE-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone>

## 5. A (`LAB19-Q05`)

The lab's reviewed command path performs this bounded action: Create separate service-endpoint and private-endpoint subnets with appropriate policies.

Objectives: NW-SECURE-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview>

## 6. B (`LAB19-Q06`)

The independent validation path must prove Microsoft.Network/privateDnsZones for the exact recorded object.

Objectives: NW-SECURE-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview>

## 7. C (`LAB19-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: NW-SECURE-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints>

## 8. D (`LAB19-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: NW-SECURE-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone>

## 9. A (`LAB19-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: NW-SECURE-04, NW-SECURE-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview>

## 10. B (`LAB19-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: NW-SECURE-05, NW-SECURE-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview>
