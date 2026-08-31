# Lab 07 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB07-Q01 — C

**Question:** The restricted storage data-plane design handoff omits the network perimeter rule needed to deny public-endpoint traffic unless an explicit network exception allows it. Which statement should the team add?

- **A — Incorrect.** An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range.
  An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range. In the restricted storage data-plane design, this statement describes storage IP network rules. Restricted storage data-plane design asks about storage firewall default action; this storage IP network rules choice leaves the storage firewall default action explanation missing.
- **B — Incorrect.** A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types.
  A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types. In the restricted storage data-plane design, this statement describes service and account SAS scope. The service and account SAS scope statement accurately describes service and account SAS scope; however, restricted storage data-plane design needs storage firewall default action to deny public-endpoint traffic unless an explicit network exception allows it; service and account SAS scope cannot replace storage firewall default action.
- **C — Correct.** A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions.
  A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions. In the restricted storage data-plane design, this storage firewall default action rule supports the need to deny public-endpoint traffic unless an explicit network exception allows it.
- **D — Incorrect.** A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier.
  A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier. In the restricted storage data-plane design, this statement describes stored access policies. Storage firewall default action governs restricted storage data-plane design; stored access policies cannot support storage firewall default action when operators must deny public-endpoint traffic unless an explicit network exception allows it.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q02 — C

**Question:** A network perimeter incident review of the restricted storage data-plane design depends on the ability to permit traffic at the public service address only from an approved IPv4 range. Which platform description is reliable?

- **A — Incorrect.** A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint.
  A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint. In the restricted storage data-plane design, this statement describes virtual-network service endpoints. The virtual-network service endpoints statement accurately describes virtual-network service endpoints; however, restricted storage data-plane design needs storage IP network rules to permit traffic at the public service address only from an approved IPv4 range; virtual-network service endpoints cannot replace storage IP network rules.
- **B — Incorrect.** A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key.
  A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key. In the restricted storage data-plane design, this statement describes user delegation SAS. Selecting user delegation SAS for restricted storage data-plane design leaves storage IP network rules unanswered in restricted storage data-plane design; the restricted storage data-plane design lacks a storage IP network rules basis to permit traffic at the public service address only from an approved IPv4 range.
- **C — Correct.** An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range.
  For the restricted storage data-plane design, the rule for storage IP network rules is defined by this statement: an IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range. It supports the required outcome to permit traffic at the public service address only from an approved IPv4 range.
- **D — Incorrect.** Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation.
  Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation. In the restricted storage data-plane design, this statement describes stored-policy revocation. Restricted storage data-plane design asks about storage IP network rules; this stored-policy revocation choice leaves the storage IP network rules explanation missing.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q03 — B

**Question:** A storage security administrator restricting data-plane access is updating the network perimeter runbook. The requirement is to authorize one subnet on the service firewall while retaining the public endpoint. Which statement describes Azure behavior correctly?

- **A — Incorrect.** A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.
  A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall. In the restricted storage data-plane design, this statement describes trusted Azure service bypass. Selecting trusted Azure service bypass for restricted storage data-plane design leaves virtual-network service endpoints unanswered in restricted storage data-plane design; the restricted storage data-plane design lacks a virtual-network service endpoints basis to authorize one subnet on the service firewall while retaining the public endpoint.
- **B — Correct.** A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint.
  A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint. The restricted storage data-plane design applies that virtual-network service endpoints boundary when operators must authorize one subnet on the service firewall while retaining the public endpoint.
- **C — Incorrect.** A SAS is valid only within its signed time window, subject to clock skew and service interpretation.
  A SAS is valid only within its signed time window, subject to clock skew and service interpretation. In the restricted storage data-plane design, this statement describes SAS start and expiry time. Restricted storage data-plane design asks about virtual-network service endpoints; this SAS start and expiry time choice leaves the virtual-network service endpoints explanation missing.
- **D — Incorrect.** Anyone holding a storage account key can authorize broad shared-key operations permitted by the service.
  Anyone holding a storage account key can authorize broad shared-key operations permitted by the service. In the restricted storage data-plane design, this statement describes account-key exposure. The account-key exposure statement accurately describes account-key exposure; however, restricted storage data-plane design needs virtual-network service endpoints to authorize one subnet on the service firewall while retaining the public endpoint; account-key exposure cannot replace virtual-network service endpoints.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q04 — A

**Question:** A network perimeter peer review asks how the restricted storage data-plane design should handle this outcome: allow only the limited platform services supported by the firewall bypass. Which explanation is accurate?

- **A — Correct.** A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.
  The restricted storage data-plane design needs trusted Azure service bypass to allow only the limited platform services supported by the firewall bypass; this option states the applicable trusted Azure service bypass rule: a trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.
- **B — Incorrect.** A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types.
  A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types. In the restricted storage data-plane design, this statement describes service and account SAS scope. Restricted storage data-plane design asks about trusted Azure service bypass; this service and account SAS scope choice leaves the trusted Azure service bypass explanation missing.
- **C — Incorrect.** A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier.
  A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier. In the restricted storage data-plane design, this statement describes stored access policies. The stored access policies statement accurately describes stored access policies; however, restricted storage data-plane design needs trusted Azure service bypass to allow only the limited platform services supported by the firewall bypass; stored access policies cannot replace trusted Azure service bypass.
- **D — Incorrect.** A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions.
  A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions. In the restricted storage data-plane design, this statement describes storage firewall default action. Selecting storage firewall default action for restricted storage data-plane design leaves trusted Azure service bypass unanswered in restricted storage data-plane design; the restricted storage data-plane design lacks a trusted Azure service bypass basis to allow only the limited platform services supported by the firewall bypass.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q05 — A

**Question:** For the restricted storage data-plane design, the network perimeter plan must choose whether delegated access covers one service or several account services. Which statement about network perimeter belongs in the restricted storage data-plane design record?

- **A — Correct.** A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types.
  A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types. This service and account SAS scope fact resolves the restricted storage data-plane design design question about how to choose whether delegated access covers one service or several account services.
- **B — Incorrect.** A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key.
  A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key. In the restricted storage data-plane design, this statement describes user delegation SAS. The user delegation SAS statement accurately describes user delegation SAS; however, restricted storage data-plane design needs service and account SAS scope to choose whether delegated access covers one service or several account services; user delegation SAS cannot replace service and account SAS scope.
- **C — Incorrect.** Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation.
  Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation. In the restricted storage data-plane design, this statement describes stored-policy revocation. Selecting stored-policy revocation for restricted storage data-plane design leaves service and account SAS scope unanswered in restricted storage data-plane design; the restricted storage data-plane design lacks a service and account SAS scope basis to choose whether delegated access covers one service or several account services.
- **D — Incorrect.** An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range.
  An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range. In the restricted storage data-plane design, this statement describes storage IP network rules. Service and account SAS scope governs restricted storage data-plane design; storage IP network rules cannot support service and account SAS scope when operators must choose whether delegated access covers one service or several account services.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Grant limited access with shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)

**Source reviewed:** 2026-08-31

## LAB07-Q06 — B

**Question:** The network perimeter review compares four claims for the restricted storage data-plane design requirement to have a Microsoft Entra principal sign temporary Blob access instead of an account credential. Which claim is technically sound?

- **A — Incorrect.** A SAS is valid only within its signed time window, subject to clock skew and service interpretation.
  A SAS is valid only within its signed time window, subject to clock skew and service interpretation. In the restricted storage data-plane design, this statement describes SAS start and expiry time. The SAS start and expiry time statement accurately describes SAS start and expiry time; however, restricted storage data-plane design needs user delegation SAS to have a Microsoft Entra principal sign temporary Blob access instead of an account credential; SAS start and expiry time cannot replace user delegation SAS.
- **B — Correct.** A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key.
  A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key. For restricted storage data-plane design, user delegation SAS supplies the service rule needed to have a Microsoft Entra principal sign temporary Blob access instead of an account credential.
- **C — Incorrect.** Anyone holding a storage account key can authorize broad shared-key operations permitted by the service.
  Anyone holding a storage account key can authorize broad shared-key operations permitted by the service. In the restricted storage data-plane design, this statement describes account-key exposure. User delegation SAS governs restricted storage data-plane design; account-key exposure cannot support user delegation SAS when operators must have a Microsoft Entra principal sign temporary Blob access instead of an account credential.
- **D — Incorrect.** A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint.
  A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint. In the restricted storage data-plane design, this statement describes virtual-network service endpoints. Restricted storage data-plane design asks about user delegation SAS; this virtual-network service endpoints choice leaves the user delegation SAS explanation missing.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Create a user delegation SAS with Azure CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

**Source reviewed:** 2026-08-31

## LAB07-Q07 — C

**Question:** The network perimeter architecture note requires the restricted storage data-plane design environment to bound delegated access to an intentional start and expiry window. Which statement defines the relevant network perimeter boundary?

- **A — Incorrect.** A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier.
  A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier. In the restricted storage data-plane design, this statement describes stored access policies. Selecting stored access policies for restricted storage data-plane design leaves SAS start and expiry time unanswered in restricted storage data-plane design; the restricted storage data-plane design lacks a SAS start and expiry time basis to bound delegated access to an intentional start and expiry window.
