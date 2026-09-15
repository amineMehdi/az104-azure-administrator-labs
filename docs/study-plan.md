# AZ-104 foundation-first study plan

This plan starts with the missing systems and networking foundations instead of
opening the numbered labs immediately. The goal is to replace answer-guessing
with a model that explains the resource relationships, traffic paths, scopes,
and failure modes. The repository's official objective baseline is documented
in [the AZ-104 blueprint](research/az-104-blueprint.md).

## Learner starting checkpoint

- **Strength:** development concepts, programming, APIs, and automation.
- **Partial:** understands terms such as VNet and subnet, but cannot yet design
  and build a small Azure network from a blank page.
- **Main gaps:** operating-system and systems-administration fundamentals,
  routing, DNS, traffic flow, network security, and the glue between Azure
  resources.
- **Risk to correct:** sometimes selects the right exam answer by guessing or
  elimination without being able to explain why.
- **Secondary goal:** learn Bash well enough to rewrite the repository's
  PowerShell-hosted Azure CLI exercises after the concepts and original lab
  behavior are understood.
- **Current status:** foundation phase; numbered labs are intentionally
  deferred.

## Learning sequence

| Phase | Focus | Exit evidence |
|---|---|---|
| 1 | Systems and Bash basics: processes, files, permissions, services, logs, exit codes, quoting, pipes, and variables | Explain a small system's state and safely compose/read commands without guessing shell behavior |
| 2 | Network primitives: IPv4/CIDR, subnetting, interfaces, gateways, routes, DNS, ports, TCP/UDP, TLS, NAT, and firewalls | Trace a request from a client to a service and distinguish route failure, DNS failure, and policy denial |
| 3 | Azure's substrate: tenant, subscription, resource group, resource IDs, regions/zones, ARM, RBAC, policy, locks, quotas, and cost | Explain where a resource lives, who can change it, and which plane/scope evaluates a request |
| 4 | Azure networking: VNets, subnets, NICs, IPs, routes, NSGs/ASGs, peering, service/private endpoints, private DNS, Bastion, load balancing, and Network Watcher | Design and explain a small network from scratch, including one allowed path and one intentional denial |
| 5 | Cross-service glue: compute, storage, App Service/containers, identity, monitoring, and recovery | Choose resources from requirements and trace identity, data, network, and telemetry paths end to end |
| 6 | Exam mapping and labs 00–27 | Complete labs because the design is understood, not because a recipe was copied |
| 7 | Bash rewrite lane | Reproduce the lab's safety, validation, break/fix, and cleanup behavior in Bash without translating syntax blindly |

## Teaching loop

For each topic: state the operational problem, build the mental model, connect
the resources, trace the end-to-end flow, compare the nearest alternatives,
perform a tiny reversible proof, and answer a retrieval question from memory.
Do not count a concept as learned until it can be explained and rebuilt from a
blank page.

## Immediate next step

Start with the smallest network story: a process listening on a port, a client
trying to reach it, name resolution, a route, and a firewall decision. Then map
each piece to an Azure VM/NIC, subnet, route, NSG, and DNS path. No Azure lab is
needed for this first lesson.

## Readiness gate before labs

Begin the numbered labs only when the learner can, without a recipe:

1. choose non-overlapping CIDRs and explain subnet boundaries;
2. draw the path from a client to a service and identify DNS, route, and policy
   decision points;
3. explain where a VNet, subnet, NIC, route table, NSG, public/private IP, and
   private endpoint attach and what each contributes;
4. diagnose a deliberately broken path as name-resolution, routing, or
   authorization failure; and
5. write and safely inspect a short Bash/Azure CLI command sequence.

Until then, use diagrams, local commands, read-only Azure CLI queries, and
small thought experiments rather than full resource deployments.
