# Lab 19 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB19-Q01 — Foundational

The endpoint comparison architecture note requires the private Storage connectivity evaluation environment to keep service traffic on the Azure backbone while using the service's public endpoint. Which statement defines the relevant endpoint comparison boundary?

- A. Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall.
- B. Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP.
- C. Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity.
- D. A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address.

## LAB19-Q02 — Foundational

A new endpoint comparison operator must explain why the private Storage connectivity evaluation can authorize a selected subnet identity on a service firewall. Which explanation is accurate?

- A. A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions.
- B. A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.
- C. A private endpoint connection must reach Approved state before the service accepts traffic through it.
- D. Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall.

## LAB19-Q03 — Foundational

The private Storage connectivity evaluation acceptance criteria require operators to deny service requests from networks that are not explicitly selected. Which service fact supports that requirement?

- A. A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource.
- B. A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design.
- C. A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions.
- D. Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet.

## LAB19-Q04 — Foundational

An endpoint comparison reviewer challenges whether the private Storage connectivity evaluation can assign a private address from the consumer network to a platform service connection. Which response resolves the concern?

- A. A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource.
- B. Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP.
- C. Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity.
- D. A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address.

## LAB19-Q05 — Foundational

The private Storage connectivity evaluation handoff omits the endpoint comparison rule needed to resolve a service hostname to the connection's private address. Which statement should the team add?

- A. A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.
- B. A private endpoint connection must reach Approved state before the service accepts traffic through it.
- C. Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP.
- D. Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall.

## LAB19-Q06 — Foundational

An endpoint comparison incident review of the private Storage connectivity evaluation depends on the ability to create the endpoint-to-name-resolution association automatically. Which platform description is reliable?

- A. A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design.
- B. Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet.
- C. A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions.
- D. A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.

## LAB19-Q07 — Foundational

A network administrator comparing Storage service and private endpoints is updating the endpoint comparison runbook. The requirement is to make private records resolvable from the intended virtual network. Which statement describes Azure behavior correctly?

- A. A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design.
- B. Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity.
- C. A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address.
- D. A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource.

## LAB19-Q08 — Foundational

An endpoint comparison peer review asks how the private Storage connectivity evaluation should handle this outcome: disable the service's public network path after private connectivity works. Which explanation is accurate?

- A. Disabling public network access makes the approved private path and DNS resolution prerequisites for service connectivity.
- B. A private endpoint connection must reach Approved state before the service accepts traffic through it.
- C. Enabling a service endpoint alone does not grant data access or automatically update the destination service firewall.
- D. Private endpoint DNS commonly maps the service hostname through a privatelink zone to the endpoint's private IP.

## LAB19-Q09 — Foundational

For the private Storage connectivity evaluation, the endpoint comparison plan must identify whether the provider accepted a pending private connection. Which statement about endpoint comparison belongs in the private Storage connectivity evaluation record?

- A. Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet.
- B. A PaaS firewall with default deny admits only configured network rules, private endpoints, and supported exceptions.
- C. A private DNS zone group associates endpoint subresources with zones and manages the corresponding DNS records.
- D. A private endpoint connection must reach Approved state before the service accepts traffic through it.

## LAB19-Q10 — Foundational

The endpoint comparison review compares four claims for the private Storage connectivity evaluation requirement to choose between subnet authorization to a public endpoint and a private network interface. Which claim is technically sound?

- A. A service endpoint extends subnet identity to a PaaS service while the service still uses its public endpoint address.
- B. A private endpoint creates a read-only NIC with a private IP in the selected subnet for a specific service subresource.
- C. Service endpoints secure a public service endpoint to a subnet, while private endpoints place a service-specific private IP in a subnet.
- D. A private DNS zone is resolvable from a virtual network only when linked directly or through an approved DNS forwarding design.

## LAB19-Q11 — Foundational

For the private Storage connectivity evaluation, operators need to keep service traffic on the Azure backbone while using the service's public endpoint. Which change realizes that requirement?

- A. Set default deny only after establishing an approved administrative and workload access path.
- B. Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall.
- C. Attach the correct private DNS zone to the endpoint's zone group.
- D. Approve the pending connection only after confirming its requester, endpoint ID, and target subresource.

