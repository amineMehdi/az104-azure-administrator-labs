# Lab 16 answer key

Return to [the questions](QUESTIONS.md).

## 1. D (`LAB16-Q01`)

The lab establishes this design principle: Custom hostnames prove DNS control, certificate bindings prove TLS identity, VNet integration governs outbound connectivity, and backups require protected storage access.

Objectives: CP-APP-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings>

## 2. A (`LAB16-Q02`)

The reviewed hands-on action for this objective is: Create a delegated integration subnet and configure regional VNet integration.

Objectives: CP-APP-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain>

## 3. B (`LAB16-Q03`)

Least privilege requires the documented boundary: Website Contributor, Network Contributor, and Storage Account Contributor; control of the DNS zone and certificate for gated paths

Objectives: CP-APP-06

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/app-service/manage-backup>

## 4. C (`LAB16-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: CP-APP-07

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration>

## 5. D (`LAB16-Q05`)

The lab's reviewed command path performs this bounded action: Create an App Service plan and web app with HTTPS-only and minimum TLS 1.2.

Objectives: CP-APP-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings>

## 6. A (`LAB16-Q06`)

The independent validation path must prove Microsoft.Web/sites for the exact recorded object.

Objectives: CP-APP-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain>

## 7. B (`LAB16-Q07`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: CP-APP-06, CP-APP-07

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/azure/app-service/manage-backup>
