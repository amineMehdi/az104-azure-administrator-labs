# Lab 15 answer key

Return to [the questions](QUESTIONS.md).

## 1. A (`LAB15-Q01`)

The lab's central distinction is: App Service plan scale affects workers shared by apps, while deployment slots isolate deployable content and selected sticky configuration before a controlled swap.

Objectives: CP-APP-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/quickstart-powershell

## 2. B (`LAB15-Q02`)

The first implementation checkpoint is: Create a Linux App Service plan and web app with deterministic names.

Objectives: CP-APP-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up

## 3. C (`LAB15-Q03`)

The documented permission boundary is Website Contributor and Monitoring Contributor on the lab resource group

Objectives: CP-APP-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/manage-scale-per-app

## 4. D (`LAB15-Q04`)

Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.

Objectives: CP-APP-08

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots

## 5. A (`LAB15-Q05`)

Validation must use the recorded scope and test the intended state independently of setup.

Objectives: CP-APP-01

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/quickstart-powershell

## 6. B (`LAB15-Q06`)

The live-only gate is explicit and must not be guessed: None beyond the declared role and a disposable subscription.

Objectives: CP-APP-02

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up

## 7. C (`LAB15-Q07`)

Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.

Objectives: CP-APP-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/manage-scale-per-app

## 8. D (`LAB15-Q08`)

Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.

Objectives: CP-APP-08, CP-APP-01

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots

## 9. A (`LAB15-Q09`)

Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.

Objectives: CP-APP-01, CP-APP-02

Why the other choices do not fit:

- **B:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/quickstart-powershell

## 10. B (`LAB15-Q10`)

Offline validation proves artifact quality and safety contracts, not live service behavior.

Objectives: CP-APP-02, CP-APP-03

Why the other choices do not fit:

- **A:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **C:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.
- **D:** This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state.

Source: https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up
