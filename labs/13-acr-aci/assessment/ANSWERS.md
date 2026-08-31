# Lab 13 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB13-Q01 — A

**Question:** The approved container image release acceptance criteria require operators to choose registry capabilities and throughput appropriate for the image workload. Which service fact supports that requirement?

- **A — Correct.** ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
  The approved container image release needs container registry service tiers to choose registry capabilities and throughput appropriate for the image workload; this option states the applicable container registry service tiers rule: aCR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
- **B — Incorrect.** An image tag is a mutable label, while a manifest digest identifies immutable image content.
  An image tag is a mutable label, while a manifest digest identifies immutable image content. In the approved container image release, this statement describes repository tags and digests. The repository tags and digests statement accurately describes repository tags and digests; however, approved container image release needs container registry service tiers to choose registry capabilities and throughput appropriate for the image workload; repository tags and digests cannot replace container registry service tiers.
- **C — Incorrect.** An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes.
  An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes. In the approved container image release, this statement describes container groups. Selecting container groups for approved container image release leaves container registry service tiers unanswered in approved container image release; the approved container image release lacks a container registry service tiers basis to choose registry capabilities and throughput appropriate for the image workload.
- **D — Incorrect.** Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively.
  Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively. In the approved container image release, this statement describes ACI restart policies. Container registry service tiers governs approved container image release; ACI restart policies cannot support container registry service tiers when operators must choose registry capabilities and throughput appropriate for the image workload.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Azure Container Registry service tiers](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus)

**Source reviewed:** 2026-08-31

## LAB13-Q02 — D

**Question:** An image release reviewer challenges whether the approved container image release can deploy by digest so later tag changes cannot move the release. Which response resolves the concern?

- **A — Incorrect.** A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository.
  A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository. In the approved container image release, this statement describes registry pull authorization. The registry pull authorization statement accurately describes registry pull authorization; however, approved container image release needs repository tags and digests to deploy by digest so later tag changes cannot move the release; registry pull authorization cannot replace repository tags and digests.
- **B — Incorrect.** A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint.
  A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint. In the approved container image release, this statement describes ACI DNS labels. Selecting ACI DNS labels for approved container image release leaves repository tags and digests unanswered in approved container image release; the approved container image release lacks a repository tags and digests basis to deploy by digest so later tag changes cannot move the release.
- **C — Incorrect.** ACI CPU and memory requests are specified per container and determine scheduling support and cost.
  ACI CPU and memory requests are specified per container and determine scheduling support and cost. In the approved container image release, this statement describes ACI resource sizing. Repository tags and digests governs approved container image release; ACI resource sizing cannot support repository tags and digests when operators must deploy by digest so later tag changes cannot move the release.
- **D — Correct.** An image tag is a mutable label, while a manifest digest identifies immutable image content.
  An image tag is a mutable label, while a manifest digest identifies immutable image content. This repository tags and digests fact resolves the approved container image release design question about how to deploy by digest so later tag changes cannot move the release.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Container image tags and versioning](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-image-tag-version)

**Source reviewed:** 2026-08-31

## LAB13-Q03 — C

**Question:** The approved container image release handoff omits the image release rule needed to let the runtime pull a private image without embedding an administrator password. Which statement should the team add?

- **A — Incorrect.** ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push.
  ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push. In the approved container image release, this statement describes server-side image import. Selecting server-side image import for approved container image release leaves registry pull authorization unanswered in approved container image release; the approved container image release lacks a registry pull authorization basis to let the runtime pull a private image without embedding an administrator password.
- **B — Incorrect.** ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
  ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling. In the approved container image release, this statement describes container environment secrets. Registry pull authorization governs approved container image release; container environment secrets cannot support registry pull authorization when operators must let the runtime pull a private image without embedding an administrator password.
- **C — Correct.** A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository.
  A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository. For approved container image release, registry pull authorization supplies the service rule needed to let the runtime pull a private image without embedding an administrator password.
- **D — Incorrect.** The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization.
  The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization. In the approved container image release, this statement describes registry credentials versus identity. The registry credentials versus identity statement accurately describes registry credentials versus identity; however, approved container image release needs registry pull authorization to let the runtime pull a private image without embedding an administrator password; registry credentials versus identity cannot replace registry pull authorization.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q04 — D

**Question:** An image release incident review of the approved container image release depends on the ability to copy an existing image into the registry without a local pull and push. Which platform description is reliable?

- **A — Incorrect.** An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes.
  An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes. In the approved container image release, this statement describes container groups. Server-side image import governs approved container image release; container groups cannot support server-side image import when operators must copy an existing image into the registry without a local pull and push.
- **B — Incorrect.** Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively.
  Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively. In the approved container image release, this statement describes ACI restart policies. Approved container image release asks about server-side image import; this ACI restart policies choice leaves the server-side image import explanation missing.
- **C — Incorrect.** ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
  ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features. In the approved container image release, this statement describes container registry service tiers. The container registry service tiers statement accurately describes container registry service tiers; however, approved container image release needs server-side image import to copy an existing image into the registry without a local pull and push; container registry service tiers cannot replace server-side image import.
- **D — Correct.** ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push.
  ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push. In the approved container image release, this server-side image import rule supports the need to copy an existing image into the registry without a local pull and push.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Import container images into a registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images)

**Source reviewed:** 2026-08-31

## LAB13-Q05 — B

**Question:** A container administrator publishing an approved image and running it in ACI is updating the image release runbook. The requirement is to run sidecars inside one jointly managed execution unit. Which statement describes Azure behavior correctly?

- **A — Incorrect.** A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint.
  A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint. In the approved container image release, this statement describes ACI DNS labels. Approved container image release asks about container groups; this ACI DNS labels choice leaves the container groups explanation missing.
- **B — Correct.** An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes.
  For the approved container image release, the rule for container groups is defined by this statement: an ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes. It supports the required outcome to run sidecars inside one jointly managed execution unit.
- **C — Incorrect.** ACI CPU and memory requests are specified per container and determine scheduling support and cost.
  ACI CPU and memory requests are specified per container and determine scheduling support and cost. In the approved container image release, this statement describes ACI resource sizing. Selecting ACI resource sizing for approved container image release leaves container groups unanswered in approved container image release; the approved container image release lacks a container groups basis to run sidecars inside one jointly managed execution unit.
- **D — Incorrect.** An image tag is a mutable label, while a manifest digest identifies immutable image content.
  An image tag is a mutable label, while a manifest digest identifies immutable image content. In the approved container image release, this statement describes repository tags and digests. Container groups governs approved container image release; repository tags and digests cannot support container groups when operators must run sidecars inside one jointly managed execution unit.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Azure Container Instances container groups](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-groups)

**Source reviewed:** 2026-08-31

## LAB13-Q06 — B

**Question:** An image release peer review asks how the approved container image release should handle this outcome: publish a stable regional name for the container group's public endpoint. Which explanation is accurate?

- **A — Incorrect.** ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
  ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling. In the approved container image release, this statement describes container environment secrets. The container environment secrets statement accurately describes container environment secrets; however, approved container image release needs ACI DNS labels to publish a stable regional name for the container group's public endpoint; container environment secrets cannot replace ACI DNS labels.
- **B — Correct.** A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint.
  A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint. The approved container image release applies that ACI DNS labels boundary when operators must publish a stable regional name for the container group's public endpoint.
- **C — Incorrect.** The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization.
  The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization. In the approved container image release, this statement describes registry credentials versus identity. ACI DNS labels governs approved container image release; registry credentials versus identity cannot support ACI DNS labels when operators must publish a stable regional name for the container group's public endpoint.
- **D — Incorrect.** A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository.
  A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository. In the approved container image release, this statement describes registry pull authorization. Approved container image release asks about ACI DNS labels; this registry pull authorization choice leaves the ACI DNS labels explanation missing.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Create a container instance with Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart)

**Source reviewed:** 2026-08-31

## LAB13-Q07 — A

**Question:** For the approved container image release, the image release plan must pass sensitive configuration without writing the clear value into ordinary output. Which statement about image release belongs in the approved container image release record?

- **A — Correct.** ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
  The approved container image release needs container environment secrets to pass sensitive configuration without writing the clear value into ordinary output; this option states the applicable container environment secrets rule: aCI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
- **B — Incorrect.** Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively.
  Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively. In the approved container image release, this statement describes ACI restart policies. Container environment secrets governs approved container image release; ACI restart policies cannot support container environment secrets when operators must pass sensitive configuration without writing the clear value into ordinary output.
- **C — Incorrect.** ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
  ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features. In the approved container image release, this statement describes container registry service tiers. Approved container image release asks about container environment secrets; this container registry service tiers choice leaves the container environment secrets explanation missing.
