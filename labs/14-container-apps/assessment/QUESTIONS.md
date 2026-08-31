# Lab 14 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB14-Q01 — Foundational

A revision rollout incident review of the revisioned serverless container release depends on the ability to place related apps inside one networking and logging boundary. Which platform description is reliable?

- A. A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision.
- B. Traffic weights route percentages to revisions or labels and must total 100 percent.
- C. A Container Apps environment is the secure boundary for apps that share networking and logging integration.
- D. Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale.

## LAB14-Q02 — Foundational

A platform administrator releasing a revisioned serverless container app is updating the revision rollout runbook. The requirement is to preserve an immutable snapshot whenever revision-scoped configuration changes. Which statement describes Azure behavior correctly?

- A. A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision.
- B. Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.
- C. The ingress target port must match the port on which the container process listens.
- D. Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.

## LAB14-Q03 — Foundational

A revision rollout peer review asks how the revisioned serverless container release should handle this outcome: move production to the newest ready version and retire the preceding active version. Which explanation is accurate?

- A. Multiple revision mode can keep several revisions active and divide traffic between them.
- B. External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path.
- C. Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.
- D. Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image.

## LAB14-Q04 — Foundational

For the revisioned serverless container release, the revision rollout plan must keep several versions active at the same time. Which statement about revision rollout belongs in the revisioned serverless container release record?

- A. Traffic weights route percentages to revisions or labels and must total 100 percent.
- B. Multiple revision mode can keep several revisions active and divide traffic between them.
- C. Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale.
- D. A Container Apps environment is the secure boundary for apps that share networking and logging integration.

## LAB14-Q05 — Foundational

The revision rollout review compares four claims for the revisioned serverless container release requirement to send controlled percentages of requests to two active versions. Which claim is technically sound?

- A. The ingress target port must match the port on which the container process listens.
- B. Traffic weights route percentages to revisions or labels and must total 100 percent.
- C. Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.
- D. A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision.

## LAB14-Q06 — Foundational

The revision rollout architecture note requires the revisioned serverless container release environment to route ingress to the port on which the container process actually listens. Which statement defines the relevant revision rollout boundary?

- A. External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path.
- B. Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image.
- C. The ingress target port must match the port on which the container process listens.
- D. Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.

## LAB14-Q07 — Foundational

A new revision rollout operator must explain why the revisioned serverless container release can choose whether the application endpoint is externally reachable or environment-internal. Which explanation is accurate?

- A. Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale.
- B. External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path.
- C. A Container Apps environment is the secure boundary for apps that share networking and logging integration.
- D. Multiple revision mode can keep several revisions active and divide traffic between them.

## LAB14-Q08 — Foundational

The revisioned serverless container release acceptance criteria require operators to keep required warm capacity while setting an upper scale limit. Which service fact supports that requirement?

- A. Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.
- B. A revision is an immutable snapshot of an app version, and revision-scope changes create a new revision.
- C. Traffic weights route percentages to revisions or labels and must total 100 percent.
- D. Minimum replicas control warm capacity and scale-to-zero, while maximum replicas cap horizontal scale.

## LAB14-Q09 — Foundational

A revision rollout reviewer challenges whether the revisioned serverless container release can translate HTTP or event demand into a desired replica count. Which response resolves the concern?

- A. Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image.
- B. Single revision mode sends traffic to the latest ready revision and deactivates the previous active revision after a successful update.
- C. The ingress target port must match the port on which the container process listens.
- D. Container Apps scale rules translate HTTP concurrency, KEDA events, or custom metrics into desired replica counts.

## LAB14-Q10 — Foundational

The revisioned serverless container release handoff omits the revision rollout rule needed to reference sensitive configuration without placing the clear value in ordinary settings. Which statement should the team add?

- A. A Container Apps environment is the secure boundary for apps that share networking and logging integration.
- B. Multiple revision mode can keep several revisions active and divide traffic between them.
- C. Container Apps secrets are referenced by configuration and environment variables without placing the secret value directly in the image.
- D. External ingress exposes the app through the environment endpoint, while internal ingress limits reachability to the environment network path.

## LAB14-Q11 — Foundational

The revisioned serverless container release plan must place related apps inside one networking and logging boundary while limiting the mutation scope to revision rollout. Which action is appropriate?

