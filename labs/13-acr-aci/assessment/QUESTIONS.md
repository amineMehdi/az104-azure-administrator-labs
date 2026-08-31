# Lab 13 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB13-Q01 — Foundational

The approved container image release acceptance criteria require operators to choose registry capabilities and throughput appropriate for the image workload. Which service fact supports that requirement?

- A. ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
- B. An image tag is a mutable label, while a manifest digest identifies immutable image content.
- C. An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes.
- D. Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively.

## LAB13-Q02 — Foundational

An image release reviewer challenges whether the approved container image release can deploy by digest so later tag changes cannot move the release. Which response resolves the concern?

- A. A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository.
- B. A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint.
- C. ACI CPU and memory requests are specified per container and determine scheduling support and cost.
- D. An image tag is a mutable label, while a manifest digest identifies immutable image content.

## LAB13-Q03 — Foundational

The approved container image release handoff omits the image release rule needed to let the runtime pull a private image without embedding an administrator password. Which statement should the team add?

- A. ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push.
- B. ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
- C. A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository.
- D. The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization.

## LAB13-Q04 — Foundational

An image release incident review of the approved container image release depends on the ability to copy an existing image into the registry without a local pull and push. Which platform description is reliable?

- A. An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes.
- B. Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively.
- C. ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
- D. ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push.

## LAB13-Q05 — Foundational

A container administrator publishing an approved image and running it in ACI is updating the image release runbook. The requirement is to run sidecars inside one jointly managed execution unit. Which statement describes Azure behavior correctly?

- A. A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint.
- B. An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes.
- C. ACI CPU and memory requests are specified per container and determine scheduling support and cost.
- D. An image tag is a mutable label, while a manifest digest identifies immutable image content.

## LAB13-Q06 — Foundational

An image release peer review asks how the approved container image release should handle this outcome: publish a stable regional name for the container group's public endpoint. Which explanation is accurate?

- A. ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
- B. A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint.
- C. The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization.
- D. A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository.

## LAB13-Q07 — Foundational

For the approved container image release, the image release plan must pass sensitive configuration without writing the clear value into ordinary output. Which statement about image release belongs in the approved container image release record?

- A. ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
- B. Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively.
- C. ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
- D. ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push.

## LAB13-Q08 — Foundational

The image release review compares four claims for the approved container image release requirement to control whether a terminated container restarts. Which claim is technically sound?

- A. ACI CPU and memory requests are specified per container and determine scheduling support and cost.
- B. An image tag is a mutable label, while a manifest digest identifies immutable image content.
- C. An ACI container group is the deployment and scheduling boundary whose containers share lifecycle, network, and local volumes.
- D. Always, OnFailure, and Never restart policies suit long-running services, retryable tasks, and one-time jobs respectively.

## LAB13-Q09 — Foundational

The image release architecture note requires the approved container image release environment to request CPU and memory values supported in the selected region. Which statement defines the relevant image release boundary?

- A. The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization.
- B. A managed identity needs the appropriate ACR pull data permission scoped to the registry or repository.
- C. A public ACI DNS name combines a region-scoped unique label with the regional Azure container endpoint.
- D. ACI CPU and memory requests are specified per container and determine scheduling support and cost.

## LAB13-Q10 — Foundational

A new image release operator must explain why the approved container image release can prefer an identity-scoped image pull over long-lived registry credentials. Which explanation is accurate?

- A. ACR Basic, Standard, and Premium share core registry APIs but differ in included performance, scale, and premium features.
- B. ACR import copies an image from a supported source into the registry without requiring a local Docker pull and push.
- C. ACI secure environment variables hide values from ordinary container property output but still require careful source and state handling.
- D. The ACR admin account provides broad registry credentials, whereas workload identity supports scoped, revocable authorization.

## LAB13-Q11 — Foundational

An approved container image release review finds image release drift from the need to choose registry capabilities and throughput appropriate for the image workload. Which correction addresses that drift?

- A. Assign the pull role to the workload identity and reference the private registry without embedding a password.
- B. Check label availability and configure the DNS name label only for a deliberately public container group.
- C. Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements.
- D. Set explicit CPU and memory requests within the selected region's supported combinations.

