# Lab 20 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB20-Q01 — Foundational

A name-resolution verification reviewer challenges whether the authoritative DNS and Bastion rollout can publish internet records by using Azure-hosted DNS authority. Which response resolves the concern?

- A. Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers.
- B. Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.
- C. Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features.
- D. An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name.

## LAB20-Q02 — Foundational

The authoritative DNS and Bastion rollout handoff omits the name-resolution verification rule needed to make the parent domain direct queries to the Azure-hosted child zone. Which statement should the team add?

- A. A DNS record set groups records of one type and name and applies a shared TTL at that label.
- B. Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers.
- C. Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior.
- D. Azure Bastion uses a supported Standard, static public IP configuration for its managed host.

## LAB20-Q03 — Foundational

A name-resolution verification incident review of the authoritative DNS and Bastion rollout depends on the ability to publish multiple values with the same owner, type, and time-to-live. Which platform description is reliable?

- A. A DNS record set groups records of one type and name and applies a shared TTL at that label.
- B. An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle.
- C. Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet.
- D. Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH.

## LAB20-Q04 — Foundational

A network administrator providing secure management and authoritative DNS is updating the name-resolution verification runbook. The requirement is to point a zone-apex record at an Azure resource without hard-coding its address. Which statement describes Azure behavior correctly?

- A. Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.
- B. An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle.
- C. Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features.
- D. An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name.

## LAB20-Q05 — Foundational

A name-resolution verification peer review asks how the authoritative DNS and Bastion rollout should handle this outcome: control how long a positive answer can remain in recursive caches. Which explanation is accurate?

- A. Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior.
- B. Azure Bastion uses a supported Standard, static public IP configuration for its managed host.
- C. Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.
- D. Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers.

## LAB20-Q06 — Foundational

For the authoritative DNS and Bastion rollout, the name-resolution verification plan must control cache duration for a negative DNS lookup. Which statement about name-resolution verification belongs in the authoritative DNS and Bastion rollout record?

- A. Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet.
- B. Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH.
- C. Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior.
- D. A DNS record set groups records of one type and name and applies a shared TTL at that label.

## LAB20-Q07 — Foundational

The name-resolution verification review compares four claims for the authoritative DNS and Bastion rollout requirement to use the exact reserved subnet name required by the managed jump service. Which claim is technically sound?

- A. Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features.
- B. Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet.
- C. An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name.
- D. An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle.

## LAB20-Q08 — Foundational

The name-resolution verification architecture note requires the authoritative DNS and Bastion rollout environment to allocate a subnet large enough for the managed jump service to scale. Which statement defines the relevant name-resolution verification boundary?

- A. Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features.
- B. Azure Bastion uses a supported Standard, static public IP configuration for its managed host.
- C. Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers.
- D. Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.

## LAB20-Q09 — Foundational

A new name-resolution verification operator must explain why the authoritative DNS and Bastion rollout can attach the supported public address configuration to the managed jump host. Which explanation is accurate?

- A. Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH.
- B. Azure Bastion uses a supported Standard, static public IP configuration for its managed host.
- C. A DNS record set groups records of one type and name and applies a shared TTL at that label.
- D. Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior.

## LAB20-Q10 — Foundational

The authoritative DNS and Bastion rollout acceptance criteria require operators to administer a private virtual machine without assigning it a public address. Which service fact supports that requirement?

- A. An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name.
- B. Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH.
- C. An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle.
- D. Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet.

## LAB20-Q11 — Foundational

The authoritative DNS and Bastion rollout window permits only the name-resolution verification change needed to publish internet records by using Azure-hosted DNS authority. Which option respects the boundary?

- A. Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL.
- B. Create required records before the validation window and account for prior negative responses.
- C. Create the zone for a domain the organization controls and retain its assigned name servers.
- D. Create a Standard static public IP and attach it to the Bastion IP configuration.

## LAB20-Q12 — Foundational

