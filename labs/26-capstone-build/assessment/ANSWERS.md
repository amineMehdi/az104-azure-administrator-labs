# Lab 26 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB26-Q01`)

The lab's central distinction is: The build capstone proves that governance, identity, networking, compute, storage, and observability are coupled design decisions and must share a recorded deployment and cleanup boundary.

Objectives: IG-ACCESS-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli

## 2. B (`LAB26-Q02`)

The first implementation checkpoint is: Run Bicep build and what-if, then deploy the governed resource group and deterministic tags.

Objectives: IG-ACCESS-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/architecture/framework/

## 3. C (`LAB26-Q03`)

The documented permission boundary is Contributor, User Access Administrator, Resource Policy Contributor, and Monitoring Contributor on the capstone resource group

Objectives: IG-GOVERN-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview

## 4. D (`LAB26-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: IG-GOVERN-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings

## 5. A (`LAB26-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: IG-GOVERN-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli

## 6. B (`LAB26-Q06`)

The live-only gate is explicit and must not be guessed: Requires AZ104_PRINCIPAL_OBJECT_ID for the RBAC checkpoint; the workload path remains deployable without assigning a role when the value is absent.

Objectives: ST-ACCOUNTS-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli

## 7. C (`LAB26-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: CP-IAC-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/architecture/framework/

## 8. D (`LAB26-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: CP-VM-01, CP-VM-06

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview

## 9. A (`LAB26-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: CP-VM-06, CP-VM-07

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings

## 10. B (`LAB26-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: CP-VM-07, NW-VNET-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli
