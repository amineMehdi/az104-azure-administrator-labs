# Lab 07 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB07-Q01 — Foundational

The restricted storage data-plane design handoff omits the network perimeter rule needed to deny public-endpoint traffic unless an explicit network exception allows it. Which statement should the team add?

- A. An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range.
- B. A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types.
- C. A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions.
- D. A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier.

## LAB07-Q02 — Foundational

A network perimeter incident review of the restricted storage data-plane design depends on the ability to permit traffic at the public service address only from an approved IPv4 range. Which platform description is reliable?

- A. A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint.
- B. A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key.
- C. An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range.
- D. Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation.

## LAB07-Q03 — Foundational

A storage security administrator restricting data-plane access is updating the network perimeter runbook. The requirement is to authorize one subnet on the service firewall while retaining the public endpoint. Which statement describes Azure behavior correctly?

- A. A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.
- B. A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint.
- C. A SAS is valid only within its signed time window, subject to clock skew and service interpretation.
- D. Anyone holding a storage account key can authorize broad shared-key operations permitted by the service.

## LAB07-Q04 — Foundational

A network perimeter peer review asks how the restricted storage data-plane design should handle this outcome: allow only the limited platform services supported by the firewall bypass. Which explanation is accurate?

- A. A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.
- B. A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types.
- C. A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier.
- D. A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions.

## LAB07-Q05 — Foundational

For the restricted storage data-plane design, the network perimeter plan must choose whether delegated access covers one service or several account services. Which statement about network perimeter belongs in the restricted storage data-plane design record?

- A. A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types.
- B. A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key.
- C. Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation.
- D. An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range.

## LAB07-Q06 — Foundational

The network perimeter review compares four claims for the restricted storage data-plane design requirement to have a Microsoft Entra principal sign temporary Blob access instead of an account credential. Which claim is technically sound?

- A. A SAS is valid only within its signed time window, subject to clock skew and service interpretation.
- B. A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key.
- C. Anyone holding a storage account key can authorize broad shared-key operations permitted by the service.
- D. A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint.

## LAB07-Q07 — Foundational

The network perimeter architecture note requires the restricted storage data-plane design environment to bound delegated access to an intentional start and expiry window. Which statement defines the relevant network perimeter boundary?

- A. A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier.
- B. A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions.
- C. A SAS is valid only within its signed time window, subject to clock skew and service interpretation.
- D. A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.

## LAB07-Q08 — Foundational

A new network perimeter operator must explain why the restricted storage data-plane design can attach revocable constraints to service-level delegated tokens. Which explanation is accurate?

- A. Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation.
- B. An IP network rule permits public-endpoint requests originating from a listed public IPv4 address or CIDR range.
- C. A stored access policy on a container or share can supply constraints for service SAS tokens that reference its identifier.
- D. A service SAS delegates access to one storage service, whereas an account SAS can cover multiple services and resource types.

## LAB07-Q09 — Foundational

The restricted storage data-plane design acceptance criteria require operators to invalidate tokens that refer to a named server-side access policy. Which service fact supports that requirement?

- A. Anyone holding a storage account key can authorize broad shared-key operations permitted by the service.
- B. A Microsoft.Storage service endpoint lets a selected subnet identity be authorized on a storage firewall while traffic reaches the service public endpoint.
- C. Changing or deleting a stored access policy can revoke service SAS tokens associated with that policy after propagation.
- D. A user delegation SAS for Blob Storage is signed with a Microsoft Entra user delegation key rather than an account key.

## LAB07-Q10 — Foundational

A network perimeter reviewer challenges whether the restricted storage data-plane design can avoid exposing a credential that grants broad authority over the account. Which response resolves the concern?

- A. A default action of Deny restricts the public endpoint to explicitly allowed networks and exceptions.
- B. A trusted-services bypass is a specific exception and does not allow every Azure resource to bypass the firewall.
- C. A SAS is valid only within its signed time window, subject to clock skew and service interpretation.
- D. Anyone holding a storage account key can authorize broad shared-key operations permitted by the service.

## LAB07-Q11 — Foundational

The network perimeter preflight has passed; the restricted storage data-plane design must now deny public-endpoint traffic unless an explicit network exception allows it. Which operation should run?

