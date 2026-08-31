# Lab 15 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB15-Q01 — Foundational

For the App Service capacity and slot release, the slot release plan must understand which web apps share workers and scale together. Which statement about slot release belongs in the App Service capacity and slot release record?

- A. The App Service plan tier controls worker capability and features such as deployment slots, autoscale, backups, and private endpoints.
- B. Metric autoscale uses threshold, aggregation, duration, cooldown, and capacity settings to adjust plan instances.
- C. Swap with preview applies target-slot configuration to the source for validation before completing the swap.
- D. Apps in one App Service plan share the plan's compute workers, region, operating-system type, and scaling boundary.

## LAB15-Q02 — Foundational

The slot release review compares four claims for the App Service capacity and slot release requirement to select a hosting tier that supplies the required production capabilities. Which claim is technically sound?

- A. Scaling up changes the App Service plan worker size or pricing tier for all apps on that plan.
- B. The App Service plan tier controls worker capability and features such as deployment slots, autoscale, backups, and private endpoints.
- C. A deployment slot is a live app with its own hostname and configurable settings that can be swapped with another slot.
- D. An App Service app must match its plan's region and operating-system type and has a globally unique default hostname.

## LAB15-Q03 — Foundational

The slot release architecture note requires the App Service capacity and slot release environment to increase worker CPU or memory without adding worker instances. Which statement defines the relevant slot release boundary?

- A. Scaling up changes the App Service plan worker size or pricing tier for all apps on that plan.
- B. Scaling out changes the number of worker instances available to apps on an App Service plan.
- C. A deployment-slot setting remains with its slot during a swap instead of moving with swappable configuration.
- D. Per-app scaling on supported plans controls how many plan workers a specific app can use but does not create a separate plan.

## LAB15-Q04 — Foundational

A new slot release operator must explain why the App Service capacity and slot release can add worker instances without changing the worker size. Which explanation is accurate?

- A. Metric autoscale uses threshold, aggregation, duration, cooldown, and capacity settings to adjust plan instances.
- B. Swap with preview applies target-slot configuration to the source for validation before completing the swap.
- C. Apps in one App Service plan share the plan's compute workers, region, operating-system type, and scaling boundary.
- D. Scaling out changes the number of worker instances available to apps on an App Service plan.

## LAB15-Q05 — Foundational

The App Service capacity and slot release acceptance criteria require operators to change instance count automatically when the selected signal crosses a threshold. Which service fact supports that requirement?

- A. A deployment slot is a live app with its own hostname and configurable settings that can be swapped with another slot.
- B. An App Service app must match its plan's region and operating-system type and has a globally unique default hostname.
- C. Metric autoscale uses threshold, aggregation, duration, cooldown, and capacity settings to adjust plan instances.
- D. The App Service plan tier controls worker capability and features such as deployment slots, autoscale, backups, and private endpoints.

## LAB15-Q06 — Foundational

A slot release reviewer challenges whether the App Service capacity and slot release can deploy a candidate release to a live URL that is separate from production. Which response resolves the concern?

- A. A deployment-slot setting remains with its slot during a swap instead of moving with swappable configuration.
- B. A deployment slot is a live app with its own hostname and configurable settings that can be swapped with another slot.
- C. Per-app scaling on supported plans controls how many plan workers a specific app can use but does not create a separate plan.
- D. Scaling up changes the App Service plan worker size or pricing tier for all apps on that plan.

## LAB15-Q07 — Foundational

The App Service capacity and slot release handoff omits the slot release rule needed to prevent environment-only configuration from moving when slots exchange content. Which statement should the team add?

- A. Swap with preview applies target-slot configuration to the source for validation before completing the swap.
- B. A deployment-slot setting remains with its slot during a swap instead of moving with swappable configuration.
- C. Apps in one App Service plan share the plan's compute workers, region, operating-system type, and scaling boundary.
- D. Scaling out changes the number of worker instances available to apps on an App Service plan.

## LAB15-Q08 — Foundational

A slot release incident review of the App Service capacity and slot release depends on the ability to validate swap behavior before the candidate becomes production. Which platform description is reliable?

