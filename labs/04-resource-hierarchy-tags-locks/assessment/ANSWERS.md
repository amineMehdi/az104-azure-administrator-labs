# Lab 04 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB04-Q01`)

The lab's central distinction is: Tags are metadata rather than access controls, and resource locks protect the control plane without replacing RBAC or data-plane protection.

Objectives: IG-GOVERN-02

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli>

## 2. B (`LAB04-Q02`)

The first implementation checkpoint is: Create a resource group with purpose, labId, runId, owner, and expiresOn tags.

Objectives: IG-GOVERN-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli>

## 3. C (`LAB04-Q03`)

The documented permission boundary is Contributor plus User Access Administrator for lock management; Management Group Contributor for the optional hierarchy path

Objectives: IG-GOVERN-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>

## 4. D (`LAB04-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: IG-GOVERN-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal>

## 5. A (`LAB04-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: IG-GOVERN-07

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli>

## 6. B (`LAB04-Q06`)

The live-only gate is explicit and must not be guessed: Management-group creation is optional and requires explicit tenant hierarchy authorization.

Objectives: IG-GOVERN-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli>

## 7. C (`LAB04-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: IG-GOVERN-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>

## 8. D (`LAB04-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: IG-GOVERN-04, IG-GOVERN-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal>

## 9. A (`LAB04-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: IG-GOVERN-05, IG-GOVERN-07

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli>

## 10. B (`LAB04-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: IG-GOVERN-07, IG-GOVERN-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli>