## LAB13-Q12 — Foundational

The approved container image release window permits only the image release change needed to deploy by digest so later tag changes cannot move the release. Which option respects the boundary?

- A. Import the approved source image into a uniquely versioned target repository and tag.
- B. Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence.
- C. Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files.
- D. Prefer managed identity for the container pull path and leave the registry admin account disabled.

## LAB13-Q13 — Foundational

The image release preflight has passed; the approved container image release must now let the runtime pull a private image without embedding an administrator password. Which operation should run?

- A. Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace.
- B. Set the restart policy from the workload's intended lifecycle and exit-code behavior.
- C. Assign the pull role to the workload identity and reference the private registry without embedding a password.
- D. Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements.

## LAB13-Q14 — Foundational

The approved container image release plan must copy an existing image into the registry without a local pull and push while limiting the mutation scope to image release. Which action is appropriate?

- A. Check label availability and configure the DNS name label only for a deliberately public container group.
- B. Set explicit CPU and memory requests within the selected region's supported combinations.
- C. Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence.
- D. Import the approved source image into a uniquely versioned target repository and tag.

## LAB13-Q15 — Foundational

An image release ticket in the approved container image release says to run sidecars inside one jointly managed execution unit. Which image release action completes the approved container image release request with minimal change?

- A. Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files.
- B. Prefer managed identity for the container pull path and leave the registry admin account disabled.
- C. Assign the pull role to the workload identity and reference the private registry without embedding a password.
- D. Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace.

## LAB13-Q16 — Applied

The approach for the approved container image release is approved, but the image release environment still cannot publish a stable regional name for the container group's public endpoint. Which implementation step closes the gap?

- A. Set the restart policy from the workload's intended lifecycle and exit-code behavior.
- B. Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements.
- C. Check label availability and configure the DNS name label only for a deliberately public container group.
- D. Import the approved source image into a uniquely versioned target repository and tag.

## LAB13-Q17 — Applied

The container administrator publishing an approved image and running it in ACI may change the approved container image release only to pass sensitive configuration without writing the clear value into ordinary output. Which image release action stays within that assignment?

- A. Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files.
- B. Set explicit CPU and memory requests within the selected region's supported combinations.
- C. Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence.
- D. Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace.

## LAB13-Q18 — Applied

An image release dry run shows no approved container image release command will control whether a terminated container restarts. Which action belongs before execution?

- A. Prefer managed identity for the container pull path and leave the registry admin account disabled.
- B. Set the restart policy from the workload's intended lifecycle and exit-code behavior.
- C. Assign the pull role to the workload identity and reference the private registry without embedding a password.
- D. Check label availability and configure the DNS name label only for a deliberately public container group.

## LAB13-Q19 — Applied

For the approved container image release, operators need to request CPU and memory values supported in the selected region. Which change realizes that requirement?

- A. Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements.
- B. Import the approved source image into a uniquely versioned target repository and tag.
- C. Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files.
- D. Set explicit CPU and memory requests within the selected region's supported combinations.

## LAB13-Q20 — Applied

Operators must automate the approved container image release change needed to prefer an identity-scoped image pull over long-lived registry credentials. Which image release operation belongs in the runbook?

- A. Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence.
- B. Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace.
- C. Set the restart policy from the workload's intended lifecycle and exit-code behavior.
- D. Prefer managed identity for the container pull path and leave the registry admin account disabled.

## LAB13-Q21 — Applied

The image release validation asks whether the approved container image release can choose registry capabilities and throughput appropriate for the image workload. Which observable state is strongest?

- A. List the target repository and verify its tag, digest, and import timestamp.
- B. Query sku.name, provisioningState, loginServer, and configured premium features.
- C. Inspect the container definition and evidence output to confirm secret values are redacted.
- D. Query adminUserEnabled and confirm the workload identity's scoped pull assignment.

## LAB13-Q22 — Applied

An approved container image release review must prove the image release ability to deploy by digest so later tag changes cannot move the release. Which check avoids an adjacent feature?

- A. Query container group provisioningState, instanceView state, IP configuration, and each container status.
- B. Query restartPolicy, currentState, previousState, exitCode, and restartCount.
- C. List repository manifests and match the selected tag to its sha256 digest.
- D. Query sku.name, provisioningState, loginServer, and configured premium features.

## LAB13-Q23 — Applied

The approved container image release evidence bundle needs an image release result showing it can let the runtime pull a private image without embedding an administrator password. Which result belongs in the checkpoint?

- A. List the identity's role assignment and confirm the deployed image resolves from the private login server.
- B. Query ipAddress.fqdn, type, ports, and the container's running state.
- C. Query each container's resources.requests and compare them with measured workload demand.
- D. List repository manifests and match the selected tag to its sha256 digest.

## LAB13-Q24 — Applied

Before approved container image release cleanup, the image release team must reconfirm it can copy an existing image into the registry without a local pull and push. Which read-only inspection should run?

- A. Inspect the container definition and evidence output to confirm secret values are redacted.
- B. Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
- C. List the identity's role assignment and confirm the deployed image resolves from the private login server.
- D. List the target repository and verify its tag, digest, and import timestamp.

## LAB13-Q25 — Applied

The approved container image release setup reports success after the image release attempt to run sidecars inside one jointly managed execution unit. Which image release read-only observation proves the approved container image release outcome?

- A. Query restartPolicy, currentState, previousState, exitCode, and restartCount.
- B. Query container group provisioningState, instanceView state, IP configuration, and each container status.
- C. Query sku.name, provisioningState, loginServer, and configured premium features.
- D. List the target repository and verify its tag, digest, and import timestamp.

## LAB13-Q26 — Applied

The image release log says the approved container image release can now publish a stable regional name for the container group's public endpoint. Which image release state should the approved container image release acceptance test retain?

- A. Query ipAddress.fqdn, type, ports, and the container's running state.
- B. Query each container's resources.requests and compare them with measured workload demand.
- C. List repository manifests and match the selected tag to its sha256 digest.
- D. Query container group provisioningState, instanceView state, IP configuration, and each container status.

## LAB13-Q27 — Applied

The approved container image release rejects image release exit status as proof it can pass sensitive configuration without writing the clear value into ordinary output. Which approved container image release result is valid evidence?

- A. Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
- B. List the identity's role assignment and confirm the deployed image resolves from the private login server.
- C. Query ipAddress.fqdn, type, ports, and the container's running state.
- D. Inspect the container definition and evidence output to confirm secret values are redacted.

## LAB13-Q28 — Applied

The image release validator needs one approved container image release query after the change to control whether a terminated container restarts. Which image release property should the approved container image release validator inspect?

- A. Query restartPolicy, currentState, previousState, exitCode, and restartCount.
- B. Query sku.name, provisioningState, loginServer, and configured premium features.
- C. List the target repository and verify its tag, digest, and import timestamp.
- D. Inspect the container definition and evidence output to confirm secret values are redacted.

## LAB13-Q29 — Applied

The container administrator publishing an approved image and running it in ACI must confirm the approved container image release, without mutation, can request CPU and memory values supported in the selected region. Which image release check qualifies?

- A. List repository manifests and match the selected tag to its sha256 digest.
- B. Query each container's resources.requests and compare them with measured workload demand.
- C. Query container group provisioningState, instanceView state, IP configuration, and each container status.
- D. Query restartPolicy, currentState, previousState, exitCode, and restartCount.

## LAB13-Q30 — Applied

The approved container image release configuration is complete; the image release reviewers need evidence it can prefer an identity-scoped image pull over long-lived registry credentials. Which observation shows success?

- A. List the identity's role assignment and confirm the deployed image resolves from the private login server.
- B. Query ipAddress.fqdn, type, ports, and the container's running state.
- C. Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
- D. Query each container's resources.requests and compare them with measured workload demand.

## LAB13-Q31 — Applied

Although the approved container image release is meant to let the image release choose registry capabilities and throughput appropriate for the image workload, its checkpoint fails. Which image release defect explains the failure?

