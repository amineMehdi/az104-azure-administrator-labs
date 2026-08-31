# Lab 18 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB18-Q01 — C

**Question:** A traffic-flow investigation peer review asks how the application traffic-control investigation should handle this outcome: ensure the intended security rule is evaluated before a broader conflicting rule. Which explanation is accurate?

- **A — Incorrect.** NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule.
  NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule. In the application traffic-control investigation, this statement describes stateful NSG processing. Application traffic-control investigation asks about NSG rule priorities; this stateful NSG processing choice leaves the NSG rule priorities explanation missing.
- **B — Incorrect.** Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet.
  Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet. In the application traffic-control investigation, this statement describes effective security rules. The effective security rules statement accurately describes effective security rules; however, application traffic-control investigation needs NSG rule priorities to ensure the intended security rule is evaluated before a broader conflicting rule; effective security rules cannot replace NSG rule priorities.
- **C — Correct.** NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow.
  NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow. This NSG rule priorities fact resolves the application traffic-control investigation design question about how to ensure the intended security rule is evaluated before a broader conflicting rule.
- **D — Incorrect.** A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path.
  A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path. In the application traffic-control investigation, this statement describes virtual appliance next hops. NSG rule priorities governs application traffic-control investigation; virtual appliance next hops cannot support NSG rule priorities when operators must ensure the intended security rule is evaluated before a broader conflicting rule.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q02 — A

**Question:** For the application traffic-control investigation, the traffic-flow investigation plan must allow return packets for an established permitted flow without a mirror rule. Which statement about traffic-flow investigation belongs in the application traffic-control investigation record?

- **A — Correct.** NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule.
  NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule. For application traffic-control investigation, stateful NSG processing supplies the service rule needed to allow return packets for an established permitted flow without a mirror rule.
- **B — Incorrect.** When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes.
  When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes. In the application traffic-control investigation, this statement describes subnet and NIC NSGs. Selecting subnet and NIC NSGs for application traffic-control investigation leaves stateful NSG processing unanswered in application traffic-control investigation; the application traffic-control investigation lacks a stateful NSG processing basis to allow return packets for an established permitted flow without a mirror rule.
- **C — Incorrect.** Azure chooses the most specific matching route before applying route-source precedence rules.
  Azure chooses the most specific matching route before applying route-source precedence rules. In the application traffic-control investigation, this statement describes longest-prefix route selection. Stateful NSG processing governs application traffic-control investigation; longest-prefix route selection cannot support stateful NSG processing when operators must allow return packets for an established permitted flow without a mirror rule.
- **D — Incorrect.** Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table.
  Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table. In the application traffic-control investigation, this statement describes gateway route propagation. Application traffic-control investigation asks about stateful NSG processing; this gateway route propagation choice leaves the stateful NSG processing explanation missing.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q03 — C

**Question:** The traffic-flow investigation review compares four claims for the application traffic-control investigation requirement to account for security filters applied at both subnet and network-interface scopes. Which claim is technically sound?

- **A — Incorrect.** An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses.
  An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses. In the application traffic-control investigation, this statement describes application security groups. Selecting application security groups for application traffic-control investigation leaves subnet and NIC NSGs unanswered in application traffic-control investigation; the application traffic-control investigation lacks a subnet and NIC NSGs basis to account for security filters applied at both subnet and network-interface scopes.
- **B — Incorrect.** A valid UDR can override a system route for the same or a broader destination prefix.
  A valid UDR can override a system route for the same or a broader destination prefix. In the application traffic-control investigation, this statement describes user-defined route overrides. Subnet and NIC NSGs governs application traffic-control investigation; user-defined route overrides cannot support subnet and NIC NSGs when operators must account for security filters applied at both subnet and network-interface scopes.
- **C — Correct.** When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes.
  When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes. In the application traffic-control investigation, this subnet and NIC NSGs rule supports the need to account for security filters applied at both subnet and network-interface scopes.
- **D — Incorrect.** IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule.
  IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule. In the application traffic-control investigation, this statement describes IP flow verification. The IP flow verification statement accurately describes IP flow verification; however, application traffic-control investigation needs subnet and NIC NSGs to account for security filters applied at both subnet and network-interface scopes; IP flow verification cannot replace subnet and NIC NSGs.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q04 — C

**Question:** The traffic-flow investigation architecture note requires the application traffic-control investigation environment to refer to application-role groups instead of fixed addresses in security rules. Which statement defines the relevant traffic-flow investigation boundary?

- **A — Incorrect.** Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet.
  Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet. In the application traffic-control investigation, this statement describes effective security rules. Application security groups governs application traffic-control investigation; effective security rules cannot support application security groups when operators must refer to application-role groups instead of fixed addresses in security rules.
- **B — Incorrect.** A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path.
  A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path. In the application traffic-control investigation, this statement describes virtual appliance next hops. Application traffic-control investigation asks about application security groups; this virtual appliance next hops choice leaves the application security groups explanation missing.
- **C — Correct.** An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses.
  For the application traffic-control investigation, the rule for application security groups is defined by this statement: an ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses. It supports the required outcome to refer to application-role groups instead of fixed addresses in security rules.
- **D — Incorrect.** NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow.
  NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow. In the application traffic-control investigation, this statement describes NSG rule priorities. Selecting NSG rule priorities for application traffic-control investigation leaves application security groups unanswered in application traffic-control investigation; the application traffic-control investigation lacks a application security groups basis to refer to application-role groups instead of fixed addresses in security rules.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups)

**Source reviewed:** 2026-08-31

## LAB18-Q05 — B

**Question:** A new traffic-flow investigation operator must explain why the application traffic-control investigation can see the combined security rules that actually apply to one interface. Which explanation is accurate?

- **A — Incorrect.** Azure chooses the most specific matching route before applying route-source precedence rules.
  Azure chooses the most specific matching route before applying route-source precedence rules. In the application traffic-control investigation, this statement describes longest-prefix route selection. Application traffic-control investigation asks about effective security rules; this longest-prefix route selection choice leaves the effective security rules explanation missing.
- **B — Correct.** Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet.
  Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet. The application traffic-control investigation applies that effective security rules boundary when operators must see the combined security rules that actually apply to one interface.
- **C — Incorrect.** Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table.
  Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table. In the application traffic-control investigation, this statement describes gateway route propagation. Selecting gateway route propagation for application traffic-control investigation leaves effective security rules unanswered in application traffic-control investigation; the application traffic-control investigation lacks a effective security rules basis to see the combined security rules that actually apply to one interface.
- **D — Incorrect.** NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule.
  NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule. In the application traffic-control investigation, this statement describes stateful NSG processing. Effective security rules governs application traffic-control investigation; stateful NSG processing cannot support effective security rules when operators must see the combined security rules that actually apply to one interface.

