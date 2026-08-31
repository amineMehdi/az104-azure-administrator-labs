# Lab 14 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB14-Q01 — C

**Question:** A revision rollout incident review of the revisioned serverless container release depends on the ability to place related apps inside one networking and logging boundary. Which platform description is reliable?

- **A — Incorrect.** A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision.
  A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision. In the revisioned serverless container release, this statement describes immutable revisions. Revisioned serverless container release asks about Container Apps environments; this immutable revisions choice leaves the Container Apps environments explanation missing.
- **B — Incorrect.** Traffic weights route percentages to revisions or labels and must total 100 percent.
  Traffic weights route percentages to revisions or labels and must total 100 percent. In the revisioned serverless container release, this statement describes revision traffic splitting. The revision traffic splitting statement accurately describes revision traffic splitting; however, revisioned serverless container release needs Container Apps environments to place related apps inside one networking and logging boundary; revision traffic splitting cannot replace Container Apps environments.
- **C — Correct.** A Container Apps environment is the secure boundary for apps that share networking and logging integration.
  For the revisioned serverless container release, the rule for Container Apps environments is defined by this statement: a Container Apps environment is the secure boundary for apps that share networking and logging integration. It supports the required outcome to place related apps inside one networking and logging boundary.
- **D — Incorrect.** Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale.
  Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale. In the revisioned serverless container release, this statement describes minimum and maximum replicas. Container Apps environments governs revisioned serverless container release; minimum and maximum replicas cannot support Container Apps environments when operators must place related apps inside one networking and logging boundary.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps environments](https://learn.microsoft.com/en-us/azure/container-apps/environment)

**Source reviewed:** 2026-08-31

## LAB14-Q02 — A

**Question:** A platform administrator releasing a revisioned serverless container app is updating the revision rollout runbook. The requirement is to preserve an immutable snapshot whenever revision-scoped configuration changes. Which statement describes Azure behavior correctly?

- **A — Correct.** A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision.
  A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision. The revisioned serverless container release applies that immutable revisions boundary when operators must preserve an immutable snapshot whenever revision-scoped configuration changes.
- **B — Incorrect.** Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.
  Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update. In the revisioned serverless container release, this statement describes single revision mode. Selecting single revision mode for revisioned serverless container release leaves immutable revisions unanswered in revisioned serverless container release; the revisioned serverless container release lacks a immutable revisions basis to preserve an immutable snapshot whenever revision-scoped configuration changes.
- **C — Incorrect.** The ingress target port must match the port on which the container process listens.
  The ingress target port must match the port on which the container process listens. In the revisioned serverless container release, this statement describes ingress target ports. Immutable revisions governs revisioned serverless container release; ingress target ports cannot support immutable revisions when operators must preserve an immutable snapshot whenever revision-scoped configuration changes.
- **D — Incorrect.** Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.
  Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts. In the revisioned serverless container release, this statement describes event-driven scale rules. Revisioned serverless container release asks about immutable revisions; this event-driven scale rules choice leaves the immutable revisions explanation missing.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q03 — C

**Question:** A revision rollout peer review asks how the revisioned serverless container release should handle this outcome: move production to the newest ready version and retire the preceding active version. Which explanation is accurate?

- **A — Incorrect.** Multiple revision mode can keep several revisions active and divide traffic between them.
  Multiple revision mode can keep several revisions active and divide traffic between them. In the revisioned serverless container release, this statement describes multiple revision mode. Selecting multiple revision mode for revisioned serverless container release leaves single revision mode unanswered in revisioned serverless container release; the revisioned serverless container release lacks a single revision mode basis to move production to the newest ready version and retire the preceding active version.
- **B — Incorrect.** External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path.
  External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path. In the revisioned serverless container release, this statement describes external and internal ingress. Single revision mode governs revisioned serverless container release; external and internal ingress cannot support single revision mode when operators must move production to the newest ready version and retire the preceding active version.
- **C — Correct.** Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.
  The revisioned serverless container release needs single revision mode to move production to the newest ready version and retire the preceding active version; this option states the applicable single revision mode rule: single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.
- **D — Incorrect.** Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image.
  Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image. In the revisioned serverless container release, this statement describes Container Apps secrets. The Container Apps secrets statement accurately describes Container Apps secrets; however, revisioned serverless container release needs single revision mode to move production to the newest ready version and retire the preceding active version; Container Apps secrets cannot replace single revision mode.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q04 — B

**Question:** For the revisioned serverless container release, the revision rollout plan must keep several versions active at the same time. Which statement about revision rollout belongs in the revisioned serverless container release record?

- **A — Incorrect.** Traffic weights route percentages to revisions or labels and must total 100 percent.
  Traffic weights route percentages to revisions or labels and must total 100 percent. In the revisioned serverless container release, this statement describes revision traffic splitting. Multiple revision mode governs revisioned serverless container release; revision traffic splitting cannot support multiple revision mode when operators must keep several versions active at the same time.
- **B — Correct.** Multiple revision mode can keep several revisions active and divide traffic between them.
  Multiple revision mode can keep several revisions active and divide traffic between them. This multiple revision mode fact resolves the revisioned serverless container release design question about how to keep several versions active at the same time.
- **C — Incorrect.** Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale.
  Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale. In the revisioned serverless container release, this statement describes minimum and maximum replicas. The minimum and maximum replicas statement accurately describes minimum and maximum replicas; however, revisioned serverless container release needs multiple revision mode to keep several versions active at the same time; minimum and maximum replicas cannot replace multiple revision mode.
- **D — Incorrect.** A Container Apps environment is the secure boundary for apps that share networking and logging integration.
  A Container Apps environment is the secure boundary for apps that share networking and logging integration. In the revisioned serverless container release, this statement describes Container Apps environments. Selecting Container Apps environments for revisioned serverless container release leaves multiple revision mode unanswered in revisioned serverless container release; the revisioned serverless container release lacks a multiple revision mode basis to keep several versions active at the same time.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q05 — B

**Question:** The revision rollout review compares four claims for the revisioned serverless container release requirement to send controlled percentages of requests to two active versions. Which claim is technically sound?

- **A — Incorrect.** The ingress target port must match the port on which the container process listens.
  The ingress target port must match the port on which the container process listens. In the revisioned serverless container release, this statement describes ingress target ports. Revisioned serverless container release asks about revision traffic splitting; this ingress target ports choice leaves the revision traffic splitting explanation missing.
- **B — Correct.** Traffic weights route percentages to revisions or labels and must total 100 percent.
  Traffic weights route percentages to revisions or labels and must total 100 percent. For revisioned serverless container release, revision traffic splitting supplies the service rule needed to send controlled percentages of requests to two active versions.
- **C — Incorrect.** Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.
  Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts. In the revisioned serverless container release, this statement describes event-driven scale rules. Selecting event-driven scale rules for revisioned serverless container release leaves revision traffic splitting unanswered in revisioned serverless container release; the revisioned serverless container release lacks a revision traffic splitting basis to send controlled percentages of requests to two active versions.
- **D — Incorrect.** A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision.
  A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision. In the revisioned serverless container release, this statement describes immutable revisions. Revision traffic splitting governs revisioned serverless container release; immutable revisions cannot support revision traffic splitting when operators must send controlled percentages of requests to two active versions.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q06 — C

**Question:** The revision rollout architecture note requires the revisioned serverless container release environment to route ingress to the port on which the container process actually listens. Which statement defines the relevant revision rollout boundary?

- **A — Incorrect.** External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path.
  External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path. In the revisioned serverless container release, this statement describes external and internal ingress. The external and internal ingress statement accurately describes external and internal ingress; however, revisioned serverless container release needs ingress target ports to route ingress to the port on which the container process actually listens; external and internal ingress cannot replace ingress target ports.
- **B — Incorrect.** Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image.
  Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image. In the revisioned serverless container release, this statement describes Container Apps secrets. Selecting Container Apps secrets for revisioned serverless container release leaves ingress target ports unanswered in revisioned serverless container release; the revisioned serverless container release lacks a ingress target ports basis to route ingress to the port on which the container process actually listens.
- **C — Correct.** The ingress target port must match the port on which the container process listens.
  The ingress target port must match the port on which the container process listens. In the revisioned serverless container release, this ingress target ports rule supports the need to route ingress to the port on which the container process actually listens.
- **D — Incorrect.** Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.
  Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update. In the revisioned serverless container release, this statement describes single revision mode. Revisioned serverless container release asks about ingress target ports; this single revision mode choice leaves the ingress target ports explanation missing.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q07 — B

**Question:** A new revision rollout operator must explain why the revisioned serverless container release can choose whether the application endpoint is externally reachable or environment-internal. Which explanation is accurate?

- **A — Incorrect.** Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale.
  Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale. In the revisioned serverless container release, this statement describes minimum and maximum replicas. Selecting minimum and maximum replicas for revisioned serverless container release leaves external and internal ingress unanswered in revisioned serverless container release; the revisioned serverless container release lacks a external and internal ingress basis to choose whether the application endpoint is externally reachable or environment-internal.
- **B — Correct.** External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path.
  For the revisioned serverless container release, the rule for external and internal ingress is defined by this statement: external ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path. It supports the required outcome to choose whether the application endpoint is externally reachable or environment-internal.
- **C — Incorrect.** A Container Apps environment is the secure boundary for apps that share networking and logging integration.
  A Container Apps environment is the secure boundary for apps that share networking and logging integration. In the revisioned serverless container release, this statement describes Container Apps environments. Revisioned serverless container release asks about external and internal ingress; this Container Apps environments choice leaves the external and internal ingress explanation missing.
- **D — Incorrect.** Multiple revision mode can keep several revisions active and divide traffic between them.
  Multiple revision mode can keep several revisions active and divide traffic between them. In the revisioned serverless container release, this statement describes multiple revision mode. The multiple revision mode statement accurately describes multiple revision mode; however, revisioned serverless container release needs external and internal ingress to choose whether the application endpoint is externally reachable or environment-internal; multiple revision mode cannot replace external and internal ingress.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q08 — D

**Question:** The revisioned serverless container release acceptance criteria require operators to keep required warm capacity while setting an upper scale limit. Which service fact supports that requirement?

- **A — Incorrect.** Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.
  Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts. In the revisioned serverless container release, this statement describes event-driven scale rules. Minimum and maximum replicas governs revisioned serverless container release; event-driven scale rules cannot support minimum and maximum replicas when operators must keep required warm capacity while setting an upper scale limit.
- **B — Incorrect.** A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision.
  A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision. In the revisioned serverless container release, this statement describes immutable revisions. Revisioned serverless container release asks about minimum and maximum replicas; this immutable revisions choice leaves the minimum and maximum replicas explanation missing.
- **C — Incorrect.** Traffic weights route percentages to revisions or labels and must total 100 percent.
  Traffic weights route percentages to revisions or labels and must total 100 percent. In the revisioned serverless container release, this statement describes revision traffic splitting. The revision traffic splitting statement accurately describes revision traffic splitting; however, revisioned serverless container release needs minimum and maximum replicas to keep required warm capacity while setting an upper scale limit; revision traffic splitting cannot replace minimum and maximum replicas.
- **D — Correct.** Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale.
  Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale. The revisioned serverless container release applies that minimum and maximum replicas boundary when operators must keep required warm capacity while setting an upper scale limit.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q09 — D

**Question:** A revision rollout reviewer challenges whether the revisioned serverless container release can translate HTTP or event demand into a desired replica count. Which response resolves the concern?

- **A — Incorrect.** Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image.
  Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image. In the revisioned serverless container release, this statement describes Container Apps secrets. Revisioned serverless container release asks about event-driven scale rules; this Container Apps secrets choice leaves the event-driven scale rules explanation missing.
- **B — Incorrect.** Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.
  Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update. In the revisioned serverless container release, this statement describes single revision mode. The single revision mode statement accurately describes single revision mode; however, revisioned serverless container release needs event-driven scale rules to translate HTTP or event demand into a desired replica count; single revision mode cannot replace event-driven scale rules.
- **C — Incorrect.** The ingress target port must match the port on which the container process listens.
  The ingress target port must match the port on which the container process listens. In the revisioned serverless container release, this statement describes ingress target ports. Selecting ingress target ports for revisioned serverless container release leaves event-driven scale rules unanswered in revisioned serverless container release; the revisioned serverless container release lacks a event-driven scale rules basis to translate HTTP or event demand into a desired replica count.
- **D — Correct.** Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.
  The revisioned serverless container release needs event-driven scale rules to translate HTTP or event demand into a desired replica count; this option states the applicable event-driven scale rules rule: container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q10 — C

**Question:** The revisioned serverless container release handoff omits the revision rollout rule needed to reference sensitive configuration without placing the clear value in ordinary settings. Which statement should the team add?

- **A — Incorrect.** A Container Apps environment is the secure boundary for apps that share networking and logging integration.
  A Container Apps environment is the secure boundary for apps that share networking and logging integration. In the revisioned serverless container release, this statement describes Container Apps environments. The Container Apps environments statement accurately describes Container Apps environments; however, revisioned serverless container release needs Container Apps secrets to reference sensitive configuration without placing the clear value in ordinary settings; Container Apps environments cannot replace Container Apps secrets.
- **B — Incorrect.** Multiple revision mode can keep several revisions active and divide traffic between them.
  Multiple revision mode can keep several revisions active and divide traffic between them. In the revisioned serverless container release, this statement describes multiple revision mode. Selecting multiple revision mode for revisioned serverless container release leaves Container Apps secrets unanswered in revisioned serverless container release; the revisioned serverless container release lacks a Container Apps secrets basis to reference sensitive configuration without placing the clear value in ordinary settings.
- **C — Correct.** Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image.
  Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image. This Container Apps secrets fact resolves the revisioned serverless container release design question about how to reference sensitive configuration without placing the clear value in ordinary settings.
- **D — Incorrect.** External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path.
  External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path. In the revisioned serverless container release, this statement describes external and internal ingress. Revisioned serverless container release asks about Container Apps secrets; this external and internal ingress choice leaves the Container Apps secrets explanation missing.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Manage secrets in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets)

