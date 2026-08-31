# Lab 20 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB20-Q01 — D

**Question:** A name-resolution verification reviewer challenges whether the authoritative DNS and Bastion rollout can publish internet records by using Azure-hosted DNS authority. Which response resolves the concern?

- **A — Incorrect.** Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers.
  Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers. In the authoritative DNS and Bastion rollout, this statement describes DNS delegation. Authoritative DNS and Bastion rollout asks about public DNS zones; this DNS delegation choice leaves the public DNS zones explanation missing.
- **B — Incorrect.** Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.
  Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes. In the authoritative DNS and Bastion rollout, this statement describes DNS TTL behavior. The DNS TTL behavior statement accurately describes DNS TTL behavior; however, authoritative DNS and Bastion rollout needs public DNS zones to publish internet records by using Azure-hosted DNS authority; DNS TTL behavior cannot replace public DNS zones.
- **C — Incorrect.** Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features.
  Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features. In the authoritative DNS and Bastion rollout, this statement describes Bastion subnet sizing. Selecting Bastion subnet sizing for authoritative DNS and Bastion rollout leaves public DNS zones unanswered in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout lacks a public DNS zones basis to publish internet records by using Azure-hosted DNS authority.
- **D — Correct.** An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name.
  An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name. For authoritative DNS and Bastion rollout, public DNS zones supplies the service rule needed to publish internet records by using Azure-hosted DNS authority.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Host a DNS zone in Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q02 — B

**Question:** The authoritative DNS and Bastion rollout handoff omits the name-resolution verification rule needed to make the parent domain direct queries to the Azure-hosted child zone. Which statement should the team add?

- **A — Incorrect.** A DNS record set groups records of one type and name and applies a shared TTL at that label.
  A DNS record set groups records of one type and name and applies a shared TTL at that label. In the authoritative DNS and Bastion rollout, this statement describes DNS record sets. The DNS record sets statement accurately describes DNS record sets; however, authoritative DNS and Bastion rollout needs DNS delegation to make the parent domain direct queries to the Azure-hosted child zone; DNS record sets cannot replace DNS delegation.
- **B — Correct.** Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers.
  Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers. In the authoritative DNS and Bastion rollout, this DNS delegation rule supports the need to make the parent domain direct queries to the Azure-hosted child zone.
- **C — Incorrect.** Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior.
  Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior. In the authoritative DNS and Bastion rollout, this statement describes DNS negative caching. DNS delegation governs authoritative DNS and Bastion rollout; DNS negative caching cannot support DNS delegation when operators must make the parent domain direct queries to the Azure-hosted child zone.
- **D — Incorrect.** Azure Bastion uses a supported Standard, static public IP configuration for its managed host.
  Azure Bastion uses a supported Standard, static public IP configuration for its managed host. In the authoritative DNS and Bastion rollout, this statement describes Bastion public IP. Authoritative DNS and Bastion rollout asks about DNS delegation; this Bastion public IP choice leaves the DNS delegation explanation missing.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Delegate a domain to Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation)

**Source reviewed:** 2026-08-31

## LAB20-Q03 — A

**Question:** A name-resolution verification incident review of the authoritative DNS and Bastion rollout depends on the ability to publish multiple values with the same owner, type, and time-to-live. Which platform description is reliable?

- **A — Correct.** A DNS record set groups records of one type and name and applies a shared TTL at that label.
  For the authoritative DNS and Bastion rollout, the rule for DNS record sets is defined by this statement: a DNS record set groups records of one type and name and applies a shared TTL at that label. It supports the required outcome to publish multiple values with the same owner, type, and time-to-live.
- **B — Incorrect.** An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle.
  An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle. In the authoritative DNS and Bastion rollout, this statement describes Azure DNS alias records. DNS record sets governs authoritative DNS and Bastion rollout; Azure DNS alias records cannot support DNS record sets when operators must publish multiple values with the same owner, type, and time-to-live.
- **C — Incorrect.** Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet.
  Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet. In the authoritative DNS and Bastion rollout, this statement describes AzureBastionSubnet naming. Authoritative DNS and Bastion rollout asks about DNS record sets; this AzureBastionSubnet naming choice leaves the DNS record sets explanation missing.
- **D — Incorrect.** Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH.
  Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH. In the authoritative DNS and Bastion rollout, this statement describes private VM administration. The private VM administration statement accurately describes private VM administration; however, authoritative DNS and Bastion rollout needs DNS record sets to publish multiple values with the same owner, type, and time-to-live; private VM administration cannot replace DNS record sets.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q04 — B

**Question:** A network administrator providing secure management and authoritative DNS is updating the name-resolution verification runbook. The requirement is to point a zone-apex record at an Azure resource without hard-coding its address. Which statement describes Azure behavior correctly?

- **A — Incorrect.** Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.
  Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes. In the authoritative DNS and Bastion rollout, this statement describes DNS TTL behavior. Azure DNS alias records governs authoritative DNS and Bastion rollout; DNS TTL behavior cannot support Azure DNS alias records when operators must point a zone-apex record at an Azure resource without hard-coding its address.
- **B — Correct.** An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle.
  An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle. The authoritative DNS and Bastion rollout applies that Azure DNS alias records boundary when operators must point a zone-apex record at an Azure resource without hard-coding its address.
- **C — Incorrect.** Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features.
  Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features. In the authoritative DNS and Bastion rollout, this statement describes Bastion subnet sizing. The Bastion subnet sizing statement accurately describes Bastion subnet sizing; however, authoritative DNS and Bastion rollout needs Azure DNS alias records to point a zone-apex record at an Azure resource without hard-coding its address; Bastion subnet sizing cannot replace Azure DNS alias records.
- **D — Incorrect.** An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name.
  An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name. In the authoritative DNS and Bastion rollout, this statement describes public DNS zones. Selecting public DNS zones for authoritative DNS and Bastion rollout leaves Azure DNS alias records unanswered in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout lacks a Azure DNS alias records basis to point a zone-apex record at an Azure resource without hard-coding its address.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q05 — C

**Question:** A name-resolution verification peer review asks how the authoritative DNS and Bastion rollout should handle this outcome: control how long a positive answer can remain in recursive caches. Which explanation is accurate?

- **A — Incorrect.** Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior.
  Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior. In the authoritative DNS and Bastion rollout, this statement describes DNS negative caching. Authoritative DNS and Bastion rollout asks about DNS TTL behavior; this DNS negative caching choice leaves the DNS TTL behavior explanation missing.
- **B — Incorrect.** Azure Bastion uses a supported Standard, static public IP configuration for its managed host.
  Azure Bastion uses a supported Standard, static public IP configuration for its managed host. In the authoritative DNS and Bastion rollout, this statement describes Bastion public IP. The Bastion public IP statement accurately describes Bastion public IP; however, authoritative DNS and Bastion rollout needs DNS TTL behavior to control how long a positive answer can remain in recursive caches; Bastion public IP cannot replace DNS TTL behavior.
- **C — Correct.** Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.
  The authoritative DNS and Bastion rollout needs DNS TTL behavior to control how long a positive answer can remain in recursive caches; this option states the applicable DNS TTL behavior rule: resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.
- **D — Incorrect.** Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers.
  Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers. In the authoritative DNS and Bastion rollout, this statement describes DNS delegation. DNS TTL behavior governs authoritative DNS and Bastion rollout; DNS delegation cannot support DNS TTL behavior when operators must control how long a positive answer can remain in recursive caches.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q06 — C

**Question:** For the authoritative DNS and Bastion rollout, the name-resolution verification plan must control cache duration for a negative DNS lookup. Which statement about name-resolution verification belongs in the authoritative DNS and Bastion rollout record?

- **A — Incorrect.** Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet.
  Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet. In the authoritative DNS and Bastion rollout, this statement describes AzureBastionSubnet naming. The AzureBastionSubnet naming statement accurately describes AzureBastionSubnet naming; however, authoritative DNS and Bastion rollout needs DNS negative caching to control cache duration for a negative DNS lookup; AzureBastionSubnet naming cannot replace DNS negative caching.
- **B — Incorrect.** Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH.
  Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH. In the authoritative DNS and Bastion rollout, this statement describes private VM administration. Selecting private VM administration for authoritative DNS and Bastion rollout leaves DNS negative caching unanswered in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout lacks a DNS negative caching basis to control cache duration for a negative DNS lookup.
- **C — Correct.** Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior.
  Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior. This DNS negative caching fact resolves the authoritative DNS and Bastion rollout design question about how to control cache duration for a negative DNS lookup.
- **D — Incorrect.** A DNS record set groups records of one type and name and applies a shared TTL at that label.
  A DNS record set groups records of one type and name and applies a shared TTL at that label. In the authoritative DNS and Bastion rollout, this statement describes DNS record sets. Authoritative DNS and Bastion rollout asks about DNS negative caching; this DNS record sets choice leaves the DNS negative caching explanation missing.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q07 — B

**Question:** The name-resolution verification review compares four claims for the authoritative DNS and Bastion rollout requirement to use the exact reserved subnet name required by the managed jump service. Which claim is technically sound?

- **A — Incorrect.** Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features.
  Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features. In the authoritative DNS and Bastion rollout, this statement describes Bastion subnet sizing. Selecting Bastion subnet sizing for authoritative DNS and Bastion rollout leaves AzureBastionSubnet naming unanswered in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout lacks a AzureBastionSubnet naming basis to use the exact reserved subnet name required by the managed jump service.
- **B — Correct.** Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet.
  Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet. For authoritative DNS and Bastion rollout, AzureBastionSubnet naming supplies the service rule needed to use the exact reserved subnet name required by the managed jump service.
- **C — Incorrect.** An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name.
  An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name. In the authoritative DNS and Bastion rollout, this statement describes public DNS zones. Authoritative DNS and Bastion rollout asks about AzureBastionSubnet naming; this public DNS zones choice leaves the AzureBastionSubnet naming explanation missing.
