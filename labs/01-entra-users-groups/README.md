# Lab 01 — Create and manage Microsoft Entra users and groups

> **Status:** Offline-validated; tenant execution and real Portal evidence are pending authorization.
> **Blueprint:** AZ-104 skills measured as of 2026-04-17.
> **Tenant changes:** Two cloud-only users, one security group, one membership, and one owner assignment.

Your organization is preparing a small Azure operations team. You must create two cloud-only identities, maintain useful user and group properties, give one user membership in an operations group, make the other user the group owner, prove the resulting state, and remove only the identities created by this run.

This lab uses Azure CLI's GA Microsoft Entra commands plus `az rest` for Microsoft Graph properties that the simplified `az ad` commands do not expose.

## Objectives

This lab directly covers:

| Objective | Skill practiced |
|---|---|
| `IG-USERS-01` | Create cloud-only users and a Microsoft Entra security group. |
| `IG-USERS-02` | Manage display, department, job title, office, group description, membership, and ownership properties. |

By the end, you can:

- distinguish Microsoft Entra roles from Azure RBAC roles;
- create cloud-only member users with verified-domain UPNs;
- create and describe a security group;
- manage direct group members and owners by object ID;
- validate positive state and a negative control;
- repair membership drift; and
- clean up active objects without broad tenant searches.

## Architecture

![Azure CLI uses Microsoft Graph to manage two cloud users and a security group while local state records exact object IDs for validation and cleanup.](diagrams/architecture.svg)

User A becomes a direct member. User B becomes the owner but deliberately remains outside the membership list. That difference creates a useful negative validation control.

## Time, cost, permissions, and risk

- **Time:** 60–75 minutes
- **Difficulty:** Foundational
- **Azure resource cost:** None
- **Licenses assigned:** None
- **Recommended directory role:** Microsoft Entra User Administrator in the disposable tenant
- **Azure RBAC role required:** None
- **Region:** Not applicable; Microsoft Entra objects are tenant-scoped
- **Safe-stop point:** Before setup is rerun with `--execute`
- **Cleanup behavior:** Group deletion is immediate; user deletion is recoverable unless separately purged

Use a dedicated non-production tenant. Owner or Contributor on an Azure subscription does not grant user-management permissions in Microsoft Entra ID. Conversely, User Administrator does not make someone Owner of Azure subscriptions.

This exercise does not require a paid license for the basic cloud-only users and security group it creates. Tenant policies, administrative units, restricted management administrative units, or protected accounts can still affect authorization. Never target production identities or privileged administrators.

## Command lane and offline-tested tools

The canonical lane is Bash with Azure CLI:

| Tool | Offline-tested version |
|---|---|
| Azure CLI | 2.88.0 |
| Bash | Git for Windows / GNU-compatible Bash |
| jq | 1.6 or newer |

Run commands from this lab directory. Azure Cloud Shell, a Linux dev container, WSL, or Git Bash can provide the Bash lane. The repository dev container is the most reproducible choice.

## What the scripts store

Setup creates a local manifest:

```text
.state/<run-id>/
└── run.json
```

Validation adds `validation.json`. State contains tenant ID, verified domain, synthetic display names, UPNs, exact object IDs, and expected properties. It never contains the temporary password, tokens, cookies, or Azure CLI credential cache.

The two user-creation request files exist only transiently with restrictive local permissions and are removed immediately after the Graph request. Do not run setup with shell tracing such as `bash -x` because tracing can expose secrets.

## Before you begin

1. Obtain permission to create and delete identities in a disposable tenant.
2. Confirm your signed-in administrator has the required Microsoft Entra role.
3. Choose one verified tenant domain, commonly a tenant's `*.onmicrosoft.com` domain.
4. Sign in yourself and review the tenant. Lab scripts never perform login or context changes.

```bash
az login --tenant '<sandbox-tenant-id>'
az account show --output table
az ad signed-in-user show \
  --query '{displayName:displayName,userPrincipalName:userPrincipalName,id:id}' \
  --output table
```

If you deliberately change tenants or subscriptions, do so before the lab and rerun the context checks. Do not hide context selection inside reusable scripts.

Set working values:

```bash
TENANT_ID='<sandbox-tenant-id>'
DOMAIN='<verified-tenant-domain>'
RUN_ID="az104l01-$(date -u +%Y%m%d%H%M%S)"
```

