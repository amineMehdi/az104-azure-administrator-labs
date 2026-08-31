# Lab 02 answer key

Return to [the questions](QUESTIONS.md).

## 1. C (`LAB02-Q01`)

The lab establishes this design principle: SSPR and group-based licensing are tenant capabilities with role and license gates; inventory and scoped pilots are safer than tenant-wide changes.

Objectives: IG-USERS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info>

## 2. D (`LAB02-Q02`)

The reviewed hands-on action for this objective is: Invite a disposable external account only when AZ104_GUEST_EMAIL is supplied.

Objectives: IG-USERS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/external-id/b2b-quickstart-invite-powershell>

## 3. A (`LAB02-Q03`)

Least privilege requires the documented boundary: User Administrator and License Administrator; Authentication Policy Administrator for the SSPR policy path

Objectives: IG-USERS-05

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/identity/users/licensing-powershell-graph-examples>

## 4. B (`LAB02-Q04`)

Preview mode is deliberately non-mutating and exposes the complete intended boundary.

Objectives: IG-USERS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-sspr>

## 5. C (`LAB02-Q05`)

The lab's reviewed command path performs this bounded action: Create a security group that represents the SSPR pilot cohort.

Objectives: IG-USERS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info>

## 6. D (`LAB02-Q06`)

The independent validation path must prove the intended recorded state for the exact recorded object.

Objectives: IG-USERS-05

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/external-id/b2b-quickstart-invite-powershell>

## 7. A (`LAB02-Q07`)

Unavailable live prerequisites remain skipped or partial; the documented gate is: Requires a real disposable guest email for invitation, an available SKU for license assignment, and an authorized tenant policy change for SSPR.

Objectives: IG-USERS-03

Why the other choices do not fit:

- **B:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/identity/users/licensing-powershell-graph-examples>

## 8. B (`LAB02-Q08`)

Evidence must come from the current run, prove state independently, and exclude secrets and identifiers.

Objectives: IG-USERS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **C:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-sspr>

## 9. C (`LAB02-Q09`)

Evidence-led repair preserves scope and makes the cause and correction auditable.

Objectives: IG-USERS-05, IG-USERS-03

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **D:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info>

## 10. D (`LAB02-Q10`)

Accepted requests and offline checks do not prove the final live state.

Objectives: IG-USERS-03, IG-USERS-04

Why the other choices do not fit:

- **A:** This choice changes or trusts a broader scope than the recorded lab boundary.
- **B:** This choice skips independent evidence or relies on ambiguous resource identity.
- **C:** This choice conflicts with the lab's authorization, safety, or truthful-status contract.

Source: <https://learn.microsoft.com/en-us/entra/external-id/b2b-quickstart-invite-powershell>