- **D — Incorrect.** An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle.
  An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle. In the authoritative DNS and Bastion rollout, this statement describes Azure DNS alias records. The Azure DNS alias records statement accurately describes Azure DNS alias records; however, authoritative DNS and Bastion rollout needs AzureBastionSubnet naming to use the exact reserved subnet name required by the managed jump service; Azure DNS alias records cannot replace AzureBastionSubnet naming.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q08 — A

**Question:** The name-resolution verification architecture note requires the authoritative DNS and Bastion rollout environment to allocate a subnet large enough for the managed jump service to scale. Which statement defines the relevant name-resolution verification boundary?

- **A — Correct.** Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features.
  Current Azure Bastion deployments require a sufficiently large dedicated subnet, commonly /26 or larger for supported scaling and features. In the authoritative DNS and Bastion rollout, this Bastion subnet sizing rule supports the need to allocate a subnet large enough for the managed jump service to scale.
- **B — Incorrect.** Azure Bastion uses a supported Standard, static public IP configuration for its managed host.
  Azure Bastion uses a supported Standard, static public IP configuration for its managed host. In the authoritative DNS and Bastion rollout, this statement describes Bastion public IP. Authoritative DNS and Bastion rollout asks about Bastion subnet sizing; this Bastion public IP choice leaves the Bastion subnet sizing explanation missing.
- **C — Incorrect.** Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers.
  Delegation requires the parent zone or registrar to publish NS records naming the child zone's Azure DNS name servers. In the authoritative DNS and Bastion rollout, this statement describes DNS delegation. The DNS delegation statement accurately describes DNS delegation; however, authoritative DNS and Bastion rollout needs Bastion subnet sizing to allocate a subnet large enough for the managed jump service to scale; DNS delegation cannot replace Bastion subnet sizing.
- **D — Incorrect.** Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes.
  Resolver caches can retain an earlier DNS answer until its TTL expires even after the authoritative record changes. In the authoritative DNS and Bastion rollout, this statement describes DNS TTL behavior. Selecting DNS TTL behavior for authoritative DNS and Bastion rollout leaves Bastion subnet sizing unanswered in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout lacks a Bastion subnet sizing basis to allocate a subnet large enough for the managed jump service to scale.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q09 — B

**Question:** A new name-resolution verification operator must explain why the authoritative DNS and Bastion rollout can attach the supported public address configuration to the managed jump host. Which explanation is accurate?

- **A — Incorrect.** Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH.
  Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH. In the authoritative DNS and Bastion rollout, this statement describes private VM administration. Authoritative DNS and Bastion rollout asks about Bastion public IP; this private VM administration choice leaves the Bastion public IP explanation missing.
- **B — Correct.** Azure Bastion uses a supported Standard, static public IP configuration for its managed host.
  For the authoritative DNS and Bastion rollout, the rule for Bastion public IP is defined by this statement: Azure Bastion uses a supported Standard, static public IP configuration for its managed host. It supports the required outcome to attach the supported public address configuration to the managed jump host.
- **C — Incorrect.** A DNS record set groups records of one type and name and applies a shared TTL at that label.
  A DNS record set groups records of one type and name and applies a shared TTL at that label. In the authoritative DNS and Bastion rollout, this statement describes DNS record sets. Selecting DNS record sets for authoritative DNS and Bastion rollout leaves Bastion public IP unanswered in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout lacks a Bastion public IP basis to attach the supported public address configuration to the managed jump host.
- **D — Incorrect.** Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior.
  Resolvers can cache a nonexistent-name response according to the zone's SOA negative caching behavior. In the authoritative DNS and Bastion rollout, this statement describes DNS negative caching. Bastion public IP governs authoritative DNS and Bastion rollout; DNS negative caching cannot support Bastion public IP when operators must attach the supported public address configuration to the managed jump host.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q10 — B

**Question:** The authoritative DNS and Bastion rollout acceptance criteria require operators to administer a private virtual machine without assigning it a public address. Which service fact supports that requirement?

- **A — Incorrect.** An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name.
  An Azure public DNS zone hosts authoritative records but does not register or purchase the domain name. In the authoritative DNS and Bastion rollout, this statement describes public DNS zones. The public DNS zones statement accurately describes public DNS zones; however, authoritative DNS and Bastion rollout needs private VM administration to administer a private virtual machine without assigning it a public address; public DNS zones cannot replace private VM administration.
- **B — Correct.** Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH.
  Azure Bastion connects to VM private addresses so managed VMs do not require individual public IP addresses for RDP or SSH. The authoritative DNS and Bastion rollout applies that private VM administration boundary when operators must administer a private virtual machine without assigning it a public address.
- **C — Incorrect.** An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle.
  An Azure DNS alias record can reference a supported Azure resource so the DNS value tracks that resource lifecycle. In the authoritative DNS and Bastion rollout, this statement describes Azure DNS alias records. Private VM administration governs authoritative DNS and Bastion rollout; Azure DNS alias records cannot support private VM administration when operators must administer a private virtual machine without assigning it a public address.
- **D — Incorrect.** Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet.
  Azure Bastion must use a dedicated subnet named exactly AzureBastionSubnet. In the authoritative DNS and Bastion rollout, this statement describes AzureBastionSubnet naming. Authoritative DNS and Bastion rollout asks about private VM administration; this AzureBastionSubnet naming choice leaves the private VM administration explanation missing.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q11 — C

**Question:** The authoritative DNS and Bastion rollout window permits only the name-resolution verification change needed to publish internet records by using Azure-hosted DNS authority. Which option respects the boundary?

- **A — Incorrect.** Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL.
  Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. In the authoritative DNS and Bastion rollout, this action changes DNS record sets. Authoritative DNS and Bastion rollout approved public DNS zones, not DNS record sets; only the public DNS zones change can publish internet records by using Azure-hosted DNS authority.
- **B — Incorrect.** Create required records before the validation window and account for prior negative responses.
  Create required records before the validation window and account for prior negative responses. In the authoritative DNS and Bastion rollout, this action changes DNS negative caching. Authoritative DNS and Bastion rollout requires public DNS zones; changing DNS negative caching leaves public DNS zones absent in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout cannot publish internet records by using Azure-hosted DNS authority.
- **C — Correct.** Create the zone for a domain the organization controls and retain its assigned name servers.
  The authoritative DNS and Bastion rollout must publish internet records by using Azure-hosted DNS authority; this option performs its direct public DNS zones change: create the zone for a domain the organization controls and retain its assigned name servers.
- **D — Incorrect.** Create a Standard static public IP and attach it to the Bastion IP configuration.
  Create a Standard static public IP and attach it to the Bastion IP configuration. In the authoritative DNS and Bastion rollout, this action changes Bastion public IP. Authoritative DNS and Bastion rollout instead needs public DNS zones: Create the zone for a domain the organization controls and retain its assigned name servers. The Bastion public IP action omits that public DNS zones work.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Host a DNS zone in Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q12 — A

**Question:** The name-resolution verification preflight has passed; the authoritative DNS and Bastion rollout must now make the parent domain direct queries to the Azure-hosted child zone. Which operation should run?

- **A — Correct.** Copy every assigned Azure DNS name server into the parent delegation.
  Copy every assigned Azure DNS name server into the parent delegation. It is the least-change DNS delegation path for the authoritative DNS and Bastion rollout requirement to make the parent domain direct queries to the Azure-hosted child zone.
- **B — Incorrect.** Use an alias A record when a supported Azure public IP or endpoint should be the record target.
  Use an alias A record when a supported Azure public IP or endpoint should be the record target. In the authoritative DNS and Bastion rollout, this action changes Azure DNS alias records. Azure DNS alias records does not implement DNS delegation for authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout still cannot make the parent domain direct queries to the Azure-hosted child zone.
- **C — Incorrect.** Create the dedicated subnet with the exact reserved name before deploying the host.
  Create the dedicated subnet with the exact reserved name before deploying the host. In the authoritative DNS and Bastion rollout, this action changes AzureBastionSubnet naming. Authoritative DNS and Bastion rollout instead needs DNS delegation: Copy every assigned Azure DNS name server into the parent delegation. The AzureBastionSubnet naming action omits that DNS delegation work.
- **D — Incorrect.** Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow.
  Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. In the authoritative DNS and Bastion rollout, this action changes private VM administration. Authoritative DNS and Bastion rollout approved DNS delegation, not private VM administration; only the DNS delegation change can make the parent domain direct queries to the Azure-hosted child zone.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Delegate a domain to Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation)

**Source reviewed:** 2026-08-31

## LAB20-Q13 — A

**Question:** The authoritative DNS and Bastion rollout plan must publish multiple values with the same owner, type, and time-to-live while limiting the mutation scope to name-resolution verification. Which action is appropriate?

- **A — Correct.** Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL.
  Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. In authoritative DNS and Bastion rollout, applying DNS record sets is the scoped way to publish multiple values with the same owner, type, and time-to-live.
- **B — Incorrect.** Lower TTL before a planned cutover, wait for prior caches, then update the record.
  Lower TTL before a planned cutover, wait for prior caches, then update the record. In the authoritative DNS and Bastion rollout, this action changes DNS TTL behavior. Authoritative DNS and Bastion rollout instead needs DNS record sets: Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. The DNS TTL behavior action omits that DNS record sets work.
- **C — Incorrect.** Allocate an approved /26-or-larger AzureBastionSubnet without other workloads.
  Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. In the authoritative DNS and Bastion rollout, this action changes Bastion subnet sizing. Authoritative DNS and Bastion rollout approved DNS record sets, not Bastion subnet sizing; only the DNS record sets change can publish multiple values with the same owner, type, and time-to-live.
- **D — Incorrect.** Create the zone for a domain the organization controls and retain its assigned name servers.
  Create the zone for a domain the organization controls and retain its assigned name servers. In the authoritative DNS and Bastion rollout, this action changes public DNS zones. Authoritative DNS and Bastion rollout requires DNS record sets; changing public DNS zones leaves DNS record sets absent in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout cannot publish multiple values with the same owner, type, and time-to-live.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q14 — A

**Question:** A name-resolution verification ticket in the authoritative DNS and Bastion rollout says to point a zone-apex record at an Azure resource without hard-coding its address. Which name-resolution verification action completes the authoritative DNS and Bastion rollout request with minimal change?

- **A — Correct.** Use an alias A record when a supported Azure public IP or endpoint should be the record target.
  Use an alias A record when a supported Azure public IP or endpoint should be the record target. The authoritative DNS and Bastion rollout uses this Azure DNS alias records operation to point a zone-apex record at an Azure resource without hard-coding its address within the approved scope.
- **B — Incorrect.** Create required records before the validation window and account for prior negative responses.
  Create required records before the validation window and account for prior negative responses. In the authoritative DNS and Bastion rollout, this action changes DNS negative caching. Authoritative DNS and Bastion rollout approved Azure DNS alias records, not DNS negative caching; only the Azure DNS alias records change can point a zone-apex record at an Azure resource without hard-coding its address.
- **C — Incorrect.** Create a Standard static public IP and attach it to the Bastion IP configuration.
  Create a Standard static public IP and attach it to the Bastion IP configuration. In the authoritative DNS and Bastion rollout, this action changes Bastion public IP. Authoritative DNS and Bastion rollout requires Azure DNS alias records; changing Bastion public IP leaves Azure DNS alias records absent in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout cannot point a zone-apex record at an Azure resource without hard-coding its address.
- **D — Incorrect.** Copy every assigned Azure DNS name server into the parent delegation.
  Copy every assigned Azure DNS name server into the parent delegation. In the authoritative DNS and Bastion rollout, this action changes DNS delegation. DNS delegation does not implement Azure DNS alias records for authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout still cannot point a zone-apex record at an Azure resource without hard-coding its address.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q15 — C

**Question:** The approach for the authoritative DNS and Bastion rollout is approved, but the name-resolution verification environment still cannot control how long a positive answer can remain in recursive caches. Which implementation step closes the gap?

- **A — Incorrect.** Create the dedicated subnet with the exact reserved name before deploying the host.
  Create the dedicated subnet with the exact reserved name before deploying the host. In the authoritative DNS and Bastion rollout, this action changes AzureBastionSubnet naming. Authoritative DNS and Bastion rollout approved DNS TTL behavior, not AzureBastionSubnet naming; only the DNS TTL behavior change can control how long a positive answer can remain in recursive caches.
- **B — Incorrect.** Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow.
  Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. In the authoritative DNS and Bastion rollout, this action changes private VM administration. Authoritative DNS and Bastion rollout requires DNS TTL behavior; changing private VM administration leaves DNS TTL behavior absent in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout cannot control how long a positive answer can remain in recursive caches.
- **C — Correct.** Lower TTL before a planned cutover, wait for prior caches, then update the record.
  For the authoritative DNS and Bastion rollout, the required DNS TTL behavior action is: lower TTL before a planned cutover, wait for prior caches, then update the record. It makes the environment able to control how long a positive answer can remain in recursive caches.
- **D — Incorrect.** Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL.
  Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. In the authoritative DNS and Bastion rollout, this action changes DNS record sets. Authoritative DNS and Bastion rollout instead needs DNS TTL behavior: Lower TTL before a planned cutover, wait for prior caches, then update the record. The DNS record sets action omits that DNS TTL behavior work.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q16 — B

**Question:** The network administrator providing secure management and authoritative DNS may change the authoritative DNS and Bastion rollout only to control cache duration for a negative DNS lookup. Which name-resolution verification action stays within that assignment?

- **A — Incorrect.** Allocate an approved /26-or-larger AzureBastionSubnet without other workloads.
  Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. In the authoritative DNS and Bastion rollout, this action changes Bastion subnet sizing. Authoritative DNS and Bastion rollout requires DNS negative caching; changing Bastion subnet sizing leaves DNS negative caching absent in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout cannot control cache duration for a negative DNS lookup.
- **B — Correct.** Create required records before the validation window and account for prior negative responses.
  Create required records before the validation window and account for prior negative responses. This changes DNS negative caching in the authoritative DNS and Bastion rollout, supplying the missing state needed to control cache duration for a negative DNS lookup.
- **C — Incorrect.** Create the zone for a domain the organization controls and retain its assigned name servers.
  Create the zone for a domain the organization controls and retain its assigned name servers. In the authoritative DNS and Bastion rollout, this action changes public DNS zones. Authoritative DNS and Bastion rollout instead needs DNS negative caching: Create required records before the validation window and account for prior negative responses. The public DNS zones action omits that DNS negative caching work.
- **D — Incorrect.** Use an alias A record when a supported Azure public IP or endpoint should be the record target.
  Use an alias A record when a supported Azure public IP or endpoint should be the record target. In the authoritative DNS and Bastion rollout, this action changes Azure DNS alias records. Authoritative DNS and Bastion rollout approved DNS negative caching, not Azure DNS alias records; only the DNS negative caching change can control cache duration for a negative DNS lookup.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q17 — D

**Question:** A name-resolution verification dry run shows no authoritative DNS and Bastion rollout command will use the exact reserved subnet name required by the managed jump service. Which action belongs before execution?

- **A — Incorrect.** Create a Standard static public IP and attach it to the Bastion IP configuration.
  Create a Standard static public IP and attach it to the Bastion IP configuration. In the authoritative DNS and Bastion rollout, this action changes Bastion public IP. Bastion public IP does not implement AzureBastionSubnet naming for authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout still cannot use the exact reserved subnet name required by the managed jump service.
- **B — Incorrect.** Copy every assigned Azure DNS name server into the parent delegation.
  Copy every assigned Azure DNS name server into the parent delegation. In the authoritative DNS and Bastion rollout, this action changes DNS delegation. Authoritative DNS and Bastion rollout instead needs AzureBastionSubnet naming: Create the dedicated subnet with the exact reserved name before deploying the host. The DNS delegation action omits that AzureBastionSubnet naming work.
- **C — Incorrect.** Lower TTL before a planned cutover, wait for prior caches, then update the record.
  Lower TTL before a planned cutover, wait for prior caches, then update the record. In the authoritative DNS and Bastion rollout, this action changes DNS TTL behavior. Authoritative DNS and Bastion rollout approved AzureBastionSubnet naming, not DNS TTL behavior; only the AzureBastionSubnet naming change can use the exact reserved subnet name required by the managed jump service.
- **D — Correct.** Create the dedicated subnet with the exact reserved name before deploying the host.
  The authoritative DNS and Bastion rollout must use the exact reserved subnet name required by the managed jump service; this option performs its direct AzureBastionSubnet naming change: create the dedicated subnet with the exact reserved name before deploying the host.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q18 — D

**Question:** For the authoritative DNS and Bastion rollout, operators need to allocate a subnet large enough for the managed jump service to scale. Which change realizes that requirement?

- **A — Incorrect.** Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow.
  Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. In the authoritative DNS and Bastion rollout, this action changes private VM administration. Authoritative DNS and Bastion rollout instead needs Bastion subnet sizing: Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. The private VM administration action omits that Bastion subnet sizing work.
- **B — Incorrect.** Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL.
  Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. In the authoritative DNS and Bastion rollout, this action changes DNS record sets. Authoritative DNS and Bastion rollout approved Bastion subnet sizing, not DNS record sets; only the Bastion subnet sizing change can allocate a subnet large enough for the managed jump service to scale.
- **C — Incorrect.** Create required records before the validation window and account for prior negative responses.
  Create required records before the validation window and account for prior negative responses. In the authoritative DNS and Bastion rollout, this action changes DNS negative caching. Authoritative DNS and Bastion rollout requires Bastion subnet sizing; changing DNS negative caching leaves Bastion subnet sizing absent in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout cannot allocate a subnet large enough for the managed jump service to scale.
- **D — Correct.** Allocate an approved /26-or-larger AzureBastionSubnet without other workloads.
  Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. It is the least-change Bastion subnet sizing path for the authoritative DNS and Bastion rollout requirement to allocate a subnet large enough for the managed jump service to scale.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q19 — A

**Question:** Operators must automate the authoritative DNS and Bastion rollout change needed to attach the supported public address configuration to the managed jump host. Which name-resolution verification operation belongs in the runbook?

- **A — Correct.** Create a Standard static public IP and attach it to the Bastion IP configuration.
  Create a Standard static public IP and attach it to the Bastion IP configuration. In authoritative DNS and Bastion rollout, applying Bastion public IP is the scoped way to attach the supported public address configuration to the managed jump host.
- **B — Incorrect.** Create the zone for a domain the organization controls and retain its assigned name servers.
  Create the zone for a domain the organization controls and retain its assigned name servers. In the authoritative DNS and Bastion rollout, this action changes public DNS zones. Authoritative DNS and Bastion rollout requires Bastion public IP; changing public DNS zones leaves Bastion public IP absent in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout cannot attach the supported public address configuration to the managed jump host.
- **C — Incorrect.** Use an alias A record when a supported Azure public IP or endpoint should be the record target.
  Use an alias A record when a supported Azure public IP or endpoint should be the record target. In the authoritative DNS and Bastion rollout, this action changes Azure DNS alias records. Azure DNS alias records does not implement Bastion public IP for authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout still cannot attach the supported public address configuration to the managed jump host.
- **D — Incorrect.** Create the dedicated subnet with the exact reserved name before deploying the host.
  Create the dedicated subnet with the exact reserved name before deploying the host. In the authoritative DNS and Bastion rollout, this action changes AzureBastionSubnet naming. Authoritative DNS and Bastion rollout instead needs Bastion public IP: Create a Standard static public IP and attach it to the Bastion IP configuration. The AzureBastionSubnet naming action omits that Bastion public IP work.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q20 — A

**Question:** An authoritative DNS and Bastion rollout review finds name-resolution verification drift from the need to administer a private virtual machine without assigning it a public address. Which correction addresses that drift?

