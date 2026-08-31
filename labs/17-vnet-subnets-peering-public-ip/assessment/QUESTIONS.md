# Lab 17 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB17-Q01 — Foundational

The hub-and-spoke network build handoff omits the network peering rule needed to connect networks without overlapping their address ranges. Which statement should the team add?

- A. Peered virtual networks require nonoverlapping IP address spaces for routable connectivity.
- B. Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network.
- C. The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
- D. A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design.

## LAB17-Q02 — Foundational

A network peering incident review of the hub-and-spoke network build depends on the ability to reserve subnet ranges that do not collide with future network segments. Which platform description is reliable?

- A. Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network.
- B. A usable virtual-network peering relationship has one peering resource in each direction.
- C. Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource.
- D. Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable.

## LAB17-Q03 — Foundational

A network administrator connecting hub and spoke address spaces is updating the network peering runbook. The requirement is to create both directional control-plane links required for connected networks. Which statement describes Azure behavior correctly?

- A. Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints.
- B. A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior.
- C. A usable virtual-network peering relationship has one peering resource in each direction.
- D. Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C.

## LAB17-Q04 — Foundational

A network peering peer review asks how the hub-and-spoke network build should handle this outcome: let a spoke use a hub gateway only when both peering sides permit it. Which explanation is accurate?

- A. The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
- B. A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design.
- C. Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints.
- D. Peered virtual networks require nonoverlapping IP address spaces for routable connectivity.

## LAB17-Q05 — Foundational

For the hub-and-spoke network build, the network peering plan must carry forwarded packets from an NVA across connected networks. Which statement about network peering belongs in the hub-and-spoke network build record?

- A. The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
- B. Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource.
- C. Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable.
- D. Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network.

## LAB17-Q06 — Foundational

The network peering review compares four claims for the hub-and-spoke network build requirement to use the production public-address SKU with secure defaults. Which claim is technically sound?

- A. A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior.
- B. Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource.
- C. Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C.
- D. A usable virtual-network peering relationship has one peering resource in each direction.

## LAB17-Q07 — Foundational

The network peering architecture note requires the hub-and-spoke network build environment to keep the assigned public address stable across resource restarts. Which statement defines the relevant network peering boundary?

- A. A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design.
- B. Peered virtual networks require nonoverlapping IP address spaces for routable connectivity.
- C. A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior.
- D. Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints.

## LAB17-Q08 — Foundational

A new network peering operator must explain why the hub-and-spoke network build can pin a public address to the intended availability-zone design. Which explanation is accurate?

- A. Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable.
- B. Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network.
- C. The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
- D. A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design.

## LAB17-Q09 — Foundational

The hub-and-spoke network build acceptance criteria require operators to make virtual machines use approved custom DNS resolvers. Which service fact supports that requirement?

- A. Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C.
- B. A usable virtual-network peering relationship has one peering resource in each direction.
- C. Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource.
- D. Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable.

## LAB17-Q10 — Foundational

A network peering reviewer challenges whether the hub-and-spoke network build can avoid assuming that connectivity automatically crosses a second peering hop. Which response resolves the concern?

- A. Peered virtual networks require nonoverlapping IP address spaces for routable connectivity.
- B. Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints.
- C. A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior.
- D. Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C.

## LAB17-Q11 — Foundational

The network peering preflight has passed; the hub-and-spoke network build must now connect networks without overlapping their address ranges. Which operation should run?

- A. Create and validate both local-to-remote and remote-to-local peering objects.
- B. Use Standard SKU and add only the required inbound NSG exposure.
- C. Allocate approved RFC 1918 ranges and check them against existing and planned connected networks.
- D. Configure approved resolver IP addresses and renew affected clients when required.

## LAB17-Q12 — Foundational

The hub-and-spoke network build plan must reserve subnet ranges that do not collide with future network segments while limiting the mutation scope to network peering. Which action is appropriate?

- A. Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects.
- B. Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets.
- C. Use static allocation when DNS or allowlists require a stable public address.
- D. Create the required direct peering or introduce an approved routed hub design.

## LAB17-Q13 — Foundational

A network peering ticket in the hub-and-spoke network build says to create both directional control-plane links required for connected networks. Which network peering action completes the hub-and-spoke network build request with minimal change?

- A. Enable forwarded traffic only on the peering directions required by the approved routing design.
- B. Create and validate both local-to-remote and remote-to-local peering objects.
- C. Select zone-redundant placement for regional zonal resilience when supported.
- D. Allocate approved RFC 1918 ranges and check them against existing and planned connected networks.

## LAB17-Q14 — Foundational