**Objectives:** `NW-SECURE-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q06 — B

**Question:** The application traffic-control investigation acceptance criteria require operators to select the most specific destination route before considering route origin. Which service fact supports that requirement?

- **A — Incorrect.** A valid UDR can override a system route for the same or a broader destination prefix.
  A valid UDR can override a system route for the same or a broader destination prefix. In the application traffic-control investigation, this statement describes user-defined route overrides. The user-defined route overrides statement accurately describes user-defined route overrides; however, application traffic-control investigation needs longest-prefix route selection to select the most specific destination route before considering route origin; user-defined route overrides cannot replace longest-prefix route selection.
- **B — Correct.** Azure chooses the most specific matching route before applying route-source precedence rules.
  The application traffic-control investigation needs longest-prefix route selection to select the most specific destination route before considering route origin; this option states the applicable longest-prefix route selection rule: Azure chooses the most specific matching route before applying route-source precedence rules.
- **C — Incorrect.** IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule.
  IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule. In the application traffic-control investigation, this statement describes IP flow verification. Longest-prefix route selection governs application traffic-control investigation; IP flow verification cannot support longest-prefix route selection when operators must select the most specific destination route before considering route origin.
- **D — Incorrect.** When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes.
  When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes. In the application traffic-control investigation, this statement describes subnet and NIC NSGs. Application traffic-control investigation asks about longest-prefix route selection; this subnet and NIC NSGs choice leaves the longest-prefix route selection explanation missing.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q07 — A

**Question:** A traffic-flow investigation reviewer challenges whether the application traffic-control investigation can override an applicable system path with an intentional custom route. Which response resolves the concern?

- **A — Correct.** A valid UDR can override a system route for the same or a broader destination prefix.
  A valid UDR can override a system route for the same or a broader destination prefix. This user-defined route overrides fact resolves the application traffic-control investigation design question about how to override an applicable system path with an intentional custom route.
- **B — Incorrect.** A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path.
  A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path. In the application traffic-control investigation, this statement describes virtual appliance next hops. User-defined route overrides governs application traffic-control investigation; virtual appliance next hops cannot support user-defined route overrides when operators must override an applicable system path with an intentional custom route.
- **C — Incorrect.** NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow.
  NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow. In the application traffic-control investigation, this statement describes NSG rule priorities. Application traffic-control investigation asks about user-defined route overrides; this NSG rule priorities choice leaves the user-defined route overrides explanation missing.
- **D — Incorrect.** An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses.
  An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses. In the application traffic-control investigation, this statement describes application security groups. The application security groups statement accurately describes application security groups; however, application traffic-control investigation needs user-defined route overrides to override an applicable system path with an intentional custom route; application security groups cannot replace user-defined route overrides.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q08 — B

**Question:** The application traffic-control investigation handoff omits the traffic-flow investigation rule needed to send traffic through a reachable forwarding appliance. Which statement should the team add?

- **A — Incorrect.** Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table.
  Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table. In the application traffic-control investigation, this statement describes gateway route propagation. Virtual appliance next hops governs application traffic-control investigation; gateway route propagation cannot support virtual appliance next hops when operators must send traffic through a reachable forwarding appliance.
- **B — Correct.** A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path.
  A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path. For application traffic-control investigation, virtual appliance next hops supplies the service rule needed to send traffic through a reachable forwarding appliance.
- **C — Incorrect.** NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule.
  NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule. In the application traffic-control investigation, this statement describes stateful NSG processing. The stateful NSG processing statement accurately describes stateful NSG processing; however, application traffic-control investigation needs virtual appliance next hops to send traffic through a reachable forwarding appliance; stateful NSG processing cannot replace virtual appliance next hops.
- **D — Incorrect.** Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet.
  Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet. In the application traffic-control investigation, this statement describes effective security rules. Selecting effective security rules for application traffic-control investigation leaves virtual appliance next hops unanswered in application traffic-control investigation; the application traffic-control investigation lacks a virtual appliance next hops basis to send traffic through a reachable forwarding appliance.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q09 — C

**Question:** A traffic-flow investigation incident review of the application traffic-control investigation depends on the ability to control whether learned gateway paths enter a subnet route table. Which platform description is reliable?

- **A — Incorrect.** IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule.
  IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule. In the application traffic-control investigation, this statement describes IP flow verification. Application traffic-control investigation asks about gateway route propagation; this IP flow verification choice leaves the gateway route propagation explanation missing.
- **B — Incorrect.** When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes.
  When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes. In the application traffic-control investigation, this statement describes subnet and NIC NSGs. The subnet and NIC NSGs statement accurately describes subnet and NIC NSGs; however, application traffic-control investigation needs gateway route propagation to control whether learned gateway paths enter a subnet route table; subnet and NIC NSGs cannot replace gateway route propagation.
- **C — Correct.** Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table.
  Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table. In the application traffic-control investigation, this gateway route propagation rule supports the need to control whether learned gateway paths enter a subnet route table.
- **D — Incorrect.** Azure chooses the most specific matching route before applying route-source precedence rules.
  Azure chooses the most specific matching route before applying route-source precedence rules. In the application traffic-control investigation, this statement describes longest-prefix route selection. Gateway route propagation governs application traffic-control investigation; longest-prefix route selection cannot support gateway route propagation when operators must control whether learned gateway paths enter a subnet route table.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q10 — A

**Question:** A network security administrator diagnosing application traffic flow is updating the traffic-flow investigation runbook. The requirement is to ask the platform which security rule allows or denies a specific flow. Which statement describes Azure behavior correctly?

- **A — Correct.** IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule.
  For the application traffic-control investigation, the rule for IP flow verification is defined by this statement: iP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule. It supports the required outcome to ask the platform which security rule allows or denies a specific flow.
- **B — Incorrect.** NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow.
  NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow. In the application traffic-control investigation, this statement describes NSG rule priorities. Selecting NSG rule priorities for application traffic-control investigation leaves IP flow verification unanswered in application traffic-control investigation; the application traffic-control investigation lacks a IP flow verification basis to ask the platform which security rule allows or denies a specific flow.
- **C — Incorrect.** An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses.
  An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses. In the application traffic-control investigation, this statement describes application security groups. IP flow verification governs application traffic-control investigation; application security groups cannot support IP flow verification when operators must ask the platform which security rule allows or denies a specific flow.
- **D — Incorrect.** A valid UDR can override a system route for the same or a broader destination prefix.
  A valid UDR can override a system route for the same or a broader destination prefix. In the application traffic-control investigation, this statement describes user-defined route overrides. Application traffic-control investigation asks about IP flow verification; this user-defined route overrides choice leaves the IP flow verification explanation missing.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Network Watcher IP flow verify](https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q11 — D

**Question:** The approach for the application traffic-control investigation is approved, but the traffic-flow investigation environment still cannot ensure the intended security rule is evaluated before a broader conflicting rule. Which implementation step closes the gap?

- **A — Incorrect.** Review both associations and keep layered rules consistent with the intended flow.
  Review both associations and keep layered rules consistent with the intended flow. In the application traffic-control investigation, this action changes subnet and NIC NSGs. Application traffic-control investigation approved NSG rule priorities, not subnet and NIC NSGs; only the NSG rule priorities change can ensure the intended security rule is evaluated before a broader conflicting rule.
- **B — Incorrect.** Compare every matching prefix and identify the longest prefix for the destination address.
  Compare every matching prefix and identify the longest prefix for the destination address. In the application traffic-control investigation, this action changes longest-prefix route selection. Application traffic-control investigation requires NSG rule priorities; changing longest-prefix route selection leaves NSG rule priorities absent in application traffic-control investigation; application traffic-control investigation cannot ensure the intended security rule is evaluated before a broader conflicting rule.
- **C — Incorrect.** Choose propagation behavior explicitly when combining a gateway with custom routes.
  Choose propagation behavior explicitly when combining a gateway with custom routes. In the application traffic-control investigation, this action changes gateway route propagation. Gateway route propagation does not implement NSG rule priorities for application traffic-control investigation; the application traffic-control investigation still cannot ensure the intended security rule is evaluated before a broader conflicting rule.
- **D — Correct.** Give the narrow required rule a unique priority that precedes conflicting broader rules.
  Give the narrow required rule a unique priority that precedes conflicting broader rules. This changes NSG rule priorities in the application traffic-control investigation, supplying the missing state needed to ensure the intended security rule is evaluated before a broader conflicting rule.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q12 — D

**Question:** The network security administrator diagnosing application traffic flow may change the application traffic-control investigation only to allow return packets for an established permitted flow without a mirror rule. Which traffic-flow investigation action stays within that assignment?

- **A — Incorrect.** Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules.
  Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. In the application traffic-control investigation, this action changes application security groups. Application traffic-control investigation requires stateful NSG processing; changing application security groups leaves stateful NSG processing absent in application traffic-control investigation; application traffic-control investigation cannot allow return packets for an established permitted flow without a mirror rule.
- **B — Incorrect.** Associate the route table with the source subnet and define the intended next hop.
  Associate the route table with the source subnet and define the intended next hop. In the application traffic-control investigation, this action changes user-defined route overrides. User-defined route overrides does not implement stateful NSG processing for application traffic-control investigation; the application traffic-control investigation still cannot allow return packets for an established permitted flow without a mirror rule.
- **C — Incorrect.** Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection.
  Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. In the application traffic-control investigation, this action changes IP flow verification. Application traffic-control investigation instead needs stateful NSG processing: Authorize the initiating direction and avoid redundant return-only rules. The IP flow verification action omits that stateful NSG processing work.
- **D — Correct.** Authorize the initiating direction and avoid redundant return-only rules.
  The application traffic-control investigation must allow return packets for an established permitted flow without a mirror rule; this option performs its direct stateful NSG processing change: authorize the initiating direction and avoid redundant return-only rules.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q13 — A

**Question:** A traffic-flow investigation dry run shows no application traffic-control investigation command will account for security filters applied at both subnet and network-interface scopes. Which action belongs before execution?

- **A — Correct.** Review both associations and keep layered rules consistent with the intended flow.
  Review both associations and keep layered rules consistent with the intended flow. It is the least-change subnet and NIC NSGs path for the application traffic-control investigation requirement to account for security filters applied at both subnet and network-interface scopes.
- **B — Incorrect.** Use the effective-rule view before modifying an individual NSG during troubleshooting.
  Use the effective-rule view before modifying an individual NSG during troubleshooting. In the application traffic-control investigation, this action changes effective security rules. Application traffic-control investigation instead needs subnet and NIC NSGs: Review both associations and keep layered rules consistent with the intended flow. The effective security rules action omits that subnet and NIC NSGs work.
- **C — Incorrect.** Set the NVA private address as nextHopIpAddress and enable forwarding where required.
  Set the NVA private address as nextHopIpAddress and enable forwarding where required. In the application traffic-control investigation, this action changes virtual appliance next hops. Application traffic-control investigation approved subnet and NIC NSGs, not virtual appliance next hops; only the subnet and NIC NSGs change can account for security filters applied at both subnet and network-interface scopes.
- **D — Incorrect.** Give the narrow required rule a unique priority that precedes conflicting broader rules.
  Give the narrow required rule a unique priority that precedes conflicting broader rules. In the application traffic-control investigation, this action changes NSG rule priorities. Application traffic-control investigation requires subnet and NIC NSGs; changing NSG rule priorities leaves subnet and NIC NSGs absent in application traffic-control investigation; application traffic-control investigation cannot account for security filters applied at both subnet and network-interface scopes.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q14 — A

**Question:** For the application traffic-control investigation, operators need to refer to application-role groups instead of fixed addresses in security rules. Which change realizes that requirement?

- **A — Correct.** Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules.
  Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. In application traffic-control investigation, applying application security groups is the scoped way to refer to application-role groups instead of fixed addresses in security rules.
- **B — Incorrect.** Compare every matching prefix and identify the longest prefix for the destination address.
  Compare every matching prefix and identify the longest prefix for the destination address. In the application traffic-control investigation, this action changes longest-prefix route selection. Application traffic-control investigation approved application security groups, not longest-prefix route selection; only the application security groups change can refer to application-role groups instead of fixed addresses in security rules.
- **C — Incorrect.** Choose propagation behavior explicitly when combining a gateway with custom routes.
  Choose propagation behavior explicitly when combining a gateway with custom routes. In the application traffic-control investigation, this action changes gateway route propagation. Application traffic-control investigation requires application security groups; changing gateway route propagation leaves application security groups absent in application traffic-control investigation; application traffic-control investigation cannot refer to application-role groups instead of fixed addresses in security rules.
- **D — Incorrect.** Authorize the initiating direction and avoid redundant return-only rules.
  Authorize the initiating direction and avoid redundant return-only rules. In the application traffic-control investigation, this action changes stateful NSG processing. Stateful NSG processing does not implement application security groups for application traffic-control investigation; the application traffic-control investigation still cannot refer to application-role groups instead of fixed addresses in security rules.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups)

**Source reviewed:** 2026-08-31

## LAB18-Q15 — C

**Question:** Operators must automate the application traffic-control investigation change needed to see the combined security rules that actually apply to one interface. Which traffic-flow investigation operation belongs in the runbook?

- **A — Incorrect.** Associate the route table with the source subnet and define the intended next hop.
  Associate the route table with the source subnet and define the intended next hop. In the application traffic-control investigation, this action changes user-defined route overrides. Application traffic-control investigation approved effective security rules, not user-defined route overrides; only the effective security rules change can see the combined security rules that actually apply to one interface.
- **B — Incorrect.** Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection.
  Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. In the application traffic-control investigation, this action changes IP flow verification. Application traffic-control investigation requires effective security rules; changing IP flow verification leaves effective security rules absent in application traffic-control investigation; application traffic-control investigation cannot see the combined security rules that actually apply to one interface.
- **C — Correct.** Use the effective-rule view before modifying an individual NSG during troubleshooting.
  Use the effective-rule view before modifying an individual NSG during troubleshooting. The application traffic-control investigation uses this effective security rules operation to see the combined security rules that actually apply to one interface within the approved scope.
- **D — Incorrect.** Review both associations and keep layered rules consistent with the intended flow.
  Review both associations and keep layered rules consistent with the intended flow. In the application traffic-control investigation, this action changes subnet and NIC NSGs. Application traffic-control investigation instead needs effective security rules: Use the effective-rule view before modifying an individual NSG during troubleshooting. The subnet and NIC NSGs action omits that effective security rules work.

**Objectives:** `NW-SECURE-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q16 — B