- **A — Correct.** Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow.
  Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. The authoritative DNS and Bastion rollout uses this private VM administration operation to administer a private virtual machine without assigning it a public address within the approved scope.
- **B — Incorrect.** Copy every assigned Azure DNS name server into the parent delegation.
  Copy every assigned Azure DNS name server into the parent delegation. In the authoritative DNS and Bastion rollout, this action changes DNS delegation. DNS delegation does not implement private VM administration for authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout still cannot administer a private virtual machine without assigning it a public address.
- **C — Incorrect.** Lower TTL before a planned cutover, wait for prior caches, then update the record.
  Lower TTL before a planned cutover, wait for prior caches, then update the record. In the authoritative DNS and Bastion rollout, this action changes DNS TTL behavior. Authoritative DNS and Bastion rollout instead needs private VM administration: Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. The DNS TTL behavior action omits that private VM administration work.
- **D — Incorrect.** Allocate an approved /26-or-larger AzureBastionSubnet without other workloads.
  Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. In the authoritative DNS and Bastion rollout, this action changes Bastion subnet sizing. Authoritative DNS and Bastion rollout approved private VM administration, not Bastion subnet sizing; only the private VM administration change can administer a private virtual machine without assigning it a public address.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q21 — B

**Question:** An authoritative DNS and Bastion rollout review must prove the name-resolution verification ability to publish internet records by using Azure-hosted DNS authority. Which check avoids an adjacent feature?

- **A — Incorrect.** Query targetResource.id and resolve the record to the current target address.
  Query targetResource.id and resolve the record to the current target address. In the authoritative DNS and Bastion rollout, this check observes Azure DNS alias records. Authoritative DNS and Bastion rollout output covers Azure DNS alias records, not public DNS zones; the public DNS zones requirement to publish internet records by using Azure-hosted DNS authority remains unverified.
- **B — Correct.** Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
  For the authoritative DNS and Bastion rollout, this public DNS zones observation is decisive: query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers. It is authoritative DNS and Bastion rollout evidence that operators can publish internet records by using Azure-hosted DNS authority.
- **C — Incorrect.** Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
  Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet. In the authoritative DNS and Bastion rollout, this check observes AzureBastionSubnet naming. Authoritative DNS and Bastion rollout reads AzureBastionSubnet naming, leaving public DNS zones unproved in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout still has no public DNS zones proof.
- **D — Incorrect.** Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
  Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address. In the authoritative DNS and Bastion rollout, this check observes private VM administration. Authoritative DNS and Bastion rollout could pass private VM administration while public DNS zones is wrong; authoritative DNS and Bastion rollout still lacks public DNS zones proof.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Host a DNS zone in Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q22 — D

**Question:** The authoritative DNS and Bastion rollout evidence bundle needs a name-resolution verification result showing it can make the parent domain direct queries to the Azure-hosted child zone. Which result belongs in the checkpoint?

- **A — Incorrect.** Query authoritative and recursive answers with TTL values during the cutover.
  Query authoritative and recursive answers with TTL values during the cutover. In the authoritative DNS and Bastion rollout, this check observes DNS TTL behavior. DNS TTL behavior success in authoritative DNS and Bastion rollout cannot verify DNS delegation; authoritative DNS and Bastion rollout cannot make the parent domain direct queries to the Azure-hosted child zone until DNS delegation evidence exists.
- **B — Incorrect.** Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
  Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached. In the authoritative DNS and Bastion rollout, this check observes Bastion subnet sizing. Authoritative DNS and Bastion rollout reads Bastion subnet sizing, leaving DNS delegation unproved in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout still has no DNS delegation proof.
- **C — Incorrect.** Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
  Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers. In the authoritative DNS and Bastion rollout, this check observes public DNS zones. Authoritative DNS and Bastion rollout could pass public DNS zones while DNS delegation is wrong; authoritative DNS and Bastion rollout still lacks DNS delegation proof.
- **D — Correct.** Query NS records from an external resolver and compare them with the zone's assigned servers.
  Query NS records from an external resolver and compare them with the zone's assigned servers. Because the authoritative DNS and Bastion rollout check observes DNS delegation, it independently verifies the requirement to make the parent domain direct queries to the Azure-hosted child zone.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Delegate a domain to Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation)

**Source reviewed:** 2026-08-31

## LAB20-Q23 — B

**Question:** Before authoritative DNS and Bastion rollout cleanup, the name-resolution verification team must reconfirm it can publish multiple values with the same owner, type, and time-to-live. Which read-only inspection should run?

- **A — Incorrect.** Query the authoritative name servers directly and compare with the recursive resolver response.
  Query the authoritative name servers directly and compare with the recursive resolver response. In the authoritative DNS and Bastion rollout, this check observes DNS negative caching. Authoritative DNS and Bastion rollout reads DNS negative caching, leaving DNS record sets unproved in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout still has no DNS record sets proof.
- **B — Correct.** Query the exact record-set name and type and compare its TTL and record values.
  The authoritative DNS and Bastion rollout validator needs this DNS record sets result: query the exact record-set name and type and compare its TTL and record values. It proves the outcome to publish multiple values with the same owner, type, and time-to-live rather than an adjacent checkpoint.
- **C — Incorrect.** Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
  Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state. In the authoritative DNS and Bastion rollout, this check observes Bastion public IP. Authoritative DNS and Bastion rollout output covers Bastion public IP, not DNS record sets; the DNS record sets requirement to publish multiple values with the same owner, type, and time-to-live remains unverified.
- **D — Incorrect.** Query NS records from an external resolver and compare them with the zone's assigned servers.
  Query NS records from an external resolver and compare them with the zone's assigned servers. In the authoritative DNS and Bastion rollout, this check observes DNS delegation. DNS delegation success in authoritative DNS and Bastion rollout cannot verify DNS record sets; authoritative DNS and Bastion rollout cannot publish multiple values with the same owner, type, and time-to-live until DNS record sets evidence exists.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q24 — B

**Question:** The authoritative DNS and Bastion rollout setup reports success after the name-resolution verification attempt to point a zone-apex record at an Azure resource without hard-coding its address. Which name-resolution verification read-only observation proves the authoritative DNS and Bastion rollout outcome?

- **A — Incorrect.** Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
  Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet. In the authoritative DNS and Bastion rollout, this check observes AzureBastionSubnet naming. Authoritative DNS and Bastion rollout could pass AzureBastionSubnet naming while Azure DNS alias records is wrong; authoritative DNS and Bastion rollout still lacks Azure DNS alias records proof.
- **B — Correct.** Query targetResource.id and resolve the record to the current target address.
  Query targetResource.id and resolve the record to the current target address. This is independent Azure DNS alias records evidence for the authoritative DNS and Bastion rollout, even if authoritative DNS and Bastion rollout setup reports success before Azure DNS alias records becomes observable.
- **C — Incorrect.** Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
  Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address. In the authoritative DNS and Bastion rollout, this check observes private VM administration. Private VM administration success in authoritative DNS and Bastion rollout cannot verify Azure DNS alias records; authoritative DNS and Bastion rollout cannot point a zone-apex record at an Azure resource without hard-coding its address until Azure DNS alias records evidence exists.
- **D — Incorrect.** Query the exact record-set name and type and compare its TTL and record values.
  Query the exact record-set name and type and compare its TTL and record values. In the authoritative DNS and Bastion rollout, this check observes DNS record sets. Authoritative DNS and Bastion rollout reads DNS record sets, leaving Azure DNS alias records unproved in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout still has no Azure DNS alias records proof.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q25 — D

**Question:** The name-resolution verification log says the authoritative DNS and Bastion rollout can now control how long a positive answer can remain in recursive caches. Which name-resolution verification state should the authoritative DNS and Bastion rollout acceptance test retain?

- **A — Incorrect.** Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
  Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached. In the authoritative DNS and Bastion rollout, this check observes Bastion subnet sizing. Authoritative DNS and Bastion rollout output covers Bastion subnet sizing, not DNS TTL behavior; the DNS TTL behavior requirement to control how long a positive answer can remain in recursive caches remains unverified.
- **B — Incorrect.** Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
  Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers. In the authoritative DNS and Bastion rollout, this check observes public DNS zones. Public DNS zones success in authoritative DNS and Bastion rollout cannot verify DNS TTL behavior; authoritative DNS and Bastion rollout cannot control how long a positive answer can remain in recursive caches until DNS TTL behavior evidence exists.
- **C — Incorrect.** Query targetResource.id and resolve the record to the current target address.
  Query targetResource.id and resolve the record to the current target address. In the authoritative DNS and Bastion rollout, this check observes Azure DNS alias records. Authoritative DNS and Bastion rollout reads Azure DNS alias records, leaving DNS TTL behavior unproved in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout still has no DNS TTL behavior proof.
- **D — Correct.** Query authoritative and recursive answers with TTL values during the cutover.
  Query authoritative and recursive answers with TTL values during the cutover. For authoritative DNS and Bastion rollout, this DNS TTL behavior read confirms the service can control how long a positive answer can remain in recursive caches.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q26 — B

**Question:** The authoritative DNS and Bastion rollout rejects name-resolution verification exit status as proof it can control cache duration for a negative DNS lookup. Which authoritative DNS and Bastion rollout result is valid evidence?

- **A — Incorrect.** Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
  Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state. In the authoritative DNS and Bastion rollout, this check observes Bastion public IP. Bastion public IP success in authoritative DNS and Bastion rollout cannot verify DNS negative caching; authoritative DNS and Bastion rollout cannot control cache duration for a negative DNS lookup until DNS negative caching evidence exists.
- **B — Correct.** Query the authoritative name servers directly and compare with the recursive resolver response.
  Query the authoritative name servers directly and compare with the recursive resolver response. The authoritative DNS and Bastion rollout reads DNS negative caching directly; that DNS negative caching result proves the authoritative DNS and Bastion rollout can control cache duration for a negative DNS lookup without another mutation.