- A. Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules.
- B. Set the storage network rule default action to Deny after adding the administrator's approved access path.
- C. Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
- D. Revoke delegated access by changing or removing the referenced stored access policy.

## LAB07-Q12 — Foundational

The restricted storage data-plane design plan must permit traffic at the public service address only from an approved IPv4 range while limiting the mutation scope to network perimeter. Which action is appropriate?

- A. Enable only the documented trusted-service bypass required by the workload.
- B. Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use.
- C. Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens.
- D. Add only the approved public egress address to the account network rules.

## LAB07-Q13 — Foundational

A network perimeter ticket in the restricted storage data-plane design says to authorize one subnet on the service firewall while retaining the public endpoint. Which network perimeter action completes the restricted storage data-plane design request with minimal change?

- A. Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request.
- B. Create a named stored access policy and generate the service SAS with that policy identifier.
- C. Set the storage network rule default action to Deny after adding the administrator's approved access path.
- D. Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules.

## LAB07-Q14 — Foundational

The approach for the restricted storage data-plane design is approved, but the network perimeter environment still cannot allow only the limited platform services supported by the firewall bypass. Which implementation step closes the gap?

- A. Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
- B. Enable only the documented trusted-service bypass required by the workload.
- C. Revoke delegated access by changing or removing the referenced stored access policy.
- D. Add only the approved public egress address to the account network rules.

## LAB07-Q15 — Foundational

The storage security administrator restricting data-plane access may change the restricted storage data-plane design only to choose whether delegated access covers one service or several account services. Which network perimeter action stays within that assignment?

- A. Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use.
- B. Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request.
- C. Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens.
- D. Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules.

## LAB07-Q16 — Applied

A network perimeter dry run shows no restricted storage data-plane design command will have a Microsoft Entra principal sign temporary Blob access instead of an account credential. Which action belongs before execution?

- A. Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
- B. Create a named stored access policy and generate the service SAS with that policy identifier.
- C. Set the storage network rule default action to Deny after adding the administrator's approved access path.
- D. Enable only the documented trusted-service bypass required by the workload.

## LAB07-Q17 — Applied

For the restricted storage data-plane design, operators need to bound delegated access to an intentional start and expiry window. Which change realizes that requirement?

- A. Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use.
- B. Revoke delegated access by changing or removing the referenced stored access policy.
- C. Add only the approved public egress address to the account network rules.
- D. Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request.

## LAB07-Q18 — Applied

Operators must automate the restricted storage data-plane design change needed to attach revocable constraints to service-level delegated tokens. Which network perimeter operation belongs in the runbook?

- A. Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens.
- B. Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules.
- C. Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS.
- D. Create a named stored access policy and generate the service SAS with that policy identifier.

## LAB07-Q19 — Applied

A restricted storage data-plane design review finds network perimeter drift from the need to invalidate tokens that refer to a named server-side access policy. Which correction addresses that drift?

- A. Set the storage network rule default action to Deny after adding the administrator's approved access path.
- B. Enable only the documented trusted-service bypass required by the workload.
- C. Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use.
- D. Revoke delegated access by changing or removing the referenced stored access policy.

## LAB07-Q20 — Applied

The restricted storage data-plane design window permits only the network perimeter change needed to avoid exposing a credential that grants broad authority over the account. Which option respects the boundary?

- A. Add only the approved public egress address to the account network rules.
- B. Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request.
- C. Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens.
- D. Create a named stored access policy and generate the service SAS with that policy identifier.

## LAB07-Q21 — Applied

The restricted storage data-plane design evidence bundle needs a network perimeter result showing it can deny public-endpoint traffic unless an explicit network exception allows it. Which result belongs in the checkpoint?

- A. Query networkRuleSet.bypass and compare it with the approved exception list.
- B. Inspect st and se values and test the minimum required operation before distribution.
- C. Scan evidence for secrets and verify data commands use login-based authorization where supported.
- D. Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.

## LAB07-Q22 — Applied

Before restricted storage data-plane design cleanup, the network perimeter team must reconfirm it can permit traffic at the public service address only from an approved IPv4 range. Which read-only inspection should run?

