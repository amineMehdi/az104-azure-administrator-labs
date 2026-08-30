# Lab 03 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB03-Q01`)

The lab's central distinction is: A role definition describes allowed actions; a role assignment binds that definition to a principal at a scope, with inheritance flowing downward.

Objectives: IG-ACCESS-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell

## 2. B (`LAB03-Q02`)

The first implementation checkpoint is: Create the dedicated tagged resource group.

Objectives: IG-ACCESS-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles

## 3. C (`LAB03-Q03`)

The documented permission boundary is User Access Administrator or Owner at the lab resource-group scope

Objectives: IG-ACCESS-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access

## 4. D (`LAB03-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: IG-ACCESS-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell

## 5. A (`LAB03-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: IG-ACCESS-02

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles

## 6. B (`LAB03-Q06`)

The live-only gate is explicit and must not be guessed: Requires the object ID of a disposable principal in AZ104_PRINCIPAL_OBJECT_ID.

Objectives: IG-ACCESS-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access

## 7. C (`LAB03-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: IG-ACCESS-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell

## 8. D (`LAB03-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: IG-ACCESS-02, IG-ACCESS-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles

## 9. A (`LAB03-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: IG-ACCESS-03, IG-ACCESS-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access

## 10. B (`LAB03-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: IG-ACCESS-01, IG-ACCESS-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell
