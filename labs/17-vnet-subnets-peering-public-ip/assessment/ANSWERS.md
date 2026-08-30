# Lab 17 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB17-Q01`)

The lab's central distinction is: VNet peering is non-transitive and requires compatible address spaces and two directional peering objects, while Standard public IPs are secure by default until an NSG permits traffic.

Objectives: NW-VNET-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell>

## 2. B (`LAB17-Q02`)

The first implementation checkpoint is: Create hub and spoke address spaces that do not overlap and subdivide them into purpose-specific subnets.

Objectives: NW-VNET-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering>

## 3. C (`LAB17-Q03`)

The documented permission boundary is Network Contributor on the lab resource group

Objectives: NW-VNET-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses>

## 4. D (`LAB17-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: NW-VNET-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell>

## 5. A (`LAB17-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: NW-VNET-02

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering>

## 6. B (`LAB17-Q06`)

The live-only gate is explicit and must not be guessed: None beyond the declared role and a disposable subscription.

Objectives: NW-VNET-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses>

## 7. C (`LAB17-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: NW-VNET-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell>

## 8. D (`LAB17-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: NW-VNET-02, NW-VNET-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering>

## 9. A (`LAB17-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: NW-VNET-03, NW-VNET-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses>

## 10. B (`LAB17-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: NW-VNET-01, NW-VNET-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell>