**Source reviewed:** 2026-08-31

## LAB14-Q11 — C

**Question:** The revisioned serverless container release plan must place related apps inside one networking and logging boundary while limiting the mutation scope to revision rollout. Which action is appropriate?

- **A — Incorrect.** Use single mode for straightforward replacement without simultaneous version traffic.
  Use single mode for straightforward replacement without simultaneous version traffic. In the revisioned serverless container release, this action changes single revision mode. Revisioned serverless container release approved Container Apps environments, not single revision mode; only the Container Apps environments change can place related apps inside one networking and logging boundary.
- **B — Incorrect.** Enable ingress with a target port that matches the application's listener.
  Enable ingress with a target port that matches the application's listener. In the revisioned serverless container release, this action changes ingress target ports. Revisioned serverless container release requires Container Apps environments; changing ingress target ports leaves Container Apps environments absent in revisioned serverless container release; revisioned serverless container release cannot place related apps inside one networking and logging boundary.
- **C — Correct.** Create or select the managed environment before deploying the container app into it.
  Create or select the managed environment before deploying the container app into it. In revisioned serverless container release, applying Container Apps environments is the scoped way to place related apps inside one networking and logging boundary.
- **D — Incorrect.** Configure a rule with the correct type, metadata, authentication references, and scale bounds.
  Configure a rule with the correct type, metadata, authentication references, and scale bounds. In the revisioned serverless container release, this action changes event-driven scale rules. Revisioned serverless container release instead needs Container Apps environments: Create or select the managed environment before deploying the container app into it. The event-driven scale rules action omits that Container Apps environments work.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps environments](https://learn.microsoft.com/en-us/azure/container-apps/environment)

**Source reviewed:** 2026-08-31

## LAB14-Q12 — A

**Question:** A revision rollout ticket in the revisioned serverless container release says to preserve an immutable snapshot whenever revision-scoped configuration changes. Which revision rollout action completes the revisioned serverless container release request with minimal change?

- **A — Correct.** Deploy the updated image or revision-scope settings and retain the resulting revision name.
  Deploy the updated image or revision-scope settings and retain the resulting revision name. The revisioned serverless container release uses this immutable revisions operation to preserve an immutable snapshot whenever revision-scoped configuration changes within the approved scope.
- **B — Incorrect.** Enable multiple mode before configuring canary or blue-green traffic weights.
  Enable multiple mode before configuring canary or blue-green traffic weights. In the revisioned serverless container release, this action changes multiple revision mode. Multiple revision mode does not implement immutable revisions for revisioned serverless container release; the revisioned serverless container release still cannot preserve an immutable snapshot whenever revision-scoped configuration changes.
- **C — Incorrect.** Choose internal or external ingress from the approved client reachability requirement.
  Choose internal or external ingress from the approved client reachability requirement. In the revisioned serverless container release, this action changes external and internal ingress. Revisioned serverless container release instead needs immutable revisions: Deploy the updated image or revision-scope settings and retain the resulting revision name. The external and internal ingress action omits that immutable revisions work.
- **D — Incorrect.** Create the secret through a secure input path and reference its name from the container configuration.
  Create the secret through a secure input path and reference its name from the container configuration. In the revisioned serverless container release, this action changes Container Apps secrets. Revisioned serverless container release approved immutable revisions, not Container Apps secrets; only the immutable revisions change can preserve an immutable snapshot whenever revision-scoped configuration changes.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q13 — B

**Question:** The approach for the revisioned serverless container release is approved, but the revision rollout environment still cannot move production to the newest ready version and retire the preceding active version. Which implementation step closes the gap?

- **A — Incorrect.** Assign an explicit small canary weight and keep the stable revision at the remaining percentage.
  Assign an explicit small canary weight and keep the stable revision at the remaining percentage. In the revisioned serverless container release, this action changes revision traffic splitting. Revision traffic splitting does not implement single revision mode for revisioned serverless container release; the revisioned serverless container release still cannot move production to the newest ready version and retire the preceding active version.
- **B — Correct.** Use single mode for straightforward replacement without simultaneous version traffic.
  For the revisioned serverless container release, the required single revision mode action is: use single mode for straightforward replacement without simultaneous version traffic. It makes the environment able to move production to the newest ready version and retire the preceding active version.
- **C — Incorrect.** Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints.
  Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. In the revisioned serverless container release, this action changes minimum and maximum replicas. Revisioned serverless container release approved single revision mode, not minimum and maximum replicas; only the single revision mode change can move production to the newest ready version and retire the preceding active version.
- **D — Incorrect.** Create or select the managed environment before deploying the container app into it.
  Create or select the managed environment before deploying the container app into it. In the revisioned serverless container release, this action changes Container Apps environments. Revisioned serverless container release requires single revision mode; changing Container Apps environments leaves single revision mode absent in revisioned serverless container release; revisioned serverless container release cannot move production to the newest ready version and retire the preceding active version.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q14 — C

**Question:** The platform administrator releasing a revisioned serverless container app may change the revisioned serverless container release only to keep several versions active at the same time. Which revision rollout action stays within that assignment?

- **A — Incorrect.** Enable ingress with a target port that matches the application's listener.
  Enable ingress with a target port that matches the application's listener. In the revisioned serverless container release, this action changes ingress target ports. Revisioned serverless container release instead needs multiple revision mode: Enable multiple mode before configuring canary or blue-green traffic weights. The ingress target ports action omits that multiple revision mode work.
- **B — Incorrect.** Configure a rule with the correct type, metadata, authentication references, and scale bounds.
  Configure a rule with the correct type, metadata, authentication references, and scale bounds. In the revisioned serverless container release, this action changes event-driven scale rules. Revisioned serverless container release approved multiple revision mode, not event-driven scale rules; only the multiple revision mode change can keep several versions active at the same time.
- **C — Correct.** Enable multiple mode before configuring canary or blue-green traffic weights.
  Enable multiple mode before configuring canary or blue-green traffic weights. This changes multiple revision mode in the revisioned serverless container release, supplying the missing state needed to keep several versions active at the same time.
- **D — Incorrect.** Deploy the updated image or revision-scope settings and retain the resulting revision name.
  Deploy the updated image or revision-scope settings and retain the resulting revision name. In the revisioned serverless container release, this action changes immutable revisions. Immutable revisions does not implement multiple revision mode for revisioned serverless container release; the revisioned serverless container release still cannot keep several versions active at the same time.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q15 — D

**Question:** A revision rollout dry run shows no revisioned serverless container release command will send controlled percentages of requests to two active versions. Which action belongs before execution?

- **A — Incorrect.** Choose internal or external ingress from the approved client reachability requirement.
  Choose internal or external ingress from the approved client reachability requirement. In the revisioned serverless container release, this action changes external and internal ingress. Revisioned serverless container release approved revision traffic splitting, not external and internal ingress; only the revision traffic splitting change can send controlled percentages of requests to two active versions.
- **B — Incorrect.** Create the secret through a secure input path and reference its name from the container configuration.
  Create the secret through a secure input path and reference its name from the container configuration. In the revisioned serverless container release, this action changes Container Apps secrets. Revisioned serverless container release requires revision traffic splitting; changing Container Apps secrets leaves revision traffic splitting absent in revisioned serverless container release; revisioned serverless container release cannot send controlled percentages of requests to two active versions.
- **C — Incorrect.** Use single mode for straightforward replacement without simultaneous version traffic.
  Use single mode for straightforward replacement without simultaneous version traffic. In the revisioned serverless container release, this action changes single revision mode. Single revision mode does not implement revision traffic splitting for revisioned serverless container release; the revisioned serverless container release still cannot send controlled percentages of requests to two active versions.
- **D — Correct.** Assign an explicit small canary weight and keep the stable revision at the remaining percentage.
  The revisioned serverless container release must send controlled percentages of requests to two active versions; this option performs its direct revision traffic splitting change: assign an explicit small canary weight and keep the stable revision at the remaining percentage.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q16 — D

**Question:** For the revisioned serverless container release, operators need to route ingress to the port on which the container process actually listens. Which change realizes that requirement?

- **A — Incorrect.** Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints.
  Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. In the revisioned serverless container release, this action changes minimum and maximum replicas. Revisioned serverless container release requires ingress target ports; changing minimum and maximum replicas leaves ingress target ports absent in revisioned serverless container release; revisioned serverless container release cannot route ingress to the port on which the container process actually listens.
- **B — Incorrect.** Create or select the managed environment before deploying the container app into it.
  Create or select the managed environment before deploying the container app into it. In the revisioned serverless container release, this action changes Container Apps environments. Container Apps environments does not implement ingress target ports for revisioned serverless container release; the revisioned serverless container release still cannot route ingress to the port on which the container process actually listens.
- **C — Incorrect.** Enable multiple mode before configuring canary or blue-green traffic weights.
  Enable multiple mode before configuring canary or blue-green traffic weights. In the revisioned serverless container release, this action changes multiple revision mode. Revisioned serverless container release instead needs ingress target ports: Enable ingress with a target port that matches the application's listener. The multiple revision mode action omits that ingress target ports work.
- **D — Correct.** Enable ingress with a target port that matches the application's listener.
  Enable ingress with a target port that matches the application's listener. It is the least-change ingress target ports path for the revisioned serverless container release requirement to route ingress to the port on which the container process actually listens.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q17 — A

**Question:** Operators must automate the revisioned serverless container release change needed to choose whether the application endpoint is externally reachable or environment-internal. Which revision rollout operation belongs in the runbook?

- **A — Correct.** Choose internal or external ingress from the approved client reachability requirement.
  Choose internal or external ingress from the approved client reachability requirement. In revisioned serverless container release, applying external and internal ingress is the scoped way to choose whether the application endpoint is externally reachable or environment-internal.
- **B — Incorrect.** Configure a rule with the correct type, metadata, authentication references, and scale bounds.
  Configure a rule with the correct type, metadata, authentication references, and scale bounds. In the revisioned serverless container release, this action changes event-driven scale rules. Revisioned serverless container release instead needs external and internal ingress: Choose internal or external ingress from the approved client reachability requirement. The event-driven scale rules action omits that external and internal ingress work.
- **C — Incorrect.** Deploy the updated image or revision-scope settings and retain the resulting revision name.
  Deploy the updated image or revision-scope settings and retain the resulting revision name. In the revisioned serverless container release, this action changes immutable revisions. Revisioned serverless container release approved external and internal ingress, not immutable revisions; only the external and internal ingress change can choose whether the application endpoint is externally reachable or environment-internal.
- **D — Incorrect.** Assign an explicit small canary weight and keep the stable revision at the remaining percentage.
  Assign an explicit small canary weight and keep the stable revision at the remaining percentage. In the revisioned serverless container release, this action changes revision traffic splitting. Revisioned serverless container release requires external and internal ingress; changing revision traffic splitting leaves external and internal ingress absent in revisioned serverless container release; revisioned serverless container release cannot choose whether the application endpoint is externally reachable or environment-internal.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q18 — D

**Question:** A revisioned serverless container release review finds revision rollout drift from the need to keep required warm capacity while setting an upper scale limit. Which correction addresses that drift?

- **A — Incorrect.** Create the secret through a secure input path and reference its name from the container configuration.
  Create the secret through a secure input path and reference its name from the container configuration. In the revisioned serverless container release, this action changes Container Apps secrets. Revisioned serverless container release instead needs minimum and maximum replicas: Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. The Container Apps secrets action omits that minimum and maximum replicas work.
- **B — Incorrect.** Use single mode for straightforward replacement without simultaneous version traffic.
  Use single mode for straightforward replacement without simultaneous version traffic. In the revisioned serverless container release, this action changes single revision mode. Revisioned serverless container release approved minimum and maximum replicas, not single revision mode; only the minimum and maximum replicas change can keep required warm capacity while setting an upper scale limit.
- **C — Incorrect.** Enable ingress with a target port that matches the application's listener.
  Enable ingress with a target port that matches the application's listener. In the revisioned serverless container release, this action changes ingress target ports. Revisioned serverless container release requires minimum and maximum replicas; changing ingress target ports leaves minimum and maximum replicas absent in revisioned serverless container release; revisioned serverless container release cannot keep required warm capacity while setting an upper scale limit.
- **D — Correct.** Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints.
  Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. The revisioned serverless container release uses this minimum and maximum replicas operation to keep required warm capacity while setting an upper scale limit within the approved scope.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q19 — D

**Question:** The revisioned serverless container release window permits only the revision rollout change needed to translate HTTP or event demand into a desired replica count. Which option respects the boundary?

- **A — Incorrect.** Create or select the managed environment before deploying the container app into it.
  Create or select the managed environment before deploying the container app into it. In the revisioned serverless container release, this action changes Container Apps environments. Revisioned serverless container release approved event-driven scale rules, not Container Apps environments; only the event-driven scale rules change can translate HTTP or event demand into a desired replica count.
- **B — Incorrect.** Enable multiple mode before configuring canary or blue-green traffic weights.
  Enable multiple mode before configuring canary or blue-green traffic weights. In the revisioned serverless container release, this action changes multiple revision mode. Revisioned serverless container release requires event-driven scale rules; changing multiple revision mode leaves event-driven scale rules absent in revisioned serverless container release; revisioned serverless container release cannot translate HTTP or event demand into a desired replica count.
- **C — Incorrect.** Choose internal or external ingress from the approved client reachability requirement.
  Choose internal or external ingress from the approved client reachability requirement. In the revisioned serverless container release, this action changes external and internal ingress. External and internal ingress does not implement event-driven scale rules for revisioned serverless container release; the revisioned serverless container release still cannot translate HTTP or event demand into a desired replica count.
- **D — Correct.** Configure a rule with the correct type, metadata, authentication references, and scale bounds.
  For the revisioned serverless container release, the required event-driven scale rules action is: configure a rule with the correct type, metadata, authentication references, and scale bounds. It makes the environment able to translate HTTP or event demand into a desired replica count.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q20 — D

**Question:** The revision rollout preflight has passed; the revisioned serverless container release must now reference sensitive configuration without placing the clear value in ordinary settings. Which operation should run?

- **A — Incorrect.** Deploy the updated image or revision-scope settings and retain the resulting revision name.
  Deploy the updated image or revision-scope settings and retain the resulting revision name. In the revisioned serverless container release, this action changes immutable revisions. Revisioned serverless container release requires Container Apps secrets; changing immutable revisions leaves Container Apps secrets absent in revisioned serverless container release; revisioned serverless container release cannot reference sensitive configuration without placing the clear value in ordinary settings.
- **B — Incorrect.** Assign an explicit small canary weight and keep the stable revision at the remaining percentage.
  Assign an explicit small canary weight and keep the stable revision at the remaining percentage. In the revisioned serverless container release, this action changes revision traffic splitting. Revision traffic splitting does not implement Container Apps secrets for revisioned serverless container release; the revisioned serverless container release still cannot reference sensitive configuration without placing the clear value in ordinary settings.
- **C — Incorrect.** Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints.
  Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. In the revisioned serverless container release, this action changes minimum and maximum replicas. Revisioned serverless container release instead needs Container Apps secrets: Create the secret through a secure input path and reference its name from the container configuration. The minimum and maximum replicas action omits that Container Apps secrets work.
- **D — Correct.** Create the secret through a secure input path and reference its name from the container configuration.
  Create the secret through a secure input path and reference its name from the container configuration. This changes Container Apps secrets in the revisioned serverless container release, supplying the missing state needed to reference sensitive configuration without placing the clear value in ordinary settings.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Manage secrets in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets)

