# Lab 03 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB03-Q01`)

The lab establishes this design principle: A role definition describes allowed actions; a role assignment binds that definition to a principal at a scope, with inheritance flowing downward.

Objectives: IG-ACCESS-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell>

## 2. B (`LAB03-Q02`)

The reviewed hands-on action for this objective is: Resolve Reader and Contributor built-in role definitions without creating custom roles.

Objectives: IG-ACCESS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles>

## 3. C (`LAB03-Q03`)

Least privilege requires the documented boundary: User Access Administrator or Owner at the lab resource-group scope

Objectives: IG-ACCESS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access>

## 4. D (`LAB03-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: IG-ACCESS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell>

## 5. A (`LAB03-Q05`)

The lab's reviewed command path performs this bounded action: Create the dedicated tagged resource group.

Objectives: IG-ACCESS-02

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles>

## 6. B (`LAB03-Q06`)

The independent validation path must prove the intended recorded state for the exact recorded object.

Objectives: IG-ACCESS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access>

## 7. C (`LAB03-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: Requires the object ID of a disposable principal in AZ104_PRINCIPAL_OBJECT_ID.

Objectives: IG-ACCESS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell>

## 8. D (`LAB03-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: IG-ACCESS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles>

## 9. A (`LAB03-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: IG-ACCESS-03, IG-ACCESS-01

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access>

## 10. B (`LAB03-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: IG-ACCESS-01, IG-ACCESS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell>