The name-resolution verification preflight has passed; the authoritative DNS and Bastion rollout must now make the parent domain direct queries to the Azure-hosted child zone. Which operation should run?

- A. Copy every assigned Azure DNS name server into the parent delegation.
- B. Use an alias A record when a supported Azure public IP or endpoint should be the record target.
- C. Create the dedicated subnet with the exact reserved name before deploying the host.
- D. Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow.

## LAB20-Q13 — Foundational

The authoritative DNS and Bastion rollout plan must publish multiple values with the same owner, type, and time-to-live while limiting the mutation scope to name-resolution verification. Which action is appropriate?

- A. Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL.
- B. Lower TTL before a planned cutover, wait for prior caches, then update the record.
- C. Allocate an approved /26-or-larger AzureBastionSubnet without other workloads.
- D. Create the zone for a domain the organization controls and retain its assigned name servers.

## LAB20-Q14 — Foundational

A name-resolution verification ticket in the authoritative DNS and Bastion rollout says to point a zone-apex record at an Azure resource without hard-coding its address. Which name-resolution verification action completes the authoritative DNS and Bastion rollout request with minimal change?

- A. Use an alias A record when a supported Azure public IP or endpoint should be the record target.
- B. Create required records before the validation window and account for prior negative responses.
- C. Create a Standard static public IP and attach it to the Bastion IP configuration.
- D. Copy every assigned Azure DNS name server into the parent delegation.

## LAB20-Q15 — Foundational

The approach for the authoritative DNS and Bastion rollout is approved, but the name-resolution verification environment still cannot control how long a positive answer can remain in recursive caches. Which implementation step closes the gap?

- A. Create the dedicated subnet with the exact reserved name before deploying the host.
- B. Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow.
- C. Lower TTL before a planned cutover, wait for prior caches, then update the record.
- D. Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL.

## LAB20-Q16 — Applied

The network administrator providing secure management and authoritative DNS may change the authoritative DNS and Bastion rollout only to control cache duration for a negative DNS lookup. Which name-resolution verification action stays within that assignment?

- A. Allocate an approved /26-or-larger AzureBastionSubnet without other workloads.
- B. Create required records before the validation window and account for prior negative responses.
- C. Create the zone for a domain the organization controls and retain its assigned name servers.
- D. Use an alias A record when a supported Azure public IP or endpoint should be the record target.

## LAB20-Q17 — Applied

A name-resolution verification dry run shows no authoritative DNS and Bastion rollout command will use the exact reserved subnet name required by the managed jump service. Which action belongs before execution?

- A. Create a Standard static public IP and attach it to the Bastion IP configuration.
- B. Copy every assigned Azure DNS name server into the parent delegation.
- C. Lower TTL before a planned cutover, wait for prior caches, then update the record.
- D. Create the dedicated subnet with the exact reserved name before deploying the host.

## LAB20-Q18 — Applied

For the authoritative DNS and Bastion rollout, operators need to allocate a subnet large enough for the managed jump service to scale. Which change realizes that requirement?

- A. Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow.
- B. Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL.
- C. Create required records before the validation window and account for prior negative responses.
- D. Allocate an approved /26-or-larger AzureBastionSubnet without other workloads.

## LAB20-Q19 — Applied

Operators must automate the authoritative DNS and Bastion rollout change needed to attach the supported public address configuration to the managed jump host. Which name-resolution verification operation belongs in the runbook?

- A. Create a Standard static public IP and attach it to the Bastion IP configuration.
- B. Create the zone for a domain the organization controls and retain its assigned name servers.
- C. Use an alias A record when a supported Azure public IP or endpoint should be the record target.
- D. Create the dedicated subnet with the exact reserved name before deploying the host.

## LAB20-Q20 — Applied

An authoritative DNS and Bastion rollout review finds name-resolution verification drift from the need to administer a private virtual machine without assigning it a public address. Which correction addresses that drift?

