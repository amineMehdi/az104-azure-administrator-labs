# Lab 19 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB19-Q01 — D

**Question:** The endpoint comparison architecture note requires the private Storage connectivity evaluation environment to keep service traffic on the Azure backbone while using the service's public endpoint. Which statement defines the relevant endpoint comparison boundary?

- **A — Incorrect.** Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall.
  Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall. In the private Storage connectivity evaluation, this statement describes service endpoint authorization. Private Storage connectivity evaluation asks about service endpoint traffic; this service endpoint authorization choice leaves the service endpoint traffic explanation missing.
- **B — Incorrect.** Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP.
  Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP. In the private Storage connectivity evaluation, this statement describes private endpoint DNS zones. The private endpoint DNS zones statement accurately describes private endpoint DNS zones; however, private Storage connectivity evaluation needs service endpoint traffic to keep service traffic on the Azure backbone while using the service's public endpoint; private endpoint DNS zones cannot replace service endpoint traffic.
- **C — Incorrect.** Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity.
  Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity. In the private Storage connectivity evaluation, this statement describes public network access. Selecting public network access for private Storage connectivity evaluation leaves service endpoint traffic unanswered in private Storage connectivity evaluation; the private Storage connectivity evaluation lacks a service endpoint traffic basis to keep service traffic on the Azure backbone while using the service's public endpoint.
- **D — Correct.** A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address.
  A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address. This service endpoint traffic fact resolves the private Storage connectivity evaluation design question about how to keep service traffic on the Azure backbone while using the service's public endpoint.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q02 — D

**Question:** A new endpoint comparison operator must explain why the private Storage connectivity evaluation can authorize a selected subnet identity on a service firewall. Which explanation is accurate?

- **A — Incorrect.** A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions.
  A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions. In the private Storage connectivity evaluation, this statement describes selected-network firewalls. The selected-network firewalls statement accurately describes selected-network firewalls; however, private Storage connectivity evaluation needs service endpoint authorization to authorize a selected subnet identity on a service firewall; selected-network firewalls cannot replace service endpoint authorization.
- **B — Incorrect.** A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.
  A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records. In the private Storage connectivity evaluation, this statement describes private DNS zone groups. Selecting private DNS zone groups for private Storage connectivity evaluation leaves service endpoint authorization unanswered in private Storage connectivity evaluation; the private Storage connectivity evaluation lacks a service endpoint authorization basis to authorize a selected subnet identity on a service firewall.
- **C — Incorrect.** A private endpoint connection must reach Approved state before the service accepts traffic through it.
  A private endpoint connection must reach Approved state before the service accepts traffic through it. In the private Storage connectivity evaluation, this statement describes private endpoint approval. Service endpoint authorization governs private Storage connectivity evaluation; private endpoint approval cannot support service endpoint authorization when operators must authorize a selected subnet identity on a service firewall.
- **D — Correct.** Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall.
  Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall. For private Storage connectivity evaluation, service endpoint authorization supplies the service rule needed to authorize a selected subnet identity on a service firewall.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q03 — C

**Question:** The private Storage connectivity evaluation acceptance criteria require operators to deny service requests from networks that are not explicitly selected. Which service fact supports that requirement?

- **A — Incorrect.** A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource.
  A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource. In the private Storage connectivity evaluation, this statement describes private endpoint network interfaces. Selecting private endpoint network interfaces for private Storage connectivity evaluation leaves selected-network firewalls unanswered in private Storage connectivity evaluation; the private Storage connectivity evaluation lacks a selected-network firewalls basis to deny service requests from networks that are not explicitly selected.
- **B — Incorrect.** A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design.
  A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design. In the private Storage connectivity evaluation, this statement describes private DNS virtual-network links. Selected-network firewalls governs private Storage connectivity evaluation; private DNS virtual-network links cannot support selected-network firewalls when operators must deny service requests from networks that are not explicitly selected.
- **C — Correct.** A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions.
  A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions. In the private Storage connectivity evaluation, this selected-network firewalls rule supports the need to deny service requests from networks that are not explicitly selected.
- **D — Incorrect.** Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet.
  Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet. In the private Storage connectivity evaluation, this statement describes service endpoints versus private endpoints. The service endpoints versus private endpoints statement accurately describes service endpoints versus private endpoints; however, private Storage connectivity evaluation needs selected-network firewalls to deny service requests from networks that are not explicitly selected; service endpoints versus private endpoints cannot replace selected-network firewalls.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q04 — A

**Question:** An endpoint comparison reviewer challenges whether the private Storage connectivity evaluation can assign a private address from the consumer network to a platform service connection. Which response resolves the concern?

- **A — Correct.** A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource.
  For the private Storage connectivity evaluation, the rule for private endpoint network interfaces is defined by this statement: a private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource. It supports the required outcome to assign a private address from the consumer network to a platform service connection.
- **B — Incorrect.** Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP.
  Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP. In the private Storage connectivity evaluation, this statement describes private endpoint DNS zones. Private Storage connectivity evaluation asks about private endpoint network interfaces; this private endpoint DNS zones choice leaves the private endpoint network interfaces explanation missing.
- **C — Incorrect.** Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity.
  Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity. In the private Storage connectivity evaluation, this statement describes public network access. The public network access statement accurately describes public network access; however, private Storage connectivity evaluation needs private endpoint network interfaces to assign a private address from the consumer network to a platform service connection; public network access cannot replace private endpoint network interfaces.
- **D — Incorrect.** A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address.
  A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address. In the private Storage connectivity evaluation, this statement describes service endpoint traffic. Selecting service endpoint traffic for private Storage connectivity evaluation leaves private endpoint network interfaces unanswered in private Storage connectivity evaluation; the private Storage connectivity evaluation lacks a private endpoint network interfaces basis to assign a private address from the consumer network to a platform service connection.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q05 — C

**Question:** The private Storage connectivity evaluation handoff omits the endpoint comparison rule needed to resolve a service hostname to the connection's private address. Which statement should the team add?

- **A — Incorrect.** A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.
  A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records. In the private Storage connectivity evaluation, this statement describes private DNS zone groups. Private Storage connectivity evaluation asks about private endpoint DNS zones; this private DNS zone groups choice leaves the private endpoint DNS zones explanation missing.
- **B — Incorrect.** A private endpoint connection must reach Approved state before the service accepts traffic through it.
  A private endpoint connection must reach Approved state before the service accepts traffic through it. In the private Storage connectivity evaluation, this statement describes private endpoint approval. The private endpoint approval statement accurately describes private endpoint approval; however, private Storage connectivity evaluation needs private endpoint DNS zones to resolve a service hostname to the connection's private address; private endpoint approval cannot replace private endpoint DNS zones.
- **C — Correct.** Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP.
  Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP. The private Storage connectivity evaluation applies that private endpoint DNS zones boundary when operators must resolve a service hostname to the connection's private address.
- **D — Incorrect.** Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall.
  Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall. In the private Storage connectivity evaluation, this statement describes service endpoint authorization. Private endpoint DNS zones governs private Storage connectivity evaluation; service endpoint authorization cannot support private endpoint DNS zones when operators must resolve a service hostname to the connection's private address.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q06 — D

**Question:** An endpoint comparison incident review of the private Storage connectivity evaluation depends on the ability to create the endpoint-to-name-resolution association automatically. Which platform description is reliable?

- **A — Incorrect.** A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design.
  A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design. In the private Storage connectivity evaluation, this statement describes private DNS virtual-network links. The private DNS virtual-network links statement accurately describes private DNS virtual-network links; however, private Storage connectivity evaluation needs private DNS zone groups to create the endpoint-to-name-resolution association automatically; private DNS virtual-network links cannot replace private DNS zone groups.
- **B — Incorrect.** Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet.
  Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet. In the private Storage connectivity evaluation, this statement describes service endpoints versus private endpoints. Selecting service endpoints versus private endpoints for private Storage connectivity evaluation leaves private DNS zone groups unanswered in private Storage connectivity evaluation; the private Storage connectivity evaluation lacks a private DNS zone groups basis to create the endpoint-to-name-resolution association automatically.
- **C — Incorrect.** A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions.
  A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions. In the private Storage connectivity evaluation, this statement describes selected-network firewalls. Private DNS zone groups governs private Storage connectivity evaluation; selected-network firewalls cannot support private DNS zone groups when operators must create the endpoint-to-name-resolution association automatically.
- **D — Correct.** A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.
  The private Storage connectivity evaluation needs private DNS zone groups to create the endpoint-to-name-resolution association automatically; this option states the applicable private DNS zone groups rule: a private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q07 — A

**Question:** A network administrator comparing Storage service and private endpoints is updating the endpoint comparison runbook. The requirement is to make private records resolvable from the intended virtual network. Which statement describes Azure behavior correctly?

- **A — Correct.** A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design.
  A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design. This private DNS virtual-network links fact resolves the private Storage connectivity evaluation design question about how to make private records resolvable from the intended virtual network.
- **B — Incorrect.** Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity.
  Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity. In the private Storage connectivity evaluation, this statement describes public network access. Private DNS virtual-network links governs private Storage connectivity evaluation; public network access cannot support private DNS virtual-network links when operators must make private records resolvable from the intended virtual network.
- **C — Incorrect.** A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address.
  A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address. In the private Storage connectivity evaluation, this statement describes service endpoint traffic. Private Storage connectivity evaluation asks about private DNS virtual-network links; this service endpoint traffic choice leaves the private DNS virtual-network links explanation missing.