- **B — Incorrect.** A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions.
  A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions. In the restricted storage data-plane design, this statement describes storage firewall default action. SAS start and expiry time governs restricted storage data-plane design; storage firewall default action cannot support SAS start and expiry time when operators must bound delegated access to an intentional start and expiry window.
- **C — Correct.** A SAS is valid only within its signed time window, subject to clock skew and service interpretation.
  A SAS is valid only within its signed time window, subject to clock skew and service interpretation. In the restricted storage data-plane design, this SAS start and expiry time rule supports the need to bound delegated access to an intentional start and expiry window.
- **D — Incorrect.** A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.
  A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall. In the restricted storage data-plane design, this statement describes trusted Azure service bypass. The trusted Azure service bypass statement accurately describes trusted Azure service bypass; however, restricted storage data-plane design needs SAS start and expiry time to bound delegated access to an intentional start and expiry window; trusted Azure service bypass cannot replace SAS start and expiry time.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Create an expiration policy for shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/sas-expiration-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q08 — C

**Question:** A new network perimeter operator must explain why the restricted storage data-plane design can attach revocable constraints to service-level delegated tokens. Which explanation is accurate?

- **A — Incorrect.** Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation.
  Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation. In the restricted storage data-plane design, this statement describes stored-policy revocation. Stored access policies governs restricted storage data-plane design; stored-policy revocation cannot support stored access policies when operators must attach revocable constraints to service-level delegated tokens.
- **B — Incorrect.** An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range.
  An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range. In the restricted storage data-plane design, this statement describes storage IP network rules. Restricted storage data-plane design asks about stored access policies; this storage IP network rules choice leaves the stored access policies explanation missing.
- **C — Correct.** A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier.
  For the restricted storage data-plane design, the rule for stored access policies is defined by this statement: a stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier. It supports the required outcome to attach revocable constraints to service-level delegated tokens.
- **D — Incorrect.** A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types.
  A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types. In the restricted storage data-plane design, this statement describes service and account SAS scope. Selecting service and account SAS scope for restricted storage data-plane design leaves stored access policies unanswered in restricted storage data-plane design; the restricted storage data-plane design lacks a stored access policies basis to attach revocable constraints to service-level delegated tokens.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q09 — C

**Question:** The restricted storage data-plane design acceptance criteria require operators to invalidate tokens that refer to a named server-side access policy. Which service fact supports that requirement?

- **A — Incorrect.** Anyone holding a storage account key can authorize broad shared-key operations permitted by the service.
  Anyone holding a storage account key can authorize broad shared-key operations permitted by the service. In the restricted storage data-plane design, this statement describes account-key exposure. Restricted storage data-plane design asks about stored-policy revocation; this account-key exposure choice leaves the stored-policy revocation explanation missing.
- **B — Incorrect.** A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint.
  A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint. In the restricted storage data-plane design, this statement describes virtual-network service endpoints. The virtual-network service endpoints statement accurately describes virtual-network service endpoints; however, restricted storage data-plane design needs stored-policy revocation to invalidate tokens that refer to a named server-side access policy; virtual-network service endpoints cannot replace stored-policy revocation.
- **C — Correct.** Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation.
  Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation. The restricted storage data-plane design applies that stored-policy revocation boundary when operators must invalidate tokens that refer to a named server-side access policy.
- **D — Incorrect.** A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key.
  A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key. In the restricted storage data-plane design, this statement describes user delegation SAS. Stored-policy revocation governs restricted storage data-plane design; user delegation SAS cannot support stored-policy revocation when operators must invalidate tokens that refer to a named server-side access policy.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q10 — D

**Question:** A network perimeter reviewer challenges whether the restricted storage data-plane design can avoid exposing a credential that grants broad authority over the account. Which response resolves the concern?

- **A — Incorrect.** A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions.
  A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions. In the restricted storage data-plane design, this statement describes storage firewall default action. The storage firewall default action statement accurately describes storage firewall default action; however, restricted storage data-plane design needs account-key exposure to avoid exposing a credential that grants broad authority over the account; storage firewall default action cannot replace account-key exposure.
- **B — Incorrect.** A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.
  A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall. In the restricted storage data-plane design, this statement describes trusted Azure service bypass. Selecting trusted Azure service bypass for restricted storage data-plane design leaves account-key exposure unanswered in restricted storage data-plane design; the restricted storage data-plane design lacks a account-key exposure basis to avoid exposing a credential that grants broad authority over the account.
- **C — Incorrect.** A SAS is valid only within its signed time window, subject to clock skew and service interpretation.
  A SAS is valid only within its signed time window, subject to clock skew and service interpretation. In the restricted storage data-plane design, this statement describes SAS start and expiry time. Account-key exposure governs restricted storage data-plane design; SAS start and expiry time cannot support account-key exposure when operators must avoid exposing a credential that grants broad authority over the account.
- **D — Correct.** Anyone holding a storage account key can authorize broad shared-key operations permitted by the service.
  The restricted storage data-plane design needs account-key exposure to avoid exposing a credential that grants broad authority over the account; this option states the applicable account-key exposure rule: anyone holding a storage account key can authorize broad shared-key operations permitted by the service.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB07-Q11 — B

**Question:** The network perimeter preflight has passed; the restricted storage data-plane design must now deny public-endpoint traffic unless an explicit network exception allows it. Which operation should run?

- **A — Incorrect.** Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules.
  Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. In the restricted storage data-plane design, this action changes virtual-network service endpoints. Restricted storage data-plane design approved storage firewall default action, not virtual-network service endpoints; only the storage firewall default action change can deny public-endpoint traffic unless an explicit network exception allows it.
- **B — Correct.** Set the storage network rule default action to Deny after adding the administrator's approved access path.
  Set the storage network rule default action to Deny after adding the administrator's approved access path. It is the least-change storage firewall default action path for the restricted storage data-plane design requirement to deny public-endpoint traffic unless an explicit network exception allows it.
- **C — Incorrect.** Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
  Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. In the restricted storage data-plane design, this action changes user delegation SAS. User delegation SAS does not implement storage firewall default action for restricted storage data-plane design; the restricted storage data-plane design still cannot deny public-endpoint traffic unless an explicit network exception allows it.
- **D — Incorrect.** Revoke delegated access by changing or removing the referenced stored access policy.
  Revoke delegated access by changing or removing the referenced stored access policy. In the restricted storage data-plane design, this action changes stored-policy revocation. Restricted storage data-plane design instead needs storage firewall default action: Set the storage network rule default action to Deny after adding the administrator's approved access path. The stored-policy revocation action omits that storage firewall default action work.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q12 — D

**Question:** The restricted storage data-plane design plan must permit traffic at the public service address only from an approved IPv4 range while limiting the mutation scope to network perimeter. Which action is appropriate?

- **A — Incorrect.** Enable only the documented trusted-service bypass required by the workload.
  Enable only the documented trusted-service bypass required by the workload. In the restricted storage data-plane design, this action changes trusted Azure service bypass. Restricted storage data-plane design requires storage IP network rules; changing trusted Azure service bypass leaves storage IP network rules absent in restricted storage data-plane design; restricted storage data-plane design cannot permit traffic at the public service address only from an approved IPv4 range.
- **B — Incorrect.** Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use.
  Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. In the restricted storage data-plane design, this action changes SAS start and expiry time. SAS start and expiry time does not implement storage IP network rules for restricted storage data-plane design; the restricted storage data-plane design still cannot permit traffic at the public service address only from an approved IPv4 range.
- **C — Incorrect.** Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens.
  Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. In the restricted storage data-plane design, this action changes account-key exposure. Restricted storage data-plane design instead needs storage IP network rules: Add only the approved public egress address to the account network rules. The account-key exposure action omits that storage IP network rules work.
- **D — Correct.** Add only the approved public egress address to the account network rules.
  Add only the approved public egress address to the account network rules. In restricted storage data-plane design, applying storage IP network rules is the scoped way to permit traffic at the public service address only from an approved IPv4 range.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q13 — D

**Question:** A network perimeter ticket in the restricted storage data-plane design says to authorize one subnet on the service firewall while retaining the public endpoint. Which network perimeter action completes the restricted storage data-plane design request with minimal change?

- **A — Incorrect.** Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request.
  Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. In the restricted storage data-plane design, this action changes service and account SAS scope. Service and account SAS scope does not implement virtual-network service endpoints for restricted storage data-plane design; the restricted storage data-plane design still cannot authorize one subnet on the service firewall while retaining the public endpoint.
- **B — Incorrect.** Create a named stored access policy and generate the service SAS with that policy identifier.
  Create a named stored access policy and generate the service SAS with that policy identifier. In the restricted storage data-plane design, this action changes stored access policies. Restricted storage data-plane design instead needs virtual-network service endpoints: Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. The stored access policies action omits that virtual-network service endpoints work.
- **C — Incorrect.** Set the storage network rule default action to Deny after adding the administrator's approved access path.
  Set the storage network rule default action to Deny after adding the administrator's approved access path. In the restricted storage data-plane design, this action changes storage firewall default action. Restricted storage data-plane design approved virtual-network service endpoints, not storage firewall default action; only the virtual-network service endpoints change can authorize one subnet on the service firewall while retaining the public endpoint.
- **D — Correct.** Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules.
  Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. The restricted storage data-plane design uses this virtual-network service endpoints operation to authorize one subnet on the service firewall while retaining the public endpoint within the approved scope.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q14 — B

**Question:** The approach for the restricted storage data-plane design is approved, but the network perimeter environment still cannot allow only the limited platform services supported by the firewall bypass. Which implementation step closes the gap?

- **A — Incorrect.** Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
  Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. In the restricted storage data-plane design, this action changes user delegation SAS. Restricted storage data-plane design instead needs trusted Azure service bypass: Enable only the documented trusted-service bypass required by the workload. The user delegation SAS action omits that trusted Azure service bypass work.
- **B — Correct.** Enable only the documented trusted-service bypass required by the workload.
  For the restricted storage data-plane design, the required trusted Azure service bypass action is: enable only the documented trusted-service bypass required by the workload. It makes the environment able to allow only the limited platform services supported by the firewall bypass.
- **C — Incorrect.** Revoke delegated access by changing or removing the referenced stored access policy.
  Revoke delegated access by changing or removing the referenced stored access policy. In the restricted storage data-plane design, this action changes stored-policy revocation. Restricted storage data-plane design requires trusted Azure service bypass; changing stored-policy revocation leaves trusted Azure service bypass absent in restricted storage data-plane design; restricted storage data-plane design cannot allow only the limited platform services supported by the firewall bypass.
- **D — Incorrect.** Add only the approved public egress address to the account network rules.
  Add only the approved public egress address to the account network rules. In the restricted storage data-plane design, this action changes storage IP network rules. Storage IP network rules does not implement trusted Azure service bypass for restricted storage data-plane design; the restricted storage data-plane design still cannot allow only the limited platform services supported by the firewall bypass.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q15 — B

**Question:** The storage security administrator restricting data-plane access may change the restricted storage data-plane design only to choose whether delegated access covers one service or several account services. Which network perimeter action stays within that assignment?

- **A — Incorrect.** Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use.
  Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. In the restricted storage data-plane design, this action changes SAS start and expiry time. Restricted storage data-plane design approved service and account SAS scope, not SAS start and expiry time; only the service and account SAS scope change can choose whether delegated access covers one service or several account services.
- **B — Correct.** Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request.
  Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. This changes service and account SAS scope in the restricted storage data-plane design, supplying the missing state needed to choose whether delegated access covers one service or several account services.
- **C — Incorrect.** Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens.
  Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. In the restricted storage data-plane design, this action changes account-key exposure. Account-key exposure does not implement service and account SAS scope for restricted storage data-plane design; the restricted storage data-plane design still cannot choose whether delegated access covers one service or several account services.
- **D — Incorrect.** Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules.
  Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. In the restricted storage data-plane design, this action changes virtual-network service endpoints. Restricted storage data-plane design instead needs service and account SAS scope: Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. The virtual-network service endpoints action omits that service and account SAS scope work.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Grant limited access with shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)

**Source reviewed:** 2026-08-31

## LAB07-Q16 — A

**Question:** A network perimeter dry run shows no restricted storage data-plane design command will have a Microsoft Entra principal sign temporary Blob access instead of an account credential. Which action belongs before execution?

- **A — Correct.** Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
  The restricted storage data-plane design must have a Microsoft Entra principal sign temporary Blob access instead of an account credential; this option performs its direct user delegation SAS change: authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
- **B — Incorrect.** Create a named stored access policy and generate the service SAS with that policy identifier.
  Create a named stored access policy and generate the service SAS with that policy identifier. In the restricted storage data-plane design, this action changes stored access policies. Stored access policies does not implement user delegation SAS for restricted storage data-plane design; the restricted storage data-plane design still cannot have a Microsoft Entra principal sign temporary Blob access instead of an account credential.
- **C — Incorrect.** Set the storage network rule default action to Deny after adding the administrator's approved access path.
  Set the storage network rule default action to Deny after adding the administrator's approved access path. In the restricted storage data-plane design, this action changes storage firewall default action. Restricted storage data-plane design instead needs user delegation SAS: Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. The storage firewall default action action omits that user delegation SAS work.
- **D — Incorrect.** Enable only the documented trusted-service bypass required by the workload.
  Enable only the documented trusted-service bypass required by the workload. In the restricted storage data-plane design, this action changes trusted Azure service bypass. Restricted storage data-plane design approved user delegation SAS, not trusted Azure service bypass; only the user delegation SAS change can have a Microsoft Entra principal sign temporary Blob access instead of an account credential.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Create a user delegation SAS with Azure CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

**Source reviewed:** 2026-08-31

## LAB07-Q17 — A

**Question:** For the restricted storage data-plane design, operators need to bound delegated access to an intentional start and expiry window. Which change realizes that requirement?

- **A — Correct.** Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use.
  Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. It is the least-change SAS start and expiry time path for the restricted storage data-plane design requirement to bound delegated access to an intentional start and expiry window.
- **B — Incorrect.** Revoke delegated access by changing or removing the referenced stored access policy.
  Revoke delegated access by changing or removing the referenced stored access policy. In the restricted storage data-plane design, this action changes stored-policy revocation. Restricted storage data-plane design instead needs SAS start and expiry time: Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. The stored-policy revocation action omits that SAS start and expiry time work.
- **C — Incorrect.** Add only the approved public egress address to the account network rules.
  Add only the approved public egress address to the account network rules. In the restricted storage data-plane design, this action changes storage IP network rules. Restricted storage data-plane design approved SAS start and expiry time, not storage IP network rules; only the SAS start and expiry time change can bound delegated access to an intentional start and expiry window.
- **D — Incorrect.** Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request.
  Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. In the restricted storage data-plane design, this action changes service and account SAS scope. Restricted storage data-plane design requires SAS start and expiry time; changing service and account SAS scope leaves SAS start and expiry time absent in restricted storage data-plane design; restricted storage data-plane design cannot bound delegated access to an intentional start and expiry window.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Create an expiration policy for shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/sas-expiration-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q18 — D

**Question:** Operators must automate the restricted storage data-plane design change needed to attach revocable constraints to service-level delegated tokens. Which network perimeter operation belongs in the runbook?

- **A — Incorrect.** Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens.
  Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. In the restricted storage data-plane design, this action changes account-key exposure. Restricted storage data-plane design instead needs stored access policies: Create a named stored access policy and generate the service SAS with that policy identifier. The account-key exposure action omits that stored access policies work.
- **B — Incorrect.** Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules.
  Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. In the restricted storage data-plane design, this action changes virtual-network service endpoints. Restricted storage data-plane design approved stored access policies, not virtual-network service endpoints; only the stored access policies change can attach revocable constraints to service-level delegated tokens.
- **C — Incorrect.** Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
  Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. In the restricted storage data-plane design, this action changes user delegation SAS. Restricted storage data-plane design requires stored access policies; changing user delegation SAS leaves stored access policies absent in restricted storage data-plane design; restricted storage data-plane design cannot attach revocable constraints to service-level delegated tokens.
- **D — Correct.** Create a named stored access policy and generate the service SAS with that policy identifier.
  Create a named stored access policy and generate the service SAS with that policy identifier. In restricted storage data-plane design, applying stored access policies is the scoped way to attach revocable constraints to service-level delegated tokens.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q19 — D

**Question:** A restricted storage data-plane design review finds network perimeter drift from the need to invalidate tokens that refer to a named server-side access policy. Which correction addresses that drift?

- **A — Incorrect.** Set the storage network rule default action to Deny after adding the administrator's approved access path.
  Set the storage network rule default action to Deny after adding the administrator's approved access path. In the restricted storage data-plane design, this action changes storage firewall default action. Restricted storage data-plane design approved stored-policy revocation, not storage firewall default action; only the stored-policy revocation change can invalidate tokens that refer to a named server-side access policy.
- **B — Incorrect.** Enable only the documented trusted-service bypass required by the workload.
  Enable only the documented trusted-service bypass required by the workload. In the restricted storage data-plane design, this action changes trusted Azure service bypass. Restricted storage data-plane design requires stored-policy revocation; changing trusted Azure service bypass leaves stored-policy revocation absent in restricted storage data-plane design; restricted storage data-plane design cannot invalidate tokens that refer to a named server-side access policy.
- **C — Incorrect.** Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use.
  Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. In the restricted storage data-plane design, this action changes SAS start and expiry time. SAS start and expiry time does not implement stored-policy revocation for restricted storage data-plane design; the restricted storage data-plane design still cannot invalidate tokens that refer to a named server-side access policy.
- **D — Correct.** Revoke delegated access by changing or removing the referenced stored access policy.
  Revoke delegated access by changing or removing the referenced stored access policy. The restricted storage data-plane design uses this stored-policy revocation operation to invalidate tokens that refer to a named server-side access policy within the approved scope.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q20 — C

**Question:** The restricted storage data-plane design window permits only the network perimeter change needed to avoid exposing a credential that grants broad authority over the account. Which option respects the boundary?

- **A — Incorrect.** Add only the approved public egress address to the account network rules.
  Add only the approved public egress address to the account network rules. In the restricted storage data-plane design, this action changes storage IP network rules. Restricted storage data-plane design requires account-key exposure; changing storage IP network rules leaves account-key exposure absent in restricted storage data-plane design; restricted storage data-plane design cannot avoid exposing a credential that grants broad authority over the account.
- **B — Incorrect.** Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request.
  Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. In the restricted storage data-plane design, this action changes service and account SAS scope. Service and account SAS scope does not implement account-key exposure for restricted storage data-plane design; the restricted storage data-plane design still cannot avoid exposing a credential that grants broad authority over the account.
- **C — Correct.** Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens.
  For the restricted storage data-plane design, the required account-key exposure action is: keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. It makes the environment able to avoid exposing a credential that grants broad authority over the account.
- **D — Incorrect.** Create a named stored access policy and generate the service SAS with that policy identifier.
  Create a named stored access policy and generate the service SAS with that policy identifier. In the restricted storage data-plane design, this action changes stored access policies. Restricted storage data-plane design approved account-key exposure, not stored access policies; only the account-key exposure change can avoid exposing a credential that grants broad authority over the account.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB07-Q21 — D

**Question:** The restricted storage data-plane design evidence bundle needs a network perimeter result showing it can deny public-endpoint traffic unless an explicit network exception allows it. Which result belongs in the checkpoint?

- **A — Incorrect.** Query networkRuleSet.bypass and compare it with the approved exception list.
  Query networkRuleSet.bypass and compare it with the approved exception list. In the restricted storage data-plane design, this check observes trusted Azure service bypass. Restricted storage data-plane design output covers trusted Azure service bypass, not storage firewall default action; the storage firewall default action requirement to deny public-endpoint traffic unless an explicit network exception allows it remains unverified.
- **B — Incorrect.** Inspect st and se values and test the minimum required operation before distribution.
  Inspect st and se values and test the minimum required operation before distribution. In the restricted storage data-plane design, this check observes SAS start and expiry time. SAS start and expiry time success in restricted storage data-plane design cannot verify storage firewall default action; restricted storage data-plane design cannot deny public-endpoint traffic unless an explicit network exception allows it until storage firewall default action evidence exists.
- **C — Incorrect.** Scan evidence for secrets and verify data commands use login-based authorization where supported.
  Scan evidence for secrets and verify data commands use login-based authorization where supported. In the restricted storage data-plane design, this check observes account-key exposure. Restricted storage data-plane design reads account-key exposure, leaving storage firewall default action unproved in restricted storage data-plane design; restricted storage data-plane design still has no storage firewall default action proof.
- **D — Correct.** Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
  Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule. Because the restricted storage data-plane design check observes storage firewall default action, it independently verifies the requirement to deny public-endpoint traffic unless an explicit network exception allows it.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q22 — A

**Question:** Before restricted storage data-plane design cleanup, the network perimeter team must reconfirm it can permit traffic at the public service address only from an approved IPv4 range. Which read-only inspection should run?

- **A — Correct.** Query ipRules and match the normalized CIDR value and Allow action.
  The restricted storage data-plane design validator needs this storage IP network rules result: query ipRules and match the normalized CIDR value and Allow action. It proves the outcome to permit traffic at the public service address only from an approved IPv4 range rather than an adjacent checkpoint.
- **B — Incorrect.** Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
  Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry. In the restricted storage data-plane design, this check observes service and account SAS scope. Restricted storage data-plane design reads service and account SAS scope, leaving storage IP network rules unproved in restricted storage data-plane design; restricted storage data-plane design still has no storage IP network rules proof.
- **C — Incorrect.** List signed identifiers on the resource and confirm the SAS si field names the expected policy.
  List signed identifiers on the resource and confirm the SAS si field names the expected policy. In the restricted storage data-plane design, this check observes stored access policies. Restricted storage data-plane design could pass stored access policies while storage IP network rules is wrong; restricted storage data-plane design still lacks storage IP network rules proof.
- **D — Incorrect.** Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
  Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule. In the restricted storage data-plane design, this check observes storage firewall default action. Restricted storage data-plane design output covers storage firewall default action, not storage IP network rules; the storage IP network rules requirement to permit traffic at the public service address only from an approved IPv4 range remains unverified.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q23 — C

**Question:** The restricted storage data-plane design setup reports success after the network perimeter attempt to authorize one subnet on the service firewall while retaining the public endpoint. Which network perimeter read-only observation proves the restricted storage data-plane design outcome?

- **A — Incorrect.** Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
  Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions. In the restricted storage data-plane design, this check observes user delegation SAS. Restricted storage data-plane design reads user delegation SAS, leaving virtual-network service endpoints unproved in restricted storage data-plane design; restricted storage data-plane design still has no virtual-network service endpoints proof.
- **B — Incorrect.** List the signed identifiers and retest the previously issued SAS until the policy change is effective.
  List the signed identifiers and retest the previously issued SAS until the policy change is effective. In the restricted storage data-plane design, this check observes stored-policy revocation. Restricted storage data-plane design could pass stored-policy revocation while virtual-network service endpoints is wrong; restricted storage data-plane design still lacks virtual-network service endpoints proof.
- **C — Correct.** Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
  Query both subnet serviceEndpoints and the account virtualNetworkRules collection. This is independent virtual-network service endpoints evidence for the restricted storage data-plane design, even if restricted storage data-plane design setup reports success before virtual-network service endpoints becomes observable.
- **D — Incorrect.** Query ipRules and match the normalized CIDR value and Allow action.
  Query ipRules and match the normalized CIDR value and Allow action. In the restricted storage data-plane design, this check observes storage IP network rules. Storage IP network rules success in restricted storage data-plane design cannot verify virtual-network service endpoints; restricted storage data-plane design cannot authorize one subnet on the service firewall while retaining the public endpoint until virtual-network service endpoints evidence exists.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q24 — B

**Question:** The network perimeter log says the restricted storage data-plane design can now allow only the limited platform services supported by the firewall bypass. Which network perimeter state should the restricted storage data-plane design acceptance test retain?

- **A — Incorrect.** Inspect st and se values and test the minimum required operation before distribution.
  Inspect st and se values and test the minimum required operation before distribution. In the restricted storage data-plane design, this check observes SAS start and expiry time. Restricted storage data-plane design could pass SAS start and expiry time while trusted Azure service bypass is wrong; restricted storage data-plane design still lacks trusted Azure service bypass proof.
- **B — Correct.** Query networkRuleSet.bypass and compare it with the approved exception list.
  Query networkRuleSet.bypass and compare it with the approved exception list. For restricted storage data-plane design, this trusted Azure service bypass read confirms the service can allow only the limited platform services supported by the firewall bypass.
- **C — Incorrect.** Scan evidence for secrets and verify data commands use login-based authorization where supported.
  Scan evidence for secrets and verify data commands use login-based authorization where supported. In the restricted storage data-plane design, this check observes account-key exposure. Account-key exposure success in restricted storage data-plane design cannot verify trusted Azure service bypass; restricted storage data-plane design cannot allow only the limited platform services supported by the firewall bypass until trusted Azure service bypass evidence exists.
- **D — Incorrect.** Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
  Query both subnet serviceEndpoints and the account virtualNetworkRules collection. In the restricted storage data-plane design, this check observes virtual-network service endpoints. Restricted storage data-plane design reads virtual-network service endpoints, leaving trusted Azure service bypass unproved in restricted storage data-plane design; restricted storage data-plane design still has no trusted Azure service bypass proof.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q25 — A

**Question:** The restricted storage data-plane design rejects network perimeter exit status as proof it can choose whether delegated access covers one service or several account services. Which restricted storage data-plane design result is valid evidence?

- **A — Correct.** Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
  Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry. The restricted storage data-plane design reads service and account SAS scope directly; that service and account SAS scope result proves the restricted storage data-plane design can choose whether delegated access covers one service or several account services without another mutation.
- **B — Incorrect.** List signed identifiers on the resource and confirm the SAS si field names the expected policy.
  List signed identifiers on the resource and confirm the SAS si field names the expected policy. In the restricted storage data-plane design, this check observes stored access policies. Stored access policies success in restricted storage data-plane design cannot verify service and account SAS scope; restricted storage data-plane design cannot choose whether delegated access covers one service or several account services until service and account SAS scope evidence exists.
- **C — Incorrect.** Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
  Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule. In the restricted storage data-plane design, this check observes storage firewall default action. Restricted storage data-plane design reads storage firewall default action, leaving service and account SAS scope unproved in restricted storage data-plane design; restricted storage data-plane design still has no service and account SAS scope proof.
- **D — Incorrect.** Query networkRuleSet.bypass and compare it with the approved exception list.
  Query networkRuleSet.bypass and compare it with the approved exception list. In the restricted storage data-plane design, this check observes trusted Azure service bypass. Restricted storage data-plane design could pass trusted Azure service bypass while service and account SAS scope is wrong; restricted storage data-plane design still lacks service and account SAS scope proof.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Grant limited access with shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)

**Source reviewed:** 2026-08-31

## LAB07-Q26 — A

**Question:** The network perimeter validator needs one restricted storage data-plane design query after the change to have a Microsoft Entra principal sign temporary Blob access instead of an account credential. Which network perimeter property should the restricted storage data-plane design validator inspect?

- **A — Correct.** Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
  For the restricted storage data-plane design, this user delegation SAS observation is decisive: inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions. It is restricted storage data-plane design evidence that operators can have a Microsoft Entra principal sign temporary Blob access instead of an account credential.
- **B — Incorrect.** List the signed identifiers and retest the previously issued SAS until the policy change is effective.
  List the signed identifiers and retest the previously issued SAS until the policy change is effective. In the restricted storage data-plane design, this check observes stored-policy revocation. Restricted storage data-plane design reads stored-policy revocation, leaving user delegation SAS unproved in restricted storage data-plane design; restricted storage data-plane design still has no user delegation SAS proof.