- **D — Incorrect.** ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push.
  ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push. In the approved container image release, this statement describes server-side image import. The server-side image import statement accurately describes server-side image import; however, approved container image release needs container environment secrets to pass sensitive configuration without writing the clear value into ordinary output; server-side image import cannot replace container environment secrets.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Set environment variables in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-environment-variables)

**Source reviewed:** 2026-08-31

## LAB13-Q08 — D

**Question:** The image release review compares four claims for the approved container image release requirement to control whether a terminated container restarts. Which claim is technically sound?

- **A — Incorrect.** ACI CPU and memory requests are specified per container and determine scheduling support and cost.
  ACI CPU and memory requests are specified per container and determine scheduling support and cost. In the approved container image release, this statement describes ACI resource sizing. ACI restart policies governs approved container image release; ACI resource sizing cannot support ACI restart policies when operators must control whether a terminated container restarts.
- **B — Incorrect.** An image tag is a mutable label, while a manifest digest identifies immutable image content.
  An image tag is a mutable label, while a manifest digest identifies immutable image content. In the approved container image release, this statement describes repository tags and digests. Approved container image release asks about ACI restart policies; this repository tags and digests choice leaves the ACI restart policies explanation missing.
- **C — Incorrect.** An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes.
  An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes. In the approved container image release, this statement describes container groups. The container groups statement accurately describes container groups; however, approved container image release needs ACI restart policies to control whether a terminated container restarts; container groups cannot replace ACI restart policies.
- **D — Correct.** Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively.
  Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively. This ACI restart policies fact resolves the approved container image release design question about how to control whether a terminated container restarts.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Azure Container Instances restart policies](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-restart-policy)

**Source reviewed:** 2026-08-31

## LAB13-Q09 — D

**Question:** The image release architecture note requires the approved container image release environment to request CPU and memory values supported in the selected region. Which statement defines the relevant image release boundary?

- **A — Incorrect.** The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization.
  The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization. In the approved container image release, this statement describes registry credentials versus identity. Approved container image release asks about ACI resource sizing; this registry credentials versus identity choice leaves the ACI resource sizing explanation missing.
- **B — Incorrect.** A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository.
  A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository. In the approved container image release, this statement describes registry pull authorization. The registry pull authorization statement accurately describes registry pull authorization; however, approved container image release needs ACI resource sizing to request CPU and memory values supported in the selected region; registry pull authorization cannot replace ACI resource sizing.
- **C — Incorrect.** A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint.
  A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint. In the approved container image release, this statement describes ACI DNS labels. Selecting ACI DNS labels for approved container image release leaves ACI resource sizing unanswered in approved container image release; the approved container image release lacks a ACI resource sizing basis to request CPU and memory values supported in the selected region.
- **D — Correct.** ACI CPU and memory requests are specified per container and determine scheduling support and cost.
  ACI CPU and memory requests are specified per container and determine scheduling support and cost. For approved container image release, ACI resource sizing supplies the service rule needed to request CPU and memory values supported in the selected region.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Azure Container Instances resource availability](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability)

**Source reviewed:** 2026-08-31

## LAB13-Q10 — D

**Question:** A new image release operator must explain why the approved container image release can prefer an identity-scoped image pull over long-lived registry credentials. Which explanation is accurate?

- **A — Incorrect.** ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
  ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features. In the approved container image release, this statement describes container registry service tiers. The container registry service tiers statement accurately describes container registry service tiers; however, approved container image release needs registry credentials versus identity to prefer an identity-scoped image pull over long-lived registry credentials; container registry service tiers cannot replace registry credentials versus identity.
- **B — Incorrect.** ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push.
  ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push. In the approved container image release, this statement describes server-side image import. Selecting server-side image import for approved container image release leaves registry credentials versus identity unanswered in approved container image release; the approved container image release lacks a registry credentials versus identity basis to prefer an identity-scoped image pull over long-lived registry credentials.
- **C — Incorrect.** ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
  ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling. In the approved container image release, this statement describes container environment secrets. Registry credentials versus identity governs approved container image release; container environment secrets cannot support registry credentials versus identity when operators must prefer an identity-scoped image pull over long-lived registry credentials.
- **D — Correct.** The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization.
  The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization. In the approved container image release, this registry credentials versus identity rule supports the need to prefer an identity-scoped image pull over long-lived registry credentials.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q11 — C

**Question:** An approved container image release review finds image release drift from the need to choose registry capabilities and throughput appropriate for the image workload. Which correction addresses that drift?

- **A — Incorrect.** Assign the pull role to the workload identity and reference the private registry without embedding a password.
  Assign the pull role to the workload identity and reference the private registry without embedding a password. In the approved container image release, this action changes registry pull authorization. Approved container image release approved container registry service tiers, not registry pull authorization; only the container registry service tiers change can choose registry capabilities and throughput appropriate for the image workload.
- **B — Incorrect.** Check label availability and configure the DNS name label only for a deliberately public container group.
  Check label availability and configure the DNS name label only for a deliberately public container group. In the approved container image release, this action changes ACI DNS labels. Approved container image release requires container registry service tiers; changing ACI DNS labels leaves container registry service tiers absent in approved container image release; approved container image release cannot choose registry capabilities and throughput appropriate for the image workload.
- **C — Correct.** Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements.
  For the approved container image release, the required container registry service tiers action is: choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. It makes the environment able to choose registry capabilities and throughput appropriate for the image workload.
- **D — Incorrect.** Set explicit CPU and memory requests within the selected region's supported combinations.
  Set explicit CPU and memory requests within the selected region's supported combinations. In the approved container image release, this action changes ACI resource sizing. Approved container image release instead needs container registry service tiers: Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. The ACI resource sizing action omits that container registry service tiers work.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Azure Container Registry service tiers](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus)

**Source reviewed:** 2026-08-31

## LAB13-Q12 — B

**Question:** The approved container image release window permits only the image release change needed to deploy by digest so later tag changes cannot move the release. Which option respects the boundary?

- **A — Incorrect.** Import the approved source image into a uniquely versioned target repository and tag.
  Import the approved source image into a uniquely versioned target repository and tag. In the approved container image release, this action changes server-side image import. Approved container image release requires repository tags and digests; changing server-side image import leaves repository tags and digests absent in approved container image release; approved container image release cannot deploy by digest so later tag changes cannot move the release.
- **B — Correct.** Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence.
  Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. This changes repository tags and digests in the approved container image release, supplying the missing state needed to deploy by digest so later tag changes cannot move the release.
- **C — Incorrect.** Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files.
  Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. In the approved container image release, this action changes container environment secrets. Approved container image release instead needs repository tags and digests: Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. The container environment secrets action omits that repository tags and digests work.
- **D — Incorrect.** Prefer managed identity for the container pull path and leave the registry admin account disabled.
  Prefer managed identity for the container pull path and leave the registry admin account disabled. In the approved container image release, this action changes registry credentials versus identity. Approved container image release approved repository tags and digests, not registry credentials versus identity; only the repository tags and digests change can deploy by digest so later tag changes cannot move the release.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Container image tags and versioning](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-image-tag-version)

**Source reviewed:** 2026-08-31

## LAB13-Q13 — C

**Question:** The image release preflight has passed; the approved container image release must now let the runtime pull a private image without embedding an administrator password. Which operation should run?

- **A — Incorrect.** Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace.
  Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. In the approved container image release, this action changes container groups. Container groups does not implement registry pull authorization for approved container image release; the approved container image release still cannot let the runtime pull a private image without embedding an administrator password.
- **B — Incorrect.** Set the restart policy from the workload's intended lifecycle and exit-code behavior.
  Set the restart policy from the workload's intended lifecycle and exit-code behavior. In the approved container image release, this action changes ACI restart policies. Approved container image release instead needs registry pull authorization: Assign the pull role to the workload identity and reference the private registry without embedding a password. The ACI restart policies action omits that registry pull authorization work.
- **C — Correct.** Assign the pull role to the workload identity and reference the private registry without embedding a password.
  The approved container image release must let the runtime pull a private image without embedding an administrator password; this option performs its direct registry pull authorization change: assign the pull role to the workload identity and reference the private registry without embedding a password.
- **D — Incorrect.** Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements.
  Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. In the approved container image release, this action changes container registry service tiers. Approved container image release requires registry pull authorization; changing container registry service tiers leaves registry pull authorization absent in approved container image release; approved container image release cannot let the runtime pull a private image without embedding an administrator password.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q14 — D

**Question:** The approved container image release plan must copy an existing image into the registry without a local pull and push while limiting the mutation scope to image release. Which action is appropriate?