**Question:** An application traffic-control investigation review finds traffic-flow investigation drift from the need to select the most specific destination route before considering route origin. Which correction addresses that drift?

- **A — Incorrect.** Set the NVA private address as nextHopIpAddress and enable forwarding where required.
  Set the NVA private address as nextHopIpAddress and enable forwarding where required. In the application traffic-control investigation, this action changes virtual appliance next hops. Application traffic-control investigation requires longest-prefix route selection; changing virtual appliance next hops leaves longest-prefix route selection absent in application traffic-control investigation; application traffic-control investigation cannot select the most specific destination route before considering route origin.
- **B — Correct.** Compare every matching prefix and identify the longest prefix for the destination address.
  For the application traffic-control investigation, the required longest-prefix route selection action is: compare every matching prefix and identify the longest prefix for the destination address. It makes the environment able to select the most specific destination route before considering route origin.
- **C — Incorrect.** Give the narrow required rule a unique priority that precedes conflicting broader rules.
  Give the narrow required rule a unique priority that precedes conflicting broader rules. In the application traffic-control investigation, this action changes NSG rule priorities. Application traffic-control investigation instead needs longest-prefix route selection: Compare every matching prefix and identify the longest prefix for the destination address. The NSG rule priorities action omits that longest-prefix route selection work.
- **D — Incorrect.** Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules.
  Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. In the application traffic-control investigation, this action changes application security groups. Application traffic-control investigation approved longest-prefix route selection, not application security groups; only the longest-prefix route selection change can select the most specific destination route before considering route origin.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q17 — D

**Question:** The application traffic-control investigation window permits only the traffic-flow investigation change needed to override an applicable system path with an intentional custom route. Which option respects the boundary?

- **A — Incorrect.** Choose propagation behavior explicitly when combining a gateway with custom routes.
  Choose propagation behavior explicitly when combining a gateway with custom routes. In the application traffic-control investigation, this action changes gateway route propagation. Gateway route propagation does not implement user-defined route overrides for application traffic-control investigation; the application traffic-control investigation still cannot override an applicable system path with an intentional custom route.
- **B — Incorrect.** Authorize the initiating direction and avoid redundant return-only rules.
  Authorize the initiating direction and avoid redundant return-only rules. In the application traffic-control investigation, this action changes stateful NSG processing. Application traffic-control investigation instead needs user-defined route overrides: Associate the route table with the source subnet and define the intended next hop. The stateful NSG processing action omits that user-defined route overrides work.
- **C — Incorrect.** Use the effective-rule view before modifying an individual NSG during troubleshooting.
  Use the effective-rule view before modifying an individual NSG during troubleshooting. In the application traffic-control investigation, this action changes effective security rules. Application traffic-control investigation approved user-defined route overrides, not effective security rules; only the user-defined route overrides change can override an applicable system path with an intentional custom route.
- **D — Correct.** Associate the route table with the source subnet and define the intended next hop.
  Associate the route table with the source subnet and define the intended next hop. This changes user-defined route overrides in the application traffic-control investigation, supplying the missing state needed to override an applicable system path with an intentional custom route.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q18 — A

**Question:** The traffic-flow investigation preflight has passed; the application traffic-control investigation must now send traffic through a reachable forwarding appliance. Which operation should run?

- **A — Correct.** Set the NVA private address as nextHopIpAddress and enable forwarding where required.
  The application traffic-control investigation must send traffic through a reachable forwarding appliance; this option performs its direct virtual appliance next hops change: set the NVA private address as nextHopIpAddress and enable forwarding where required.
- **B — Incorrect.** Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection.
  Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. In the application traffic-control investigation, this action changes IP flow verification. Application traffic-control investigation approved virtual appliance next hops, not IP flow verification; only the virtual appliance next hops change can send traffic through a reachable forwarding appliance.
- **C — Incorrect.** Review both associations and keep layered rules consistent with the intended flow.
  Review both associations and keep layered rules consistent with the intended flow. In the application traffic-control investigation, this action changes subnet and NIC NSGs. Application traffic-control investigation requires virtual appliance next hops; changing subnet and NIC NSGs leaves virtual appliance next hops absent in application traffic-control investigation; application traffic-control investigation cannot send traffic through a reachable forwarding appliance.
- **D — Incorrect.** Compare every matching prefix and identify the longest prefix for the destination address.
  Compare every matching prefix and identify the longest prefix for the destination address. In the application traffic-control investigation, this action changes longest-prefix route selection. Longest-prefix route selection does not implement virtual appliance next hops for application traffic-control investigation; the application traffic-control investigation still cannot send traffic through a reachable forwarding appliance.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q19 — C

**Question:** The application traffic-control investigation plan must control whether learned gateway paths enter a subnet route table while limiting the mutation scope to traffic-flow investigation. Which action is appropriate?

- **A — Incorrect.** Give the narrow required rule a unique priority that precedes conflicting broader rules.
  Give the narrow required rule a unique priority that precedes conflicting broader rules. In the application traffic-control investigation, this action changes NSG rule priorities. Application traffic-control investigation approved gateway route propagation, not NSG rule priorities; only the gateway route propagation change can control whether learned gateway paths enter a subnet route table.
- **B — Incorrect.** Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules.
  Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. In the application traffic-control investigation, this action changes application security groups. Application traffic-control investigation requires gateway route propagation; changing application security groups leaves gateway route propagation absent in application traffic-control investigation; application traffic-control investigation cannot control whether learned gateway paths enter a subnet route table.
- **C — Correct.** Choose propagation behavior explicitly when combining a gateway with custom routes.
  Choose propagation behavior explicitly when combining a gateway with custom routes. It is the least-change gateway route propagation path for the application traffic-control investigation requirement to control whether learned gateway paths enter a subnet route table.
- **D — Incorrect.** Associate the route table with the source subnet and define the intended next hop.
  Associate the route table with the source subnet and define the intended next hop. In the application traffic-control investigation, this action changes user-defined route overrides. Application traffic-control investigation instead needs gateway route propagation: Choose propagation behavior explicitly when combining a gateway with custom routes. The user-defined route overrides action omits that gateway route propagation work.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q20 — D

**Question:** A traffic-flow investigation ticket in the application traffic-control investigation says to ask the platform which security rule allows or denies a specific flow. Which traffic-flow investigation action completes the application traffic-control investigation request with minimal change?