- A. Query ipRules and match the normalized CIDR value and Allow action.
- B. Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
- C. List signed identifiers on the resource and confirm the SAS si field names the expected policy.
- D. Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.

## LAB07-Q23 — Applied

The restricted storage data-plane design setup reports success after the network perimeter attempt to authorize one subnet on the service firewall while retaining the public endpoint. Which network perimeter read-only observation proves the restricted storage data-plane design outcome?

- A. Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
- B. List the signed identifiers and retest the previously issued SAS until the policy change is effective.
- C. Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
- D. Query ipRules and match the normalized CIDR value and Allow action.

## LAB07-Q24 — Applied

The network perimeter log says the restricted storage data-plane design can now allow only the limited platform services supported by the firewall bypass. Which network perimeter state should the restricted storage data-plane design acceptance test retain?

- A. Inspect st and se values and test the minimum required operation before distribution.
- B. Query networkRuleSet.bypass and compare it with the approved exception list.
- C. Scan evidence for secrets and verify data commands use login-based authorization where supported.
- D. Query both subnet serviceEndpoints and the account virtualNetworkRules collection.

## LAB07-Q25 — Applied

The restricted storage data-plane design rejects network perimeter exit status as proof it can choose whether delegated access covers one service or several account services. Which restricted storage data-plane design result is valid evidence?

- A. Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
- B. List signed identifiers on the resource and confirm the SAS si field names the expected policy.
- C. Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
- D. Query networkRuleSet.bypass and compare it with the approved exception list.

## LAB07-Q26 — Applied

The network perimeter validator needs one restricted storage data-plane design query after the change to have a Microsoft Entra principal sign temporary Blob access instead of an account credential. Which network perimeter property should the restricted storage data-plane design validator inspect?

- A. Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
- B. List the signed identifiers and retest the previously issued SAS until the policy change is effective.
- C. Query ipRules and match the normalized CIDR value and Allow action.
- D. Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.

## LAB07-Q27 — Applied

The storage security administrator restricting data-plane access must confirm the restricted storage data-plane design, without mutation, can bound delegated access to an intentional start and expiry window. Which network perimeter check qualifies?

- A. Scan evidence for secrets and verify data commands use login-based authorization where supported.
- B. Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
- C. Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
- D. Inspect st and se values and test the minimum required operation before distribution.

## LAB07-Q28 — Applied

The restricted storage data-plane design configuration is complete; the network perimeter reviewers need evidence it can attach revocable constraints to service-level delegated tokens. Which observation shows success?

- A. Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
- B. List signed identifiers on the resource and confirm the SAS si field names the expected policy.
- C. Query networkRuleSet.bypass and compare it with the approved exception list.
- D. Inspect st and se values and test the minimum required operation before distribution.

## LAB07-Q29 — Applied

The network perimeter validation asks whether the restricted storage data-plane design can invalidate tokens that refer to a named server-side access policy. Which observable state is strongest?

- A. List the signed identifiers and retest the previously issued SAS until the policy change is effective.
- B. Query ipRules and match the normalized CIDR value and Allow action.
- C. Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
- D. List signed identifiers on the resource and confirm the SAS si field names the expected policy.

## LAB07-Q30 — Applied

A restricted storage data-plane design review must prove the network perimeter ability to avoid exposing a credential that grants broad authority over the account. Which check avoids an adjacent feature?

- A. Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
- B. Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
- C. List the signed identifiers and retest the previously issued SAS until the policy change is effective.
- D. Scan evidence for secrets and verify data commands use login-based authorization where supported.

## LAB07-Q31 — Applied

A restricted storage data-plane design query surprises the storage security administrator restricting data-plane access during the network perimeter attempt to deny public-endpoint traffic unless an explicit network exception allows it. Which finding explains it?

- A. The rule contains a private client address rather than the client's public egress address.
- B. DefaultAction remains Allow, so traffic from unlisted public networks is accepted.
- C. The caller lacks the data action needed to request a user delegation key.
- D. A full account key was copied into a committed command transcript.

## LAB07-Q32 — Applied

Other restricted storage data-plane design components are healthy, but the network perimeter still cannot permit traffic at the public service address only from an approved IPv4 range. Which state causes the isolated failure?

