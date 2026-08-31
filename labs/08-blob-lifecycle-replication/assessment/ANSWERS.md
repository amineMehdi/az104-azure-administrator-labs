# Lab 08 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB08-Q01`)

The lab establishes this design principle: Object replication depends on versioning and change feed, while lifecycle rules act asynchronously and should be validated as configuration rather than immediate data movement.

Objectives: ST-ACCOUNTS-03

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview>

## 2. B (`LAB08-Q02`)

The reviewed hands-on action for this objective is: Enable blob and container soft delete and create private containers.

Objectives: ST-ACCOUNTS-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview>

## 3. C (`LAB08-Q03`)

Least privilege requires the documented boundary: Contributor and Storage Blob Data Contributor on the lab resource group

Objectives: ST-DATA-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview>

## 4. D (`LAB08-Q04`)

The lab records the exact scope and identity of lifecycle policy before validation and cleanup.

Objectives: ST-DATA-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview>

## 5. A (`LAB08-Q05`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: ST-DATA-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10>

## 6. B (`LAB08-Q06`)

The lab's reviewed command path performs this bounded action: Enable blob and container soft delete and create private containers.

Objectives: ST-DATA-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview>

## 7. C (`LAB08-Q07`)

The independent validation path must prove Microsoft.Storage/storageAccounts for the exact recorded object.

Objectives: ST-DATA-07

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview>

## 8. D (`LAB08-Q08`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: ST-ACCOUNTS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview>

## 9. A (`LAB08-Q09`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: ST-ACCOUNTS-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview>

## 10. B (`LAB08-Q10`)

A bounded negative assertion detects accidental privilege or exposure beyond the intended state.

Objectives: ST-DATA-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10>

## 11. C (`LAB08-Q11`)

Immutable recorded IDs create a deterministic validation and cleanup boundary.

Objectives: ST-DATA-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview>

## 12. D (`LAB08-Q12`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: ST-DATA-04, ST-DATA-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview>

## 13. A (`LAB08-Q13`)

Accepted requests and offline checks do not prove the final live state.

Objectives: ST-DATA-06, ST-DATA-07

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview>

## 14. B (`LAB08-Q14`)

The narrowest evidence-supported correction avoids unrelated changes and excess privilege.

Objectives: ST-DATA-07, ST-ACCOUNTS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview>