- **C — Incorrect.** Query NS records from an external resolver and compare them with the zone's assigned servers.
  Query NS records from an external resolver and compare them with the zone's assigned servers. In the authoritative DNS and Bastion rollout, this check observes DNS delegation. Authoritative DNS and Bastion rollout could pass DNS delegation while DNS negative caching is wrong; authoritative DNS and Bastion rollout still lacks DNS negative caching proof.
- **D — Incorrect.** Query authoritative and recursive answers with TTL values during the cutover.
  Query authoritative and recursive answers with TTL values during the cutover. In the authoritative DNS and Bastion rollout, this check observes DNS TTL behavior. Authoritative DNS and Bastion rollout output covers DNS TTL behavior, not DNS negative caching; the DNS negative caching requirement to control cache duration for a negative DNS lookup remains unverified.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q27 — D

**Question:** The name-resolution verification validator needs one authoritative DNS and Bastion rollout query after the change to use the exact reserved subnet name required by the managed jump service. Which name-resolution verification property should the authoritative DNS and Bastion rollout validator inspect?

- **A — Incorrect.** Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
  Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address. In the authoritative DNS and Bastion rollout, this check observes private VM administration. Authoritative DNS and Bastion rollout reads private VM administration, leaving AzureBastionSubnet naming unproved in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout still has no AzureBastionSubnet naming proof.
- **B — Incorrect.** Query the exact record-set name and type and compare its TTL and record values.
  Query the exact record-set name and type and compare its TTL and record values. In the authoritative DNS and Bastion rollout, this check observes DNS record sets. Authoritative DNS and Bastion rollout could pass DNS record sets while AzureBastionSubnet naming is wrong; authoritative DNS and Bastion rollout still lacks AzureBastionSubnet naming proof.
- **C — Incorrect.** Query the authoritative name servers directly and compare with the recursive resolver response.
  Query the authoritative name servers directly and compare with the recursive resolver response. In the authoritative DNS and Bastion rollout, this check observes DNS negative caching. Authoritative DNS and Bastion rollout output covers DNS negative caching, not AzureBastionSubnet naming; the AzureBastionSubnet naming requirement to use the exact reserved subnet name required by the managed jump service remains unverified.
- **D — Correct.** Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
  For the authoritative DNS and Bastion rollout, this AzureBastionSubnet naming observation is decisive: query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet. It is authoritative DNS and Bastion rollout evidence that operators can use the exact reserved subnet name required by the managed jump service.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q28 — D

**Question:** The network administrator providing secure management and authoritative DNS must confirm the authoritative DNS and Bastion rollout, without mutation, can allocate a subnet large enough for the managed jump service to scale. Which name-resolution verification check qualifies?

- **A — Incorrect.** Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
  Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers. In the authoritative DNS and Bastion rollout, this check observes public DNS zones. Authoritative DNS and Bastion rollout could pass public DNS zones while Bastion subnet sizing is wrong; authoritative DNS and Bastion rollout still lacks Bastion subnet sizing proof.
- **B — Incorrect.** Query targetResource.id and resolve the record to the current target address.
  Query targetResource.id and resolve the record to the current target address. In the authoritative DNS and Bastion rollout, this check observes Azure DNS alias records. Authoritative DNS and Bastion rollout output covers Azure DNS alias records, not Bastion subnet sizing; the Bastion subnet sizing requirement to allocate a subnet large enough for the managed jump service to scale remains unverified.
- **C — Incorrect.** Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
  Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet. In the authoritative DNS and Bastion rollout, this check observes AzureBastionSubnet naming. AzureBastionSubnet naming success in authoritative DNS and Bastion rollout cannot verify Bastion subnet sizing; authoritative DNS and Bastion rollout cannot allocate a subnet large enough for the managed jump service to scale until Bastion subnet sizing evidence exists.
- **D — Correct.** Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
  Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached. Because the authoritative DNS and Bastion rollout check observes Bastion subnet sizing, it independently verifies the requirement to allocate a subnet large enough for the managed jump service to scale.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q29 — A

**Question:** The authoritative DNS and Bastion rollout configuration is complete; the name-resolution verification reviewers need evidence it can attach the supported public address configuration to the managed jump host. Which observation shows success?

- **A — Correct.** Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
  The authoritative DNS and Bastion rollout validator needs this Bastion public IP result: query the Bastion public IP resource ID, SKU, allocation method, and provisioning state. It proves the outcome to attach the supported public address configuration to the managed jump host rather than an adjacent checkpoint.
- **B — Incorrect.** Query NS records from an external resolver and compare them with the zone's assigned servers.
  Query NS records from an external resolver and compare them with the zone's assigned servers. In the authoritative DNS and Bastion rollout, this check observes DNS delegation. DNS delegation success in authoritative DNS and Bastion rollout cannot verify Bastion public IP; authoritative DNS and Bastion rollout cannot attach the supported public address configuration to the managed jump host until Bastion public IP evidence exists.
- **C — Incorrect.** Query authoritative and recursive answers with TTL values during the cutover.
  Query authoritative and recursive answers with TTL values during the cutover. In the authoritative DNS and Bastion rollout, this check observes DNS TTL behavior. Authoritative DNS and Bastion rollout reads DNS TTL behavior, leaving Bastion public IP unproved in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout still has no Bastion public IP proof.
- **D — Incorrect.** Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
  Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached. In the authoritative DNS and Bastion rollout, this check observes Bastion subnet sizing. Authoritative DNS and Bastion rollout could pass Bastion subnet sizing while Bastion public IP is wrong; authoritative DNS and Bastion rollout still lacks Bastion public IP proof.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q30 — D

**Question:** The name-resolution verification validation asks whether the authoritative DNS and Bastion rollout can administer a private virtual machine without assigning it a public address. Which observable state is strongest?

- **A — Incorrect.** Query the exact record-set name and type and compare its TTL and record values.
  Query the exact record-set name and type and compare its TTL and record values. In the authoritative DNS and Bastion rollout, this check observes DNS record sets. DNS record sets success in authoritative DNS and Bastion rollout cannot verify private VM administration; authoritative DNS and Bastion rollout cannot administer a private virtual machine without assigning it a public address until private VM administration evidence exists.
- **B — Incorrect.** Query the authoritative name servers directly and compare with the recursive resolver response.
  Query the authoritative name servers directly and compare with the recursive resolver response. In the authoritative DNS and Bastion rollout, this check observes DNS negative caching. Authoritative DNS and Bastion rollout reads DNS negative caching, leaving private VM administration unproved in authoritative DNS and Bastion rollout; authoritative DNS and Bastion rollout still has no private VM administration proof.
- **C — Incorrect.** Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
  Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state. In the authoritative DNS and Bastion rollout, this check observes Bastion public IP. Authoritative DNS and Bastion rollout could pass Bastion public IP while private VM administration is wrong; authoritative DNS and Bastion rollout still lacks private VM administration proof.
- **D — Correct.** Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
  Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address. This is independent private VM administration evidence for the authoritative DNS and Bastion rollout, even if authoritative DNS and Bastion rollout setup reports success before private VM administration becomes observable.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q31 — A

**Question:** The name-resolution verification support team isolated the authoritative DNS and Bastion rollout incident to the attempt to publish internet records by using Azure-hosted DNS authority. Which condition prevents success?

- **A — Correct.** The domain registrar still delegates to different authoritative name servers.
  The domain registrar still delegates to different authoritative name servers. In authoritative DNS and Bastion rollout, this public DNS zones cause matches the failure to publish internet records by using Azure-hosted DNS authority.
- **B — Incorrect.** Only one of the assigned name servers was added at the registrar.
  Only one of the assigned name servers was added at the registrar. The authoritative DNS and Bastion rollout fault concerns DNS delegation. Authoritative DNS and Bastion rollout could repair DNS delegation while public DNS zones stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to publish internet records by using Azure-hosted DNS authority.
- **C — Incorrect.** The recursive resolver cached NXDOMAIN from a query made before the record existed.
  The recursive resolver cached NXDOMAIN from a query made before the record existed. The authoritative DNS and Bastion rollout fault concerns DNS negative caching. Authoritative DNS and Bastion rollout failed on public DNS zones; this DNS negative caching finding redirects authoritative DNS and Bastion rollout remediation away from public DNS zones.
- **D — Incorrect.** The VM NSG blocks the management port from the Bastion subnet.
  The VM NSG blocks the management port from the Bastion subnet. The authoritative DNS and Bastion rollout fault concerns private VM administration. Authoritative DNS and Bastion rollout may fix private VM administration, yet public DNS zones still fails; this authoritative DNS and Bastion rollout diagnosis of private VM administration is wrong for public DNS zones.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Host a DNS zone in Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q32 — D

**Question:** An authoritative DNS and Bastion rollout query surprises the network administrator providing secure management and authoritative DNS during the name-resolution verification attempt to make the parent domain direct queries to the Azure-hosted child zone. Which finding explains it?

- **A — Incorrect.** A CNAME was created at a label that also has another conflicting record type.
  A CNAME was created at a label that also has another conflicting record type. The authoritative DNS and Bastion rollout fault concerns DNS record sets. Authoritative DNS and Bastion rollout could repair DNS record sets while DNS delegation stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to make the parent domain direct queries to the Azure-hosted child zone.
- **B — Incorrect.** The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment.
  The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment. The authoritative DNS and Bastion rollout fault concerns AzureBastionSubnet naming. Authoritative DNS and Bastion rollout failed on DNS delegation; this AzureBastionSubnet naming finding redirects authoritative DNS and Bastion rollout remediation away from DNS delegation.
- **C — Incorrect.** The domain registrar still delegates to different authoritative name servers.
  The domain registrar still delegates to different authoritative name servers. The authoritative DNS and Bastion rollout fault concerns public DNS zones. Authoritative DNS and Bastion rollout may fix public DNS zones, yet DNS delegation still fails; this authoritative DNS and Bastion rollout diagnosis of public DNS zones is wrong for DNS delegation.