- A. The deployment uses the mutable latest tag and cannot prove which image content ran.
- B. The requested DNS label is already used in the selected region.
- C. The design requires geo-replication while the registry uses a non-Premium SKU.
- D. The deployment depends on an enabled registry admin password embedded in automation.

## LAB13-Q32 — Applied

The image release support team isolated the approved container image release incident to the attempt to deploy by digest so later tag changes cannot move the release. Which condition prevents success?

- A. The deployment uses the mutable latest tag and cannot prove which image content ran.
- B. The identity exists but has no permission to pull image content from the registry.
- C. A credential was stored as a plain environment variable in the committed deployment definition.
- D. The design requires geo-replication while the registry uses a non-Premium SKU.

## LAB13-Q33 — Applied

An approved container image release query surprises the container administrator publishing an approved image and running it in ACI during the image release attempt to let the runtime pull a private image without embedding an administrator password. Which finding explains it?

- A. The source registry requires credentials that were not supplied to the import operation.
- B. A completed batch job uses Always and repeatedly starts again.
- C. The identity exists but has no permission to pull image content from the registry.
- D. The deployment uses the mutable latest tag and cannot prove which image content ran.

## LAB13-Q34 — Applied

Other approved container image release components are healthy, but the image release still cannot copy an existing image into the registry without a local pull and push. Which state causes the isolated failure?

- A. The source registry requires credentials that were not supplied to the import operation.
- B. Two independently scaled services were placed in one container group.
- C. The requested CPU and memory combination is unavailable in the deployment region.
- D. The identity exists but has no permission to pull image content from the registry.

## LAB13-Q35 — Applied

During an image release fault drill, the approved container image release does not run sidecars inside one jointly managed execution unit. Which finding identifies the defect?

- A. The requested DNS label is already used in the selected region.
- B. The deployment depends on an enabled registry admin password embedded in automation.
- C. The source registry requires credentials that were not supplied to the import operation.
- D. Two independently scaled services were placed in one container group.

## LAB13-Q36 — Applied

The approved container image release setup finishes, yet the image release cannot publish a stable regional name for the container group's public endpoint. Which misconfiguration explains the mismatch?

- A. A credential was stored as a plain environment variable in the committed deployment definition.
- B. The requested DNS label is already used in the selected region.
- C. The design requires geo-replication while the registry uses a non-Premium SKU.
- D. Two independently scaled services were placed in one container group.

## LAB13-Q37 — Applied

An image release break/fix in the approved container image release fails when operators try to pass sensitive configuration without writing the clear value into ordinary output. Which diagnosis fits?

- A. A credential was stored as a plain environment variable in the committed deployment definition.
- B. A completed batch job uses Always and repeatedly starts again.
- C. The deployment uses the mutable latest tag and cannot prove which image content ran.
- D. The requested DNS label is already used in the selected region.

## LAB13-Q38 — Applied

The approved container image release troubleshooting scope is the image release need to control whether a terminated container restarts. Which condition should be corrected first?

- A. The requested CPU and memory combination is unavailable in the deployment region.
- B. A completed batch job uses Always and repeatedly starts again.
- C. The identity exists but has no permission to pull image content from the registry.
- D. A credential was stored as a plain environment variable in the committed deployment definition.

## LAB13-Q39 — Applied

The approved container image release result is partial because the image release cannot request CPU and memory values supported in the selected region. Which condition accounts for that result?

- A. The requested CPU and memory combination is unavailable in the deployment region.
- B. The deployment depends on an enabled registry admin password embedded in automation.
- C. The source registry requires credentials that were not supplied to the import operation.
- D. A completed batch job uses Always and repeatedly starts again.

## LAB13-Q40 — Applied

The image release evidence shows the approved container image release cannot prefer an identity-scoped image pull over long-lived registry credentials. Which root cause fits that evidence?

- A. The design requires geo-replication while the registry uses a non-Premium SKU.
- B. Two independently scaled services were placed in one container group.
- C. The deployment depends on an enabled registry admin password embedded in automation.
- D. The requested CPU and memory combination is unavailable in the deployment region.