- **A — Incorrect.** Authorize the initiating direction and avoid redundant return-only rules.
  Authorize the initiating direction and avoid redundant return-only rules. In the application traffic-control investigation, this action changes stateful NSG processing. Application traffic-control investigation requires IP flow verification; changing stateful NSG processing leaves IP flow verification absent in application traffic-control investigation; application traffic-control investigation cannot ask the platform which security rule allows or denies a specific flow.
- **B — Incorrect.** Use the effective-rule view before modifying an individual NSG during troubleshooting.
  Use the effective-rule view before modifying an individual NSG during troubleshooting. In the application traffic-control investigation, this action changes effective security rules. Effective security rules does not implement IP flow verification for application traffic-control investigation; the application traffic-control investigation still cannot ask the platform which security rule allows or denies a specific flow.
- **C — Incorrect.** Set the NVA private address as nextHopIpAddress and enable forwarding where required.
  Set the NVA private address as nextHopIpAddress and enable forwarding where required. In the application traffic-control investigation, this action changes virtual appliance next hops. Application traffic-control investigation instead needs IP flow verification: Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. The virtual appliance next hops action omits that IP flow verification work.
- **D — Correct.** Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection.
  Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. In application traffic-control investigation, applying IP flow verification is the scoped way to ask the platform which security rule allows or denies a specific flow.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Network Watcher IP flow verify](https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q21 — D

**Question:** The traffic-flow investigation log says the application traffic-control investigation can now ensure the intended security rule is evaluated before a broader conflicting rule. Which traffic-flow investigation state should the application traffic-control investigation acceptance test retain?

- **A — Incorrect.** Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
  Query ASG membership and confirm the effective rule resolves the intended source and destination roles. In the application traffic-control investigation, this check observes application security groups. Application traffic-control investigation output covers application security groups, not NSG rule priorities; the NSG rule priorities requirement to ensure the intended security rule is evaluated before a broader conflicting rule remains unverified.
- **B — Incorrect.** Query subnet route-table association and the NIC's effective routes.
  Query subnet route-table association and the NIC's effective routes. In the application traffic-control investigation, this check observes user-defined route overrides. User-defined route overrides success in application traffic-control investigation cannot verify NSG rule priorities; application traffic-control investigation cannot ensure the intended security rule is evaluated before a broader conflicting rule until NSG rule priorities evidence exists.
- **C — Incorrect.** Capture access, rule name, and the tested five-tuple in validation evidence.
  Capture access, rule name, and the tested five-tuple in validation evidence. In the application traffic-control investigation, this check observes IP flow verification. Application traffic-control investigation reads IP flow verification, leaving NSG rule priorities unproved in application traffic-control investigation; application traffic-control investigation still has no NSG rule priorities proof.
- **D — Correct.** List rules ordered by priority and identify the first match for the test five-tuple.
  List rules ordered by priority and identify the first match for the test five-tuple. The application traffic-control investigation reads NSG rule priorities directly; that NSG rule priorities result proves the application traffic-control investigation can ensure the intended security rule is evaluated before a broader conflicting rule without another mutation.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q22 — B

**Question:** The application traffic-control investigation rejects traffic-flow investigation exit status as proof it can allow return packets for an established permitted flow without a mirror rule. Which application traffic-control investigation result is valid evidence?

- **A — Incorrect.** List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
  List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority. In the application traffic-control investigation, this check observes effective security rules. Effective security rules success in application traffic-control investigation cannot verify stateful NSG processing; application traffic-control investigation cannot allow return packets for an established permitted flow without a mirror rule until stateful NSG processing evidence exists.
- **B — Correct.** Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
  For the application traffic-control investigation, this stateful NSG processing observation is decisive: inspect the initiating rule and use flow logs or a connection test to confirm the established response path. It is application traffic-control investigation evidence that operators can allow return packets for an established permitted flow without a mirror rule.
- **C — Incorrect.** Inspect the effective route and verify forwarding and reachability on the appliance NIC.
  Inspect the effective route and verify forwarding and reachability on the appliance NIC. In the application traffic-control investigation, this check observes virtual appliance next hops. Application traffic-control investigation could pass virtual appliance next hops while stateful NSG processing is wrong; application traffic-control investigation still lacks stateful NSG processing proof.
- **D — Incorrect.** List rules ordered by priority and identify the first match for the test five-tuple.
  List rules ordered by priority and identify the first match for the test five-tuple. In the application traffic-control investigation, this check observes NSG rule priorities. Application traffic-control investigation output covers NSG rule priorities, not stateful NSG processing; the stateful NSG processing requirement to allow return packets for an established permitted flow without a mirror rule remains unverified.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q23 — D

**Question:** The traffic-flow investigation validator needs one application traffic-control investigation query after the change to account for security filters applied at both subnet and network-interface scopes. Which traffic-flow investigation property should the application traffic-control investigation validator inspect?

- **A — Incorrect.** Read effective routes and show the selected prefix, next hop type, and next hop IP.
  Read effective routes and show the selected prefix, next hop type, and next hop IP. In the application traffic-control investigation, this check observes longest-prefix route selection. Application traffic-control investigation reads longest-prefix route selection, leaving subnet and NIC NSGs unproved in application traffic-control investigation; application traffic-control investigation still has no subnet and NIC NSGs proof.
- **B — Incorrect.** Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
  Query disableBgpRoutePropagation and inspect effective routes learned from the gateway. In the application traffic-control investigation, this check observes gateway route propagation. Application traffic-control investigation could pass gateway route propagation while subnet and NIC NSGs is wrong; application traffic-control investigation still lacks subnet and NIC NSGs proof.
- **C — Incorrect.** Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
  Inspect the initiating rule and use flow logs or a connection test to confirm the established response path. In the application traffic-control investigation, this check observes stateful NSG processing. Application traffic-control investigation output covers stateful NSG processing, not subnet and NIC NSGs; the subnet and NIC NSGs requirement to account for security filters applied at both subnet and network-interface scopes remains unverified.
- **D — Correct.** Query the NIC's effective security rules and trace each match to its source NSG.
  Query the NIC's effective security rules and trace each match to its source NSG. Because the application traffic-control investigation check observes subnet and NIC NSGs, it independently verifies the requirement to account for security filters applied at both subnet and network-interface scopes.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q24 — A

**Question:** The network security administrator diagnosing application traffic flow must confirm the application traffic-control investigation, without mutation, can refer to application-role groups instead of fixed addresses in security rules. Which traffic-flow investigation check qualifies?

- **A — Correct.** Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
  The application traffic-control investigation validator needs this application security groups result: query ASG membership and confirm the effective rule resolves the intended source and destination roles. It proves the outcome to refer to application-role groups instead of fixed addresses in security rules rather than an adjacent checkpoint.
- **B — Incorrect.** Query subnet route-table association and the NIC's effective routes.
  Query subnet route-table association and the NIC's effective routes. In the application traffic-control investigation, this check observes user-defined route overrides. Application traffic-control investigation output covers user-defined route overrides, not application security groups; the application security groups requirement to refer to application-role groups instead of fixed addresses in security rules remains unverified.
- **C — Incorrect.** Capture access, rule name, and the tested five-tuple in validation evidence.
  Capture access, rule name, and the tested five-tuple in validation evidence. In the application traffic-control investigation, this check observes IP flow verification. IP flow verification success in application traffic-control investigation cannot verify application security groups; application traffic-control investigation cannot refer to application-role groups instead of fixed addresses in security rules until application security groups evidence exists.
- **D — Incorrect.** Query the NIC's effective security rules and trace each match to its source NSG.
  Query the NIC's effective security rules and trace each match to its source NSG. In the application traffic-control investigation, this check observes subnet and NIC NSGs. Application traffic-control investigation reads subnet and NIC NSGs, leaving application security groups unproved in application traffic-control investigation; application traffic-control investigation still has no application security groups proof.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups)

**Source reviewed:** 2026-08-31

## LAB18-Q25 — A

**Question:** The application traffic-control investigation configuration is complete; the traffic-flow investigation reviewers need evidence it can see the combined security rules that actually apply to one interface. Which observation shows success?

- **A — Correct.** List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
  List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority. This is independent effective security rules evidence for the application traffic-control investigation, even if application traffic-control investigation setup reports success before effective security rules becomes observable.
- **B — Incorrect.** Inspect the effective route and verify forwarding and reachability on the appliance NIC.
  Inspect the effective route and verify forwarding and reachability on the appliance NIC. In the application traffic-control investigation, this check observes virtual appliance next hops. Virtual appliance next hops success in application traffic-control investigation cannot verify effective security rules; application traffic-control investigation cannot see the combined security rules that actually apply to one interface until effective security rules evidence exists.
- **C — Incorrect.** List rules ordered by priority and identify the first match for the test five-tuple.
  List rules ordered by priority and identify the first match for the test five-tuple. In the application traffic-control investigation, this check observes NSG rule priorities. Application traffic-control investigation reads NSG rule priorities, leaving effective security rules unproved in application traffic-control investigation; application traffic-control investigation still has no effective security rules proof.
- **D — Incorrect.** Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
  Query ASG membership and confirm the effective rule resolves the intended source and destination roles. In the application traffic-control investigation, this check observes application security groups. Application traffic-control investigation could pass application security groups while effective security rules is wrong; application traffic-control investigation still lacks effective security rules proof.

**Objectives:** `NW-SECURE-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q26 — B

**Question:** The traffic-flow investigation validation asks whether the application traffic-control investigation can select the most specific destination route before considering route origin. Which observable state is strongest?

- **A — Incorrect.** Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
  Query disableBgpRoutePropagation and inspect effective routes learned from the gateway. In the application traffic-control investigation, this check observes gateway route propagation. Gateway route propagation success in application traffic-control investigation cannot verify longest-prefix route selection; application traffic-control investigation cannot select the most specific destination route before considering route origin until longest-prefix route selection evidence exists.
- **B — Correct.** Read effective routes and show the selected prefix, next hop type, and next hop IP.
  Read effective routes and show the selected prefix, next hop type, and next hop IP. For application traffic-control investigation, this longest-prefix route selection read confirms the service can select the most specific destination route before considering route origin.
- **C — Incorrect.** Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
  Inspect the initiating rule and use flow logs or a connection test to confirm the established response path. In the application traffic-control investigation, this check observes stateful NSG processing. Application traffic-control investigation could pass stateful NSG processing while longest-prefix route selection is wrong; application traffic-control investigation still lacks longest-prefix route selection proof.
- **D — Incorrect.** List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
  List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority. In the application traffic-control investigation, this check observes effective security rules. Application traffic-control investigation output covers effective security rules, not longest-prefix route selection; the longest-prefix route selection requirement to select the most specific destination route before considering route origin remains unverified.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q27 — C

**Question:** An application traffic-control investigation review must prove the traffic-flow investigation ability to override an applicable system path with an intentional custom route. Which check avoids an adjacent feature?

- **A — Incorrect.** Capture access, rule name, and the tested five-tuple in validation evidence.
  Capture access, rule name, and the tested five-tuple in validation evidence. In the application traffic-control investigation, this check observes IP flow verification. Application traffic-control investigation reads IP flow verification, leaving user-defined route overrides unproved in application traffic-control investigation; application traffic-control investigation still has no user-defined route overrides proof.
- **B — Incorrect.** Query the NIC's effective security rules and trace each match to its source NSG.
  Query the NIC's effective security rules and trace each match to its source NSG. In the application traffic-control investigation, this check observes subnet and NIC NSGs. Application traffic-control investigation could pass subnet and NIC NSGs while user-defined route overrides is wrong; application traffic-control investigation still lacks user-defined route overrides proof.
- **C — Correct.** Query subnet route-table association and the NIC's effective routes.
  Query subnet route-table association and the NIC's effective routes. The application traffic-control investigation reads user-defined route overrides directly; that user-defined route overrides result proves the application traffic-control investigation can override an applicable system path with an intentional custom route without another mutation.
- **D — Incorrect.** Read effective routes and show the selected prefix, next hop type, and next hop IP.
  Read effective routes and show the selected prefix, next hop type, and next hop IP. In the application traffic-control investigation, this check observes longest-prefix route selection. Longest-prefix route selection success in application traffic-control investigation cannot verify user-defined route overrides; application traffic-control investigation cannot override an applicable system path with an intentional custom route until user-defined route overrides evidence exists.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q28 — B

**Question:** The application traffic-control investigation evidence bundle needs a traffic-flow investigation result showing it can send traffic through a reachable forwarding appliance. Which result belongs in the checkpoint?

- **A — Incorrect.** List rules ordered by priority and identify the first match for the test five-tuple.
  List rules ordered by priority and identify the first match for the test five-tuple. In the application traffic-control investigation, this check observes NSG rule priorities. Application traffic-control investigation could pass NSG rule priorities while virtual appliance next hops is wrong; application traffic-control investigation still lacks virtual appliance next hops proof.
- **B — Correct.** Inspect the effective route and verify forwarding and reachability on the appliance NIC.
  For the application traffic-control investigation, this virtual appliance next hops observation is decisive: inspect the effective route and verify forwarding and reachability on the appliance NIC. It is application traffic-control investigation evidence that operators can send traffic through a reachable forwarding appliance.
- **C — Incorrect.** Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
  Query ASG membership and confirm the effective rule resolves the intended source and destination roles. In the application traffic-control investigation, this check observes application security groups. Application security groups success in application traffic-control investigation cannot verify virtual appliance next hops; application traffic-control investigation cannot send traffic through a reachable forwarding appliance until virtual appliance next hops evidence exists.
- **D — Incorrect.** Query subnet route-table association and the NIC's effective routes.
  Query subnet route-table association and the NIC's effective routes. In the application traffic-control investigation, this check observes user-defined route overrides. Application traffic-control investigation reads user-defined route overrides, leaving virtual appliance next hops unproved in application traffic-control investigation; application traffic-control investigation still has no virtual appliance next hops proof.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q29 — D

**Question:** Before application traffic-control investigation cleanup, the traffic-flow investigation team must reconfirm it can control whether learned gateway paths enter a subnet route table. Which read-only inspection should run?

- **A — Incorrect.** Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
  Inspect the initiating rule and use flow logs or a connection test to confirm the established response path. In the application traffic-control investigation, this check observes stateful NSG processing. Application traffic-control investigation output covers stateful NSG processing, not gateway route propagation; the gateway route propagation requirement to control whether learned gateway paths enter a subnet route table remains unverified.
- **B — Incorrect.** List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
  List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority. In the application traffic-control investigation, this check observes effective security rules. Effective security rules success in application traffic-control investigation cannot verify gateway route propagation; application traffic-control investigation cannot control whether learned gateway paths enter a subnet route table until gateway route propagation evidence exists.
- **C — Incorrect.** Inspect the effective route and verify forwarding and reachability on the appliance NIC.
  Inspect the effective route and verify forwarding and reachability on the appliance NIC. In the application traffic-control investigation, this check observes virtual appliance next hops. Application traffic-control investigation reads virtual appliance next hops, leaving gateway route propagation unproved in application traffic-control investigation; application traffic-control investigation still has no gateway route propagation proof.
- **D — Correct.** Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
  Query disableBgpRoutePropagation and inspect effective routes learned from the gateway. Because the application traffic-control investigation check observes gateway route propagation, it independently verifies the requirement to control whether learned gateway paths enter a subnet route table.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q30 — A

**Question:** The application traffic-control investigation setup reports success after the traffic-flow investigation attempt to ask the platform which security rule allows or denies a specific flow. Which traffic-flow investigation read-only observation proves the application traffic-control investigation outcome?

- **A — Correct.** Capture access, rule name, and the tested five-tuple in validation evidence.
  The application traffic-control investigation validator needs this IP flow verification result: capture access, rule name, and the tested five-tuple in validation evidence. It proves the outcome to ask the platform which security rule allows or denies a specific flow rather than an adjacent checkpoint.
- **B — Incorrect.** Query the NIC's effective security rules and trace each match to its source NSG.
  Query the NIC's effective security rules and trace each match to its source NSG. In the application traffic-control investigation, this check observes subnet and NIC NSGs. Application traffic-control investigation reads subnet and NIC NSGs, leaving IP flow verification unproved in application traffic-control investigation; application traffic-control investigation still has no IP flow verification proof.
- **C — Incorrect.** Read effective routes and show the selected prefix, next hop type, and next hop IP.
  Read effective routes and show the selected prefix, next hop type, and next hop IP. In the application traffic-control investigation, this check observes longest-prefix route selection. Application traffic-control investigation could pass longest-prefix route selection while IP flow verification is wrong; application traffic-control investigation still lacks IP flow verification proof.
- **D — Incorrect.** Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
  Query disableBgpRoutePropagation and inspect effective routes learned from the gateway. In the application traffic-control investigation, this check observes gateway route propagation. Application traffic-control investigation output covers gateway route propagation, not IP flow verification; the IP flow verification requirement to ask the platform which security rule allows or denies a specific flow remains unverified.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Network Watcher IP flow verify](https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q31 — C

**Question:** The application traffic-control investigation setup finishes, yet the traffic-flow investigation cannot ensure the intended security rule is evaluated before a broader conflicting rule. Which misconfiguration explains the mismatch?

- **A — Incorrect.** Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow.
  Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow. The application traffic-control investigation fault concerns stateful NSG processing. Application traffic-control investigation has stateful NSG processing impact, but NSG rule priorities is the application traffic-control investigation failed path; the stateful NSG processing state cannot produce NSG rule priorities failure.
- **B — Incorrect.** Troubleshooting selected a broader default route even though a more-specific route exists.
  Troubleshooting selected a broader default route even though a more-specific route exists. The application traffic-control investigation fault concerns longest-prefix route selection. Application traffic-control investigation could repair longest-prefix route selection while NSG rule priorities stays broken in application traffic-control investigation; the application traffic-control investigation remains unable to ensure the intended security rule is evaluated before a broader conflicting rule.
- **C — Correct.** A broad deny rule has a lower priority number than the required allow rule.
  A broad deny rule has a lower priority number than the required allow rule. Removing this NSG rule priorities condition lets the application traffic-control investigation ensure the intended security rule is evaluated before a broader conflicting rule while leaving healthy controls unchanged.
- **D — Incorrect.** The diagnostic used the wrong local port and therefore evaluated a different flow.
  The diagnostic used the wrong local port and therefore evaluated a different flow. The application traffic-control investigation fault concerns IP flow verification. Application traffic-control investigation may fix IP flow verification, yet NSG rule priorities still fails; this application traffic-control investigation diagnosis of IP flow verification is wrong for NSG rule priorities.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q32 — B

**Question:** A traffic-flow investigation break/fix in the application traffic-control investigation fails when operators try to allow return packets for an established permitted flow without a mirror rule. Which diagnosis fits?

- **A — Incorrect.** The subnet NSG allows the flow, but the NIC NSG denies it.
  The subnet NSG allows the flow, but the NIC NSG denies it. The application traffic-control investigation fault concerns subnet and NIC NSGs. Application traffic-control investigation could repair subnet and NIC NSGs while stateful NSG processing stays broken in application traffic-control investigation; the application traffic-control investigation remains unable to allow return packets for an established permitted flow without a mirror rule.
- **B — Correct.** Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow.
  Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow. In application traffic-control investigation, this stateful NSG processing cause matches the failure to allow return packets for an established permitted flow without a mirror rule.
- **C — Incorrect.** The route table exists but is associated with a different subnet.
  The route table exists but is associated with a different subnet. The application traffic-control investigation fault concerns user-defined route overrides. Application traffic-control investigation may fix user-defined route overrides, yet stateful NSG processing still fails; this application traffic-control investigation diagnosis of user-defined route overrides is wrong for stateful NSG processing.
- **D — Incorrect.** A broad deny rule has a lower priority number than the required allow rule.
  A broad deny rule has a lower priority number than the required allow rule. The application traffic-control investigation fault concerns NSG rule priorities. Application traffic-control investigation has NSG rule priorities impact, but stateful NSG processing is the application traffic-control investigation failed path; the NSG rule priorities state cannot produce stateful NSG processing failure.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q33 — B

**Question:** The application traffic-control investigation troubleshooting scope is the traffic-flow investigation need to account for security filters applied at both subnet and network-interface scopes. Which condition should be corrected first?

- **A — Incorrect.** The VM's NIC was never added to the ASG referenced by the allow rule.
  The VM's NIC was never added to the ASG referenced by the allow rule. The application traffic-control investigation fault concerns application security groups. Application traffic-control investigation failed on subnet and NIC NSGs; this application security groups finding redirects application traffic-control investigation remediation away from subnet and NIC NSGs.
- **B — Correct.** The subnet NSG allows the flow, but the NIC NSG denies it.
  The subnet NSG allows the flow, but the NIC NSG denies it. This application traffic-control investigation condition breaks subnet and NIC NSGs, explaining why operators cannot account for security filters applied at both subnet and network-interface scopes.
- **C — Incorrect.** The route points to an old NVA address that is no longer assigned.
  The route points to an old NVA address that is no longer assigned. The application traffic-control investigation fault concerns virtual appliance next hops. Application traffic-control investigation has virtual appliance next hops impact, but subnet and NIC NSGs is the application traffic-control investigation failed path; the virtual appliance next hops state cannot produce subnet and NIC NSGs failure.
- **D — Incorrect.** Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow.
  Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow. The application traffic-control investigation fault concerns stateful NSG processing. Application traffic-control investigation could repair stateful NSG processing while subnet and NIC NSGs stays broken in application traffic-control investigation; the application traffic-control investigation remains unable to account for security filters applied at both subnet and network-interface scopes.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q34 — C

**Question:** The application traffic-control investigation result is partial because the traffic-flow investigation cannot refer to application-role groups instead of fixed addresses in security rules. Which condition accounts for that result?

- **A — Incorrect.** The review examined only one NSG and missed a higher-priority rule from the other association.
  The review examined only one NSG and missed a higher-priority rule from the other association. The application traffic-control investigation fault concerns effective security rules. Application traffic-control investigation may fix effective security rules, yet application security groups still fails; this application traffic-control investigation diagnosis of effective security rules is wrong for application security groups.
- **B — Incorrect.** Propagation is disabled, so the expected on-premises routes never reach the subnet.
  Propagation is disabled, so the expected on-premises routes never reach the subnet. The application traffic-control investigation fault concerns gateway route propagation. Application traffic-control investigation has gateway route propagation impact, but application security groups is the application traffic-control investigation failed path; the gateway route propagation state cannot produce application security groups failure.
- **C — Correct.** The VM's NIC was never added to the ASG referenced by the allow rule.
  For the application traffic-control investigation, the application security groups failure is causal: the VM's NIC was never added to the ASG referenced by the allow rule. Correcting it restores the ability to refer to application-role groups instead of fixed addresses in security rules.
- **D — Incorrect.** The subnet NSG allows the flow, but the NIC NSG denies it.
  The subnet NSG allows the flow, but the NIC NSG denies it. The application traffic-control investigation fault concerns subnet and NIC NSGs. Application traffic-control investigation failed on application security groups; this subnet and NIC NSGs finding redirects application traffic-control investigation remediation away from application security groups.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups)

**Source reviewed:** 2026-08-31

## LAB18-Q35 — B

**Question:** The traffic-flow investigation evidence shows the application traffic-control investigation cannot see the combined security rules that actually apply to one interface. Which root cause fits that evidence?

- **A — Incorrect.** Troubleshooting selected a broader default route even though a more-specific route exists.
  Troubleshooting selected a broader default route even though a more-specific route exists. The application traffic-control investigation fault concerns longest-prefix route selection. Application traffic-control investigation has longest-prefix route selection impact, but effective security rules is the application traffic-control investigation failed path; the longest-prefix route selection state cannot produce effective security rules failure.
- **B — Correct.** The review examined only one NSG and missed a higher-priority rule from the other association.
  The review examined only one NSG and missed a higher-priority rule from the other association. The finding is specific to effective security rules in the application traffic-control investigation; repairing effective security rules restores the application traffic-control investigation ability to see the combined security rules that actually apply to one interface.
- **C — Incorrect.** The diagnostic used the wrong local port and therefore evaluated a different flow.
  The diagnostic used the wrong local port and therefore evaluated a different flow. The application traffic-control investigation fault concerns IP flow verification. Application traffic-control investigation failed on effective security rules; this IP flow verification finding redirects application traffic-control investigation remediation away from effective security rules.
- **D — Incorrect.** The VM's NIC was never added to the ASG referenced by the allow rule.
  The VM's NIC was never added to the ASG referenced by the allow rule. The application traffic-control investigation fault concerns application security groups. Application traffic-control investigation may fix application security groups, yet effective security rules still fails; this application traffic-control investigation diagnosis of application security groups is wrong for effective security rules.

**Objectives:** `NW-SECURE-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q36 — A

**Question:** Although the application traffic-control investigation is meant to let the traffic-flow investigation select the most specific destination route before considering route origin, its checkpoint fails. Which traffic-flow investigation defect explains the failure?

- **A — Correct.** Troubleshooting selected a broader default route even though a more-specific route exists.
  The application traffic-control investigation cannot select the most specific destination route before considering route origin because of this longest-prefix route selection defect: troubleshooting selected a broader default route even though a more-specific route exists. The symptom and repair align.
- **B — Incorrect.** The route table exists but is associated with a different subnet.
  The route table exists but is associated with a different subnet. The application traffic-control investigation fault concerns user-defined route overrides. Application traffic-control investigation failed on longest-prefix route selection; this user-defined route overrides finding redirects application traffic-control investigation remediation away from longest-prefix route selection.
- **C — Incorrect.** A broad deny rule has a lower priority number than the required allow rule.
  A broad deny rule has a lower priority number than the required allow rule. The application traffic-control investigation fault concerns NSG rule priorities. Application traffic-control investigation may fix NSG rule priorities, yet longest-prefix route selection still fails; this application traffic-control investigation diagnosis of NSG rule priorities is wrong for longest-prefix route selection.
- **D — Incorrect.** The review examined only one NSG and missed a higher-priority rule from the other association.
  The review examined only one NSG and missed a higher-priority rule from the other association. The application traffic-control investigation fault concerns effective security rules. Application traffic-control investigation has effective security rules impact, but longest-prefix route selection is the application traffic-control investigation failed path; the effective security rules state cannot produce longest-prefix route selection failure.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q37 — D

**Question:** The traffic-flow investigation support team isolated the application traffic-control investigation incident to the attempt to override an applicable system path with an intentional custom route. Which condition prevents success?

- **A — Incorrect.** The route points to an old NVA address that is no longer assigned.
  The route points to an old NVA address that is no longer assigned. The application traffic-control investigation fault concerns virtual appliance next hops. Application traffic-control investigation failed on user-defined route overrides; this virtual appliance next hops finding redirects application traffic-control investigation remediation away from user-defined route overrides.
- **B — Incorrect.** Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow.
  Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow. The application traffic-control investigation fault concerns stateful NSG processing. Application traffic-control investigation may fix stateful NSG processing, yet user-defined route overrides still fails; this application traffic-control investigation diagnosis of stateful NSG processing is wrong for user-defined route overrides.
- **C — Incorrect.** Troubleshooting selected a broader default route even though a more-specific route exists.
  Troubleshooting selected a broader default route even though a more-specific route exists. The application traffic-control investigation fault concerns longest-prefix route selection. Application traffic-control investigation has longest-prefix route selection impact, but user-defined route overrides is the application traffic-control investigation failed path; the longest-prefix route selection state cannot produce user-defined route overrides failure.
- **D — Correct.** The route table exists but is associated with a different subnet.
  The route table exists but is associated with a different subnet. Removing this user-defined route overrides condition lets the application traffic-control investigation override an applicable system path with an intentional custom route while leaving healthy controls unchanged.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q38 — D

**Question:** An application traffic-control investigation query surprises the network security administrator diagnosing application traffic flow during the traffic-flow investigation attempt to send traffic through a reachable forwarding appliance. Which finding explains it?

- **A — Incorrect.** Propagation is disabled, so the expected on-premises routes never reach the subnet.
  Propagation is disabled, so the expected on-premises routes never reach the subnet. The application traffic-control investigation fault concerns gateway route propagation. Application traffic-control investigation may fix gateway route propagation, yet virtual appliance next hops still fails; this application traffic-control investigation diagnosis of gateway route propagation is wrong for virtual appliance next hops.
- **B — Incorrect.** The subnet NSG allows the flow, but the NIC NSG denies it.
  The subnet NSG allows the flow, but the NIC NSG denies it. The application traffic-control investigation fault concerns subnet and NIC NSGs. Application traffic-control investigation has subnet and NIC NSGs impact, but virtual appliance next hops is the application traffic-control investigation failed path; the subnet and NIC NSGs state cannot produce virtual appliance next hops failure.
- **C — Incorrect.** The route table exists but is associated with a different subnet.
  The route table exists but is associated with a different subnet. The application traffic-control investigation fault concerns user-defined route overrides. Application traffic-control investigation could repair user-defined route overrides while virtual appliance next hops stays broken in application traffic-control investigation; the application traffic-control investigation remains unable to send traffic through a reachable forwarding appliance.
- **D — Correct.** The route points to an old NVA address that is no longer assigned.
  The route points to an old NVA address that is no longer assigned. In application traffic-control investigation, this virtual appliance next hops cause matches the failure to send traffic through a reachable forwarding appliance.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q39 — C

**Question:** Other application traffic-control investigation components are healthy, but the traffic-flow investigation still cannot control whether learned gateway paths enter a subnet route table. Which state causes the isolated failure?

- **A — Incorrect.** The diagnostic used the wrong local port and therefore evaluated a different flow.
  The diagnostic used the wrong local port and therefore evaluated a different flow. The application traffic-control investigation fault concerns IP flow verification. Application traffic-control investigation has IP flow verification impact, but gateway route propagation is the application traffic-control investigation failed path; the IP flow verification state cannot produce gateway route propagation failure.
- **B — Incorrect.** The VM's NIC was never added to the ASG referenced by the allow rule.
  The VM's NIC was never added to the ASG referenced by the allow rule. The application traffic-control investigation fault concerns application security groups. Application traffic-control investigation could repair application security groups while gateway route propagation stays broken in application traffic-control investigation; the application traffic-control investigation remains unable to control whether learned gateway paths enter a subnet route table.
- **C — Correct.** Propagation is disabled, so the expected on-premises routes never reach the subnet.
  Propagation is disabled, so the expected on-premises routes never reach the subnet. This application traffic-control investigation condition breaks gateway route propagation, explaining why operators cannot control whether learned gateway paths enter a subnet route table.
- **D — Incorrect.** The route points to an old NVA address that is no longer assigned.
  The route points to an old NVA address that is no longer assigned. The application traffic-control investigation fault concerns virtual appliance next hops. Application traffic-control investigation may fix virtual appliance next hops, yet gateway route propagation still fails; this application traffic-control investigation diagnosis of virtual appliance next hops is wrong for gateway route propagation.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q40 — B

**Question:** During a traffic-flow investigation fault drill, the application traffic-control investigation does not ask the platform which security rule allows or denies a specific flow. Which finding identifies the defect?

- **A — Incorrect.** A broad deny rule has a lower priority number than the required allow rule.
  A broad deny rule has a lower priority number than the required allow rule. The application traffic-control investigation fault concerns NSG rule priorities. Application traffic-control investigation could repair NSG rule priorities while IP flow verification stays broken in application traffic-control investigation; the application traffic-control investigation remains unable to ask the platform which security rule allows or denies a specific flow.
- **B — Correct.** The diagnostic used the wrong local port and therefore evaluated a different flow.
  For the application traffic-control investigation, the IP flow verification failure is causal: the diagnostic used the wrong local port and therefore evaluated a different flow. Correcting it restores the ability to ask the platform which security rule allows or denies a specific flow.
- **C — Incorrect.** The review examined only one NSG and missed a higher-priority rule from the other association.
  The review examined only one NSG and missed a higher-priority rule from the other association. The application traffic-control investigation fault concerns effective security rules. Application traffic-control investigation may fix effective security rules, yet IP flow verification still fails; this application traffic-control investigation diagnosis of effective security rules is wrong for IP flow verification.
- **D — Incorrect.** Propagation is disabled, so the expected on-premises routes never reach the subnet.
  Propagation is disabled, so the expected on-premises routes never reach the subnet. The application traffic-control investigation fault concerns gateway route propagation. Application traffic-control investigation has gateway route propagation impact, but IP flow verification is the application traffic-control investigation failed path; the gateway route propagation state cannot produce IP flow verification failure.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Network Watcher IP flow verify](https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q41 — A

**Question:** To satisfy the traffic-flow investigation requirement, operators must change the application traffic-control investigation configuration and prove it can ensure the intended security rule is evaluated before a broader conflicting rule. Which sequence is coherent?

- **A — Correct.** First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple.
  First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple. The application traffic-control investigation uses its NSG rule priorities mutation gate and NSG rule priorities verification gate before it can ensure the intended security rule is evaluated before a broader conflicting rule.
- **B — Incorrect.** First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.
  First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG. This application traffic-control investigation pair serves subnet and NIC NSGs. Application traffic-control investigation proves subnet and NIC NSGs, but NSG rule priorities lacks implementation in application traffic-control investigation and NSG rule priorities proof; the NSG rule priorities outcome to ensure the intended security rule is evaluated before a broader conflicting rule remains open.
- **C — Incorrect.** First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes.
  First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes. This application traffic-control investigation pair serves user-defined route overrides. Application traffic-control investigation uses user-defined route overrides for both steps; NSG rule priorities remains untouched in application traffic-control investigation, so its NSG rule priorities gate to ensure the intended security rule is evaluated before a broader conflicting rule fails.
- **D — Incorrect.** First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.
  First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC. This application traffic-control investigation pair serves virtual appliance next hops. Application traffic-control investigation closes virtual appliance next hops, not NSG rule priorities; without the NSG rule priorities workflow, it cannot ensure the intended security rule is evaluated before a broader conflicting rule.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q42 — A

**Question:** The network security administrator diagnosing application traffic flow needs a safe application traffic-control investigation change to allow return packets for an established permitted flow without a mirror rule, followed by traffic-flow investigation evidence. Which pair merits approval?

- **A — Correct.** First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
  The application traffic-control investigation gets a complete stateful NSG processing sequence here: first, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path. Read-back evidence follows the change.
- **B — Incorrect.** First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
  First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles. This application traffic-control investigation pair serves application security groups. Application traffic-control investigation uses application security groups for both steps; stateful NSG processing remains untouched in application traffic-control investigation, so its stateful NSG processing gate to allow return packets for an established permitted flow without a mirror rule fails.
- **C — Incorrect.** First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.
  First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC. This application traffic-control investigation pair serves virtual appliance next hops. Application traffic-control investigation closes virtual appliance next hops, not stateful NSG processing; without the stateful NSG processing workflow, it cannot allow return packets for an established permitted flow without a mirror rule.
- **D — Incorrect.** First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
  First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway. This application traffic-control investigation pair serves gateway route propagation. Gateway route propagation cannot replace stateful NSG processing in application traffic-control investigation. Use this stateful NSG processing pair instead: First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q43 — D

**Question:** The application traffic-control investigation has two traffic-flow investigation gates: account for security filters applied at both subnet and network-interface scopes, then prove the application traffic-control investigation state. Which traffic-flow investigation sequence works?

- **A — Incorrect.** First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
  First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority. This application traffic-control investigation pair serves effective security rules. Application traffic-control investigation uses effective security rules for both steps; subnet and NIC NSGs remains untouched in application traffic-control investigation, so its subnet and NIC NSGs gate to account for security filters applied at both subnet and network-interface scopes fails.
- **B — Incorrect.** First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
  First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway. This application traffic-control investigation pair serves gateway route propagation. Application traffic-control investigation closes gateway route propagation, not subnet and NIC NSGs; without the subnet and NIC NSGs workflow, it cannot account for security filters applied at both subnet and network-interface scopes.
- **C — Incorrect.** First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence.
  First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence. This application traffic-control investigation pair serves IP flow verification. IP flow verification cannot replace subnet and NIC NSGs in application traffic-control investigation. Use this subnet and NIC NSGs pair instead: First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.
- **D — Correct.** First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.
  First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG. This ordered subnet and NIC NSGs workflow lets the application traffic-control investigation account for security filters applied at both subnet and network-interface scopes and then verify the resulting state.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q44 — B

**Question:** Which traffic-flow investigation path makes the application traffic-control investigation able to refer to application-role groups instead of fixed addresses in security rules, then inspects the defining properties?

- **A — Incorrect.** First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.
  First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP. This application traffic-control investigation pair serves longest-prefix route selection. Application traffic-control investigation closes longest-prefix route selection, not application security groups; without the application security groups workflow, it cannot refer to application-role groups instead of fixed addresses in security rules.
- **B — Correct.** First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
  First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles. For application traffic-control investigation, the application security groups operation precedes its application security groups read-back check, allowing it to refer to application-role groups instead of fixed addresses in security rules.
- **C — Incorrect.** First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence.
  First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence. This application traffic-control investigation pair serves IP flow verification. Application traffic-control investigation proves IP flow verification, but application security groups lacks implementation in application traffic-control investigation and application security groups proof; the application security groups outcome to refer to application-role groups instead of fixed addresses in security rules remains open.
- **D — Incorrect.** First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple.
  First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple. This application traffic-control investigation pair serves NSG rule priorities. Application traffic-control investigation uses NSG rule priorities for both steps; application security groups remains untouched in application traffic-control investigation, so its application security groups gate to refer to application-role groups instead of fixed addresses in security rules fails.

**Objectives:** `NW-SECURE-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups)

**Source reviewed:** 2026-08-31

## LAB18-Q45 — B

**Question:** At the application traffic-control investigation approval gate, operators must show that the traffic-flow investigation can see the combined security rules that actually apply to one interface. Which traffic-flow investigation configure-and-check pair is defensible?

- **A — Incorrect.** First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes.
  First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes. This application traffic-control investigation pair serves user-defined route overrides. User-defined route overrides cannot replace effective security rules in application traffic-control investigation. Use this effective security rules pair instead: First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
- **B — Correct.** First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
  First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority. In the application traffic-control investigation, the first effective security rules step runs; the application traffic-control investigation then reads effective security rules state to prove it can see the combined security rules that actually apply to one interface.
- **C — Incorrect.** First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple.
  First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple. This application traffic-control investigation pair serves NSG rule priorities. Application traffic-control investigation uses NSG rule priorities for both steps; effective security rules remains untouched in application traffic-control investigation, so its effective security rules gate to see the combined security rules that actually apply to one interface fails.
- **D — Incorrect.** First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
  First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path. This application traffic-control investigation pair serves stateful NSG processing. Application traffic-control investigation closes stateful NSG processing, not effective security rules; without the effective security rules workflow, it cannot see the combined security rules that actually apply to one interface.

**Objectives:** `NW-SECURE-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Azure network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q46 — C

**Question:** The application traffic-control investigation forbids a partial traffic-flow investigation result. Operators must first select the most specific destination route before considering route origin and afterward confirm the application traffic-control investigation outcome. Which traffic-flow investigation sequence is complete?

- **A — Incorrect.** First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.
  First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC. This application traffic-control investigation pair serves virtual appliance next hops. Application traffic-control investigation proves virtual appliance next hops, but longest-prefix route selection lacks implementation in application traffic-control investigation and longest-prefix route selection proof; the longest-prefix route selection outcome to select the most specific destination route before considering route origin remains open.
- **B — Incorrect.** First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
  First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path. This application traffic-control investigation pair serves stateful NSG processing. Application traffic-control investigation uses stateful NSG processing for both steps; longest-prefix route selection remains untouched in application traffic-control investigation, so its longest-prefix route selection gate to select the most specific destination route before considering route origin fails.
- **C — Correct.** First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.
  For the application traffic-control investigation, the safe longest-prefix route selection order is: first, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP. The application traffic-control investigation records longest-prefix route selection proof after configuration.
- **D — Incorrect.** First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.
  First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG. This application traffic-control investigation pair serves subnet and NIC NSGs. Subnet and NIC NSGs cannot replace longest-prefix route selection in application traffic-control investigation. Use this longest-prefix route selection pair instead: First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB18-CP01`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q47 — C

**Question:** Only the application traffic-control investigation change needed to override an applicable system path with an intentional custom route is allowed, and traffic-flow investigation proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
  First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway. This application traffic-control investigation pair serves gateway route propagation. Application traffic-control investigation uses gateway route propagation for both steps; user-defined route overrides remains untouched in application traffic-control investigation, so its user-defined route overrides gate to override an applicable system path with an intentional custom route fails.
- **B — Incorrect.** First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.
  First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG. This application traffic-control investigation pair serves subnet and NIC NSGs. Application traffic-control investigation closes subnet and NIC NSGs, not user-defined route overrides; without the user-defined route overrides workflow, it cannot override an applicable system path with an intentional custom route.
- **C — Correct.** First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes.
  First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes. The application traffic-control investigation uses its user-defined route overrides mutation gate and user-defined route overrides verification gate before it can override an applicable system path with an intentional custom route.
- **D — Incorrect.** First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
  First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles. This application traffic-control investigation pair serves application security groups. Application traffic-control investigation proves application security groups, but user-defined route overrides lacks implementation in application traffic-control investigation and user-defined route overrides proof; the user-defined route overrides outcome to override an applicable system path with an intentional custom route remains open.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB18-CP02`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q48 — D

**Question:** The application traffic-control investigation runbook separates traffic-flow investigation mutation from validation while it must send traffic through a reachable forwarding appliance. Which sequence proves it cleanly?

- **A — Incorrect.** First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence.
  First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence. This application traffic-control investigation pair serves IP flow verification. Application traffic-control investigation closes IP flow verification, not virtual appliance next hops; without the virtual appliance next hops workflow, it cannot send traffic through a reachable forwarding appliance.
- **B — Incorrect.** First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
  First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles. This application traffic-control investigation pair serves application security groups. Application security groups cannot replace virtual appliance next hops in application traffic-control investigation. Use this virtual appliance next hops pair instead: First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.
- **C — Incorrect.** First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
  First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority. This application traffic-control investigation pair serves effective security rules. Application traffic-control investigation proves effective security rules, but virtual appliance next hops lacks implementation in application traffic-control investigation and virtual appliance next hops proof; the virtual appliance next hops outcome to send traffic through a reachable forwarding appliance remains open.
- **D — Correct.** First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.
  The application traffic-control investigation gets a complete virtual appliance next hops sequence here: first, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC. Read-back evidence follows the change.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB18-CP03`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q49 — A

**Question:** The application traffic-control investigation checkpoint requires both this traffic-flow investigation outcome—control whether learned gateway paths enter a subnet route table—and a read-only application traffic-control investigation state check. Which traffic-flow investigation response is complete?

- **A — Correct.** First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
  First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway. This ordered gateway route propagation workflow lets the application traffic-control investigation control whether learned gateway paths enter a subnet route table and then verify the resulting state.
- **B — Incorrect.** First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple.
  First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple. This application traffic-control investigation pair serves NSG rule priorities. Application traffic-control investigation proves NSG rule priorities, but gateway route propagation lacks implementation in application traffic-control investigation and gateway route propagation proof; the gateway route propagation outcome to control whether learned gateway paths enter a subnet route table remains open.
- **C — Incorrect.** First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
  First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority. This application traffic-control investigation pair serves effective security rules. Application traffic-control investigation uses effective security rules for both steps; gateway route propagation remains untouched in application traffic-control investigation, so its gateway route propagation gate to control whether learned gateway paths enter a subnet route table fails.
- **D — Incorrect.** First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.
  First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP. This application traffic-control investigation pair serves longest-prefix route selection. Application traffic-control investigation closes longest-prefix route selection, not gateway route propagation; without the gateway route propagation workflow, it cannot control whether learned gateway paths enter a subnet route table.

**Objectives:** `NW-VNET-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB18-CP04`).

**Microsoft Learn sources:**

- [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)

**Source reviewed:** 2026-08-31

## LAB18-Q50 — D

**Question:** The application traffic-control investigation runbook must ask the platform which security rule allows or denies a specific flow, then retain traffic-flow investigation read-back evidence. Which application traffic-control investigation pair completes both duties?

- **A — Incorrect.** First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
  First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path. This application traffic-control investigation pair serves stateful NSG processing. Application traffic-control investigation proves stateful NSG processing, but IP flow verification lacks implementation in application traffic-control investigation and IP flow verification proof; the IP flow verification outcome to ask the platform which security rule allows or denies a specific flow remains open.
- **B — Incorrect.** First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.
  First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP. This application traffic-control investigation pair serves longest-prefix route selection. Application traffic-control investigation uses longest-prefix route selection for both steps; IP flow verification remains untouched in application traffic-control investigation, so its IP flow verification gate to ask the platform which security rule allows or denies a specific flow fails.
- **C — Incorrect.** First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes.
  First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes. This application traffic-control investigation pair serves user-defined route overrides. Application traffic-control investigation closes user-defined route overrides, not IP flow verification; without the IP flow verification workflow, it cannot ask the platform which security rule allows or denies a specific flow.
- **D — Correct.** First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence.
  First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence. For application traffic-control investigation, the IP flow verification operation precedes its IP flow verification read-back check, allowing it to ask the platform which security rule allows or denies a specific flow.

**Objectives:** `NW-VNET-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB18-CP05`).

**Microsoft Learn sources:**

- [Network Watcher IP flow verify](https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview)

**Source reviewed:** 2026-08-31