- **D — Correct.** Only one of the assigned name servers was added at the registrar.
  Only one of the assigned name servers was added at the registrar. This authoritative DNS and Bastion rollout condition breaks DNS delegation, explaining why operators cannot make the parent domain direct queries to the Azure-hosted child zone.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Delegate a domain to Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation)

**Source reviewed:** 2026-08-31

## LAB20-Q33 — C

**Question:** Other authoritative DNS and Bastion rollout components are healthy, but the name-resolution verification still cannot publish multiple values with the same owner, type, and time-to-live. Which state causes the isolated failure?

- **A — Incorrect.** A literal A record was used and became stale after the public IP changed.
  A literal A record was used and became stale after the public IP changed. The authoritative DNS and Bastion rollout fault concerns Azure DNS alias records. Authoritative DNS and Bastion rollout failed on DNS record sets; this Azure DNS alias records finding redirects authoritative DNS and Bastion rollout remediation away from DNS record sets.
- **B — Incorrect.** The existing AzureBastionSubnet is too small for the requested Bastion deployment.
  The existing AzureBastionSubnet is too small for the requested Bastion deployment. The authoritative DNS and Bastion rollout fault concerns Bastion subnet sizing. Authoritative DNS and Bastion rollout may fix Bastion subnet sizing, yet DNS record sets still fails; this authoritative DNS and Bastion rollout diagnosis of Bastion subnet sizing is wrong for DNS record sets.
- **C — Correct.** A CNAME was created at a label that also has another conflicting record type.
  For the authoritative DNS and Bastion rollout, the DNS record sets failure is causal: a CNAME was created at a label that also has another conflicting record type. Correcting it restores the ability to publish multiple values with the same owner, type, and time-to-live.
- **D — Incorrect.** Only one of the assigned name servers was added at the registrar.
  Only one of the assigned name servers was added at the registrar. The authoritative DNS and Bastion rollout fault concerns DNS delegation. Authoritative DNS and Bastion rollout could repair DNS delegation while DNS record sets stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to publish multiple values with the same owner, type, and time-to-live.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q34 — A

**Question:** During a name-resolution verification fault drill, the authoritative DNS and Bastion rollout does not point a zone-apex record at an Azure resource without hard-coding its address. Which finding identifies the defect?

- **A — Correct.** A literal A record was used and became stale after the public IP changed.
  A literal A record was used and became stale after the public IP changed. The finding is specific to Azure DNS alias records in the authoritative DNS and Bastion rollout; repairing Azure DNS alias records restores the authoritative DNS and Bastion rollout ability to point a zone-apex record at an Azure resource without hard-coding its address.
- **B — Incorrect.** Validation used a recursive cache that still holds the previous answer.
  Validation used a recursive cache that still holds the previous answer. The authoritative DNS and Bastion rollout fault concerns DNS TTL behavior. Authoritative DNS and Bastion rollout has DNS TTL behavior impact, but Azure DNS alias records is the authoritative DNS and Bastion rollout failed path; the DNS TTL behavior state cannot produce Azure DNS alias records failure.
- **C — Incorrect.** The supplied public IP uses an unsupported Basic SKU.
  The supplied public IP uses an unsupported Basic SKU. The authoritative DNS and Bastion rollout fault concerns Bastion public IP. Authoritative DNS and Bastion rollout could repair Bastion public IP while Azure DNS alias records stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to point a zone-apex record at an Azure resource without hard-coding its address.
- **D — Incorrect.** A CNAME was created at a label that also has another conflicting record type.
  A CNAME was created at a label that also has another conflicting record type. The authoritative DNS and Bastion rollout fault concerns DNS record sets. Authoritative DNS and Bastion rollout failed on Azure DNS alias records; this DNS record sets finding redirects authoritative DNS and Bastion rollout remediation away from Azure DNS alias records.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q35 — A

**Question:** The authoritative DNS and Bastion rollout setup finishes, yet the name-resolution verification cannot control how long a positive answer can remain in recursive caches. Which misconfiguration explains the mismatch?

- **A — Correct.** Validation used a recursive cache that still holds the previous answer.
  The authoritative DNS and Bastion rollout cannot control how long a positive answer can remain in recursive caches because of this DNS TTL behavior defect: validation used a recursive cache that still holds the previous answer. The symptom and repair align.
- **B — Incorrect.** The recursive resolver cached NXDOMAIN from a query made before the record existed.
  The recursive resolver cached NXDOMAIN from a query made before the record existed. The authoritative DNS and Bastion rollout fault concerns DNS negative caching. Authoritative DNS and Bastion rollout could repair DNS negative caching while DNS TTL behavior stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to control how long a positive answer can remain in recursive caches.
- **C — Incorrect.** The VM NSG blocks the management port from the Bastion subnet.
  The VM NSG blocks the management port from the Bastion subnet. The authoritative DNS and Bastion rollout fault concerns private VM administration. Authoritative DNS and Bastion rollout failed on DNS TTL behavior; this private VM administration finding redirects authoritative DNS and Bastion rollout remediation away from DNS TTL behavior.
- **D — Incorrect.** A literal A record was used and became stale after the public IP changed.
  A literal A record was used and became stale after the public IP changed. The authoritative DNS and Bastion rollout fault concerns Azure DNS alias records. Authoritative DNS and Bastion rollout may fix Azure DNS alias records, yet DNS TTL behavior still fails; this authoritative DNS and Bastion rollout diagnosis of Azure DNS alias records is wrong for DNS TTL behavior.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q36 — C

**Question:** A name-resolution verification break/fix in the authoritative DNS and Bastion rollout fails when operators try to control cache duration for a negative DNS lookup. Which diagnosis fits?

- **A — Incorrect.** The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment.
  The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment. The authoritative DNS and Bastion rollout fault concerns AzureBastionSubnet naming. Authoritative DNS and Bastion rollout could repair AzureBastionSubnet naming while DNS negative caching stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to control cache duration for a negative DNS lookup.
- **B — Incorrect.** The domain registrar still delegates to different authoritative name servers.
  The domain registrar still delegates to different authoritative name servers. The authoritative DNS and Bastion rollout fault concerns public DNS zones. Authoritative DNS and Bastion rollout failed on DNS negative caching; this public DNS zones finding redirects authoritative DNS and Bastion rollout remediation away from DNS negative caching.
- **C — Correct.** The recursive resolver cached NXDOMAIN from a query made before the record existed.
  The recursive resolver cached NXDOMAIN from a query made before the record existed. Removing this DNS negative caching condition lets the authoritative DNS and Bastion rollout control cache duration for a negative DNS lookup while leaving healthy controls unchanged.
- **D — Incorrect.** Validation used a recursive cache that still holds the previous answer.
  Validation used a recursive cache that still holds the previous answer. The authoritative DNS and Bastion rollout fault concerns DNS TTL behavior. Authoritative DNS and Bastion rollout has DNS TTL behavior impact, but DNS negative caching is the authoritative DNS and Bastion rollout failed path; the DNS TTL behavior state cannot produce DNS negative caching failure.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q37 — D

**Question:** The authoritative DNS and Bastion rollout troubleshooting scope is the name-resolution verification need to use the exact reserved subnet name required by the managed jump service. Which condition should be corrected first?

- **A — Incorrect.** The existing AzureBastionSubnet is too small for the requested Bastion deployment.
  The existing AzureBastionSubnet is too small for the requested Bastion deployment. The authoritative DNS and Bastion rollout fault concerns Bastion subnet sizing. Authoritative DNS and Bastion rollout failed on AzureBastionSubnet naming; this Bastion subnet sizing finding redirects authoritative DNS and Bastion rollout remediation away from AzureBastionSubnet naming.
- **B — Incorrect.** Only one of the assigned name servers was added at the registrar.
  Only one of the assigned name servers was added at the registrar. The authoritative DNS and Bastion rollout fault concerns DNS delegation. Authoritative DNS and Bastion rollout may fix DNS delegation, yet AzureBastionSubnet naming still fails; this authoritative DNS and Bastion rollout diagnosis of DNS delegation is wrong for AzureBastionSubnet naming.
- **C — Incorrect.** The recursive resolver cached NXDOMAIN from a query made before the record existed.
  The recursive resolver cached NXDOMAIN from a query made before the record existed. The authoritative DNS and Bastion rollout fault concerns DNS negative caching. Authoritative DNS and Bastion rollout has DNS negative caching impact, but AzureBastionSubnet naming is the authoritative DNS and Bastion rollout failed path; the DNS negative caching state cannot produce AzureBastionSubnet naming failure.
- **D — Correct.** The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment.
  The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment. In authoritative DNS and Bastion rollout, this AzureBastionSubnet naming cause matches the failure to use the exact reserved subnet name required by the managed jump service.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q38 — D

**Question:** The authoritative DNS and Bastion rollout result is partial because the name-resolution verification cannot allocate a subnet large enough for the managed jump service to scale. Which condition accounts for that result?

- **A — Incorrect.** The supplied public IP uses an unsupported Basic SKU.
  The supplied public IP uses an unsupported Basic SKU. The authoritative DNS and Bastion rollout fault concerns Bastion public IP. Authoritative DNS and Bastion rollout may fix Bastion public IP, yet Bastion subnet sizing still fails; this authoritative DNS and Bastion rollout diagnosis of Bastion public IP is wrong for Bastion subnet sizing.
- **B — Incorrect.** A CNAME was created at a label that also has another conflicting record type.
  A CNAME was created at a label that also has another conflicting record type. The authoritative DNS and Bastion rollout fault concerns DNS record sets. Authoritative DNS and Bastion rollout has DNS record sets impact, but Bastion subnet sizing is the authoritative DNS and Bastion rollout failed path; the DNS record sets state cannot produce Bastion subnet sizing failure.
- **C — Incorrect.** The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment.
  The subnet is named BastionSubnet and therefore is not recognized for Bastion deployment. The authoritative DNS and Bastion rollout fault concerns AzureBastionSubnet naming. Authoritative DNS and Bastion rollout could repair AzureBastionSubnet naming while Bastion subnet sizing stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to allocate a subnet large enough for the managed jump service to scale.
