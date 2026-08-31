# Lab 18 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB18-Q01 — Foundational

A traffic-flow investigation peer review asks how the application traffic-control investigation should handle this outcome: ensure the intended security rule is evaluated before a broader conflicting rule. Which explanation is accurate?

- A. NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule.
- B. Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet.
- C. NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow.
- D. A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path.

## LAB18-Q02 — Foundational

For the application traffic-control investigation, the traffic-flow investigation plan must allow return packets for an established permitted flow without a mirror rule. Which statement about traffic-flow investigation belongs in the application traffic-control investigation record?

- A. NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule.
- B. When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes.
- C. Azure chooses the most specific matching route before applying route-source precedence rules.
- D. Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table.

## LAB18-Q03 — Foundational

The traffic-flow investigation review compares four claims for the application traffic-control investigation requirement to account for security filters applied at both subnet and network-interface scopes. Which claim is technically sound?

- A. An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses.
- B. A valid UDR can override a system route for the same or a broader destination prefix.
- C. When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes.
- D. IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule.

## LAB18-Q04 — Foundational

The traffic-flow investigation architecture note requires the application traffic-control investigation environment to refer to application-role groups instead of fixed addresses in security rules. Which statement defines the relevant traffic-flow investigation boundary?

- A. Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet.
- B. A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path.
- C. An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses.
- D. NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow.

## LAB18-Q05 — Foundational

A new traffic-flow investigation operator must explain why the application traffic-control investigation can see the combined security rules that actually apply to one interface. Which explanation is accurate?

- A. Azure chooses the most specific matching route before applying route-source precedence rules.
- B. Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet.
- C. Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table.
- D. NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule.

## LAB18-Q06 — Foundational

The application traffic-control investigation acceptance criteria require operators to select the most specific destination route before considering route origin. Which service fact supports that requirement?

- A. A valid UDR can override a system route for the same or a broader destination prefix.
- B. Azure chooses the most specific matching route before applying route-source precedence rules.
- C. IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule.
- D. When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes.

## LAB18-Q07 — Foundational

A traffic-flow investigation reviewer challenges whether the application traffic-control investigation can override an applicable system path with an intentional custom route. Which response resolves the concern?

- A. A valid UDR can override a system route for the same or a broader destination prefix.
- B. A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path.
- C. NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow.
- D. An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses.

## LAB18-Q08 — Foundational

The application traffic-control investigation handoff omits the traffic-flow investigation rule needed to send traffic through a reachable forwarding appliance. Which statement should the team add?

- A. Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table.
- B. A VirtualAppliance route requires a reachable next-hop private IP and IP forwarding on the appliance path.
- C. NSG flow records are stateful, so return traffic for an allowed established flow does not require a mirrored rule.
- D. Effective security rules combine default and custom rules from every NSG associated with the NIC and subnet.

## LAB18-Q09 — Foundational

A traffic-flow investigation incident review of the application traffic-control investigation depends on the ability to control whether learned gateway paths enter a subnet route table. Which platform description is reliable?

- A. IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule.
- B. When NSGs apply at both subnet and NIC, a flow must be allowed by the effective rules at both scopes.
- C. Gateway route propagation can add learned routes to a subnet unless it is disabled on the associated route table.
- D. Azure chooses the most specific matching route before applying route-source precedence rules.

## LAB18-Q10 — Foundational

A network security administrator diagnosing application traffic flow is updating the traffic-flow investigation runbook. The requirement is to ask the platform which security rule allows or denies a specific flow. Which statement describes Azure behavior correctly?

- A. IP flow verify reports whether a specified packet would be allowed or denied and identifies the matching NSG rule.
- B. NSG rules are evaluated from lower numeric priority to higher until the first matching rule decides the flow.
- C. An ASG lets NSG rules refer to groups of NIC IP configurations by application role instead of fixed addresses.
- D. A valid UDR can override a system route for the same or a broader destination prefix.

## LAB18-Q11 — Foundational

The approach for the application traffic-control investigation is approved, but the traffic-flow investigation environment still cannot ensure the intended security rule is evaluated before a broader conflicting rule. Which implementation step closes the gap?

- A. Review both associations and keep layered rules consistent with the intended flow.
- B. Compare every matching prefix and identify the longest prefix for the destination address.
- C. Choose propagation behavior explicitly when combining a gateway with custom routes.
- D. Give the narrow required rule a unique priority that precedes conflicting broader rules.