- **A — Incorrect.** Check label availability and configure the DNS name label only for a deliberately public container group.
  Check label availability and configure the DNS name label only for a deliberately public container group. In the approved container image release, this action changes ACI DNS labels. Approved container image release instead needs server-side image import: Import the approved source image into a uniquely versioned target repository and tag. The ACI DNS labels action omits that server-side image import work.
- **B — Incorrect.** Set explicit CPU and memory requests within the selected region's supported combinations.
  Set explicit CPU and memory requests within the selected region's supported combinations. In the approved container image release, this action changes ACI resource sizing. Approved container image release approved server-side image import, not ACI resource sizing; only the server-side image import change can copy an existing image into the registry without a local pull and push.
- **C — Incorrect.** Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence.
  Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. In the approved container image release, this action changes repository tags and digests. Approved container image release requires server-side image import; changing repository tags and digests leaves server-side image import absent in approved container image release; approved container image release cannot copy an existing image into the registry without a local pull and push.
- **D — Correct.** Import the approved source image into a uniquely versioned target repository and tag.
  Import the approved source image into a uniquely versioned target repository and tag. It is the least-change server-side image import path for the approved container image release requirement to copy an existing image into the registry without a local pull and push.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Import container images into a registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images)

**Source reviewed:** 2026-08-31

## LAB13-Q15 — D

**Question:** An image release ticket in the approved container image release says to run sidecars inside one jointly managed execution unit. Which image release action completes the approved container image release request with minimal change?

- **A — Incorrect.** Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files.
  Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. In the approved container image release, this action changes container environment secrets. Approved container image release approved container groups, not container environment secrets; only the container groups change can run sidecars inside one jointly managed execution unit.
- **B — Incorrect.** Prefer managed identity for the container pull path and leave the registry admin account disabled.
  Prefer managed identity for the container pull path and leave the registry admin account disabled. In the approved container image release, this action changes registry credentials versus identity. Approved container image release requires container groups; changing registry credentials versus identity leaves container groups absent in approved container image release; approved container image release cannot run sidecars inside one jointly managed execution unit.
- **C — Incorrect.** Assign the pull role to the workload identity and reference the private registry without embedding a password.
  Assign the pull role to the workload identity and reference the private registry without embedding a password. In the approved container image release, this action changes registry pull authorization. Registry pull authorization does not implement container groups for approved container image release; the approved container image release still cannot run sidecars inside one jointly managed execution unit.
- **D — Correct.** Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace.
  Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. In approved container image release, applying container groups is the scoped way to run sidecars inside one jointly managed execution unit.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Azure Container Instances container groups](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-groups)

**Source reviewed:** 2026-08-31

## LAB13-Q16 — C

**Question:** The approach for the approved container image release is approved, but the image release environment still cannot publish a stable regional name for the container group's public endpoint. Which implementation step closes the gap?

- **A — Incorrect.** Set the restart policy from the workload's intended lifecycle and exit-code behavior.
  Set the restart policy from the workload's intended lifecycle and exit-code behavior. In the approved container image release, this action changes ACI restart policies. Approved container image release requires ACI DNS labels; changing ACI restart policies leaves ACI DNS labels absent in approved container image release; approved container image release cannot publish a stable regional name for the container group's public endpoint.
- **B — Incorrect.** Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements.
  Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. In the approved container image release, this action changes container registry service tiers. Container registry service tiers does not implement ACI DNS labels for approved container image release; the approved container image release still cannot publish a stable regional name for the container group's public endpoint.
- **C — Correct.** Check label availability and configure the DNS name label only for a deliberately public container group.
  Check label availability and configure the DNS name label only for a deliberately public container group. The approved container image release uses this ACI DNS labels operation to publish a stable regional name for the container group's public endpoint within the approved scope.
- **D — Incorrect.** Import the approved source image into a uniquely versioned target repository and tag.
  Import the approved source image into a uniquely versioned target repository and tag. In the approved container image release, this action changes server-side image import. Approved container image release approved ACI DNS labels, not server-side image import; only the ACI DNS labels change can publish a stable regional name for the container group's public endpoint.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Create a container instance with Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart)

**Source reviewed:** 2026-08-31

## LAB13-Q17 — A

**Question:** The container administrator publishing an approved image and running it in ACI may change the approved container image release only to pass sensitive configuration without writing the clear value into ordinary output. Which image release action stays within that assignment?

- **A — Correct.** Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files.
  For the approved container image release, the required container environment secrets action is: pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. It makes the environment able to pass sensitive configuration without writing the clear value into ordinary output.
- **B — Incorrect.** Set explicit CPU and memory requests within the selected region's supported combinations.
  Set explicit CPU and memory requests within the selected region's supported combinations. In the approved container image release, this action changes ACI resource sizing. Approved container image release instead needs container environment secrets: Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. The ACI resource sizing action omits that container environment secrets work.
- **C — Incorrect.** Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence.
  Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. In the approved container image release, this action changes repository tags and digests. Approved container image release approved container environment secrets, not repository tags and digests; only the container environment secrets change can pass sensitive configuration without writing the clear value into ordinary output.
- **D — Incorrect.** Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace.
  Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. In the approved container image release, this action changes container groups. Approved container image release requires container environment secrets; changing container groups leaves container environment secrets absent in approved container image release; approved container image release cannot pass sensitive configuration without writing the clear value into ordinary output.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Set environment variables in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-environment-variables)

**Source reviewed:** 2026-08-31

## LAB13-Q18 — B

**Question:** An image release dry run shows no approved container image release command will control whether a terminated container restarts. Which action belongs before execution?

- **A — Incorrect.** Prefer managed identity for the container pull path and leave the registry admin account disabled.
  Prefer managed identity for the container pull path and leave the registry admin account disabled. In the approved container image release, this action changes registry credentials versus identity. Approved container image release instead needs ACI restart policies: Set the restart policy from the workload's intended lifecycle and exit-code behavior. The registry credentials versus identity action omits that ACI restart policies work.
- **B — Correct.** Set the restart policy from the workload's intended lifecycle and exit-code behavior.
  Set the restart policy from the workload's intended lifecycle and exit-code behavior. This changes ACI restart policies in the approved container image release, supplying the missing state needed to control whether a terminated container restarts.
- **C — Incorrect.** Assign the pull role to the workload identity and reference the private registry without embedding a password.
  Assign the pull role to the workload identity and reference the private registry without embedding a password. In the approved container image release, this action changes registry pull authorization. Approved container image release requires ACI restart policies; changing registry pull authorization leaves ACI restart policies absent in approved container image release; approved container image release cannot control whether a terminated container restarts.
- **D — Incorrect.** Check label availability and configure the DNS name label only for a deliberately public container group.
  Check label availability and configure the DNS name label only for a deliberately public container group. In the approved container image release, this action changes ACI DNS labels. ACI DNS labels does not implement ACI restart policies for approved container image release; the approved container image release still cannot control whether a terminated container restarts.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Azure Container Instances restart policies](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-restart-policy)

**Source reviewed:** 2026-08-31

## LAB13-Q19 — D

**Question:** For the approved container image release, operators need to request CPU and memory values supported in the selected region. Which change realizes that requirement?

- **A — Incorrect.** Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements.
  Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. In the approved container image release, this action changes container registry service tiers. Approved container image release approved ACI resource sizing, not container registry service tiers; only the ACI resource sizing change can request CPU and memory values supported in the selected region.
- **B — Incorrect.** Import the approved source image into a uniquely versioned target repository and tag.
  Import the approved source image into a uniquely versioned target repository and tag. In the approved container image release, this action changes server-side image import. Approved container image release requires ACI resource sizing; changing server-side image import leaves ACI resource sizing absent in approved container image release; approved container image release cannot request CPU and memory values supported in the selected region.
- **C — Incorrect.** Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files.
  Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. In the approved container image release, this action changes container environment secrets. Container environment secrets does not implement ACI resource sizing for approved container image release; the approved container image release still cannot request CPU and memory values supported in the selected region.
- **D — Correct.** Set explicit CPU and memory requests within the selected region's supported combinations.
  The approved container image release must request CPU and memory values supported in the selected region; this option performs its direct ACI resource sizing change: set explicit CPU and memory requests within the selected region's supported combinations.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Azure Container Instances resource availability](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability)

**Source reviewed:** 2026-08-31

## LAB13-Q20 — D

**Question:** Operators must automate the approved container image release change needed to prefer an identity-scoped image pull over long-lived registry credentials. Which image release operation belongs in the runbook?

- **A — Incorrect.** Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence.
  Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. In the approved container image release, this action changes repository tags and digests. Approved container image release requires registry credentials versus identity; changing repository tags and digests leaves registry credentials versus identity absent in approved container image release; approved container image release cannot prefer an identity-scoped image pull over long-lived registry credentials.