- **D — Correct.** The existing AzureBastionSubnet is too small for the requested Bastion deployment.
  The existing AzureBastionSubnet is too small for the requested Bastion deployment. This authoritative DNS and Bastion rollout condition breaks Bastion subnet sizing, explaining why operators cannot allocate a subnet large enough for the managed jump service to scale.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q39 — C

**Question:** The name-resolution verification evidence shows the authoritative DNS and Bastion rollout cannot attach the supported public address configuration to the managed jump host. Which root cause fits that evidence?

- **A — Incorrect.** The VM NSG blocks the management port from the Bastion subnet.
  The VM NSG blocks the management port from the Bastion subnet. The authoritative DNS and Bastion rollout fault concerns private VM administration. Authoritative DNS and Bastion rollout has private VM administration impact, but Bastion public IP is the authoritative DNS and Bastion rollout failed path; the private VM administration state cannot produce Bastion public IP failure.
- **B — Incorrect.** A literal A record was used and became stale after the public IP changed.
  A literal A record was used and became stale after the public IP changed. The authoritative DNS and Bastion rollout fault concerns Azure DNS alias records. Authoritative DNS and Bastion rollout could repair Azure DNS alias records while Bastion public IP stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to attach the supported public address configuration to the managed jump host.
- **C — Correct.** The supplied public IP uses an unsupported Basic SKU.
  For the authoritative DNS and Bastion rollout, the Bastion public IP failure is causal: the supplied public IP uses an unsupported Basic SKU. Correcting it restores the ability to attach the supported public address configuration to the managed jump host.
- **D — Incorrect.** The existing AzureBastionSubnet is too small for the requested Bastion deployment.
  The existing AzureBastionSubnet is too small for the requested Bastion deployment. The authoritative DNS and Bastion rollout fault concerns Bastion subnet sizing. Authoritative DNS and Bastion rollout may fix Bastion subnet sizing, yet Bastion public IP still fails; this authoritative DNS and Bastion rollout diagnosis of Bastion subnet sizing is wrong for Bastion public IP.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q40 — D

**Question:** Although the authoritative DNS and Bastion rollout is meant to let the name-resolution verification administer a private virtual machine without assigning it a public address, its checkpoint fails. Which name-resolution verification defect explains the failure?

- **A — Incorrect.** The domain registrar still delegates to different authoritative name servers.
  The domain registrar still delegates to different authoritative name servers. The authoritative DNS and Bastion rollout fault concerns public DNS zones. Authoritative DNS and Bastion rollout could repair public DNS zones while private VM administration stays broken in authoritative DNS and Bastion rollout; the authoritative DNS and Bastion rollout remains unable to administer a private virtual machine without assigning it a public address.
- **B — Incorrect.** Validation used a recursive cache that still holds the previous answer.
  Validation used a recursive cache that still holds the previous answer. The authoritative DNS and Bastion rollout fault concerns DNS TTL behavior. Authoritative DNS and Bastion rollout failed on private VM administration; this DNS TTL behavior finding redirects authoritative DNS and Bastion rollout remediation away from private VM administration.
- **C — Incorrect.** The supplied public IP uses an unsupported Basic SKU.
  The supplied public IP uses an unsupported Basic SKU. The authoritative DNS and Bastion rollout fault concerns Bastion public IP. Authoritative DNS and Bastion rollout may fix Bastion public IP, yet private VM administration still fails; this authoritative DNS and Bastion rollout diagnosis of Bastion public IP is wrong for private VM administration.
- **D — Correct.** The VM NSG blocks the management port from the Bastion subnet.
  The VM NSG blocks the management port from the Bastion subnet. The finding is specific to private VM administration in the authoritative DNS and Bastion rollout; repairing private VM administration restores the authoritative DNS and Bastion rollout ability to administer a private virtual machine without assigning it a public address.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q41 — A

**Question:** Only the authoritative DNS and Bastion rollout change needed to publish internet records by using Azure-hosted DNS authority is allowed, and name-resolution verification proof is mandatory. Which pair fits?

- **A — Correct.** First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
  The authoritative DNS and Bastion rollout gets a complete public DNS zones sequence here: first, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers. Read-back evidence follows the change.
- **B — Incorrect.** First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values.
  First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values. This authoritative DNS and Bastion rollout pair serves DNS record sets. Authoritative DNS and Bastion rollout proves DNS record sets, but public DNS zones lacks implementation in authoritative DNS and Bastion rollout and public DNS zones proof; the public DNS zones outcome to publish internet records by using Azure-hosted DNS authority remains open.
- **C — Incorrect.** First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
  First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet. This authoritative DNS and Bastion rollout pair serves AzureBastionSubnet naming. Authoritative DNS and Bastion rollout uses AzureBastionSubnet naming for both steps; public DNS zones remains untouched in authoritative DNS and Bastion rollout, so its public DNS zones gate to publish internet records by using Azure-hosted DNS authority fails.
- **D — Incorrect.** First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
  First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached. This authoritative DNS and Bastion rollout pair serves Bastion subnet sizing. Authoritative DNS and Bastion rollout closes Bastion subnet sizing, not public DNS zones; without the public DNS zones workflow, it cannot publish internet records by using Azure-hosted DNS authority.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Host a DNS zone in Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q42 — B

**Question:** The authoritative DNS and Bastion rollout runbook separates name-resolution verification mutation from validation while it must make the parent domain direct queries to the Azure-hosted child zone. Which sequence proves it cleanly?

- **A — Incorrect.** First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
  First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address. This authoritative DNS and Bastion rollout pair serves Azure DNS alias records. Authoritative DNS and Bastion rollout proves Azure DNS alias records, but DNS delegation lacks implementation in authoritative DNS and Bastion rollout and DNS delegation proof; the DNS delegation outcome to make the parent domain direct queries to the Azure-hosted child zone remains open.
- **B — Correct.** First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.
  First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers. This ordered DNS delegation workflow lets the authoritative DNS and Bastion rollout make the parent domain direct queries to the Azure-hosted child zone and then verify the resulting state.
- **C — Incorrect.** First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
  First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached. This authoritative DNS and Bastion rollout pair serves Bastion subnet sizing. Authoritative DNS and Bastion rollout closes Bastion subnet sizing, not DNS delegation; without the DNS delegation workflow, it cannot make the parent domain direct queries to the Azure-hosted child zone.
- **D — Incorrect.** First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
  First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state. This authoritative DNS and Bastion rollout pair serves Bastion public IP. Bastion public IP cannot replace DNS delegation in authoritative DNS and Bastion rollout. Use this DNS delegation pair instead: First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Delegate a domain to Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation)

**Source reviewed:** 2026-08-31

## LAB20-Q43 — C

**Question:** The authoritative DNS and Bastion rollout checkpoint requires both this name-resolution verification outcome—publish multiple values with the same owner, type, and time-to-live—and a read-only authoritative DNS and Bastion rollout state check. Which name-resolution verification response is complete?

- **A — Incorrect.** First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.
  First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover. This authoritative DNS and Bastion rollout pair serves DNS TTL behavior. Authoritative DNS and Bastion rollout uses DNS TTL behavior for both steps; DNS record sets remains untouched in authoritative DNS and Bastion rollout, so its DNS record sets gate to publish multiple values with the same owner, type, and time-to-live fails.
- **B — Incorrect.** First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
  First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state. This authoritative DNS and Bastion rollout pair serves Bastion public IP. Authoritative DNS and Bastion rollout closes Bastion public IP, not DNS record sets; without the DNS record sets workflow, it cannot publish multiple values with the same owner, type, and time-to-live.
- **C — Correct.** First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values.
  First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values. For authoritative DNS and Bastion rollout, the DNS record sets operation precedes its DNS record sets read-back check, allowing it to publish multiple values with the same owner, type, and time-to-live.
- **D — Incorrect.** First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
  First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address. This authoritative DNS and Bastion rollout pair serves private VM administration. Authoritative DNS and Bastion rollout proves private VM administration, but DNS record sets lacks implementation in authoritative DNS and Bastion rollout and DNS record sets proof; the DNS record sets outcome to publish multiple values with the same owner, type, and time-to-live remains open.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q44 — C

**Question:** The authoritative DNS and Bastion rollout runbook must point a zone-apex record at an Azure resource without hard-coding its address, then retain name-resolution verification read-back evidence. Which authoritative DNS and Bastion rollout pair completes both duties?

- **A — Incorrect.** First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.
  First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response. This authoritative DNS and Bastion rollout pair serves DNS negative caching. Authoritative DNS and Bastion rollout closes DNS negative caching, not Azure DNS alias records; without the Azure DNS alias records workflow, it cannot point a zone-apex record at an Azure resource without hard-coding its address.
- **B — Incorrect.** First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
  First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address. This authoritative DNS and Bastion rollout pair serves private VM administration. Private VM administration cannot replace Azure DNS alias records in authoritative DNS and Bastion rollout. Use this Azure DNS alias records pair instead: First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
- **C — Correct.** First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
  First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address. In the authoritative DNS and Bastion rollout, the first Azure DNS alias records step runs; the authoritative DNS and Bastion rollout then reads Azure DNS alias records state to prove it can point a zone-apex record at an Azure resource without hard-coding its address.
- **D — Incorrect.** First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
  First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers. This authoritative DNS and Bastion rollout pair serves public DNS zones. Authoritative DNS and Bastion rollout uses public DNS zones for both steps; Azure DNS alias records remains untouched in authoritative DNS and Bastion rollout, so its Azure DNS alias records gate to point a zone-apex record at an Azure resource without hard-coding its address fails.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q45 — B

**Question:** To satisfy the name-resolution verification requirement, operators must change the authoritative DNS and Bastion rollout configuration and prove it can control how long a positive answer can remain in recursive caches. Which sequence is coherent?