The run ID accepts 3–21 lowercase letters, digits, or hyphens.

## Checkpoint 1 — Preflight the directory context

Predict whether an Azure subscription Owner without a Microsoft Entra role can create users. Then run the read-only preflight:

```bash
./scripts/cli/preflight.sh \
  --tenant-id "$TENANT_ID" \
  --domain "$DOMAIN"
```

Preflight verifies:

- Azure CLI and jq are available;
- the active Azure CLI context has the expected tenant ID;
- Microsoft Graph is reachable with the signed-in identity;
- the supplied domain exists and is verified; and
- basic user discovery is readable.

It cannot prove write authorization without attempting a write. If preflight passes but setup receives `Authorization_RequestDenied`, review the Microsoft Entra role assignment and scope rather than assigning an Azure subscription role.

## Checkpoint 2 — Review and create users

First run setup without `--execute`:

```bash
./scripts/cli/setup.sh \
  --run-id "$RUN_ID" \
  --tenant-id "$TENANT_ID" \
  --domain "$DOMAIN"
```

Expected result: a plan lists two UPNs and one group, but no state directory or tenant object is created.

When the tenant and names are correct, enter a policy-compliant temporary password without putting it in shell history:

```bash
read -rsp 'Temporary password for both disposable lab users: ' AZ104_LAB_INITIAL_PASSWORD
echo
export AZ104_LAB_INITIAL_PASSWORD

./scripts/cli/setup.sh \
  --run-id "$RUN_ID" \
  --tenant-id "$TENANT_ID" \
  --domain "$DOMAIN" \
  --execute

unset AZ104_LAB_INITIAL_PASSWORD
```

The password must satisfy the tenant's password policy. Both users are configured to change it at first sign-in, but this lab never signs in as either user.

Setup performs these actions:

1. Creates user A and user B through Microsoft Graph.
2. Applies department, job title, and office location properties.
3. Creates a security group with `az ad group create`.
4. Changes the group description through a Graph `PATCH` request.
5. Adds user A as a direct member.
6. Adds user B as an owner.
7. Records exact object IDs in `run.json`.

Inspect only the safe state fields:

```bash
jq '{labId,runId,tenantId,domain,status,names,resources,relationships,expected,passwordStored}' \
  ".state/$RUN_ID/run.json"
```

Expected result: three resources are recorded and `passwordStored` is `false`.

### Portal evidence: users