**Source reviewed:** 2026-08-31

## LAB14-Q21 — B

**Question:** Before revisioned serverless container release cleanup, the revision rollout team must reconfirm it can place related apps inside one networking and logging boundary. Which read-only inspection should run?

- **A — Incorrect.** List active revisions and confirm their combined traffic percentages equal 100.
  List active revisions and confirm their combined traffic percentages equal 100. In the revisioned serverless container release, this check observes multiple revision mode. Revisioned serverless container release output covers multiple revision mode, not Container Apps environments; the Container Apps environments requirement to place related apps inside one networking and logging boundary remains unverified.
- **B — Correct.** Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
  The revisioned serverless container release validator needs this Container Apps environments result: query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration. It proves the outcome to place related apps inside one networking and logging boundary rather than an adjacent checkpoint.
- **C — Incorrect.** Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
  Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location. In the revisioned serverless container release, this check observes external and internal ingress. Revisioned serverless container release reads external and internal ingress, leaving Container Apps environments unproved in revisioned serverless container release; revisioned serverless container release still has no Container Apps environments proof.
- **D — Incorrect.** Query secret references and confirm command output does not reveal the stored secret value.
  Query secret references and confirm command output does not reveal the stored secret value. In the revisioned serverless container release, this check observes Container Apps secrets. Revisioned serverless container release could pass Container Apps secrets while Container Apps environments is wrong; revisioned serverless container release still lacks Container Apps environments proof.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps environments](https://learn.microsoft.com/en-us/azure/container-apps/environment)

**Source reviewed:** 2026-08-31

## LAB14-Q22 — C

**Question:** The revisioned serverless container release setup reports success after the revision rollout attempt to preserve an immutable snapshot whenever revision-scoped configuration changes. Which revision rollout read-only observation proves the revisioned serverless container release outcome?

- **A — Incorrect.** Query ingress.traffic and match revision names, labels, and exact weights.
  Query ingress.traffic and match revision names, labels, and exact weights. In the revisioned serverless container release, this check observes revision traffic splitting. Revision traffic splitting success in revisioned serverless container release cannot verify immutable revisions; revisioned serverless container release cannot preserve an immutable snapshot whenever revision-scoped configuration changes until immutable revisions evidence exists.
- **B — Incorrect.** Query the active revision template scale bounds and current replica count.
  Query the active revision template scale bounds and current replica count. In the revisioned serverless container release, this check observes minimum and maximum replicas. Revisioned serverless container release reads minimum and maximum replicas, leaving immutable revisions unproved in revisioned serverless container release; revisioned serverless container release still has no immutable revisions proof.
- **C — Correct.** List revisions and compare image, createdTime, active state, health, and traffic weight.
  List revisions and compare image, createdTime, active state, health, and traffic weight. This is independent immutable revisions evidence for the revisioned serverless container release, even if revisioned serverless container release setup reports success before immutable revisions becomes observable.
- **D — Incorrect.** Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
  Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration. In the revisioned serverless container release, this check observes Container Apps environments. Revisioned serverless container release output covers Container Apps environments, not immutable revisions; the immutable revisions requirement to preserve an immutable snapshot whenever revision-scoped configuration changes remains unverified.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q23 — D

**Question:** The revision rollout log says the revisioned serverless container release can now move production to the newest ready version and retire the preceding active version. Which revision rollout state should the revisioned serverless container release acceptance test retain?

- **A — Incorrect.** Query ingress.targetPort and compare it with container startup logs and probe configuration.
  Query ingress.targetPort and compare it with container startup logs and probe configuration. In the revisioned serverless container release, this check observes ingress target ports. Revisioned serverless container release reads ingress target ports, leaving single revision mode unproved in revisioned serverless container release; revisioned serverless container release still has no single revision mode proof.
- **B — Incorrect.** Query the revision's scale rules and inspect replica changes while generating controlled demand.
  Query the revision's scale rules and inspect replica changes while generating controlled demand. In the revisioned serverless container release, this check observes event-driven scale rules. Revisioned serverless container release could pass event-driven scale rules while single revision mode is wrong; revisioned serverless container release still lacks single revision mode proof.
- **C — Incorrect.** List revisions and compare image, createdTime, active state, health, and traffic weight.
  List revisions and compare image, createdTime, active state, health, and traffic weight. In the revisioned serverless container release, this check observes immutable revisions. Revisioned serverless container release output covers immutable revisions, not single revision mode; the single revision mode requirement to move production to the newest ready version and retire the preceding active version remains unverified.
- **D — Correct.** Query activeRevisionsMode and confirm exactly the intended latest revision is active.
  Query activeRevisionsMode and confirm exactly the intended latest revision is active. For revisioned serverless container release, this single revision mode read confirms the service can move production to the newest ready version and retire the preceding active version.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q24 — C

**Question:** The revisioned serverless container release rejects revision rollout exit status as proof it can keep several versions active at the same time. Which revisioned serverless container release result is valid evidence?

- **A — Incorrect.** Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
  Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location. In the revisioned serverless container release, this check observes external and internal ingress. Revisioned serverless container release could pass external and internal ingress while multiple revision mode is wrong; revisioned serverless container release still lacks multiple revision mode proof.
- **B — Incorrect.** Query secret references and confirm command output does not reveal the stored secret value.
  Query secret references and confirm command output does not reveal the stored secret value. In the revisioned serverless container release, this check observes Container Apps secrets. Revisioned serverless container release output covers Container Apps secrets, not multiple revision mode; the multiple revision mode requirement to keep several versions active at the same time remains unverified.
- **C — Correct.** List active revisions and confirm their combined traffic percentages equal 100.
  List active revisions and confirm their combined traffic percentages equal 100. The revisioned serverless container release reads multiple revision mode directly; that multiple revision mode result proves the revisioned serverless container release can keep several versions active at the same time without another mutation.
- **D — Incorrect.** Query activeRevisionsMode and confirm exactly the intended latest revision is active.
  Query activeRevisionsMode and confirm exactly the intended latest revision is active. In the revisioned serverless container release, this check observes single revision mode. Revisioned serverless container release reads single revision mode, leaving multiple revision mode unproved in revisioned serverless container release; revisioned serverless container release still has no multiple revision mode proof.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q25 — A

**Question:** The revision rollout validator needs one revisioned serverless container release query after the change to send controlled percentages of requests to two active versions. Which revision rollout property should the revisioned serverless container release validator inspect?

- **A — Correct.** Query ingress.traffic and match revision names, labels, and exact weights.
  For the revisioned serverless container release, this revision traffic splitting observation is decisive: query ingress.traffic and match revision names, labels, and exact weights. It is revisioned serverless container release evidence that operators can send controlled percentages of requests to two active versions.
- **B — Incorrect.** Query the active revision template scale bounds and current replica count.
  Query the active revision template scale bounds and current replica count. In the revisioned serverless container release, this check observes minimum and maximum replicas. Minimum and maximum replicas success in revisioned serverless container release cannot verify revision traffic splitting; revisioned serverless container release cannot send controlled percentages of requests to two active versions until revision traffic splitting evidence exists.
- **C — Incorrect.** Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
  Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration. In the revisioned serverless container release, this check observes Container Apps environments. Revisioned serverless container release reads Container Apps environments, leaving revision traffic splitting unproved in revisioned serverless container release; revisioned serverless container release still has no revision traffic splitting proof.
- **D — Incorrect.** List active revisions and confirm their combined traffic percentages equal 100.
  List active revisions and confirm their combined traffic percentages equal 100. In the revisioned serverless container release, this check observes multiple revision mode. Revisioned serverless container release could pass multiple revision mode while revision traffic splitting is wrong; revisioned serverless container release still lacks revision traffic splitting proof.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q26 — D

**Question:** The platform administrator releasing a revisioned serverless container app must confirm the revisioned serverless container release, without mutation, can route ingress to the port on which the container process actually listens. Which revision rollout check qualifies?

- **A — Incorrect.** Query the revision's scale rules and inspect replica changes while generating controlled demand.
  Query the revision's scale rules and inspect replica changes while generating controlled demand. In the revisioned serverless container release, this check observes event-driven scale rules. Event-driven scale rules success in revisioned serverless container release cannot verify ingress target ports; revisioned serverless container release cannot route ingress to the port on which the container process actually listens until ingress target ports evidence exists.
- **B — Incorrect.** List revisions and compare image, createdTime, active state, health, and traffic weight.
  List revisions and compare image, createdTime, active state, health, and traffic weight. In the revisioned serverless container release, this check observes immutable revisions. Revisioned serverless container release reads immutable revisions, leaving ingress target ports unproved in revisioned serverless container release; revisioned serverless container release still has no ingress target ports proof.
- **C — Incorrect.** Query ingress.traffic and match revision names, labels, and exact weights.
  Query ingress.traffic and match revision names, labels, and exact weights. In the revisioned serverless container release, this check observes revision traffic splitting. Revisioned serverless container release could pass revision traffic splitting while ingress target ports is wrong; revisioned serverless container release still lacks ingress target ports proof.
- **D — Correct.** Query ingress.targetPort and compare it with container startup logs and probe configuration.
  Query ingress.targetPort and compare it with container startup logs and probe configuration. Because the revisioned serverless container release check observes ingress target ports, it independently verifies the requirement to route ingress to the port on which the container process actually listens.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q27 — B

**Question:** The revisioned serverless container release configuration is complete; the revision rollout reviewers need evidence it can choose whether the application endpoint is externally reachable or environment-internal. Which observation shows success?

- **A — Incorrect.** Query secret references and confirm command output does not reveal the stored secret value.
  Query secret references and confirm command output does not reveal the stored secret value. In the revisioned serverless container release, this check observes Container Apps secrets. Revisioned serverless container release reads Container Apps secrets, leaving external and internal ingress unproved in revisioned serverless container release; revisioned serverless container release still has no external and internal ingress proof.
- **B — Correct.** Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
  The revisioned serverless container release validator needs this external and internal ingress result: query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location. It proves the outcome to choose whether the application endpoint is externally reachable or environment-internal rather than an adjacent checkpoint.
- **C — Incorrect.** Query activeRevisionsMode and confirm exactly the intended latest revision is active.
  Query activeRevisionsMode and confirm exactly the intended latest revision is active. In the revisioned serverless container release, this check observes single revision mode. Revisioned serverless container release output covers single revision mode, not external and internal ingress; the external and internal ingress requirement to choose whether the application endpoint is externally reachable or environment-internal remains unverified.
- **D — Incorrect.** Query ingress.targetPort and compare it with container startup logs and probe configuration.
  Query ingress.targetPort and compare it with container startup logs and probe configuration. In the revisioned serverless container release, this check observes ingress target ports. Ingress target ports success in revisioned serverless container release cannot verify external and internal ingress; revisioned serverless container release cannot choose whether the application endpoint is externally reachable or environment-internal until external and internal ingress evidence exists.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q28 — A

**Question:** The revision rollout validation asks whether the revisioned serverless container release can keep required warm capacity while setting an upper scale limit. Which observable state is strongest?

- **A — Correct.** Query the active revision template scale bounds and current replica count.
  Query the active revision template scale bounds and current replica count. This is independent minimum and maximum replicas evidence for the revisioned serverless container release, even if revisioned serverless container release setup reports success before minimum and maximum replicas becomes observable.
- **B — Incorrect.** Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
  Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration. In the revisioned serverless container release, this check observes Container Apps environments. Revisioned serverless container release output covers Container Apps environments, not minimum and maximum replicas; the minimum and maximum replicas requirement to keep required warm capacity while setting an upper scale limit remains unverified.
- **C — Incorrect.** List active revisions and confirm their combined traffic percentages equal 100.
  List active revisions and confirm their combined traffic percentages equal 100. In the revisioned serverless container release, this check observes multiple revision mode. Multiple revision mode success in revisioned serverless container release cannot verify minimum and maximum replicas; revisioned serverless container release cannot keep required warm capacity while setting an upper scale limit until minimum and maximum replicas evidence exists.
- **D — Incorrect.** Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
  Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location. In the revisioned serverless container release, this check observes external and internal ingress. Revisioned serverless container release reads external and internal ingress, leaving minimum and maximum replicas unproved in revisioned serverless container release; revisioned serverless container release still has no minimum and maximum replicas proof.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q29 — A

**Question:** A revisioned serverless container release review must prove the revision rollout ability to translate HTTP or event demand into a desired replica count. Which check avoids an adjacent feature?

- **A — Correct.** Query the revision's scale rules and inspect replica changes while generating controlled demand.
  Query the revision's scale rules and inspect replica changes while generating controlled demand. For revisioned serverless container release, this event-driven scale rules read confirms the service can translate HTTP or event demand into a desired replica count.
- **B — Incorrect.** List revisions and compare image, createdTime, active state, health, and traffic weight.
  List revisions and compare image, createdTime, active state, health, and traffic weight. In the revisioned serverless container release, this check observes immutable revisions. Immutable revisions success in revisioned serverless container release cannot verify event-driven scale rules; revisioned serverless container release cannot translate HTTP or event demand into a desired replica count until event-driven scale rules evidence exists.
- **C — Incorrect.** Query ingress.traffic and match revision names, labels, and exact weights.
  Query ingress.traffic and match revision names, labels, and exact weights. In the revisioned serverless container release, this check observes revision traffic splitting. Revisioned serverless container release reads revision traffic splitting, leaving event-driven scale rules unproved in revisioned serverless container release; revisioned serverless container release still has no event-driven scale rules proof.
- **D — Incorrect.** Query the active revision template scale bounds and current replica count.
  Query the active revision template scale bounds and current replica count. In the revisioned serverless container release, this check observes minimum and maximum replicas. Revisioned serverless container release could pass minimum and maximum replicas while event-driven scale rules is wrong; revisioned serverless container release still lacks event-driven scale rules proof.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q30 — A

**Question:** The revisioned serverless container release evidence bundle needs a revision rollout result showing it can reference sensitive configuration without placing the clear value in ordinary settings. Which result belongs in the checkpoint?

- **A — Correct.** Query secret references and confirm command output does not reveal the stored secret value.
  Query secret references and confirm command output does not reveal the stored secret value. The revisioned serverless container release reads Container Apps secrets directly; that Container Apps secrets result proves the revisioned serverless container release can reference sensitive configuration without placing the clear value in ordinary settings without another mutation.
- **B — Incorrect.** Query activeRevisionsMode and confirm exactly the intended latest revision is active.
  Query activeRevisionsMode and confirm exactly the intended latest revision is active. In the revisioned serverless container release, this check observes single revision mode. Revisioned serverless container release reads single revision mode, leaving Container Apps secrets unproved in revisioned serverless container release; revisioned serverless container release still has no Container Apps secrets proof.
- **C — Incorrect.** Query ingress.targetPort and compare it with container startup logs and probe configuration.
  Query ingress.targetPort and compare it with container startup logs and probe configuration. In the revisioned serverless container release, this check observes ingress target ports. Revisioned serverless container release could pass ingress target ports while Container Apps secrets is wrong; revisioned serverless container release still lacks Container Apps secrets proof.
- **D — Incorrect.** Query the revision's scale rules and inspect replica changes while generating controlled demand.
  Query the revision's scale rules and inspect replica changes while generating controlled demand. In the revisioned serverless container release, this check observes event-driven scale rules. Revisioned serverless container release output covers event-driven scale rules, not Container Apps secrets; the Container Apps secrets requirement to reference sensitive configuration without placing the clear value in ordinary settings remains unverified.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Manage secrets in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets)

**Source reviewed:** 2026-08-31

## LAB14-Q31 — D

**Question:** Other revisioned serverless container release components are healthy, but the revision rollout still cannot place related apps inside one networking and logging boundary. Which state causes the isolated failure?

- **A — Incorrect.** Validation queried only the app object and missed that the new revision is unhealthy.
  Validation queried only the app object and missed that the new revision is unhealthy. The revisioned serverless container release fault concerns immutable revisions. Revisioned serverless container release has immutable revisions impact, but Container Apps environments is the revisioned serverless container release failed path; the immutable revisions state cannot produce Container Apps environments failure.
- **B — Incorrect.** Ingress forwards to port 80 while the container process listens on port 8080.
  Ingress forwards to port 80 while the container process listens on port 8080. The revisioned serverless container release fault concerns ingress target ports. Revisioned serverless container release could repair ingress target ports while Container Apps environments stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to place related apps inside one networking and logging boundary.
- **C — Incorrect.** The environment variable contains the literal credential instead of a secret reference.
  The environment variable contains the literal credential instead of a secret reference. The revisioned serverless container release fault concerns Container Apps secrets. Revisioned serverless container release failed on Container Apps environments; this Container Apps secrets finding redirects revisioned serverless container release remediation away from Container Apps environments.
- **D — Correct.** The app deployment references an environment in a different region.
  For the revisioned serverless container release, the Container Apps environments failure is causal: the app deployment references an environment in a different region. Correcting it restores the ability to place related apps inside one networking and logging boundary.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps environments](https://learn.microsoft.com/en-us/azure/container-apps/environment)

**Source reviewed:** 2026-08-31

## LAB14-Q32 — B

**Question:** During a revision rollout fault drill, the revisioned serverless container release does not preserve an immutable snapshot whenever revision-scoped configuration changes. Which finding identifies the defect?

- **A — Incorrect.** The new revision never becomes ready, so the earlier revision remains serving traffic.
  The new revision never becomes ready, so the earlier revision remains serving traffic. The revisioned serverless container release fault concerns single revision mode. Revisioned serverless container release could repair single revision mode while immutable revisions stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to preserve an immutable snapshot whenever revision-scoped configuration changes.
- **B — Correct.** Validation queried only the app object and missed that the new revision is unhealthy.
  Validation queried only the app object and missed that the new revision is unhealthy. The finding is specific to immutable revisions in the revisioned serverless container release; repairing immutable revisions restores the revisioned serverless container release ability to preserve an immutable snapshot whenever revision-scoped configuration changes.
- **C — Incorrect.** External ingress was enabled for a service intended to be reachable only inside the environment.
  External ingress was enabled for a service intended to be reachable only inside the environment. The revisioned serverless container release fault concerns external and internal ingress. Revisioned serverless container release may fix external and internal ingress, yet immutable revisions still fails; this revisioned serverless container release diagnosis of external and internal ingress is wrong for immutable revisions.
- **D — Incorrect.** The app deployment references an environment in a different region.
  The app deployment references an environment in a different region. The revisioned serverless container release fault concerns Container Apps environments. Revisioned serverless container release has Container Apps environments impact, but immutable revisions is the revisioned serverless container release failed path; the Container Apps environments state cannot produce immutable revisions failure.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q33 — A

**Question:** The revisioned serverless container release setup finishes, yet the revision rollout cannot move production to the newest ready version and retire the preceding active version. Which misconfiguration explains the mismatch?

- **A — Correct.** The new revision never becomes ready, so the earlier revision remains serving traffic.
  The revisioned serverless container release cannot move production to the newest ready version and retire the preceding active version because of this single revision mode defect: the new revision never becomes ready, so the earlier revision remains serving traffic. The symptom and repair align.
- **B — Incorrect.** The app remains in single revision mode while the runbook attempts a traffic split.
  The app remains in single revision mode while the runbook attempts a traffic split. The revisioned serverless container release fault concerns multiple revision mode. Revisioned serverless container release may fix multiple revision mode, yet single revision mode still fails; this revisioned serverless container release diagnosis of multiple revision mode is wrong for single revision mode.
- **C — Incorrect.** minReplicas is zero even though the workload requires one continuously warm instance.
  minReplicas is zero even though the workload requires one continuously warm instance. The revisioned serverless container release fault concerns minimum and maximum replicas. Revisioned serverless container release has minimum and maximum replicas impact, but single revision mode is the revisioned serverless container release failed path; the minimum and maximum replicas state cannot produce single revision mode failure.
- **D — Incorrect.** Validation queried only the app object and missed that the new revision is unhealthy.
  Validation queried only the app object and missed that the new revision is unhealthy. The revisioned serverless container release fault concerns immutable revisions. Revisioned serverless container release could repair immutable revisions while single revision mode stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to move production to the newest ready version and retire the preceding active version.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q34 — A

**Question:** A revision rollout break/fix in the revisioned serverless container release fails when operators try to keep several versions active at the same time. Which diagnosis fits?

- **A — Correct.** The app remains in single revision mode while the runbook attempts a traffic split.
  The app remains in single revision mode while the runbook attempts a traffic split. Removing this multiple revision mode condition lets the revisioned serverless container release keep several versions active at the same time while leaving healthy controls unchanged.
- **B — Incorrect.** The configured traffic weights total more than 100 percent.
  The configured traffic weights total more than 100 percent. The revisioned serverless container release fault concerns revision traffic splitting. Revisioned serverless container release has revision traffic splitting impact, but multiple revision mode is the revisioned serverless container release failed path; the revision traffic splitting state cannot produce multiple revision mode failure.
- **C — Incorrect.** The rule metadata names a secret that is not defined for the container app.
  The rule metadata names a secret that is not defined for the container app. The revisioned serverless container release fault concerns event-driven scale rules. Revisioned serverless container release could repair event-driven scale rules while multiple revision mode stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to keep several versions active at the same time.
- **D — Incorrect.** The new revision never becomes ready, so the earlier revision remains serving traffic.
  The new revision never becomes ready, so the earlier revision remains serving traffic. The revisioned serverless container release fault concerns single revision mode. Revisioned serverless container release failed on multiple revision mode; this single revision mode finding redirects revisioned serverless container release remediation away from multiple revision mode.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q35 — C

**Question:** The revisioned serverless container release troubleshooting scope is the revision rollout need to send controlled percentages of requests to two active versions. Which condition should be corrected first?

- **A — Incorrect.** Ingress forwards to port 80 while the container process listens on port 8080.
  Ingress forwards to port 80 while the container process listens on port 8080. The revisioned serverless container release fault concerns ingress target ports. Revisioned serverless container release has ingress target ports impact, but revision traffic splitting is the revisioned serverless container release failed path; the ingress target ports state cannot produce revision traffic splitting failure.
- **B — Incorrect.** The environment variable contains the literal credential instead of a secret reference.
  The environment variable contains the literal credential instead of a secret reference. The revisioned serverless container release fault concerns Container Apps secrets. Revisioned serverless container release could repair Container Apps secrets while revision traffic splitting stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to send controlled percentages of requests to two active versions.
- **C — Correct.** The configured traffic weights total more than 100 percent.
  The configured traffic weights total more than 100 percent. In revisioned serverless container release, this revision traffic splitting cause matches the failure to send controlled percentages of requests to two active versions.
- **D — Incorrect.** The app remains in single revision mode while the runbook attempts a traffic split.
  The app remains in single revision mode while the runbook attempts a traffic split. The revisioned serverless container release fault concerns multiple revision mode. Revisioned serverless container release may fix multiple revision mode, yet revision traffic splitting still fails; this revisioned serverless container release diagnosis of multiple revision mode is wrong for revision traffic splitting.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q36 — C

**Question:** The revisioned serverless container release result is partial because the revision rollout cannot route ingress to the port on which the container process actually listens. Which condition accounts for that result?

- **A — Incorrect.** External ingress was enabled for a service intended to be reachable only inside the environment.
  External ingress was enabled for a service intended to be reachable only inside the environment. The revisioned serverless container release fault concerns external and internal ingress. Revisioned serverless container release could repair external and internal ingress while ingress target ports stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to route ingress to the port on which the container process actually listens.
- **B — Incorrect.** The app deployment references an environment in a different region.
  The app deployment references an environment in a different region. The revisioned serverless container release fault concerns Container Apps environments. Revisioned serverless container release failed on ingress target ports; this Container Apps environments finding redirects revisioned serverless container release remediation away from ingress target ports.
- **C — Correct.** Ingress forwards to port 80 while the container process listens on port 8080.
  Ingress forwards to port 80 while the container process listens on port 8080. This revisioned serverless container release condition breaks ingress target ports, explaining why operators cannot route ingress to the port on which the container process actually listens.
- **D — Incorrect.** The configured traffic weights total more than 100 percent.
  The configured traffic weights total more than 100 percent. The revisioned serverless container release fault concerns revision traffic splitting. Revisioned serverless container release has revision traffic splitting impact, but ingress target ports is the revisioned serverless container release failed path; the revision traffic splitting state cannot produce ingress target ports failure.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q37 — B

**Question:** The revision rollout evidence shows the revisioned serverless container release cannot choose whether the application endpoint is externally reachable or environment-internal. Which root cause fits that evidence?

- **A — Incorrect.** minReplicas is zero even though the workload requires one continuously warm instance.
  minReplicas is zero even though the workload requires one continuously warm instance. The revisioned serverless container release fault concerns minimum and maximum replicas. Revisioned serverless container release failed on external and internal ingress; this minimum and maximum replicas finding redirects revisioned serverless container release remediation away from external and internal ingress.
- **B — Correct.** External ingress was enabled for a service intended to be reachable only inside the environment.
  For the revisioned serverless container release, the external and internal ingress failure is causal: external ingress was enabled for a service intended to be reachable only inside the environment. Correcting it restores the ability to choose whether the application endpoint is externally reachable or environment-internal.
- **C — Incorrect.** Validation queried only the app object and missed that the new revision is unhealthy.
  Validation queried only the app object and missed that the new revision is unhealthy. The revisioned serverless container release fault concerns immutable revisions. Revisioned serverless container release has immutable revisions impact, but external and internal ingress is the revisioned serverless container release failed path; the immutable revisions state cannot produce external and internal ingress failure.
- **D — Incorrect.** Ingress forwards to port 80 while the container process listens on port 8080.
  Ingress forwards to port 80 while the container process listens on port 8080. The revisioned serverless container release fault concerns ingress target ports. Revisioned serverless container release could repair ingress target ports while external and internal ingress stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to choose whether the application endpoint is externally reachable or environment-internal.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q38 — C

**Question:** Although the revisioned serverless container release is meant to let the revision rollout keep required warm capacity while setting an upper scale limit, its checkpoint fails. Which revision rollout defect explains the failure?

- **A — Incorrect.** The rule metadata names a secret that is not defined for the container app.
  The rule metadata names a secret that is not defined for the container app. The revisioned serverless container release fault concerns event-driven scale rules. Revisioned serverless container release may fix event-driven scale rules, yet minimum and maximum replicas still fails; this revisioned serverless container release diagnosis of event-driven scale rules is wrong for minimum and maximum replicas.
- **B — Incorrect.** The new revision never becomes ready, so the earlier revision remains serving traffic.
  The new revision never becomes ready, so the earlier revision remains serving traffic. The revisioned serverless container release fault concerns single revision mode. Revisioned serverless container release has single revision mode impact, but minimum and maximum replicas is the revisioned serverless container release failed path; the single revision mode state cannot produce minimum and maximum replicas failure.
- **C — Correct.** minReplicas is zero even though the workload requires one continuously warm instance.
  MinReplicas is zero even though the workload requires one continuously warm instance. The finding is specific to minimum and maximum replicas in the revisioned serverless container release; repairing minimum and maximum replicas restores the revisioned serverless container release ability to keep required warm capacity while setting an upper scale limit.
- **D — Incorrect.** External ingress was enabled for a service intended to be reachable only inside the environment.
  External ingress was enabled for a service intended to be reachable only inside the environment. The revisioned serverless container release fault concerns external and internal ingress. Revisioned serverless container release failed on minimum and maximum replicas; this external and internal ingress finding redirects revisioned serverless container release remediation away from minimum and maximum replicas.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q39 — A

**Question:** The revision rollout support team isolated the revisioned serverless container release incident to the attempt to translate HTTP or event demand into a desired replica count. Which condition prevents success?

- **A — Correct.** The rule metadata names a secret that is not defined for the container app.
  The revisioned serverless container release cannot translate HTTP or event demand into a desired replica count because of this event-driven scale rules defect: the rule metadata names a secret that is not defined for the container app. The symptom and repair align.
- **B — Incorrect.** The environment variable contains the literal credential instead of a secret reference.
  The environment variable contains the literal credential instead of a secret reference. The revisioned serverless container release fault concerns Container Apps secrets. Revisioned serverless container release could repair Container Apps secrets while event-driven scale rules stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to translate HTTP or event demand into a desired replica count.
- **C — Incorrect.** The app remains in single revision mode while the runbook attempts a traffic split.
  The app remains in single revision mode while the runbook attempts a traffic split. The revisioned serverless container release fault concerns multiple revision mode. Revisioned serverless container release failed on event-driven scale rules; this multiple revision mode finding redirects revisioned serverless container release remediation away from event-driven scale rules.
- **D — Incorrect.** minReplicas is zero even though the workload requires one continuously warm instance.
  minReplicas is zero even though the workload requires one continuously warm instance. The revisioned serverless container release fault concerns minimum and maximum replicas. Revisioned serverless container release may fix minimum and maximum replicas, yet event-driven scale rules still fails; this revisioned serverless container release diagnosis of minimum and maximum replicas is wrong for event-driven scale rules.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q40 — B

**Question:** A revisioned serverless container release query surprises the platform administrator releasing a revisioned serverless container app during the revision rollout attempt to reference sensitive configuration without placing the clear value in ordinary settings. Which finding explains it?

- **A — Incorrect.** The app deployment references an environment in a different region.
  The app deployment references an environment in a different region. The revisioned serverless container release fault concerns Container Apps environments. Revisioned serverless container release could repair Container Apps environments while Container Apps secrets stays broken in revisioned serverless container release; the revisioned serverless container release remains unable to reference sensitive configuration without placing the clear value in ordinary settings.
- **B — Correct.** The environment variable contains the literal credential instead of a secret reference.
  The environment variable contains the literal credential instead of a secret reference. Removing this Container Apps secrets condition lets the revisioned serverless container release reference sensitive configuration without placing the clear value in ordinary settings while leaving healthy controls unchanged.
- **C — Incorrect.** The configured traffic weights total more than 100 percent.
  The configured traffic weights total more than 100 percent. The revisioned serverless container release fault concerns revision traffic splitting. Revisioned serverless container release may fix revision traffic splitting, yet Container Apps secrets still fails; this revisioned serverless container release diagnosis of revision traffic splitting is wrong for Container Apps secrets.
- **D — Incorrect.** The rule metadata names a secret that is not defined for the container app.
  The rule metadata names a secret that is not defined for the container app. The revisioned serverless container release fault concerns event-driven scale rules. Revisioned serverless container release has event-driven scale rules impact, but Container Apps secrets is the revisioned serverless container release failed path; the event-driven scale rules state cannot produce Container Apps secrets failure.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Manage secrets in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets)

