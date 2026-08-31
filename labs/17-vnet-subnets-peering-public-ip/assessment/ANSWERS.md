# Lab 17 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB17-Q01 — A

**Question:** The hub-and-spoke network build handoff omits the network peering rule needed to connect networks without overlapping their address ranges. Which statement should the team add?

- **A — Correct.** Peered virtual networks require nonoverlapping IP address spaces for routable connectivity.
  Peered virtual networks require nonoverlapping IP address spaces for routable connectivity. For hub-and-spoke network build, nonoverlapping address spaces supplies the service rule needed to connect networks without overlapping their address ranges.
- **B — Incorrect.** Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network.
  Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network. In the hub-and-spoke network build, this statement describes subnet address planning. The subnet address planning statement accurately describes subnet address planning; however, hub-and-spoke network build needs nonoverlapping address spaces to connect networks without overlapping their address ranges; subnet address planning cannot replace nonoverlapping address spaces.
- **C — Incorrect.** The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
  The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering. In the hub-and-spoke network build, this statement describes forwarded traffic on peering. Selecting forwarded traffic on peering for hub-and-spoke network build leaves nonoverlapping address spaces unanswered in hub-and-spoke network build; the hub-and-spoke network build lacks a nonoverlapping address spaces basis to connect networks without overlapping their address ranges.
- **D — Incorrect.** A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design.
  A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design. In the hub-and-spoke network build, this statement describes zonal public IP configuration. Nonoverlapping address spaces governs hub-and-spoke network build; zonal public IP configuration cannot support nonoverlapping address spaces when operators must connect networks without overlapping their address ranges.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q02 — A

**Question:** A network peering incident review of the hub-and-spoke network build depends on the ability to reserve subnet ranges that do not collide with future network segments. Which platform description is reliable?

- **A — Correct.** Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network.
  Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network. In the hub-and-spoke network build, this subnet address planning rule supports the need to reserve subnet ranges that do not collide with future network segments.
- **B — Incorrect.** A usable virtual-network peering relationship has one peering resource in each direction.
  A usable virtual-network peering relationship has one peering resource in each direction. In the hub-and-spoke network build, this statement describes bidirectional peering objects. Selecting bidirectional peering objects for hub-and-spoke network build leaves subnet address planning unanswered in hub-and-spoke network build; the hub-and-spoke network build lacks a subnet address planning basis to reserve subnet ranges that do not collide with future network segments.
- **C — Incorrect.** Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource.
  Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource. In the hub-and-spoke network build, this statement describes Standard public IP SKU. Subnet address planning governs hub-and-spoke network build; Standard public IP SKU cannot support subnet address planning when operators must reserve subnet ranges that do not collide with future network segments.
- **D — Incorrect.** Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable.
  Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable. In the hub-and-spoke network build, this statement describes custom virtual-network DNS servers. Hub-and-spoke network build asks about subnet address planning; this custom virtual-network DNS servers choice leaves the subnet address planning explanation missing.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q03 — C

**Question:** A network administrator connecting hub and spoke address spaces is updating the network peering runbook. The requirement is to create both directional control-plane links required for connected networks. Which statement describes Azure behavior correctly?

- **A — Incorrect.** Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints.
  Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints. In the hub-and-spoke network build, this statement describes gateway transit peering. Selecting gateway transit peering for hub-and-spoke network build leaves bidirectional peering objects unanswered in hub-and-spoke network build; the hub-and-spoke network build lacks a bidirectional peering objects basis to create both directional control-plane links required for connected networks.
- **B — Incorrect.** A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior.
  A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior. In the hub-and-spoke network build, this statement describes static public IP allocation. Bidirectional peering objects governs hub-and-spoke network build; static public IP allocation cannot support bidirectional peering objects when operators must create both directional control-plane links required for connected networks.
- **C — Correct.** A usable virtual-network peering relationship has one peering resource in each direction.
  For the hub-and-spoke network build, the rule for bidirectional peering objects is defined by this statement: a usable virtual-network peering relationship has one peering resource in each direction. It supports the required outcome to create both directional control-plane links required for connected networks.
- **D — Incorrect.** Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C.
  Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C. In the hub-and-spoke network build, this statement describes nontransitive peering. The nontransitive peering statement accurately describes nontransitive peering; however, hub-and-spoke network build needs bidirectional peering objects to create both directional control-plane links required for connected networks; nontransitive peering cannot replace bidirectional peering objects.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q04 — C

**Question:** A network peering peer review asks how the hub-and-spoke network build should handle this outcome: let a spoke use a hub gateway only when both peering sides permit it. Which explanation is accurate?

- **A — Incorrect.** The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
  The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering. In the hub-and-spoke network build, this statement describes forwarded traffic on peering. Gateway transit peering governs hub-and-spoke network build; forwarded traffic on peering cannot support gateway transit peering when operators must let a spoke use a hub gateway only when both peering sides permit it.
- **B — Incorrect.** A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design.
  A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design. In the hub-and-spoke network build, this statement describes zonal public IP configuration. Hub-and-spoke network build asks about gateway transit peering; this zonal public IP configuration choice leaves the gateway transit peering explanation missing.
- **C — Correct.** Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints.
  Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints. The hub-and-spoke network build applies that gateway transit peering boundary when operators must let a spoke use a hub gateway only when both peering sides permit it.
- **D — Incorrect.** Peered virtual networks require nonoverlapping IP address spaces for routable connectivity.
  Peered virtual networks require nonoverlapping IP address spaces for routable connectivity. In the hub-and-spoke network build, this statement describes nonoverlapping address spaces. Selecting nonoverlapping address spaces for hub-and-spoke network build leaves gateway transit peering unanswered in hub-and-spoke network build; the hub-and-spoke network build lacks a gateway transit peering basis to let a spoke use a hub gateway only when both peering sides permit it.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q05 — A

**Question:** For the hub-and-spoke network build, the network peering plan must carry forwarded packets from an NVA across connected networks. Which statement about network peering belongs in the hub-and-spoke network build record?

- **A — Correct.** The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
  The hub-and-spoke network build needs forwarded traffic on peering to carry forwarded packets from an NVA across connected networks; this option states the applicable forwarded traffic on peering rule: the allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
- **B — Incorrect.** Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource.
  Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource. In the hub-and-spoke network build, this statement describes Standard public IP SKU. The Standard public IP SKU statement accurately describes Standard public IP SKU; however, hub-and-spoke network build needs forwarded traffic on peering to carry forwarded packets from an NVA across connected networks; Standard public IP SKU cannot replace forwarded traffic on peering.
- **C — Incorrect.** Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable.
  Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable. In the hub-and-spoke network build, this statement describes custom virtual-network DNS servers. Selecting custom virtual-network DNS servers for hub-and-spoke network build leaves forwarded traffic on peering unanswered in hub-and-spoke network build; the hub-and-spoke network build lacks a forwarded traffic on peering basis to carry forwarded packets from an NVA across connected networks.
- **D — Incorrect.** Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network.
  Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network. In the hub-and-spoke network build, this statement describes subnet address planning. Forwarded traffic on peering governs hub-and-spoke network build; subnet address planning cannot support forwarded traffic on peering when operators must carry forwarded packets from an NVA across connected networks.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q06 — B

**Question:** The network peering review compares four claims for the hub-and-spoke network build requirement to use the production public-address SKU with secure defaults. Which claim is technically sound?

- **A — Incorrect.** A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior.
  A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior. In the hub-and-spoke network build, this statement describes static public IP allocation. The static public IP allocation statement accurately describes static public IP allocation; however, hub-and-spoke network build needs Standard public IP SKU to use the production public-address SKU with secure defaults; static public IP allocation cannot replace Standard public IP SKU.
- **B — Correct.** Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource.
  Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource. This Standard public IP SKU fact resolves the hub-and-spoke network build design question about how to use the production public-address SKU with secure defaults.
- **C — Incorrect.** Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C.
  Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C. In the hub-and-spoke network build, this statement describes nontransitive peering. Standard public IP SKU governs hub-and-spoke network build; nontransitive peering cannot support Standard public IP SKU when operators must use the production public-address SKU with secure defaults.
- **D — Incorrect.** A usable virtual-network peering relationship has one peering resource in each direction.
  A usable virtual-network peering relationship has one peering resource in each direction. In the hub-and-spoke network build, this statement describes bidirectional peering objects. Hub-and-spoke network build asks about Standard public IP SKU; this bidirectional peering objects choice leaves the Standard public IP SKU explanation missing.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q07 — C

**Question:** The network peering architecture note requires the hub-and-spoke network build environment to keep the assigned public address stable across resource restarts. Which statement defines the relevant network peering boundary?

- **A — Incorrect.** A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design.
  A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design. In the hub-and-spoke network build, this statement describes zonal public IP configuration. Selecting zonal public IP configuration for hub-and-spoke network build leaves static public IP allocation unanswered in hub-and-spoke network build; the hub-and-spoke network build lacks a static public IP allocation basis to keep the assigned public address stable across resource restarts.
- **B — Incorrect.** Peered virtual networks require nonoverlapping IP address spaces for routable connectivity.
  Peered virtual networks require nonoverlapping IP address spaces for routable connectivity. In the hub-and-spoke network build, this statement describes nonoverlapping address spaces. Static public IP allocation governs hub-and-spoke network build; nonoverlapping address spaces cannot support static public IP allocation when operators must keep the assigned public address stable across resource restarts.
- **C — Correct.** A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior.
  A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior. For hub-and-spoke network build, static public IP allocation supplies the service rule needed to keep the assigned public address stable across resource restarts.