- A. The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled.
- B. The rule contains a private client address rather than the client's public egress address.
- C. The SAS start time is later than the client's current clock, so authorization is not yet valid.
- D. DefaultAction remains Allow, so traffic from unlisted public networks is accepted.

## LAB07-Q33 — Applied

During a network perimeter fault drill, the restricted storage data-plane design does not authorize one subnet on the service firewall while retaining the public endpoint. Which finding identifies the defect?

- A. The design assumes the AzureServices bypass grants access to any workload hosted in Azure.
- B. The SAS embeds ad hoc permissions and does not reference the stored policy identifier.
- C. The rule contains a private client address rather than the client's public egress address.
- D. The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled.

## LAB07-Q34 — Applied

The restricted storage data-plane design setup finishes, yet the network perimeter cannot allow only the limited platform services supported by the firewall bypass. Which misconfiguration explains the mismatch?

- A. An account SAS grants Queue and Table access even though the consumer needs only one blob container.
- B. The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it.
- C. The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled.
- D. The design assumes the AzureServices bypass grants access to any workload hosted in Azure.

## LAB07-Q35 — Applied

A network perimeter break/fix in the restricted storage data-plane design fails when operators try to choose whether delegated access covers one service or several account services. Which diagnosis fits?

- A. An account SAS grants Queue and Table access even though the consumer needs only one blob container.
- B. The caller lacks the data action needed to request a user delegation key.
- C. A full account key was copied into a committed command transcript.
- D. The design assumes the AzureServices bypass grants access to any workload hosted in Azure.

## LAB07-Q36 — Applied

The restricted storage data-plane design troubleshooting scope is the network perimeter need to have a Microsoft Entra principal sign temporary Blob access instead of an account credential. Which condition should be corrected first?

- A. The SAS start time is later than the client's current clock, so authorization is not yet valid.
- B. DefaultAction remains Allow, so traffic from unlisted public networks is accepted.
- C. An account SAS grants Queue and Table access even though the consumer needs only one blob container.
- D. The caller lacks the data action needed to request a user delegation key.

## LAB07-Q37 — Applied

The restricted storage data-plane design result is partial because the network perimeter cannot bound delegated access to an intentional start and expiry window. Which condition accounts for that result?

- A. The SAS start time is later than the client's current clock, so authorization is not yet valid.
- B. The SAS embeds ad hoc permissions and does not reference the stored policy identifier.
- C. The rule contains a private client address rather than the client's public egress address.
- D. The caller lacks the data action needed to request a user delegation key.

## LAB07-Q38 — Applied

The network perimeter evidence shows the restricted storage data-plane design cannot attach revocable constraints to service-level delegated tokens. Which root cause fits that evidence?

- A. The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it.
- B. The SAS embeds ad hoc permissions and does not reference the stored policy identifier.
- C. The subnet is listed in the firewall but does not have the Microsoft.Storage service endpoint enabled.
- D. The SAS start time is later than the client's current clock, so authorization is not yet valid.

## LAB07-Q39 — Applied

Although the restricted storage data-plane design is meant to let the network perimeter invalidate tokens that refer to a named server-side access policy, its checkpoint fails. Which network perimeter defect explains the failure?

- A. A full account key was copied into a committed command transcript.
- B. The design assumes the AzureServices bypass grants access to any workload hosted in Azure.
- C. The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it.
- D. The SAS embeds ad hoc permissions and does not reference the stored policy identifier.

## LAB07-Q40 — Applied

The network perimeter support team isolated the restricted storage data-plane design incident to the attempt to avoid exposing a credential that grants broad authority over the account. Which condition prevents success?

- A. DefaultAction remains Allow, so traffic from unlisted public networks is accepted.
- B. An account SAS grants Queue and Table access even though the consumer needs only one blob container.
- C. The token is an ad hoc SAS, so deleting an unrelated stored access policy does not revoke it.
- D. A full account key was copied into a committed command transcript.

## LAB07-Q41 — Advanced

The restricted storage data-plane design runbook separates network perimeter mutation from validation while it must deny public-endpoint traffic unless an explicit network exception allows it. Which sequence proves it cleanly?

- A. First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
- B. First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
- C. First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
- D. First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.