- **A — Incorrect.** First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
  First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet. This authoritative DNS and Bastion rollout pair serves AzureBastionSubnet naming. AzureBastionSubnet naming cannot replace DNS TTL behavior in authoritative DNS and Bastion rollout. Use this DNS TTL behavior pair instead: First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.
- **B — Correct.** First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.
  For the authoritative DNS and Bastion rollout, the safe DNS TTL behavior order is: first, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover. The authoritative DNS and Bastion rollout records DNS TTL behavior proof after configuration.
- **C — Incorrect.** First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
  First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers. This authoritative DNS and Bastion rollout pair serves public DNS zones. Authoritative DNS and Bastion rollout uses public DNS zones for both steps; DNS TTL behavior remains untouched in authoritative DNS and Bastion rollout, so its DNS TTL behavior gate to control how long a positive answer can remain in recursive caches fails.
- **D — Incorrect.** First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.
  First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers. This authoritative DNS and Bastion rollout pair serves DNS delegation. Authoritative DNS and Bastion rollout closes DNS delegation, not DNS TTL behavior; without the DNS TTL behavior workflow, it cannot control how long a positive answer can remain in recursive caches.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q46 — C

**Question:** The network administrator providing secure management and authoritative DNS needs a safe authoritative DNS and Bastion rollout change to control cache duration for a negative DNS lookup, followed by name-resolution verification evidence. Which pair merits approval?

- **A — Incorrect.** First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
  First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached. This authoritative DNS and Bastion rollout pair serves Bastion subnet sizing. Authoritative DNS and Bastion rollout proves Bastion subnet sizing, but DNS negative caching lacks implementation in authoritative DNS and Bastion rollout and DNS negative caching proof; the DNS negative caching outcome to control cache duration for a negative DNS lookup remains open.
- **B — Incorrect.** First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.
  First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers. This authoritative DNS and Bastion rollout pair serves DNS delegation. Authoritative DNS and Bastion rollout uses DNS delegation for both steps; DNS negative caching remains untouched in authoritative DNS and Bastion rollout, so its DNS negative caching gate to control cache duration for a negative DNS lookup fails.
- **C — Correct.** First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.
  First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response. The authoritative DNS and Bastion rollout uses its DNS negative caching mutation gate and DNS negative caching verification gate before it can control cache duration for a negative DNS lookup.
- **D — Incorrect.** First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values.
  First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values. This authoritative DNS and Bastion rollout pair serves DNS record sets. DNS record sets cannot replace DNS negative caching in authoritative DNS and Bastion rollout. Use this DNS negative caching pair instead: First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.

**Objectives:** `NW-DNSLB-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB20-CP01`).

**Microsoft Learn sources:**

- [Azure DNS records and record sets](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records)

**Source reviewed:** 2026-08-31

## LAB20-Q47 — D

**Question:** The authoritative DNS and Bastion rollout has two name-resolution verification gates: use the exact reserved subnet name required by the managed jump service, then prove the authoritative DNS and Bastion rollout state. Which name-resolution verification sequence works?

- **A — Incorrect.** First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
  First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state. This authoritative DNS and Bastion rollout pair serves Bastion public IP. Authoritative DNS and Bastion rollout uses Bastion public IP for both steps; AzureBastionSubnet naming remains untouched in authoritative DNS and Bastion rollout, so its AzureBastionSubnet naming gate to use the exact reserved subnet name required by the managed jump service fails.
- **B — Incorrect.** First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values.
  First, Create the required A, AAAA, CNAME, MX, TXT, or other supported record set with an intentional TTL. Then, Query the exact record-set name and type and compare its TTL and record values. This authoritative DNS and Bastion rollout pair serves DNS record sets. Authoritative DNS and Bastion rollout closes DNS record sets, not AzureBastionSubnet naming; without the AzureBastionSubnet naming workflow, it cannot use the exact reserved subnet name required by the managed jump service.
- **C — Incorrect.** First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
  First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address. This authoritative DNS and Bastion rollout pair serves Azure DNS alias records. Azure DNS alias records cannot replace AzureBastionSubnet naming in authoritative DNS and Bastion rollout. Use this AzureBastionSubnet naming pair instead: First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
- **D — Correct.** First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
  The authoritative DNS and Bastion rollout gets a complete AzureBastionSubnet naming sequence here: first, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet. Read-back evidence follows the change.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB20-CP02`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q48 — C

**Question:** Which name-resolution verification path makes the authoritative DNS and Bastion rollout able to allocate a subnet large enough for the managed jump service to scale, then inspects the defining properties?

- **A — Incorrect.** First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
  First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address. This authoritative DNS and Bastion rollout pair serves private VM administration. Authoritative DNS and Bastion rollout closes private VM administration, not Bastion subnet sizing; without the Bastion subnet sizing workflow, it cannot allocate a subnet large enough for the managed jump service to scale.
- **B — Incorrect.** First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address.
  First, Use an alias A record when a supported Azure public IP or endpoint should be the record target. Then, Query targetResource.id and resolve the record to the current target address. This authoritative DNS and Bastion rollout pair serves Azure DNS alias records. Azure DNS alias records cannot replace Bastion subnet sizing in authoritative DNS and Bastion rollout. Use this Bastion subnet sizing pair instead: First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
- **C — Correct.** First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached.
  First, Allocate an approved /26-or-larger AzureBastionSubnet without other workloads. Then, Query the subnet addressPrefix and confirm no unrelated NIC configurations are attached. This ordered Bastion subnet sizing workflow lets the authoritative DNS and Bastion rollout allocate a subnet large enough for the managed jump service to scale and then verify the resulting state.
- **D — Incorrect.** First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.
  First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover. This authoritative DNS and Bastion rollout pair serves DNS TTL behavior. Authoritative DNS and Bastion rollout uses DNS TTL behavior for both steps; Bastion subnet sizing remains untouched in authoritative DNS and Bastion rollout, so its Bastion subnet sizing gate to allocate a subnet large enough for the managed jump service to scale fails.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB20-CP03`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q49 — B

**Question:** At the authoritative DNS and Bastion rollout approval gate, operators must show that the name-resolution verification can attach the supported public address configuration to the managed jump host. Which name-resolution verification configure-and-check pair is defensible?

- **A — Incorrect.** First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers.
  First, Create the zone for a domain the organization controls and retain its assigned name servers. Then, Query zone name, numberOfRecordSets, maxNumberOfRecordSets, and assigned nameServers. This authoritative DNS and Bastion rollout pair serves public DNS zones. Public DNS zones cannot replace Bastion public IP in authoritative DNS and Bastion rollout. Use this Bastion public IP pair instead: First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
- **B — Correct.** First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state.
  First, Create a Standard static public IP and attach it to the Bastion IP configuration. Then, Query the Bastion public IP resource ID, SKU, allocation method, and provisioning state. For authoritative DNS and Bastion rollout, the Bastion public IP operation precedes its Bastion public IP read-back check, allowing it to attach the supported public address configuration to the managed jump host.
- **C — Incorrect.** First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover.
  First, Lower TTL before a planned cutover, wait for prior caches, then update the record. Then, Query authoritative and recursive answers with TTL values during the cutover. This authoritative DNS and Bastion rollout pair serves DNS TTL behavior. Authoritative DNS and Bastion rollout uses DNS TTL behavior for both steps; Bastion public IP remains untouched in authoritative DNS and Bastion rollout, so its Bastion public IP gate to attach the supported public address configuration to the managed jump host fails.
- **D — Incorrect.** First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.
  First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response. This authoritative DNS and Bastion rollout pair serves DNS negative caching. Authoritative DNS and Bastion rollout closes DNS negative caching, not Bastion public IP; without the Bastion public IP workflow, it cannot attach the supported public address configuration to the managed jump host.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB20-CP04`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31

## LAB20-Q50 — C

**Question:** The authoritative DNS and Bastion rollout forbids a partial name-resolution verification result. Operators must first administer a private virtual machine without assigning it a public address and afterward confirm the authoritative DNS and Bastion rollout outcome. Which name-resolution verification sequence is complete?

- **A — Incorrect.** First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers.
  First, Copy every assigned Azure DNS name server into the parent delegation. Then, Query NS records from an external resolver and compare them with the zone's assigned servers. This authoritative DNS and Bastion rollout pair serves DNS delegation. Authoritative DNS and Bastion rollout proves DNS delegation, but private VM administration lacks implementation in authoritative DNS and Bastion rollout and private VM administration proof; the private VM administration outcome to administer a private virtual machine without assigning it a public address remains open.
- **B — Incorrect.** First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response.
  First, Create required records before the validation window and account for prior negative responses. Then, Query the authoritative name servers directly and compare with the recursive resolver response. This authoritative DNS and Bastion rollout pair serves DNS negative caching. Authoritative DNS and Bastion rollout uses DNS negative caching for both steps; private VM administration remains untouched in authoritative DNS and Bastion rollout, so its private VM administration gate to administer a private virtual machine without assigning it a public address fails.
- **C — Correct.** First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.
  First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address. In the authoritative DNS and Bastion rollout, the first private VM administration step runs; the authoritative DNS and Bastion rollout then reads private VM administration state to prove it can administer a private virtual machine without assigning it a public address.
- **D — Incorrect.** First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet.
  First, Create the dedicated subnet with the exact reserved name before deploying the host. Then, Query the Bastion IP configuration and confirm its subnet resource ID ends with AzureBastionSubnet. This authoritative DNS and Bastion rollout pair serves AzureBastionSubnet naming. AzureBastionSubnet naming cannot replace private VM administration in authoritative DNS and Bastion rollout. Use this private VM administration pair instead: First, Remove unnecessary VM public exposure and allow the required Bastion-to-VM management flow. Then, Confirm the VM NIC has only a private IP and validate Bastion connectivity to that address.

**Objectives:** `NW-SECURE-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB20-CP05`).

**Microsoft Learn sources:**

- [Create an Azure Bastion host with Azure CLI](https://learn.microsoft.com/en-us/azure/bastion/create-host-cli)

**Source reviewed:** 2026-08-31