Open the [Microsoft Entra admin center](https://entra.microsoft.com), go to **Identity > Users > All users**, and filter using the `AZ104-L01-<run-id>` display-name prefix. Confirm both accounts are enabled.

After a live run, capture the sanitized evidence described in `images/manifest.yml` as `portal/01-lab-users.png`. Do not capture the temporary password, other users, or personal browser information.

## Checkpoint 3 — Inspect managed properties

Read the exact object IDs from state:

```bash
USER_A_ID=$(jq -r '.relationships.memberUserId' ".state/$RUN_ID/run.json")
USER_B_ID=$(jq -r '.relationships.ownerUserId' ".state/$RUN_ID/run.json")
GROUP_ID=$(jq -r '.relationships.groupId' ".state/$RUN_ID/run.json")
```

Inspect user properties through Graph:

```bash
az rest \
  --method get \
  --url "https://graph.microsoft.com/v1.0/users/$USER_A_ID?\$select=displayName,userPrincipalName,accountEnabled,department,jobTitle,officeLocation" \
  --output json
```

Inspect the group:

```bash
az rest \
  --method get \
  --url "https://graph.microsoft.com/v1.0/groups/$GROUP_ID?\$select=displayName,mailNickname,description,securityEnabled,mailEnabled" \
  --output json
```

Expected group type: `securityEnabled=true` and `mailEnabled=false`. Its description contains this run ID. Display names are convenient for people but are not safe cleanup identifiers because directories can contain duplicates.

Capture `portal/02-group-properties.png` only after a live run and sanitization.

## Checkpoint 4 — Compare membership and ownership

Check the direct member:

```bash
az ad group member check \
  --group "$GROUP_ID" \
  --member-id "$USER_A_ID" \
  --output json
```

Expected: `value` is `true`.

List owners and members separately:

```bash
az ad group member list \
  --group "$GROUP_ID" \
  --query '[].{displayName:displayName,id:id}' \
  --output table

az ad group owner list \
  --group "$GROUP_ID" \
  --query '[].{displayName:displayName,id:id}' \
  --output table
```

User B owns the group but is not automatically a member. Ownership grants group-management capability according to tenant policy; it does not grant access that is assigned to group members.

Capture the sanitized member and owner blades as `portal/03-group-members.png` and `portal/04-group-owners.png`.

## Checkpoint 5 — Validate positive and negative state

Run the read-only validator:

```bash
./scripts/cli/validate.sh --run-id "$RUN_ID"
jq '{result,checks}' ".state/$RUN_ID/validation.json"
```

Expected checks include:

- tenant context matches;
- both users have their exact expected properties;
- the group is a non-mail-enabled security group with the managed description;
- user A is a member;
- user B is not a member—the negative control; and
- user B is an owner.

Exit code `0` means pass, `1` means one or more required checks failed, and `2` means partial validation with warnings. The validator never repairs drift.

## Break/fix challenge — Missing membership

Simulate a common access incident by removing only user A's membership:

```bash
az ad group member remove \
  --group "$GROUP_ID" \
  --member-id "$USER_A_ID" \
  --output none

./scripts/cli/validate.sh --run-id "$RUN_ID"
```

Expected result: `relationship.member` fails while user and group property checks remain intact.

Repair the incident using exact IDs without recreating the user or group. Verify that user B remains an owner and does not become a member. The recovery commands and reasoning are in [solution/README.md](solution/README.md).

## Cleanup preview, execution, and audit

Preview first:

```bash
./scripts/cli/cleanup.sh --run-id "$RUN_ID"
```

For a completed run, the preview shows exactly one group ID and two user IDs. For a setup that failed partway through, it safely lists and deletes the recorded subset. Cleanup refuses an active-tenant mismatch, more than three objects, duplicate keys, unknown object types, or missing IDs.

Perform recoverable cleanup:

```bash
./scripts/cli/cleanup.sh --run-id "$RUN_ID" --execute
```

This deletes the group and soft-deletes both users. The script then confirms none of the three objects remains active. The user objects stay recoverable under **Users > Deleted users** until Microsoft Entra retention expires.

If tenant policy requires immediate permanent removal and you are explicitly authorized, preview the recorded IDs again, then use the irreversible mode:

```bash
./scripts/cli/cleanup.sh \
  --run-id "$RUN_ID" \
  --execute \
  --purge-deleted-users
```

Permanent purge cannot be undone and can require additional permissions. Do not use it on an ID that was not recorded by this run.

Cleanup retains local `run.json` as audit evidence. After reviewing the cleanup status and before publishing screenshots, you may remove only `.state/$RUN_ID/` locally. The entire `.state/` tree is excluded from Git.

## Administrator and exam takeaways

- Microsoft Entra roles manage directory objects; Azure RBAC roles manage Azure resource access.
- A cloud user's UPN must use a verified tenant domain.
- Object IDs are immutable identifiers; display names can be duplicated and changed.
- A group owner and a group member are different relationships.
- Group membership can grant downstream access only where that group is assigned access.
- Direct membership checks do not automatically answer every transitive-membership question.
- Rich user and group properties can be managed through Microsoft Graph when a simplified CLI command lacks a parameter.
- Deleting a user normally moves it to Deleted users; permanent deletion is a separate lifecycle decision.
- Validation should detect drift, and cleanup should use recorded IDs rather than broad searches.

## Knowledge check

Complete the ten questions in [assessment/QUESTIONS.md](assessment/QUESTIONS.md) before opening [assessment/ANSWERS.md](assessment/ANSWERS.md). Questions are original learning material, not certification exam items.

## Official references

Last verified: **2026-08-30**.

- [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Azure CLI: manage Microsoft Entra users](https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)
- [Azure CLI: manage Microsoft Entra groups](https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest)
- [Azure CLI: manage group members](https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest)
- [Microsoft Graph: create user](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0)
- [Microsoft Graph: create group](https://learn.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0)
- [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
- [Recover or permanently remove recently deleted users](https://learn.microsoft.com/en-us/entra/fundamentals/users-restore)

Portal layout, permissions, and commands evolve. Revalidate the documentation and replace screenshots whenever the interface or behavior changes.