- **B — Incorrect.** Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace.
  Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. In the approved container image release, this action changes container groups. Container groups does not implement registry credentials versus identity for approved container image release; the approved container image release still cannot prefer an identity-scoped image pull over long-lived registry credentials.
- **C — Incorrect.** Set the restart policy from the workload's intended lifecycle and exit-code behavior.
  Set the restart policy from the workload's intended lifecycle and exit-code behavior. In the approved container image release, this action changes ACI restart policies. Approved container image release instead needs registry credentials versus identity: Prefer managed identity for the container pull path and leave the registry admin account disabled. The ACI restart policies action omits that registry credentials versus identity work.
- **D — Correct.** Prefer managed identity for the container pull path and leave the registry admin account disabled.
  Prefer managed identity for the container pull path and leave the registry admin account disabled. It is the least-change registry credentials versus identity path for the approved container image release requirement to prefer an identity-scoped image pull over long-lived registry credentials.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q21 — B

**Question:** The image release validation asks whether the approved container image release can choose registry capabilities and throughput appropriate for the image workload. Which observable state is strongest?

- **A — Incorrect.** List the target repository and verify its tag, digest, and import timestamp.
  List the target repository and verify its tag, digest, and import timestamp. In the approved container image release, this check observes server-side image import. Approved container image release output covers server-side image import, not container registry service tiers; the container registry service tiers requirement to choose registry capabilities and throughput appropriate for the image workload remains unverified.
- **B — Correct.** Query sku.name, provisioningState, loginServer, and configured premium features.
  Query sku.name, provisioningState, loginServer, and configured premium features. For approved container image release, this container registry service tiers read confirms the service can choose registry capabilities and throughput appropriate for the image workload.
- **C — Incorrect.** Inspect the container definition and evidence output to confirm secret values are redacted.
  Inspect the container definition and evidence output to confirm secret values are redacted. In the approved container image release, this check observes container environment secrets. Approved container image release reads container environment secrets, leaving container registry service tiers unproved in approved container image release; approved container image release still has no container registry service tiers proof.
- **D — Incorrect.** Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
  Query adminUserEnabled and confirm the workload identity's scoped pull assignment. In the approved container image release, this check observes registry credentials versus identity. Approved container image release could pass registry credentials versus identity while container registry service tiers is wrong; approved container image release still lacks container registry service tiers proof.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Azure Container Registry service tiers](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus)

**Source reviewed:** 2026-08-31

## LAB13-Q22 — C

**Question:** An approved container image release review must prove the image release ability to deploy by digest so later tag changes cannot move the release. Which check avoids an adjacent feature?

- **A — Incorrect.** Query container group provisioningState, instanceView state, IP configuration, and each container status.
  Query container group provisioningState, instanceView state, IP configuration, and each container status. In the approved container image release, this check observes container groups. Container groups success in approved container image release cannot verify repository tags and digests; approved container image release cannot deploy by digest so later tag changes cannot move the release until repository tags and digests evidence exists.
- **B — Incorrect.** Query restartPolicy, currentState, previousState, exitCode, and restartCount.
  Query restartPolicy, currentState, previousState, exitCode, and restartCount. In the approved container image release, this check observes ACI restart policies. Approved container image release reads ACI restart policies, leaving repository tags and digests unproved in approved container image release; approved container image release still has no repository tags and digests proof.
- **C — Correct.** List repository manifests and match the selected tag to its sha256 digest.
  List repository manifests and match the selected tag to its sha256 digest. The approved container image release reads repository tags and digests directly; that repository tags and digests result proves the approved container image release can deploy by digest so later tag changes cannot move the release without another mutation.
- **D — Incorrect.** Query sku.name, provisioningState, loginServer, and configured premium features.
  Query sku.name, provisioningState, loginServer, and configured premium features. In the approved container image release, this check observes container registry service tiers. Approved container image release output covers container registry service tiers, not repository tags and digests; the repository tags and digests requirement to deploy by digest so later tag changes cannot move the release remains unverified.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Container image tags and versioning](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-image-tag-version)

**Source reviewed:** 2026-08-31

## LAB13-Q23 — A

**Question:** The approved container image release evidence bundle needs an image release result showing it can let the runtime pull a private image without embedding an administrator password. Which result belongs in the checkpoint?

- **A — Correct.** List the identity's role assignment and confirm the deployed image resolves from the private login server.
  For the approved container image release, this registry pull authorization observation is decisive: list the identity's role assignment and confirm the deployed image resolves from the private login server. It is approved container image release evidence that operators can let the runtime pull a private image without embedding an administrator password.
- **B — Incorrect.** Query ipAddress.fqdn, type, ports, and the container's running state.
  Query ipAddress.fqdn, type, ports, and the container's running state. In the approved container image release, this check observes ACI DNS labels. Approved container image release could pass ACI DNS labels while registry pull authorization is wrong; approved container image release still lacks registry pull authorization proof.
- **C — Incorrect.** Query each container's resources.requests and compare them with measured workload demand.
  Query each container's resources.requests and compare them with measured workload demand. In the approved container image release, this check observes ACI resource sizing. Approved container image release output covers ACI resource sizing, not registry pull authorization; the registry pull authorization requirement to let the runtime pull a private image without embedding an administrator password remains unverified.
- **D — Incorrect.** List repository manifests and match the selected tag to its sha256 digest.
  List repository manifests and match the selected tag to its sha256 digest. In the approved container image release, this check observes repository tags and digests. Repository tags and digests success in approved container image release cannot verify registry pull authorization; approved container image release cannot let the runtime pull a private image without embedding an administrator password until registry pull authorization evidence exists.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q24 — D

**Question:** Before approved container image release cleanup, the image release team must reconfirm it can copy an existing image into the registry without a local pull and push. Which read-only inspection should run?

- **A — Incorrect.** Inspect the container definition and evidence output to confirm secret values are redacted.
  Inspect the container definition and evidence output to confirm secret values are redacted. In the approved container image release, this check observes container environment secrets. Approved container image release could pass container environment secrets while server-side image import is wrong; approved container image release still lacks server-side image import proof.
- **B — Incorrect.** Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
  Query adminUserEnabled and confirm the workload identity's scoped pull assignment. In the approved container image release, this check observes registry credentials versus identity. Approved container image release output covers registry credentials versus identity, not server-side image import; the server-side image import requirement to copy an existing image into the registry without a local pull and push remains unverified.
- **C — Incorrect.** List the identity's role assignment and confirm the deployed image resolves from the private login server.
  List the identity's role assignment and confirm the deployed image resolves from the private login server. In the approved container image release, this check observes registry pull authorization. Registry pull authorization success in approved container image release cannot verify server-side image import; approved container image release cannot copy an existing image into the registry without a local pull and push until server-side image import evidence exists.
- **D — Correct.** List the target repository and verify its tag, digest, and import timestamp.
  List the target repository and verify its tag, digest, and import timestamp. Because the approved container image release check observes server-side image import, it independently verifies the requirement to copy an existing image into the registry without a local pull and push.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Import container images into a registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images)

**Source reviewed:** 2026-08-31

## LAB13-Q25 — B

**Question:** The approved container image release setup reports success after the image release attempt to run sidecars inside one jointly managed execution unit. Which image release read-only observation proves the approved container image release outcome?

- **A — Incorrect.** Query restartPolicy, currentState, previousState, exitCode, and restartCount.
  Query restartPolicy, currentState, previousState, exitCode, and restartCount. In the approved container image release, this check observes ACI restart policies. Approved container image release output covers ACI restart policies, not container groups; the container groups requirement to run sidecars inside one jointly managed execution unit remains unverified.
- **B — Correct.** Query container group provisioningState, instanceView state, IP configuration, and each container status.
  The approved container image release validator needs this container groups result: query container group provisioningState, instanceView state, IP configuration, and each container status. It proves the outcome to run sidecars inside one jointly managed execution unit rather than an adjacent checkpoint.
- **C — Incorrect.** Query sku.name, provisioningState, loginServer, and configured premium features.
  Query sku.name, provisioningState, loginServer, and configured premium features. In the approved container image release, this check observes container registry service tiers. Approved container image release reads container registry service tiers, leaving container groups unproved in approved container image release; approved container image release still has no container groups proof.
- **D — Incorrect.** List the target repository and verify its tag, digest, and import timestamp.
  List the target repository and verify its tag, digest, and import timestamp. In the approved container image release, this check observes server-side image import. Approved container image release could pass server-side image import while container groups is wrong; approved container image release still lacks container groups proof.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Azure Container Instances container groups](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-groups)

**Source reviewed:** 2026-08-31

## LAB13-Q26 — A

**Question:** The image release log says the approved container image release can now publish a stable regional name for the container group's public endpoint. Which image release state should the approved container image release acceptance test retain?

