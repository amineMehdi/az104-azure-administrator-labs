# Lab 00 Knowledge Check: Answers

These explanations correspond to the questions in `QUESTIONS.md`. Each answer
is supported by current Microsoft Learn documentation and was verified on
2026-08-30.

## LAB00-Q01 · B

**Why B is correct:** Azure CLI is designed for command-line shells, including
Bash, and supports JMESPath through `--query` plus tab-separated output through
`--output tsv`. That makes it the direct fit for this shell workflow. Az
PowerShell is equally valid for Azure administration, but it uses a
PowerShell-native object pipeline rather than the requested Bash/JMESPath/TSV
workflow.

**Why the other options are wrong:**

- A. Az PowerShell returns .NET objects by default, not TSV, and would change the scripting model described in the scenario.
- C. The portal is useful for visual inspection, but it does not guarantee an exportable Bash command for every action.
- D. REST APIs can manage Azure, but manually issuing requests in a browser is not the direct, reusable command surface requested here.

Sources: [What is the Azure CLI?](https://learn.microsoft.com/en-us/cli/azure/what-is-azure-cli?view=azure-cli-latest), [query Azure CLI output](https://learn.microsoft.com/en-us/cli/azure/use-azure-cli-successfully-query?view=azure-cli-latest), and [Azure CLI output formats](https://learn.microsoft.com/en-us/cli/azure/format-output-azure-cli?view=azure-cli-latest).

## LAB00-Q02 · D

**Why D is correct:** Az PowerShell cmdlets use the current context. A safe
preflight lists accessible subscriptions, explicitly sets the intended tenant
and subscription, and reads the resulting context to compare both IDs with
expected values before any mutation.

**Why the other options are wrong:**

- A. Interactive sign-in can select a subscription, but silently trusting that selection is unsafe when the account can access several subscriptions.
- B. A default Azure region affects location parameters; it does not select an Azure subscription context.
- C. Resource names are not authoritative identity or scope evidence and might be duplicated across subscriptions.

Sources: [`Get-AzSubscription`](https://learn.microsoft.com/en-us/powershell/module/az.accounts/get-azsubscription?view=azps-15.6.0), [`Set-AzContext`](https://learn.microsoft.com/en-us/powershell/module/az.accounts/set-azcontext?view=azps-15.6.0), and [`Get-AzContext`](https://learn.microsoft.com/en-us/powershell/module/az.accounts/get-azcontext?view=azps-15.6.0).

## LAB00-Q03 · A

**Why A is correct:** Azure Cost Management budgets track cost and trigger
configured notifications when thresholds are met. Microsoft states that
resources are not affected and consumption is not stopped. A budget is an
alerting and governance mechanism, not a general-purpose hard spending cap.

**Why the other options are wrong:**

- B. Budget evaluation does not automatically deallocate virtual machines.
- C. A Cost Management budget is not automatically converted into a hard spending cap.
- D. A budget expiration or period boundary does not delete the resource group it monitors.

Source: [Create and manage Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

## LAB00-Q04 · C

**Why C is correct:** Azure CLI supports tenant-specific interactive sign-in.
After signing in to Tenant B, select the sandbox subscription by immutable ID and
verify the resulting tenant and subscription metadata before running a mutating
command.

**Why the other options are wrong:**

- A. Azure regions are shared across many tenants and subscriptions; a location cannot establish identity or subscription context.
- B. Clearing the local subscription cache removes the usable context. The user must sign in again before Azure CLI commands can run.
- D. Creating a resource to discover scope is an unsafe mutation and can place resources in the wrong subscription.

Sources: [Sign in interactively with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli-interactively?view=azure-cli-latest) and [manage Azure subscriptions with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli?view=azure-cli-latest).

## LAB00-Q05 · B

**Why B is correct:** A unique run ID distinguishes concurrent runs. Consistent
`labId` and `runId` tags support inventory and cost analysis, while exact
resource IDs in run-local state give cleanup an authoritative scope. Tags should
contain management metadata rather than personal or secret values.

**Why the other options are wrong:**

- A. Shared names can collide, and creation time is not reliable evidence of ownership.
- C. Personal information should not be embedded in resource names or tags, and an email address is not a unique run identifier.
- D. Unrecorded random names make deterministic cleanup difficult; the Activity Log is not a substitute for an explicit state manifest.

Sources: [Azure resource naming guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming) and [use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources).

## LAB00-Q06 · A

**Why A is correct:** The subscription must be able to use the relevant resource
provider, the VM SKU must be available in the target region, and the deployment
must fit both total regional and VM-family vCPU quotas. Provider registration
should be limited to services the lab is ready to use.

**Why the other options are wrong:**

- B. General website reachability says nothing about subscription provider state, regional SKU availability, or quota.
- C. Microsoft recommends registering providers only when ready to use them, and registration does not replace quota checks.
- D. VM vCPU quotas are enforced per subscription and per region, including a regional total and a VM-family tier.

Sources: [Azure resource providers and types](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types), [check vCPU quotas](https://learn.microsoft.com/en-us/azure/virtual-machines/quotas), and [`az vm list-usage`](https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-list-usage).

## LAB00-Q07 · D

**Why D is correct:** A run state file needs identifiers and lifecycle metadata,
not credentials. Tokens, passwords, access keys, and client secrets are
sensitive and must not be stored in a repository state file. Interactive
authentication is appropriate for a learner's local session; application
secrets belong in a secure secret store when genuinely required.

**Why the other options are wrong:**

- A. Access and refresh tokens are credentials. Persisting them in transferable lab state exposes the signed-in identity.
- B. A password must never be stored in the lab state file.
- C. Microsoft explicitly warns against putting credentials and secrets in source code or GitHub.

Sources: [Authenticate with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest), [secure PaaS deployments](https://learn.microsoft.com/en-us/azure/security/fundamentals/paas-deployments), and [secure Azure Key Vault secrets](https://learn.microsoft.com/en-us/azure/key-vault/secrets/secure-secrets).

## LAB00-Q08 · B

**Why B is correct:** `AuthorizationFailed` indicates that the current identity
lacks permission at the requested scope. Because the check is gated by a
declared optional role, the honest result is `skipped` with evidence of the
reason. A gated check must not be converted into a pass or hidden inside an
unqualified live-verification claim.

**Why the other options are wrong:**

- A. A nonmutating failed query did not prove the intended state, so it cannot be a pass.
- C. Reporting the whole lab as `live-verified` would overstate the evidence when a declared check could not run.
- D. Missing authorization is not a transient condition that unbounded retries can safely solve.

Sources: [Troubleshoot Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting#access-denied-or-permission-errors) and [common Azure deployment errors](https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

## LAB00-Q09 · C

**Why C is correct:** Cleanup should first confirm scope and show its intended
changes. A resource group protected by `CanNotDelete` must have the lock removed
before deletion, and a role assignment outside the group must be removed at its
own recorded scope. Exact IDs plus a residual check avoid broad,
assumption-based deletion.

**Why the other options are wrong:**

- A. A name prefix and learner identity do not prove that resources belong to this run; this could delete unrelated work and access.
- B. Unregistering a provider is not a cleanup mechanism, and Azure prevents unregistration while dependent resource types still exist.
- D. Role names are not unique assignment identifiers, and a subscription-wide deletion is far broader than the lab's ownership.

Sources: [Manage Azure resource groups with PowerShell](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-powershell#delete-resource-groups), [Azure Resource Manager resource group deletion](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/delete-resource-group), and [remove Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-remove).

## LAB00-Q10 · A

**Why A is correct:** An idempotent cleanup converges on the same clean state
when rerun. It verifies target context, reuses the original ownership evidence,
accepts an already-absent target as complete, and continues with only the
remaining exact work. Azure deletions can be asynchronous, so bounded polling
and a final residual inventory provide stronger evidence than assuming the first
request finished.

**Why the other options are wrong:**

- B. A new run ID creates new ownership metadata and must not broaden cleanup of the interrupted run.
- C. Not found can mean that the first deletion succeeded; aborting prevents the script from completing other recorded cleanup work.
- D. Similar names are not proof of ownership, so this approach risks deleting unrelated resources.

Sources: [Azure Resource Manager resource group deletion](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/delete-resource-group), [handle transient faults](https://learn.microsoft.com/en-us/azure/well-architected/design-guides/handle-transient-faults), and [Retry pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry).
