#!/usr/bin/env python3
"""One-time assessment prose rewrite used during the 2026-08 curriculum overhaul.

The script preserves question identity, mappings, difficulty, answer position,
options, sources, and review dates. It rewrites only stems and option
explanations. Remove this helper after the authored YAML and rendered Markdown
have been reviewed.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from assessment_sources import expected_source


ROOT = Path(__file__).resolve().parents[1]
LETTERS = ("A", "B", "C", "D")
WORD_RE = re.compile(r"[a-z0-9]+")

PROFILES = {
    "01": "operations-team identity onboarding",
    "02": "external-collaboration and SSPR pilot",
    "03": "least-privilege workload delegation",
    "04": "governed disposable-workload hierarchy",
    "05": "policy-and-cost governance rollout",
    "06": "hardened general-purpose storage account",
    "07": "restricted storage data-plane design",
    "08": "blob retention and replication service",
    "09": "recoverable team file share",
    "10": "reviewed Bicep deployment pipeline",
    "11": "secured Linux VM maintenance window",
    "12": "resilient compute capacity design",
    "13": "approved container image release",
    "14": "revisioned serverless container release",
    "15": "App Service capacity and slot release",
    "16": "hardened and recoverable web application",
    "17": "hub-and-spoke network build",
    "18": "application traffic-control investigation",
    "19": "private Storage connectivity evaluation",
    "20": "authoritative DNS and Bastion rollout",
    "21": "resilient HTTP backend publication",
    "22": "evidence-based monitoring workspace",
    "23": "actionable alert-routing design",
    "24": "test-VM protection and restore drill",
    "25": "Azure-to-Azure disaster-recovery pilot",
}

LENSES = {
    "01": "identity onboarding",
    "02": "guest collaboration",
    "03": "access delegation",
    "04": "resource hierarchy",
    "05": "cost governance",
    "06": "storage hardening",
    "07": "network perimeter",
    "08": "blob retention",
    "09": "file-service acceptance",
    "10": "template deployment",
    "11": "VM maintenance",
    "12": "compute resilience",
    "13": "image release",
    "14": "revision rollout",
    "15": "slot release",
    "16": "web hardening",
    "17": "network peering",
    "18": "traffic-flow investigation",
    "19": "endpoint comparison",
    "20": "name-resolution verification",
    "21": "backend readiness",
    "22": "telemetry assessment",
    "23": "alert routing",
    "24": "restore rehearsal",
    "25": "failover pilot",
}


# Operational requirements deliberately avoid repeating the feature label used
# by the correct option.  Each ten-entry tuple follows the concept order for the
# lab and is reused across behavior, implementation, validation, diagnosis, and
# implement/verify questions.
CONCEPT_CUES = {
    "01": (
        "use a custom tenant suffix when creating an operations account",
        "create a user whose identity exists only in this tenant",
        "capture organizational profile metadata on the directory object",
        "block one user from signing in without deleting the account",
        "build a security-only group that has no email address",
        "give a user the access assigned to an operations group",
        "let an administrator manage membership without receiving the group's access",
        "target automation to members while excluding external collaborators",
        "recover a user that was deleted during the retention window",
        "keep automation stable after a display name or sign-in name changes",
    ),
    "02": (
        "confirm that the tenant has an unused product unit before assignment",
        "supply the regional attribute required before a cloud license is assigned",
        "license one pilot user without depending on group membership",
        "license a rotating team through membership rather than individual assignments",
        "send a redeemable collaboration invitation to an external address",
        "distinguish an invited account from one that has accepted its invitation",
        "identify external collaborators without relying on their display names",
        "limit password-reset registration to the approved pilot population",
        "allow only the approved proofs during password reset",
        "stop safely when the tenant lacks the entitlement or role needed for reset changes",
    ),
    "03": (
        "separate a role's permissions from the principal and scope that receive them",
        "let an auditor inspect configuration without changing it",
        "let an operator manage resources without granting access to other principals",
        "delegate role-assignment administration without granting broad resource changes",
        "grant only the permissions and scope needed for the stated job",
        "predict access inherited from a parent management boundary",
        "limit an assignment to one named resource",
        "delegate the same access to a team through one directory group",
        "explain a principal's final permissions after all applicable assignments are combined",
        "explain why an allow assignment does not overcome an explicit platform block",
    ),
    "04": (
        "create and later remove one owned deployment boundary",
        "prevent commands from targeting the wrong Azure subscription",
        "organize subscriptions under the intended governance parent",
        "apply parent governance consistently to descendant subscriptions",
        "label resources so cost and ownership queries can find them",
        "avoid assuming that a parent label automatically appears on every child",
        "prevent accidental deletion while still allowing supported updates",
        "prevent both deletion and control-plane modification of a protected resource",
        "relocate supported resources without recreating them",
        "choose the metadata region for a deployment boundary independently of its resources",
    ),
    "05": (
        "package a governance rule and apply it at the intended scope",
        "deploy several related governance rules as one versioned assignment",
        "measure existing resources against an assigned governance rule",
        "block a noncompliant creation request before the resource is deployed",
        "correct existing noncompliant resources after a managed change is assigned",
        "receive notifications without expecting spending to be stopped automatically",
        "notify owners before projected spending reaches the configured limit",
        "route cost notifications to the approved recipients",
        "identify rightsizing or shutdown opportunities from service telemetry",
        "exclude an approved child scope without weakening governance elsewhere",
    ),
    "06": (
        "create the general-purpose account type that supports current storage services",
        "produce a globally unique lowercase account name with no punctuation",
        "replicate data synchronously three ways at a single site",
        "survive a single availability-zone failure within the primary region",
        "allow reads from the secondary region when geo-replicated data is available",
        "reject storage requests that do not use an encrypted transport",
        "refuse clients that negotiate an obsolete transport protocol",
        "accept only Microsoft Entra credentials for data access",
        "replace a compromised credential without losing the second recovery credential",
        "confirm that stored service data is encrypted without an application change",
    ),
    "07": (
        "deny public-endpoint traffic unless an explicit network exception allows it",
        "permit traffic at the public service address only from an approved IPv4 range",
        "authorize one subnet on the service firewall while retaining the public endpoint",
        "allow only the limited platform services supported by the firewall bypass",
        "choose whether delegated access covers one service or several account services",
        "have a Microsoft Entra principal sign temporary Blob access instead of an account credential",
        "bound delegated access to an intentional start and expiry window",
        "attach revocable constraints to service-level delegated tokens",
        "invalidate tokens that refer to a named server-side access policy",
        "avoid exposing a credential that grants broad authority over the account",
    ),
    "08": (
        "keep private data from being read without an authorization header",
        "place frequently read and rarely read blobs in cost-appropriate tiers",
        "apply retention automation only to blobs matching the intended prefix or type",
        "move eligible data to a cooler tier after the configured age",
        "delete only objects that satisfy the retention rule's age conditions",
        "recover a blob deleted after data protection was enabled",
        "recover a container removed during its retention window",
        "retain an earlier block-blob state after a write or deletion",
        "copy supported block-blob changes asynchronously to a second account",
        "copy a directory safely without deleting unrelated destination data",
    ),
    "09": (
        "cap the capacity available to a team file share",
        "select the file-sharing protocol that matches the client workload",
        "authenticate file clients with an approved directory identity",
        "grant a principal access at the share boundary",
        "limit access to particular directories and files after share access is granted",
        "restrict share connectivity to the sanctioned route",
        "capture a point-in-time, read-only view of share contents",
        "restore a share removed during the service retention period",
        "transfer file-share content with a resumable command-line data mover",
        "diagnose clients that cannot reach the SMB endpoint on its required port",
    ),
    "10": (
        "describe desired Azure resources so repeated deployments converge on that state",
        "vary deployment inputs between environments without changing the template body",
        "reuse a computed expression inside the template without exposing it to callers",
        "return a deployment value needed by a later workflow",
        "ensure one declared resource is deployed after another resource it references",
        "preview control-plane changes before applying the deployment",
        "deploy the template at the intended boundary with understood replacement behavior",
        "change a declared resource and redeploy the updated desired state",
        "turn an exported JSON template into maintainable Bicep as a starting point",
        "modify a JSON deployment template without breaking its schema structure",
    ),
    "11": (
        "choose a regionally available Marketplace image reference",
        "attach the virtual machine to the intended subnet through its network interface",
        "encrypt supported host caches and temporary storage at the compute host",
        "keep durable workload data off the host-local scratch disk",
        "choose a managed disk tier that meets the workload's performance requirement",
        "add persistent capacity without replacing the operating-system disk",
        "confirm that the requested compute shape is offered in the deployment region",
        "change compute size when the destination cluster cannot resize the running machine in place",
        "end compute charges rather than only powering off inside the machine",
        "capture a point-in-time copy of a managed disk",
    ),
    "12": (
        "place instances in separate datacenter fault boundaries within one region",
        "spread virtual machines across fault and update domains in one datacenter",
        "manage individually configurable virtual machines as one scalable group",
        "make every instance follow one centrally maintained definition",
        "adjust instance count from a metric without manual intervention",
        "confirm regional SKU availability and subscription capacity before deployment",
        "relocate a supported virtual machine and its dependencies to another resource group",
        "relocate a supported virtual machine across subscription boundaries",
        "recreate supported workload resources in a different Azure region through an orchestrated move",
        "prove that the chosen placement model survives its intended failure boundary",
    ),
    "13": (
        "choose registry capabilities and throughput appropriate for the image workload",
        "deploy by digest so later tag changes cannot move the release",
        "let the runtime pull a private image without embedding an administrator password",
        "copy an existing image into the registry without a local pull and push",
        "run sidecars inside one jointly managed execution unit",
        "publish a stable regional name for the container group's public endpoint",
        "pass sensitive configuration without writing the clear value into ordinary output",
        "control whether a terminated container restarts",
        "request CPU and memory values supported in the selected region",
        "prefer an identity-scoped image pull over long-lived registry credentials",
    ),
    "14": (
        "place related apps inside one networking and logging boundary",
        "preserve an immutable snapshot whenever revision-scoped configuration changes",
        "move production to the newest ready version and retire the preceding active version",
        "keep several versions active at the same time",
        "send controlled percentages of requests to two active versions",
        "route ingress to the port on which the container process actually listens",
        "choose whether the application endpoint is externally reachable or environment-internal",
        "keep required warm capacity while setting an upper scale limit",
        "translate HTTP or event demand into a desired replica count",
        "reference sensitive configuration without placing the clear value in ordinary settings",
    ),
    "15": (
        "understand which web apps share workers and scale together",
        "select a hosting tier that supplies the required production capabilities",
        "increase worker CPU or memory without adding worker instances",
        "add worker instances without changing the worker size",
        "change instance count automatically when the selected signal crosses a threshold",
        "deploy a candidate release to a live URL that is separate from production",
        "prevent environment-only configuration from moving when slots exchange content",
        "validate swap behavior before the candidate becomes production",
        "create an application inside the intended existing hosting plan",
        "limit how many shared-plan workers one application may use",
    ),
    "16": (
        "reject inbound clients that negotiate a protocol below the approved TLS version",
        "redirect unencrypted application requests to HTTPS",
        "bind a supported platform-managed certificate to a custom hostname",
        "publish the record type required for the chosen custom hostname",
        "prove control of a hostname before binding it to the application",
        "write application backups to an authorized storage destination",
        "retain scheduled backups for the required recovery window",
        "send outbound application traffic into an approved regional virtual network",
        "give the application an inbound private address without making integration bidirectional",
        "allow inbound requests only from approved network sources",
    ),
    "17": (
        "connect networks without overlapping their address ranges",
        "reserve subnet ranges that do not collide with future network segments",
        "create both directional control-plane links required for connected networks",
        "let a spoke use a hub gateway only when both peering sides permit it",
        "carry forwarded packets from an NVA across connected networks",
        "use the production public-address SKU with secure defaults",
        "keep the assigned public address stable across resource restarts",
        "pin a public address to the intended availability-zone design",
        "make virtual machines use approved custom DNS resolvers",
        "avoid assuming that connectivity automatically crosses a second peering hop",
    ),
    "18": (
        "ensure the intended security rule is evaluated before a broader conflicting rule",
        "allow return packets for an established permitted flow without a mirror rule",
        "account for security filters applied at both subnet and network-interface scopes",
        "refer to application-role groups instead of fixed addresses in security rules",
        "see the combined security rules that actually apply to one interface",
        "select the most specific destination route before considering route origin",
        "override an applicable system path with an intentional custom route",
        "send traffic through a reachable forwarding appliance",
        "control whether learned gateway paths enter a subnet route table",
        "ask the platform which security rule allows or denies a specific flow",
    ),
    "19": (
        "keep service traffic on the Azure backbone while using the service's public endpoint",
        "authorize a selected subnet identity on a service firewall",
        "deny service requests from networks that are not explicitly selected",
        "assign a private address from the consumer network to a platform service connection",
        "resolve a service hostname to the connection's private address",
        "create the endpoint-to-name-resolution association automatically",
        "make private records resolvable from the intended virtual network",
        "disable the service's public network path after private connectivity works",
        "identify whether the provider accepted a pending private connection",
        "choose between subnet authorization to a public endpoint and a private network interface",
    ),
    "20": (
        "publish internet records by using Azure-hosted DNS authority",
        "make the parent domain direct queries to the Azure-hosted child zone",
        "publish multiple values with the same owner, type, and time-to-live",
        "point a zone-apex record at an Azure resource without hard-coding its address",
        "control how long a positive answer can remain in recursive caches",
        "control cache duration for a negative DNS lookup",
        "use the exact reserved subnet name required by the managed jump service",
        "allocate a subnet large enough for the managed jump service to scale",
        "attach the supported public address configuration to the managed jump host",
        "administer a private virtual machine without assigning it a public address",
    ),
    "21": (
        "expose one ingress IP for incoming balanced traffic",
        "register every serving network interface as an eligible target",
        "remove an instance from rotation when its application endpoint is unhealthy",
        "connect the ingress IP, eligible targets, health signal, protocol, and ports in one rule",
        "allow the platform probe source while keeping other unsolicited traffic denied",
        "provide explicit outbound connectivity for a Standard load-balanced backend",
        "keep successive flows from one client on the affinity mode the application expects",
        "explain why no new client flow is sent when every target fails its probe",
        "test reachability between two endpoints and return the responsible hop or policy",
        "measure connection reachability and latency continuously over time",
    ),
    "22": (
        "decide whether a measurement belongs in metrics or queryable events",
        "interpret a chart only after checking its aggregation and time grain",
        "send supported resource telemetry to an approved destination",
        "enable the service-specific log categories required by the query",
        "store and query records from several monitored resources in one boundary",
        "filter records and calculate a grouped summary with KQL",
        "allow for collection and processing delay before declaring telemetry missing",
        "use a curated service view backed by the required monitoring data",
        "bring continuous network-test telemetry into the monitoring workflow",
        "control retention and ingestion volume before monitoring cost grows unexpectedly",
    ),
    "23": (
        "evaluate a numeric signal against a threshold over a defined window",
        "attach an alert rule to the resource that emits the monitored signal",
        "connect an alert rule to reusable notification and automation actions",
        "route a fired alert to the intended email, webhook, or automation endpoint",
        "change delivery of matching notifications while leaving detection intact",
        "apply alert-routing behavior only during an approved maintenance window",
        "trigger on a matching Activity Log record",
        "keep an alert fired until the measured condition has resolved",
        "let the service learn a changing baseline instead of using one static threshold",
        "encode operational urgency independently of whether a rule fires",
    ),
    "24": (
        "store supported Azure VM protection metadata in the correct vault type",
        "use the vault type designed for newer data-source protection workloads",
        "define how often recovery points are created and how long they remain",
        "associate the intended protection schedule with the test workload",
        "create an extra recovery point before a risky maintenance window",
        "select a recovery point that meets the required recovery time",
        "recover selected files without replacing the complete virtual machine",
        "choose between creating a restored machine and restoring disks for controlled assembly",
        "hold erased recovery data temporarily so accidental removal can be reversed",
        "detect failed protection jobs and route them to operators",
    ),
    "25": (
        "replicate supported virtual-machine disks from one region to recovery resources in another",
        "place recovery orchestration outside the failure boundary it must survive",
        "configure retention plus the cadence for application-aware recovery points",
        "buffer replication changes in a supported source-region storage account",
        "connect recovered machines to the intended target network and subnet",
        "wait until initial synchronization completes and protection reports normal",
        "exercise recovery on an isolated network without disrupting production replication",
        "shut down the source and capture its latest changes for low-loss recovery",
        "start outage recovery from the most appropriate stored point",
        "finalize recovery, reverse protection direction, and return service to the original region",
    ),
}


CONCEPT_TOPICS = {
    "01": ("verified UPN suffixes", "cloud-only user creation", "user profile properties", "account enabled state", "security group creation", "group membership", "group ownership", "member and guest user types", "deleted-user recovery", "immutable directory object IDs"),
    "02": ("available license capacity", "usage location prerequisite", "direct license assignment", "group-based licensing", "B2B guest invitations", "guest redemption state", "guest lifecycle properties", "SSPR registration scope", "SSPR authentication methods", "SSPR licensing and role gates"),
    "03": ("role definitions and assignments", "Reader role", "Contributor role", "User Access Administrator role", "least-privilege role selection", "scope inheritance", "resource-level assignments", "group-based role assignment", "effective access interpretation", "deny assignments"),
    "04": ("resource group lifecycle", "subscription context", "management group hierarchy", "management group inheritance", "resource tags", "tag inheritance limitations", "CanNotDelete locks", "ReadOnly locks", "resource moves", "resource group location"),
    "05": ("policy definitions and assignments", "policy initiatives", "policy compliance evaluation", "deny policy effect", "modify and remediation", "budget behavior", "forecast budget alerts", "budget notification contacts", "Advisor cost recommendations", "governance scope and exclusions"),
    "06": ("StorageV2 accounts", "storage account naming", "locally redundant storage", "zone-redundant storage", "geo-redundant read access", "secure transfer required", "minimum TLS version", "shared key authorization", "access-key rotation", "storage service encryption"),
    "07": ("storage firewall default action", "storage IP network rules", "virtual-network service endpoints", "trusted Azure service bypass", "service and account SAS scope", "user delegation SAS", "SAS start and expiry time", "stored access policies", "stored-policy revocation", "account-key exposure"),
    "08": ("blob containers", "blob access tiers", "lifecycle rule filters", "lifecycle tier transitions", "lifecycle deletion", "blob soft delete", "container soft delete", "blob versioning", "object replication", "AzCopy copy and sync"),
    "09": ("file share quota", "SMB and NFS share protocols", "identity-based file authentication", "share-level Azure RBAC", "file and directory ACLs", "Azure Files network path", "file share snapshots", "file share soft delete", "AzCopy file transfers", "SMB port connectivity"),
    "10": ("declarative resource state", "Bicep parameters", "Bicep variables", "Bicep outputs", "symbolic dependencies", "deployment what-if", "deployment scope and mode", "modifying Bicep resources", "ARM-to-Bicep decompilation", "ARM template modification"),
    "11": ("virtual machine image selection", "network interface dependency", "encryption at host", "temporary disks", "managed disk performance tiers", "attaching data disks", "VM size availability", "resize deallocation", "stopped and deallocated states", "managed disk snapshots"),
    "12": ("availability zones", "availability sets", "flexible scale sets", "uniform scale sets", "VM scale-set autoscale", "regional size and quota checks", "resource-group VM moves", "cross-subscription VM moves", "cross-region VM movement", "resilience validation"),
    "13": ("container registry service tiers", "repository tags and digests", "registry pull authorization", "server-side image import", "container groups", "ACI DNS labels", "container environment secrets", "ACI restart policies", "ACI resource sizing", "registry credentials versus identity"),
    "14": ("Container Apps environments", "immutable revisions", "single revision mode", "multiple revision mode", "revision traffic splitting", "ingress target ports", "external and internal ingress", "minimum and maximum replicas", "event-driven scale rules", "Container Apps secrets"),
    "15": ("App Service plan boundaries", "App Service pricing tiers", "vertical plan scaling", "horizontal plan scaling", "App Service autoscale rules", "deployment slots", "slot-specific settings", "swap with preview", "web app creation", "per-app scaling"),
    "16": ("minimum inbound TLS", "HTTPS-only redirection", "App Service managed certificates", "custom-domain DNS records", "domain ownership verification", "App Service backup storage", "backup schedules and retention", "regional VNet integration", "App Service private endpoints", "App Service access restrictions"),
    "17": ("nonoverlapping address spaces", "subnet address planning", "bidirectional peering objects", "gateway transit peering", "forwarded traffic on peering", "Standard public IP SKU", "static public IP allocation", "zonal public IP configuration", "custom virtual-network DNS servers", "nontransitive peering"),
    "18": ("NSG rule priorities", "stateful NSG processing", "subnet and NIC NSGs", "application security groups", "effective security rules", "longest-prefix route selection", "user-defined route overrides", "virtual appliance next hops", "gateway route propagation", "IP flow verification"),
    "19": ("service endpoint traffic", "service endpoint authorization", "selected-network firewalls", "private endpoint network interfaces", "private endpoint DNS zones", "private DNS zone groups", "private DNS virtual-network links", "public network access", "private endpoint approval", "service endpoints versus private endpoints"),
    "20": ("public DNS zones", "DNS delegation", "DNS record sets", "Azure DNS alias records", "DNS TTL behavior", "DNS negative caching", "AzureBastionSubnet naming", "Bastion subnet sizing", "Bastion public IP", "private VM administration"),
    "21": ("load balancer frontends", "backend address pools", "health probes", "load-balancing rules", "health probe NSG traffic", "outbound connectivity", "session persistence", "all-backend probe failure", "connection troubleshoot", "Connection Monitor"),
    "22": ("metrics and logs", "metric aggregation and time grain", "diagnostic setting destinations", "resource-specific log categories", "Log Analytics workspaces", "KQL filtering and summarization", "log ingestion latency", "Azure Monitor Insights", "Connection Monitor telemetry", "monitoring retention and cost"),
    "23": ("metric alert conditions", "alert target scopes", "action group association", "action group receivers", "alert suppression rules", "scheduled alert processing", "activity log alerts", "stateful metric alerts", "dynamic thresholds", "alert severity"),
    "24": ("Recovery Services vaults", "Backup vaults", "backup frequency and retention", "policy association", "on-demand backups", "recovery-point selection", "file-level recovery", "VM restore choices", "backup soft delete", "backup monitoring and alerts"),
    "25": ("source and target regions", "Site Recovery vault placement", "replication policies", "cache storage accounts", "target network mapping", "replication health", "test failover isolation", "planned failover", "unplanned failover", "commit, reprotect, and failback"),
}


STEM_PATTERNS = {
    "behavior": (
        "{actor_article} {actor} is updating the {lens} runbook. The requirement is to {cue}. Which statement describes Azure behavior correctly?",
        "{lens_article} {lens} peer review asks how the {profile} should handle this outcome: {cue}. Which explanation is accurate?",
        "For the {profile}, the {lens} plan must {cue}. Which statement about {lens} belongs in the {profile} record?",
        "The {lens} review compares four claims for the {profile} requirement to {cue}. Which claim is technically sound?",
        "The {lens} architecture note requires the {profile} environment to {cue}. Which statement defines the relevant {lens} boundary?",
        "A new {lens} operator must explain why the {profile} can {cue}. Which explanation is accurate?",
        "The {profile} acceptance criteria require operators to {cue}. Which service fact supports that requirement?",
        "{lens_article} {lens} reviewer challenges whether the {profile} can {cue}. Which response resolves the concern?",
        "The {profile} handoff omits the {lens} rule needed to {cue}. Which statement should the team add?",
        "{lens_article} {lens} incident review of the {profile} depends on the ability to {cue}. Which platform description is reliable?",
    ),
    "implementation": (
        "{lens_article} {lens} ticket in the {profile} says to {cue}. Which {lens} action completes the {profile} request with minimal change?",
        "The approach for the {profile} is approved, but the {lens} environment still cannot {cue}. Which implementation step closes the gap?",
        "The {actor} may change the {profile} only to {cue}. Which {lens} action stays within that assignment?",
        "{lens_article} {lens} dry run shows no {profile} command will {cue}. Which action belongs before execution?",
        "For the {profile}, operators need to {cue}. Which change realizes that requirement?",
        "Operators must automate the {profile} change needed to {cue}. Which {lens} operation belongs in the runbook?",
        "{profile_article} {profile} review finds {lens} drift from the need to {cue}. Which correction addresses that drift?",
        "The {profile} window permits only the {lens} change needed to {cue}. Which option respects the boundary?",
        "The {lens} preflight has passed; the {profile} must now {cue}. Which operation should run?",
        "The {profile} plan must {cue} while limiting the mutation scope to {lens}. Which action is appropriate?",
    ),
    "validation": (
        "The {profile} setup reports success after the {lens} attempt to {cue}. Which {lens} read-only observation proves the {profile} outcome?",
        "The {lens} log says the {profile} can now {cue}. Which {lens} state should the {profile} acceptance test retain?",
        "The {profile} rejects {lens} exit status as proof it can {cue}. Which {profile} result is valid evidence?",
        "The {lens} validator needs one {profile} query after the change to {cue}. Which {lens} property should the {profile} validator inspect?",
        "The {actor} must confirm the {profile}, without mutation, can {cue}. Which {lens} check qualifies?",
        "The {profile} configuration is complete; the {lens} reviewers need evidence it can {cue}. Which observation shows success?",
        "The {lens} validation asks whether the {profile} can {cue}. Which observable state is strongest?",
        "{profile_article} {profile} review must prove the {lens} ability to {cue}. Which check avoids an adjacent feature?",
        "The {profile} evidence bundle needs {lens_article_lower} {lens} result showing it can {cue}. Which result belongs in the checkpoint?",
        "Before {profile} cleanup, the {lens} team must reconfirm it can {cue}. Which read-only inspection should run?",
    ),
    "diagnosis": (
        "During {lens_article_lower} {lens} fault drill, the {profile} does not {cue}. Which finding identifies the defect?",
        "The {profile} setup finishes, yet the {lens} cannot {cue}. Which misconfiguration explains the mismatch?",
        "{lens_article} {lens} break/fix in the {profile} fails when operators try to {cue}. Which diagnosis fits?",
        "The {profile} troubleshooting scope is the {lens} need to {cue}. Which condition should be corrected first?",
        "The {profile} result is partial because the {lens} cannot {cue}. Which condition accounts for that result?",
        "The {lens} evidence shows the {profile} cannot {cue}. Which root cause fits that evidence?",
        "Although the {profile} is meant to let the {lens} {cue}, its checkpoint fails. Which {lens} defect explains the failure?",
        "The {lens} support team isolated the {profile} incident to the attempt to {cue}. Which condition prevents success?",
        "{profile_article} {profile} query surprises the {actor} during the {lens} attempt to {cue}. Which finding explains it?",
        "Other {profile} components are healthy, but the {lens} still cannot {cue}. Which state causes the isolated failure?",
    ),
    "sequence": (
        "The {profile} runbook must {cue}, then retain {lens} read-back evidence. Which {profile} pair completes both duties?",
        "To satisfy the {lens} requirement, operators must change the {profile} configuration and prove it can {cue}. Which sequence is coherent?",
        "The {actor} needs a safe {profile} change to {cue}, followed by {lens} evidence. Which pair merits approval?",
        "The {profile} has two {lens} gates: {cue}, then prove the {profile} state. Which {lens} sequence works?",
        "Which {lens} path makes the {profile} able to {cue}, then inspects the defining properties?",
        "At the {profile} approval gate, operators must show that the {lens} can {cue}. Which {lens} configure-and-check pair is defensible?",
        "The {profile} forbids a partial {lens} result. Operators must first {cue} and afterward confirm the {profile} outcome. Which {lens} sequence is complete?",
        "Only the {profile} change needed to {cue} is allowed, and {lens} proof is mandatory. Which pair fits?",
        "The {profile} runbook separates {lens} mutation from validation while it must {cue}. Which sequence proves it cleanly?",
        "The {profile} checkpoint requires both this {lens} outcome—{cue}—and a read-only {profile} state check. Which {lens} response is complete?",
    ),
}


KNOWN_CANNED = (
    "real but separate behavior",
    "documented service behavior",
    "leaving the required",
    "queried state directly exposes",
    "condition directly breaks",
    "pair implements and checks",
    "first step establishes",
)


def normalize(value: str) -> str:
    return " ".join(WORD_RE.findall(str(value).casefold()))


def indefinite_article(value: str) -> str:
    """Return the English indefinite article for the generated noun phrase."""

    token_match = re.search(r"[A-Za-z]+", value)
    if not token_match:
        return "A"
    token = token_match.group(0)
    lowered = token.casefold()
    if token.isupper() and token[0] in "AEFHILMNORSX":
        return "An"
    if lowered.startswith(("honest", "hour", "heir")):
        return "An"
    if lowered.startswith(("user", "use", "uni", "euro", "one")):
        return "A"
    return "An" if lowered[0] in "aeio" else "A"


def stage_for(index: int) -> str:
    if index <= 10:
        return "behavior"
    if index <= 20:
        return "implementation"
    if index <= 30:
        return "validation"
    if index <= 40:
        return "diagnosis"
    return "sequence"


def target_from_rationale(stage: str, rationale: str) -> str:
    patterns = {
        "behavior": r"documented service behavior for (.*?);",
        "implementation": r"required implementation step for (.*?);",
        "validation": r"directly exposes (.*?), providing",
        "diagnosis": r"directly breaks (.*?) and matches",
        "sequence": r"first step establishes (.*?), and the second",
    }
    match = re.search(patterns[stage], rationale, flags=re.IGNORECASE)
    if not match:
        match = re.search(
            {
                "behavior": r"^(?:For (.*?):|For (.*?), this claim|The governing statement for (.*?) is|The (.*?) statement|Under (.*?),|This option frames (.*?) as follows|Its (?:concrete )?(.*?) \brule\b|(.*?) is described by|(.*?) appears in this claim|The (.*?) rule is)",
                "implementation": r"^(?:For (.*?), execute|For (.*?), the proposed operation|The (.*?) action is|The (.*?) (?:change|operation)|Applied as written to (.*?),|This option applies to (.*?) by|Its (?:concrete effect on )?(.*?) (?:mutation|would)|(.*?) changes through)",
                "validation": r"^(?:For (.*?), inspect|For (.*?), the proposed check|The (.*?) check is|The (.*?) (?:inspection|evidence)|Run against (.*?),|This option observes (.*?) by|Its (?:concrete )?(.*?) (?:evidence|observation)|(.*?) evidence comes from|To observe (.*?),)",
                "diagnosis": r"^(?:For (.*?), investigate|For (.*?), the reported condition|The (.*?) (?:fault|failure described)|Observed under (.*?),|This option attributes (.*?) to|Its (?:concrete impact on )?(.*?) (?:fault|is)|(.*?) fails when|(.*?) is attributed to|The (.*?) fault is)",
                "sequence": r"^(?:For (.*?), use|For (.*?), this .*? pair|The (.*?) path is|The (.*?) sequence|Taken in order for (.*?),|This option pairs (.*?) with|Its (?:concrete )?(.*?) (?:runbook|path)|(.*?) follows this sequence|To complete (.*?),)",
            }[stage],
            rationale,
            flags=re.IGNORECASE,
        )
        if match:
            return next(group.strip() for group in match.groups() if group)
        raise ValueError(f"Cannot recover target from rationale: {rationale}")
    return match.group(1).strip()


def option_topic_from_rationale(stage: str, rationale: str, correct: bool, target: str) -> str:
    if correct:
        return target
    patterns = {
        "behavior": r"^(.*?) is a real but separate behavior;",
        "implementation": r"^This changes (.*?), leaving the required",
        "validation": r"^This reads evidence for (.*?) rather than proving",
        "diagnosis": r"^This would explain a failure of (.*?), not the failed",
        "sequence": r"^The pair implements and checks (.*?) instead of the required",
    }
    match = re.search(patterns[stage], rationale, flags=re.IGNORECASE)
    if not match:
        return target_from_rationale(stage, rationale)
    return match.group(1).strip()


def clean_topic(value: str) -> str:
    """Strip prose accidentally captured after an authored topic label."""
    markers = (
        " action is:",
        " mutation is:",
        " changes through:",
        " can use this for ",
        " can approve this for ",
        " performs the ",
        " appears in the ",
        " criteria concern ",
        " boundary stays ",
    )
    lowered = value.casefold()
    cut = len(value)
    for marker in markers:
        position = lowered.find(marker)
        if position >= 0:
            cut = min(cut, position)
    return value[:cut].strip().rstrip(";:,. ")


def normalize_topic_label(value: str) -> str:
    """Use sentence-friendly case without lowercasing product names or acronyms."""
    value = clean_topic(value)
    proper_prefixes = (
        "ACI", "ARM", "App Service", "AzCopy", "Azure", "AzureBastionSubnet",
        "B2B", "Bicep", "CanNotDelete", "Container Apps", "Contributor",
        "DNS", "Geo-", "HTTPS", "IP", "KQL", "Log Analytics", "Microsoft",
        "NSG", "NFS", "Reader", "SAS", "SMB", "Site Recovery", "StorageV2",
        "TLS", "User Access Administrator", "VM",
    )
    if value.startswith(proper_prefixes):
        return value
    return value[0].lower() + value[1:] if value else value


def actor_from_metadata(metadata: dict) -> str:
    role = str(metadata["experience"]["role"]).strip().rstrip(".")
    role = re.sub(r"^(?:an?|the)\s+", "", role, flags=re.IGNORECASE)
    return role


def uncap(value: str) -> str:
    value = value.strip().rstrip(".")
    if value.startswith(("Azure ", "Azure-", "Microsoft ")):
        return value
    for prefix in ("A ", "An ", "The "):
        if value.startswith(prefix):
            return prefix.casefold() + value[len(prefix) :]
    if value and value[0].isalpha() and not value[:2].isupper():
        return value[0].lower() + value[1:]
    return value


def technical_effect(stage: str, option: str, topic: str, variant: int) -> str:
    detail = uncap(option)
    topic_display = topic[0].upper() + topic[1:] if topic else topic
    patterns = {
        "behavior": (
            "For {topic}: {detail}.",
            "{Topic} is described by: {detail}.",
            "This claim concerns {topic}: {detail}.",
            "Rule governing {topic}: {detail}.",
        ),
        "implementation": (
            "For {topic}, execute: {detail}.",
            "{Topic} changes through: {detail}.",
            "The {topic} action is: {detail}.",
            "Its {topic} mutation is: {detail}.",
        ),
        "validation": (
            "For {topic}, inspect: {detail}.",
            "For evidence about {topic}: {detail}.",
            "To observe {topic}, use: {detail}.",
            "The {topic} check is: {detail}.",
        ),
        "diagnosis": (
            "For {topic}, investigate: {detail}.",
            "Failure in {topic} occurs when: {detail}.",
            "This finding concerns {topic}: {detail}.",
            "The {topic} fault is: {detail}.",
        ),
        "sequence": (
            "For {topic}, use: {detail}.",
            "This sequence serves {topic}: {detail}.",
            "To complete {topic}, use: {detail}.",
            "The {topic} path is: {detail}.",
        ),
    }
    return patterns[stage][variant % len(patterns[stage])].format(
        topic=topic,
        Topic=topic_display,
        detail=detail,
    )


def rationale(
    *,
    stage: str,
    option: str,
    option_topic: str,
    target: str,
    cue: str,
    profile: str,
    correct_option: str,
    correct: bool,
    question_index: int,
    letter_index: int,
) -> str:
    claim = option.strip().rstrip(".") + "."
    if correct:
        conclusions = {
            "behavior": (
                "{Claim} In the {profile}, this {target} rule supports the need to {cue}.",
                "For the {profile}, the rule for {target} is defined by this statement: {claim} It supports the required outcome to {cue}.",
                "{Claim} The {profile} applies that {target} boundary when operators must {cue}.",
                "The {profile} needs {target} to {cue}; this option states the applicable {target} rule: {claim}",
                "{Claim} This {target} fact resolves the {profile} design question about how to {cue}.",
                "{Claim} For {profile}, {target} supplies the service rule needed to {cue}.",
            ),
            "implementation": (
                "{Claim} The {profile} uses this {target} operation to {cue} within the approved scope.",
                "For the {profile}, the required {target} action is: {claim} It makes the environment able to {cue}.",
                "{Claim} This changes {target} in the {profile}, supplying the missing state needed to {cue}.",
                "The {profile} must {cue}; this option performs its direct {target} change: {claim}",
                "{Claim} It is the least-change {target} path for the {profile} requirement to {cue}.",
                "{Claim} In {profile}, applying {target} is the scoped way to {cue}.",
            ),
            "validation": (
                "{Claim} The {profile} reads {target} directly; that {target} result proves the {profile} can {cue} without another mutation.",
                "For the {profile}, this {target} observation is decisive: {claim} It is {profile} evidence that operators can {cue}.",
                "{Claim} Because the {profile} check observes {target}, it independently verifies the requirement to {cue}.",
                "The {profile} validator needs this {target} result: {claim} It proves the outcome to {cue} rather than an adjacent checkpoint.",
                "{Claim} This is independent {target} evidence for the {profile}, even if {profile} setup reports success before {target} becomes observable.",
                "{Claim} For {profile}, this {target} read confirms the service can {cue}.",
            ),
            "diagnosis": (
                "{Claim} This {profile} condition breaks {target}, explaining why operators cannot {cue}.",
                "For the {profile}, the {target} failure is causal: {claim} Correcting it restores the ability to {cue}.",
                "{Claim} The finding is specific to {target} in the {profile}; repairing {target} restores the {profile} ability to {cue}.",
                "The {profile} cannot {cue} because of this {target} defect: {claim} The symptom and repair align.",
                "{Claim} Removing this {target} condition lets the {profile} {cue} while leaving healthy controls unchanged.",
                "{Claim} In {profile}, this {target} cause matches the failure to {cue}.",
            ),
            "sequence": (
                "{Claim} In the {profile}, the first {target} step runs; the {profile} then reads {target} state to prove it can {cue}.",
                "For the {profile}, the safe {target} order is: {claim} The {profile} records {target} proof after configuration.",
                "{Claim} The {profile} uses its {target} mutation gate and {target} verification gate before it can {cue}.",
                "The {profile} gets a complete {target} sequence here: {claim} Read-back evidence follows the change.",
                "{Claim} This ordered {target} workflow lets the {profile} {cue} and then verify the resulting state.",
                "{Claim} For {profile}, the {target} operation precedes its {target} read-back check, allowing it to {cue}.",
            ),
        }
        variant_seed = question_index + sum(ord(character) for character in profile)
        ending = conclusions[stage][variant_seed % len(conclusions[stage])]
        return ending.format(
            Claim=claim[0].upper() + claim[1:],
            claim=claim[0].lower() + claim[1:] if not claim.startswith(("Azure", "Microsoft")) else claim,
            profile=profile,
            target=target,
            cue=cue,
        )

    intro_templates = {
        "behavior": "{Claim} In the {profile}, this statement describes {option_topic}.",
        "implementation": "{Claim} In the {profile}, this action changes {option_topic}.",
        "validation": "{Claim} In the {profile}, this check observes {option_topic}.",
        "diagnosis": "{Claim} The {profile} fault concerns {option_topic}.",
        "sequence": "{Claim} This {profile} pair serves {option_topic}.",
    }
    endings = {
        "behavior": (
            "{Target} governs {profile}; {option_topic} cannot support {target} when operators must {cue}.",
            "{Profile} asks about {target}; this {option_topic} choice leaves the {target} explanation missing.",
            "The {option_topic} statement accurately describes {option_topic}; however, {profile} needs {target} to {cue}; {option_topic} cannot replace {target}.",
            "Selecting {option_topic} for {profile} leaves {target} unanswered in {profile}; the {profile} lacks a {target} basis to {cue}.",
        ),
        "implementation": (
            "{Profile} requires {target}; changing {option_topic} leaves {target} absent in {profile}; {profile} cannot {cue}.",
            "{Option_topic} does not implement {target} for {profile}; the {profile} still cannot {cue}.",
            "{Profile} instead needs {target}: {correct}. The {option_topic} action omits that {target} work.",
            "{Profile} approved {target}, not {option_topic}; only the {target} change can {cue}.",
        ),
        "validation": (
            "{Profile} could pass {option_topic} while {target} is wrong; {profile} still lacks {target} proof.",
            "{Profile} output covers {option_topic}, not {target}; the {target} requirement to {cue} remains unverified.",
            "{Option_topic} success in {profile} cannot verify {target}; {profile} cannot {cue} until {target} evidence exists.",
            "{Profile} reads {option_topic}, leaving {target} unproved in {profile}; {profile} still has no {target} proof.",
        ),
        "diagnosis": (
            "{Profile} could repair {option_topic} while {target} stays broken in {profile}; the {profile} remains unable to {cue}.",
            "{Profile} failed on {target}; this {option_topic} finding redirects {profile} remediation away from {target}.",
            "{Profile} may fix {option_topic}, yet {target} still fails; this {profile} diagnosis of {option_topic} is wrong for {target}.",
            "{Profile} has {option_topic} impact, but {target} is the {profile} failed path; the {option_topic} state cannot produce {target} failure.",
        ),
        "sequence": (
            "{Profile} closes {option_topic}, not {target}; without the {target} workflow, it cannot {cue}.",
            "{Option_topic} cannot replace {target} in {profile}. Use this {target} pair instead: {correct}.",
            "{Profile} proves {option_topic}, but {target} lacks implementation in {profile} and {target} proof; the {target} outcome to {cue} remains open.",
            "{Profile} uses {option_topic} for both steps; {target} remains untouched in {profile}, so its {target} gate to {cue} fails.",
        ),
    }
    intro = intro_templates[stage].format(
        Claim=claim,
        option_topic=option_topic,
        profile=profile,
    )
    ending = endings[stage][(question_index + letter_index) % len(endings[stage])].format(
        target=target,
        option_topic=option_topic,
        Target=target[0].upper() + target[1:] if target else target,
        profile=profile,
        Profile=profile[0].upper() + profile[1:] if profile else profile,
        Option_topic=option_topic[0].upper() + option_topic[1:] if option_topic else option_topic,
        cue=cue,
        correct=correct_option.strip().rstrip("."),
    )
    return f"{intro} {ending}"


def rewritten_questions(lab_dir: Path) -> tuple[list[dict], dict[str, dict]]:
    questions = yaml.safe_load((lab_dir / "assessment" / "questions.yml").read_text(encoding="utf-8"))
    metadata = yaml.safe_load((lab_dir / "lab.yml").read_text(encoding="utf-8"))
    number = lab_dir.name[:2]
    profile = PROFILES[number]
    lens = LENSES[number]
    actor = actor_from_metadata(metadata)
    replacements: dict[str, dict] = {}

    topics = list(CONCEPT_TOPICS[number])
    cues = CONCEPT_CUES[number]
    if len(cues) != 10:
        raise ValueError(f"Lab {number} must define exactly ten concept cues")

    option_topics: dict[str, dict[str, str]] = {}
    for stage_offset, stage in enumerate(("behavior", "implementation", "validation", "diagnosis", "sequence")):
        stage_map: dict[str, str] = {}
        for topic_offset, topic in enumerate(topics):
            stage_question = questions[stage_offset * 10 + topic_offset]
            correct_text = stage_question["options"][stage_question["correctOption"]]
            stage_map[normalize(correct_text)] = topic
        option_topics[stage] = stage_map

    for index, question in enumerate(questions, start=1):
        stage = stage_for(index)
        correct = question["correctOption"]
        old_explanations = question["optionExplanations"]
        target = topics[(index - 1) % 10]
        cue = cues[(index - 1) % 10]
        # Rotate the prose pattern independently of the concept position so the
        # same ordinal question does not announce the same sentence template
        # in every lab.
        pattern_offset = ((index - 1) + (int(number) - 1) * 3) % 10
        pattern = STEM_PATTERNS[stage][pattern_offset]
        new_stem = pattern.format(
            profile=profile,
            lens=lens,
            actor=actor,
            profile_article=indefinite_article(profile),
            lens_article=indefinite_article(lens),
            lens_article_lower=indefinite_article(lens).casefold(),
            actor_article=indefinite_article(actor),
            target=target,
            cue=cue,
        )
        new_explanations = {}
        correct_option = question["options"][correct]
        for letter_index, letter in enumerate(LETTERS):
            option_topic = option_topics[stage].get(normalize(question["options"][letter]))
            if not option_topic:
                option_topic = option_topic_from_rationale(
                    stage,
                    old_explanations[letter],
                    letter == correct,
                    target,
                )
            new_explanations[letter] = rationale(
                stage=stage,
                option=question["options"][letter],
                option_topic=option_topic,
                target=target,
                cue=cue,
                profile=profile,
                correct_option=correct_option,
                correct=letter == correct,
                question_index=index,
                letter_index=letter_index,
            )
        question["stem"] = new_stem
        question["optionExplanations"] = new_explanations
        question["sources"] = [expected_source(number, index)]
        replacements[question["id"]] = {
            "stem": new_stem,
            "optionExplanations": new_explanations,
            "sources": question["sources"],
        }
    return questions, replacements


def replace_authored_scalars(path: Path, replacements: dict[str, dict]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    current_id = None
    in_explanations = False
    skipping_sources = False
    output: list[str] = []
    for line in lines:
        if skipping_sources:
            if line.startswith("  lastVerified:"):
                skipping_sources = False
                output.append(line)
            continue
        id_match = re.match(r'^- id: ["\']?([^"\']+)["\']?$', line)
        if id_match:
            current_id = id_match.group(1)
            in_explanations = False
        elif line == "  optionExplanations:":
            in_explanations = True
        elif re.match(r"^  [A-Za-z]", line) and not line.startswith("    "):
            in_explanations = False

        if current_id in replacements and line.startswith("  stem:"):
            line = "  stem: " + json.dumps(replacements[current_id]["stem"], ensure_ascii=False)
        elif current_id in replacements and in_explanations:
            option_match = re.match(r"^    ([A-D]):", line)
            if option_match:
                letter = option_match.group(1)
                line = f"    {letter}: " + json.dumps(
                    replacements[current_id]["optionExplanations"][letter],
                    ensure_ascii=False,
                )
        elif current_id in replacements and line == "  sources:":
            output.append(line)
            for source in replacements[current_id]["sources"]:
                output.append("    - title: " + json.dumps(source["title"], ensure_ascii=False))
                output.append("      url: " + json.dumps(source["url"], ensure_ascii=False))
            skipping_sources = True
            continue
        output.append(line)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(output) + "\n")


def load_bank() -> list[tuple[str, dict]]:
    bank = []
    for lab_dir in sorted((ROOT / "labs").iterdir()):
        if not lab_dir.is_dir() or not lab_dir.name[:2].isdigit():
            continue
        number = int(lab_dir.name[:2])
        if not 1 <= number <= 25:
            continue
        questions = yaml.safe_load((lab_dir / "assessment" / "questions.yml").read_text(encoding="utf-8"))
        bank.extend((lab_dir.name, question) for question in questions)
    return bank


def repetition_metrics() -> dict:
    bank = load_bank()
    prefix_locations: dict[tuple[str, ...], list[tuple[str, str]]] = defaultdict(list)
    stem_grams: dict[tuple[str, ...], list[tuple[str, str]]] = defaultdict(list)
    rationale_grams: dict[tuple[str, ...], list[tuple[str, str]]] = defaultdict(list)
    rationale_four_grams: dict[tuple[str, ...], list[tuple[str, str]]] = defaultdict(list)
    canned = Counter()
    for lab_name, question in bank:
        words = normalize(question["stem"]).split()
        prefix_locations[tuple(words[:6])].append((lab_name, question["id"]))
        for offset in range(max(0, len(words) - 6)):
            stem_grams[tuple(words[offset : offset + 7])].append((lab_name, question["id"]))
        for letter, explanation in question["optionExplanations"].items():
            normalized = normalize(explanation)
            for phrase in KNOWN_CANNED:
                if normalize(phrase) in normalized:
                    canned[phrase] += 1
            rationale_words = normalized.split()
            for offset in range(max(0, len(rationale_words) - 6)):
                rationale_grams[tuple(rationale_words[offset : offset + 7])].append(
                    (lab_name, f"{question['id']}/{letter}")
                )
            for offset in range(max(0, len(rationale_words) - 3)):
                rationale_four_grams[tuple(rationale_words[offset : offset + 4])].append(
                    (lab_name, f"{question['id']}/{letter}")
                )
    repeated_prefixes = {
        key: values
        for key, values in prefix_locations.items()
        if len({lab for lab, _ in values}) > 1
    }
    repeated_rationale_grams = {
        key: values
        for key, values in rationale_grams.items()
        if len(values) >= 12 and len({lab for lab, _ in values}) >= 3
    }
    repeated_rationale_four_grams = {
        key: values
        for key, values in rationale_four_grams.items()
        if len(values) >= 50 and len({lab for lab, _ in values}) >= 5
    }
    repeated_stem_grams = {
        key: values
        for key, values in stem_grams.items()
        if len(values) >= 10 and len({lab for lab, _ in values}) >= 5
    }
    top_gram_count = max((len(values) for values in repeated_rationale_grams.values()), default=0)
    top_prefixes = sorted(repeated_prefixes.items(), key=lambda item: (-len(item[1]), item[0]))[:12]
    top_grams = sorted(repeated_rationale_grams.items(), key=lambda item: (-len(item[1]), item[0]))[:20]
    top_four_grams = sorted(
        repeated_rationale_four_grams.items(), key=lambda item: (-len(item[1]), item[0])
    )[:40]
    top_stem_grams = sorted(repeated_stem_grams.items(), key=lambda item: (-len(item[1]), item[0]))[:50]
    return {
        "questionCount": len(bank),
        "crossLabRepeatedSixWordPrefixes": len(repeated_prefixes),
        "questionsWithRepeatedSixWordPrefix": sum(len(values) for values in repeated_prefixes.values()),
        "crossLabSevenWordStemGramsAtLeast10": len(repeated_stem_grams),
        "maximumCrossLabSevenWordStemGramFrequency": max(
            (len(values) for values in repeated_stem_grams.values()), default=0
        ),
        "knownCannedPhraseOccurrences": dict(canned),
        "crossLabSevenWordRationaleGramsAtLeast12": len(repeated_rationale_grams),
        "maximumCrossLabSevenWordRationaleGramFrequency": top_gram_count,
        "crossLabFourWordRationaleGramsAtLeast50": len(repeated_rationale_four_grams),
        "maximumCrossLabFourWordRationaleGramFrequency": max(
            (len(values) for values in repeated_rationale_four_grams.values()), default=0
        ),
        "topRepeatedPrefixes": [
            {"phrase": " ".join(key), "count": len(values)} for key, values in top_prefixes
        ],
        "topRepeatedStemGrams": [
            {"phrase": " ".join(key), "count": len(values)} for key, values in top_stem_grams
        ],
        "topRepeatedRationaleGrams": [
            {"phrase": " ".join(key), "count": len(values)} for key, values in top_grams
        ],
        "topRepeatedFourWordRationaleGrams": [
            {"phrase": " ".join(key), "count": len(values)} for key, values in top_four_grams
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rewrite", action="store_true", help="Rewrite the authoritative YAML files")
    parser.add_argument("--labs", nargs="*", help="Optional two-digit lab numbers to rewrite")
    parser.add_argument("--quiet", action="store_true", help="Suppress repetition reports during batched migration")
    args = parser.parse_args()

    if not args.quiet:
        print(json.dumps(repetition_metrics(), indent=2))
    if not args.rewrite:
        return 0
    for lab_dir in sorted((ROOT / "labs").iterdir()):
        if not lab_dir.is_dir() or not lab_dir.name[:2].isdigit():
            continue
        number = int(lab_dir.name[:2])
        if not 1 <= number <= 25:
            continue
        if args.labs and lab_dir.name[:2] not in set(args.labs):
            continue
        _, replacements = rewritten_questions(lab_dir)
        path = lab_dir / "assessment" / "questions.yml"
        replace_authored_scalars(path, replacements)
        print(f"WRITE {path.relative_to(ROOT)}")
    if not args.quiet:
        print(json.dumps(repetition_metrics(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
