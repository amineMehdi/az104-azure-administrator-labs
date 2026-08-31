# Lab 09 answer key

Return to [the questions](QUESTIONS.md).

## 1. C (`LAB09-Q01`)

The lab establishes this design principle: Share snapshots and soft delete solve different recovery problems, while identity-based SMB authentication requires an approved directory source and data-plane authorization.

Objectives: ST-ACCESS-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share>

## 2. D (`LAB09-Q02`)

The reviewed hands-on action for this objective is: Enable Azure Files share soft delete and create a point-in-time share snapshot.

Objectives: ST-ACCOUNTS-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files>

## 3. A (`LAB09-Q03`)

Least privilege requires the documented boundary: Contributor and Storage File Data SMB Share Contributor; directory permissions for the optional identity-source path

Objectives: ST-DATA-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion>

## 4. B (`LAB09-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: ST-DATA-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview>

## 5. C (`LAB09-Q05`)

The lab's reviewed command path performs this bounded action: Create a secure StorageV2 account and transaction-optimized file share with quota.

Objectives: ST-ACCESS-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files>

## 6. D (`LAB09-Q06`)

The independent validation path must prove Microsoft.Storage/storageAccounts/fileServices/shares for the exact recorded object.

Objectives: ST-ACCOUNTS-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share>

## 7. A (`LAB09-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: Identity-based SMB configuration is gated by AZ104_FILES_IDENTITY_SOURCE because Entra Kerberos, AD DS, and Entra Domain Services have different prerequisites.

Objectives: ST-DATA-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files>

## 8. B (`LAB09-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: ST-DATA-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion>

## 9. C (`LAB09-Q09`)

A bounded negative assertion detects accidental privilege or exposure beyond the intended state.

Objectives: ST-ACCESS-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview>

## 10. D (`LAB09-Q10`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: ST-ACCOUNTS-05, ST-DATA-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files>

## 11. A (`LAB09-Q11`)

Accepted requests and offline checks do not prove the final live state.

Objectives: ST-DATA-01, ST-DATA-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share>

## 12. B (`LAB09-Q12`)

The narrowest evidence-supported correction avoids unrelated changes and excess privilege.

Objectives: ST-DATA-05, ST-ACCESS-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files>