## LAB18-Q12 — Foundational

The network security administrator diagnosing application traffic flow may change the application traffic-control investigation only to allow return packets for an established permitted flow without a mirror rule. Which traffic-flow investigation action stays within that assignment?

- A. Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules.
- B. Associate the route table with the source subnet and define the intended next hop.
- C. Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection.
- D. Authorize the initiating direction and avoid redundant return-only rules.

## LAB18-Q13 — Foundational

A traffic-flow investigation dry run shows no application traffic-control investigation command will account for security filters applied at both subnet and network-interface scopes. Which action belongs before execution?

- A. Review both associations and keep layered rules consistent with the intended flow.
- B. Use the effective-rule view before modifying an individual NSG during troubleshooting.
- C. Set the NVA private address as nextHopIpAddress and enable forwarding where required.
- D. Give the narrow required rule a unique priority that precedes conflicting broader rules.

## LAB18-Q14 — Foundational

For the application traffic-control investigation, operators need to refer to application-role groups instead of fixed addresses in security rules. Which change realizes that requirement?

- A. Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules.
- B. Compare every matching prefix and identify the longest prefix for the destination address.
- C. Choose propagation behavior explicitly when combining a gateway with custom routes.
- D. Authorize the initiating direction and avoid redundant return-only rules.

## LAB18-Q15 — Foundational

Operators must automate the application traffic-control investigation change needed to see the combined security rules that actually apply to one interface. Which traffic-flow investigation operation belongs in the runbook?

- A. Associate the route table with the source subnet and define the intended next hop.
- B. Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection.
- C. Use the effective-rule view before modifying an individual NSG during troubleshooting.
- D. Review both associations and keep layered rules consistent with the intended flow.

## LAB18-Q16 — Applied

An application traffic-control investigation review finds traffic-flow investigation drift from the need to select the most specific destination route before considering route origin. Which correction addresses that drift?

- A. Set the NVA private address as nextHopIpAddress and enable forwarding where required.
- B. Compare every matching prefix and identify the longest prefix for the destination address.
- C. Give the narrow required rule a unique priority that precedes conflicting broader rules.
- D. Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules.

## LAB18-Q17 — Applied

The application traffic-control investigation window permits only the traffic-flow investigation change needed to override an applicable system path with an intentional custom route. Which option respects the boundary?

- A. Choose propagation behavior explicitly when combining a gateway with custom routes.
- B. Authorize the initiating direction and avoid redundant return-only rules.
- C. Use the effective-rule view before modifying an individual NSG during troubleshooting.
- D. Associate the route table with the source subnet and define the intended next hop.

## LAB18-Q18 — Applied

The traffic-flow investigation preflight has passed; the application traffic-control investigation must now send traffic through a reachable forwarding appliance. Which operation should run?

- A. Set the NVA private address as nextHopIpAddress and enable forwarding where required.
- B. Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection.
- C. Review both associations and keep layered rules consistent with the intended flow.
- D. Compare every matching prefix and identify the longest prefix for the destination address.

## LAB18-Q19 — Applied

The application traffic-control investigation plan must control whether learned gateway paths enter a subnet route table while limiting the mutation scope to traffic-flow investigation. Which action is appropriate?

- A. Give the narrow required rule a unique priority that precedes conflicting broader rules.
- B. Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules.
- C. Choose propagation behavior explicitly when combining a gateway with custom routes.
- D. Associate the route table with the source subnet and define the intended next hop.

## LAB18-Q20 — Applied

A traffic-flow investigation ticket in the application traffic-control investigation says to ask the platform which security rule allows or denies a specific flow. Which traffic-flow investigation action completes the application traffic-control investigation request with minimal change?

- A. Authorize the initiating direction and avoid redundant return-only rules.
- B. Use the effective-rule view before modifying an individual NSG during troubleshooting.
- C. Set the NVA private address as nextHopIpAddress and enable forwarding where required.
- D. Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection.

## LAB18-Q21 — Applied

The traffic-flow investigation log says the application traffic-control investigation can now ensure the intended security rule is evaluated before a broader conflicting rule. Which traffic-flow investigation state should the application traffic-control investigation acceptance test retain?