- **D — Incorrect.** A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource.
  A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource. In the private Storage connectivity evaluation, this statement describes private endpoint network interfaces. The private endpoint network interfaces statement accurately describes private endpoint network interfaces; however, private Storage connectivity evaluation needs private DNS virtual-network links to make private records resolvable from the intended virtual network; private endpoint network interfaces cannot replace private DNS virtual-network links.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Azure Private DNS zones](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone)

**Source reviewed:** 2026-08-31

## LAB19-Q08 — A

**Question:** An endpoint comparison peer review asks how the private Storage connectivity evaluation should handle this outcome: disable the service's public network path after private connectivity works. Which explanation is accurate?

- **A — Correct.** Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity.
  Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity. For private Storage connectivity evaluation, public network access supplies the service rule needed to disable the service's public network path after private connectivity works.
- **B — Incorrect.** A private endpoint connection must reach Approved state before the service accepts traffic through it.
  A private endpoint connection must reach Approved state before the service accepts traffic through it. In the private Storage connectivity evaluation, this statement describes private endpoint approval. Private Storage connectivity evaluation asks about public network access; this private endpoint approval choice leaves the public network access explanation missing.
- **C — Incorrect.** Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall.
  Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall. In the private Storage connectivity evaluation, this statement describes service endpoint authorization. The service endpoint authorization statement accurately describes service endpoint authorization; however, private Storage connectivity evaluation needs public network access to disable the service's public network path after private connectivity works; service endpoint authorization cannot replace public network access.
- **D — Incorrect.** Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP.
  Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP. In the private Storage connectivity evaluation, this statement describes private endpoint DNS zones. Selecting private endpoint DNS zones for private Storage connectivity evaluation leaves public network access unanswered in private Storage connectivity evaluation; the private Storage connectivity evaluation lacks a public network access basis to disable the service's public network path after private connectivity works.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q09 — D

**Question:** For the private Storage connectivity evaluation, the endpoint comparison plan must identify whether the provider accepted a pending private connection. Which statement about endpoint comparison belongs in the private Storage connectivity evaluation record?

- **A — Incorrect.** Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet.
  Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet. In the private Storage connectivity evaluation, this statement describes service endpoints versus private endpoints. Private Storage connectivity evaluation asks about private endpoint approval; this service endpoints versus private endpoints choice leaves the private endpoint approval explanation missing.
- **B — Incorrect.** A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions.
  A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions. In the private Storage connectivity evaluation, this statement describes selected-network firewalls. The selected-network firewalls statement accurately describes selected-network firewalls; however, private Storage connectivity evaluation needs private endpoint approval to identify whether the provider accepted a pending private connection; selected-network firewalls cannot replace private endpoint approval.
- **C — Incorrect.** A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.
  A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records. In the private Storage connectivity evaluation, this statement describes private DNS zone groups. Selecting private DNS zone groups for private Storage connectivity evaluation leaves private endpoint approval unanswered in private Storage connectivity evaluation; the private Storage connectivity evaluation lacks a private endpoint approval basis to identify whether the provider accepted a pending private connection.
- **D — Correct.** A private endpoint connection must reach Approved state before the service accepts traffic through it.
  A private endpoint connection must reach Approved state before the service accepts traffic through it. In the private Storage connectivity evaluation, this private endpoint approval rule supports the need to identify whether the provider accepted a pending private connection.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q10 — C

**Question:** The endpoint comparison review compares four claims for the private Storage connectivity evaluation requirement to choose between subnet authorization to a public endpoint and a private network interface. Which claim is technically sound?

- **A — Incorrect.** A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address.
  A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address. In the private Storage connectivity evaluation, this statement describes service endpoint traffic. The service endpoint traffic statement accurately describes service endpoint traffic; however, private Storage connectivity evaluation needs service endpoints versus private endpoints to choose between subnet authorization to a public endpoint and a private network interface; service endpoint traffic cannot replace service endpoints versus private endpoints.
- **B — Incorrect.** A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource.
  A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource. In the private Storage connectivity evaluation, this statement describes private endpoint network interfaces. Selecting private endpoint network interfaces for private Storage connectivity evaluation leaves service endpoints versus private endpoints unanswered in private Storage connectivity evaluation; the private Storage connectivity evaluation lacks a service endpoints versus private endpoints basis to choose between subnet authorization to a public endpoint and a private network interface.
- **C — Correct.** Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet.
  For the private Storage connectivity evaluation, the rule for service endpoints versus private endpoints is defined by this statement: service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet. It supports the required outcome to choose between subnet authorization to a public endpoint and a private network interface.
- **D — Incorrect.** A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design.
  A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design. In the private Storage connectivity evaluation, this statement describes private DNS virtual-network links. Private Storage connectivity evaluation asks about service endpoints versus private endpoints; this private DNS virtual-network links choice leaves the service endpoints versus private endpoints explanation missing.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q11 — B

**Question:** For the private Storage connectivity evaluation, operators need to keep service traffic on the Azure backbone while using the service's public endpoint. Which change realizes that requirement?

- **A — Incorrect.** Set default deny only after establishing an approved administrative and workload access path.
  Set default deny only after establishing an approved administrative and workload access path. In the private Storage connectivity evaluation, this action changes selected-network firewalls. Private Storage connectivity evaluation approved service endpoint traffic, not selected-network firewalls; only the service endpoint traffic change can keep service traffic on the Azure backbone while using the service's public endpoint.
- **B — Correct.** Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall.
  Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. This changes service endpoint traffic in the private Storage connectivity evaluation, supplying the missing state needed to keep service traffic on the Azure backbone while using the service's public endpoint.
- **C — Incorrect.** Attach the correct private DNS zone to the endpoint's zone group.
  Attach the correct private DNS zone to the endpoint's zone group. In the private Storage connectivity evaluation, this action changes private DNS zone groups. Private DNS zone groups does not implement service endpoint traffic for private Storage connectivity evaluation; the private Storage connectivity evaluation still cannot keep service traffic on the Azure backbone while using the service's public endpoint.
- **D — Incorrect.** Approve the pending connection only after confirming its requester, endpoint ID, and target subresource.
  Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. In the private Storage connectivity evaluation, this action changes private endpoint approval. Private Storage connectivity evaluation instead needs service endpoint traffic: Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. The private endpoint approval action omits that service endpoint traffic work.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q12 — D

**Question:** Operators must automate the private Storage connectivity evaluation change needed to authorize a selected subnet identity on a service firewall. Which endpoint comparison operation belongs in the runbook?

- **A — Incorrect.** Create the endpoint in the approved subnet and select the correct group ID for the service.
  Create the endpoint in the approved subnet and select the correct group ID for the service. In the private Storage connectivity evaluation, this action changes private endpoint network interfaces. Private Storage connectivity evaluation requires service endpoint authorization; changing private endpoint network interfaces leaves service endpoint authorization absent in private Storage connectivity evaluation; private Storage connectivity evaluation cannot authorize a selected subnet identity on a service firewall.
- **B — Incorrect.** Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration.
  Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. In the private Storage connectivity evaluation, this action changes private DNS virtual-network links. Private DNS virtual-network links does not implement service endpoint authorization for private Storage connectivity evaluation; the private Storage connectivity evaluation still cannot authorize a selected subnet identity on a service firewall.
- **C — Incorrect.** Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure.
  Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. In the private Storage connectivity evaluation, this action changes service endpoints versus private endpoints. Private Storage connectivity evaluation instead needs service endpoint authorization: Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. The service endpoints versus private endpoints action omits that service endpoint authorization work.
- **D — Correct.** Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.
  The private Storage connectivity evaluation must authorize a selected subnet identity on a service firewall; this option performs its direct service endpoint authorization change: add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q13 — D

**Question:** A private Storage connectivity evaluation review finds endpoint comparison drift from the need to deny service requests from networks that are not explicitly selected. Which correction addresses that drift?

- **A — Incorrect.** Create or reuse the service-specific private DNS zone and attach it through a zone group.
  Create or reuse the service-specific private DNS zone and attach it through a zone group. In the private Storage connectivity evaluation, this action changes private endpoint DNS zones. Private endpoint DNS zones does not implement selected-network firewalls for private Storage connectivity evaluation; the private Storage connectivity evaluation still cannot deny service requests from networks that are not explicitly selected.
- **B — Incorrect.** Validate private connectivity completely before disabling the public endpoint.
  Validate private connectivity completely before disabling the public endpoint. In the private Storage connectivity evaluation, this action changes public network access. Private Storage connectivity evaluation instead needs selected-network firewalls: Set default deny only after establishing an approved administrative and workload access path. The public network access action omits that selected-network firewalls work.
- **C — Incorrect.** Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall.
  Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. In the private Storage connectivity evaluation, this action changes service endpoint traffic. Private Storage connectivity evaluation approved selected-network firewalls, not service endpoint traffic; only the selected-network firewalls change can deny service requests from networks that are not explicitly selected.
- **D — Correct.** Set default deny only after establishing an approved administrative and workload access path.
  Set default deny only after establishing an approved administrative and workload access path. It is the least-change selected-network firewalls path for the private Storage connectivity evaluation requirement to deny service requests from networks that are not explicitly selected.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q14 — B

**Question:** The private Storage connectivity evaluation window permits only the endpoint comparison change needed to assign a private address from the consumer network to a platform service connection. Which option respects the boundary?

- **A — Incorrect.** Attach the correct private DNS zone to the endpoint's zone group.
  Attach the correct private DNS zone to the endpoint's zone group. In the private Storage connectivity evaluation, this action changes private DNS zone groups. Private Storage connectivity evaluation instead needs private endpoint network interfaces: Create the endpoint in the approved subnet and select the correct group ID for the service. The private DNS zone groups action omits that private endpoint network interfaces work.