- **A — Correct.** Query ipAddress.fqdn, type, ports, and the container's running state.
  Query ipAddress.fqdn, type, ports, and the container's running state. This is independent ACI DNS labels evidence for the approved container image release, even if approved container image release setup reports success before ACI DNS labels becomes observable.
- **B — Incorrect.** Query each container's resources.requests and compare them with measured workload demand.
  Query each container's resources.requests and compare them with measured workload demand. In the approved container image release, this check observes ACI resource sizing. Approved container image release reads ACI resource sizing, leaving ACI DNS labels unproved in approved container image release; approved container image release still has no ACI DNS labels proof.
- **C — Incorrect.** List repository manifests and match the selected tag to its sha256 digest.
  List repository manifests and match the selected tag to its sha256 digest. In the approved container image release, this check observes repository tags and digests. Approved container image release could pass repository tags and digests while ACI DNS labels is wrong; approved container image release still lacks ACI DNS labels proof.
- **D — Incorrect.** Query container group provisioningState, instanceView state, IP configuration, and each container status.
  Query container group provisioningState, instanceView state, IP configuration, and each container status. In the approved container image release, this check observes container groups. Approved container image release output covers container groups, not ACI DNS labels; the ACI DNS labels requirement to publish a stable regional name for the container group's public endpoint remains unverified.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Create a container instance with Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart)

**Source reviewed:** 2026-08-31

## LAB13-Q27 — D

**Question:** The approved container image release rejects image release exit status as proof it can pass sensitive configuration without writing the clear value into ordinary output. Which approved container image release result is valid evidence?

- **A — Incorrect.** Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
  Query adminUserEnabled and confirm the workload identity's scoped pull assignment. In the approved container image release, this check observes registry credentials versus identity. Approved container image release reads registry credentials versus identity, leaving container environment secrets unproved in approved container image release; approved container image release still has no container environment secrets proof.
- **B — Incorrect.** List the identity's role assignment and confirm the deployed image resolves from the private login server.
  List the identity's role assignment and confirm the deployed image resolves from the private login server. In the approved container image release, this check observes registry pull authorization. Approved container image release could pass registry pull authorization while container environment secrets is wrong; approved container image release still lacks container environment secrets proof.
- **C — Incorrect.** Query ipAddress.fqdn, type, ports, and the container's running state.
  Query ipAddress.fqdn, type, ports, and the container's running state. In the approved container image release, this check observes ACI DNS labels. Approved container image release output covers ACI DNS labels, not container environment secrets; the container environment secrets requirement to pass sensitive configuration without writing the clear value into ordinary output remains unverified.
- **D — Correct.** Inspect the container definition and evidence output to confirm secret values are redacted.
  Inspect the container definition and evidence output to confirm secret values are redacted. For approved container image release, this container environment secrets read confirms the service can pass sensitive configuration without writing the clear value into ordinary output.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Set environment variables in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-environment-variables)

**Source reviewed:** 2026-08-31

## LAB13-Q28 — A

**Question:** The image release validator needs one approved container image release query after the change to control whether a terminated container restarts. Which image release property should the approved container image release validator inspect?

- **A — Correct.** Query restartPolicy, currentState, previousState, exitCode, and restartCount.
  Query restartPolicy, currentState, previousState, exitCode, and restartCount. The approved container image release reads ACI restart policies directly; that ACI restart policies result proves the approved container image release can control whether a terminated container restarts without another mutation.
- **B — Incorrect.** Query sku.name, provisioningState, loginServer, and configured premium features.
  Query sku.name, provisioningState, loginServer, and configured premium features. In the approved container image release, this check observes container registry service tiers. Approved container image release output covers container registry service tiers, not ACI restart policies; the ACI restart policies requirement to control whether a terminated container restarts remains unverified.
- **C — Incorrect.** List the target repository and verify its tag, digest, and import timestamp.
  List the target repository and verify its tag, digest, and import timestamp. In the approved container image release, this check observes server-side image import. Server-side image import success in approved container image release cannot verify ACI restart policies; approved container image release cannot control whether a terminated container restarts until ACI restart policies evidence exists.
- **D — Incorrect.** Inspect the container definition and evidence output to confirm secret values are redacted.
  Inspect the container definition and evidence output to confirm secret values are redacted. In the approved container image release, this check observes container environment secrets. Approved container image release reads container environment secrets, leaving ACI restart policies unproved in approved container image release; approved container image release still has no ACI restart policies proof.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Azure Container Instances restart policies](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-restart-policy)

**Source reviewed:** 2026-08-31

## LAB13-Q29 — B

**Question:** The container administrator publishing an approved image and running it in ACI must confirm the approved container image release, without mutation, can request CPU and memory values supported in the selected region. Which image release check qualifies?

- **A — Incorrect.** List repository manifests and match the selected tag to its sha256 digest.
  List repository manifests and match the selected tag to its sha256 digest. In the approved container image release, this check observes repository tags and digests. Approved container image release output covers repository tags and digests, not ACI resource sizing; the ACI resource sizing requirement to request CPU and memory values supported in the selected region remains unverified.
- **B — Correct.** Query each container's resources.requests and compare them with measured workload demand.
  For the approved container image release, this ACI resource sizing observation is decisive: query each container's resources.requests and compare them with measured workload demand. It is approved container image release evidence that operators can request CPU and memory values supported in the selected region.
- **C — Incorrect.** Query container group provisioningState, instanceView state, IP configuration, and each container status.
  Query container group provisioningState, instanceView state, IP configuration, and each container status. In the approved container image release, this check observes container groups. Approved container image release reads container groups, leaving ACI resource sizing unproved in approved container image release; approved container image release still has no ACI resource sizing proof.
- **D — Incorrect.** Query restartPolicy, currentState, previousState, exitCode, and restartCount.
  Query restartPolicy, currentState, previousState, exitCode, and restartCount. In the approved container image release, this check observes ACI restart policies. Approved container image release could pass ACI restart policies while ACI resource sizing is wrong; approved container image release still lacks ACI resource sizing proof.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Azure Container Instances resource availability](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability)

**Source reviewed:** 2026-08-31

## LAB13-Q30 — C

**Question:** The approved container image release configuration is complete; the image release reviewers need evidence it can prefer an identity-scoped image pull over long-lived registry credentials. Which observation shows success?

- **A — Incorrect.** List the identity's role assignment and confirm the deployed image resolves from the private login server.
  List the identity's role assignment and confirm the deployed image resolves from the private login server. In the approved container image release, this check observes registry pull authorization. Registry pull authorization success in approved container image release cannot verify registry credentials versus identity; approved container image release cannot prefer an identity-scoped image pull over long-lived registry credentials until registry credentials versus identity evidence exists.
- **B — Incorrect.** Query ipAddress.fqdn, type, ports, and the container's running state.
  Query ipAddress.fqdn, type, ports, and the container's running state. In the approved container image release, this check observes ACI DNS labels. Approved container image release reads ACI DNS labels, leaving registry credentials versus identity unproved in approved container image release; approved container image release still has no registry credentials versus identity proof.
- **C — Correct.** Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
  Query adminUserEnabled and confirm the workload identity's scoped pull assignment. Because the approved container image release check observes registry credentials versus identity, it independently verifies the requirement to prefer an identity-scoped image pull over long-lived registry credentials.
- **D — Incorrect.** Query each container's resources.requests and compare them with measured workload demand.
  Query each container's resources.requests and compare them with measured workload demand. In the approved container image release, this check observes ACI resource sizing. Approved container image release output covers ACI resource sizing, not registry credentials versus identity; the registry credentials versus identity requirement to prefer an identity-scoped image pull over long-lived registry credentials remains unverified.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q31 — C

**Question:** Although the approved container image release is meant to let the image release choose registry capabilities and throughput appropriate for the image workload, its checkpoint fails. Which image release defect explains the failure?

- **A — Incorrect.** The deployment uses the mutable latest tag and cannot prove which image content ran.
  The deployment uses the mutable latest tag and cannot prove which image content ran. The approved container image release fault concerns repository tags and digests. Approved container image release has repository tags and digests impact, but container registry service tiers is the approved container image release failed path; the repository tags and digests state cannot produce container registry service tiers failure.
- **B — Incorrect.** The requested DNS label is already used in the selected region.
  The requested DNS label is already used in the selected region. The approved container image release fault concerns ACI DNS labels. Approved container image release could repair ACI DNS labels while container registry service tiers stays broken in approved container image release; the approved container image release remains unable to choose registry capabilities and throughput appropriate for the image workload.
- **C — Correct.** The design requires geo-replication while the registry uses a non-Premium SKU.
  The approved container image release cannot choose registry capabilities and throughput appropriate for the image workload because of this container registry service tiers defect: the design requires geo-replication while the registry uses a non-Premium SKU. The symptom and repair align.
