# Lab 04 answer key

Return to [the questions](QUESTIONS.md).

## 1. C (`LAB04-Q01`)

The lab establishes this design principle: Tags are metadata rather than access controls, and resource locks protect the control plane without replacing RBAC or data-plane protection.

Objectives: IG-GOVERN-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli>

## 2. D (`LAB04-Q02`)

The reviewed hands-on action for this objective is: Update tags using merge semantics and verify which values do not inherit automatically.

Objectives: IG-GOVERN-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli>

## 3. A (`LAB04-Q03`)

Least privilege requires the documented boundary: Contributor plus User Access Administrator for lock management; Management Group Contributor for the optional hierarchy path

Objectives: IG-GOVERN-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>

## 4. B (`LAB04-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: IG-GOVERN-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal>

## 5. C (`LAB04-Q05`)

The lab's reviewed command path performs this bounded action: Create a resource group with purpose, labId, runId, owner, and expiresOn tags.

Objectives: IG-GOVERN-07

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli>

## 6. D (`LAB04-Q06`)

The independent validation path must prove Microsoft.Authorization/locks for the exact recorded object.

Objectives: IG-GOVERN-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli>

## 7. A (`LAB04-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: Management-group creation is optional and requires explicit tenant hierarchy authorization.

Objectives: IG-GOVERN-03

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>

## 8. B (`LAB04-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: IG-GOVERN-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal>

## 9. C (`LAB04-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: IG-GOVERN-05, IG-GOVERN-07

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli>

## 10. D (`LAB04-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: IG-GOVERN-07, IG-GOVERN-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli>