- A. Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
- B. Query subnet route-table association and the NIC's effective routes.
- C. Capture access, rule name, and the tested five-tuple in validation evidence.
- D. List rules ordered by priority and identify the first match for the test five-tuple.

## LAB18-Q22 — Applied

The application traffic-control investigation rejects traffic-flow investigation exit status as proof it can allow return packets for an established permitted flow without a mirror rule. Which application traffic-control investigation result is valid evidence?

- A. List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
- B. Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
- C. Inspect the effective route and verify forwarding and reachability on the appliance NIC.
- D. List rules ordered by priority and identify the first match for the test five-tuple.

## LAB18-Q23 — Applied

The traffic-flow investigation validator needs one application traffic-control investigation query after the change to account for security filters applied at both subnet and network-interface scopes. Which traffic-flow investigation property should the application traffic-control investigation validator inspect?

- A. Read effective routes and show the selected prefix, next hop type, and next hop IP.
- B. Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
- C. Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
- D. Query the NIC's effective security rules and trace each match to its source NSG.

## LAB18-Q24 — Applied

The network security administrator diagnosing application traffic flow must confirm the application traffic-control investigation, without mutation, can refer to application-role groups instead of fixed addresses in security rules. Which traffic-flow investigation check qualifies?

- A. Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
- B. Query subnet route-table association and the NIC's effective routes.
- C. Capture access, rule name, and the tested five-tuple in validation evidence.
- D. Query the NIC's effective security rules and trace each match to its source NSG.

## LAB18-Q25 — Applied

The application traffic-control investigation configuration is complete; the traffic-flow investigation reviewers need evidence it can see the combined security rules that actually apply to one interface. Which observation shows success?

- A. List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
- B. Inspect the effective route and verify forwarding and reachability on the appliance NIC.
- C. List rules ordered by priority and identify the first match for the test five-tuple.
- D. Query ASG membership and confirm the effective rule resolves the intended source and destination roles.

## LAB18-Q26 — Applied

The traffic-flow investigation validation asks whether the application traffic-control investigation can select the most specific destination route before considering route origin. Which observable state is strongest?

- A. Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
- B. Read effective routes and show the selected prefix, next hop type, and next hop IP.
- C. Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
- D. List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.

## LAB18-Q27 — Applied

An application traffic-control investigation review must prove the traffic-flow investigation ability to override an applicable system path with an intentional custom route. Which check avoids an adjacent feature?

- A. Capture access, rule name, and the tested five-tuple in validation evidence.
- B. Query the NIC's effective security rules and trace each match to its source NSG.
- C. Query subnet route-table association and the NIC's effective routes.
- D. Read effective routes and show the selected prefix, next hop type, and next hop IP.

## LAB18-Q28 — Applied

The application traffic-control investigation evidence bundle needs a traffic-flow investigation result showing it can send traffic through a reachable forwarding appliance. Which result belongs in the checkpoint?

- A. List rules ordered by priority and identify the first match for the test five-tuple.
- B. Inspect the effective route and verify forwarding and reachability on the appliance NIC.
- C. Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
- D. Query subnet route-table association and the NIC's effective routes.

## LAB18-Q29 — Applied

Before application traffic-control investigation cleanup, the traffic-flow investigation team must reconfirm it can control whether learned gateway paths enter a subnet route table. Which read-only inspection should run?

- A. Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
- B. List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
- C. Inspect the effective route and verify forwarding and reachability on the appliance NIC.
- D. Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.

## LAB18-Q30 — Applied

The application traffic-control investigation setup reports success after the traffic-flow investigation attempt to ask the platform which security rule allows or denies a specific flow. Which traffic-flow investigation read-only observation proves the application traffic-control investigation outcome?

- A. Capture access, rule name, and the tested five-tuple in validation evidence.
- B. Query the NIC's effective security rules and trace each match to its source NSG.
- C. Read effective routes and show the selected prefix, next hop type, and next hop IP.
- D. Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.

## LAB18-Q31 — Applied

The application traffic-control investigation setup finishes, yet the traffic-flow investigation cannot ensure the intended security rule is evaluated before a broader conflicting rule. Which misconfiguration explains the mismatch?

- A. Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow.
- B. Troubleshooting selected a broader default route even though a more-specific route exists.
- C. A broad deny rule has a lower priority number than the required allow rule.
- D. The diagnostic used the wrong local port and therefore evaluated a different flow.