- **D — Incorrect.** The deployment depends on an enabled registry admin password embedded in automation.
  The deployment depends on an enabled registry admin password embedded in automation. The approved container image release fault concerns registry credentials versus identity. Approved container image release may fix registry credentials versus identity, yet container registry service tiers still fails; this approved container image release diagnosis of registry credentials versus identity is wrong for container registry service tiers.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Azure Container Registry service tiers](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus)

**Source reviewed:** 2026-08-31

## LAB13-Q32 — A

**Question:** The image release support team isolated the approved container image release incident to the attempt to deploy by digest so later tag changes cannot move the release. Which condition prevents success?

- **A — Correct.** The deployment uses the mutable latest tag and cannot prove which image content ran.
  The deployment uses the mutable latest tag and cannot prove which image content ran. Removing this repository tags and digests condition lets the approved container image release deploy by digest so later tag changes cannot move the release while leaving healthy controls unchanged.
- **B — Incorrect.** The identity exists but has no permission to pull image content from the registry.
  The identity exists but has no permission to pull image content from the registry. The approved container image release fault concerns registry pull authorization. Approved container image release failed on repository tags and digests; this registry pull authorization finding redirects approved container image release remediation away from repository tags and digests.
- **C — Incorrect.** A credential was stored as a plain environment variable in the committed deployment definition.
  A credential was stored as a plain environment variable in the committed deployment definition. The approved container image release fault concerns container environment secrets. Approved container image release may fix container environment secrets, yet repository tags and digests still fails; this approved container image release diagnosis of container environment secrets is wrong for repository tags and digests.
- **D — Incorrect.** The design requires geo-replication while the registry uses a non-Premium SKU.
  The design requires geo-replication while the registry uses a non-Premium SKU. The approved container image release fault concerns container registry service tiers. Approved container image release has container registry service tiers impact, but repository tags and digests is the approved container image release failed path; the container registry service tiers state cannot produce repository tags and digests failure.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Container image tags and versioning](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-image-tag-version)

**Source reviewed:** 2026-08-31

## LAB13-Q33 — C

**Question:** An approved container image release query surprises the container administrator publishing an approved image and running it in ACI during the image release attempt to let the runtime pull a private image without embedding an administrator password. Which finding explains it?

- **A — Incorrect.** The source registry requires credentials that were not supplied to the import operation.
  The source registry requires credentials that were not supplied to the import operation. The approved container image release fault concerns server-side image import. Approved container image release failed on registry pull authorization; this server-side image import finding redirects approved container image release remediation away from registry pull authorization.
- **B — Incorrect.** A completed batch job uses Always and repeatedly starts again.
  A completed batch job uses Always and repeatedly starts again. The approved container image release fault concerns ACI restart policies. Approved container image release may fix ACI restart policies, yet registry pull authorization still fails; this approved container image release diagnosis of ACI restart policies is wrong for registry pull authorization.
- **C — Correct.** The identity exists but has no permission to pull image content from the registry.
  The identity exists but has no permission to pull image content from the registry. In approved container image release, this registry pull authorization cause matches the failure to let the runtime pull a private image without embedding an administrator password.
- **D — Incorrect.** The deployment uses the mutable latest tag and cannot prove which image content ran.
  The deployment uses the mutable latest tag and cannot prove which image content ran. The approved container image release fault concerns repository tags and digests. Approved container image release could repair repository tags and digests while registry pull authorization stays broken in approved container image release; the approved container image release remains unable to let the runtime pull a private image without embedding an administrator password.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q34 — A

**Question:** Other approved container image release components are healthy, but the image release still cannot copy an existing image into the registry without a local pull and push. Which state causes the isolated failure?

- **A — Correct.** The source registry requires credentials that were not supplied to the import operation.
  The source registry requires credentials that were not supplied to the import operation. This approved container image release condition breaks server-side image import, explaining why operators cannot copy an existing image into the registry without a local pull and push.
- **B — Incorrect.** Two independently scaled services were placed in one container group.
  Two independently scaled services were placed in one container group. The approved container image release fault concerns container groups. Approved container image release has container groups impact, but server-side image import is the approved container image release failed path; the container groups state cannot produce server-side image import failure.
- **C — Incorrect.** The requested CPU and memory combination is unavailable in the deployment region.
  The requested CPU and memory combination is unavailable in the deployment region. The approved container image release fault concerns ACI resource sizing. Approved container image release could repair ACI resource sizing while server-side image import stays broken in approved container image release; the approved container image release remains unable to copy an existing image into the registry without a local pull and push.
- **D — Incorrect.** The identity exists but has no permission to pull image content from the registry.
  The identity exists but has no permission to pull image content from the registry. The approved container image release fault concerns registry pull authorization. Approved container image release failed on server-side image import; this registry pull authorization finding redirects approved container image release remediation away from server-side image import.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Import container images into a registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images)

**Source reviewed:** 2026-08-31

## LAB13-Q35 — D

**Question:** During an image release fault drill, the approved container image release does not run sidecars inside one jointly managed execution unit. Which finding identifies the defect?

- **A — Incorrect.** The requested DNS label is already used in the selected region.
  The requested DNS label is already used in the selected region. The approved container image release fault concerns ACI DNS labels. Approved container image release has ACI DNS labels impact, but container groups is the approved container image release failed path; the ACI DNS labels state cannot produce container groups failure.
- **B — Incorrect.** The deployment depends on an enabled registry admin password embedded in automation.
  The deployment depends on an enabled registry admin password embedded in automation. The approved container image release fault concerns registry credentials versus identity. Approved container image release could repair registry credentials versus identity while container groups stays broken in approved container image release; the approved container image release remains unable to run sidecars inside one jointly managed execution unit.
- **C — Incorrect.** The source registry requires credentials that were not supplied to the import operation.
  The source registry requires credentials that were not supplied to the import operation. The approved container image release fault concerns server-side image import. Approved container image release failed on container groups; this server-side image import finding redirects approved container image release remediation away from container groups.
- **D — Correct.** Two independently scaled services were placed in one container group.
  For the approved container image release, the container groups failure is causal: two independently scaled services were placed in one container group. Correcting it restores the ability to run sidecars inside one jointly managed execution unit.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Azure Container Instances container groups](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-groups)

**Source reviewed:** 2026-08-31

## LAB13-Q36 — B

**Question:** The approved container image release setup finishes, yet the image release cannot publish a stable regional name for the container group's public endpoint. Which misconfiguration explains the mismatch?

- **A — Incorrect.** A credential was stored as a plain environment variable in the committed deployment definition.
  A credential was stored as a plain environment variable in the committed deployment definition. The approved container image release fault concerns container environment secrets. Approved container image release could repair container environment secrets while ACI DNS labels stays broken in approved container image release; the approved container image release remains unable to publish a stable regional name for the container group's public endpoint.
- **B — Correct.** The requested DNS label is already used in the selected region.
  The requested DNS label is already used in the selected region. The finding is specific to ACI DNS labels in the approved container image release; repairing ACI DNS labels restores the approved container image release ability to publish a stable regional name for the container group's public endpoint.
- **C — Incorrect.** The design requires geo-replication while the registry uses a non-Premium SKU.
  The design requires geo-replication while the registry uses a non-Premium SKU. The approved container image release fault concerns container registry service tiers. Approved container image release may fix container registry service tiers, yet ACI DNS labels still fails; this approved container image release diagnosis of container registry service tiers is wrong for ACI DNS labels.
- **D — Incorrect.** Two independently scaled services were placed in one container group.
  Two independently scaled services were placed in one container group. The approved container image release fault concerns container groups. Approved container image release has container groups impact, but ACI DNS labels is the approved container image release failed path; the container groups state cannot produce ACI DNS labels failure.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Create a container instance with Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart)

**Source reviewed:** 2026-08-31

## LAB13-Q37 — A

**Question:** An image release break/fix in the approved container image release fails when operators try to pass sensitive configuration without writing the clear value into ordinary output. Which diagnosis fits?

- **A — Correct.** A credential was stored as a plain environment variable in the committed deployment definition.
  The approved container image release cannot pass sensitive configuration without writing the clear value into ordinary output because of this container environment secrets defect: a credential was stored as a plain environment variable in the committed deployment definition. The symptom and repair align.
- **B — Incorrect.** A completed batch job uses Always and repeatedly starts again.
  A completed batch job uses Always and repeatedly starts again. The approved container image release fault concerns ACI restart policies. Approved container image release may fix ACI restart policies, yet container environment secrets still fails; this approved container image release diagnosis of ACI restart policies is wrong for container environment secrets.