- **B — Correct.** Create the endpoint in the approved subnet and select the correct group ID for the service.
  Create the endpoint in the approved subnet and select the correct group ID for the service. In private Storage connectivity evaluation, applying private endpoint network interfaces is the scoped way to assign a private address from the consumer network to a platform service connection.
- **C — Incorrect.** Approve the pending connection only after confirming its requester, endpoint ID, and target subresource.
  Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. In the private Storage connectivity evaluation, this action changes private endpoint approval. Private Storage connectivity evaluation requires private endpoint network interfaces; changing private endpoint approval leaves private endpoint network interfaces absent in private Storage connectivity evaluation; private Storage connectivity evaluation cannot assign a private address from the consumer network to a platform service connection.
- **D — Incorrect.** Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.
  Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. In the private Storage connectivity evaluation, this action changes service endpoint authorization. Service endpoint authorization does not implement private endpoint network interfaces for private Storage connectivity evaluation; the private Storage connectivity evaluation still cannot assign a private address from the consumer network to a platform service connection.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q15 — D

**Question:** The endpoint comparison preflight has passed; the private Storage connectivity evaluation must now resolve a service hostname to the connection's private address. Which operation should run?

- **A — Incorrect.** Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration.
  Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. In the private Storage connectivity evaluation, this action changes private DNS virtual-network links. Private Storage connectivity evaluation approved private endpoint DNS zones, not private DNS virtual-network links; only the private endpoint DNS zones change can resolve a service hostname to the connection's private address.
- **B — Incorrect.** Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure.
  Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. In the private Storage connectivity evaluation, this action changes service endpoints versus private endpoints. Private Storage connectivity evaluation requires private endpoint DNS zones; changing service endpoints versus private endpoints leaves private endpoint DNS zones absent in private Storage connectivity evaluation; private Storage connectivity evaluation cannot resolve a service hostname to the connection's private address.
- **C — Incorrect.** Set default deny only after establishing an approved administrative and workload access path.
  Set default deny only after establishing an approved administrative and workload access path. In the private Storage connectivity evaluation, this action changes selected-network firewalls. Selected-network firewalls does not implement private endpoint DNS zones for private Storage connectivity evaluation; the private Storage connectivity evaluation still cannot resolve a service hostname to the connection's private address.
- **D — Correct.** Create or reuse the service-specific private DNS zone and attach it through a zone group.
  Create or reuse the service-specific private DNS zone and attach it through a zone group. The private Storage connectivity evaluation uses this private endpoint DNS zones operation to resolve a service hostname to the connection's private address within the approved scope.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q16 — A

**Question:** The private Storage connectivity evaluation plan must create the endpoint-to-name-resolution association automatically while limiting the mutation scope to endpoint comparison. Which action is appropriate?

- **A — Correct.** Attach the correct private DNS zone to the endpoint's zone group.
  For the private Storage connectivity evaluation, the required private DNS zone groups action is: attach the correct private DNS zone to the endpoint's zone group. It makes the environment able to create the endpoint-to-name-resolution association automatically.
- **B — Incorrect.** Validate private connectivity completely before disabling the public endpoint.
  Validate private connectivity completely before disabling the public endpoint. In the private Storage connectivity evaluation, this action changes public network access. Public network access does not implement private DNS zone groups for private Storage connectivity evaluation; the private Storage connectivity evaluation still cannot create the endpoint-to-name-resolution association automatically.
- **C — Incorrect.** Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall.
  Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. In the private Storage connectivity evaluation, this action changes service endpoint traffic. Private Storage connectivity evaluation instead needs private DNS zone groups: Attach the correct private DNS zone to the endpoint's zone group. The service endpoint traffic action omits that private DNS zone groups work.
- **D — Incorrect.** Create the endpoint in the approved subnet and select the correct group ID for the service.
  Create the endpoint in the approved subnet and select the correct group ID for the service. In the private Storage connectivity evaluation, this action changes private endpoint network interfaces. Private Storage connectivity evaluation approved private DNS zone groups, not private endpoint network interfaces; only the private DNS zone groups change can create the endpoint-to-name-resolution association automatically.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q17 — B

**Question:** An endpoint comparison ticket in the private Storage connectivity evaluation says to make private records resolvable from the intended virtual network. Which endpoint comparison action completes the private Storage connectivity evaluation request with minimal change?

- **A — Incorrect.** Approve the pending connection only after confirming its requester, endpoint ID, and target subresource.
  Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. In the private Storage connectivity evaluation, this action changes private endpoint approval. Private endpoint approval does not implement private DNS virtual-network links for private Storage connectivity evaluation; the private Storage connectivity evaluation still cannot make private records resolvable from the intended virtual network.
- **B — Correct.** Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration.
  Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. This changes private DNS virtual-network links in the private Storage connectivity evaluation, supplying the missing state needed to make private records resolvable from the intended virtual network.
- **C — Incorrect.** Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.
  Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. In the private Storage connectivity evaluation, this action changes service endpoint authorization. Private Storage connectivity evaluation approved private DNS virtual-network links, not service endpoint authorization; only the private DNS virtual-network links change can make private records resolvable from the intended virtual network.
- **D — Incorrect.** Create or reuse the service-specific private DNS zone and attach it through a zone group.
  Create or reuse the service-specific private DNS zone and attach it through a zone group. In the private Storage connectivity evaluation, this action changes private endpoint DNS zones. Private Storage connectivity evaluation requires private DNS virtual-network links; changing private endpoint DNS zones leaves private DNS virtual-network links absent in private Storage connectivity evaluation; private Storage connectivity evaluation cannot make private records resolvable from the intended virtual network.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Azure Private DNS zones](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone)

**Source reviewed:** 2026-08-31

## LAB19-Q18 — D

**Question:** The approach for the private Storage connectivity evaluation is approved, but the endpoint comparison environment still cannot disable the service's public network path after private connectivity works. Which implementation step closes the gap?

- **A — Incorrect.** Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure.
  Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. In the private Storage connectivity evaluation, this action changes service endpoints versus private endpoints. Private Storage connectivity evaluation instead needs public network access: Validate private connectivity completely before disabling the public endpoint. The service endpoints versus private endpoints action omits that public network access work.
- **B — Incorrect.** Set default deny only after establishing an approved administrative and workload access path.
  Set default deny only after establishing an approved administrative and workload access path. In the private Storage connectivity evaluation, this action changes selected-network firewalls. Private Storage connectivity evaluation approved public network access, not selected-network firewalls; only the public network access change can disable the service's public network path after private connectivity works.
- **C — Incorrect.** Attach the correct private DNS zone to the endpoint's zone group.
  Attach the correct private DNS zone to the endpoint's zone group. In the private Storage connectivity evaluation, this action changes private DNS zone groups. Private Storage connectivity evaluation requires public network access; changing private DNS zone groups leaves public network access absent in private Storage connectivity evaluation; private Storage connectivity evaluation cannot disable the service's public network path after private connectivity works.
- **D — Correct.** Validate private connectivity completely before disabling the public endpoint.
  The private Storage connectivity evaluation must disable the service's public network path after private connectivity works; this option performs its direct public network access change: validate private connectivity completely before disabling the public endpoint.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q19 — C

**Question:** The network administrator comparing Storage service and private endpoints may change the private Storage connectivity evaluation only to identify whether the provider accepted a pending private connection. Which endpoint comparison action stays within that assignment?

- **A — Incorrect.** Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall.
  Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. In the private Storage connectivity evaluation, this action changes service endpoint traffic. Private Storage connectivity evaluation approved private endpoint approval, not service endpoint traffic; only the private endpoint approval change can identify whether the provider accepted a pending private connection.
- **B — Incorrect.** Create the endpoint in the approved subnet and select the correct group ID for the service.
  Create the endpoint in the approved subnet and select the correct group ID for the service. In the private Storage connectivity evaluation, this action changes private endpoint network interfaces. Private Storage connectivity evaluation requires private endpoint approval; changing private endpoint network interfaces leaves private endpoint approval absent in private Storage connectivity evaluation; private Storage connectivity evaluation cannot identify whether the provider accepted a pending private connection.
- **C — Correct.** Approve the pending connection only after confirming its requester, endpoint ID, and target subresource.
  Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. It is the least-change private endpoint approval path for the private Storage connectivity evaluation requirement to identify whether the provider accepted a pending private connection.
- **D — Incorrect.** Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration.
  Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. In the private Storage connectivity evaluation, this action changes private DNS virtual-network links. Private Storage connectivity evaluation instead needs private endpoint approval: Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. The private DNS virtual-network links action omits that private endpoint approval work.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q20 — B

**Question:** An endpoint comparison dry run shows no private Storage connectivity evaluation command will choose between subnet authorization to a public endpoint and a private network interface. Which action belongs before execution?

- **A — Incorrect.** Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.
  Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. In the private Storage connectivity evaluation, this action changes service endpoint authorization. Private Storage connectivity evaluation requires service endpoints versus private endpoints; changing service endpoint authorization leaves service endpoints versus private endpoints absent in private Storage connectivity evaluation; private Storage connectivity evaluation cannot choose between subnet authorization to a public endpoint and a private network interface.
- **B — Correct.** Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure.
  Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. In private Storage connectivity evaluation, applying service endpoints versus private endpoints is the scoped way to choose between subnet authorization to a public endpoint and a private network interface.
