# Learning pathways

Each path uses the same authoritative labs. The difference is sequencing and
depth. Mark a lab complete only after deployment validation and post-cleanup
validation both pass.

## Quick start

Use this route to learn the repository workflow and sample every major domain.

1. [Lab 00](../../labs/00-safe-bootstrap/README.md) — safe bootstrap and
   context selection.
2. [Lab 01](../../labs/01-entra-users-groups/README.md) — Microsoft Entra users
   and groups.
3. [Lab 06](../../labs/06-storage-accounts-security/README.md) — storage account
   security.
4. [Lab 10](../../labs/10-arm-bicep-lifecycle/README.md) — Bicep deployment
   lifecycle.
5. [Lab 17](../../labs/17-vnet-subnets-peering-public-ip/README.md) — virtual networks,
   subnets, peering, and public IPs.
6. [Lab 22](../../labs/22-azure-monitor-logs-insights/README.md) — Azure Monitor,
   logs, and insights.
7. [Lab 26](../../labs/26-capstone-build/README.md) — governed workload
   build capstone.

## Full exam preparation

Complete Labs 00–25 in numerical order, using each lab assessment as a review
gate. After each lab:

- score 85–100%: record mastery and continue;
- score 70–84%: repeat the mapped checkpoints for missed questions;
- score below 70%: repeat the lab's guided tasks before retesting.

Finish with both capstones, then use the
[objective map](../objective-map.md) to identify any objective without a
recent successful checkpoint.

## Job-ready path

Complete the full exam path, but add the operational challenge in every lab.
For each checkpoint, be able to explain:

- why the resource or setting exists;
- which identity and scope authorize the change;
- what independent query proves the expected state;
- what failure looks like and how to diagnose it;
- what must be deleted first and what may remain soft-deleted.

Repeat Capstone 26 from an empty state, then perform Capstone 27 without reading
the solution notes until your first diagnostic pass is complete.

## Suggested pace

Plan two focused sessions per week: one build-and-validate session and one
break/fix, cleanup, and assessment session. The repository's
[eight-week study plan](../study-plan.md) provides a domain-by-domain
schedule.
