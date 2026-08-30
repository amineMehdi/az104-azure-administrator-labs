# Lab 00 Knowledge Check: Safe Bootstrap

These 10 original practice questions assess safe use of Azure CLI and Az
PowerShell, Azure account context, cost awareness, run ownership, preflight
checks, validation, and cleanup. They are learning questions, not real Microsoft
exam questions.

Choose the single best answer for each question. The answer key is intentionally
kept in `ANSWERS.md` so you can complete the knowledge check without spoilers.

## LAB00-Q01 · Foundational

A learner is writing an AZ-104 lab in Bash. The solution must use JMESPath
queries and return tab-separated values to later shell commands. Which Azure
management command surface is the most direct fit?

- A. Az PowerShell, because every Az cmdlet returns tab-separated text by default.
- B. Azure CLI, because it runs naturally in Bash and supports `--query` with `--output tsv`.
- C. Azure portal, because every portal action can be exported as a reusable Bash command.
- D. Azure Resource Manager REST API entered manually in a web browser.

## LAB00-Q02 · Foundational

You are signed in through Az PowerShell and can access several subscriptions.
Before a script creates any resources, which sequence most safely establishes
and verifies the intended subscription context?

- A. Run `Connect-AzAccount`, accept whichever subscription is selected, and begin creating resources.
- B. Set a default location and assume that this also selects the Azure subscription.
- C. Run `Get-AzResourceGroup` and infer the active subscription from familiar resource names.
- D. List accessible subscriptions with `Get-AzSubscription`, set the target tenant and subscription with `Set-AzContext`, then compare `Get-AzContext` with the expected IDs.

## LAB00-Q03 · Foundational

A learner creates a monthly Azure Cost Management budget of EUR 10 with an
alert at 100 percent. What should the learner expect when evaluated cost
reaches the threshold?

- A. The configured notification is triggered, but Azure resources keep running unless a separate action is designed to affect them.
- B. Azure immediately deallocates every virtual machine in the budget scope.
- C. Azure converts the budget into a hard spending cap and rejects all subsequent requests.
- D. The resource group is automatically deleted at the end of the evaluation period.

## LAB00-Q04 · Applied

An administrator belongs to Tenant A and Tenant B. The sandbox subscription is
in Tenant B, but the current Azure CLI context points to Tenant A. Which action
sequence is safest before running a lab setup script?

- A. Pass only `--location` to the setup commands, because a region uniquely identifies the tenant.
- B. Run `az account clear` and start the setup script without signing in again.
- C. Sign in with `az login --tenant` for Tenant B, set the sandbox subscription by ID, and verify both IDs with `az account show`.
- D. Create the resource group first, then use its deployment history to discover which tenant received it.

## LAB00-Q05 · Applied

Two learners may run the same lab concurrently in one subscription. Which
design best reduces naming collisions and makes later cleanup safely scoped to
one run?

- A. Use identical resource names for every run and delete whichever resources were created most recently.
- B. Include a unique run ID in eligible names, tag taggable resources with `labId` and `runId`, and record the exact created resource IDs in run-local state.
- C. Put the learner's email address in every resource name and tag, then delete all resources with that email address.
- D. Use random names without recording them because Azure Activity Log can always reconstruct every dependency immediately.

## LAB00-Q06 · Applied

A lab will deploy a D-family virtual machine in West Europe. Which preflight is
most likely to catch subscription-specific blockers before the deployment
starts?

- A. Check the `Microsoft.Compute` provider state, register it only if required, verify the requested SKU is available in the region, and inspect both total regional and D-family vCPU usage and limits.
- B. Check only whether `azure.microsoft.com` is reachable from the learner's browser.
- C. Register every resource provider in the subscription and skip quota checks.
- D. Check quota in any one Azure region because vCPU quota is shared globally across all regions.

## LAB00-Q07 · Applied

A lab needs a local state file so validation and cleanup can resume after an
interruption. Which content is safest to persist in that file?

- A. The current Azure CLI access token and refresh token so another learner can resume the run.
- B. The administrator's password together with the tenant ID and subscription ID.
- C. Storage account keys and service principal client secrets, committed to Git for portability.
- D. Nonsecret metadata such as tenant ID, subscription ID, run ID, tags, exact resource IDs, timestamps, and lifecycle status; credentials remain outside the file.

## LAB00-Q08 · Applied

An optional validation check requires a role the learner does not have. The
read-only query returns `AuthorizationFailed`, and the lab documentation clearly
declared the role as an optional prerequisite. How should the validation report
represent this result?

- A. Mark it `pass` because no Azure resources changed.
- B. Mark the check `skipped` with the permission reason and keep the overall lab `partial` unless every required check still passed independently.
- C. Mark it `warning` but silently report the whole lab as `live-verified`.
- D. Retry the request indefinitely until Azure grants the missing permission.

## LAB00-Q09 · Advanced

A lab run created a resource group, a `CanNotDelete` lock on that group, and a
subscription-scope role assignment. Which cleanup workflow has the narrowest
safe deletion scope?

- A. Delete every resource group whose name begins with `az104`, then remove all role assignments for the learner.
- B. Unregister the resource providers used by the lab and assume Azure removes the resources that depended on them.
- C. Verify the recorded tenant and subscription, print the exact deletion plan, remove the recorded role assignment and lock by ID, delete the recorded resource group, wait for deletion, and query for residual run resources.
- D. Delete the subscription-scope role assignment by matching only its role name, then issue a subscription-wide resource deletion.

## LAB00-Q10 · Advanced

Cleanup was interrupted after Azure accepted deletion of the lab's recorded
resource group but before the script updated local state. What behavior makes a
second cleanup run safely idempotent?

- A. Reconfirm context, read the same recorded IDs, treat an already-absent target as clean, resume only remaining exact deletions with bounded handling for asynchronous operations, and finish with a residual check.
- B. Generate a new run ID and delete resources associated with both the old and new IDs.
- C. Fail immediately whenever a recorded resource returns not found, leaving all remaining cleanup steps unattempted.
- D. Search the subscription for similarly named resources and delete them all to guarantee that nothing remains.