- **C — Incorrect.** Create or reuse the service-specific private DNS zone and attach it through a zone group.
  Create or reuse the service-specific private DNS zone and attach it through a zone group. In the private Storage connectivity evaluation, this action changes private endpoint DNS zones. Private Storage connectivity evaluation instead needs service endpoints versus private endpoints: Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. The private endpoint DNS zones action omits that service endpoints versus private endpoints work.
- **D — Incorrect.** Validate private connectivity completely before disabling the public endpoint.
  Validate private connectivity completely before disabling the public endpoint. In the private Storage connectivity evaluation, this action changes public network access. Private Storage connectivity evaluation approved service endpoints versus private endpoints, not public network access; only the service endpoints versus private endpoints change can choose between subnet authorization to a public endpoint and a private network interface.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q21 — A

**Question:** The network administrator comparing Storage service and private endpoints must confirm the private Storage connectivity evaluation, without mutation, can keep service traffic on the Azure backbone while using the service's public endpoint. Which endpoint comparison check qualifies?

- **A — Correct.** Query subnet serviceEndpoints and the service's virtual network rules.
  Query subnet serviceEndpoints and the service's virtual network rules. The private Storage connectivity evaluation reads service endpoint traffic directly; that service endpoint traffic result proves the private Storage connectivity evaluation can keep service traffic on the Azure backbone while using the service's public endpoint without another mutation.
- **B — Incorrect.** Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
  Query the endpoint NIC private IP, groupIds, subnet ID, and connection state. In the private Storage connectivity evaluation, this check observes private endpoint network interfaces. Private endpoint network interfaces success in private Storage connectivity evaluation cannot verify service endpoint traffic; private Storage connectivity evaluation cannot keep service traffic on the Azure backbone while using the service's public endpoint until service endpoint traffic evidence exists.
- **C — Incorrect.** List virtualNetworkLinks and test resolution from each intended client network.
  List virtualNetworkLinks and test resolution from each intended client network. In the private Storage connectivity evaluation, this check observes private DNS virtual-network links. Private Storage connectivity evaluation reads private DNS virtual-network links, leaving service endpoint traffic unproved in private Storage connectivity evaluation; private Storage connectivity evaluation still has no service endpoint traffic proof.
- **D — Incorrect.** Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
  Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination. In the private Storage connectivity evaluation, this check observes service endpoints versus private endpoints. Private Storage connectivity evaluation could pass service endpoints versus private endpoints while service endpoint traffic is wrong; private Storage connectivity evaluation still lacks service endpoint traffic proof.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q22 — D

**Question:** The private Storage connectivity evaluation configuration is complete; the endpoint comparison reviewers need evidence it can authorize a selected subnet identity on a service firewall. Which observation shows success?

- **A — Incorrect.** Resolve the normal service hostname inside the VNet and confirm the final private address.
  Resolve the normal service hostname inside the VNet and confirm the final private address. In the private Storage connectivity evaluation, this check observes private endpoint DNS zones. Private endpoint DNS zones success in private Storage connectivity evaluation cannot verify service endpoint authorization; private Storage connectivity evaluation cannot authorize a selected subnet identity on a service firewall until service endpoint authorization evidence exists.
- **B — Incorrect.** Query publicNetworkAccess and perform positive private and negative public-path tests.
  Query publicNetworkAccess and perform positive private and negative public-path tests. In the private Storage connectivity evaluation, this check observes public network access. Private Storage connectivity evaluation reads public network access, leaving service endpoint authorization unproved in private Storage connectivity evaluation; private Storage connectivity evaluation still has no service endpoint authorization proof.
- **C — Incorrect.** Query subnet serviceEndpoints and the service's virtual network rules.
  Query subnet serviceEndpoints and the service's virtual network rules. In the private Storage connectivity evaluation, this check observes service endpoint traffic. Private Storage connectivity evaluation could pass service endpoint traffic while service endpoint authorization is wrong; private Storage connectivity evaluation still lacks service endpoint authorization proof.
- **D — Correct.** Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
  For the private Storage connectivity evaluation, this service endpoint authorization observation is decisive: verify endpoint state, firewall rule, and data-plane authorization as separate controls. It is private Storage connectivity evaluation evidence that operators can authorize a selected subnet identity on a service firewall.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q23 — B

**Question:** The endpoint comparison validation asks whether the private Storage connectivity evaluation can deny service requests from networks that are not explicitly selected. Which observable state is strongest?

- **A — Incorrect.** Query the zone group and match its privateDnsZoneConfigs and generated record IP.
  Query the zone group and match its privateDnsZoneConfigs and generated record IP. In the private Storage connectivity evaluation, this check observes private DNS zone groups. Private Storage connectivity evaluation reads private DNS zone groups, leaving selected-network firewalls unproved in private Storage connectivity evaluation; private Storage connectivity evaluation still has no selected-network firewalls proof.
- **B — Correct.** Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
  Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections. Because the private Storage connectivity evaluation check observes selected-network firewalls, it independently verifies the requirement to deny service requests from networks that are not explicitly selected.
- **C — Incorrect.** Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
  Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs. In the private Storage connectivity evaluation, this check observes private endpoint approval. Private Storage connectivity evaluation output covers private endpoint approval, not selected-network firewalls; the selected-network firewalls requirement to deny service requests from networks that are not explicitly selected remains unverified.
- **D — Incorrect.** Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
  Verify endpoint state, firewall rule, and data-plane authorization as separate controls. In the private Storage connectivity evaluation, this check observes service endpoint authorization. Service endpoint authorization success in private Storage connectivity evaluation cannot verify selected-network firewalls; private Storage connectivity evaluation cannot deny service requests from networks that are not explicitly selected until selected-network firewalls evidence exists.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q24 — B

**Question:** A private Storage connectivity evaluation review must prove the endpoint comparison ability to assign a private address from the consumer network to a platform service connection. Which check avoids an adjacent feature?

- **A — Incorrect.** List virtualNetworkLinks and test resolution from each intended client network.
  List virtualNetworkLinks and test resolution from each intended client network. In the private Storage connectivity evaluation, this check observes private DNS virtual-network links. Private Storage connectivity evaluation could pass private DNS virtual-network links while private endpoint network interfaces is wrong; private Storage connectivity evaluation still lacks private endpoint network interfaces proof.
- **B — Correct.** Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
  The private Storage connectivity evaluation validator needs this private endpoint network interfaces result: query the endpoint NIC private IP, groupIds, subnet ID, and connection state. It proves the outcome to assign a private address from the consumer network to a platform service connection rather than an adjacent checkpoint.
- **C — Incorrect.** Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
  Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination. In the private Storage connectivity evaluation, this check observes service endpoints versus private endpoints. Service endpoints versus private endpoints success in private Storage connectivity evaluation cannot verify private endpoint network interfaces; private Storage connectivity evaluation cannot assign a private address from the consumer network to a platform service connection until private endpoint network interfaces evidence exists.
- **D — Incorrect.** Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
  Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections. In the private Storage connectivity evaluation, this check observes selected-network firewalls. Private Storage connectivity evaluation reads selected-network firewalls, leaving private endpoint network interfaces unproved in private Storage connectivity evaluation; private Storage connectivity evaluation still has no private endpoint network interfaces proof.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q25 — C

**Question:** The private Storage connectivity evaluation evidence bundle needs an endpoint comparison result showing it can resolve a service hostname to the connection's private address. Which result belongs in the checkpoint?

- **A — Incorrect.** Query publicNetworkAccess and perform positive private and negative public-path tests.
  Query publicNetworkAccess and perform positive private and negative public-path tests. In the private Storage connectivity evaluation, this check observes public network access. Private Storage connectivity evaluation output covers public network access, not private endpoint DNS zones; the private endpoint DNS zones requirement to resolve a service hostname to the connection's private address remains unverified.
- **B — Incorrect.** Query subnet serviceEndpoints and the service's virtual network rules.
  Query subnet serviceEndpoints and the service's virtual network rules. In the private Storage connectivity evaluation, this check observes service endpoint traffic. Service endpoint traffic success in private Storage connectivity evaluation cannot verify private endpoint DNS zones; private Storage connectivity evaluation cannot resolve a service hostname to the connection's private address until private endpoint DNS zones evidence exists.
- **C — Correct.** Resolve the normal service hostname inside the VNet and confirm the final private address.
  Resolve the normal service hostname inside the VNet and confirm the final private address. This is independent private endpoint DNS zones evidence for the private Storage connectivity evaluation, even if private Storage connectivity evaluation setup reports success before private endpoint DNS zones becomes observable.
- **D — Incorrect.** Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
  Query the endpoint NIC private IP, groupIds, subnet ID, and connection state. In the private Storage connectivity evaluation, this check observes private endpoint network interfaces. Private Storage connectivity evaluation could pass private endpoint network interfaces while private endpoint DNS zones is wrong; private Storage connectivity evaluation still lacks private endpoint DNS zones proof.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q26 — B

**Question:** Before private Storage connectivity evaluation cleanup, the endpoint comparison team must reconfirm it can create the endpoint-to-name-resolution association automatically. Which read-only inspection should run?

- **A — Incorrect.** Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
  Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs. In the private Storage connectivity evaluation, this check observes private endpoint approval. Private endpoint approval success in private Storage connectivity evaluation cannot verify private DNS zone groups; private Storage connectivity evaluation cannot create the endpoint-to-name-resolution association automatically until private DNS zone groups evidence exists.
- **B — Correct.** Query the zone group and match its privateDnsZoneConfigs and generated record IP.
  Query the zone group and match its privateDnsZoneConfigs and generated record IP. For private Storage connectivity evaluation, this private DNS zone groups read confirms the service can create the endpoint-to-name-resolution association automatically.