- A. Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow.
- B. Copy every assigned Azure DNS name server into the parent delegation.
- C. Lower TTL before a planned cutover, wait for prior caches, then update the record.
- D. Allocate an approved /26-or-larger AzureBastionSubnet without other workloads.

## LAB20-Q21 — Applied

An authoritative DNS and Bastion rollout review must prove the name-resolution verification ability to publish internet records by using Azure-hosted DNS authority. Which check avoids an adjacent feature?

- A. Query targetResource.id and resolve the record to the current target address.
- B. Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
- C. Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
- D. Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.

## LAB20-Q22 — Applied

The authoritative DNS and Bastion rollout evidence bundle needs a name-resolution verification result showing it can make the parent domain direct queries to the Azure-hosted child zone. Which result belongs in the checkpoint?

- A. Query authoritative and recursive answers with TTL values during the cutover.
- B. Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
- C. Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
- D. Query NS records from an external resolver and compare them with the zone's assigned servers.

## LAB20-Q23 — Applied

Before authoritative DNS and Bastion rollout cleanup, the name-resolution verification team must reconfirm it can publish multiple values with the same owner, type, and time-to-live. Which read-only inspection should run?

- A. Query the authoritative name servers directly and compare with the recursive resolver response.
- B. Query the exact record-set name and type and compare its TTL and record values.
- C. Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
- D. Query NS records from an external resolver and compare them with the zone's assigned servers.

## LAB20-Q24 — Applied

The authoritative DNS and Bastion rollout setup reports success after the name-resolution verification attempt to point a zone-apex record at an Azure resource without hard-coding its address. Which name-resolution verification read-only observation proves the authoritative DNS and Bastion rollout outcome?

- A. Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
- B. Query targetResource.id and resolve the record to the current target address.
- C. Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
- D. Query the exact record-set name and type and compare its TTL and record values.

## LAB20-Q25 — Applied

The name-resolution verification log says the authoritative DNS and Bastion rollout can now control how long a positive answer can remain in recursive caches. Which name-resolution verification state should the authoritative DNS and Bastion rollout acceptance test retain?

- A. Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
- B. Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
- C. Query targetResource.id and resolve the record to the current target address.
- D. Query authoritative and recursive answers with TTL values during the cutover.

## LAB20-Q26 — Applied

The authoritative DNS and Bastion rollout rejects name-resolution verification exit status as proof it can control cache duration for a negative DNS lookup. Which authoritative DNS and Bastion rollout result is valid evidence?

- A. Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
- B. Query the authoritative name servers directly and compare with the recursive resolver response.
- C. Query NS records from an external resolver and compare them with the zone's assigned servers.
- D. Query authoritative and recursive answers with TTL values during the cutover.

## LAB20-Q27 — Applied

The name-resolution verification validator needs one authoritative DNS and Bastion rollout query after the change to use the exact reserved subnet name required by the managed jump service. Which name-resolution verification property should the authoritative DNS and Bastion rollout validator inspect?

- A. Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
- B. Query the exact record-set name and type and compare its TTL and record values.
- C. Query the authoritative name servers directly and compare with the recursive resolver response.
- D. Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.

## LAB20-Q28 — Applied

The network administrator providing secure management and authoritative DNS must confirm the authoritative DNS and Bastion rollout, without mutation, can allocate a subnet large enough for the managed jump service to scale. Which name-resolution verification check qualifies?

- A. Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
- B. Query targetResource.id and resolve the record to the current target address.
- C. Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
- D. Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.

## LAB20-Q29 — Applied

The authoritative DNS and Bastion rollout configuration is complete; the name-resolution verification reviewers need evidence it can attach the supported public address configuration to the managed jump host. Which observation shows success?

- A. Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
- B. Query NS records from an external resolver and compare them with the zone's assigned servers.
- C. Query authoritative and recursive answers with TTL values during the cutover.
- D. Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.

## LAB20-Q30 — Applied

The name-resolution verification validation asks whether the authoritative DNS and Bastion rollout can administer a private virtual machine without assigning it a public address. Which observable state is strongest?