- **C — Incorrect.** The deployment uses the mutable latest tag and cannot prove which image content ran.
  The deployment uses the mutable latest tag and cannot prove which image content ran. The approved container image release fault concerns repository tags and digests. Approved container image release has repository tags and digests impact, but container environment secrets is the approved container image release failed path; the repository tags and digests state cannot produce container environment secrets failure.
- **D — Incorrect.** The requested DNS label is already used in the selected region.
  The requested DNS label is already used in the selected region. The approved container image release fault concerns ACI DNS labels. Approved container image release could repair ACI DNS labels while container environment secrets stays broken in approved container image release; the approved container image release remains unable to pass sensitive configuration without writing the clear value into ordinary output.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Set environment variables in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-environment-variables)

**Source reviewed:** 2026-08-31

## LAB13-Q38 — B

**Question:** The approved container image release troubleshooting scope is the image release need to control whether a terminated container restarts. Which condition should be corrected first?

- **A — Incorrect.** The requested CPU and memory combination is unavailable in the deployment region.
  The requested CPU and memory combination is unavailable in the deployment region. The approved container image release fault concerns ACI resource sizing. Approved container image release may fix ACI resource sizing, yet ACI restart policies still fails; this approved container image release diagnosis of ACI resource sizing is wrong for ACI restart policies.
- **B — Correct.** A completed batch job uses Always and repeatedly starts again.
  A completed batch job uses Always and repeatedly starts again. Removing this ACI restart policies condition lets the approved container image release control whether a terminated container restarts while leaving healthy controls unchanged.
- **C — Incorrect.** The identity exists but has no permission to pull image content from the registry.
  The identity exists but has no permission to pull image content from the registry. The approved container image release fault concerns registry pull authorization. Approved container image release could repair registry pull authorization while ACI restart policies stays broken in approved container image release; the approved container image release remains unable to control whether a terminated container restarts.
- **D — Incorrect.** A credential was stored as a plain environment variable in the committed deployment definition.
  A credential was stored as a plain environment variable in the committed deployment definition. The approved container image release fault concerns container environment secrets. Approved container image release failed on ACI restart policies; this container environment secrets finding redirects approved container image release remediation away from ACI restart policies.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Azure Container Instances restart policies](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-restart-policy)

**Source reviewed:** 2026-08-31

## LAB13-Q39 — A

**Question:** The approved container image release result is partial because the image release cannot request CPU and memory values supported in the selected region. Which condition accounts for that result?

- **A — Correct.** The requested CPU and memory combination is unavailable in the deployment region.
  The requested CPU and memory combination is unavailable in the deployment region. In approved container image release, this ACI resource sizing cause matches the failure to request CPU and memory values supported in the selected region.
- **B — Incorrect.** The deployment depends on an enabled registry admin password embedded in automation.
  The deployment depends on an enabled registry admin password embedded in automation. The approved container image release fault concerns registry credentials versus identity. Approved container image release could repair registry credentials versus identity while ACI resource sizing stays broken in approved container image release; the approved container image release remains unable to request CPU and memory values supported in the selected region.
- **C — Incorrect.** The source registry requires credentials that were not supplied to the import operation.
  The source registry requires credentials that were not supplied to the import operation. The approved container image release fault concerns server-side image import. Approved container image release failed on ACI resource sizing; this server-side image import finding redirects approved container image release remediation away from ACI resource sizing.
- **D — Incorrect.** A completed batch job uses Always and repeatedly starts again.
  A completed batch job uses Always and repeatedly starts again. The approved container image release fault concerns ACI restart policies. Approved container image release may fix ACI restart policies, yet ACI resource sizing still fails; this approved container image release diagnosis of ACI restart policies is wrong for ACI resource sizing.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Azure Container Instances resource availability](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability)

**Source reviewed:** 2026-08-31

## LAB13-Q40 — C

**Question:** The image release evidence shows the approved container image release cannot prefer an identity-scoped image pull over long-lived registry credentials. Which root cause fits that evidence?

- **A — Incorrect.** The design requires geo-replication while the registry uses a non-Premium SKU.
  The design requires geo-replication while the registry uses a non-Premium SKU. The approved container image release fault concerns container registry service tiers. Approved container image release could repair container registry service tiers while registry credentials versus identity stays broken in approved container image release; the approved container image release remains unable to prefer an identity-scoped image pull over long-lived registry credentials.
- **B — Incorrect.** Two independently scaled services were placed in one container group.
  Two independently scaled services were placed in one container group. The approved container image release fault concerns container groups. Approved container image release failed on registry credentials versus identity; this container groups finding redirects approved container image release remediation away from registry credentials versus identity.
- **C — Correct.** The deployment depends on an enabled registry admin password embedded in automation.
  The deployment depends on an enabled registry admin password embedded in automation. This approved container image release condition breaks registry credentials versus identity, explaining why operators cannot prefer an identity-scoped image pull over long-lived registry credentials.
- **D — Incorrect.** The requested CPU and memory combination is unavailable in the deployment region.
  The requested CPU and memory combination is unavailable in the deployment region. The approved container image release fault concerns ACI resource sizing. Approved container image release has ACI resource sizing impact, but registry credentials versus identity is the approved container image release failed path; the ACI resource sizing state cannot produce registry credentials versus identity failure.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q41 — B

**Question:** The approved container image release forbids a partial image release result. Operators must first choose registry capabilities and throughput appropriate for the image workload and afterward confirm the approved container image release outcome. Which image release sequence is complete?

- **A — Incorrect.** First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.
  First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server. This approved container image release pair serves registry pull authorization. Registry pull authorization cannot replace container registry service tiers in approved container image release. Use this container registry service tiers pair instead: First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.
- **B — Correct.** First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.
  For the approved container image release, the safe container registry service tiers order is: first, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features. The approved container image release records container registry service tiers proof after configuration.
- **C — Incorrect.** First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.
  First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted. This approved container image release pair serves container environment secrets. Approved container image release uses container environment secrets for both steps; container registry service tiers remains untouched in approved container image release, so its container registry service tiers gate to choose registry capabilities and throughput appropriate for the image workload fails.
- **D — Incorrect.** First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.
  First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount. This approved container image release pair serves ACI restart policies. Approved container image release closes ACI restart policies, not container registry service tiers; without the container registry service tiers workflow, it cannot choose registry capabilities and throughput appropriate for the image workload.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Azure Container Registry service tiers](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus)

**Source reviewed:** 2026-08-31

## LAB13-Q42 — D

**Question:** Only the approved container image release change needed to deploy by digest so later tag changes cannot move the release is allowed, and image release proof is mandatory. Which pair fits?

- **A — Incorrect.** First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp.
  First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp. This approved container image release pair serves server-side image import. Approved container image release proves server-side image import, but repository tags and digests lacks implementation in approved container image release and repository tags and digests proof; the repository tags and digests outcome to deploy by digest so later tag changes cannot move the release remains open.
- **B — Incorrect.** First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.
  First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount. This approved container image release pair serves ACI restart policies. Approved container image release uses ACI restart policies for both steps; repository tags and digests remains untouched in approved container image release, so its repository tags and digests gate to deploy by digest so later tag changes cannot move the release fails.
- **C — Incorrect.** First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
  First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand. This approved container image release pair serves ACI resource sizing. Approved container image release closes ACI resource sizing, not repository tags and digests; without the repository tags and digests workflow, it cannot deploy by digest so later tag changes cannot move the release.
- **D — Correct.** First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest.
  First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest. The approved container image release uses its repository tags and digests mutation gate and repository tags and digests verification gate before it can deploy by digest so later tag changes cannot move the release.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Container image tags and versioning](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-image-tag-version)

**Source reviewed:** 2026-08-31

## LAB13-Q43 — A

**Question:** The approved container image release runbook separates image release mutation from validation while it must let the runtime pull a private image without embedding an administrator password. Which sequence proves it cleanly?

- **A — Correct.** First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.
  The approved container image release gets a complete registry pull authorization sequence here: first, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server. Read-back evidence follows the change.
- **B — Incorrect.** First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.
  First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status. This approved container image release pair serves container groups. Approved container image release closes container groups, not registry pull authorization; without the registry pull authorization workflow, it cannot let the runtime pull a private image without embedding an administrator password.
- **C — Incorrect.** First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
  First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand. This approved container image release pair serves ACI resource sizing. ACI resource sizing cannot replace registry pull authorization in approved container image release. Use this registry pull authorization pair instead: First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.
- **D — Incorrect.** First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
  First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment. This approved container image release pair serves registry credentials versus identity. Approved container image release proves registry credentials versus identity, but registry pull authorization lacks implementation in approved container image release and registry pull authorization proof; the registry pull authorization outcome to let the runtime pull a private image without embedding an administrator password remains open.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31

## LAB13-Q44 — B