**Source reviewed:** 2026-08-31

## LAB14-Q41 — B

**Question:** The revisioned serverless container release checkpoint requires both this revision rollout outcome—place related apps inside one networking and logging boundary—and a read-only revisioned serverless container release state check. Which revision rollout response is complete?

- **A — Incorrect.** First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
  First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active. This revisioned serverless container release pair serves single revision mode. Single revision mode cannot replace Container Apps environments in revisioned serverless container release. Use this Container Apps environments pair instead: First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
- **B — Correct.** First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
  First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration. For revisioned serverless container release, the Container Apps environments operation precedes its Container Apps environments read-back check, allowing it to place related apps inside one networking and logging boundary.
- **C — Incorrect.** First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
  First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location. This revisioned serverless container release pair serves external and internal ingress. Revisioned serverless container release uses external and internal ingress for both steps; Container Apps environments remains untouched in revisioned serverless container release, so its Container Apps environments gate to place related apps inside one networking and logging boundary fails.
- **D — Incorrect.** First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.
  First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count. This revisioned serverless container release pair serves minimum and maximum replicas. Revisioned serverless container release closes minimum and maximum replicas, not Container Apps environments; without the Container Apps environments workflow, it cannot place related apps inside one networking and logging boundary.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps environments](https://learn.microsoft.com/en-us/azure/container-apps/environment)

**Source reviewed:** 2026-08-31

## LAB14-Q42 — C

**Question:** The revisioned serverless container release runbook must preserve an immutable snapshot whenever revision-scoped configuration changes, then retain revision rollout read-back evidence. Which revisioned serverless container release pair completes both duties?

- **A — Incorrect.** First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100.
  First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100. This revisioned serverless container release pair serves multiple revision mode. Revisioned serverless container release proves multiple revision mode, but immutable revisions lacks implementation in revisioned serverless container release and immutable revisions proof; the immutable revisions outcome to preserve an immutable snapshot whenever revision-scoped configuration changes remains open.
- **B — Incorrect.** First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.
  First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count. This revisioned serverless container release pair serves minimum and maximum replicas. Revisioned serverless container release uses minimum and maximum replicas for both steps; immutable revisions remains untouched in revisioned serverless container release, so its immutable revisions gate to preserve an immutable snapshot whenever revision-scoped configuration changes fails.
- **C — Correct.** First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.
  First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight. In the revisioned serverless container release, the first immutable revisions step runs; the revisioned serverless container release then reads immutable revisions state to prove it can preserve an immutable snapshot whenever revision-scoped configuration changes.
- **D — Incorrect.** First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.
  First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand. This revisioned serverless container release pair serves event-driven scale rules. Event-driven scale rules cannot replace immutable revisions in revisioned serverless container release. Use this immutable revisions pair instead: First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q43 — B

**Question:** To satisfy the revision rollout requirement, operators must change the revisioned serverless container release configuration and prove it can move production to the newest ready version and retire the preceding active version. Which sequence is coherent?

- **A — Incorrect.** First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights.
  First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights. This revisioned serverless container release pair serves revision traffic splitting. Revisioned serverless container release uses revision traffic splitting for both steps; single revision mode remains untouched in revisioned serverless container release, so its single revision mode gate to move production to the newest ready version and retire the preceding active version fails.
- **B — Correct.** First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
  For the revisioned serverless container release, the safe single revision mode order is: first, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active. The revisioned serverless container release records single revision mode proof after configuration.
- **C — Incorrect.** First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.
  First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand. This revisioned serverless container release pair serves event-driven scale rules. Event-driven scale rules cannot replace single revision mode in revisioned serverless container release. Use this single revision mode pair instead: First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
- **D — Incorrect.** First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value.
  First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value. This revisioned serverless container release pair serves Container Apps secrets. Revisioned serverless container release proves Container Apps secrets, but single revision mode lacks implementation in revisioned serverless container release and single revision mode proof; the single revision mode outcome to move production to the newest ready version and retire the preceding active version remains open.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q44 — B

**Question:** The platform administrator releasing a revisioned serverless container app needs a safe revisioned serverless container release change to keep several versions active at the same time, followed by revision rollout evidence. Which pair merits approval?

- **A — Incorrect.** First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration.
  First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration. This revisioned serverless container release pair serves ingress target ports. Revisioned serverless container release closes ingress target ports, not multiple revision mode; without the multiple revision mode workflow, it cannot keep several versions active at the same time.
- **B — Correct.** First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100.
  First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100. The revisioned serverless container release uses its multiple revision mode mutation gate and multiple revision mode verification gate before it can keep several versions active at the same time.
- **C — Incorrect.** First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value.
  First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value. This revisioned serverless container release pair serves Container Apps secrets. Revisioned serverless container release proves Container Apps secrets, but multiple revision mode lacks implementation in revisioned serverless container release and multiple revision mode proof; the multiple revision mode outcome to keep several versions active at the same time remains open.
- **D — Incorrect.** First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
  First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration. This revisioned serverless container release pair serves Container Apps environments. Revisioned serverless container release uses Container Apps environments for both steps; multiple revision mode remains untouched in revisioned serverless container release, so its multiple revision mode gate to keep several versions active at the same time fails.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q45 — A

**Question:** The revisioned serverless container release has two revision rollout gates: send controlled percentages of requests to two active versions, then prove the revisioned serverless container release state. Which revision rollout sequence works?

- **A — Correct.** First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights.
  The revisioned serverless container release gets a complete revision traffic splitting sequence here: first, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights. Read-back evidence follows the change.
- **B — Incorrect.** First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
  First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location. This revisioned serverless container release pair serves external and internal ingress. Revisioned serverless container release proves external and internal ingress, but revision traffic splitting lacks implementation in revisioned serverless container release and revision traffic splitting proof; the revision traffic splitting outcome to send controlled percentages of requests to two active versions remains open.
- **C — Incorrect.** First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
  First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration. This revisioned serverless container release pair serves Container Apps environments. Revisioned serverless container release uses Container Apps environments for both steps; revision traffic splitting remains untouched in revisioned serverless container release, so its revision traffic splitting gate to send controlled percentages of requests to two active versions fails.
- **D — Incorrect.** First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.
  First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight. This revisioned serverless container release pair serves immutable revisions. Revisioned serverless container release closes immutable revisions, not revision traffic splitting; without the revision traffic splitting workflow, it cannot send controlled percentages of requests to two active versions.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

**Source reviewed:** 2026-08-31

## LAB14-Q46 — D

**Question:** Which revision rollout path makes the revisioned serverless container release able to route ingress to the port on which the container process actually listens, then inspects the defining properties?

- **A — Incorrect.** First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.
  First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count. This revisioned serverless container release pair serves minimum and maximum replicas. Revisioned serverless container release proves minimum and maximum replicas, but ingress target ports lacks implementation in revisioned serverless container release and ingress target ports proof; the ingress target ports outcome to route ingress to the port on which the container process actually listens remains open.
- **B — Incorrect.** First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.
  First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight. This revisioned serverless container release pair serves immutable revisions. Revisioned serverless container release uses immutable revisions for both steps; ingress target ports remains untouched in revisioned serverless container release, so its ingress target ports gate to route ingress to the port on which the container process actually listens fails.
- **C — Incorrect.** First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
  First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active. This revisioned serverless container release pair serves single revision mode. Revisioned serverless container release closes single revision mode, not ingress target ports; without the ingress target ports workflow, it cannot route ingress to the port on which the container process actually listens.
- **D — Correct.** First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration.
  First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration. This ordered ingress target ports workflow lets the revisioned serverless container release route ingress to the port on which the container process actually listens and then verify the resulting state.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB14-CP01`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q47 — A

**Question:** At the revisioned serverless container release approval gate, operators must show that the revision rollout can choose whether the application endpoint is externally reachable or environment-internal. Which revision rollout configure-and-check pair is defensible?

- **A — Correct.** First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
  First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location. For revisioned serverless container release, the external and internal ingress operation precedes its external and internal ingress read-back check, allowing it to choose whether the application endpoint is externally reachable or environment-internal.
- **B — Incorrect.** First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.
  First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand. This revisioned serverless container release pair serves event-driven scale rules. Revisioned serverless container release closes event-driven scale rules, not external and internal ingress; without the external and internal ingress workflow, it cannot choose whether the application endpoint is externally reachable or environment-internal.
- **C — Incorrect.** First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
  First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active. This revisioned serverless container release pair serves single revision mode. Single revision mode cannot replace external and internal ingress in revisioned serverless container release. Use this external and internal ingress pair instead: First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
- **D — Incorrect.** First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100.
  First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100. This revisioned serverless container release pair serves multiple revision mode. Revisioned serverless container release proves multiple revision mode, but external and internal ingress lacks implementation in revisioned serverless container release and external and internal ingress proof; the external and internal ingress outcome to choose whether the application endpoint is externally reachable or environment-internal remains open.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB14-CP02`).