- A. An App Service app must match its plan's region and operating-system type and has a globally unique default hostname.
- B. The App Service plan tier controls worker capability and features such as deployment slots, autoscale, backups, and private endpoints.
- C. Swap with preview applies target-slot configuration to the source for validation before completing the swap.
- D. Metric autoscale uses threshold, aggregation, duration, cooldown, and capacity settings to adjust plan instances.

## LAB15-Q09 — Foundational

An application-platform administrator operating App Service capacity and releases is updating the slot release runbook. The requirement is to create an application inside the intended existing hosting plan. Which statement describes Azure behavior correctly?

- A. Per-app scaling on supported plans controls how many plan workers a specific app can use but does not create a separate plan.
- B. An App Service app must match its plan's region and operating-system type and has a globally unique default hostname.
- C. Scaling up changes the App Service plan worker size or pricing tier for all apps on that plan.
- D. A deployment slot is a live app with its own hostname and configurable settings that can be swapped with another slot.

## LAB15-Q10 — Foundational

A slot release peer review asks how the App Service capacity and slot release should handle this outcome: limit how many shared-plan workers one application may use. Which explanation is accurate?

- A. Apps in one App Service plan share the plan's compute workers, region, operating-system type, and scaling boundary.
- B. Scaling out changes the number of worker instances available to apps on an App Service plan.
- C. Per-app scaling on supported plans controls how many plan workers a specific app can use but does not create a separate plan.
- D. A deployment-slot setting remains with its slot during a swap instead of moving with swappable configuration.

## LAB15-Q11 — Foundational

The application-platform administrator operating App Service capacity and releases may change the App Service capacity and slot release only to understand which web apps share workers and scale together. Which slot release action stays within that assignment?

- A. Place apps together only when shared capacity, region, OS, cost, and scale behavior are acceptable.
- B. Scale up when each worker needs more CPU, memory, or tier-specific capability.
- C. Deploy and validate a release in a staging slot before swapping it into production.
- D. Create the app in the intended plan with a supported runtime and unique name.

## LAB15-Q12 — Foundational

A slot release dry run shows no App Service capacity and slot release command will select a hosting tier that supplies the required production capabilities. Which action belongs before execution?

- A. Increase capacity or configure autoscale when concurrent demand requires more workers.
- B. Select a tier that supports every required feature before creating dependent configuration.
- C. Mark environment-specific connection and app settings as slot settings before the swap.
- D. Enable and limit per-app scaling only when supported and justified by shared-plan capacity design.

## LAB15-Q13 — Foundational

For the App Service capacity and slot release, operators need to increase worker CPU or memory without adding worker instances. Which change realizes that requirement?

- A. Create complementary scale-out and scale-in rules with nonoverlapping thresholds and safe cooldowns.
- B. Use preview when the release must be tested with production configuration before cutover.
- C. Place apps together only when shared capacity, region, OS, cost, and scale behavior are acceptable.
- D. Scale up when each worker needs more CPU, memory, or tier-specific capability.

## LAB15-Q14 — Foundational

Operators must automate the App Service capacity and slot release change needed to add worker instances without changing the worker size. Which slot release operation belongs in the runbook?

- A. Deploy and validate a release in a staging slot before swapping it into production.
- B. Create the app in the intended plan with a supported runtime and unique name.
- C. Select a tier that supports every required feature before creating dependent configuration.
- D. Increase capacity or configure autoscale when concurrent demand requires more workers.

## LAB15-Q15 — Foundational

An App Service capacity and slot release review finds slot release drift from the need to change instance count automatically when the selected signal crosses a threshold. Which correction addresses that drift?

- A. Create complementary scale-out and scale-in rules with nonoverlapping thresholds and safe cooldowns.
- B. Mark environment-specific connection and app settings as slot settings before the swap.
- C. Enable and limit per-app scaling only when supported and justified by shared-plan capacity design.
- D. Scale up when each worker needs more CPU, memory, or tier-specific capability.

## LAB15-Q16 — Applied

The App Service capacity and slot release window permits only the slot release change needed to deploy a candidate release to a live URL that is separate from production. Which option respects the boundary?

