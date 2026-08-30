# Lab 08 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB08-Q01`)

The lab's central distinction is: Object replication depends on versioning and change feed, while lifecycle rules act asynchronously and should be validated as configuration rather than immediate data movement.

Objectives: ST-ACCOUNTS-03

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview

## 2. B (`LAB08-Q02`)

The first implementation checkpoint is: Create source and destination general-purpose v2 accounts with change feed and blob versioning.

Objectives: ST-ACCOUNTS-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview

## 3. C (`LAB08-Q03`)

The documented permission boundary is Contributor and Storage Blob Data Contributor on the lab resource group

Objectives: ST-DATA-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview

## 4. D (`LAB08-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: ST-DATA-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview

## 5. A (`LAB08-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: ST-DATA-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10

## 6. B (`LAB08-Q06`)

The live-only gate is explicit and must not be guessed: None beyond the declared role and a disposable subscription.

Objectives: ST-DATA-06

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview

## 7. C (`LAB08-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: ST-DATA-07

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview

## 8. D (`LAB08-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: ST-ACCOUNTS-03, ST-ACCOUNTS-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview

## 9. A (`LAB08-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: ST-ACCOUNTS-05, ST-DATA-02

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview

## 10. B (`LAB08-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: ST-DATA-02, ST-DATA-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10