- A. Query the exact record-set name and type and compare its TTL and record values.
- B. Query the authoritative name servers directly and compare with the recursive resolver response.
- C. Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
- D. Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.

## LAB20-Q31 — Applied

The name-resolution verification support team isolated the authoritative DNS and Bastion rollout incident to the attempt to publish internet records by using Azure-hosted DNS authority. Which condition prevents success?

- A. The domain registrar still delegates to different authoritative name servers.
- B. Only one of the assigned name servers was added at the registrar.
- C. The recursive resolver cached NXDOMAIN from a query made before the record existed.
- D. The VM NSG blocks the management port from the Bastion subnet.

## LAB20-Q32 — Applied

An authoritative DNS and Bastion rollout query surprises the network administrator providing secure management and authoritative DNS during the name-resolution verification attempt to make the parent domain direct queries to the Azure-hosted child zone. Which finding explains it?

- A. A CNAME was created at a label that also has another conflicting record type.
- B. The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment.
- C. The domain registrar still delegates to different authoritative name servers.
- D. Only one of the assigned name servers was added at the registrar.

## LAB20-Q33 — Applied

Other authoritative DNS and Bastion rollout components are healthy, but the name-resolution verification still cannot publish multiple values with the same owner, type, and time-to-live. Which state causes the isolated failure?

- A. A literal A record was used and became stale after the public IP changed.
- B. The existing AzureBastionSubnet is too small for the requested Bastion deployment.
- C. A CNAME was created at a label that also has another conflicting record type.
- D. Only one of the assigned name servers was added at the registrar.

## LAB20-Q34 — Applied

During a name-resolution verification fault drill, the authoritative DNS and Bastion rollout does not point a zone-apex record at an Azure resource without hard-coding its address. Which finding identifies the defect?

- A. A literal A record was used and became stale after the public IP changed.
- B. Validation used a recursive cache that still holds the previous answer.
- C. The supplied public IP uses an unsupported Basic SKU.
- D. A CNAME was created at a label that also has another conflicting record type.

## LAB20-Q35 — Applied

The authoritative DNS and Bastion rollout setup finishes, yet the name-resolution verification cannot control how long a positive answer can remain in recursive caches. Which misconfiguration explains the mismatch?

- A. Validation used a recursive cache that still holds the previous answer.
- B. The recursive resolver cached NXDOMAIN from a query made before the record existed.
- C. The VM NSG blocks the management port from the Bastion subnet.
- D. A literal A record was used and became stale after the public IP changed.

## LAB20-Q36 — Applied

A name-resolution verification break/fix in the authoritative DNS and Bastion rollout fails when operators try to control cache duration for a negative DNS lookup. Which diagnosis fits?

- A. The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment.
- B. The domain registrar still delegates to different authoritative name servers.
- C. The recursive resolver cached NXDOMAIN from a query made before the record existed.
- D. Validation used a recursive cache that still holds the previous answer.

## LAB20-Q37 — Applied

The authoritative DNS and Bastion rollout troubleshooting scope is the name-resolution verification need to use the exact reserved subnet name required by the managed jump service. Which condition should be corrected first?

- A. The existing AzureBastionSubnet is too small for the requested Bastion deployment.
- B. Only one of the assigned name servers was added at the registrar.
- C. The recursive resolver cached NXDOMAIN from a query made before the record existed.
- D. The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment.

## LAB20-Q38 — Applied

The authoritative DNS and Bastion rollout result is partial because the name-resolution verification cannot allocate a subnet large enough for the managed jump service to scale. Which condition accounts for that result?

- A. The supplied public IP uses an unsupported Basic SKU.
- B. A CNAME was created at a label that also has another conflicting record type.
- C. The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment.
- D. The existing AzureBastionSubnet is too small for the requested Bastion deployment.

## LAB20-Q39 — Applied

The name-resolution verification evidence shows the authoritative DNS and Bastion rollout cannot attach the supported public address configuration to the managed jump host. Which root cause fits that evidence?