- A. Deploy and validate a release in a staging slot before swapping it into production.
- B. Use preview when the release must be tested with production configuration before cutover.
- C. Place apps together only when shared capacity, region, OS, cost, and scale behavior are acceptable.
- D. Increase capacity or configure autoscale when concurrent demand requires more workers.

## LAB15-Q17 — Applied

The slot release preflight has passed; the App Service capacity and slot release must now prevent environment-only configuration from moving when slots exchange content. Which operation should run?

- A. Create the app in the intended plan with a supported runtime and unique name.
- B. Select a tier that supports every required feature before creating dependent configuration.
- C. Mark environment-specific connection and app settings as slot settings before the swap.
- D. Create complementary scale-out and scale-in rules with nonoverlapping thresholds and safe cooldowns.

## LAB15-Q18 — Applied

The App Service capacity and slot release plan must validate swap behavior before the candidate becomes production while limiting the mutation scope to slot release. Which action is appropriate?

- A. Use preview when the release must be tested with production configuration before cutover.
- B. Enable and limit per-app scaling only when supported and justified by shared-plan capacity design.
- C. Scale up when each worker needs more CPU, memory, or tier-specific capability.
- D. Deploy and validate a release in a staging slot before swapping it into production.

## LAB15-Q19 — Applied

A slot release ticket in the App Service capacity and slot release says to create an application inside the intended existing hosting plan. Which slot release action completes the App Service capacity and slot release request with minimal change?

- A. Place apps together only when shared capacity, region, OS, cost, and scale behavior are acceptable.
- B. Create the app in the intended plan with a supported runtime and unique name.
- C. Increase capacity or configure autoscale when concurrent demand requires more workers.
- D. Mark environment-specific connection and app settings as slot settings before the swap.

## LAB15-Q20 — Applied

The approach for the App Service capacity and slot release is approved, but the slot release environment still cannot limit how many shared-plan workers one application may use. Which implementation step closes the gap?

- A. Select a tier that supports every required feature before creating dependent configuration.
- B. Enable and limit per-app scaling only when supported and justified by shared-plan capacity design.
- C. Create complementary scale-out and scale-in rules with nonoverlapping thresholds and safe cooldowns.
- D. Use preview when the release must be tested with production configuration before cutover.

## LAB15-Q21 — Applied

The App Service capacity and slot release rejects slot release exit status as proof it can understand which web apps share workers and scale together. Which App Service capacity and slot release result is valid evidence?

- A. Query sku.capacity and active worker metrics after the scale operation.
- B. Query slotConfigNames and compare each slot's effective setting after a test swap.
- C. Query perSiteScaling on the plan and the app's siteConfig.numberOfWorkers value.
- D. Query each app's serverFarmId and confirm the plan's region, reserved flag, SKU, and worker count.

## LAB15-Q22 — Applied

The slot release validator needs one App Service capacity and slot release query after the change to select a hosting tier that supplies the required production capabilities. Which slot release property should the App Service capacity and slot release validator inspect?

- A. Query sku.name, sku.tier, capacity, and the availability of each required feature.
- B. Query the autoscale profile, capacity bounds, metric resource ID, rules, and enabled state.
- C. Inspect the swap phase and validate the warmed source slot before completing or resetting.
- D. Query each app's serverFarmId and confirm the plan's region, reserved flag, SKU, and worker count.

## LAB15-Q23 — Applied

The application-platform administrator operating App Service capacity and releases must confirm the App Service capacity and slot release, without mutation, can increase worker CPU or memory without adding worker instances. Which slot release check qualifies?

- A. List slots and query staging state, hostname, deployment content, and health independently.
- B. Query the plan SKU after the change and compare app health and cost impact.
- C. Query state, hostNames, serverFarmId, httpsOnly, and siteConfig runtime values.
- D. Query sku.name, sku.tier, capacity, and the availability of each required feature.

## LAB15-Q24 — Applied

The App Service capacity and slot release configuration is complete; the slot release reviewers need evidence it can add worker instances without changing the worker size. Which observation shows success?