The approach for the hub-and-spoke network build is approved, but the network peering environment still cannot let a spoke use a hub gateway only when both peering sides permit it. Which implementation step closes the gap?

- A. Use Standard SKU and add only the required inbound NSG exposure.
- B. Configure approved resolver IP addresses and renew affected clients when required.
- C. Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets.
- D. Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects.

## LAB17-Q15 — Foundational

The network administrator connecting hub and spoke address spaces may change the hub-and-spoke network build only to carry forwarded packets from an NVA across connected networks. Which network peering action stays within that assignment?

- A. Enable forwarded traffic only on the peering directions required by the approved routing design.
- B. Use static allocation when DNS or allowlists require a stable public address.
- C. Create the required direct peering or introduce an approved routed hub design.
- D. Create and validate both local-to-remote and remote-to-local peering objects.

## LAB17-Q16 — Applied

A network peering dry run shows no hub-and-spoke network build command will use the production public-address SKU with secure defaults. Which action belongs before execution?

- A. Select zone-redundant placement for regional zonal resilience when supported.
- B. Allocate approved RFC 1918 ranges and check them against existing and planned connected networks.
- C. Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects.
- D. Use Standard SKU and add only the required inbound NSG exposure.

## LAB17-Q17 — Applied

For the hub-and-spoke network build, operators need to keep the assigned public address stable across resource restarts. Which change realizes that requirement?

- A. Configure approved resolver IP addresses and renew affected clients when required.
- B. Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets.
- C. Enable forwarded traffic only on the peering directions required by the approved routing design.
- D. Use static allocation when DNS or allowlists require a stable public address.

## LAB17-Q18 — Applied

Operators must automate the hub-and-spoke network build change needed to pin a public address to the intended availability-zone design. Which network peering operation belongs in the runbook?

- A. Select zone-redundant placement for regional zonal resilience when supported.
- B. Create the required direct peering or introduce an approved routed hub design.
- C. Create and validate both local-to-remote and remote-to-local peering objects.
- D. Use Standard SKU and add only the required inbound NSG exposure.

## LAB17-Q19 — Applied

A hub-and-spoke network build review finds network peering drift from the need to make virtual machines use approved custom DNS resolvers. Which correction addresses that drift?

- A. Allocate approved RFC 1918 ranges and check them against existing and planned connected networks.
- B. Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects.
- C. Use static allocation when DNS or allowlists require a stable public address.
- D. Configure approved resolver IP addresses and renew affected clients when required.

## LAB17-Q20 — Applied

The hub-and-spoke network build window permits only the network peering change needed to avoid assuming that connectivity automatically crosses a second peering hop. Which option respects the boundary?

- A. Create the required direct peering or introduce an approved routed hub design.
- B. Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets.
- C. Enable forwarded traffic only on the peering directions required by the approved routing design.
- D. Select zone-redundant placement for regional zonal resilience when supported.

## LAB17-Q21 — Applied

The hub-and-spoke network build evidence bundle needs a network peering result showing it can connect networks without overlapping their address ranges. Which result belongs in the checkpoint?

- A. Query both peerings and confirm the gateway flags and connected state.
- B. Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
- C. Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
- D. Inspect effective routes from the source and test the exact destination path.

## LAB17-Q22 — Applied

Before hub-and-spoke network build cleanup, the network peering team must reconfirm it can reserve subnet ranges that do not collide with future network segments. Which read-only inspection should run?

- A. Read allowForwardedTraffic on both directional peering resources.
- B. List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
- C. Query the public IP zones array and the region's zone support.
- D. Query every addressSpace.addressPrefixes value and prove no peered range overlaps.

## LAB17-Q23 — Applied

The hub-and-spoke network build setup reports success after the network peering attempt to create both directional control-plane links required for connected networks. Which network peering read-only observation proves the hub-and-spoke network build outcome?

- A. Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
- B. Query peeringState and peeringSyncLevel on both virtual networks.
- C. Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
- D. List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.

## LAB17-Q24 — Applied

The network peering log says the hub-and-spoke network build can now let a spoke use a hub gateway only when both peering sides permit it. Which network peering state should the hub-and-spoke network build acceptance test retain?

- A. Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
- B. Inspect effective routes from the source and test the exact destination path.
- C. Query peeringState and peeringSyncLevel on both virtual networks.
- D. Query both peerings and confirm the gateway flags and connected state.

## LAB17-Q25 — Applied

The hub-and-spoke network build rejects network peering exit status as proof it can carry forwarded packets from an NVA across connected networks. Which hub-and-spoke network build result is valid evidence?