## LAB18-Q32 — Applied

A traffic-flow investigation break/fix in the application traffic-control investigation fails when operators try to allow return packets for an established permitted flow without a mirror rule. Which diagnosis fits?

- A. The subnet NSG allows the flow, but the NIC NSG denies it.
- B. Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow.
- C. The route table exists but is associated with a different subnet.
- D. A broad deny rule has a lower priority number than the required allow rule.

## LAB18-Q33 — Applied

The application traffic-control investigation troubleshooting scope is the traffic-flow investigation need to account for security filters applied at both subnet and network-interface scopes. Which condition should be corrected first?

- A. The VM's NIC was never added to the ASG referenced by the allow rule.
- B. The subnet NSG allows the flow, but the NIC NSG denies it.
- C. The route points to an old NVA address that is no longer assigned.
- D. Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow.

## LAB18-Q34 — Applied

The application traffic-control investigation result is partial because the traffic-flow investigation cannot refer to application-role groups instead of fixed addresses in security rules. Which condition accounts for that result?

- A. The review examined only one NSG and missed a higher-priority rule from the other association.
- B. Propagation is disabled, so the expected on-premises routes never reach the subnet.
- C. The VM's NIC was never added to the ASG referenced by the allow rule.
- D. The subnet NSG allows the flow, but the NIC NSG denies it.

## LAB18-Q35 — Applied

The traffic-flow investigation evidence shows the application traffic-control investigation cannot see the combined security rules that actually apply to one interface. Which root cause fits that evidence?

- A. Troubleshooting selected a broader default route even though a more-specific route exists.
- B. The review examined only one NSG and missed a higher-priority rule from the other association.
- C. The diagnostic used the wrong local port and therefore evaluated a different flow.
- D. The VM's NIC was never added to the ASG referenced by the allow rule.

## LAB18-Q36 — Applied

Although the application traffic-control investigation is meant to let the traffic-flow investigation select the most specific destination route before considering route origin, its checkpoint fails. Which traffic-flow investigation defect explains the failure?

- A. Troubleshooting selected a broader default route even though a more-specific route exists.
- B. The route table exists but is associated with a different subnet.
- C. A broad deny rule has a lower priority number than the required allow rule.
- D. The review examined only one NSG and missed a higher-priority rule from the other association.

## LAB18-Q37 — Applied

The traffic-flow investigation support team isolated the application traffic-control investigation incident to the attempt to override an applicable system path with an intentional custom route. Which condition prevents success?

- A. The route points to an old NVA address that is no longer assigned.
- B. Troubleshooting adds an unnecessary mirrored rule instead of checking the initiating flow.
- C. Troubleshooting selected a broader default route even though a more-specific route exists.
- D. The route table exists but is associated with a different subnet.

## LAB18-Q38 — Applied

An application traffic-control investigation query surprises the network security administrator diagnosing application traffic flow during the traffic-flow investigation attempt to send traffic through a reachable forwarding appliance. Which finding explains it?

- A. Propagation is disabled, so the expected on-premises routes never reach the subnet.
- B. The subnet NSG allows the flow, but the NIC NSG denies it.
- C. The route table exists but is associated with a different subnet.
- D. The route points to an old NVA address that is no longer assigned.

## LAB18-Q39 — Applied

Other application traffic-control investigation components are healthy, but the traffic-flow investigation still cannot control whether learned gateway paths enter a subnet route table. Which state causes the isolated failure?

- A. The diagnostic used the wrong local port and therefore evaluated a different flow.
- B. The VM's NIC was never added to the ASG referenced by the allow rule.
- C. Propagation is disabled, so the expected on-premises routes never reach the subnet.
- D. The route points to an old NVA address that is no longer assigned.

## LAB18-Q40 — Applied

During a traffic-flow investigation fault drill, the application traffic-control investigation does not ask the platform which security rule allows or denies a specific flow. Which finding identifies the defect?

- A. A broad deny rule has a lower priority number than the required allow rule.
- B. The diagnostic used the wrong local port and therefore evaluated a different flow.
- C. The review examined only one NSG and missed a higher-priority rule from the other association.
- D. Propagation is disabled, so the expected on-premises routes never reach the subnet.

## LAB18-Q41 — Advanced

