# Lab 18 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB18-Q01`)

The lab's central distinction is: NSG evaluation uses priority and direction, ASGs replace hard-coded IP membership, and route selection uses longest-prefix matching before connectivity diagnostics explain the result.

Objectives: NW-VNET-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group>

## 2. B (`LAB18-Q02`)

The first implementation checkpoint is: Create frontend and backend ASGs and associate test NIC configurations.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups>

## 3. C (`LAB18-Q03`)

The documented permission boundary is Network Contributor on the lab resource group

Objectives: NW-SECURE-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-route-table>

## 4. D (`LAB18-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: NW-SECURE-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview>

## 5. A (`LAB18-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: NW-VNET-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group>

## 6. B (`LAB18-Q06`)

The live-only gate is explicit and must not be guessed: None beyond the declared role and a disposable subscription.

Objectives: NW-VNET-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups>

## 7. C (`LAB18-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: NW-SECURE-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-route-table>

## 8. D (`LAB18-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: NW-SECURE-02, NW-VNET-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview>

## 9. A (`LAB18-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: NW-VNET-04, NW-VNET-05

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group>

## 10. B (`LAB18-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: NW-VNET-05, NW-SECURE-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups>