- **D — Incorrect.** Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints.
  Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints. In the hub-and-spoke network build, this statement describes gateway transit peering. The gateway transit peering statement accurately describes gateway transit peering; however, hub-and-spoke network build needs static public IP allocation to keep the assigned public address stable across resource restarts; gateway transit peering cannot replace static public IP allocation.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q08 — D

**Question:** A new network peering operator must explain why the hub-and-spoke network build can pin a public address to the intended availability-zone design. Which explanation is accurate?

- **A — Incorrect.** Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable.
  Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable. In the hub-and-spoke network build, this statement describes custom virtual-network DNS servers. Zonal public IP configuration governs hub-and-spoke network build; custom virtual-network DNS servers cannot support zonal public IP configuration when operators must pin a public address to the intended availability-zone design.
- **B — Incorrect.** Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network.
  Each subnet prefix must fit inside its virtual network address space and cannot overlap another subnet in that network. In the hub-and-spoke network build, this statement describes subnet address planning. Hub-and-spoke network build asks about zonal public IP configuration; this subnet address planning choice leaves the zonal public IP configuration explanation missing.
- **C — Incorrect.** The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering.
  The allowForwardedTraffic setting controls whether traffic forwarded by a network virtual appliance can cross a peering. In the hub-and-spoke network build, this statement describes forwarded traffic on peering. The forwarded traffic on peering statement accurately describes forwarded traffic on peering; however, hub-and-spoke network build needs zonal public IP configuration to pin a public address to the intended availability-zone design; forwarded traffic on peering cannot replace zonal public IP configuration.
- **D — Correct.** A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design.
  A Standard public IP can be zone-redundant or zonal in supported regions, and its zone choice must fit the attached resource design. In the hub-and-spoke network build, this zonal public IP configuration rule supports the need to pin a public address to the intended availability-zone design.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q09 — D

**Question:** The hub-and-spoke network build acceptance criteria require operators to make virtual machines use approved custom DNS resolvers. Which service fact supports that requirement?

- **A — Incorrect.** Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C.
  Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C. In the hub-and-spoke network build, this statement describes nontransitive peering. Hub-and-spoke network build asks about custom virtual-network DNS servers; this nontransitive peering choice leaves the custom virtual-network DNS servers explanation missing.
- **B — Incorrect.** A usable virtual-network peering relationship has one peering resource in each direction.
  A usable virtual-network peering relationship has one peering resource in each direction. In the hub-and-spoke network build, this statement describes bidirectional peering objects. The bidirectional peering objects statement accurately describes bidirectional peering objects; however, hub-and-spoke network build needs custom virtual-network DNS servers to make virtual machines use approved custom DNS resolvers; bidirectional peering objects cannot replace custom virtual-network DNS servers.
- **C — Incorrect.** Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource.
  Standard public IP addresses are secure by default and require an NSG rule to permit inbound traffic to an attached resource. In the hub-and-spoke network build, this statement describes Standard public IP SKU. Selecting Standard public IP SKU for hub-and-spoke network build leaves custom virtual-network DNS servers unanswered in hub-and-spoke network build; the hub-and-spoke network build lacks a custom virtual-network DNS servers basis to make virtual machines use approved custom DNS resolvers.
- **D — Correct.** Custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable.
  For the hub-and-spoke network build, the rule for custom virtual-network DNS servers is defined by this statement: custom DNS server addresses configured on a virtual network are inherited by attached interfaces after renewal, and the DNS servers must be reachable. It supports the required outcome to make virtual machines use approved custom DNS resolvers.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network name resolution](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances)

**Source reviewed:** 2026-08-31

## LAB17-Q10 — D

**Question:** A network peering reviewer challenges whether the hub-and-spoke network build can avoid assuming that connectivity automatically crosses a second peering hop. Which response resolves the concern?

- **A — Incorrect.** Peered virtual networks require nonoverlapping IP address spaces for routable connectivity.
  Peered virtual networks require nonoverlapping IP address spaces for routable connectivity. In the hub-and-spoke network build, this statement describes nonoverlapping address spaces. The nonoverlapping address spaces statement accurately describes nonoverlapping address spaces; however, hub-and-spoke network build needs nontransitive peering to avoid assuming that connectivity automatically crosses a second peering hop; nonoverlapping address spaces cannot replace nontransitive peering.
- **B — Incorrect.** Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints.
  Gateway transit requires one side to allow gateway transit and the other to use the remote gateway, with topology constraints. In the hub-and-spoke network build, this statement describes gateway transit peering. Selecting gateway transit peering for hub-and-spoke network build leaves nontransitive peering unanswered in hub-and-spoke network build; the hub-and-spoke network build lacks a nontransitive peering basis to avoid assuming that connectivity automatically crosses a second peering hop.
- **C — Incorrect.** A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior.
  A static public IP retains its assigned address while the resource exists, subject to platform lifecycle behavior. In the hub-and-spoke network build, this statement describes static public IP allocation. Nontransitive peering governs hub-and-spoke network build; static public IP allocation cannot support nontransitive peering when operators must avoid assuming that connectivity automatically crosses a second peering hop.
- **D — Correct.** Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C.
  Virtual-network peering is not transitive; peering A to B and B to C does not automatically connect A to C. The hub-and-spoke network build applies that nontransitive peering boundary when operators must avoid assuming that connectivity automatically crosses a second peering hop.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q11 — C

**Question:** The network peering preflight has passed; the hub-and-spoke network build must now connect networks without overlapping their address ranges. Which operation should run?

- **A — Incorrect.** Create and validate both local-to-remote and remote-to-local peering objects.
  Create and validate both local-to-remote and remote-to-local peering objects. In the hub-and-spoke network build, this action changes bidirectional peering objects. Hub-and-spoke network build approved nonoverlapping address spaces, not bidirectional peering objects; only the nonoverlapping address spaces change can connect networks without overlapping their address ranges.
- **B — Incorrect.** Use Standard SKU and add only the required inbound NSG exposure.
  Use Standard SKU and add only the required inbound NSG exposure. In the hub-and-spoke network build, this action changes Standard public IP SKU. Hub-and-spoke network build requires nonoverlapping address spaces; changing Standard public IP SKU leaves nonoverlapping address spaces absent in hub-and-spoke network build; hub-and-spoke network build cannot connect networks without overlapping their address ranges.
- **C — Correct.** Allocate approved RFC 1918 ranges and check them against existing and planned connected networks.
  The hub-and-spoke network build must connect networks without overlapping their address ranges; this option performs its direct nonoverlapping address spaces change: allocate approved RFC 1918 ranges and check them against existing and planned connected networks.
- **D — Incorrect.** Configure approved resolver IP addresses and renew affected clients when required.
  Configure approved resolver IP addresses and renew affected clients when required. In the hub-and-spoke network build, this action changes custom virtual-network DNS servers. Hub-and-spoke network build instead needs nonoverlapping address spaces: Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. The custom virtual-network DNS servers action omits that nonoverlapping address spaces work.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q12 — B

**Question:** The hub-and-spoke network build plan must reserve subnet ranges that do not collide with future network segments while limiting the mutation scope to network peering. Which action is appropriate?

- **A — Incorrect.** Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects.
  Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. In the hub-and-spoke network build, this action changes gateway transit peering. Hub-and-spoke network build requires subnet address planning; changing gateway transit peering leaves subnet address planning absent in hub-and-spoke network build; hub-and-spoke network build cannot reserve subnet ranges that do not collide with future network segments.
- **B — Correct.** Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets.
  Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. It is the least-change subnet address planning path for the hub-and-spoke network build requirement to reserve subnet ranges that do not collide with future network segments.
- **C — Incorrect.** Use static allocation when DNS or allowlists require a stable public address.
  Use static allocation when DNS or allowlists require a stable public address. In the hub-and-spoke network build, this action changes static public IP allocation. Hub-and-spoke network build instead needs subnet address planning: Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. The static public IP allocation action omits that subnet address planning work.
- **D — Incorrect.** Create the required direct peering or introduce an approved routed hub design.
  Create the required direct peering or introduce an approved routed hub design. In the hub-and-spoke network build, this action changes nontransitive peering. Hub-and-spoke network build approved subnet address planning, not nontransitive peering; only the subnet address planning change can reserve subnet ranges that do not collide with future network segments.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q13 — B

**Question:** A network peering ticket in the hub-and-spoke network build says to create both directional control-plane links required for connected networks. Which network peering action completes the hub-and-spoke network build request with minimal change?

- **A — Incorrect.** Enable forwarded traffic only on the peering directions required by the approved routing design.
  Enable forwarded traffic only on the peering directions required by the approved routing design. In the hub-and-spoke network build, this action changes forwarded traffic on peering. Forwarded traffic on peering does not implement bidirectional peering objects for hub-and-spoke network build; the hub-and-spoke network build still cannot create both directional control-plane links required for connected networks.
- **B — Correct.** Create and validate both local-to-remote and remote-to-local peering objects.
  Create and validate both local-to-remote and remote-to-local peering objects. In hub-and-spoke network build, applying bidirectional peering objects is the scoped way to create both directional control-plane links required for connected networks.
- **C — Incorrect.** Select zone-redundant placement for regional zonal resilience when supported.
  Select zone-redundant placement for regional zonal resilience when supported. In the hub-and-spoke network build, this action changes zonal public IP configuration. Hub-and-spoke network build approved bidirectional peering objects, not zonal public IP configuration; only the bidirectional peering objects change can create both directional control-plane links required for connected networks.
