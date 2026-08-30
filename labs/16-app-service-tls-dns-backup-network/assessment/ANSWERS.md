# Lab 16 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB16-Q01`)

The lab's central distinction is: Custom hostnames prove DNS control, certificate bindings prove TLS identity, VNet integration governs outbound connectivity, and backups require protected storage access.

Objectives: CP-APP-04

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings>

## 2. B (`LAB16-Q02`)

The first implementation checkpoint is: Create an App Service plan and web app with HTTPS-only and minimum TLS 1.2.

Objectives: CP-APP-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain>

## 3. C (`LAB16-Q03`)

The documented permission boundary is Website Contributor, Network Contributor, and Storage Account Contributor; control of the DNS zone and certificate for gated paths

Objectives: CP-APP-06

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/manage-backup>

## 4. D (`LAB16-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: CP-APP-07

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration>

## 5. A (`LAB16-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: NW-DNSLB-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings>

## 6. B (`LAB16-Q06`)

The live-only gate is explicit and must not be guessed: Custom DNS and certificate steps require AZ104_CUSTOM_HOSTNAME plus an owned DNS zone and an authorized certificate; they remain gated otherwise.

Objectives: CP-APP-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain>

## 7. C (`LAB16-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: CP-APP-05

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/manage-backup>

## 8. D (`LAB16-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: CP-APP-06, CP-APP-07

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration>

## 9. A (`LAB16-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: CP-APP-07, NW-DNSLB-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings>

## 10. B (`LAB16-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: NW-DNSLB-01, CP-APP-04

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: <https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain>