- A. Query the public IP zones array and the region's zone support.
- B. Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
- C. Query both peerings and confirm the gateway flags and connected state.
- D. Read allowForwardedTraffic on both directional peering resources.

## LAB17-Q26 — Applied

The network peering validator needs one hub-and-spoke network build query after the change to use the production public-address SKU with secure defaults. Which network peering property should the hub-and-spoke network build validator inspect?

- A. Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
- B. List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
- C. Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
- D. Read allowForwardedTraffic on both directional peering resources.

## LAB17-Q27 — Applied

The network administrator connecting hub and spoke address spaces must confirm the hub-and-spoke network build, without mutation, can keep the assigned public address stable across resource restarts. Which network peering check qualifies?

- A. Inspect effective routes from the source and test the exact destination path.
- B. Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
- C. Query peeringState and peeringSyncLevel on both virtual networks.
- D. Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.

## LAB17-Q28 — Applied

The hub-and-spoke network build configuration is complete; the network peering reviewers need evidence it can pin a public address to the intended availability-zone design. Which observation shows success?

- A. Query the public IP zones array and the region's zone support.
- B. Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
- C. Query both peerings and confirm the gateway flags and connected state.
- D. Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.

## LAB17-Q29 — Applied

The network peering validation asks whether the hub-and-spoke network build can make virtual machines use approved custom DNS resolvers. Which observable state is strongest?

- A. Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
- B. List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
- C. Read allowForwardedTraffic on both directional peering resources.
- D. Query the public IP zones array and the region's zone support.

## LAB17-Q30 — Applied

A hub-and-spoke network build review must prove the network peering ability to avoid assuming that connectivity automatically crosses a second peering hop. Which check avoids an adjacent feature?

- A. Query peeringState and peeringSyncLevel on both virtual networks.
- B. Inspect effective routes from the source and test the exact destination path.
- C. Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
- D. Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.

## LAB17-Q31 — Applied

A hub-and-spoke network build query surprises the network administrator connecting hub and spoke address spaces during the network peering attempt to connect networks without overlapping their address ranges. Which finding explains it?

- A. The proposed subnet prefix overlaps an existing application subnet.
- B. A Standard public IP is attached, but no NSG rule allows the intended inbound flow.
- C. The two virtual networks contain overlapping prefixes.
- D. The topology assumes two peering hops provide automatic transitive routing.

## LAB17-Q32 — Applied

Other hub-and-spoke network build components are healthy, but the network peering still cannot reserve subnet ranges that do not collide with future network segments. Which state causes the isolated failure?

- A. Only one directional peering object was created.
- B. A dynamic allocation was selected for an address consumed by an external allowlist.
- C. The proposed subnet prefix overlaps an existing application subnet.
- D. The two virtual networks contain overlapping prefixes.

## LAB17-Q33 — Applied

During a network peering fault drill, the hub-and-spoke network build does not create both directional control-plane links required for connected networks. Which finding identifies the defect?

- A. Both sides attempt to use a remote gateway, which is not a valid transit relationship.
- B. Only one directional peering object was created.
- C. A zonal frontend address is bound to a design that expects zone-redundant availability.
- D. The proposed subnet prefix overlaps an existing application subnet.

## LAB17-Q34 — Applied

The hub-and-spoke network build setup finishes, yet the network peering cannot let a spoke use a hub gateway only when both peering sides permit it. Which misconfiguration explains the mismatch?

- A. Both sides attempt to use a remote gateway, which is not a valid transit relationship.
- B. An NVA forwards packets, but the receiving peering blocks forwarded traffic.
- C. The configured DNS server address is not reachable from the workload subnet.
- D. Only one directional peering object was created.

## LAB17-Q35 — Applied

A network peering break/fix in the hub-and-spoke network build fails when operators try to carry forwarded packets from an NVA across connected networks. Which diagnosis fits?

- A. A Standard public IP is attached, but no NSG rule allows the intended inbound flow.
- B. An NVA forwards packets, but the receiving peering blocks forwarded traffic.
- C. The topology assumes two peering hops provide automatic transitive routing.
- D. Both sides attempt to use a remote gateway, which is not a valid transit relationship.

## LAB17-Q36 — Applied

The hub-and-spoke network build troubleshooting scope is the network peering need to use the production public-address SKU with secure defaults. Which condition should be corrected first?

- A. A dynamic allocation was selected for an address consumed by an external allowlist.
- B. The two virtual networks contain overlapping prefixes.
- C. An NVA forwards packets, but the receiving peering blocks forwarded traffic.
- D. A Standard public IP is attached, but no NSG rule allows the intended inbound flow.