- A. Use single mode for straightforward replacement without simultaneous version traffic.
- B. Enable ingress with a target port that matches the application's listener.
- C. Create or select the managed environment before deploying the container app into it.
- D. Configure a rule with the correct type, metadata, authentication references, and scale bounds.

## LAB14-Q12 — Foundational

A revision rollout ticket in the revisioned serverless container release says to preserve an immutable snapshot whenever revision-scoped configuration changes. Which revision rollout action completes the revisioned serverless container release request with minimal change?

- A. Deploy the updated image or revision-scope settings and retain the resulting revision name.
- B. Enable multiple mode before configuring canary or blue-green traffic weights.
- C. Choose internal or external ingress from the approved client reachability requirement.
- D. Create the secret through a secure input path and reference its name from the container configuration.

## LAB14-Q13 — Foundational

The approach for the revisioned serverless container release is approved, but the revision rollout environment still cannot move production to the newest ready version and retire the preceding active version. Which implementation step closes the gap?

- A. Assign an explicit small canary weight and keep the stable revision at the remaining percentage.
- B. Use single mode for straightforward replacement without simultaneous version traffic.
- C. Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints.
- D. Create or select the managed environment before deploying the container app into it.

## LAB14-Q14 — Foundational

The platform administrator releasing a revisioned serverless container app may change the revisioned serverless container release only to keep several versions active at the same time. Which revision rollout action stays within that assignment?

- A. Enable ingress with a target port that matches the application's listener.
- B. Configure a rule with the correct type, metadata, authentication references, and scale bounds.
- C. Enable multiple mode before configuring canary or blue-green traffic weights.
- D. Deploy the updated image or revision-scope settings and retain the resulting revision name.

## LAB14-Q15 — Foundational

A revision rollout dry run shows no revisioned serverless container release command will send controlled percentages of requests to two active versions. Which action belongs before execution?

- A. Choose internal or external ingress from the approved client reachability requirement.
- B. Create the secret through a secure input path and reference its name from the container configuration.
- C. Use single mode for straightforward replacement without simultaneous version traffic.
- D. Assign an explicit small canary weight and keep the stable revision at the remaining percentage.

## LAB14-Q16 — Applied

For the revisioned serverless container release, operators need to route ingress to the port on which the container process actually listens. Which change realizes that requirement?

- A. Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints.
- B. Create or select the managed environment before deploying the container app into it.
- C. Enable multiple mode before configuring canary or blue-green traffic weights.
- D. Enable ingress with a target port that matches the application's listener.

## LAB14-Q17 — Applied

Operators must automate the revisioned serverless container release change needed to choose whether the application endpoint is externally reachable or environment-internal. Which revision rollout operation belongs in the runbook?

- A. Choose internal or external ingress from the approved client reachability requirement.
- B. Configure a rule with the correct type, metadata, authentication references, and scale bounds.
- C. Deploy the updated image or revision-scope settings and retain the resulting revision name.
- D. Assign an explicit small canary weight and keep the stable revision at the remaining percentage.

## LAB14-Q18 — Applied

A revisioned serverless container release review finds revision rollout drift from the need to keep required warm capacity while setting an upper scale limit. Which correction addresses that drift?

- A. Create the secret through a secure input path and reference its name from the container configuration.
- B. Use single mode for straightforward replacement without simultaneous version traffic.
- C. Enable ingress with a target port that matches the application's listener.
- D. Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints.

## LAB14-Q19 — Applied

The revisioned serverless container release window permits only the revision rollout change needed to translate HTTP or event demand into a desired replica count. Which option respects the boundary?

- A. Create or select the managed environment before deploying the container app into it.
- B. Enable multiple mode before configuring canary or blue-green traffic weights.
- C. Choose internal or external ingress from the approved client reachability requirement.
- D. Configure a rule with the correct type, metadata, authentication references, and scale bounds.

## LAB14-Q20 — Applied

The revision rollout preflight has passed; the revisioned serverless container release must now reference sensitive configuration without placing the clear value in ordinary settings. Which operation should run?

- A. Deploy the updated image or revision-scope settings and retain the resulting revision name.
- B. Assign an explicit small canary weight and keep the stable revision at the remaining percentage.
- C. Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints.
- D. Create the secret through a secure input path and reference its name from the container configuration.

## LAB14-Q21 — Applied

Before revisioned serverless container release cleanup, the revision rollout team must reconfirm it can place related apps inside one networking and logging boundary. Which read-only inspection should run?