- **D — Incorrect.** Allocate approved RFC 1918 ranges and check them against existing and planned connected networks.
  Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. In the hub-and-spoke network build, this action changes nonoverlapping address spaces. Hub-and-spoke network build requires bidirectional peering objects; changing nonoverlapping address spaces leaves bidirectional peering objects absent in hub-and-spoke network build; hub-and-spoke network build cannot create both directional control-plane links required for connected networks.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q14 — D

**Question:** The approach for the hub-and-spoke network build is approved, but the network peering environment still cannot let a spoke use a hub gateway only when both peering sides permit it. Which implementation step closes the gap?

- **A — Incorrect.** Use Standard SKU and add only the required inbound NSG exposure.
  Use Standard SKU and add only the required inbound NSG exposure. In the hub-and-spoke network build, this action changes Standard public IP SKU. Hub-and-spoke network build instead needs gateway transit peering: Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. The Standard public IP SKU action omits that gateway transit peering work.
- **B — Incorrect.** Configure approved resolver IP addresses and renew affected clients when required.
  Configure approved resolver IP addresses and renew affected clients when required. In the hub-and-spoke network build, this action changes custom virtual-network DNS servers. Hub-and-spoke network build approved gateway transit peering, not custom virtual-network DNS servers; only the gateway transit peering change can let a spoke use a hub gateway only when both peering sides permit it.
- **C — Incorrect.** Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets.
  Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. In the hub-and-spoke network build, this action changes subnet address planning. Hub-and-spoke network build requires gateway transit peering; changing subnet address planning leaves gateway transit peering absent in hub-and-spoke network build; hub-and-spoke network build cannot let a spoke use a hub gateway only when both peering sides permit it.
- **D — Correct.** Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects.
  Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. The hub-and-spoke network build uses this gateway transit peering operation to let a spoke use a hub gateway only when both peering sides permit it within the approved scope.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q15 — A

**Question:** The network administrator connecting hub and spoke address spaces may change the hub-and-spoke network build only to carry forwarded packets from an NVA across connected networks. Which network peering action stays within that assignment?

- **A — Correct.** Enable forwarded traffic only on the peering directions required by the approved routing design.
  For the hub-and-spoke network build, the required forwarded traffic on peering action is: enable forwarded traffic only on the peering directions required by the approved routing design. It makes the environment able to carry forwarded packets from an NVA across connected networks.
- **B — Incorrect.** Use static allocation when DNS or allowlists require a stable public address.
  Use static allocation when DNS or allowlists require a stable public address. In the hub-and-spoke network build, this action changes static public IP allocation. Hub-and-spoke network build requires forwarded traffic on peering; changing static public IP allocation leaves forwarded traffic on peering absent in hub-and-spoke network build; hub-and-spoke network build cannot carry forwarded packets from an NVA across connected networks.
- **C — Incorrect.** Create the required direct peering or introduce an approved routed hub design.
  Create the required direct peering or introduce an approved routed hub design. In the hub-and-spoke network build, this action changes nontransitive peering. Nontransitive peering does not implement forwarded traffic on peering for hub-and-spoke network build; the hub-and-spoke network build still cannot carry forwarded packets from an NVA across connected networks.
- **D — Incorrect.** Create and validate both local-to-remote and remote-to-local peering objects.
  Create and validate both local-to-remote and remote-to-local peering objects. In the hub-and-spoke network build, this action changes bidirectional peering objects. Hub-and-spoke network build instead needs forwarded traffic on peering: Enable forwarded traffic only on the peering directions required by the approved routing design. The bidirectional peering objects action omits that forwarded traffic on peering work.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q16 — D

**Question:** A network peering dry run shows no hub-and-spoke network build command will use the production public-address SKU with secure defaults. Which action belongs before execution?

- **A — Incorrect.** Select zone-redundant placement for regional zonal resilience when supported.
  Select zone-redundant placement for regional zonal resilience when supported. In the hub-and-spoke network build, this action changes zonal public IP configuration. Hub-and-spoke network build requires Standard public IP SKU; changing zonal public IP configuration leaves Standard public IP SKU absent in hub-and-spoke network build; hub-and-spoke network build cannot use the production public-address SKU with secure defaults.
- **B — Incorrect.** Allocate approved RFC 1918 ranges and check them against existing and planned connected networks.
  Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. In the hub-and-spoke network build, this action changes nonoverlapping address spaces. Nonoverlapping address spaces does not implement Standard public IP SKU for hub-and-spoke network build; the hub-and-spoke network build still cannot use the production public-address SKU with secure defaults.
- **C — Incorrect.** Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects.
  Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. In the hub-and-spoke network build, this action changes gateway transit peering. Hub-and-spoke network build instead needs Standard public IP SKU: Use Standard SKU and add only the required inbound NSG exposure. The gateway transit peering action omits that Standard public IP SKU work.
- **D — Correct.** Use Standard SKU and add only the required inbound NSG exposure.
  Use Standard SKU and add only the required inbound NSG exposure. This changes Standard public IP SKU in the hub-and-spoke network build, supplying the missing state needed to use the production public-address SKU with secure defaults.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q17 — D

**Question:** For the hub-and-spoke network build, operators need to keep the assigned public address stable across resource restarts. Which change realizes that requirement?

- **A — Incorrect.** Configure approved resolver IP addresses and renew affected clients when required.
  Configure approved resolver IP addresses and renew affected clients when required. In the hub-and-spoke network build, this action changes custom virtual-network DNS servers. Custom virtual-network DNS servers does not implement static public IP allocation for hub-and-spoke network build; the hub-and-spoke network build still cannot keep the assigned public address stable across resource restarts.
- **B — Incorrect.** Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets.
  Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. In the hub-and-spoke network build, this action changes subnet address planning. Hub-and-spoke network build instead needs static public IP allocation: Use static allocation when DNS or allowlists require a stable public address. The subnet address planning action omits that static public IP allocation work.
- **C — Incorrect.** Enable forwarded traffic only on the peering directions required by the approved routing design.
  Enable forwarded traffic only on the peering directions required by the approved routing design. In the hub-and-spoke network build, this action changes forwarded traffic on peering. Hub-and-spoke network build approved static public IP allocation, not forwarded traffic on peering; only the static public IP allocation change can keep the assigned public address stable across resource restarts.
- **D — Correct.** Use static allocation when DNS or allowlists require a stable public address.
  The hub-and-spoke network build must keep the assigned public address stable across resource restarts; this option performs its direct static public IP allocation change: use static allocation when DNS or allowlists require a stable public address.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q18 — A

**Question:** Operators must automate the hub-and-spoke network build change needed to pin a public address to the intended availability-zone design. Which network peering operation belongs in the runbook?

- **A — Correct.** Select zone-redundant placement for regional zonal resilience when supported.
  Select zone-redundant placement for regional zonal resilience when supported. It is the least-change zonal public IP configuration path for the hub-and-spoke network build requirement to pin a public address to the intended availability-zone design.
- **B — Incorrect.** Create the required direct peering or introduce an approved routed hub design.
  Create the required direct peering or introduce an approved routed hub design. In the hub-and-spoke network build, this action changes nontransitive peering. Hub-and-spoke network build approved zonal public IP configuration, not nontransitive peering; only the zonal public IP configuration change can pin a public address to the intended availability-zone design.
- **C — Incorrect.** Create and validate both local-to-remote and remote-to-local peering objects.
  Create and validate both local-to-remote and remote-to-local peering objects. In the hub-and-spoke network build, this action changes bidirectional peering objects. Hub-and-spoke network build requires zonal public IP configuration; changing bidirectional peering objects leaves zonal public IP configuration absent in hub-and-spoke network build; hub-and-spoke network build cannot pin a public address to the intended availability-zone design.
- **D — Incorrect.** Use Standard SKU and add only the required inbound NSG exposure.
  Use Standard SKU and add only the required inbound NSG exposure. In the hub-and-spoke network build, this action changes Standard public IP SKU. Standard public IP SKU does not implement zonal public IP configuration for hub-and-spoke network build; the hub-and-spoke network build still cannot pin a public address to the intended availability-zone design.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q19 — D

**Question:** A hub-and-spoke network build review finds network peering drift from the need to make virtual machines use approved custom DNS resolvers. Which correction addresses that drift?

- **A — Incorrect.** Allocate approved RFC 1918 ranges and check them against existing and planned connected networks.
  Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. In the hub-and-spoke network build, this action changes nonoverlapping address spaces. Hub-and-spoke network build approved custom virtual-network DNS servers, not nonoverlapping address spaces; only the custom virtual-network DNS servers change can make virtual machines use approved custom DNS resolvers.
- **B — Incorrect.** Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects.
  Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. In the hub-and-spoke network build, this action changes gateway transit peering. Hub-and-spoke network build requires custom virtual-network DNS servers; changing gateway transit peering leaves custom virtual-network DNS servers absent in hub-and-spoke network build; hub-and-spoke network build cannot make virtual machines use approved custom DNS resolvers.
- **C — Incorrect.** Use static allocation when DNS or allowlists require a stable public address.
  Use static allocation when DNS or allowlists require a stable public address. In the hub-and-spoke network build, this action changes static public IP allocation. Static public IP allocation does not implement custom virtual-network DNS servers for hub-and-spoke network build; the hub-and-spoke network build still cannot make virtual machines use approved custom DNS resolvers.
- **D — Correct.** Configure approved resolver IP addresses and renew affected clients when required.
  Configure approved resolver IP addresses and renew affected clients when required. In hub-and-spoke network build, applying custom virtual-network DNS servers is the scoped way to make virtual machines use approved custom DNS resolvers.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network name resolution](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances)