**Microsoft Learn sources:**

- [Azure Container Apps ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview)

**Source reviewed:** 2026-08-31

## LAB14-Q48 — D

**Question:** The revisioned serverless container release forbids a partial revision rollout result. Operators must first keep required warm capacity while setting an upper scale limit and afterward confirm the revisioned serverless container release outcome. Which revision rollout sequence is complete?

- **A — Incorrect.** First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value.
  First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value. This revisioned serverless container release pair serves Container Apps secrets. Revisioned serverless container release closes Container Apps secrets, not minimum and maximum replicas; without the minimum and maximum replicas workflow, it cannot keep required warm capacity while setting an upper scale limit.
- **B — Incorrect.** First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100.
  First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100. This revisioned serverless container release pair serves multiple revision mode. Multiple revision mode cannot replace minimum and maximum replicas in revisioned serverless container release. Use this minimum and maximum replicas pair instead: First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.
- **C — Incorrect.** First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights.
  First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights. This revisioned serverless container release pair serves revision traffic splitting. Revisioned serverless container release proves revision traffic splitting, but minimum and maximum replicas lacks implementation in revisioned serverless container release and minimum and maximum replicas proof; the minimum and maximum replicas outcome to keep required warm capacity while setting an upper scale limit remains open.
- **D — Correct.** First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.
  First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count. In the revisioned serverless container release, the first minimum and maximum replicas step runs; the revisioned serverless container release then reads minimum and maximum replicas state to prove it can keep required warm capacity while setting an upper scale limit.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB14-CP03`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q49 — C

**Question:** Only the revisioned serverless container release change needed to translate HTTP or event demand into a desired replica count is allowed, and revision rollout proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
  First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration. This revisioned serverless container release pair serves Container Apps environments. Container Apps environments cannot replace event-driven scale rules in revisioned serverless container release. Use this event-driven scale rules pair instead: First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.
- **B — Incorrect.** First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights.
  First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights. This revisioned serverless container release pair serves revision traffic splitting. Revisioned serverless container release proves revision traffic splitting, but event-driven scale rules lacks implementation in revisioned serverless container release and event-driven scale rules proof; the event-driven scale rules outcome to translate HTTP or event demand into a desired replica count remains open.
- **C — Correct.** First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.
  For the revisioned serverless container release, the safe event-driven scale rules order is: first, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand. The revisioned serverless container release records event-driven scale rules proof after configuration.
- **D — Incorrect.** First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration.
  First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration. This revisioned serverless container release pair serves ingress target ports. Revisioned serverless container release closes ingress target ports, not event-driven scale rules; without the event-driven scale rules workflow, it cannot translate HTTP or event demand into a desired replica count.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB14-CP04`).