## LAB07-Q42 — Advanced

The restricted storage data-plane design checkpoint requires both this network perimeter outcome—permit traffic at the public service address only from an approved IPv4 range—and a read-only restricted storage data-plane design state check. Which network perimeter response is complete?

- A. First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.
- B. First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.
- C. First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.
- D. First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.

## LAB07-Q43 — Advanced

The restricted storage data-plane design runbook must authorize one subnet on the service firewall while retaining the public endpoint, then retain network perimeter read-back evidence. Which restricted storage data-plane design pair completes both duties?

- A. First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
- B. First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.
- C. First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
- D. First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported.

## LAB07-Q44 — Advanced

To satisfy the network perimeter requirement, operators must change the restricted storage data-plane design configuration and prove it can allow only the limited platform services supported by the firewall bypass. Which sequence is coherent?

- A. First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
- B. First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported.
- C. First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.
- D. First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.

## LAB07-Q45 — Advanced

The storage security administrator restricting data-plane access needs a safe restricted storage data-plane design change to choose whether delegated access covers one service or several account services, followed by network perimeter evidence. Which pair merits approval?

- A. First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
- B. First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
- C. First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
- D. First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.

## LAB07-Q46 — Advanced

The restricted storage data-plane design has two network perimeter gates: have a Microsoft Entra principal sign temporary Blob access instead of an account credential, then prove the restricted storage data-plane design state. Which network perimeter sequence works?

- A. First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.
- B. First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
- C. First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.
- D. First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection.

## LAB07-Q47 — Advanced

Which network perimeter path makes the restricted storage data-plane design able to bound delegated access to an intentional start and expiry window, then inspects the defining properties?

- A. First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
- B. First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.
- C. First, Enable the Microsoft.Storage endpoint on the subnet and add that subnet resource ID to the storage network rules. Then, Query both subnet serviceEndpoints and the account virtualNetworkRules collection.
- D. First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.

## LAB07-Q48 — Advanced

At the restricted storage data-plane design approval gate, operators must show that the network perimeter can attach revocable constraints to service-level delegated tokens. Which network perimeter configure-and-check pair is defensible?

- A. First, Create a named stored access policy and generate the service SAS with that policy identifier. Then, List signed identifiers on the resource and confirm the SAS si field names the expected policy.
- B. First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported.
- C. First, Enable only the documented trusted-service bypass required by the workload. Then, Query networkRuleSet.bypass and compare it with the approved exception list.
- D. First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.

## LAB07-Q49 — Advanced

The restricted storage data-plane design forbids a partial network perimeter result. Operators must first invalidate tokens that refer to a named server-side access policy and afterward confirm the restricted storage data-plane design outcome. Which network perimeter sequence is complete?

- A. First, Set the storage network rule default action to Deny after adding the administrator's approved access path. Then, Query networkRuleSet.defaultAction and enumerate every IP and virtual-network rule.
- B. First, Choose the narrowest SAS type whose services, resource types, and permissions satisfy the request. Then, Decode or inspect the SAS fields and confirm services, resource types, permissions, and expiry.
- C. First, Revoke delegated access by changing or removing the referenced stored access policy. Then, List the signed identifiers and retest the previously issued SAS until the policy change is effective.
- D. First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.

## LAB07-Q50 — Advanced

Only the restricted storage data-plane design change needed to avoid exposing a credential that grants broad authority over the account is allowed, and network perimeter proof is mandatory. Which pair fits?

- A. First, Add only the approved public egress address to the account network rules. Then, Query ipRules and match the normalized CIDR value and Allow action.
- B. First, Authenticate with Microsoft Entra ID and request a user delegation key before generating the blob SAS. Then, Inspect the SAS fields and confirm user-delegation identifiers are present with the intended permissions.
- C. First, Use a short expiry and omit or backdate the start slightly when clock skew could block immediate use. Then, Inspect st and se values and test the minimum required operation before distribution.
- D. First, Keep account keys out of learner output and prefer Microsoft Entra authorization or narrowly scoped SAS tokens. Then, Scan evidence for secrets and verify data commands use login-based authorization where supported.

[Open the answer key](./ANSWERS.md)