- **C — Incorrect.** Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
  Verify endpoint state, firewall rule, and data-plane authorization as separate controls. In the private Storage connectivity evaluation, this check observes service endpoint authorization. Private Storage connectivity evaluation could pass service endpoint authorization while private DNS zone groups is wrong; private Storage connectivity evaluation still lacks private DNS zone groups proof.
- **D — Incorrect.** Resolve the normal service hostname inside the VNet and confirm the final private address.
  Resolve the normal service hostname inside the VNet and confirm the final private address. In the private Storage connectivity evaluation, this check observes private endpoint DNS zones. Private Storage connectivity evaluation output covers private endpoint DNS zones, not private DNS zone groups; the private DNS zone groups requirement to create the endpoint-to-name-resolution association automatically remains unverified.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q27 — A

**Question:** The private Storage connectivity evaluation setup reports success after the endpoint comparison attempt to make private records resolvable from the intended virtual network. Which endpoint comparison read-only observation proves the private Storage connectivity evaluation outcome?

- **A — Correct.** List virtualNetworkLinks and test resolution from each intended client network.
  List virtualNetworkLinks and test resolution from each intended client network. The private Storage connectivity evaluation reads private DNS virtual-network links directly; that private DNS virtual-network links result proves the private Storage connectivity evaluation can make private records resolvable from the intended virtual network without another mutation.
- **B — Incorrect.** Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
  Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination. In the private Storage connectivity evaluation, this check observes service endpoints versus private endpoints. Private Storage connectivity evaluation could pass service endpoints versus private endpoints while private DNS virtual-network links is wrong; private Storage connectivity evaluation still lacks private DNS virtual-network links proof.
- **C — Incorrect.** Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
  Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections. In the private Storage connectivity evaluation, this check observes selected-network firewalls. Private Storage connectivity evaluation output covers selected-network firewalls, not private DNS virtual-network links; the private DNS virtual-network links requirement to make private records resolvable from the intended virtual network remains unverified.
- **D — Incorrect.** Query the zone group and match its privateDnsZoneConfigs and generated record IP.
  Query the zone group and match its privateDnsZoneConfigs and generated record IP. In the private Storage connectivity evaluation, this check observes private DNS zone groups. Private DNS zone groups success in private Storage connectivity evaluation cannot verify private DNS virtual-network links; private Storage connectivity evaluation cannot make private records resolvable from the intended virtual network until private DNS virtual-network links evidence exists.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Azure Private DNS zones](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone)

**Source reviewed:** 2026-08-31

## LAB19-Q28 — B

**Question:** The endpoint comparison log says the private Storage connectivity evaluation can now disable the service's public network path after private connectivity works. Which endpoint comparison state should the private Storage connectivity evaluation acceptance test retain?

- **A — Incorrect.** Query subnet serviceEndpoints and the service's virtual network rules.
  Query subnet serviceEndpoints and the service's virtual network rules. In the private Storage connectivity evaluation, this check observes service endpoint traffic. Private Storage connectivity evaluation could pass service endpoint traffic while public network access is wrong; private Storage connectivity evaluation still lacks public network access proof.
- **B — Correct.** Query publicNetworkAccess and perform positive private and negative public-path tests.
  For the private Storage connectivity evaluation, this public network access observation is decisive: query publicNetworkAccess and perform positive private and negative public-path tests. It is private Storage connectivity evaluation evidence that operators can disable the service's public network path after private connectivity works.
- **C — Incorrect.** Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
  Query the endpoint NIC private IP, groupIds, subnet ID, and connection state. In the private Storage connectivity evaluation, this check observes private endpoint network interfaces. Private endpoint network interfaces success in private Storage connectivity evaluation cannot verify public network access; private Storage connectivity evaluation cannot disable the service's public network path after private connectivity works until public network access evidence exists.
- **D — Incorrect.** List virtualNetworkLinks and test resolution from each intended client network.
  List virtualNetworkLinks and test resolution from each intended client network. In the private Storage connectivity evaluation, this check observes private DNS virtual-network links. Private Storage connectivity evaluation reads private DNS virtual-network links, leaving public network access unproved in private Storage connectivity evaluation; private Storage connectivity evaluation still has no public network access proof.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q29 — D

**Question:** The private Storage connectivity evaluation rejects endpoint comparison exit status as proof it can identify whether the provider accepted a pending private connection. Which private Storage connectivity evaluation result is valid evidence?

- **A — Incorrect.** Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
  Verify endpoint state, firewall rule, and data-plane authorization as separate controls. In the private Storage connectivity evaluation, this check observes service endpoint authorization. Private Storage connectivity evaluation output covers service endpoint authorization, not private endpoint approval; the private endpoint approval requirement to identify whether the provider accepted a pending private connection remains unverified.
- **B — Incorrect.** Resolve the normal service hostname inside the VNet and confirm the final private address.
  Resolve the normal service hostname inside the VNet and confirm the final private address. In the private Storage connectivity evaluation, this check observes private endpoint DNS zones. Private endpoint DNS zones success in private Storage connectivity evaluation cannot verify private endpoint approval; private Storage connectivity evaluation cannot identify whether the provider accepted a pending private connection until private endpoint approval evidence exists.
- **C — Incorrect.** Query publicNetworkAccess and perform positive private and negative public-path tests.
  Query publicNetworkAccess and perform positive private and negative public-path tests. In the private Storage connectivity evaluation, this check observes public network access. Private Storage connectivity evaluation reads public network access, leaving private endpoint approval unproved in private Storage connectivity evaluation; private Storage connectivity evaluation still has no private endpoint approval proof.
- **D — Correct.** Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
  Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs. Because the private Storage connectivity evaluation check observes private endpoint approval, it independently verifies the requirement to identify whether the provider accepted a pending private connection.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q30 — C

**Question:** The endpoint comparison validator needs one private Storage connectivity evaluation query after the change to choose between subnet authorization to a public endpoint and a private network interface. Which endpoint comparison property should the private Storage connectivity evaluation validator inspect?

- **A — Incorrect.** Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
  Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections. In the private Storage connectivity evaluation, this check observes selected-network firewalls. Selected-network firewalls success in private Storage connectivity evaluation cannot verify service endpoints versus private endpoints; private Storage connectivity evaluation cannot choose between subnet authorization to a public endpoint and a private network interface until service endpoints versus private endpoints evidence exists.
- **B — Incorrect.** Query the zone group and match its privateDnsZoneConfigs and generated record IP.
  Query the zone group and match its privateDnsZoneConfigs and generated record IP. In the private Storage connectivity evaluation, this check observes private DNS zone groups. Private Storage connectivity evaluation reads private DNS zone groups, leaving service endpoints versus private endpoints unproved in private Storage connectivity evaluation; private Storage connectivity evaluation still has no service endpoints versus private endpoints proof.
- **C — Correct.** Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
  The private Storage connectivity evaluation validator needs this service endpoints versus private endpoints result: inspect endpoint type, destination DNS answer, firewall configuration, and packet destination. It proves the outcome to choose between subnet authorization to a public endpoint and a private network interface rather than an adjacent checkpoint.
- **D — Incorrect.** Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
  Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs. In the private Storage connectivity evaluation, this check observes private endpoint approval. Private Storage connectivity evaluation output covers private endpoint approval, not service endpoints versus private endpoints; the service endpoints versus private endpoints requirement to choose between subnet authorization to a public endpoint and a private network interface remains unverified.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q31 — A

**Question:** The private Storage connectivity evaluation result is partial because the endpoint comparison cannot keep service traffic on the Azure backbone while using the service's public endpoint. Which condition accounts for that result?

- **A — Correct.** The design expects a service endpoint to allocate a private IP address in the subnet.
  The design expects a service endpoint to allocate a private IP address in the subnet. Removing this service endpoint traffic condition lets the private Storage connectivity evaluation keep service traffic on the Azure backbone while using the service's public endpoint while leaving healthy controls unchanged.
- **B — Incorrect.** The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule.
  The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule. The private Storage connectivity evaluation fault concerns service endpoint authorization. Private Storage connectivity evaluation could repair service endpoint authorization while service endpoint traffic stays broken in private Storage connectivity evaluation; the private Storage connectivity evaluation remains unable to keep service traffic on the Azure backbone while using the service's public endpoint.
- **C — Incorrect.** The zone group references a private DNS zone for a different service subresource.
  The zone group references a private DNS zone for a different service subresource. The private Storage connectivity evaluation fault concerns private DNS zone groups. Private Storage connectivity evaluation failed on service endpoint traffic; this private DNS zone groups finding redirects private Storage connectivity evaluation remediation away from service endpoint traffic.
- **D — Incorrect.** The design selects a service endpoint even though clients require a private IP reachable from on-premises.
  The design selects a service endpoint even though clients require a private IP reachable from on-premises. The private Storage connectivity evaluation fault concerns service endpoints versus private endpoints. Private Storage connectivity evaluation may fix service endpoints versus private endpoints, yet service endpoint traffic still fails; this private Storage connectivity evaluation diagnosis of service endpoints versus private endpoints is wrong for service endpoint traffic.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q32 — B

**Question:** The endpoint comparison evidence shows the private Storage connectivity evaluation cannot authorize a selected subnet identity on a service firewall. Which root cause fits that evidence?

- **A — Incorrect.** The public firewall changed to deny before the deployment host had an allowed path.
  The public firewall changed to deny before the deployment host had an allowed path. The private Storage connectivity evaluation fault concerns selected-network firewalls. Private Storage connectivity evaluation could repair selected-network firewalls while service endpoint authorization stays broken in private Storage connectivity evaluation; the private Storage connectivity evaluation remains unable to authorize a selected subnet identity on a service firewall.