**Source reviewed:** 2026-08-31

## LAB17-Q20 — A

**Question:** The hub-and-spoke network build window permits only the network peering change needed to avoid assuming that connectivity automatically crosses a second peering hop. Which option respects the boundary?

- **A — Correct.** Create the required direct peering or introduce an approved routed hub design.
  Create the required direct peering or introduce an approved routed hub design. The hub-and-spoke network build uses this nontransitive peering operation to avoid assuming that connectivity automatically crosses a second peering hop within the approved scope.
- **B — Incorrect.** Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets.
  Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. In the hub-and-spoke network build, this action changes subnet address planning. Subnet address planning does not implement nontransitive peering for hub-and-spoke network build; the hub-and-spoke network build still cannot avoid assuming that connectivity automatically crosses a second peering hop.
- **C — Incorrect.** Enable forwarded traffic only on the peering directions required by the approved routing design.
  Enable forwarded traffic only on the peering directions required by the approved routing design. In the hub-and-spoke network build, this action changes forwarded traffic on peering. Hub-and-spoke network build instead needs nontransitive peering: Create the required direct peering or introduce an approved routed hub design. The forwarded traffic on peering action omits that nontransitive peering work.
- **D — Incorrect.** Select zone-redundant placement for regional zonal resilience when supported.
  Select zone-redundant placement for regional zonal resilience when supported. In the hub-and-spoke network build, this action changes zonal public IP configuration. Hub-and-spoke network build approved nontransitive peering, not zonal public IP configuration; only the nontransitive peering change can avoid assuming that connectivity automatically crosses a second peering hop.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q21 — B

**Question:** The hub-and-spoke network build evidence bundle needs a network peering result showing it can connect networks without overlapping their address ranges. Which result belongs in the checkpoint?

- **A — Incorrect.** Query both peerings and confirm the gateway flags and connected state.
  Query both peerings and confirm the gateway flags and connected state. In the hub-and-spoke network build, this check observes gateway transit peering. Hub-and-spoke network build output covers gateway transit peering, not nonoverlapping address spaces; the nonoverlapping address spaces requirement to connect networks without overlapping their address ranges remains unverified.
- **B — Correct.** Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
  For the hub-and-spoke network build, this nonoverlapping address spaces observation is decisive: query every addressSpace.addressPrefixes value and prove no peered range overlaps. It is hub-and-spoke network build evidence that operators can connect networks without overlapping their address ranges.
- **C — Incorrect.** Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
  Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning. In the hub-and-spoke network build, this check observes static public IP allocation. Hub-and-spoke network build reads static public IP allocation, leaving nonoverlapping address spaces unproved in hub-and-spoke network build; hub-and-spoke network build still has no nonoverlapping address spaces proof.
- **D — Incorrect.** Inspect effective routes from the source and test the exact destination path.
  Inspect effective routes from the source and test the exact destination path. In the hub-and-spoke network build, this check observes nontransitive peering. Hub-and-spoke network build could pass nontransitive peering while nonoverlapping address spaces is wrong; hub-and-spoke network build still lacks nonoverlapping address spaces proof.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q22 — B

**Question:** Before hub-and-spoke network build cleanup, the network peering team must reconfirm it can reserve subnet ranges that do not collide with future network segments. Which read-only inspection should run?

- **A — Incorrect.** Read allowForwardedTraffic on both directional peering resources.
  Read allowForwardedTraffic on both directional peering resources. In the hub-and-spoke network build, this check observes forwarded traffic on peering. Forwarded traffic on peering success in hub-and-spoke network build cannot verify subnet address planning; hub-and-spoke network build cannot reserve subnet ranges that do not collide with future network segments until subnet address planning evidence exists.
- **B — Correct.** List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
  List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses. Because the hub-and-spoke network build check observes subnet address planning, it independently verifies the requirement to reserve subnet ranges that do not collide with future network segments.
- **C — Incorrect.** Query the public IP zones array and the region's zone support.
  Query the public IP zones array and the region's zone support. In the hub-and-spoke network build, this check observes zonal public IP configuration. Hub-and-spoke network build could pass zonal public IP configuration while subnet address planning is wrong; hub-and-spoke network build still lacks subnet address planning proof.
- **D — Incorrect.** Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
  Query every addressSpace.addressPrefixes value and prove no peered range overlaps. In the hub-and-spoke network build, this check observes nonoverlapping address spaces. Hub-and-spoke network build output covers nonoverlapping address spaces, not subnet address planning; the subnet address planning requirement to reserve subnet ranges that do not collide with future network segments remains unverified.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q23 — B

**Question:** The hub-and-spoke network build setup reports success after the network peering attempt to create both directional control-plane links required for connected networks. Which network peering read-only observation proves the hub-and-spoke network build outcome?

- **A — Incorrect.** Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
  Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration. In the hub-and-spoke network build, this check observes Standard public IP SKU. Hub-and-spoke network build reads Standard public IP SKU, leaving bidirectional peering objects unproved in hub-and-spoke network build; hub-and-spoke network build still has no bidirectional peering objects proof.
- **B — Correct.** Query peeringState and peeringSyncLevel on both virtual networks.
  The hub-and-spoke network build validator needs this bidirectional peering objects result: query peeringState and peeringSyncLevel on both virtual networks. It proves the outcome to create both directional control-plane links required for connected networks rather than an adjacent checkpoint.
- **C — Incorrect.** Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
  Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration. In the hub-and-spoke network build, this check observes custom virtual-network DNS servers. Hub-and-spoke network build output covers custom virtual-network DNS servers, not bidirectional peering objects; the bidirectional peering objects requirement to create both directional control-plane links required for connected networks remains unverified.
- **D — Incorrect.** List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
  List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses. In the hub-and-spoke network build, this check observes subnet address planning. Subnet address planning success in hub-and-spoke network build cannot verify bidirectional peering objects; hub-and-spoke network build cannot create both directional control-plane links required for connected networks until bidirectional peering objects evidence exists.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q24 — D

**Question:** The network peering log says the hub-and-spoke network build can now let a spoke use a hub gateway only when both peering sides permit it. Which network peering state should the hub-and-spoke network build acceptance test retain?

- **A — Incorrect.** Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
  Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning. In the hub-and-spoke network build, this check observes static public IP allocation. Hub-and-spoke network build could pass static public IP allocation while gateway transit peering is wrong; hub-and-spoke network build still lacks gateway transit peering proof.
- **B — Incorrect.** Inspect effective routes from the source and test the exact destination path.
  Inspect effective routes from the source and test the exact destination path. In the hub-and-spoke network build, this check observes nontransitive peering. Hub-and-spoke network build output covers nontransitive peering, not gateway transit peering; the gateway transit peering requirement to let a spoke use a hub gateway only when both peering sides permit it remains unverified.
- **C — Incorrect.** Query peeringState and peeringSyncLevel on both virtual networks.
  Query peeringState and peeringSyncLevel on both virtual networks. In the hub-and-spoke network build, this check observes bidirectional peering objects. Bidirectional peering objects success in hub-and-spoke network build cannot verify gateway transit peering; hub-and-spoke network build cannot let a spoke use a hub gateway only when both peering sides permit it until gateway transit peering evidence exists.
- **D — Correct.** Query both peerings and confirm the gateway flags and connected state.
  Query both peerings and confirm the gateway flags and connected state. This is independent gateway transit peering evidence for the hub-and-spoke network build, even if hub-and-spoke network build setup reports success before gateway transit peering becomes observable.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q25 — D

**Question:** The hub-and-spoke network build rejects network peering exit status as proof it can carry forwarded packets from an NVA across connected networks. Which hub-and-spoke network build result is valid evidence?

- **A — Incorrect.** Query the public IP zones array and the region's zone support.
  Query the public IP zones array and the region's zone support. In the hub-and-spoke network build, this check observes zonal public IP configuration. Hub-and-spoke network build output covers zonal public IP configuration, not forwarded traffic on peering; the forwarded traffic on peering requirement to carry forwarded packets from an NVA across connected networks remains unverified.
- **B — Incorrect.** Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
  Query every addressSpace.addressPrefixes value and prove no peered range overlaps. In the hub-and-spoke network build, this check observes nonoverlapping address spaces. Nonoverlapping address spaces success in hub-and-spoke network build cannot verify forwarded traffic on peering; hub-and-spoke network build cannot carry forwarded packets from an NVA across connected networks until forwarded traffic on peering evidence exists.
- **C — Incorrect.** Query both peerings and confirm the gateway flags and connected state.
  Query both peerings and confirm the gateway flags and connected state. In the hub-and-spoke network build, this check observes gateway transit peering. Hub-and-spoke network build reads gateway transit peering, leaving forwarded traffic on peering unproved in hub-and-spoke network build; hub-and-spoke network build still has no forwarded traffic on peering proof.
- **D — Correct.** Read allowForwardedTraffic on both directional peering resources.
  Read allowForwardedTraffic on both directional peering resources. For hub-and-spoke network build, this forwarded traffic on peering read confirms the service can carry forwarded packets from an NVA across connected networks.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q26 — C

**Question:** The network peering validator needs one hub-and-spoke network build query after the change to use the production public-address SKU with secure defaults. Which network peering property should the hub-and-spoke network build validator inspect?

- **A — Incorrect.** Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
  Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration. In the hub-and-spoke network build, this check observes custom virtual-network DNS servers. Custom virtual-network DNS servers success in hub-and-spoke network build cannot verify Standard public IP SKU; hub-and-spoke network build cannot use the production public-address SKU with secure defaults until Standard public IP SKU evidence exists.
