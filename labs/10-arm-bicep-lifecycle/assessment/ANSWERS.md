# Lab 10 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB10-Q01`)

The lab establishes this design principle: Bicep compiles to ARM JSON, what-if predicts control-plane changes, and exported/decompiled templates require human review rather than being treated as pristine source.

Objectives: CP-IAC-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview>

## 2. B (`LAB10-Q02`)

The reviewed hands-on action for this objective is: Modify parameter values and run a resource-group what-if before deployment.

Objectives: CP-IAC-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli>

## 3. C (`LAB10-Q03`)

Least privilege requires the documented boundary: Contributor on the lab resource group

Objectives: CP-IAC-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile>

## 4. D (`LAB10-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: CP-IAC-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal>

## 5. A (`LAB10-Q05`)

The lab's reviewed command path performs this bounded action: Build and lint the supplied Bicep file and inspect its generated ARM JSON.

Objectives: CP-IAC-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview>

## 6. B (`LAB10-Q06`)

The independent validation path must prove Microsoft.Storage/storageAccounts for the exact recorded object.

Objectives: CP-IAC-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli>

## 7. C (`LAB10-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: None beyond the declared role and a disposable subscription.

Objectives: CP-IAC-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile>

## 8. D (`LAB10-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: CP-IAC-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal>

## 9. A (`LAB10-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: CP-IAC-04, CP-IAC-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview>

## 10. B (`LAB10-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: CP-IAC-05, CP-IAC-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli>