- A. Query slotConfigNames and compare each slot's effective setting after a test swap.
- B. Query sku.capacity and active worker metrics after the scale operation.
- C. Query perSiteScaling on the plan and the app's siteConfig.numberOfWorkers value.
- D. Query the plan SKU after the change and compare app health and cost impact.

## LAB15-Q25 — Applied

The slot release validation asks whether the App Service capacity and slot release can change instance count automatically when the selected signal crosses a threshold. Which observable state is strongest?

- A. Inspect the swap phase and validate the warmed source slot before completing or resetting.
- B. Query each app's serverFarmId and confirm the plan's region, reserved flag, SKU, and worker count.
- C. Query the autoscale profile, capacity bounds, metric resource ID, rules, and enabled state.
- D. Query sku.capacity and active worker metrics after the scale operation.

## LAB15-Q26 — Applied

An App Service capacity and slot release review must prove the slot release ability to deploy a candidate release to a live URL that is separate from production. Which check avoids an adjacent feature?

- A. List slots and query staging state, hostname, deployment content, and health independently.
- B. Query state, hostNames, serverFarmId, httpsOnly, and siteConfig runtime values.
- C. Query sku.name, sku.tier, capacity, and the availability of each required feature.
- D. Query the autoscale profile, capacity bounds, metric resource ID, rules, and enabled state.

## LAB15-Q27 — Applied

The App Service capacity and slot release evidence bundle needs a slot release result showing it can prevent environment-only configuration from moving when slots exchange content. Which result belongs in the checkpoint?

- A. Query perSiteScaling on the plan and the app's siteConfig.numberOfWorkers value.
- B. Query slotConfigNames and compare each slot's effective setting after a test swap.
- C. Query the plan SKU after the change and compare app health and cost impact.
- D. List slots and query staging state, hostname, deployment content, and health independently.

## LAB15-Q28 — Applied

Before App Service capacity and slot release cleanup, the slot release team must reconfirm it can validate swap behavior before the candidate becomes production. Which read-only inspection should run?

- A. Inspect the swap phase and validate the warmed source slot before completing or resetting.
- B. Query each app's serverFarmId and confirm the plan's region, reserved flag, SKU, and worker count.
- C. Query sku.capacity and active worker metrics after the scale operation.
- D. Query slotConfigNames and compare each slot's effective setting after a test swap.

## LAB15-Q29 — Applied

The App Service capacity and slot release setup reports success after the slot release attempt to create an application inside the intended existing hosting plan. Which slot release read-only observation proves the App Service capacity and slot release outcome?

- A. Query sku.name, sku.tier, capacity, and the availability of each required feature.
- B. Query the autoscale profile, capacity bounds, metric resource ID, rules, and enabled state.
- C. Query state, hostNames, serverFarmId, httpsOnly, and siteConfig runtime values.
- D. Inspect the swap phase and validate the warmed source slot before completing or resetting.

## LAB15-Q30 — Applied

The slot release log says the App Service capacity and slot release can now limit how many shared-plan workers one application may use. Which slot release state should the App Service capacity and slot release acceptance test retain?

- A. Query the plan SKU after the change and compare app health and cost impact.
- B. List slots and query staging state, hostname, deployment content, and health independently.
- C. Query state, hostNames, serverFarmId, httpsOnly, and siteConfig runtime values.
- D. Query perSiteScaling on the plan and the app's siteConfig.numberOfWorkers value.

## LAB15-Q31 — Applied

A slot release break/fix in the App Service capacity and slot release fails when operators try to understand which web apps share workers and scale together. Which diagnosis fits?

- A. The selected tier does not support the requested deployment slots.
- B. The release was deployed directly to production, leaving no isolated slot validation path.
- C. The app requests more workers than the shared plan currently provides.
- D. A workload needing independent scaling shares a plan with an unrelated production app.

## LAB15-Q32 — Applied

The App Service capacity and slot release troubleshooting scope is the slot release need to select a hosting tier that supplies the required production capabilities. Which condition should be corrected first?