## LAB19-Q12 — Foundational

Operators must automate the private Storage connectivity evaluation change needed to authorize a selected subnet identity on a service firewall. Which endpoint comparison operation belongs in the runbook?

- A. Create the endpoint in the approved subnet and select the correct group ID for the service.
- B. Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration.
- C. Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure.
- D. Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.

## LAB19-Q13 — Foundational

A private Storage connectivity evaluation review finds endpoint comparison drift from the need to deny service requests from networks that are not explicitly selected. Which correction addresses that drift?

- A. Create or reuse the service-specific private DNS zone and attach it through a zone group.
- B. Validate private connectivity completely before disabling the public endpoint.
- C. Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall.
- D. Set default deny only after establishing an approved administrative and workload access path.

## LAB19-Q14 — Foundational

The private Storage connectivity evaluation window permits only the endpoint comparison change needed to assign a private address from the consumer network to a platform service connection. Which option respects the boundary?

- A. Attach the correct private DNS zone to the endpoint's zone group.
- B. Create the endpoint in the approved subnet and select the correct group ID for the service.
- C. Approve the pending connection only after confirming its requester, endpoint ID, and target subresource.
- D. Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.

## LAB19-Q15 — Foundational

The endpoint comparison preflight has passed; the private Storage connectivity evaluation must now resolve a service hostname to the connection's private address. Which operation should run?

- A. Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration.
- B. Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure.
- C. Set default deny only after establishing an approved administrative and workload access path.
- D. Create or reuse the service-specific private DNS zone and attach it through a zone group.

## LAB19-Q16 — Applied

The private Storage connectivity evaluation plan must create the endpoint-to-name-resolution association automatically while limiting the mutation scope to endpoint comparison. Which action is appropriate?

- A. Attach the correct private DNS zone to the endpoint's zone group.
- B. Validate private connectivity completely before disabling the public endpoint.
- C. Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall.
- D. Create the endpoint in the approved subnet and select the correct group ID for the service.

## LAB19-Q17 — Applied

An endpoint comparison ticket in the private Storage connectivity evaluation says to make private records resolvable from the intended virtual network. Which endpoint comparison action completes the private Storage connectivity evaluation request with minimal change?

- A. Approve the pending connection only after confirming its requester, endpoint ID, and target subresource.
- B. Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration.
- C. Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.
- D. Create or reuse the service-specific private DNS zone and attach it through a zone group.

## LAB19-Q18 — Applied

The approach for the private Storage connectivity evaluation is approved, but the endpoint comparison environment still cannot disable the service's public network path after private connectivity works. Which implementation step closes the gap?

- A. Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure.
- B. Set default deny only after establishing an approved administrative and workload access path.
- C. Attach the correct private DNS zone to the endpoint's zone group.
- D. Validate private connectivity completely before disabling the public endpoint.

## LAB19-Q19 — Applied

The network administrator comparing Storage service and private endpoints may change the private Storage connectivity evaluation only to identify whether the provider accepted a pending private connection. Which endpoint comparison action stays within that assignment?

- A. Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall.
- B. Create the endpoint in the approved subnet and select the correct group ID for the service.
- C. Approve the pending connection only after confirming its requester, endpoint ID, and target subresource.
- D. Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration.

## LAB19-Q20 — Applied

An endpoint comparison dry run shows no private Storage connectivity evaluation command will choose between subnet authorization to a public endpoint and a private network interface. Which action belongs before execution?

- A. Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization.
- B. Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure.
- C. Create or reuse the service-specific private DNS zone and attach it through a zone group.
- D. Validate private connectivity completely before disabling the public endpoint.

## LAB19-Q21 — Applied

The network administrator comparing Storage service and private endpoints must confirm the private Storage connectivity evaluation, without mutation, can keep service traffic on the Azure backbone while using the service's public endpoint. Which endpoint comparison check qualifies?

- A. Query subnet serviceEndpoints and the service's virtual network rules.
- B. Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
- C. List virtualNetworkLinks and test resolution from each intended client network.
- D. Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.

## LAB19-Q22 — Applied

The private Storage connectivity evaluation configuration is complete; the endpoint comparison reviewers need evidence it can authorize a selected subnet identity on a service firewall. Which observation shows success?

