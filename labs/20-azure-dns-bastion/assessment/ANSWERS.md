# Lab 20 answer key

Return to [the questions](QUESTIONS.md).

## 1. C (`LAB20-Q01`)

The lab establishes this design principle: Bastion provides managed administrative connectivity without VM public IPs, while Azure DNS becomes authoritative only after the parent domain delegates to its assigned name servers.

Objectives: NW-SECURE-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/bastion/tutorial-create-host-cli>

## 2. D (`LAB20-Q02`)

The reviewed hands-on action for this objective is: Deploy Azure Bastion and inspect SKU, scale units, and supported native-client features.

Objectives: NW-DNSLB-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/bastion/configuration-settings>

## 3. A (`LAB20-Q03`)

Least privilege requires the documented boundary: Network Contributor; DNS Zone Contributor for an owned zone

Objectives: NW-SECURE-03

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli>

## 4. B (`LAB20-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: NW-DNSLB-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation>

## 5. C (`LAB20-Q05`)

The lab's reviewed command path performs this bounded action: Create a correctly named and sized AzureBastionSubnet with a Standard static public IP.

Objectives: NW-SECURE-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/bastion/tutorial-create-host-cli>

## 6. D (`LAB20-Q06`)

The independent validation path must prove Microsoft.Network/dnsZones for the exact recorded object.

Objectives: NW-DNSLB-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/bastion/configuration-settings>

## 7. A (`LAB20-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: Real public DNS delegation requires AZ104_OWNED_DNS_ZONE and control of the parent registrar; the isolated zone path is always available.

Objectives: NW-SECURE-03

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli>

## 8. B (`LAB20-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: NW-DNSLB-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation>

## 9. C (`LAB20-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: NW-SECURE-03, NW-DNSLB-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/bastion/tutorial-create-host-cli>

## 10. D (`LAB20-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: NW-DNSLB-01, NW-SECURE-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/bastion/configuration-settings>