- A. The selected tier does not support the requested deployment slots.
- B. The change request expects scale-up to add worker instances without changing worker size.
- C. A production-only connection string is swappable and moves into the staging slot.
- D. A workload needing independent scaling shares a plan with an unrelated production app.

## LAB15-Q33 — Applied

The App Service capacity and slot release result is partial because the slot release cannot increase worker CPU or memory without adding worker instances. Which condition accounts for that result?

- A. The plan was scaled to a larger worker size but instance count remained one.
- B. The preview was completed without validating the source slot under target configuration.
- C. The selected tier does not support the requested deployment slots.
- D. The change request expects scale-up to add worker instances without changing worker size.

## LAB15-Q34 — Applied

The slot release evidence shows the App Service capacity and slot release cannot add worker instances without changing the worker size. Which root cause fits that evidence?

- A. The scale-out rule exists, but maximum capacity prevents adding another instance.
- B. A Linux runtime was requested on a Windows App Service plan.
- C. The plan was scaled to a larger worker size but instance count remained one.
- D. The change request expects scale-up to add worker instances without changing worker size.

## LAB15-Q35 — Applied

Although the App Service capacity and slot release is meant to let the slot release change instance count automatically when the selected signal crosses a threshold, its checkpoint fails. Which slot release defect explains the failure?

- A. The release was deployed directly to production, leaving no isolated slot validation path.
- B. The app requests more workers than the shared plan currently provides.
- C. The scale-out rule exists, but maximum capacity prevents adding another instance.
- D. The plan was scaled to a larger worker size but instance count remained one.

## LAB15-Q36 — Applied

The slot release support team isolated the App Service capacity and slot release incident to the attempt to deploy a candidate release to a live URL that is separate from production. Which condition prevents success?

- A. A production-only connection string is swappable and moves into the staging slot.
- B. A workload needing independent scaling shares a plan with an unrelated production app.
- C. The scale-out rule exists, but maximum capacity prevents adding another instance.
- D. The release was deployed directly to production, leaving no isolated slot validation path.

## LAB15-Q37 — Applied

An App Service capacity and slot release query surprises the application-platform administrator operating App Service capacity and releases during the slot release attempt to prevent environment-only configuration from moving when slots exchange content. Which finding explains it?

- A. The preview was completed without validating the source slot under target configuration.
- B. The selected tier does not support the requested deployment slots.
- C. A production-only connection string is swappable and moves into the staging slot.
- D. The release was deployed directly to production, leaving no isolated slot validation path.

## LAB15-Q38 — Applied

Other App Service capacity and slot release components are healthy, but the slot release still cannot validate swap behavior before the candidate becomes production. Which state causes the isolated failure?

- A. The preview was completed without validating the source slot under target configuration.
- B. A Linux runtime was requested on a Windows App Service plan.
- C. The change request expects scale-up to add worker instances without changing worker size.
- D. A production-only connection string is swappable and moves into the staging slot.

## LAB15-Q39 — Applied

During a slot release fault drill, the App Service capacity and slot release does not create an application inside the intended existing hosting plan. Which finding identifies the defect?

- A. A Linux runtime was requested on a Windows App Service plan.
- B. The app requests more workers than the shared plan currently provides.
- C. The plan was scaled to a larger worker size but instance count remained one.
- D. The preview was completed without validating the source slot under target configuration.

## LAB15-Q40 — Applied

The App Service capacity and slot release setup finishes, yet the slot release cannot limit how many shared-plan workers one application may use. Which misconfiguration explains the mismatch?

- A. A workload needing independent scaling shares a plan with an unrelated production app.
- B. The app requests more workers than the shared plan currently provides.
- C. The scale-out rule exists, but maximum capacity prevents adding another instance.
- D. A Linux runtime was requested on a Windows App Service plan.

## LAB15-Q41 — Advanced

The application-platform administrator operating App Service capacity and releases needs a safe App Service capacity and slot release change to understand which web apps share workers and scale together, followed by slot release evidence. Which pair merits approval?

