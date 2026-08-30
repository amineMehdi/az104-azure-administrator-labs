# Lab 07 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB07-Q01`)

The lab's central distinction is: A stored access policy can revoke or change a service SAS, while account SAS and access keys have broader authority and require stricter handling.

Objectives: ST-ACCESS-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security>

## 2. B (`LAB07-Q02`)

The first implementation checkpoint is: Create a virtual network subnet with the Microsoft.Storage service endpoint.

Objectives: ST-ACCESS-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview>

## 3. C (`LAB07-Q03`)

The documented permission boundary is Contributor plus Storage Account Contributor on the lab resource group

Objectives: ST-ACCESS-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy>

## 4. D (`LAB07-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: ST-ACCESS-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/powershell/module/az.storage/>

## 5. A (`LAB07-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: ST-ACCESS-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security>

## 6. B (`LAB07-Q06`)

The live-only gate is explicit and must not be guessed: None beyond the declared role and a disposable subscription.

Objectives: ST-ACCESS-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview>

## 7. C (`LAB07-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: ST-ACCESS-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy>

## 8. D (`LAB07-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: ST-ACCESS-04, ST-ACCESS-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/powershell/module/az.storage/>

## 9. A (`LAB07-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: ST-ACCESS-01, ST-ACCESS-02

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security>

## 10. B (`LAB07-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: ST-ACCESS-02, ST-ACCESS-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview>