- **B — Correct.** The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule.
  The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule. In private Storage connectivity evaluation, this service endpoint authorization cause matches the failure to authorize a selected subnet identity on a service firewall.
- **C — Incorrect.** The zone is linked only to the endpoint VNet, not to the separate client VNet.
  The zone is linked only to the endpoint VNet, not to the separate client VNet. The private Storage connectivity evaluation fault concerns private DNS virtual-network links. Private Storage connectivity evaluation may fix private DNS virtual-network links, yet service endpoint authorization still fails; this private Storage connectivity evaluation diagnosis of private DNS virtual-network links is wrong for service endpoint authorization.
- **D — Incorrect.** The design expects a service endpoint to allocate a private IP address in the subnet.
  The design expects a service endpoint to allocate a private IP address in the subnet. The private Storage connectivity evaluation fault concerns service endpoint traffic. Private Storage connectivity evaluation has service endpoint traffic impact, but service endpoint authorization is the private Storage connectivity evaluation failed path; the service endpoint traffic state cannot produce service endpoint authorization failure.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q33 — C

**Question:** Although the private Storage connectivity evaluation is meant to let the endpoint comparison deny service requests from networks that are not explicitly selected, its checkpoint fails. Which endpoint comparison defect explains the failure?

- **A — Incorrect.** The endpoint targets the blob subresource while the client accesses the file endpoint.
  The endpoint targets the blob subresource while the client accesses the file endpoint. The private Storage connectivity evaluation fault concerns private endpoint network interfaces. Private Storage connectivity evaluation failed on selected-network firewalls; this private endpoint network interfaces finding redirects private Storage connectivity evaluation remediation away from selected-network firewalls.
- **B — Incorrect.** Public access was disabled before the private DNS record propagated to clients.
  Public access was disabled before the private DNS record propagated to clients. The private Storage connectivity evaluation fault concerns public network access. Private Storage connectivity evaluation may fix public network access, yet selected-network firewalls still fails; this private Storage connectivity evaluation diagnosis of public network access is wrong for selected-network firewalls.
- **C — Correct.** The public firewall changed to deny before the deployment host had an allowed path.
  The public firewall changed to deny before the deployment host had an allowed path. This private Storage connectivity evaluation condition breaks selected-network firewalls, explaining why operators cannot deny service requests from networks that are not explicitly selected.
- **D — Incorrect.** The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule.
  The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule. The private Storage connectivity evaluation fault concerns service endpoint authorization. Private Storage connectivity evaluation could repair service endpoint authorization while selected-network firewalls stays broken in private Storage connectivity evaluation; the private Storage connectivity evaluation remains unable to deny service requests from networks that are not explicitly selected.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q34 — B

**Question:** The endpoint comparison support team isolated the private Storage connectivity evaluation incident to the attempt to assign a private address from the consumer network to a platform service connection. Which condition prevents success?

- **A — Incorrect.** No matching privatelink private DNS zone is available to the client resolver.
  No matching privatelink private DNS zone is available to the client resolver. The private Storage connectivity evaluation fault concerns private endpoint DNS zones. Private Storage connectivity evaluation may fix private endpoint DNS zones, yet private endpoint network interfaces still fails; this private Storage connectivity evaluation diagnosis of private endpoint DNS zones is wrong for private endpoint network interfaces.
- **B — Correct.** The endpoint targets the blob subresource while the client accesses the file endpoint.
  For the private Storage connectivity evaluation, the private endpoint network interfaces failure is causal: the endpoint targets the blob subresource while the client accesses the file endpoint. Correcting it restores the ability to assign a private address from the consumer network to a platform service connection.
- **C — Incorrect.** The connection remains Pending because the service owner has not approved it.
  The connection remains Pending because the service owner has not approved it. The private Storage connectivity evaluation fault concerns private endpoint approval. Private Storage connectivity evaluation could repair private endpoint approval while private endpoint network interfaces stays broken in private Storage connectivity evaluation; the private Storage connectivity evaluation remains unable to assign a private address from the consumer network to a platform service connection.
- **D — Incorrect.** The public firewall changed to deny before the deployment host had an allowed path.
  The public firewall changed to deny before the deployment host had an allowed path. The private Storage connectivity evaluation fault concerns selected-network firewalls. Private Storage connectivity evaluation failed on private endpoint network interfaces; this selected-network firewalls finding redirects private Storage connectivity evaluation remediation away from private endpoint network interfaces.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q35 — A

**Question:** A private Storage connectivity evaluation query surprises the network administrator comparing Storage service and private endpoints during the endpoint comparison attempt to resolve a service hostname to the connection's private address. Which finding explains it?

- **A — Correct.** No matching privatelink private DNS zone is available to the client resolver.
  No matching privatelink private DNS zone is available to the client resolver. The finding is specific to private endpoint DNS zones in the private Storage connectivity evaluation; repairing private endpoint DNS zones restores the private Storage connectivity evaluation ability to resolve a service hostname to the connection's private address.
- **B — Incorrect.** The zone group references a private DNS zone for a different service subresource.
  The zone group references a private DNS zone for a different service subresource. The private Storage connectivity evaluation fault concerns private DNS zone groups. Private Storage connectivity evaluation could repair private DNS zone groups while private endpoint DNS zones stays broken in private Storage connectivity evaluation; the private Storage connectivity evaluation remains unable to resolve a service hostname to the connection's private address.
- **C — Incorrect.** The design selects a service endpoint even though clients require a private IP reachable from on-premises.
  The design selects a service endpoint even though clients require a private IP reachable from on-premises. The private Storage connectivity evaluation fault concerns service endpoints versus private endpoints. Private Storage connectivity evaluation failed on private endpoint DNS zones; this service endpoints versus private endpoints finding redirects private Storage connectivity evaluation remediation away from private endpoint DNS zones.
- **D — Incorrect.** The endpoint targets the blob subresource while the client accesses the file endpoint.
  The endpoint targets the blob subresource while the client accesses the file endpoint. The private Storage connectivity evaluation fault concerns private endpoint network interfaces. Private Storage connectivity evaluation may fix private endpoint network interfaces, yet private endpoint DNS zones still fails; this private Storage connectivity evaluation diagnosis of private endpoint network interfaces is wrong for private endpoint DNS zones.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q36 — A

**Question:** Other private Storage connectivity evaluation components are healthy, but the endpoint comparison still cannot create the endpoint-to-name-resolution association automatically. Which state causes the isolated failure?

- **A — Correct.** The zone group references a private DNS zone for a different service subresource.
  The private Storage connectivity evaluation cannot create the endpoint-to-name-resolution association automatically because of this private DNS zone groups defect: the zone group references a private DNS zone for a different service subresource. The symptom and repair align.
- **B — Incorrect.** The zone is linked only to the endpoint VNet, not to the separate client VNet.
  The zone is linked only to the endpoint VNet, not to the separate client VNet. The private Storage connectivity evaluation fault concerns private DNS virtual-network links. Private Storage connectivity evaluation failed on private DNS zone groups; this private DNS virtual-network links finding redirects private Storage connectivity evaluation remediation away from private DNS zone groups.
- **C — Incorrect.** The design expects a service endpoint to allocate a private IP address in the subnet.
  The design expects a service endpoint to allocate a private IP address in the subnet. The private Storage connectivity evaluation fault concerns service endpoint traffic. Private Storage connectivity evaluation may fix service endpoint traffic, yet private DNS zone groups still fails; this private Storage connectivity evaluation diagnosis of service endpoint traffic is wrong for private DNS zone groups.
- **D — Incorrect.** No matching privatelink private DNS zone is available to the client resolver.
  No matching privatelink private DNS zone is available to the client resolver. The private Storage connectivity evaluation fault concerns private endpoint DNS zones. Private Storage connectivity evaluation has private endpoint DNS zones impact, but private DNS zone groups is the private Storage connectivity evaluation failed path; the private endpoint DNS zones state cannot produce private DNS zone groups failure.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q37 — C

**Question:** During an endpoint comparison fault drill, the private Storage connectivity evaluation does not make private records resolvable from the intended virtual network. Which finding identifies the defect?

- **A — Incorrect.** Public access was disabled before the private DNS record propagated to clients.
  Public access was disabled before the private DNS record propagated to clients. The private Storage connectivity evaluation fault concerns public network access. Private Storage connectivity evaluation failed on private DNS virtual-network links; this public network access finding redirects private Storage connectivity evaluation remediation away from private DNS virtual-network links.
- **B — Incorrect.** The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule.
  The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule. The private Storage connectivity evaluation fault concerns service endpoint authorization. Private Storage connectivity evaluation may fix service endpoint authorization, yet private DNS virtual-network links still fails; this private Storage connectivity evaluation diagnosis of service endpoint authorization is wrong for private DNS virtual-network links.
- **C — Correct.** The zone is linked only to the endpoint VNet, not to the separate client VNet.
  The zone is linked only to the endpoint VNet, not to the separate client VNet. Removing this private DNS virtual-network links condition lets the private Storage connectivity evaluation make private records resolvable from the intended virtual network while leaving healthy controls unchanged.
- **D — Incorrect.** The zone group references a private DNS zone for a different service subresource.
  The zone group references a private DNS zone for a different service subresource. The private Storage connectivity evaluation fault concerns private DNS zone groups. Private Storage connectivity evaluation could repair private DNS zone groups while private DNS virtual-network links stays broken in private Storage connectivity evaluation; the private Storage connectivity evaluation remains unable to make private records resolvable from the intended virtual network.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Azure Private DNS zones](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone)