- **C — Incorrect.** Query ipRules and match the normalized CIDR value and Allow action.
  Query ipRules and match the normalized CIDR value and Allow action. In the restricted storage data-plane design, this check observes storage IP network rules. Restricted storage data-plane design could pass storage IP network rules while user delegation SAS is wrong; restricted storage data-plane design still lacks user delegation SAS proof.
- **D — Incorrect.** Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
  Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry. In the restricted storage data-plane design, this check observes service and account SAS scope. Restricted storage data-plane design output covers service and account SAS scope, not user delegation SAS; the user delegation SAS requirement to have a Microsoft Entra principal sign temporary Blob access instead of an account credential remains unverified.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Create a user delegation SAS with Azure CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

**Source reviewed:** 2026-08-31

## LAB07-Q27 — D

**Question:** The storage security administrator restricting data-plane access must confirm the restricted storage data-plane design, without mutation, can bound delegated access to an intentional start and expiry window. Which network perimeter check qualifies?

- **A — Incorrect.** Scan evidence for secrets and verify data commands use login-based authorization where supported.
  Scan evidence for secrets and verify data commands use login-based authorization where supported. In the restricted storage data-plane design, this check observes account-key exposure. Restricted storage data-plane design reads account-key exposure, leaving SAS start and expiry time unproved in restricted storage data-plane design; restricted storage data-plane design still has no SAS start and expiry time proof.
- **B — Incorrect.** Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
  Query both subnet serviceEndpoints and the account virtualNetworkRules collection. In the restricted storage data-plane design, this check observes virtual-network service endpoints. Restricted storage data-plane design could pass virtual-network service endpoints while SAS start and expiry time is wrong; restricted storage data-plane design still lacks SAS start and expiry time proof.
- **C — Incorrect.** Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
  Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions. In the restricted storage data-plane design, this check observes user delegation SAS. Restricted storage data-plane design output covers user delegation SAS, not SAS start and expiry time; the SAS start and expiry time requirement to bound delegated access to an intentional start and expiry window remains unverified.
- **D — Correct.** Inspect st and se values and test the minimum required operation before distribution.
  Inspect st and se values and test the minimum required operation before distribution. Because the restricted storage data-plane design check observes SAS start and expiry time, it independently verifies the requirement to bound delegated access to an intentional start and expiry window.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Create an expiration policy for shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/sas-expiration-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q28 — B

**Question:** The restricted storage data-plane design configuration is complete; the network perimeter reviewers need evidence it can attach revocable constraints to service-level delegated tokens. Which observation shows success?

- **A — Incorrect.** Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
  Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule. In the restricted storage data-plane design, this check observes storage firewall default action. Restricted storage data-plane design could pass storage firewall default action while stored access policies is wrong; restricted storage data-plane design still lacks stored access policies proof.
- **B — Correct.** List signed identifiers on the resource and confirm the SAS si field names the expected policy.
  The restricted storage data-plane design validator needs this stored access policies result: list signed identifiers on the resource and confirm the SAS si field names the expected policy. It proves the outcome to attach revocable constraints to service-level delegated tokens rather than an adjacent checkpoint.
- **C — Incorrect.** Query networkRuleSet.bypass and compare it with the approved exception list.
  Query networkRuleSet.bypass and compare it with the approved exception list. In the restricted storage data-plane design, this check observes trusted Azure service bypass. Trusted Azure service bypass success in restricted storage data-plane design cannot verify stored access policies; restricted storage data-plane design cannot attach revocable constraints to service-level delegated tokens until stored access policies evidence exists.
- **D — Incorrect.** Inspect st and se values and test the minimum required operation before distribution.
  Inspect st and se values and test the minimum required operation before distribution. In the restricted storage data-plane design, this check observes SAS start and expiry time. Restricted storage data-plane design reads SAS start and expiry time, leaving stored access policies unproved in restricted storage data-plane design; restricted storage data-plane design still has no stored access policies proof.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q29 — A

**Question:** The network perimeter validation asks whether the restricted storage data-plane design can invalidate tokens that refer to a named server-side access policy. Which observable state is strongest?

- **A — Correct.** List the signed identifiers and retest the previously issued SAS until the policy change is effective.
  List the signed identifiers and retest the previously issued SAS until the policy change is effective. This is independent stored-policy revocation evidence for the restricted storage data-plane design, even if restricted storage data-plane design setup reports success before stored-policy revocation becomes observable.
- **B — Incorrect.** Query ipRules and match the normalized CIDR value and Allow action.
  Query ipRules and match the normalized CIDR value and Allow action. In the restricted storage data-plane design, this check observes storage IP network rules. Storage IP network rules success in restricted storage data-plane design cannot verify stored-policy revocation; restricted storage data-plane design cannot invalidate tokens that refer to a named server-side access policy until stored-policy revocation evidence exists.
- **C — Incorrect.** Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
  Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry. In the restricted storage data-plane design, this check observes service and account SAS scope. Restricted storage data-plane design reads service and account SAS scope, leaving stored-policy revocation unproved in restricted storage data-plane design; restricted storage data-plane design still has no stored-policy revocation proof.
- **D — Incorrect.** List signed identifiers on the resource and confirm the SAS si field names the expected policy.
  List signed identifiers on the resource and confirm the SAS si field names the expected policy. In the restricted storage data-plane design, this check observes stored access policies. Restricted storage data-plane design could pass stored access policies while stored-policy revocation is wrong; restricted storage data-plane design still lacks stored-policy revocation proof.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q30 — D

**Question:** A restricted storage data-plane design review must prove the network perimeter ability to avoid exposing a credential that grants broad authority over the account. Which check avoids an adjacent feature?

- **A — Incorrect.** Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
  Query both subnet serviceEndpoints and the account virtualNetworkRules collection. In the restricted storage data-plane design, this check observes virtual-network service endpoints. Virtual-network service endpoints success in restricted storage data-plane design cannot verify account-key exposure; restricted storage data-plane design cannot avoid exposing a credential that grants broad authority over the account until account-key exposure evidence exists.
- **B — Incorrect.** Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
  Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions. In the restricted storage data-plane design, this check observes user delegation SAS. Restricted storage data-plane design reads user delegation SAS, leaving account-key exposure unproved in restricted storage data-plane design; restricted storage data-plane design still has no account-key exposure proof.
- **C — Incorrect.** List the signed identifiers and retest the previously issued SAS until the policy change is effective.
  List the signed identifiers and retest the previously issued SAS until the policy change is effective. In the restricted storage data-plane design, this check observes stored-policy revocation. Restricted storage data-plane design could pass stored-policy revocation while account-key exposure is wrong; restricted storage data-plane design still lacks account-key exposure proof.
- **D — Correct.** Scan evidence for secrets and verify data commands use login-based authorization where supported.
  Scan evidence for secrets and verify data commands use login-based authorization where supported. For restricted storage data-plane design, this account-key exposure read confirms the service can avoid exposing a credential that grants broad authority over the account.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB07-Q31 — B

**Question:** A restricted storage data-plane design query surprises the storage security administrator restricting data-plane access during the network perimeter attempt to deny public-endpoint traffic unless an explicit network exception allows it. Which finding explains it?

- **A — Incorrect.** The rule contains a private client address rather than the client's public egress address.
  The rule contains a private client address rather than the client's public egress address. The restricted storage data-plane design fault concerns storage IP network rules. Restricted storage data-plane design has storage IP network rules impact, but storage firewall default action is the restricted storage data-plane design failed path; the storage IP network rules state cannot produce storage firewall default action failure.
- **B — Correct.** DefaultAction remains Allow, so traffic from unlisted public networks is accepted.
  DefaultAction remains Allow, so traffic from unlisted public networks is accepted. This restricted storage data-plane design condition breaks storage firewall default action, explaining why operators cannot deny public-endpoint traffic unless an explicit network exception allows it.
- **C — Incorrect.** The caller lacks the data action needed to request a user delegation key.
  The caller lacks the data action needed to request a user delegation key. The restricted storage data-plane design fault concerns user delegation SAS. Restricted storage data-plane design failed on storage firewall default action; this user delegation SAS finding redirects restricted storage data-plane design remediation away from storage firewall default action.
- **D — Incorrect.** A full account key was copied into a committed command transcript.
  A full account key was copied into a committed command transcript. The restricted storage data-plane design fault concerns account-key exposure. Restricted storage data-plane design may fix account-key exposure, yet storage firewall default action still fails; this restricted storage data-plane design diagnosis of account-key exposure is wrong for storage firewall default action.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q32 — B

**Question:** Other restricted storage data-plane design components are healthy, but the network perimeter still cannot permit traffic at the public service address only from an approved IPv4 range. Which state causes the isolated failure?

- **A — Incorrect.** The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled.
  The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled. The restricted storage data-plane design fault concerns virtual-network service endpoints. Restricted storage data-plane design could repair virtual-network service endpoints while storage IP network rules stays broken in restricted storage data-plane design; the restricted storage data-plane design remains unable to permit traffic at the public service address only from an approved IPv4 range.
- **B — Correct.** The rule contains a private client address rather than the client's public egress address.
  For the restricted storage data-plane design, the storage IP network rules failure is causal: the rule contains a private client address rather than the client's public egress address. Correcting it restores the ability to permit traffic at the public service address only from an approved IPv4 range.
