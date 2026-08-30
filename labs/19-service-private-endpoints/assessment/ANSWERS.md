# Lab 19 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB19-Q01`)

The lab's central distinction is: Service endpoints keep the service's public endpoint while adding subnet identity, whereas private endpoints place a private NIC in the VNet and depend on correct private DNS resolution.

Objectives: ST-ACCESS-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview>

## 2. B (`LAB19-Q02`)

The first implementation checkpoint is: Create separate service-endpoint and private-endpoint subnets with appropriate policies.

Objectives: CP-APP-07

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview>

## 3. C (`LAB19-Q03`)

The documented permission boundary is Network Contributor and Storage Account Contributor on the lab resource group

Objectives: NW-SECURE-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints>

## 4. D (`LAB19-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: NW-SECURE-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone>

## 5. A (`LAB19-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: ST-ACCESS-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview>

## 6. B (`LAB19-Q06`)

The live-only gate is explicit and must not be guessed: None beyond the declared role and a disposable subscription.

Objectives: CP-APP-07

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview>

## 7. C (`LAB19-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: NW-SECURE-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints>

## 8. D (`LAB19-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: NW-SECURE-05, ST-ACCESS-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone>

## 9. A (`LAB19-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: ST-ACCESS-01, CP-APP-07

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview>

## 10. B (`LAB19-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: CP-APP-07, NW-SECURE-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview>
