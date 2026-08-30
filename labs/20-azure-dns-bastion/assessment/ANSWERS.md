# Lab 20 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB20-Q01`)

The lab's central distinction is: Bastion provides managed administrative connectivity without VM public IPs, while Azure DNS becomes authoritative only after the parent domain delegates to its assigned name servers.

Objectives: NW-SECURE-03

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/bastion/tutorial-create-host-cli>

## 2. B (`LAB20-Q02`)

The first implementation checkpoint is: Create a correctly named and sized AzureBastionSubnet with a Standard static public IP.

Objectives: NW-DNSLB-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/bastion/configuration-settings>

## 3. C (`LAB20-Q03`)

The documented permission boundary is Network Contributor; DNS Zone Contributor for an owned zone

Objectives: NW-SECURE-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli>

## 4. D (`LAB20-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: NW-DNSLB-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation>

## 5. A (`LAB20-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: NW-SECURE-03

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/bastion/tutorial-create-host-cli>

## 6. B (`LAB20-Q06`)

The live-only gate is explicit and must not be guessed: Real public DNS delegation requires AZ104_OWNED_DNS_ZONE and control of the parent registrar; the isolated zone path is always available.

Objectives: NW-DNSLB-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/bastion/configuration-settings>

## 7. C (`LAB20-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: NW-SECURE-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli>

## 8. D (`LAB20-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: NW-DNSLB-01, NW-SECURE-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation>

## 9. A (`LAB20-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: NW-SECURE-03, NW-DNSLB-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/bastion/tutorial-create-host-cli>

## 10. B (`LAB20-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: NW-DNSLB-01, NW-SECURE-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/bastion/configuration-settings>