- A. List active revisions and confirm their combined traffic percentages equal 100.
- B. Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
- C. Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
- D. Query secret references and confirm command output does not reveal the stored secret value.

## LAB14-Q22 — Applied

The revisioned serverless container release setup reports success after the revision rollout attempt to preserve an immutable snapshot whenever revision-scoped configuration changes. Which revision rollout read-only observation proves the revisioned serverless container release outcome?

- A. Query ingress.traffic and match revision names, labels, and exact weights.
- B. Query the active revision template scale bounds and current replica count.
- C. List revisions and compare image, createdTime, active state, health, and traffic weight.
- D. Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.

## LAB14-Q23 — Applied

The revision rollout log says the revisioned serverless container release can now move production to the newest ready version and retire the preceding active version. Which revision rollout state should the revisioned serverless container release acceptance test retain?

- A. Query ingress.targetPort and compare it with container startup logs and probe configuration.
- B. Query the revision's scale rules and inspect replica changes while generating controlled demand.
- C. List revisions and compare image, createdTime, active state, health, and traffic weight.
- D. Query activeRevisionsMode and confirm exactly the intended latest revision is active.

## LAB14-Q24 — Applied

The revisioned serverless container release rejects revision rollout exit status as proof it can keep several versions active at the same time. Which revisioned serverless container release result is valid evidence?

- A. Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
- B. Query secret references and confirm command output does not reveal the stored secret value.
- C. List active revisions and confirm their combined traffic percentages equal 100.
- D. Query activeRevisionsMode and confirm exactly the intended latest revision is active.

## LAB14-Q25 — Applied

The revision rollout validator needs one revisioned serverless container release query after the change to send controlled percentages of requests to two active versions. Which revision rollout property should the revisioned serverless container release validator inspect?

- A. Query ingress.traffic and match revision names, labels, and exact weights.
- B. Query the active revision template scale bounds and current replica count.
- C. Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
- D. List active revisions and confirm their combined traffic percentages equal 100.

## LAB14-Q26 — Applied

The platform administrator releasing a revisioned serverless container app must confirm the revisioned serverless container release, without mutation, can route ingress to the port on which the container process actually listens. Which revision rollout check qualifies?

- A. Query the revision's scale rules and inspect replica changes while generating controlled demand.
- B. List revisions and compare image, createdTime, active state, health, and traffic weight.
- C. Query ingress.traffic and match revision names, labels, and exact weights.
- D. Query ingress.targetPort and compare it with container startup logs and probe configuration.

## LAB14-Q27 — Applied

The revisioned serverless container release configuration is complete; the revision rollout reviewers need evidence it can choose whether the application endpoint is externally reachable or environment-internal. Which observation shows success?

- A. Query secret references and confirm command output does not reveal the stored secret value.
- B. Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
- C. Query activeRevisionsMode and confirm exactly the intended latest revision is active.
- D. Query ingress.targetPort and compare it with container startup logs and probe configuration.

## LAB14-Q28 — Applied

The revision rollout validation asks whether the revisioned serverless container release can keep required warm capacity while setting an upper scale limit. Which observable state is strongest?

- A. Query the active revision template scale bounds and current replica count.
- B. Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
- C. List active revisions and confirm their combined traffic percentages equal 100.
- D. Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.

## LAB14-Q29 — Applied

A revisioned serverless container release review must prove the revision rollout ability to translate HTTP or event demand into a desired replica count. Which check avoids an adjacent feature?

- A. Query the revision's scale rules and inspect replica changes while generating controlled demand.
- B. List revisions and compare image, createdTime, active state, health, and traffic weight.
- C. Query ingress.traffic and match revision names, labels, and exact weights.
- D. Query the active revision template scale bounds and current replica count.

## LAB14-Q30 — Applied

The revisioned serverless container release evidence bundle needs a revision rollout result showing it can reference sensitive configuration without placing the clear value in ordinary settings. Which result belongs in the checkpoint?

- A. Query secret references and confirm command output does not reveal the stored secret value.
- B. Query activeRevisionsMode and confirm exactly the intended latest revision is active.
- C. Query ingress.targetPort and compare it with container startup logs and probe configuration.
- D. Query the revision's scale rules and inspect replica changes while generating controlled demand.

## LAB14-Q31 — Applied