**Source reviewed:** 2026-08-31

## LAB19-Q38 — C

**Question:** The private Storage connectivity evaluation setup finishes, yet the endpoint comparison cannot disable the service's public network path after private connectivity works. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The connection remains Pending because the service owner has not approved it.
  The connection remains Pending because the service owner has not approved it. The private Storage connectivity evaluation fault concerns private endpoint approval. Private Storage connectivity evaluation may fix private endpoint approval, yet public network access still fails; this private Storage connectivity evaluation diagnosis of private endpoint approval is wrong for public network access.
- **B — Incorrect.** The public firewall changed to deny before the deployment host had an allowed path.
  The public firewall changed to deny before the deployment host had an allowed path. The private Storage connectivity evaluation fault concerns selected-network firewalls. Private Storage connectivity evaluation has selected-network firewalls impact, but public network access is the private Storage connectivity evaluation failed path; the selected-network firewalls state cannot produce public network access failure.
- **C — Correct.** Public access was disabled before the private DNS record propagated to clients.
  Public access was disabled before the private DNS record propagated to clients. In private Storage connectivity evaluation, this public network access cause matches the failure to disable the service's public network path after private connectivity works.
- **D — Incorrect.** The zone is linked only to the endpoint VNet, not to the separate client VNet.
  The zone is linked only to the endpoint VNet, not to the separate client VNet. The private Storage connectivity evaluation fault concerns private DNS virtual-network links. Private Storage connectivity evaluation failed on public network access; this private DNS virtual-network links finding redirects private Storage connectivity evaluation remediation away from public network access.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q39 — A

**Question:** An endpoint comparison break/fix in the private Storage connectivity evaluation fails when operators try to identify whether the provider accepted a pending private connection. Which diagnosis fits?

- **A — Correct.** The connection remains Pending because the service owner has not approved it.
  The connection remains Pending because the service owner has not approved it. This private Storage connectivity evaluation condition breaks private endpoint approval, explaining why operators cannot identify whether the provider accepted a pending private connection.
- **B — Incorrect.** The design selects a service endpoint even though clients require a private IP reachable from on-premises.
  The design selects a service endpoint even though clients require a private IP reachable from on-premises. The private Storage connectivity evaluation fault concerns service endpoints versus private endpoints. Private Storage connectivity evaluation could repair service endpoints versus private endpoints while private endpoint approval stays broken in private Storage connectivity evaluation; the private Storage connectivity evaluation remains unable to identify whether the provider accepted a pending private connection.
- **C — Incorrect.** The endpoint targets the blob subresource while the client accesses the file endpoint.
  The endpoint targets the blob subresource while the client accesses the file endpoint. The private Storage connectivity evaluation fault concerns private endpoint network interfaces. Private Storage connectivity evaluation failed on private endpoint approval; this private endpoint network interfaces finding redirects private Storage connectivity evaluation remediation away from private endpoint approval.
- **D — Incorrect.** Public access was disabled before the private DNS record propagated to clients.
  Public access was disabled before the private DNS record propagated to clients. The private Storage connectivity evaluation fault concerns public network access. Private Storage connectivity evaluation may fix public network access, yet private endpoint approval still fails; this private Storage connectivity evaluation diagnosis of public network access is wrong for private endpoint approval.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q40 — A

**Question:** The private Storage connectivity evaluation troubleshooting scope is the endpoint comparison need to choose between subnet authorization to a public endpoint and a private network interface. Which condition should be corrected first?

- **A — Correct.** The design selects a service endpoint even though clients require a private IP reachable from on-premises.
  For the private Storage connectivity evaluation, the service endpoints versus private endpoints failure is causal: the design selects a service endpoint even though clients require a private IP reachable from on-premises. Correcting it restores the ability to choose between subnet authorization to a public endpoint and a private network interface.
- **B — Incorrect.** The design expects a service endpoint to allocate a private IP address in the subnet.
  The design expects a service endpoint to allocate a private IP address in the subnet. The private Storage connectivity evaluation fault concerns service endpoint traffic. Private Storage connectivity evaluation failed on service endpoints versus private endpoints; this service endpoint traffic finding redirects private Storage connectivity evaluation remediation away from service endpoints versus private endpoints.
- **C — Incorrect.** No matching privatelink private DNS zone is available to the client resolver.
  No matching privatelink private DNS zone is available to the client resolver. The private Storage connectivity evaluation fault concerns private endpoint DNS zones. Private Storage connectivity evaluation may fix private endpoint DNS zones, yet service endpoints versus private endpoints still fails; this private Storage connectivity evaluation diagnosis of private endpoint DNS zones is wrong for service endpoints versus private endpoints.
- **D — Incorrect.** The connection remains Pending because the service owner has not approved it.
  The connection remains Pending because the service owner has not approved it. The private Storage connectivity evaluation fault concerns private endpoint approval. Private Storage connectivity evaluation has private endpoint approval impact, but service endpoints versus private endpoints is the private Storage connectivity evaluation failed path; the private endpoint approval state cannot produce service endpoints versus private endpoints failure.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q41 — B

**Question:** Which endpoint comparison path makes the private Storage connectivity evaluation able to keep service traffic on the Azure backbone while using the service's public endpoint, then inspects the defining properties?

- **A — Incorrect.** First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
  First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections. This private Storage connectivity evaluation pair serves selected-network firewalls. Selected-network firewalls cannot replace service endpoint traffic in private Storage connectivity evaluation. Use this service endpoint traffic pair instead: First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.
- **B — Correct.** First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.
  First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules. The private Storage connectivity evaluation uses its service endpoint traffic mutation gate and service endpoint traffic verification gate before it can keep service traffic on the Azure backbone while using the service's public endpoint.
- **C — Incorrect.** First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network.
  First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network. This private Storage connectivity evaluation pair serves private DNS virtual-network links. Private Storage connectivity evaluation uses private DNS virtual-network links for both steps; service endpoint traffic remains untouched in private Storage connectivity evaluation, so its service endpoint traffic gate to keep service traffic on the Azure backbone while using the service's public endpoint fails.
- **D — Incorrect.** First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.
  First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests. This private Storage connectivity evaluation pair serves public network access. Private Storage connectivity evaluation closes public network access, not service endpoint traffic; without the service endpoint traffic workflow, it cannot keep service traffic on the Azure backbone while using the service's public endpoint.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q42 — D

**Question:** At the private Storage connectivity evaluation approval gate, operators must show that the endpoint comparison can authorize a selected subnet identity on a service firewall. Which endpoint comparison configure-and-check pair is defensible?

- **A — Incorrect.** First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
  First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state. This private Storage connectivity evaluation pair serves private endpoint network interfaces. Private Storage connectivity evaluation proves private endpoint network interfaces, but service endpoint authorization lacks implementation in private Storage connectivity evaluation and service endpoint authorization proof; the service endpoint authorization outcome to authorize a selected subnet identity on a service firewall remains open.
- **B — Incorrect.** First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.
  First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests. This private Storage connectivity evaluation pair serves public network access. Private Storage connectivity evaluation uses public network access for both steps; service endpoint authorization remains untouched in private Storage connectivity evaluation, so its service endpoint authorization gate to authorize a selected subnet identity on a service firewall fails.
- **C — Incorrect.** First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
  First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs. This private Storage connectivity evaluation pair serves private endpoint approval. Private Storage connectivity evaluation closes private endpoint approval, not service endpoint authorization; without the service endpoint authorization workflow, it cannot authorize a selected subnet identity on a service firewall.
- **D — Correct.** First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
  The private Storage connectivity evaluation gets a complete service endpoint authorization sequence here: first, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls. Read-back evidence follows the change.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q43 — C

**Question:** The private Storage connectivity evaluation forbids a partial endpoint comparison result. Operators must first deny service requests from networks that are not explicitly selected and afterward confirm the private Storage connectivity evaluation outcome. Which endpoint comparison sequence is complete?

- **A — Incorrect.** First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
  First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address. This private Storage connectivity evaluation pair serves private endpoint DNS zones. Private Storage connectivity evaluation uses private endpoint DNS zones for both steps; selected-network firewalls remains untouched in private Storage connectivity evaluation, so its selected-network firewalls gate to deny service requests from networks that are not explicitly selected fails.
- **B — Incorrect.** First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
  First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs. This private Storage connectivity evaluation pair serves private endpoint approval. Private Storage connectivity evaluation closes private endpoint approval, not selected-network firewalls; without the selected-network firewalls workflow, it cannot deny service requests from networks that are not explicitly selected.
- **C — Correct.** First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
  First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections. This ordered selected-network firewalls workflow lets the private Storage connectivity evaluation deny service requests from networks that are not explicitly selected and then verify the resulting state.
- **D — Incorrect.** First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
  First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination. This private Storage connectivity evaluation pair serves service endpoints versus private endpoints. Private Storage connectivity evaluation proves service endpoints versus private endpoints, but selected-network firewalls lacks implementation in private Storage connectivity evaluation and selected-network firewalls proof; the selected-network firewalls outcome to deny service requests from networks that are not explicitly selected remains open.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q44 — C

**Question:** Only the private Storage connectivity evaluation change needed to assign a private address from the consumer network to a platform service connection is allowed, and endpoint comparison proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.
  First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP. This private Storage connectivity evaluation pair serves private DNS zone groups. Private Storage connectivity evaluation closes private DNS zone groups, not private endpoint network interfaces; without the private endpoint network interfaces workflow, it cannot assign a private address from the consumer network to a platform service connection.