- **C — Incorrect.** The SAS start time is later than the client's current clock, so authorization is not yet valid.
  The SAS start time is later than the client's current clock, so authorization is not yet valid. The restricted storage data-plane design fault concerns SAS start and expiry time. Restricted storage data-plane design may fix SAS start and expiry time, yet storage IP network rules still fails; this restricted storage data-plane design diagnosis of SAS start and expiry time is wrong for storage IP network rules.
- **D — Incorrect.** DefaultAction remains Allow, so traffic from unlisted public networks is accepted.
  DefaultAction remains Allow, so traffic from unlisted public networks is accepted. The restricted storage data-plane design fault concerns storage firewall default action. Restricted storage data-plane design has storage firewall default action impact, but storage IP network rules is the restricted storage data-plane design failed path; the storage firewall default action state cannot produce storage IP network rules failure.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q33 — D

**Question:** During a network perimeter fault drill, the restricted storage data-plane design does not authorize one subnet on the service firewall while retaining the public endpoint. Which finding identifies the defect?

- **A — Incorrect.** The design assumes the AzureServices bypass grants access to any workload hosted in Azure.
  The design assumes the AzureServices bypass grants access to any workload hosted in Azure. The restricted storage data-plane design fault concerns trusted Azure service bypass. Restricted storage data-plane design failed on virtual-network service endpoints; this trusted Azure service bypass finding redirects restricted storage data-plane design remediation away from virtual-network service endpoints.
- **B — Incorrect.** The SAS embeds ad hoc permissions and does not reference the stored policy identifier.
  The SAS embeds ad hoc permissions and does not reference the stored policy identifier. The restricted storage data-plane design fault concerns stored access policies. Restricted storage data-plane design may fix stored access policies, yet virtual-network service endpoints still fails; this restricted storage data-plane design diagnosis of stored access policies is wrong for virtual-network service endpoints.
- **C — Incorrect.** The rule contains a private client address rather than the client's public egress address.
  The rule contains a private client address rather than the client's public egress address. The restricted storage data-plane design fault concerns storage IP network rules. Restricted storage data-plane design has storage IP network rules impact, but virtual-network service endpoints is the restricted storage data-plane design failed path; the storage IP network rules state cannot produce virtual-network service endpoints failure.
- **D — Correct.** The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled.
  The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled. The finding is specific to virtual-network service endpoints in the restricted storage data-plane design; repairing virtual-network service endpoints restores the restricted storage data-plane design ability to authorize one subnet on the service firewall while retaining the public endpoint.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q34 — D

**Question:** The restricted storage data-plane design setup finishes, yet the network perimeter cannot allow only the limited platform services supported by the firewall bypass. Which misconfiguration explains the mismatch?

- **A — Incorrect.** An account SAS grants Queue and Table access even though the consumer needs only one blob container.
  An account SAS grants Queue and Table access even though the consumer needs only one blob container. The restricted storage data-plane design fault concerns service and account SAS scope. Restricted storage data-plane design may fix service and account SAS scope, yet trusted Azure service bypass still fails; this restricted storage data-plane design diagnosis of service and account SAS scope is wrong for trusted Azure service bypass.
- **B — Incorrect.** The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it.
  The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it. The restricted storage data-plane design fault concerns stored-policy revocation. Restricted storage data-plane design has stored-policy revocation impact, but trusted Azure service bypass is the restricted storage data-plane design failed path; the stored-policy revocation state cannot produce trusted Azure service bypass failure.
- **C — Incorrect.** The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled.
  The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled. The restricted storage data-plane design fault concerns virtual-network service endpoints. Restricted storage data-plane design could repair virtual-network service endpoints while trusted Azure service bypass stays broken in restricted storage data-plane design; the restricted storage data-plane design remains unable to allow only the limited platform services supported by the firewall bypass.
- **D — Correct.** The design assumes the AzureServices bypass grants access to any workload hosted in Azure.
  The restricted storage data-plane design cannot allow only the limited platform services supported by the firewall bypass because of this trusted Azure service bypass defect: the design assumes the AzureServices bypass grants access to any workload hosted in Azure. The symptom and repair align.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q35 — A

**Question:** A network perimeter break/fix in the restricted storage data-plane design fails when operators try to choose whether delegated access covers one service or several account services. Which diagnosis fits?

- **A — Correct.** An account SAS grants Queue and Table access even though the consumer needs only one blob container.
  An account SAS grants Queue and Table access even though the consumer needs only one blob container. Removing this service and account SAS scope condition lets the restricted storage data-plane design choose whether delegated access covers one service or several account services while leaving healthy controls unchanged.
- **B — Incorrect.** The caller lacks the data action needed to request a user delegation key.
  The caller lacks the data action needed to request a user delegation key. The restricted storage data-plane design fault concerns user delegation SAS. Restricted storage data-plane design could repair user delegation SAS while service and account SAS scope stays broken in restricted storage data-plane design; the restricted storage data-plane design remains unable to choose whether delegated access covers one service or several account services.
- **C — Incorrect.** A full account key was copied into a committed command transcript.
  A full account key was copied into a committed command transcript. The restricted storage data-plane design fault concerns account-key exposure. Restricted storage data-plane design failed on service and account SAS scope; this account-key exposure finding redirects restricted storage data-plane design remediation away from service and account SAS scope.
- **D — Incorrect.** The design assumes the AzureServices bypass grants access to any workload hosted in Azure.
  The design assumes the AzureServices bypass grants access to any workload hosted in Azure. The restricted storage data-plane design fault concerns trusted Azure service bypass. Restricted storage data-plane design may fix trusted Azure service bypass, yet service and account SAS scope still fails; this restricted storage data-plane design diagnosis of trusted Azure service bypass is wrong for service and account SAS scope.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Grant limited access with shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)

**Source reviewed:** 2026-08-31

## LAB07-Q36 — D

**Question:** The restricted storage data-plane design troubleshooting scope is the network perimeter need to have a Microsoft Entra principal sign temporary Blob access instead of an account credential. Which condition should be corrected first?

- **A — Incorrect.** The SAS start time is later than the client's current clock, so authorization is not yet valid.
  The SAS start time is later than the client's current clock, so authorization is not yet valid. The restricted storage data-plane design fault concerns SAS start and expiry time. Restricted storage data-plane design could repair SAS start and expiry time while user delegation SAS stays broken in restricted storage data-plane design; the restricted storage data-plane design remains unable to have a Microsoft Entra principal sign temporary Blob access instead of an account credential.
- **B — Incorrect.** DefaultAction remains Allow, so traffic from unlisted public networks is accepted.
  DefaultAction remains Allow, so traffic from unlisted public networks is accepted. The restricted storage data-plane design fault concerns storage firewall default action. Restricted storage data-plane design failed on user delegation SAS; this storage firewall default action finding redirects restricted storage data-plane design remediation away from user delegation SAS.
- **C — Incorrect.** An account SAS grants Queue and Table access even though the consumer needs only one blob container.
  An account SAS grants Queue and Table access even though the consumer needs only one blob container. The restricted storage data-plane design fault concerns service and account SAS scope. Restricted storage data-plane design may fix service and account SAS scope, yet user delegation SAS still fails; this restricted storage data-plane design diagnosis of service and account SAS scope is wrong for user delegation SAS.
- **D — Correct.** The caller lacks the data action needed to request a user delegation key.
  The caller lacks the data action needed to request a user delegation key. In restricted storage data-plane design, this user delegation SAS cause matches the failure to have a Microsoft Entra principal sign temporary Blob access instead of an account credential.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Create a user delegation SAS with Azure CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

**Source reviewed:** 2026-08-31

## LAB07-Q37 — A

**Question:** The restricted storage data-plane design result is partial because the network perimeter cannot bound delegated access to an intentional start and expiry window. Which condition accounts for that result?

- **A — Correct.** The SAS start time is later than the client's current clock, so authorization is not yet valid.
  The SAS start time is later than the client's current clock, so authorization is not yet valid. This restricted storage data-plane design condition breaks SAS start and expiry time, explaining why operators cannot bound delegated access to an intentional start and expiry window.
- **B — Incorrect.** The SAS embeds ad hoc permissions and does not reference the stored policy identifier.
  The SAS embeds ad hoc permissions and does not reference the stored policy identifier. The restricted storage data-plane design fault concerns stored access policies. Restricted storage data-plane design may fix stored access policies, yet SAS start and expiry time still fails; this restricted storage data-plane design diagnosis of stored access policies is wrong for SAS start and expiry time.
- **C — Incorrect.** The rule contains a private client address rather than the client's public egress address.
  The rule contains a private client address rather than the client's public egress address. The restricted storage data-plane design fault concerns storage IP network rules. Restricted storage data-plane design has storage IP network rules impact, but SAS start and expiry time is the restricted storage data-plane design failed path; the storage IP network rules state cannot produce SAS start and expiry time failure.
- **D — Incorrect.** The caller lacks the data action needed to request a user delegation key.
  The caller lacks the data action needed to request a user delegation key. The restricted storage data-plane design fault concerns user delegation SAS. Restricted storage data-plane design could repair user delegation SAS while SAS start and expiry time stays broken in restricted storage data-plane design; the restricted storage data-plane design remains unable to bound delegated access to an intentional start and expiry window.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Create an expiration policy for shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/sas-expiration-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q38 — B

