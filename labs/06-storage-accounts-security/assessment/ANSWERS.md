# Lab 06 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB06-Q01`)

The lab establishes this design principle: Redundancy protects copies of data, encryption protects data at rest, and access keys are broad secrets that must be rotated without entering state or command evidence.

Objectives: ST-ACCESS-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create>

## 2. B (`LAB06-Q02`)

The reviewed hands-on action for this objective is: Require HTTPS, TLS 1.2, and disabled anonymous blob access.

Objectives: ST-ACCOUNTS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy>

## 3. C (`LAB06-Q03`)

Least privilege requires the documented boundary: Contributor on the lab resource group

Objectives: ST-ACCOUNTS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption>

## 4. D (`LAB06-Q04`)

The lab records the exact scope and identity of StorageV2 account before validation and cleanup.

Objectives: ST-ACCOUNTS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage>

## 5. A (`LAB06-Q05`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: ST-ACCESS-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create>

## 6. B (`LAB06-Q06`)

The lab's reviewed command path performs this bounded action: Require HTTPS, TLS 1.2, and disabled anonymous blob access.

Objectives: ST-ACCOUNTS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy>

## 7. C (`LAB06-Q07`)

The independent validation path must prove Microsoft.Storage/storageAccounts for the exact recorded object.

Objectives: ST-ACCOUNTS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption>

## 8. D (`LAB06-Q08`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: ST-ACCOUNTS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage>

## 9. A (`LAB06-Q09`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: ST-ACCESS-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create>

## 10. B (`LAB06-Q10`)

A bounded negative assertion detects accidental privilege or exposure beyond the intended state.

Objectives: ST-ACCOUNTS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy>

## 11. C (`LAB06-Q11`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: ST-ACCOUNTS-02, ST-ACCOUNTS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption>

## 12. D (`LAB06-Q12`)

Accepted requests and offline checks do not prove the final live state.

Objectives: ST-ACCOUNTS-04, ST-ACCESS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage>
