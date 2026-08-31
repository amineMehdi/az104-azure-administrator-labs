# Lab 07 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB07-Q01`)

The lab establishes this design principle: A stored access policy can revoke or change a service SAS, while account SAS and access keys have broader authority and require stricter handling.

Objectives: ST-ACCESS-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security>

## 2. B (`LAB07-Q02`)

The reviewed hands-on action for this objective is: Create a secure StorageV2 account and change the network default action to Deny.

Objectives: ST-ACCESS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview>

## 3. C (`LAB07-Q03`)

Least privilege requires the documented boundary: Contributor plus Storage Account Contributor on the lab resource group

Objectives: ST-ACCESS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy>

## 4. D (`LAB07-Q04`)

The lab records the exact scope and identity of blob container before validation and cleanup.

Objectives: ST-ACCESS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/cli/azure/storage>

## 5. A (`LAB07-Q05`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: ST-ACCESS-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security>

## 6. B (`LAB07-Q06`)

The lab's reviewed command path performs this bounded action: Create a secure StorageV2 account and change the network default action to Deny.

Objectives: ST-ACCESS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview>

## 7. C (`LAB07-Q07`)

The independent validation path must prove Microsoft.Network/virtualNetworks for the exact recorded object.

Objectives: ST-ACCESS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy>

## 8. D (`LAB07-Q08`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: ST-ACCESS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/cli/azure/storage>

## 9. A (`LAB07-Q09`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: ST-ACCESS-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security>

## 10. B (`LAB07-Q10`)

A bounded negative assertion detects accidental privilege or exposure beyond the intended state.

Objectives: ST-ACCESS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview>

## 11. C (`LAB07-Q11`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: ST-ACCESS-03, ST-ACCESS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy>

## 12. D (`LAB07-Q12`)

Accepted requests and offline checks do not prove the final live state.

Objectives: ST-ACCESS-04, ST-ACCESS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/cli/azure/storage>