- A. Resolve the normal service hostname inside the VNet and confirm the final private address.
- B. Query publicNetworkAccess and perform positive private and negative public-path tests.
- C. Query subnet serviceEndpoints and the service's virtual network rules.
- D. Verify endpoint state, firewall rule, and data-plane authorization as separate controls.

## LAB19-Q23 — Applied

The endpoint comparison validation asks whether the private Storage connectivity evaluation can deny service requests from networks that are not explicitly selected. Which observable state is strongest?

- A. Query the zone group and match its privateDnsZoneConfigs and generated record IP.
- B. Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
- C. Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
- D. Verify endpoint state, firewall rule, and data-plane authorization as separate controls.

## LAB19-Q24 — Applied

A private Storage connectivity evaluation review must prove the endpoint comparison ability to assign a private address from the consumer network to a platform service connection. Which check avoids an adjacent feature?

- A. List virtualNetworkLinks and test resolution from each intended client network.
- B. Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
- C. Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
- D. Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.

## LAB19-Q25 — Applied

The private Storage connectivity evaluation evidence bundle needs an endpoint comparison result showing it can resolve a service hostname to the connection's private address. Which result belongs in the checkpoint?

- A. Query publicNetworkAccess and perform positive private and negative public-path tests.
- B. Query subnet serviceEndpoints and the service's virtual network rules.
- C. Resolve the normal service hostname inside the VNet and confirm the final private address.
- D. Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.

## LAB19-Q26 — Applied

Before private Storage connectivity evaluation cleanup, the endpoint comparison team must reconfirm it can create the endpoint-to-name-resolution association automatically. Which read-only inspection should run?

- A. Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
- B. Query the zone group and match its privateDnsZoneConfigs and generated record IP.
- C. Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
- D. Resolve the normal service hostname inside the VNet and confirm the final private address.

## LAB19-Q27 — Applied

The private Storage connectivity evaluation setup reports success after the endpoint comparison attempt to make private records resolvable from the intended virtual network. Which endpoint comparison read-only observation proves the private Storage connectivity evaluation outcome?

- A. List virtualNetworkLinks and test resolution from each intended client network.
- B. Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
- C. Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
- D. Query the zone group and match its privateDnsZoneConfigs and generated record IP.

## LAB19-Q28 — Applied

The endpoint comparison log says the private Storage connectivity evaluation can now disable the service's public network path after private connectivity works. Which endpoint comparison state should the private Storage connectivity evaluation acceptance test retain?

- A. Query subnet serviceEndpoints and the service's virtual network rules.
- B. Query publicNetworkAccess and perform positive private and negative public-path tests.
- C. Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
- D. List virtualNetworkLinks and test resolution from each intended client network.

## LAB19-Q29 — Applied

The private Storage connectivity evaluation rejects endpoint comparison exit status as proof it can identify whether the provider accepted a pending private connection. Which private Storage connectivity evaluation result is valid evidence?

- A. Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
- B. Resolve the normal service hostname inside the VNet and confirm the final private address.
- C. Query publicNetworkAccess and perform positive private and negative public-path tests.
- D. Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.

## LAB19-Q30 — Applied

The endpoint comparison validator needs one private Storage connectivity evaluation query after the change to choose between subnet authorization to a public endpoint and a private network interface. Which endpoint comparison property should the private Storage connectivity evaluation validator inspect?

- A. Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
- B. Query the zone group and match its privateDnsZoneConfigs and generated record IP.
- C. Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
- D. Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.

## LAB19-Q31 — Applied

The private Storage connectivity evaluation result is partial because the endpoint comparison cannot keep service traffic on the Azure backbone while using the service's public endpoint. Which condition accounts for that result?

- A. The design expects a service endpoint to allocate a private IP address in the subnet.
- B. The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule.
- C. The zone group references a private DNS zone for a different service subresource.
- D. The design selects a service endpoint even though clients require a private IP reachable from on-premises.

## LAB19-Q32 — Applied

The endpoint comparison evidence shows the private Storage connectivity evaluation cannot authorize a selected subnet identity on a service firewall. Which root cause fits that evidence?

- A. The public firewall changed to deny before the deployment host had an allowed path.
- B. The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule.
- C. The zone is linked only to the endpoint VNet, not to the separate client VNet.
- D. The design expects a service endpoint to allocate a private IP address in the subnet.