- A. First, Scale up when each worker needs more CPU, memory, or tier-specific capability. Then, Query the plan SKU after the change and compare app health and cost impact.
- B. First, Place apps together only when shared capacity, region, OS, cost, and scale behavior are acceptable. Then, Query each app's serverFarmId and confirm the plan's region, reserved flag, SKU, and worker count.
- C. First, Mark environment-specific connection and app settings as slot settings before the swap. Then, Query slotConfigNames and compare each slot's effective setting after a test swap.
- D. First, Use preview when the release must be tested with production configuration before cutover. Then, Inspect the swap phase and validate the warmed source slot before completing or resetting.

## LAB15-Q42 — Advanced

The App Service capacity and slot release has two slot release gates: select a hosting tier that supplies the required production capabilities, then prove the App Service capacity and slot release state. Which slot release sequence works?

- A. First, Increase capacity or configure autoscale when concurrent demand requires more workers. Then, Query sku.capacity and active worker metrics after the scale operation.
- B. First, Use preview when the release must be tested with production configuration before cutover. Then, Inspect the swap phase and validate the warmed source slot before completing or resetting.
- C. First, Select a tier that supports every required feature before creating dependent configuration. Then, Query sku.name, sku.tier, capacity, and the availability of each required feature.
- D. First, Create the app in the intended plan with a supported runtime and unique name. Then, Query state, hostNames, serverFarmId, httpsOnly, and siteConfig runtime values.

## LAB15-Q43 — Advanced

Which slot release path makes the App Service capacity and slot release able to increase worker CPU or memory without adding worker instances, then inspects the defining properties?

- A. First, Create complementary scale-out and scale-in rules with nonoverlapping thresholds and safe cooldowns. Then, Query the autoscale profile, capacity bounds, metric resource ID, rules, and enabled state.
- B. First, Create the app in the intended plan with a supported runtime and unique name. Then, Query state, hostNames, serverFarmId, httpsOnly, and siteConfig runtime values.
- C. First, Enable and limit per-app scaling only when supported and justified by shared-plan capacity design. Then, Query perSiteScaling on the plan and the app's siteConfig.numberOfWorkers value.
- D. First, Scale up when each worker needs more CPU, memory, or tier-specific capability. Then, Query the plan SKU after the change and compare app health and cost impact.

## LAB15-Q44 — Advanced

At the App Service capacity and slot release approval gate, operators must show that the slot release can add worker instances without changing the worker size. Which slot release configure-and-check pair is defensible?

- A. First, Deploy and validate a release in a staging slot before swapping it into production. Then, List slots and query staging state, hostname, deployment content, and health independently.
- B. First, Enable and limit per-app scaling only when supported and justified by shared-plan capacity design. Then, Query perSiteScaling on the plan and the app's siteConfig.numberOfWorkers value.
- C. First, Increase capacity or configure autoscale when concurrent demand requires more workers. Then, Query sku.capacity and active worker metrics after the scale operation.
- D. First, Place apps together only when shared capacity, region, OS, cost, and scale behavior are acceptable. Then, Query each app's serverFarmId and confirm the plan's region, reserved flag, SKU, and worker count.

## LAB15-Q45 — Advanced

The App Service capacity and slot release forbids a partial slot release result. Operators must first change instance count automatically when the selected signal crosses a threshold and afterward confirm the App Service capacity and slot release outcome. Which slot release sequence is complete?

- A. First, Mark environment-specific connection and app settings as slot settings before the swap. Then, Query slotConfigNames and compare each slot's effective setting after a test swap.
- B. First, Place apps together only when shared capacity, region, OS, cost, and scale behavior are acceptable. Then, Query each app's serverFarmId and confirm the plan's region, reserved flag, SKU, and worker count.
- C. First, Select a tier that supports every required feature before creating dependent configuration. Then, Query sku.name, sku.tier, capacity, and the availability of each required feature.
- D. First, Create complementary scale-out and scale-in rules with nonoverlapping thresholds and safe cooldowns. Then, Query the autoscale profile, capacity bounds, metric resource ID, rules, and enabled state.

## LAB15-Q46 — Advanced

Only the App Service capacity and slot release change needed to deploy a candidate release to a live URL that is separate from production is allowed, and slot release proof is mandatory. Which pair fits?