## LAB17-Q37 — Applied

The hub-and-spoke network build result is partial because the network peering cannot keep the assigned public address stable across resource restarts. Which condition accounts for that result?

- A. A dynamic allocation was selected for an address consumed by an external allowlist.
- B. A zonal frontend address is bound to a design that expects zone-redundant availability.
- C. The proposed subnet prefix overlaps an existing application subnet.
- D. A Standard public IP is attached, but no NSG rule allows the intended inbound flow.

## LAB17-Q38 — Applied

The network peering evidence shows the hub-and-spoke network build cannot pin a public address to the intended availability-zone design. Which root cause fits that evidence?

- A. The configured DNS server address is not reachable from the workload subnet.
- B. A zonal frontend address is bound to a design that expects zone-redundant availability.
- C. Only one directional peering object was created.
- D. A dynamic allocation was selected for an address consumed by an external allowlist.

## LAB17-Q39 — Applied

Although the hub-and-spoke network build is meant to let the network peering make virtual machines use approved custom DNS resolvers, its checkpoint fails. Which network peering defect explains the failure?

- A. The configured DNS server address is not reachable from the workload subnet.
- B. The topology assumes two peering hops provide automatic transitive routing.
- C. Both sides attempt to use a remote gateway, which is not a valid transit relationship.
- D. A zonal frontend address is bound to a design that expects zone-redundant availability.

## LAB17-Q40 — Applied

The network peering support team isolated the hub-and-spoke network build incident to the attempt to avoid assuming that connectivity automatically crosses a second peering hop. Which condition prevents success?

- A. The two virtual networks contain overlapping prefixes.
- B. The topology assumes two peering hops provide automatic transitive routing.
- C. An NVA forwards packets, but the receiving peering blocks forwarded traffic.
- D. The configured DNS server address is not reachable from the workload subnet.

## LAB17-Q41 — Advanced

The hub-and-spoke network build runbook separates network peering mutation from validation while it must connect networks without overlapping their address ranges. Which sequence proves it cleanly?

- A. First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
- B. First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
- C. First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
- D. First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.

## LAB17-Q42 — Advanced

The hub-and-spoke network build checkpoint requires both this network peering outcome—reserve subnet ranges that do not collide with future network segments—and a read-only hub-and-spoke network build state check. Which network peering response is complete?

- A. First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.
- B. First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.
- C. First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
- D. First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.

## LAB17-Q43 — Advanced

The hub-and-spoke network build runbook must create both directional control-plane links required for connected networks, then retain network peering read-back evidence. Which hub-and-spoke network build pair completes both duties?

- A. First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.
- B. First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
- C. First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
- D. First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.

## LAB17-Q44 — Advanced

To satisfy the network peering requirement, operators must change the hub-and-spoke network build configuration and prove it can let a spoke use a hub gateway only when both peering sides permit it. Which sequence is coherent?

- A. First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
- B. First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.
- C. First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
- D. First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.

## LAB17-Q45 — Advanced

The network administrator connecting hub and spoke address spaces needs a safe hub-and-spoke network build change to carry forwarded packets from an NVA across connected networks, followed by network peering evidence. Which pair merits approval?

- A. First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
- B. First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
- C. First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.
- D. First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.

## LAB17-Q46 — Advanced

The hub-and-spoke network build has two network peering gates: use the production public-address SKU with secure defaults, then prove the hub-and-spoke network build state. Which network peering sequence works?

- A. First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.
- B. First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
- C. First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
- D. First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.

## LAB17-Q47 — Advanced

Which network peering path makes the hub-and-spoke network build able to keep the assigned public address stable across resource restarts, then inspects the defining properties?

- A. First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
- B. First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
- C. First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
- D. First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.

## LAB17-Q48 — Advanced

At the hub-and-spoke network build approval gate, operators must show that the network peering can pin a public address to the intended availability-zone design. Which network peering configure-and-check pair is defensible?

- A. First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.
- B. First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.
- C. First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.
- D. First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.

## LAB17-Q49 — Advanced

The hub-and-spoke network build forbids a partial network peering result. Operators must first make virtual machines use approved custom DNS resolvers and afterward confirm the hub-and-spoke network build outcome. Which network peering sequence is complete?

- A. First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
- B. First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.
- C. First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
- D. First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.

## LAB17-Q50 — Advanced

Only the hub-and-spoke network build change needed to avoid assuming that connectivity automatically crosses a second peering hop is allowed, and network peering proof is mandatory. Which pair fits?

- A. First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
- B. First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
- C. First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.
- D. First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.

[Open the answer key](./ANSWERS.md)