**Question:** The network perimeter evidence shows the restricted storage data-plane design cannot attach revocable constraints to service-level delegated tokens. Which root cause fits that evidence?

- **A — Incorrect.** The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it.
  The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it. The restricted storage data-plane design fault concerns stored-policy revocation. Restricted storage data-plane design may fix stored-policy revocation, yet stored access policies still fails; this restricted storage data-plane design diagnosis of stored-policy revocation is wrong for stored access policies.
- **B — Correct.** The SAS embeds ad hoc permissions and does not reference the stored policy identifier.
  For the restricted storage data-plane design, the stored access policies failure is causal: the SAS embeds ad hoc permissions and does not reference the stored policy identifier. Correcting it restores the ability to attach revocable constraints to service-level delegated tokens.
- **C — Incorrect.** The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled.
  The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled. The restricted storage data-plane design fault concerns virtual-network service endpoints. Restricted storage data-plane design could repair virtual-network service endpoints while stored access policies stays broken in restricted storage data-plane design; the restricted storage data-plane design remains unable to attach revocable constraints to service-level delegated tokens.
- **D — Incorrect.** The SAS start time is later than the client's current clock, so authorization is not yet valid.
  The SAS start time is later than the client's current clock, so authorization is not yet valid. The restricted storage data-plane design fault concerns SAS start and expiry time. Restricted storage data-plane design failed on stored access policies; this SAS start and expiry time finding redirects restricted storage data-plane design remediation away from stored access policies.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q39 — C

**Question:** Although the restricted storage data-plane design is meant to let the network perimeter invalidate tokens that refer to a named server-side access policy, its checkpoint fails. Which network perimeter defect explains the failure?

- **A — Incorrect.** A full account key was copied into a committed command transcript.
  A full account key was copied into a committed command transcript. The restricted storage data-plane design fault concerns account-key exposure. Restricted storage data-plane design has account-key exposure impact, but stored-policy revocation is the restricted storage data-plane design failed path; the account-key exposure state cannot produce stored-policy revocation failure.
- **B — Incorrect.** The design assumes the AzureServices bypass grants access to any workload hosted in Azure.
  The design assumes the AzureServices bypass grants access to any workload hosted in Azure. The restricted storage data-plane design fault concerns trusted Azure service bypass. Restricted storage data-plane design could repair trusted Azure service bypass while stored-policy revocation stays broken in restricted storage data-plane design; the restricted storage data-plane design remains unable to invalidate tokens that refer to a named server-side access policy.
- **C — Correct.** The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it.
  The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it. The finding is specific to stored-policy revocation in the restricted storage data-plane design; repairing stored-policy revocation restores the restricted storage data-plane design ability to invalidate tokens that refer to a named server-side access policy.
- **D — Incorrect.** The SAS embeds ad hoc permissions and does not reference the stored policy identifier.
  The SAS embeds ad hoc permissions and does not reference the stored policy identifier. The restricted storage data-plane design fault concerns stored access policies. Restricted storage data-plane design may fix stored access policies, yet stored-policy revocation still fails; this restricted storage data-plane design diagnosis of stored access policies is wrong for stored-policy revocation.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q40 — D

**Question:** The network perimeter support team isolated the restricted storage data-plane design incident to the attempt to avoid exposing a credential that grants broad authority over the account. Which condition prevents success?

- **A — Incorrect.** DefaultAction remains Allow, so traffic from unlisted public networks is accepted.
  DefaultAction remains Allow, so traffic from unlisted public networks is accepted. The restricted storage data-plane design fault concerns storage firewall default action. Restricted storage data-plane design could repair storage firewall default action while account-key exposure stays broken in restricted storage data-plane design; the restricted storage data-plane design remains unable to avoid exposing a credential that grants broad authority over the account.
- **B — Incorrect.** An account SAS grants Queue and Table access even though the consumer needs only one blob container.
  An account SAS grants Queue and Table access even though the consumer needs only one blob container. The restricted storage data-plane design fault concerns service and account SAS scope. Restricted storage data-plane design failed on account-key exposure; this service and account SAS scope finding redirects restricted storage data-plane design remediation away from account-key exposure.
- **C — Incorrect.** The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it.
  The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it. The restricted storage data-plane design fault concerns stored-policy revocation. Restricted storage data-plane design may fix stored-policy revocation, yet account-key exposure still fails; this restricted storage data-plane design diagnosis of stored-policy revocation is wrong for account-key exposure.
- **D — Correct.** A full account key was copied into a committed command transcript.
  The restricted storage data-plane design cannot avoid exposing a credential that grants broad authority over the account because of this account-key exposure defect: a full account key was copied into a committed command transcript. The symptom and repair align.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31

## LAB07-Q41 — C

**Question:** The restricted storage data-plane design runbook separates network perimeter mutation from validation while it must deny public-endpoint traffic unless an explicit network exception allows it. Which sequence proves it cleanly?

- **A — Incorrect.** First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
  First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection. This restricted storage data-plane design pair serves virtual-network service endpoints. Virtual-network service endpoints cannot replace storage firewall default action in restricted storage data-plane design. Use this storage firewall default action pair instead: First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
- **B — Incorrect.** First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
  First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution. This restricted storage data-plane design pair serves SAS start and expiry time. Restricted storage data-plane design proves SAS start and expiry time, but storage firewall default action lacks implementation in restricted storage data-plane design and storage firewall default action proof; the storage firewall default action outcome to deny public-endpoint traffic unless an explicit network exception allows it remains open.
- **C — Correct.** First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
  First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule. This ordered storage firewall default action workflow lets the restricted storage data-plane design deny public-endpoint traffic unless an explicit network exception allows it and then verify the resulting state.
- **D — Incorrect.** First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.
  First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy. This restricted storage data-plane design pair serves stored access policies. Restricted storage data-plane design closes stored access policies, not storage firewall default action; without the storage firewall default action workflow, it cannot deny public-endpoint traffic unless an explicit network exception allows it.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q42 — B

**Question:** The restricted storage data-plane design checkpoint requires both this network perimeter outcome—permit traffic at the public service address only from an approved IPv4 range—and a read-only restricted storage data-plane design state check. Which network perimeter response is complete?

- **A — Incorrect.** First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.
  First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list. This restricted storage data-plane design pair serves trusted Azure service bypass. Restricted storage data-plane design proves trusted Azure service bypass, but storage IP network rules lacks implementation in restricted storage data-plane design and storage IP network rules proof; the storage IP network rules outcome to permit traffic at the public service address only from an approved IPv4 range remains open.
- **B — Correct.** First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.
  First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action. For restricted storage data-plane design, the storage IP network rules operation precedes its storage IP network rules read-back check, allowing it to permit traffic at the public service address only from an approved IPv4 range.
- **C — Incorrect.** First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.
  First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy. This restricted storage data-plane design pair serves stored access policies. Restricted storage data-plane design closes stored access policies, not storage IP network rules; without the storage IP network rules workflow, it cannot permit traffic at the public service address only from an approved IPv4 range.
- **D — Incorrect.** First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.
  First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective. This restricted storage data-plane design pair serves stored-policy revocation. Stored-policy revocation cannot replace storage IP network rules in restricted storage data-plane design. Use this storage IP network rules pair instead: First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q43 — C

**Question:** The restricted storage data-plane design runbook must authorize one subnet on the service firewall while retaining the public endpoint, then retain network perimeter read-back evidence. Which restricted storage data-plane design pair completes both duties?

- **A — Incorrect.** First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
  First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry. This restricted storage data-plane design pair serves service and account SAS scope. Restricted storage data-plane design uses service and account SAS scope for both steps; virtual-network service endpoints remains untouched in restricted storage data-plane design, so its virtual-network service endpoints gate to authorize one subnet on the service firewall while retaining the public endpoint fails.
- **B — Incorrect.** First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.
  First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective. This restricted storage data-plane design pair serves stored-policy revocation. Restricted storage data-plane design closes stored-policy revocation, not virtual-network service endpoints; without the virtual-network service endpoints workflow, it cannot authorize one subnet on the service firewall while retaining the public endpoint.
- **C — Correct.** First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
  First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection. In the restricted storage data-plane design, the first virtual-network service endpoints step runs; the restricted storage data-plane design then reads virtual-network service endpoints state to prove it can authorize one subnet on the service firewall while retaining the public endpoint.
- **D — Incorrect.** First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported.
  First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported. This restricted storage data-plane design pair serves account-key exposure. Restricted storage data-plane design proves account-key exposure, but virtual-network service endpoints lacks implementation in restricted storage data-plane design and virtual-network service endpoints proof; the virtual-network service endpoints outcome to authorize one subnet on the service firewall while retaining the public endpoint remains open.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q44 — C

**Question:** To satisfy the network perimeter requirement, operators must change the restricted storage data-plane design configuration and prove it can allow only the limited platform services supported by the firewall bypass. Which sequence is coherent?

- **A — Incorrect.** First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
  First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions. This restricted storage data-plane design pair serves user delegation SAS. Restricted storage data-plane design closes user delegation SAS, not trusted Azure service bypass; without the trusted Azure service bypass workflow, it cannot allow only the limited platform services supported by the firewall bypass.