- A. First, Use preview when the release must be tested with production configuration before cutover. Then, Inspect the swap phase and validate the warmed source slot before completing or resetting.
- B. First, Select a tier that supports every required feature before creating dependent configuration. Then, Query sku.name, sku.tier, capacity, and the availability of each required feature.
- C. First, Scale up when each worker needs more CPU, memory, or tier-specific capability. Then, Query the plan SKU after the change and compare app health and cost impact.
- D. First, Deploy and validate a release in a staging slot before swapping it into production. Then, List slots and query staging state, hostname, deployment content, and health independently.

## LAB15-Q47 — Advanced

The App Service capacity and slot release runbook separates slot release mutation from validation while it must prevent environment-only configuration from moving when slots exchange content. Which sequence proves it cleanly?

- A. First, Mark environment-specific connection and app settings as slot settings before the swap. Then, Query slotConfigNames and compare each slot's effective setting after a test swap.
- B. First, Create the app in the intended plan with a supported runtime and unique name. Then, Query state, hostNames, serverFarmId, httpsOnly, and siteConfig runtime values.
- C. First, Scale up when each worker needs more CPU, memory, or tier-specific capability. Then, Query the plan SKU after the change and compare app health and cost impact.
- D. First, Increase capacity or configure autoscale when concurrent demand requires more workers. Then, Query sku.capacity and active worker metrics after the scale operation.

## LAB15-Q48 — Advanced

The App Service capacity and slot release checkpoint requires both this slot release outcome—validate swap behavior before the candidate becomes production—and a read-only App Service capacity and slot release state check. Which slot release response is complete?

- A. First, Use preview when the release must be tested with production configuration before cutover. Then, Inspect the swap phase and validate the warmed source slot before completing or resetting.
- B. First, Enable and limit per-app scaling only when supported and justified by shared-plan capacity design. Then, Query perSiteScaling on the plan and the app's siteConfig.numberOfWorkers value.
- C. First, Increase capacity or configure autoscale when concurrent demand requires more workers. Then, Query sku.capacity and active worker metrics after the scale operation.
- D. First, Create complementary scale-out and scale-in rules with nonoverlapping thresholds and safe cooldowns. Then, Query the autoscale profile, capacity bounds, metric resource ID, rules, and enabled state.

## LAB15-Q49 — Advanced

The App Service capacity and slot release runbook must create an application inside the intended existing hosting plan, then retain slot release read-back evidence. Which App Service capacity and slot release pair completes both duties?

- A. First, Place apps together only when shared capacity, region, OS, cost, and scale behavior are acceptable. Then, Query each app's serverFarmId and confirm the plan's region, reserved flag, SKU, and worker count.
- B. First, Create complementary scale-out and scale-in rules with nonoverlapping thresholds and safe cooldowns. Then, Query the autoscale profile, capacity bounds, metric resource ID, rules, and enabled state.
- C. First, Create the app in the intended plan with a supported runtime and unique name. Then, Query state, hostNames, serverFarmId, httpsOnly, and siteConfig runtime values.
- D. First, Deploy and validate a release in a staging slot before swapping it into production. Then, List slots and query staging state, hostname, deployment content, and health independently.

## LAB15-Q50 — Advanced

To satisfy the slot release requirement, operators must change the App Service capacity and slot release configuration and prove it can limit how many shared-plan workers one application may use. Which sequence is coherent?

- A. First, Select a tier that supports every required feature before creating dependent configuration. Then, Query sku.name, sku.tier, capacity, and the availability of each required feature.
- B. First, Deploy and validate a release in a staging slot before swapping it into production. Then, List slots and query staging state, hostname, deployment content, and health independently.
- C. First, Enable and limit per-app scaling only when supported and justified by shared-plan capacity design. Then, Query perSiteScaling on the plan and the app's siteConfig.numberOfWorkers value.
- D. First, Mark environment-specific connection and app settings as slot settings before the swap. Then, Query slotConfigNames and compare each slot's effective setting after a test swap.

[Open the answer key](./ANSWERS.md)