- **B — Incorrect.** List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
  List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses. In the hub-and-spoke network build, this check observes subnet address planning. Hub-and-spoke network build reads subnet address planning, leaving Standard public IP SKU unproved in hub-and-spoke network build; hub-and-spoke network build still has no Standard public IP SKU proof.
- **C — Correct.** Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
  Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration. The hub-and-spoke network build reads Standard public IP SKU directly; that Standard public IP SKU result proves the hub-and-spoke network build can use the production public-address SKU with secure defaults without another mutation.
- **D — Incorrect.** Read allowForwardedTraffic on both directional peering resources.
  Read allowForwardedTraffic on both directional peering resources. In the hub-and-spoke network build, this check observes forwarded traffic on peering. Hub-and-spoke network build output covers forwarded traffic on peering, not Standard public IP SKU; the Standard public IP SKU requirement to use the production public-address SKU with secure defaults remains unverified.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q27 — B

**Question:** The network administrator connecting hub and spoke address spaces must confirm the hub-and-spoke network build, without mutation, can keep the assigned public address stable across resource restarts. Which network peering check qualifies?

- **A — Incorrect.** Inspect effective routes from the source and test the exact destination path.
  Inspect effective routes from the source and test the exact destination path. In the hub-and-spoke network build, this check observes nontransitive peering. Hub-and-spoke network build reads nontransitive peering, leaving static public IP allocation unproved in hub-and-spoke network build; hub-and-spoke network build still has no static public IP allocation proof.
- **B — Correct.** Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
  For the hub-and-spoke network build, this static public IP allocation observation is decisive: query publicIPAllocationMethod and persist the assigned ipAddress after provisioning. It is hub-and-spoke network build evidence that operators can keep the assigned public address stable across resource restarts.
- **C — Incorrect.** Query peeringState and peeringSyncLevel on both virtual networks.
  Query peeringState and peeringSyncLevel on both virtual networks. In the hub-and-spoke network build, this check observes bidirectional peering objects. Hub-and-spoke network build output covers bidirectional peering objects, not static public IP allocation; the static public IP allocation requirement to keep the assigned public address stable across resource restarts remains unverified.
- **D — Incorrect.** Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
  Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration. In the hub-and-spoke network build, this check observes Standard public IP SKU. Standard public IP SKU success in hub-and-spoke network build cannot verify static public IP allocation; hub-and-spoke network build cannot keep the assigned public address stable across resource restarts until static public IP allocation evidence exists.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q28 — A

**Question:** The hub-and-spoke network build configuration is complete; the network peering reviewers need evidence it can pin a public address to the intended availability-zone design. Which observation shows success?

- **A — Correct.** Query the public IP zones array and the region's zone support.
  Query the public IP zones array and the region's zone support. Because the hub-and-spoke network build check observes zonal public IP configuration, it independently verifies the requirement to pin a public address to the intended availability-zone design.
- **B — Incorrect.** Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
  Query every addressSpace.addressPrefixes value and prove no peered range overlaps. In the hub-and-spoke network build, this check observes nonoverlapping address spaces. Hub-and-spoke network build output covers nonoverlapping address spaces, not zonal public IP configuration; the zonal public IP configuration requirement to pin a public address to the intended availability-zone design remains unverified.
- **C — Incorrect.** Query both peerings and confirm the gateway flags and connected state.
  Query both peerings and confirm the gateway flags and connected state. In the hub-and-spoke network build, this check observes gateway transit peering. Gateway transit peering success in hub-and-spoke network build cannot verify zonal public IP configuration; hub-and-spoke network build cannot pin a public address to the intended availability-zone design until zonal public IP configuration evidence exists.
- **D — Incorrect.** Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
  Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning. In the hub-and-spoke network build, this check observes static public IP allocation. Hub-and-spoke network build reads static public IP allocation, leaving zonal public IP configuration unproved in hub-and-spoke network build; hub-and-spoke network build still has no zonal public IP configuration proof.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q29 — A

**Question:** The network peering validation asks whether the hub-and-spoke network build can make virtual machines use approved custom DNS resolvers. Which observable state is strongest?

- **A — Correct.** Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
  The hub-and-spoke network build validator needs this custom virtual-network DNS servers result: query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration. It proves the outcome to make virtual machines use approved custom DNS resolvers rather than an adjacent checkpoint.
- **B — Incorrect.** List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
  List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses. In the hub-and-spoke network build, this check observes subnet address planning. Subnet address planning success in hub-and-spoke network build cannot verify custom virtual-network DNS servers; hub-and-spoke network build cannot make virtual machines use approved custom DNS resolvers until custom virtual-network DNS servers evidence exists.
- **C — Incorrect.** Read allowForwardedTraffic on both directional peering resources.
  Read allowForwardedTraffic on both directional peering resources. In the hub-and-spoke network build, this check observes forwarded traffic on peering. Hub-and-spoke network build reads forwarded traffic on peering, leaving custom virtual-network DNS servers unproved in hub-and-spoke network build; hub-and-spoke network build still has no custom virtual-network DNS servers proof.
- **D — Incorrect.** Query the public IP zones array and the region's zone support.
  Query the public IP zones array and the region's zone support. In the hub-and-spoke network build, this check observes zonal public IP configuration. Hub-and-spoke network build could pass zonal public IP configuration while custom virtual-network DNS servers is wrong; hub-and-spoke network build still lacks custom virtual-network DNS servers proof.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network name resolution](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances)

**Source reviewed:** 2026-08-31

## LAB17-Q30 — B

**Question:** A hub-and-spoke network build review must prove the network peering ability to avoid assuming that connectivity automatically crosses a second peering hop. Which check avoids an adjacent feature?

- **A — Incorrect.** Query peeringState and peeringSyncLevel on both virtual networks.
  Query peeringState and peeringSyncLevel on both virtual networks. In the hub-and-spoke network build, this check observes bidirectional peering objects. Bidirectional peering objects success in hub-and-spoke network build cannot verify nontransitive peering; hub-and-spoke network build cannot avoid assuming that connectivity automatically crosses a second peering hop until nontransitive peering evidence exists.
- **B — Correct.** Inspect effective routes from the source and test the exact destination path.
  Inspect effective routes from the source and test the exact destination path. This is independent nontransitive peering evidence for the hub-and-spoke network build, even if hub-and-spoke network build setup reports success before nontransitive peering becomes observable.
- **C — Incorrect.** Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
  Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration. In the hub-and-spoke network build, this check observes Standard public IP SKU. Hub-and-spoke network build could pass Standard public IP SKU while nontransitive peering is wrong; hub-and-spoke network build still lacks nontransitive peering proof.
- **D — Incorrect.** Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
  Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration. In the hub-and-spoke network build, this check observes custom virtual-network DNS servers. Hub-and-spoke network build output covers custom virtual-network DNS servers, not nontransitive peering; the nontransitive peering requirement to avoid assuming that connectivity automatically crosses a second peering hop remains unverified.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q31 — C

**Question:** A hub-and-spoke network build query surprises the network administrator connecting hub and spoke address spaces during the network peering attempt to connect networks without overlapping their address ranges. Which finding explains it?

- **A — Incorrect.** The proposed subnet prefix overlaps an existing application subnet.
  The proposed subnet prefix overlaps an existing application subnet. The hub-and-spoke network build fault concerns subnet address planning. Hub-and-spoke network build has subnet address planning impact, but nonoverlapping address spaces is the hub-and-spoke network build failed path; the subnet address planning state cannot produce nonoverlapping address spaces failure.
- **B — Incorrect.** A Standard public IP is attached, but no NSG rule allows the intended inbound flow.
  A Standard public IP is attached, but no NSG rule allows the intended inbound flow. The hub-and-spoke network build fault concerns Standard public IP SKU. Hub-and-spoke network build could repair Standard public IP SKU while nonoverlapping address spaces stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to connect networks without overlapping their address ranges.
- **C — Correct.** The two virtual networks contain overlapping prefixes.
  The two virtual networks contain overlapping prefixes. In hub-and-spoke network build, this nonoverlapping address spaces cause matches the failure to connect networks without overlapping their address ranges.
- **D — Incorrect.** The topology assumes two peering hops provide automatic transitive routing.
  The topology assumes two peering hops provide automatic transitive routing. The hub-and-spoke network build fault concerns nontransitive peering. Hub-and-spoke network build may fix nontransitive peering, yet nonoverlapping address spaces still fails; this hub-and-spoke network build diagnosis of nontransitive peering is wrong for nonoverlapping address spaces.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q32 — C

**Question:** Other hub-and-spoke network build components are healthy, but the network peering still cannot reserve subnet ranges that do not collide with future network segments. Which state causes the isolated failure?

- **A — Incorrect.** Only one directional peering object was created.
  Only one directional peering object was created. The hub-and-spoke network build fault concerns bidirectional peering objects. Hub-and-spoke network build could repair bidirectional peering objects while subnet address planning stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to reserve subnet ranges that do not collide with future network segments.
- **B — Incorrect.** A dynamic allocation was selected for an address consumed by an external allowlist.
  A dynamic allocation was selected for an address consumed by an external allowlist. The hub-and-spoke network build fault concerns static public IP allocation. Hub-and-spoke network build failed on subnet address planning; this static public IP allocation finding redirects hub-and-spoke network build remediation away from subnet address planning.