Other revisioned serverless container release components are healthy, but the revision rollout still cannot place related apps inside one networking and logging boundary. Which state causes the isolated failure?

- A. Validation queried only the app object and missed that the new revision is unhealthy.
- B. Ingress forwards to port 80 while the container process listens on port 8080.
- C. The environment variable contains the literal credential instead of a secret reference.
- D. The app deployment references an environment in a different region.

## LAB14-Q32 — Applied

During a revision rollout fault drill, the revisioned serverless container release does not preserve an immutable snapshot whenever revision-scoped configuration changes. Which finding identifies the defect?

- A. The new revision never becomes ready, so the earlier revision remains serving traffic.
- B. Validation queried only the app object and missed that the new revision is unhealthy.
- C. External ingress was enabled for a service intended to be reachable only inside the environment.
- D. The app deployment references an environment in a different region.

## LAB14-Q33 — Applied

The revisioned serverless container release setup finishes, yet the revision rollout cannot move production to the newest ready version and retire the preceding active version. Which misconfiguration explains the mismatch?

- A. The new revision never becomes ready, so the earlier revision remains serving traffic.
- B. The app remains in single revision mode while the runbook attempts a traffic split.
- C. minReplicas is zero even though the workload requires one continuously warm instance.
- D. Validation queried only the app object and missed that the new revision is unhealthy.

## LAB14-Q34 — Applied

A revision rollout break/fix in the revisioned serverless container release fails when operators try to keep several versions active at the same time. Which diagnosis fits?

- A. The app remains in single revision mode while the runbook attempts a traffic split.
- B. The configured traffic weights total more than 100 percent.
- C. The rule metadata names a secret that is not defined for the container app.
- D. The new revision never becomes ready, so the earlier revision remains serving traffic.

## LAB14-Q35 — Applied

The revisioned serverless container release troubleshooting scope is the revision rollout need to send controlled percentages of requests to two active versions. Which condition should be corrected first?

- A. Ingress forwards to port 80 while the container process listens on port 8080.
- B. The environment variable contains the literal credential instead of a secret reference.
- C. The configured traffic weights total more than 100 percent.
- D. The app remains in single revision mode while the runbook attempts a traffic split.

## LAB14-Q36 — Applied

The revisioned serverless container release result is partial because the revision rollout cannot route ingress to the port on which the container process actually listens. Which condition accounts for that result?

- A. External ingress was enabled for a service intended to be reachable only inside the environment.
- B. The app deployment references an environment in a different region.
- C. Ingress forwards to port 80 while the container process listens on port 8080.
- D. The configured traffic weights total more than 100 percent.

## LAB14-Q37 — Applied

The revision rollout evidence shows the revisioned serverless container release cannot choose whether the application endpoint is externally reachable or environment-internal. Which root cause fits that evidence?

- A. minReplicas is zero even though the workload requires one continuously warm instance.
- B. External ingress was enabled for a service intended to be reachable only inside the environment.
- C. Validation queried only the app object and missed that the new revision is unhealthy.
- D. Ingress forwards to port 80 while the container process listens on port 8080.

## LAB14-Q38 — Applied

Although the revisioned serverless container release is meant to let the revision rollout keep required warm capacity while setting an upper scale limit, its checkpoint fails. Which revision rollout defect explains the failure?

- A. The rule metadata names a secret that is not defined for the container app.
- B. The new revision never becomes ready, so the earlier revision remains serving traffic.
- C. minReplicas is zero even though the workload requires one continuously warm instance.
- D. External ingress was enabled for a service intended to be reachable only inside the environment.

## LAB14-Q39 — Applied

The revision rollout support team isolated the revisioned serverless container release incident to the attempt to translate HTTP or event demand into a desired replica count. Which condition prevents success?

- A. The rule metadata names a secret that is not defined for the container app.
- B. The environment variable contains the literal credential instead of a secret reference.
- C. The app remains in single revision mode while the runbook attempts a traffic split.
- D. minReplicas is zero even though the workload requires one continuously warm instance.

## LAB14-Q40 — Applied

A revisioned serverless container release query surprises the platform administrator releasing a revisioned serverless container app during the revision rollout attempt to reference sensitive configuration without placing the clear value in ordinary settings. Which finding explains it?

- A. The app deployment references an environment in a different region.
- B. The environment variable contains the literal credential instead of a secret reference.
- C. The configured traffic weights total more than 100 percent.
- D. The rule metadata names a secret that is not defined for the container app.