To satisfy the traffic-flow investigation requirement, operators must change the application traffic-control investigation configuration and prove it can ensure the intended security rule is evaluated before a broader conflicting rule. Which sequence is coherent?

- A. First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple.
- B. First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.
- C. First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes.
- D. First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.

## LAB18-Q42 — Advanced

The network security administrator diagnosing application traffic flow needs a safe application traffic-control investigation change to allow return packets for an established permitted flow without a mirror rule, followed by traffic-flow investigation evidence. Which pair merits approval?

- A. First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
- B. First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
- C. First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.
- D. First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.

## LAB18-Q43 — Advanced

The application traffic-control investigation has two traffic-flow investigation gates: account for security filters applied at both subnet and network-interface scopes, then prove the application traffic-control investigation state. Which traffic-flow investigation sequence works?

- A. First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
- B. First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
- C. First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence.
- D. First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.

## LAB18-Q44 — Advanced

Which traffic-flow investigation path makes the application traffic-control investigation able to refer to application-role groups instead of fixed addresses in security rules, then inspects the defining properties?

- A. First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.
- B. First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
- C. First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence.
- D. First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple.

## LAB18-Q45 — Advanced

At the application traffic-control investigation approval gate, operators must show that the traffic-flow investigation can see the combined security rules that actually apply to one interface. Which traffic-flow investigation configure-and-check pair is defensible?

- A. First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes.
- B. First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
- C. First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple.
- D. First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.

## LAB18-Q46 — Advanced

The application traffic-control investigation forbids a partial traffic-flow investigation result. Operators must first select the most specific destination route before considering route origin and afterward confirm the application traffic-control investigation outcome. Which traffic-flow investigation sequence is complete?

- A. First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.
- B. First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
- C. First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.
- D. First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.

## LAB18-Q47 — Advanced

Only the application traffic-control investigation change needed to override an applicable system path with an intentional custom route is allowed, and traffic-flow investigation proof is mandatory. Which pair fits?

- A. First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
- B. First, Review both associations and keep layered rules consistent with the intended flow. Then, Query the NIC's effective security rules and trace each match to its source NSG.
- C. First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes.
- D. First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles.

## LAB18-Q48 — Advanced

The application traffic-control investigation runbook separates traffic-flow investigation mutation from validation while it must send traffic through a reachable forwarding appliance. Which sequence proves it cleanly?

- A. First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence.
- B. First, Place eligible NIC configurations in role-based ASGs and reference those ASGs in NSG rules. Then, Query ASG membership and confirm the effective rule resolves the intended source and destination roles.
- C. First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
- D. First, Set the NVA private address as nextHopIpAddress and enable forwarding where required. Then, Inspect the effective route and verify forwarding and reachability on the appliance NIC.

## LAB18-Q49 — Advanced

The application traffic-control investigation checkpoint requires both this traffic-flow investigation outcome—control whether learned gateway paths enter a subnet route table—and a read-only application traffic-control investigation state check. Which traffic-flow investigation response is complete?

- A. First, Choose propagation behavior explicitly when combining a gateway with custom routes. Then, Query disableBgpRoutePropagation and inspect effective routes learned from the gateway.
- B. First, Give the narrow required rule a unique priority that precedes conflicting broader rules. Then, List rules ordered by priority and identify the first match for the test five-tuple.
- C. First, Use the effective-rule view before modifying an individual NSG during troubleshooting. Then, List effective rules for the target NIC and match direction, protocol, addresses, ports, and priority.
- D. First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.

## LAB18-Q50 — Advanced

The application traffic-control investigation runbook must ask the platform which security rule allows or denies a specific flow, then retain traffic-flow investigation read-back evidence. Which application traffic-control investigation pair completes both duties?

- A. First, Authorize the initiating direction and avoid redundant return-only rules. Then, Inspect the initiating rule and use flow logs or a connection test to confirm the established response path.
- B. First, Compare every matching prefix and identify the longest prefix for the destination address. Then, Read effective routes and show the selected prefix, next hop type, and next hop IP.
- C. First, Associate the route table with the source subnet and define the intended next hop. Then, Query subnet route-table association and the NIC's effective routes.
- D. First, Run IP flow verify with the exact VM, NIC, direction, protocol, addresses, and ports from the failed connection. Then, Capture access, rule name, and the tested five-tuple in validation evidence.

[Open the answer key](./ANSWERS.md)