- A. The VM NSG blocks the management port from the Bastion subnet.
- B. A literal A record was used and became stale after the public IP changed.
- C. The supplied public IP uses an unsupported Basic SKU.
- D. The existing AzureBastionSubnet is too small for the requested Bastion deployment.

## LAB20-Q40 — Applied

Although the authoritative DNS and Bastion rollout is meant to let the name-resolution verification administer a private virtual machine without assigning it a public address, its checkpoint fails. Which name-resolution verification defect explains the failure?

- A. The domain registrar still delegates to different authoritative name servers.
- B. Validation used a recursive cache that still holds the previous answer.
- C. The supplied public IP uses an unsupported Basic SKU.
- D. The VM NSG blocks the management port from the Bastion subnet.

## LAB20-Q41 — Advanced

Only the authoritative DNS and Bastion rollout change needed to publish internet records by using Azure-hosted DNS authority is allowed, and name-resolution verification proof is mandatory. Which pair fits?

- A. First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
- B. First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values.
- C. First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
- D. First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.

## LAB20-Q42 — Advanced

The authoritative DNS and Bastion rollout runbook separates name-resolution verification mutation from validation while it must make the parent domain direct queries to the Azure-hosted child zone. Which sequence proves it cleanly?

- A. First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
- B. First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.
- C. First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
- D. First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.

## LAB20-Q43 — Advanced

The authoritative DNS and Bastion rollout checkpoint requires both this name-resolution verification outcome—publish multiple values with the same owner, type, and time-to-live—and a read-only authoritative DNS and Bastion rollout state check. Which name-resolution verification response is complete?

- A. First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.
- B. First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
- C. First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values.
- D. First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.

## LAB20-Q44 — Advanced

The authoritative DNS and Bastion rollout runbook must point a zone-apex record at an Azure resource without hard-coding its address, then retain name-resolution verification read-back evidence. Which authoritative DNS and Bastion rollout pair completes both duties?

- A. First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.
- B. First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
- C. First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
- D. First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.

## LAB20-Q45 — Advanced

To satisfy the name-resolution verification requirement, operators must change the authoritative DNS and Bastion rollout configuration and prove it can control how long a positive answer can remain in recursive caches. Which sequence is coherent?

- A. First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
- B. First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.
- C. First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
- D. First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.

## LAB20-Q46 — Advanced

The network administrator providing secure management and authoritative DNS needs a safe authoritative DNS and Bastion rollout change to control cache duration for a negative DNS lookup, followed by name-resolution verification evidence. Which pair merits approval?

- A. First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
- B. First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.
- C. First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.
- D. First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values.

## LAB20-Q47 — Advanced

The authoritative DNS and Bastion rollout has two name-resolution verification gates: use the exact reserved subnet name required by the managed jump service, then prove the authoritative DNS and Bastion rollout state. Which name-resolution verification sequence works?

- A. First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
- B. First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values.
- C. First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
- D. First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.

## LAB20-Q48 — Advanced

Which name-resolution verification path makes the authoritative DNS and Bastion rollout able to allocate a subnet large enough for the managed jump service to scale, then inspects the defining properties?

- A. First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
- B. First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
- C. First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
- D. First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.

## LAB20-Q49 — Advanced

At the authoritative DNS and Bastion rollout approval gate, operators must show that the name-resolution verification can attach the supported public address configuration to the managed jump host. Which name-resolution verification configure-and-check pair is defensible?

- A. First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
- B. First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
- C. First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.
- D. First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.

## LAB20-Q50 — Advanced

The authoritative DNS and Bastion rollout forbids a partial name-resolution verification result. Operators must first administer a private virtual machine without assigning it a public address and afterward confirm the authoritative DNS and Bastion rollout outcome. Which name-resolution verification sequence is complete?

- A. First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.
- B. First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.
- C. First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
- D. First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.

[Open the answer key](./ANSWERS.md)