- **B — Incorrect.** First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported.
  First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported. This restricted storage data-plane design pair serves account-key exposure. Account-key exposure cannot replace trusted Azure service bypass in restricted storage data-plane design. Use this trusted Azure service bypass pair instead: First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.
- **C — Correct.** First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.
  For the restricted storage data-plane design, the safe trusted Azure service bypass order is: first, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list. The restricted storage data-plane design records trusted Azure service bypass proof after configuration.
- **D — Incorrect.** First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
  First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule. This restricted storage data-plane design pair serves storage firewall default action. Restricted storage data-plane design uses storage firewall default action for both steps; trusted Azure service bypass remains untouched in restricted storage data-plane design, so its trusted Azure service bypass gate to allow only the limited platform services supported by the firewall bypass fails.

**Objectives:** `ST-ACCESS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

**Source reviewed:** 2026-08-31

## LAB07-Q45 — C

**Question:** The storage security administrator restricting data-plane access needs a safe restricted storage data-plane design change to choose whether delegated access covers one service or several account services, followed by network perimeter evidence. Which pair merits approval?

- **A — Incorrect.** First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
  First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution. This restricted storage data-plane design pair serves SAS start and expiry time. SAS start and expiry time cannot replace service and account SAS scope in restricted storage data-plane design. Use this service and account SAS scope pair instead: First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
- **B — Incorrect.** First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
  First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule. This restricted storage data-plane design pair serves storage firewall default action. Restricted storage data-plane design proves storage firewall default action, but service and account SAS scope lacks implementation in restricted storage data-plane design and service and account SAS scope proof; the service and account SAS scope outcome to choose whether delegated access covers one service or several account services remains open.
- **C — Correct.** First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
  First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry. The restricted storage data-plane design uses its service and account SAS scope mutation gate and service and account SAS scope verification gate before it can choose whether delegated access covers one service or several account services.
- **D — Incorrect.** First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.
  First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action. This restricted storage data-plane design pair serves storage IP network rules. Restricted storage data-plane design closes storage IP network rules, not service and account SAS scope; without the service and account SAS scope workflow, it cannot choose whether delegated access covers one service or several account services.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Grant limited access with shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)

**Source reviewed:** 2026-08-31

## LAB07-Q46 — B

**Question:** The restricted storage data-plane design has two network perimeter gates: have a Microsoft Entra principal sign temporary Blob access instead of an account credential, then prove the restricted storage data-plane design state. Which network perimeter sequence works?

- **A — Incorrect.** First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.
  First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy. This restricted storage data-plane design pair serves stored access policies. Restricted storage data-plane design proves stored access policies, but user delegation SAS lacks implementation in restricted storage data-plane design and user delegation SAS proof; the user delegation SAS outcome to have a Microsoft Entra principal sign temporary Blob access instead of an account credential remains open.
- **B — Correct.** First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
  The restricted storage data-plane design gets a complete user delegation SAS sequence here: first, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions. Read-back evidence follows the change.
- **C — Incorrect.** First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.
  First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action. This restricted storage data-plane design pair serves storage IP network rules. Restricted storage data-plane design closes storage IP network rules, not user delegation SAS; without the user delegation SAS workflow, it cannot have a Microsoft Entra principal sign temporary Blob access instead of an account credential.
- **D — Incorrect.** First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
  First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection. This restricted storage data-plane design pair serves virtual-network service endpoints. Virtual-network service endpoints cannot replace user delegation SAS in restricted storage data-plane design. Use this user delegation SAS pair instead: First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB07-CP01`).

**Microsoft Learn sources:**

- [Create a user delegation SAS with Azure CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

**Source reviewed:** 2026-08-31

## LAB07-Q47 — A

**Question:** Which network perimeter path makes the restricted storage data-plane design able to bound delegated access to an intentional start and expiry window, then inspects the defining properties?

- **A — Correct.** First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
  First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution. This ordered SAS start and expiry time workflow lets the restricted storage data-plane design bound delegated access to an intentional start and expiry window and then verify the resulting state.
- **B — Incorrect.** First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.
  First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective. This restricted storage data-plane design pair serves stored-policy revocation. Restricted storage data-plane design closes stored-policy revocation, not SAS start and expiry time; without the SAS start and expiry time workflow, it cannot bound delegated access to an intentional start and expiry window.
- **C — Incorrect.** First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
  First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection. This restricted storage data-plane design pair serves virtual-network service endpoints. Virtual-network service endpoints cannot replace SAS start and expiry time in restricted storage data-plane design. Use this SAS start and expiry time pair instead: First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
- **D — Incorrect.** First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.
  First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list. This restricted storage data-plane design pair serves trusted Azure service bypass. Restricted storage data-plane design proves trusted Azure service bypass, but SAS start and expiry time lacks implementation in restricted storage data-plane design and SAS start and expiry time proof; the SAS start and expiry time outcome to bound delegated access to an intentional start and expiry window remains open.

**Objectives:** `ST-ACCESS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB07-CP02`).

**Microsoft Learn sources:**

- [Create an expiration policy for shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/sas-expiration-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q48 — A

**Question:** At the restricted storage data-plane design approval gate, operators must show that the network perimeter can attach revocable constraints to service-level delegated tokens. Which network perimeter configure-and-check pair is defensible?

- **A — Correct.** First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.
  First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy. For restricted storage data-plane design, the stored access policies operation precedes its stored access policies read-back check, allowing it to attach revocable constraints to service-level delegated tokens.
- **B — Incorrect.** First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported.
  First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported. This restricted storage data-plane design pair serves account-key exposure. Account-key exposure cannot replace stored access policies in restricted storage data-plane design. Use this stored access policies pair instead: First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.
- **C — Incorrect.** First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.
  First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list. This restricted storage data-plane design pair serves trusted Azure service bypass. Restricted storage data-plane design proves trusted Azure service bypass, but stored access policies lacks implementation in restricted storage data-plane design and stored access policies proof; the stored access policies outcome to attach revocable constraints to service-level delegated tokens remains open.
- **D — Incorrect.** First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
  First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry. This restricted storage data-plane design pair serves service and account SAS scope. Restricted storage data-plane design uses service and account SAS scope for both steps; stored access policies remains untouched in restricted storage data-plane design, so its stored access policies gate to attach revocable constraints to service-level delegated tokens fails.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB07-CP03`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q49 — C

**Question:** The restricted storage data-plane design forbids a partial network perimeter result. Operators must first invalidate tokens that refer to a named server-side access policy and afterward confirm the restricted storage data-plane design outcome. Which network perimeter sequence is complete?

- **A — Incorrect.** First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
  First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule. This restricted storage data-plane design pair serves storage firewall default action. Storage firewall default action cannot replace stored-policy revocation in restricted storage data-plane design. Use this stored-policy revocation pair instead: First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.
- **B — Incorrect.** First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
  First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry. This restricted storage data-plane design pair serves service and account SAS scope. Restricted storage data-plane design proves service and account SAS scope, but stored-policy revocation lacks implementation in restricted storage data-plane design and stored-policy revocation proof; the stored-policy revocation outcome to invalidate tokens that refer to a named server-side access policy remains open.
- **C — Correct.** First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.
  First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective. In the restricted storage data-plane design, the first stored-policy revocation step runs; the restricted storage data-plane design then reads stored-policy revocation state to prove it can invalidate tokens that refer to a named server-side access policy.
- **D — Incorrect.** First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
  First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions. This restricted storage data-plane design pair serves user delegation SAS. Restricted storage data-plane design closes user delegation SAS, not stored-policy revocation; without the stored-policy revocation workflow, it cannot invalidate tokens that refer to a named server-side access policy.

**Objectives:** `ST-ACCESS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB07-CP04`).

**Microsoft Learn sources:**

- [Define a stored access policy](https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy)

**Source reviewed:** 2026-08-31

## LAB07-Q50 — D

**Question:** Only the restricted storage data-plane design change needed to avoid exposing a credential that grants broad authority over the account is allowed, and network perimeter proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.
  First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action. This restricted storage data-plane design pair serves storage IP network rules. Restricted storage data-plane design proves storage IP network rules, but account-key exposure lacks implementation in restricted storage data-plane design and account-key exposure proof; the account-key exposure outcome to avoid exposing a credential that grants broad authority over the account remains open.
- **B — Incorrect.** First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
  First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions. This restricted storage data-plane design pair serves user delegation SAS. Restricted storage data-plane design uses user delegation SAS for both steps; account-key exposure remains untouched in restricted storage data-plane design, so its account-key exposure gate to avoid exposing a credential that grants broad authority over the account fails.
- **C — Incorrect.** First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
  First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution. This restricted storage data-plane design pair serves SAS start and expiry time. Restricted storage data-plane design closes SAS start and expiry time, not account-key exposure; without the account-key exposure workflow, it cannot avoid exposing a credential that grants broad authority over the account.
- **D — Correct.** First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported.
  For the restricted storage data-plane design, the safe account-key exposure order is: first, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported. The restricted storage data-plane design records account-key exposure proof after configuration.

**Objectives:** `ST-ACCESS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB07-CP05`).

**Microsoft Learn sources:**

- [Prevent Shared Key authorization for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

**Source reviewed:** 2026-08-31