- **C — Correct.** The proposed subnet prefix overlaps an existing application subnet.
  The proposed subnet prefix overlaps an existing application subnet. This hub-and-spoke network build condition breaks subnet address planning, explaining why operators cannot reserve subnet ranges that do not collide with future network segments.
- **D — Incorrect.** The two virtual networks contain overlapping prefixes.
  The two virtual networks contain overlapping prefixes. The hub-and-spoke network build fault concerns nonoverlapping address spaces. Hub-and-spoke network build has nonoverlapping address spaces impact, but subnet address planning is the hub-and-spoke network build failed path; the nonoverlapping address spaces state cannot produce subnet address planning failure.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q33 — B

**Question:** During a network peering fault drill, the hub-and-spoke network build does not create both directional control-plane links required for connected networks. Which finding identifies the defect?

- **A — Incorrect.** Both sides attempt to use a remote gateway, which is not a valid transit relationship.
  Both sides attempt to use a remote gateway, which is not a valid transit relationship. The hub-and-spoke network build fault concerns gateway transit peering. Hub-and-spoke network build failed on bidirectional peering objects; this gateway transit peering finding redirects hub-and-spoke network build remediation away from bidirectional peering objects.
- **B — Correct.** Only one directional peering object was created.
  For the hub-and-spoke network build, the bidirectional peering objects failure is causal: only one directional peering object was created. Correcting it restores the ability to create both directional control-plane links required for connected networks.
- **C — Incorrect.** A zonal frontend address is bound to a design that expects zone-redundant availability.
  A zonal frontend address is bound to a design that expects zone-redundant availability. The hub-and-spoke network build fault concerns zonal public IP configuration. Hub-and-spoke network build has zonal public IP configuration impact, but bidirectional peering objects is the hub-and-spoke network build failed path; the zonal public IP configuration state cannot produce bidirectional peering objects failure.
- **D — Incorrect.** The proposed subnet prefix overlaps an existing application subnet.
  The proposed subnet prefix overlaps an existing application subnet. The hub-and-spoke network build fault concerns subnet address planning. Hub-and-spoke network build could repair subnet address planning while bidirectional peering objects stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to create both directional control-plane links required for connected networks.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q34 — A

**Question:** The hub-and-spoke network build setup finishes, yet the network peering cannot let a spoke use a hub gateway only when both peering sides permit it. Which misconfiguration explains the mismatch?

- **A — Correct.** Both sides attempt to use a remote gateway, which is not a valid transit relationship.
  Both sides attempt to use a remote gateway, which is not a valid transit relationship. The finding is specific to gateway transit peering in the hub-and-spoke network build; repairing gateway transit peering restores the hub-and-spoke network build ability to let a spoke use a hub gateway only when both peering sides permit it.
- **B — Incorrect.** An NVA forwards packets, but the receiving peering blocks forwarded traffic.
  An NVA forwards packets, but the receiving peering blocks forwarded traffic. The hub-and-spoke network build fault concerns forwarded traffic on peering. Hub-and-spoke network build has forwarded traffic on peering impact, but gateway transit peering is the hub-and-spoke network build failed path; the forwarded traffic on peering state cannot produce gateway transit peering failure.
- **C — Incorrect.** The configured DNS server address is not reachable from the workload subnet.
  The configured DNS server address is not reachable from the workload subnet. The hub-and-spoke network build fault concerns custom virtual-network DNS servers. Hub-and-spoke network build could repair custom virtual-network DNS servers while gateway transit peering stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to let a spoke use a hub gateway only when both peering sides permit it.
- **D — Incorrect.** Only one directional peering object was created.
  Only one directional peering object was created. The hub-and-spoke network build fault concerns bidirectional peering objects. Hub-and-spoke network build failed on gateway transit peering; this bidirectional peering objects finding redirects hub-and-spoke network build remediation away from gateway transit peering.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q35 — B

**Question:** A network peering break/fix in the hub-and-spoke network build fails when operators try to carry forwarded packets from an NVA across connected networks. Which diagnosis fits?

- **A — Incorrect.** A Standard public IP is attached, but no NSG rule allows the intended inbound flow.
  A Standard public IP is attached, but no NSG rule allows the intended inbound flow. The hub-and-spoke network build fault concerns Standard public IP SKU. Hub-and-spoke network build has Standard public IP SKU impact, but forwarded traffic on peering is the hub-and-spoke network build failed path; the Standard public IP SKU state cannot produce forwarded traffic on peering failure.
- **B — Correct.** An NVA forwards packets, but the receiving peering blocks forwarded traffic.
  The hub-and-spoke network build cannot carry forwarded packets from an NVA across connected networks because of this forwarded traffic on peering defect: an NVA forwards packets, but the receiving peering blocks forwarded traffic. The symptom and repair align.
- **C — Incorrect.** The topology assumes two peering hops provide automatic transitive routing.
  The topology assumes two peering hops provide automatic transitive routing. The hub-and-spoke network build fault concerns nontransitive peering. Hub-and-spoke network build failed on forwarded traffic on peering; this nontransitive peering finding redirects hub-and-spoke network build remediation away from forwarded traffic on peering.
- **D — Incorrect.** Both sides attempt to use a remote gateway, which is not a valid transit relationship.
  Both sides attempt to use a remote gateway, which is not a valid transit relationship. The hub-and-spoke network build fault concerns gateway transit peering. Hub-and-spoke network build may fix gateway transit peering, yet forwarded traffic on peering still fails; this hub-and-spoke network build diagnosis of gateway transit peering is wrong for forwarded traffic on peering.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q36 — D

**Question:** The hub-and-spoke network build troubleshooting scope is the network peering need to use the production public-address SKU with secure defaults. Which condition should be corrected first?

- **A — Incorrect.** A dynamic allocation was selected for an address consumed by an external allowlist.
  A dynamic allocation was selected for an address consumed by an external allowlist. The hub-and-spoke network build fault concerns static public IP allocation. Hub-and-spoke network build could repair static public IP allocation while Standard public IP SKU stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to use the production public-address SKU with secure defaults.
- **B — Incorrect.** The two virtual networks contain overlapping prefixes.
  The two virtual networks contain overlapping prefixes. The hub-and-spoke network build fault concerns nonoverlapping address spaces. Hub-and-spoke network build failed on Standard public IP SKU; this nonoverlapping address spaces finding redirects hub-and-spoke network build remediation away from Standard public IP SKU.
- **C — Incorrect.** An NVA forwards packets, but the receiving peering blocks forwarded traffic.
  An NVA forwards packets, but the receiving peering blocks forwarded traffic. The hub-and-spoke network build fault concerns forwarded traffic on peering. Hub-and-spoke network build may fix forwarded traffic on peering, yet Standard public IP SKU still fails; this hub-and-spoke network build diagnosis of forwarded traffic on peering is wrong for Standard public IP SKU.
- **D — Correct.** A Standard public IP is attached, but no NSG rule allows the intended inbound flow.
  A Standard public IP is attached, but no NSG rule allows the intended inbound flow. Removing this Standard public IP SKU condition lets the hub-and-spoke network build use the production public-address SKU with secure defaults while leaving healthy controls unchanged.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q37 — A

**Question:** The hub-and-spoke network build result is partial because the network peering cannot keep the assigned public address stable across resource restarts. Which condition accounts for that result?

- **A — Correct.** A dynamic allocation was selected for an address consumed by an external allowlist.
  A dynamic allocation was selected for an address consumed by an external allowlist. In hub-and-spoke network build, this static public IP allocation cause matches the failure to keep the assigned public address stable across resource restarts.
- **B — Incorrect.** A zonal frontend address is bound to a design that expects zone-redundant availability.
  A zonal frontend address is bound to a design that expects zone-redundant availability. The hub-and-spoke network build fault concerns zonal public IP configuration. Hub-and-spoke network build may fix zonal public IP configuration, yet static public IP allocation still fails; this hub-and-spoke network build diagnosis of zonal public IP configuration is wrong for static public IP allocation.
- **C — Incorrect.** The proposed subnet prefix overlaps an existing application subnet.
  The proposed subnet prefix overlaps an existing application subnet. The hub-and-spoke network build fault concerns subnet address planning. Hub-and-spoke network build has subnet address planning impact, but static public IP allocation is the hub-and-spoke network build failed path; the subnet address planning state cannot produce static public IP allocation failure.
- **D — Incorrect.** A Standard public IP is attached, but no NSG rule allows the intended inbound flow.
  A Standard public IP is attached, but no NSG rule allows the intended inbound flow. The hub-and-spoke network build fault concerns Standard public IP SKU. Hub-and-spoke network build could repair Standard public IP SKU while static public IP allocation stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to keep the assigned public address stable across resource restarts.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q38 — B

**Question:** The network peering evidence shows the hub-and-spoke network build cannot pin a public address to the intended availability-zone design. Which root cause fits that evidence?

- **A — Incorrect.** The configured DNS server address is not reachable from the workload subnet.
  The configured DNS server address is not reachable from the workload subnet. The hub-and-spoke network build fault concerns custom virtual-network DNS servers. Hub-and-spoke network build may fix custom virtual-network DNS servers, yet zonal public IP configuration still fails; this hub-and-spoke network build diagnosis of custom virtual-network DNS servers is wrong for zonal public IP configuration.
- **B — Correct.** A zonal frontend address is bound to a design that expects zone-redundant availability.
  A zonal frontend address is bound to a design that expects zone-redundant availability. This hub-and-spoke network build condition breaks zonal public IP configuration, explaining why operators cannot pin a public address to the intended availability-zone design.