## LAB14-Q41 — Advanced

The revisioned serverless container release checkpoint requires both this revision rollout outcome—place related apps inside one networking and logging boundary—and a read-only revisioned serverless container release state check. Which revision rollout response is complete?

- A. First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
- B. First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
- C. First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
- D. First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.

## LAB14-Q42 — Advanced

The revisioned serverless container release runbook must preserve an immutable snapshot whenever revision-scoped configuration changes, then retain revision rollout read-back evidence. Which revisioned serverless container release pair completes both duties?

- A. First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100.
- B. First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.
- C. First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.
- D. First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.

## LAB14-Q43 — Advanced

To satisfy the revision rollout requirement, operators must change the revisioned serverless container release configuration and prove it can move production to the newest ready version and retire the preceding active version. Which sequence is coherent?

- A. First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights.
- B. First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
- C. First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.
- D. First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value.

## LAB14-Q44 — Advanced

The platform administrator releasing a revisioned serverless container app needs a safe revisioned serverless container release change to keep several versions active at the same time, followed by revision rollout evidence. Which pair merits approval?

- A. First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration.
- B. First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100.
- C. First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value.
- D. First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.

## LAB14-Q45 — Advanced

The revisioned serverless container release has two revision rollout gates: send controlled percentages of requests to two active versions, then prove the revisioned serverless container release state. Which revision rollout sequence works?

- A. First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights.
- B. First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
- C. First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
- D. First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.

## LAB14-Q46 — Advanced

Which revision rollout path makes the revisioned serverless container release able to route ingress to the port on which the container process actually listens, then inspects the defining properties?

- A. First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.
- B. First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.
- C. First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
- D. First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration.

## LAB14-Q47 — Advanced

At the revisioned serverless container release approval gate, operators must show that the revision rollout can choose whether the application endpoint is externally reachable or environment-internal. Which revision rollout configure-and-check pair is defensible?

- A. First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
- B. First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.
- C. First, Use single mode for straightforward replacement without simultaneous version traffic. Then, Query activeRevisionsMode and confirm exactly the intended latest revision is active.
- D. First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100.

## LAB14-Q48 — Advanced

The revisioned serverless container release forbids a partial revision rollout result. Operators must first keep required warm capacity while setting an upper scale limit and afterward confirm the revisioned serverless container release outcome. Which revision rollout sequence is complete?

- A. First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value.
- B. First, Enable multiple mode before configuring canary or blue-green traffic weights. Then, List active revisions and confirm their combined traffic percentages equal 100.
- C. First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights.
- D. First, Set minReplicas and maxReplicas from availability, cold-start, cost, and capacity constraints. Then, Query the active revision template scale bounds and current replica count.

## LAB14-Q49 — Advanced

Only the revisioned serverless container release change needed to translate HTTP or event demand into a desired replica count is allowed, and revision rollout proof is mandatory. Which pair fits?

- A. First, Create or select the managed environment before deploying the container app into it. Then, Query managedEnvironmentId, provisioningState, defaultDomain, and logging configuration.
- B. First, Assign an explicit small canary weight and keep the stable revision at the remaining percentage. Then, Query ingress.traffic and match revision names, labels, and exact weights.
- C. First, Configure a rule with the correct type, metadata, authentication references, and scale bounds. Then, Query the revision's scale rules and inspect replica changes while generating controlled demand.
- D. First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration.

## LAB14-Q50 — Advanced

The revisioned serverless container release runbook separates revision rollout mutation from validation while it must reference sensitive configuration without placing the clear value in ordinary settings. Which sequence proves it cleanly?

- A. First, Deploy the updated image or revision-scope settings and retain the resulting revision name. Then, List revisions and compare image, createdTime, active state, health, and traffic weight.
- B. First, Enable ingress with a target port that matches the application's listener. Then, Query ingress.targetPort and compare it with container startup logs and probe configuration.
- C. First, Choose internal or external ingress from the approved client reachability requirement. Then, Query ingress.external, fqdn, transport, and targetPort, then test from an appropriate network location.
- D. First, Create the secret through a secure input path and reference its name from the container configuration. Then, Query secret references and confirm command output does not reveal the stored secret value.

[Open the answer key](./ANSWERS.md)
