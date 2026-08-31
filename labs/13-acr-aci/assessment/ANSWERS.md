# Lab 13 answer key

Return to [the questions](QUESTIONS.md).

## 1. C (`LAB13-Q01`)

The lab establishes this design principle: ACR stores image artifacts and ACI runs container groups; registry admin credentials are not required when managed identities or scoped tokens are available.

Objectives: CP-CONTAINERS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli>

## 2. D (`LAB13-Q02`)

The reviewed hands-on action for this objective is: Import a public Microsoft sample image and inspect repository and tag metadata.

Objectives: CP-CONTAINERS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images>

## 3. A (`LAB13-Q03`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: CP-CONTAINERS-04

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart>

## 4. B (`LAB13-Q04`)

The lab's reviewed command path performs this bounded action: Inspect CPU, memory, restart policy, events, logs, and current container state.

Objectives: CP-CONTAINERS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-groups>

## 5. C (`LAB13-Q05`)

The independent validation path must prove Microsoft.ContainerRegistry/registries for the exact recorded object.

Objectives: CP-CONTAINERS-02

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli>

## 6. D (`LAB13-Q06`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: CP-CONTAINERS-04, CP-CONTAINERS-01

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images>