- **C — Incorrect.** Only one directional peering object was created.
  Only one directional peering object was created. The hub-and-spoke network build fault concerns bidirectional peering objects. Hub-and-spoke network build could repair bidirectional peering objects while zonal public IP configuration stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to pin a public address to the intended availability-zone design.
- **D — Incorrect.** A dynamic allocation was selected for an address consumed by an external allowlist.
  A dynamic allocation was selected for an address consumed by an external allowlist. The hub-and-spoke network build fault concerns static public IP allocation. Hub-and-spoke network build failed on zonal public IP configuration; this static public IP allocation finding redirects hub-and-spoke network build remediation away from zonal public IP configuration.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q39 — A

**Question:** Although the hub-and-spoke network build is meant to let the network peering make virtual machines use approved custom DNS resolvers, its checkpoint fails. Which network peering defect explains the failure?

- **A — Correct.** The configured DNS server address is not reachable from the workload subnet.
  For the hub-and-spoke network build, the custom virtual-network DNS servers failure is causal: the configured DNS server address is not reachable from the workload subnet. Correcting it restores the ability to make virtual machines use approved custom DNS resolvers.
- **B — Incorrect.** The topology assumes two peering hops provide automatic transitive routing.
  The topology assumes two peering hops provide automatic transitive routing. The hub-and-spoke network build fault concerns nontransitive peering. Hub-and-spoke network build could repair nontransitive peering while custom virtual-network DNS servers stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to make virtual machines use approved custom DNS resolvers.
- **C — Incorrect.** Both sides attempt to use a remote gateway, which is not a valid transit relationship.
  Both sides attempt to use a remote gateway, which is not a valid transit relationship. The hub-and-spoke network build fault concerns gateway transit peering. Hub-and-spoke network build failed on custom virtual-network DNS servers; this gateway transit peering finding redirects hub-and-spoke network build remediation away from custom virtual-network DNS servers.
- **D — Incorrect.** A zonal frontend address is bound to a design that expects zone-redundant availability.
  A zonal frontend address is bound to a design that expects zone-redundant availability. The hub-and-spoke network build fault concerns zonal public IP configuration. Hub-and-spoke network build may fix zonal public IP configuration, yet custom virtual-network DNS servers still fails; this hub-and-spoke network build diagnosis of zonal public IP configuration is wrong for custom virtual-network DNS servers.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network name resolution](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances)

**Source reviewed:** 2026-08-31

## LAB17-Q40 — B

**Question:** The network peering support team isolated the hub-and-spoke network build incident to the attempt to avoid assuming that connectivity automatically crosses a second peering hop. Which condition prevents success?

- **A — Incorrect.** The two virtual networks contain overlapping prefixes.
  The two virtual networks contain overlapping prefixes. The hub-and-spoke network build fault concerns nonoverlapping address spaces. Hub-and-spoke network build could repair nonoverlapping address spaces while nontransitive peering stays broken in hub-and-spoke network build; the hub-and-spoke network build remains unable to avoid assuming that connectivity automatically crosses a second peering hop.
- **B — Correct.** The topology assumes two peering hops provide automatic transitive routing.
  The topology assumes two peering hops provide automatic transitive routing. The finding is specific to nontransitive peering in the hub-and-spoke network build; repairing nontransitive peering restores the hub-and-spoke network build ability to avoid assuming that connectivity automatically crosses a second peering hop.
- **C — Incorrect.** An NVA forwards packets, but the receiving peering blocks forwarded traffic.
  An NVA forwards packets, but the receiving peering blocks forwarded traffic. The hub-and-spoke network build fault concerns forwarded traffic on peering. Hub-and-spoke network build may fix forwarded traffic on peering, yet nontransitive peering still fails; this hub-and-spoke network build diagnosis of forwarded traffic on peering is wrong for nontransitive peering.
- **D — Incorrect.** The configured DNS server address is not reachable from the workload subnet.
  The configured DNS server address is not reachable from the workload subnet. The hub-and-spoke network build fault concerns custom virtual-network DNS servers. Hub-and-spoke network build has custom virtual-network DNS servers impact, but nontransitive peering is the hub-and-spoke network build failed path; the custom virtual-network DNS servers state cannot produce nontransitive peering failure.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q41 — A

**Question:** The hub-and-spoke network build runbook separates network peering mutation from validation while it must connect networks without overlapping their address ranges. Which sequence proves it cleanly?

- **A — Correct.** First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
  The hub-and-spoke network build gets a complete nonoverlapping address spaces sequence here: first, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps. Read-back evidence follows the change.
- **B — Incorrect.** First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
  First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks. This hub-and-spoke network build pair serves bidirectional peering objects. Hub-and-spoke network build proves bidirectional peering objects, but nonoverlapping address spaces lacks implementation in hub-and-spoke network build and nonoverlapping address spaces proof; the nonoverlapping address spaces outcome to connect networks without overlapping their address ranges remains open.
- **C — Incorrect.** First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
  First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning. This hub-and-spoke network build pair serves static public IP allocation. Hub-and-spoke network build uses static public IP allocation for both steps; nonoverlapping address spaces remains untouched in hub-and-spoke network build, so its nonoverlapping address spaces gate to connect networks without overlapping their address ranges fails.
- **D — Incorrect.** First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.
  First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support. This hub-and-spoke network build pair serves zonal public IP configuration. Hub-and-spoke network build closes zonal public IP configuration, not nonoverlapping address spaces; without the nonoverlapping address spaces workflow, it cannot connect networks without overlapping their address ranges.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q42 — C

**Question:** The hub-and-spoke network build checkpoint requires both this network peering outcome—reserve subnet ranges that do not collide with future network segments—and a read-only hub-and-spoke network build state check. Which network peering response is complete?

- **A — Incorrect.** First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.
  First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state. This hub-and-spoke network build pair serves gateway transit peering. Hub-and-spoke network build proves gateway transit peering, but subnet address planning lacks implementation in hub-and-spoke network build and subnet address planning proof; the subnet address planning outcome to reserve subnet ranges that do not collide with future network segments remains open.
- **B — Incorrect.** First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.
  First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support. This hub-and-spoke network build pair serves zonal public IP configuration. Hub-and-spoke network build uses zonal public IP configuration for both steps; subnet address planning remains untouched in hub-and-spoke network build, so its subnet address planning gate to reserve subnet ranges that do not collide with future network segments fails.
- **C — Correct.** First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
  First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses. This ordered subnet address planning workflow lets the hub-and-spoke network build reserve subnet ranges that do not collide with future network segments and then verify the resulting state.
- **D — Incorrect.** First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
  First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration. This hub-and-spoke network build pair serves custom virtual-network DNS servers. Custom virtual-network DNS servers cannot replace subnet address planning in hub-and-spoke network build. Use this subnet address planning pair instead: First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Plan Azure virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm)

**Source reviewed:** 2026-08-31

## LAB17-Q43 — B

**Question:** The hub-and-spoke network build runbook must create both directional control-plane links required for connected networks, then retain network peering read-back evidence. Which hub-and-spoke network build pair completes both duties?

- **A — Incorrect.** First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.
  First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources. This hub-and-spoke network build pair serves forwarded traffic on peering. Hub-and-spoke network build uses forwarded traffic on peering for both steps; bidirectional peering objects remains untouched in hub-and-spoke network build, so its bidirectional peering objects gate to create both directional control-plane links required for connected networks fails.
- **B — Correct.** First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
  First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks. For hub-and-spoke network build, the bidirectional peering objects operation precedes its bidirectional peering objects read-back check, allowing it to create both directional control-plane links required for connected networks.
- **C — Incorrect.** First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
  First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration. This hub-and-spoke network build pair serves custom virtual-network DNS servers. Custom virtual-network DNS servers cannot replace bidirectional peering objects in hub-and-spoke network build. Use this bidirectional peering objects pair instead: First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
- **D — Incorrect.** First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.
  First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path. This hub-and-spoke network build pair serves nontransitive peering. Hub-and-spoke network build proves nontransitive peering, but bidirectional peering objects lacks implementation in hub-and-spoke network build and bidirectional peering objects proof; the bidirectional peering objects outcome to create both directional control-plane links required for connected networks remains open.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q44 — D

**Question:** To satisfy the network peering requirement, operators must change the hub-and-spoke network build configuration and prove it can let a spoke use a hub gateway only when both peering sides permit it. Which sequence is coherent?

- **A — Incorrect.** First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
  First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration. This hub-and-spoke network build pair serves Standard public IP SKU. Hub-and-spoke network build closes Standard public IP SKU, not gateway transit peering; without the gateway transit peering workflow, it cannot let a spoke use a hub gateway only when both peering sides permit it.
- **B — Incorrect.** First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.
  First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path. This hub-and-spoke network build pair serves nontransitive peering. Nontransitive peering cannot replace gateway transit peering in hub-and-spoke network build. Use this gateway transit peering pair instead: First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.
- **C — Incorrect.** First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
  First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps. This hub-and-spoke network build pair serves nonoverlapping address spaces. Hub-and-spoke network build proves nonoverlapping address spaces, but gateway transit peering lacks implementation in hub-and-spoke network build and gateway transit peering proof; the gateway transit peering outcome to let a spoke use a hub gateway only when both peering sides permit it remains open.
- **D — Correct.** First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.
  First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state. In the hub-and-spoke network build, the first gateway transit peering step runs; the hub-and-spoke network build then reads gateway transit peering state to prove it can let a spoke use a hub gateway only when both peering sides permit it.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q45 — C

