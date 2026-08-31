# Lab 14 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB14-Q01`)

The lab establishes this design principle: Container Apps revisions are immutable deployment snapshots, while replicas scale within an active revision according to minimum, maximum, and event rules.

Objectives: CP-CONTAINERS-03

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-apps/get-started>

## 2. B (`LAB14-Q02`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: CP-CONTAINERS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-apps/revisions>

## 3. C (`LAB14-Q03`)

The lab's reviewed command path performs this bounded action: Create a new revision by changing an environment variable and split traffic deliberately.

Objectives: CP-CONTAINERS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-apps/scale-app>

## 4. D (`LAB14-Q04`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: CP-CONTAINERS-04, CP-CONTAINERS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview>