- **B — Incorrect.** First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
  First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination. This private Storage connectivity evaluation pair serves service endpoints versus private endpoints. Service endpoints versus private endpoints cannot replace private endpoint network interfaces in private Storage connectivity evaluation. Use this private endpoint network interfaces pair instead: First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
- **C — Correct.** First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
  First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state. For private Storage connectivity evaluation, the private endpoint network interfaces operation precedes its private endpoint network interfaces read-back check, allowing it to assign a private address from the consumer network to a platform service connection.
- **D — Incorrect.** First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.
  First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules. This private Storage connectivity evaluation pair serves service endpoint traffic. Private Storage connectivity evaluation uses service endpoint traffic for both steps; private endpoint network interfaces remains untouched in private Storage connectivity evaluation, so its private endpoint network interfaces gate to assign a private address from the consumer network to a platform service connection fails.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q45 — C

**Question:** The private Storage connectivity evaluation runbook separates endpoint comparison mutation from validation while it must resolve a service hostname to the connection's private address. Which sequence proves it cleanly?

- **A — Incorrect.** First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network.
  First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network. This private Storage connectivity evaluation pair serves private DNS virtual-network links. Private DNS virtual-network links cannot replace private endpoint DNS zones in private Storage connectivity evaluation. Use this private endpoint DNS zones pair instead: First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
- **B — Incorrect.** First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.
  First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules. This private Storage connectivity evaluation pair serves service endpoint traffic. Private Storage connectivity evaluation proves service endpoint traffic, but private endpoint DNS zones lacks implementation in private Storage connectivity evaluation and private endpoint DNS zones proof; the private endpoint DNS zones outcome to resolve a service hostname to the connection's private address remains open.
- **C — Correct.** First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
  First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address. In the private Storage connectivity evaluation, the first private endpoint DNS zones step runs; the private Storage connectivity evaluation then reads private endpoint DNS zones state to prove it can resolve a service hostname to the connection's private address.
- **D — Incorrect.** First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
  First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls. This private Storage connectivity evaluation pair serves service endpoint authorization. Private Storage connectivity evaluation closes service endpoint authorization, not private endpoint DNS zones; without the private endpoint DNS zones workflow, it cannot resolve a service hostname to the connection's private address.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q46 — B

**Question:** The private Storage connectivity evaluation checkpoint requires both this endpoint comparison outcome—create the endpoint-to-name-resolution association automatically—and a read-only private Storage connectivity evaluation state check. Which endpoint comparison response is complete?

- **A — Incorrect.** First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.
  First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests. This private Storage connectivity evaluation pair serves public network access. Private Storage connectivity evaluation proves public network access, but private DNS zone groups lacks implementation in private Storage connectivity evaluation and private DNS zone groups proof; the private DNS zone groups outcome to create the endpoint-to-name-resolution association automatically remains open.
- **B — Correct.** First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.
  For the private Storage connectivity evaluation, the safe private DNS zone groups order is: first, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP. The private Storage connectivity evaluation records private DNS zone groups proof after configuration.
- **C — Incorrect.** First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
  First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls. This private Storage connectivity evaluation pair serves service endpoint authorization. Private Storage connectivity evaluation closes service endpoint authorization, not private DNS zone groups; without the private DNS zone groups workflow, it cannot create the endpoint-to-name-resolution association automatically.
- **D — Incorrect.** First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
  First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections. This private Storage connectivity evaluation pair serves selected-network firewalls. Selected-network firewalls cannot replace private DNS zone groups in private Storage connectivity evaluation. Use this private DNS zone groups pair instead: First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB19-CP01`).

**Microsoft Learn sources:**

- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

**Source reviewed:** 2026-08-31

## LAB19-Q47 — C

**Question:** The private Storage connectivity evaluation runbook must make private records resolvable from the intended virtual network, then retain endpoint comparison read-back evidence. Which private Storage connectivity evaluation pair completes both duties?

- **A — Incorrect.** First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
  First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs. This private Storage connectivity evaluation pair serves private endpoint approval. Private Storage connectivity evaluation uses private endpoint approval for both steps; private DNS virtual-network links remains untouched in private Storage connectivity evaluation, so its private DNS virtual-network links gate to make private records resolvable from the intended virtual network fails.
- **B — Incorrect.** First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
  First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections. This private Storage connectivity evaluation pair serves selected-network firewalls. Private Storage connectivity evaluation closes selected-network firewalls, not private DNS virtual-network links; without the private DNS virtual-network links workflow, it cannot make private records resolvable from the intended virtual network.
- **C — Correct.** First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network.
  First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network. The private Storage connectivity evaluation uses its private DNS virtual-network links mutation gate and private DNS virtual-network links verification gate before it can make private records resolvable from the intended virtual network.
- **D — Incorrect.** First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
  First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state. This private Storage connectivity evaluation pair serves private endpoint network interfaces. Private Storage connectivity evaluation proves private endpoint network interfaces, but private DNS virtual-network links lacks implementation in private Storage connectivity evaluation and private DNS virtual-network links proof; the private DNS virtual-network links outcome to make private records resolvable from the intended virtual network remains open.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB19-CP02`).

**Microsoft Learn sources:**

- [Azure Private DNS zones](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone)

**Source reviewed:** 2026-08-31

## LAB19-Q48 — D

**Question:** To satisfy the endpoint comparison requirement, operators must change the private Storage connectivity evaluation configuration and prove it can disable the service's public network path after private connectivity works. Which sequence is coherent?

- **A — Incorrect.** First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
  First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination. This private Storage connectivity evaluation pair serves service endpoints versus private endpoints. Private Storage connectivity evaluation closes service endpoints versus private endpoints, not public network access; without the public network access workflow, it cannot disable the service's public network path after private connectivity works.
- **B — Incorrect.** First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
  First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state. This private Storage connectivity evaluation pair serves private endpoint network interfaces. Private endpoint network interfaces cannot replace public network access in private Storage connectivity evaluation. Use this public network access pair instead: First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.
- **C — Incorrect.** First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
  First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address. This private Storage connectivity evaluation pair serves private endpoint DNS zones. Private Storage connectivity evaluation proves private endpoint DNS zones, but public network access lacks implementation in private Storage connectivity evaluation and public network access proof; the public network access outcome to disable the service's public network path after private connectivity works remains open.
- **D — Correct.** First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.
  The private Storage connectivity evaluation gets a complete public network access sequence here: first, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests. Read-back evidence follows the change.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB19-CP03`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q49 — A

**Question:** The network administrator comparing Storage service and private endpoints needs a safe private Storage connectivity evaluation change to identify whether the provider accepted a pending private connection, followed by endpoint comparison evidence. Which pair merits approval?

- **A — Correct.** First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
  First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs. This ordered private endpoint approval workflow lets the private Storage connectivity evaluation identify whether the provider accepted a pending private connection and then verify the resulting state.
- **B — Incorrect.** First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.
  First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules. This private Storage connectivity evaluation pair serves service endpoint traffic. Private Storage connectivity evaluation proves service endpoint traffic, but private endpoint approval lacks implementation in private Storage connectivity evaluation and private endpoint approval proof; the private endpoint approval outcome to identify whether the provider accepted a pending private connection remains open.
- **C — Incorrect.** First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
  First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address. This private Storage connectivity evaluation pair serves private endpoint DNS zones. Private Storage connectivity evaluation uses private endpoint DNS zones for both steps; private endpoint approval remains untouched in private Storage connectivity evaluation, so its private endpoint approval gate to identify whether the provider accepted a pending private connection fails.
- **D — Incorrect.** First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.
  First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP. This private Storage connectivity evaluation pair serves private DNS zone groups. Private Storage connectivity evaluation closes private DNS zone groups, not private endpoint approval; without the private endpoint approval workflow, it cannot identify whether the provider accepted a pending private connection.

**Objectives:** `NW-SECURE-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB19-CP04`).

**Microsoft Learn sources:**

- [Azure Private Endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Source reviewed:** 2026-08-31

## LAB19-Q50 — A

**Question:** The private Storage connectivity evaluation has two endpoint comparison gates: choose between subnet authorization to a public endpoint and a private network interface, then prove the private Storage connectivity evaluation state. Which endpoint comparison sequence works?

- **A — Correct.** First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
  First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination. For private Storage connectivity evaluation, the service endpoints versus private endpoints operation precedes its service endpoints versus private endpoints read-back check, allowing it to choose between subnet authorization to a public endpoint and a private network interface.
- **B — Incorrect.** First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
  First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls. This private Storage connectivity evaluation pair serves service endpoint authorization. Private Storage connectivity evaluation uses service endpoint authorization for both steps; service endpoints versus private endpoints remains untouched in private Storage connectivity evaluation, so its service endpoints versus private endpoints gate to choose between subnet authorization to a public endpoint and a private network interface fails.
- **C — Incorrect.** First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.
  First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP. This private Storage connectivity evaluation pair serves private DNS zone groups. Private Storage connectivity evaluation closes private DNS zone groups, not service endpoints versus private endpoints; without the service endpoints versus private endpoints workflow, it cannot choose between subnet authorization to a public endpoint and a private network interface.
- **D — Incorrect.** First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network.
  First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network. This private Storage connectivity evaluation pair serves private DNS virtual-network links. Private DNS virtual-network links cannot replace service endpoints versus private endpoints in private Storage connectivity evaluation. Use this service endpoints versus private endpoints pair instead: First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.

**Objectives:** `NW-SECURE-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB19-CP05`).

**Microsoft Learn sources:**

- [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Source reviewed:** 2026-08-31