## LAB19-Q33 — Applied

Although the private Storage connectivity evaluation is meant to let the endpoint comparison deny service requests from networks that are not explicitly selected, its checkpoint fails. Which endpoint comparison defect explains the failure?

- A. The endpoint targets the blob subresource while the client accesses the file endpoint.
- B. Public access was disabled before the private DNS record propagated to clients.
- C. The public firewall changed to deny before the deployment host had an allowed path.
- D. The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule.

## LAB19-Q34 — Applied

The endpoint comparison support team isolated the private Storage connectivity evaluation incident to the attempt to assign a private address from the consumer network to a platform service connection. Which condition prevents success?

- A. No matching privatelink private DNS zone is available to the client resolver.
- B. The endpoint targets the blob subresource while the client accesses the file endpoint.
- C. The connection remains Pending because the service owner has not approved it.
- D. The public firewall changed to deny before the deployment host had an allowed path.

## LAB19-Q35 — Applied

A private Storage connectivity evaluation query surprises the network administrator comparing Storage service and private endpoints during the endpoint comparison attempt to resolve a service hostname to the connection's private address. Which finding explains it?

- A. No matching privatelink private DNS zone is available to the client resolver.
- B. The zone group references a private DNS zone for a different service subresource.
- C. The design selects a service endpoint even though clients require a private IP reachable from on-premises.
- D. The endpoint targets the blob subresource while the client accesses the file endpoint.

## LAB19-Q36 — Applied

Other private Storage connectivity evaluation components are healthy, but the endpoint comparison still cannot create the endpoint-to-name-resolution association automatically. Which state causes the isolated failure?

- A. The zone group references a private DNS zone for a different service subresource.
- B. The zone is linked only to the endpoint VNet, not to the separate client VNet.
- C. The design expects a service endpoint to allocate a private IP address in the subnet.
- D. No matching privatelink private DNS zone is available to the client resolver.

## LAB19-Q37 — Applied

During an endpoint comparison fault drill, the private Storage connectivity evaluation does not make private records resolvable from the intended virtual network. Which finding identifies the defect?

- A. Public access was disabled before the private DNS record propagated to clients.
- B. The subnet endpoint is enabled, but the storage firewall has no matching virtual-network rule.
- C. The zone is linked only to the endpoint VNet, not to the separate client VNet.
- D. The zone group references a private DNS zone for a different service subresource.

## LAB19-Q38 — Applied

The private Storage connectivity evaluation setup finishes, yet the endpoint comparison cannot disable the service's public network path after private connectivity works. Which misconfiguration explains the mismatch?

- A. The connection remains Pending because the service owner has not approved it.
- B. The public firewall changed to deny before the deployment host had an allowed path.
- C. Public access was disabled before the private DNS record propagated to clients.
- D. The zone is linked only to the endpoint VNet, not to the separate client VNet.

## LAB19-Q39 — Applied

An endpoint comparison break/fix in the private Storage connectivity evaluation fails when operators try to identify whether the provider accepted a pending private connection. Which diagnosis fits?

- A. The connection remains Pending because the service owner has not approved it.
- B. The design selects a service endpoint even though clients require a private IP reachable from on-premises.
- C. The endpoint targets the blob subresource while the client accesses the file endpoint.
- D. Public access was disabled before the private DNS record propagated to clients.

## LAB19-Q40 — Applied

The private Storage connectivity evaluation troubleshooting scope is the endpoint comparison need to choose between subnet authorization to a public endpoint and a private network interface. Which condition should be corrected first?

- A. The design selects a service endpoint even though clients require a private IP reachable from on-premises.
- B. The design expects a service endpoint to allocate a private IP address in the subnet.
- C. No matching privatelink private DNS zone is available to the client resolver.
- D. The connection remains Pending because the service owner has not approved it.

## LAB19-Q41 — Advanced

Which endpoint comparison path makes the private Storage connectivity evaluation able to keep service traffic on the Azure backbone while using the service's public endpoint, then inspects the defining properties?

- A. First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
- B. First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.
- C. First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network.
- D. First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.

## LAB19-Q42 — Advanced