**Microsoft Learn sources:**

- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

**Source reviewed:** 2026-08-31

## LAB14-Q50 — D

**Question:** The revisioned serverless container release runbook separates revision rollout mutation from validation while it must reference sensitive configuration without placing the clear value in ordinary settings. Which sequence proves it cleanly?

- **A — Incorrect.** First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.
  First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight. This revisioned serverless container release pair serves immutable revisions. Revisioned serverless container release proves immutable revisions, but Container Apps secrets lacks implementation in revisioned serverless container release and Container Apps secrets proof; the Container Apps secrets outcome to reference sensitive configuration without placing the clear value in ordinary settings remains open.
- **B — Incorrect.** First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration.
  First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration. This revisioned serverless container release pair serves ingress target ports. Revisioned serverless container release uses ingress target ports for both steps; Container Apps secrets remains untouched in revisioned serverless container release, so its Container Apps secrets gate to reference sensitive configuration without placing the clear value in ordinary settings fails.
- **C — Incorrect.** First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
  First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location. This revisioned serverless container release pair serves external and internal ingress. Revisioned serverless container release closes external and internal ingress, not Container Apps secrets; without the Container Apps secrets workflow, it cannot reference sensitive configuration without placing the clear value in ordinary settings.
- **D — Correct.** First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value.
  First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value. The revisioned serverless container release uses its Container Apps secrets mutation gate and Container Apps secrets verification gate before it can reference sensitive configuration without placing the clear value in ordinary settings.

**Objectives:** `CP-CONTAINERS-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB14-CP05`).

**Microsoft Learn sources:**

- [Manage secrets in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets)

**Source reviewed:** 2026-08-31