**Question:** The approved container image release checkpoint requires both this image release outcome—copy an existing image into the registry without a local pull and push—and a read-only approved container image release state check. Which image release response is complete?

- **A — Incorrect.** First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.
  First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state. This approved container image release pair serves ACI DNS labels. Approved container image release closes ACI DNS labels, not server-side image import; without the server-side image import workflow, it cannot copy an existing image into the registry without a local pull and push.
- **B — Correct.** First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp.
  First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp. This ordered server-side image import workflow lets the approved container image release copy an existing image into the registry without a local pull and push and then verify the resulting state.
- **C — Incorrect.** First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
  First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment. This approved container image release pair serves registry credentials versus identity. Approved container image release proves registry credentials versus identity, but server-side image import lacks implementation in approved container image release and server-side image import proof; the server-side image import outcome to copy an existing image into the registry without a local pull and push remains open.
- **D — Incorrect.** First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.
  First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features. This approved container image release pair serves container registry service tiers. Approved container image release uses container registry service tiers for both steps; server-side image import remains untouched in approved container image release, so its server-side image import gate to copy an existing image into the registry without a local pull and push fails.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Import container images into a registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images)

**Source reviewed:** 2026-08-31

## LAB13-Q45 — C

**Question:** The approved container image release runbook must run sidecars inside one jointly managed execution unit, then retain image release read-back evidence. Which approved container image release pair completes both duties?

- **A — Incorrect.** First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.
  First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted. This approved container image release pair serves container environment secrets. Container environment secrets cannot replace container groups in approved container image release. Use this container groups pair instead: First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.
- **B — Incorrect.** First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.
  First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features. This approved container image release pair serves container registry service tiers. Approved container image release proves container registry service tiers, but container groups lacks implementation in approved container image release and container groups proof; the container groups outcome to run sidecars inside one jointly managed execution unit remains open.
- **C — Correct.** First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.
  First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status. For approved container image release, the container groups operation precedes its container groups read-back check, allowing it to run sidecars inside one jointly managed execution unit.
- **D — Incorrect.** First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest.
  First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest. This approved container image release pair serves repository tags and digests. Approved container image release closes repository tags and digests, not container groups; without the container groups workflow, it cannot run sidecars inside one jointly managed execution unit.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Azure Container Instances container groups](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-groups)

**Source reviewed:** 2026-08-31

## LAB13-Q46 — C

**Question:** To satisfy the image release requirement, operators must change the approved container image release configuration and prove it can publish a stable regional name for the container group's public endpoint. Which sequence is coherent?

- **A — Incorrect.** First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.
  First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount. This approved container image release pair serves ACI restart policies. Approved container image release proves ACI restart policies, but ACI DNS labels lacks implementation in approved container image release and ACI DNS labels proof; the ACI DNS labels outcome to publish a stable regional name for the container group's public endpoint remains open.
- **B — Incorrect.** First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest.
  First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest. This approved container image release pair serves repository tags and digests. Approved container image release uses repository tags and digests for both steps; ACI DNS labels remains untouched in approved container image release, so its ACI DNS labels gate to publish a stable regional name for the container group's public endpoint fails.
- **C — Correct.** First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.
  First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state. In the approved container image release, the first ACI DNS labels step runs; the approved container image release then reads ACI DNS labels state to prove it can publish a stable regional name for the container group's public endpoint.
- **D — Incorrect.** First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.
  First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server. This approved container image release pair serves registry pull authorization. Registry pull authorization cannot replace ACI DNS labels in approved container image release. Use this ACI DNS labels pair instead: First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB13-CP01`).

**Microsoft Learn sources:**

- [Create a container instance with Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart)

**Source reviewed:** 2026-08-31

## LAB13-Q47 — B

**Question:** The container administrator publishing an approved image and running it in ACI needs a safe approved container image release change to pass sensitive configuration without writing the clear value into ordinary output, followed by image release evidence. Which pair merits approval?

- **A — Incorrect.** First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
  First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand. This approved container image release pair serves ACI resource sizing. Approved container image release uses ACI resource sizing for both steps; container environment secrets remains untouched in approved container image release, so its container environment secrets gate to pass sensitive configuration without writing the clear value into ordinary output fails.
- **B — Correct.** First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.
  For the approved container image release, the safe container environment secrets order is: first, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted. The approved container image release records container environment secrets proof after configuration.
- **C — Incorrect.** First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.
  First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server. This approved container image release pair serves registry pull authorization. Registry pull authorization cannot replace container environment secrets in approved container image release. Use this container environment secrets pair instead: First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.
- **D — Incorrect.** First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp.
  First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp. This approved container image release pair serves server-side image import. Approved container image release proves server-side image import, but container environment secrets lacks implementation in approved container image release and container environment secrets proof; the container environment secrets outcome to pass sensitive configuration without writing the clear value into ordinary output remains open.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB13-CP02`).

**Microsoft Learn sources:**

- [Set environment variables in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-environment-variables)

**Source reviewed:** 2026-08-31

## LAB13-Q48 — C

**Question:** The approved container image release has two image release gates: control whether a terminated container restarts, then prove the approved container image release state. Which image release sequence works?

- **A — Incorrect.** First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
  First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment. This approved container image release pair serves registry credentials versus identity. Approved container image release closes registry credentials versus identity, not ACI restart policies; without the ACI restart policies workflow, it cannot control whether a terminated container restarts.
- **B — Incorrect.** First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp.
  First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp. This approved container image release pair serves server-side image import. Server-side image import cannot replace ACI restart policies in approved container image release. Use this ACI restart policies pair instead: First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.
- **C — Correct.** First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.
  First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount. The approved container image release uses its ACI restart policies mutation gate and ACI restart policies verification gate before it can control whether a terminated container restarts.
- **D — Incorrect.** First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.
  First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status. This approved container image release pair serves container groups. Approved container image release uses container groups for both steps; ACI restart policies remains untouched in approved container image release, so its ACI restart policies gate to control whether a terminated container restarts fails.

**Objectives:** `CP-CONTAINERS-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB13-CP03`).

**Microsoft Learn sources:**

- [Azure Container Instances restart policies](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-restart-policy)

**Source reviewed:** 2026-08-31

## LAB13-Q49 — B

**Question:** Which image release path makes the approved container image release able to request CPU and memory values supported in the selected region, then inspects the defining properties?

- **A — Incorrect.** First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.
  First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features. This approved container image release pair serves container registry service tiers. Container registry service tiers cannot replace ACI resource sizing in approved container image release. Use this ACI resource sizing pair instead: First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
- **B — Correct.** First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
  The approved container image release gets a complete ACI resource sizing sequence here: first, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand. Read-back evidence follows the change.
- **C — Incorrect.** First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.
  First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status. This approved container image release pair serves container groups. Approved container image release uses container groups for both steps; ACI resource sizing remains untouched in approved container image release, so its ACI resource sizing gate to request CPU and memory values supported in the selected region fails.
- **D — Incorrect.** First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.
  First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state. This approved container image release pair serves ACI DNS labels. Approved container image release closes ACI DNS labels, not ACI resource sizing; without the ACI resource sizing workflow, it cannot request CPU and memory values supported in the selected region.

**Objectives:** `CP-CONTAINERS-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB13-CP04`).

**Microsoft Learn sources:**

- [Azure Container Instances resource availability](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability)

**Source reviewed:** 2026-08-31

## LAB13-Q50 — A

**Question:** At the approved container image release approval gate, operators must show that the image release can prefer an identity-scoped image pull over long-lived registry credentials. Which image release configure-and-check pair is defensible?

- **A — Correct.** First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
  First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment. This ordered registry credentials versus identity workflow lets the approved container image release prefer an identity-scoped image pull over long-lived registry credentials and then verify the resulting state.
- **B — Incorrect.** First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest.
  First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest. This approved container image release pair serves repository tags and digests. Approved container image release uses repository tags and digests for both steps; registry credentials versus identity remains untouched in approved container image release, so its registry credentials versus identity gate to prefer an identity-scoped image pull over long-lived registry credentials fails.
- **C — Incorrect.** First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.
  First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state. This approved container image release pair serves ACI DNS labels. Approved container image release closes ACI DNS labels, not registry credentials versus identity; without the registry credentials versus identity workflow, it cannot prefer an identity-scoped image pull over long-lived registry credentials.
- **D — Incorrect.** First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.
  First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted. This approved container image release pair serves container environment secrets. Container environment secrets cannot replace registry credentials versus identity in approved container image release. Use this registry credentials versus identity pair instead: First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.

**Objectives:** `CP-CONTAINERS-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB13-CP05`).

**Microsoft Learn sources:**

- [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication)

**Source reviewed:** 2026-08-31