At the private Storage connectivity evaluation approval gate, operators must show that the endpoint comparison can authorize a selected subnet identity on a service firewall. Which endpoint comparison configure-and-check pair is defensible?

- A. First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
- B. First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.
- C. First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
- D. First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls.

## LAB19-Q43 — Advanced

The private Storage connectivity evaluation forbids a partial endpoint comparison result. Operators must first deny service requests from networks that are not explicitly selected and afterward confirm the private Storage connectivity evaluation outcome. Which endpoint comparison sequence is complete?

- A. First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
- B. First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
- C. First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
- D. First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.

## LAB19-Q44 — Advanced

Only the private Storage connectivity evaluation change needed to assign a private address from the consumer network to a platform service connection is allowed, and endpoint comparison proof is mandatory. Which pair fits?

- A. First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.
- B. First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
- C. First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
- D. First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.

## LAB19-Q45 — Advanced

The private Storage connectivity evaluation runbook separates endpoint comparison mutation from validation while it must resolve a service hostname to the connection's private address. Which sequence proves it cleanly?

- A. First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network.
- B. First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.
- C. First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
- D. First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls.

## LAB19-Q46 — Advanced

The private Storage connectivity evaluation checkpoint requires both this endpoint comparison outcome—create the endpoint-to-name-resolution association automatically—and a read-only private Storage connectivity evaluation state check. Which endpoint comparison response is complete?

- A. First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.
- B. First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.
- C. First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
- D. First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.

## LAB19-Q47 — Advanced

The private Storage connectivity evaluation runbook must make private records resolvable from the intended virtual network, then retain endpoint comparison read-back evidence. Which private Storage connectivity evaluation pair completes both duties?

- A. First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
- B. First, Set default deny only after establishing an approved administrative and workload access path. Then, Query defaultAction, bypass, IP rules, virtual-network rules, and private endpoint connections.
- C. First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network.
- D. First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.

## LAB19-Q48 — Advanced

To satisfy the endpoint comparison requirement, operators must change the private Storage connectivity evaluation configuration and prove it can disable the service's public network path after private connectivity works. Which sequence is coherent?

- A. First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
- B. First, Create the endpoint in the approved subnet and select the correct group ID for the service. Then, Query the endpoint NIC private IP, groupIds, subnet ID, and connection state.
- C. First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
- D. First, Validate private connectivity completely before disabling the public endpoint. Then, Query publicNetworkAccess and perform positive private and negative public-path tests.

## LAB19-Q49 — Advanced

The network administrator comparing Storage service and private endpoints needs a safe private Storage connectivity evaluation change to identify whether the provider accepted a pending private connection, followed by endpoint comparison evidence. Which pair merits approval?

- A. First, Approve the pending connection only after confirming its requester, endpoint ID, and target subresource. Then, Query privateLinkServiceConnectionState.status and compare the endpoint and service-side connection IDs.
- B. First, Enable the service endpoint on the source subnet and authorize that subnet on the PaaS firewall. Then, Query subnet serviceEndpoints and the service's virtual network rules.
- C. First, Create or reuse the service-specific private DNS zone and attach it through a zone group. Then, Resolve the normal service hostname inside the VNet and confirm the final private address.
- D. First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.

## LAB19-Q50 — Advanced

The private Storage connectivity evaluation has two endpoint comparison gates: choose between subnet authorization to a public endpoint and a private network interface, then prove the private Storage connectivity evaluation state. Which endpoint comparison sequence works?

- A. First, Choose the model from requirements for private addressing, on-premises access, DNS, and public exposure. Then, Inspect endpoint type, destination DNS answer, firewall configuration, and packet destination.
- B. First, Add the endpoint-enabled subnet to the service network ACLs and retain identity authorization. Then, Verify endpoint state, firewall rule, and data-plane authorization as separate controls.
- C. First, Attach the correct private DNS zone to the endpoint's zone group. Then, Query the zone group and match its privateDnsZoneConfigs and generated record IP.
- D. First, Link every client VNet that must resolve the endpoint zone without enabling unnecessary autoregistration. Then, List virtualNetworkLinks and test resolution from each intended client network.

[Open the answer key](./ANSWERS.md)