**Question:** The network administrator connecting hub and spoke address spaces needs a safe hub-and-spoke network build change to carry forwarded packets from an NVA across connected networks, followed by network peering evidence. Which pair merits approval?

- **A — Incorrect.** First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
  First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning. This hub-and-spoke network build pair serves static public IP allocation. Static public IP allocation cannot replace forwarded traffic on peering in hub-and-spoke network build. Use this forwarded traffic on peering pair instead: First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.
- **B — Incorrect.** First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
  First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps. This hub-and-spoke network build pair serves nonoverlapping address spaces. Hub-and-spoke network build proves nonoverlapping address spaces, but forwarded traffic on peering lacks implementation in hub-and-spoke network build and forwarded traffic on peering proof; the forwarded traffic on peering outcome to carry forwarded packets from an NVA across connected networks remains open.
- **C — Correct.** First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.
  For the hub-and-spoke network build, the safe forwarded traffic on peering order is: first, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources. The hub-and-spoke network build records forwarded traffic on peering proof after configuration.
- **D — Incorrect.** First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
  First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses. This hub-and-spoke network build pair serves subnet address planning. Hub-and-spoke network build closes subnet address planning, not forwarded traffic on peering; without the forwarded traffic on peering workflow, it cannot carry forwarded packets from an NVA across connected networks.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31

## LAB17-Q46 — D

**Question:** The hub-and-spoke network build has two network peering gates: use the production public-address SKU with secure defaults, then prove the hub-and-spoke network build state. Which network peering sequence works?

- **A — Incorrect.** First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.
  First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support. This hub-and-spoke network build pair serves zonal public IP configuration. Hub-and-spoke network build proves zonal public IP configuration, but Standard public IP SKU lacks implementation in hub-and-spoke network build and Standard public IP SKU proof; the Standard public IP SKU outcome to use the production public-address SKU with secure defaults remains open.
- **B — Incorrect.** First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
  First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses. This hub-and-spoke network build pair serves subnet address planning. Hub-and-spoke network build uses subnet address planning for both steps; Standard public IP SKU remains untouched in hub-and-spoke network build, so its Standard public IP SKU gate to use the production public-address SKU with secure defaults fails.
- **C — Incorrect.** First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
  First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks. This hub-and-spoke network build pair serves bidirectional peering objects. Hub-and-spoke network build closes bidirectional peering objects, not Standard public IP SKU; without the Standard public IP SKU workflow, it cannot use the production public-address SKU with secure defaults.
- **D — Correct.** First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
  First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration. The hub-and-spoke network build uses its Standard public IP SKU mutation gate and Standard public IP SKU verification gate before it can use the production public-address SKU with secure defaults.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB17-CP01`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q47 — A

**Question:** Which network peering path makes the hub-and-spoke network build able to keep the assigned public address stable across resource restarts, then inspects the defining properties?

- **A — Correct.** First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
  The hub-and-spoke network build gets a complete static public IP allocation sequence here: first, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning. Read-back evidence follows the change.
- **B — Incorrect.** First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
  First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration. This hub-and-spoke network build pair serves custom virtual-network DNS servers. Hub-and-spoke network build closes custom virtual-network DNS servers, not static public IP allocation; without the static public IP allocation workflow, it cannot keep the assigned public address stable across resource restarts.
- **C — Incorrect.** First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks.
  First, Create and validate both local-to-remote and remote-to-local peering objects. Then, Query peeringState and peeringSyncLevel on both virtual networks. This hub-and-spoke network build pair serves bidirectional peering objects. Bidirectional peering objects cannot replace static public IP allocation in hub-and-spoke network build. Use this static public IP allocation pair instead: First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
- **D — Incorrect.** First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.
  First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state. This hub-and-spoke network build pair serves gateway transit peering. Hub-and-spoke network build proves gateway transit peering, but static public IP allocation lacks implementation in hub-and-spoke network build and static public IP allocation proof; the static public IP allocation outcome to keep the assigned public address stable across resource restarts remains open.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB17-CP02`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q48 — C

**Question:** At the hub-and-spoke network build approval gate, operators must show that the network peering can pin a public address to the intended availability-zone design. Which network peering configure-and-check pair is defensible?

- **A — Incorrect.** First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.
  First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path. This hub-and-spoke network build pair serves nontransitive peering. Hub-and-spoke network build closes nontransitive peering, not zonal public IP configuration; without the zonal public IP configuration workflow, it cannot pin a public address to the intended availability-zone design.
- **B — Incorrect.** First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state.
  First, Configure allowGatewayTransit and useRemoteGateways on the correct opposite peering objects. Then, Query both peerings and confirm the gateway flags and connected state. This hub-and-spoke network build pair serves gateway transit peering. Gateway transit peering cannot replace zonal public IP configuration in hub-and-spoke network build. Use this zonal public IP configuration pair instead: First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.
- **C — Correct.** First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support.
  First, Select zone-redundant placement for regional zonal resilience when supported. Then, Query the public IP zones array and the region's zone support. This ordered zonal public IP configuration workflow lets the hub-and-spoke network build pin a public address to the intended availability-zone design and then verify the resulting state.
- **D — Incorrect.** First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.
  First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources. This hub-and-spoke network build pair serves forwarded traffic on peering. Hub-and-spoke network build uses forwarded traffic on peering for both steps; zonal public IP configuration remains untouched in hub-and-spoke network build, so its zonal public IP configuration gate to pin a public address to the intended availability-zone design fails.

**Objectives:** `NW-VNET-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB17-CP03`).

**Microsoft Learn sources:**

- [Azure public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)

**Source reviewed:** 2026-08-31

## LAB17-Q49 — C

**Question:** The hub-and-spoke network build forbids a partial network peering result. Operators must first make virtual machines use approved custom DNS resolvers and afterward confirm the hub-and-spoke network build outcome. Which network peering sequence is complete?

- **A — Incorrect.** First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps.
  First, Allocate approved RFC 1918 ranges and check them against existing and planned connected networks. Then, Query every addressSpace.addressPrefixes value and prove no peered range overlaps. This hub-and-spoke network build pair serves nonoverlapping address spaces. Nonoverlapping address spaces cannot replace custom virtual-network DNS servers in hub-and-spoke network build. Use this custom virtual-network DNS servers pair instead: First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
- **B — Incorrect.** First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources.
  First, Enable forwarded traffic only on the peering directions required by the approved routing design. Then, Read allowForwardedTraffic on both directional peering resources. This hub-and-spoke network build pair serves forwarded traffic on peering. Hub-and-spoke network build proves forwarded traffic on peering, but custom virtual-network DNS servers lacks implementation in hub-and-spoke network build and custom virtual-network DNS servers proof; the custom virtual-network DNS servers outcome to make virtual machines use approved custom DNS resolvers remains open.
- **C — Correct.** First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration.
  First, Configure approved resolver IP addresses and renew affected clients when required. Then, Query dhcpOptions.dnsServers and test resolution from a VM after renewing its configuration. For hub-and-spoke network build, the custom virtual-network DNS servers operation precedes its custom virtual-network DNS servers read-back check, allowing it to make virtual machines use approved custom DNS resolvers.
- **D — Incorrect.** First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
  First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration. This hub-and-spoke network build pair serves Standard public IP SKU. Hub-and-spoke network build closes Standard public IP SKU, not custom virtual-network DNS servers; without the custom virtual-network DNS servers workflow, it cannot make virtual machines use approved custom DNS resolvers.

**Objectives:** `NW-VNET-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB17-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network name resolution](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances)

**Source reviewed:** 2026-08-31

## LAB17-Q50 — C

**Question:** Only the hub-and-spoke network build change needed to avoid assuming that connectivity automatically crosses a second peering hop is allowed, and network peering proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses.
  First, Reserve distinct prefixes for workloads, private endpoints, gateways, and platform-specific subnets. Then, List subnet prefixes and verify containment, nonoverlap, delegations, and available addresses. This hub-and-spoke network build pair serves subnet address planning. Hub-and-spoke network build proves subnet address planning, but nontransitive peering lacks implementation in hub-and-spoke network build and nontransitive peering proof; the nontransitive peering outcome to avoid assuming that connectivity automatically crosses a second peering hop remains open.
- **B — Incorrect.** First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration.
  First, Use Standard SKU and add only the required inbound NSG exposure. Then, Query sku.name, publicIPAllocationMethod, ipAddress, and associated IP configuration. This hub-and-spoke network build pair serves Standard public IP SKU. Hub-and-spoke network build uses Standard public IP SKU for both steps; nontransitive peering remains untouched in hub-and-spoke network build, so its nontransitive peering gate to avoid assuming that connectivity automatically crosses a second peering hop fails.
- **C — Correct.** First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.
  First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path. In the hub-and-spoke network build, the first nontransitive peering step runs; the hub-and-spoke network build then reads nontransitive peering state to prove it can avoid assuming that connectivity automatically crosses a second peering hop.
- **D — Incorrect.** First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning.
  First, Use static allocation when DNS or allowlists require a stable public address. Then, Query publicIPAllocationMethod and persist the assigned ipAddress after provisioning. This hub-and-spoke network build pair serves static public IP allocation. Static public IP allocation cannot replace nontransitive peering in hub-and-spoke network build. Use this nontransitive peering pair instead: First, Create the required direct peering or introduce an approved routed hub design. Then, Inspect effective routes from the source and test the exact destination path.

**Objectives:** `NW-VNET-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB17-CP05`).

**Microsoft Learn sources:**

- [Create or change virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering)

**Source reviewed:** 2026-08-31