## LAB13-Q41 — Advanced

The approved container image release forbids a partial image release result. Operators must first choose registry capabilities and throughput appropriate for the image workload and afterward confirm the approved container image release outcome. Which image release sequence is complete?

- A. First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.
- B. First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.
- C. First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.
- D. First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.

## LAB13-Q42 — Advanced

Only the approved container image release change needed to deploy by digest so later tag changes cannot move the release is allowed, and image release proof is mandatory. Which pair fits?

- A. First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp.
- B. First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.
- C. First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
- D. First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest.

## LAB13-Q43 — Advanced

The approved container image release runbook separates image release mutation from validation while it must let the runtime pull a private image without embedding an administrator password. Which sequence proves it cleanly?

- A. First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.
- B. First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.
- C. First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
- D. First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.

## LAB13-Q44 — Advanced

The approved container image release checkpoint requires both this image release outcome—copy an existing image into the registry without a local pull and push—and a read-only approved container image release state check. Which image release response is complete?

- A. First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.
- B. First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp.
- C. First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
- D. First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.

## LAB13-Q45 — Advanced

The approved container image release runbook must run sidecars inside one jointly managed execution unit, then retain image release read-back evidence. Which approved container image release pair completes both duties?

- A. First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.
- B. First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.
- C. First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.
- D. First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest.

## LAB13-Q46 — Advanced

To satisfy the image release requirement, operators must change the approved container image release configuration and prove it can publish a stable regional name for the container group's public endpoint. Which sequence is coherent?

- A. First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.
- B. First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest.
- C. First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.
- D. First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.

## LAB13-Q47 — Advanced

The container administrator publishing an approved image and running it in ACI needs a safe approved container image release change to pass sensitive configuration without writing the clear value into ordinary output, followed by image release evidence. Which pair merits approval?

- A. First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
- B. First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.
- C. First, Assign the pull role to the workload identity and reference the private registry without embedding a password. Then, List the identity's role assignment and confirm the deployed image resolves from the private login server.
- D. First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp.

## LAB13-Q48 — Advanced

The approved container image release has two image release gates: control whether a terminated container restarts, then prove the approved container image release state. Which image release sequence works?

- A. First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
- B. First, Import the approved source image into a uniquely versioned target repository and tag. Then, List the target repository and verify its tag, digest, and import timestamp.
- C. First, Set the restart policy from the workload's intended lifecycle and exit-code behavior. Then, Query restartPolicy, currentState, previousState, exitCode, and restartCount.
- D. First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.

## LAB13-Q49 — Advanced

Which image release path makes the approved container image release able to request CPU and memory values supported in the selected region, then inspects the defining properties?

- A. First, Choose the lowest registry SKU that meets throughput, storage, replication, and network-control requirements. Then, Query sku.name, provisioningState, loginServer, and configured premium features.
- B. First, Set explicit CPU and memory requests within the selected region's supported combinations. Then, Query each container's resources.requests and compare them with measured workload demand.
- C. First, Place tightly coupled containers in one group only when they should share deployment lifecycle and network namespace. Then, Query container group provisioningState, instanceView state, IP configuration, and each container status.
- D. First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.

## LAB13-Q50 — Advanced

At the approved container image release approval gate, operators must show that the image release can prefer an identity-scoped image pull over long-lived registry credentials. Which image release configure-and-check pair is defensible?

- A. First, Prefer managed identity for the container pull path and leave the registry admin account disabled. Then, Query adminUserEnabled and confirm the workload identity's scoped pull assignment.
- B. First, Use a unique version tag for delivery and retain the resolved digest for reproducible deployment evidence. Then, List repository manifests and match the selected tag to its sha256 digest.
- C. First, Check label availability and configure the DNS name label only for a deliberately public container group. Then, Query ipAddress.fqdn, type, ports, and the container's running state.
- D. First, Pass secret values through a transient secure mechanism and never commit them in scripts or run-state files. Then, Inspect the container definition and evidence output to confirm secret values are redacted.

[Open the answer key](./ANSWERS.md)
