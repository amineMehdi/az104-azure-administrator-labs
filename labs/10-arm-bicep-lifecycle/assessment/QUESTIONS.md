# Lab 10 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB10-Q01 — Foundational

A template deployment reviewer challenges whether the reviewed Bicep deployment pipeline can describe desired Azure resources so repeated deployments converge on that state. Which response resolves the concern?

- A. Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling.
- B. A symbolic resource reference creates an implicit dependency when one resource consumes another's property.
- C. Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations.
- D. Changing a Bicep resource property can update in place or replace the resource according to provider behavior.

## LAB10-Q02 — Foundational

The reviewed Bicep deployment pipeline handoff omits the template deployment rule needed to vary deployment inputs between environments without changing the template body. Which statement should the team add?

- A. Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime.
- B. What-if predicts resource changes without applying the deployment, although some properties may produce noise.
- C. Decompilation provides a starting point and may require manual refactoring, naming, and semantic review.
- D. Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling.

## LAB10-Q03 — Foundational

A template deployment incident review of the reviewed Bicep deployment pipeline depends on the ability to reuse a computed expression inside the template without exposing it to callers. Which platform description is reliable?

- A. Outputs return deployment information but should not expose secrets or sensitive values.
- B. The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope.
- C. ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior.
- D. Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime.

## LAB10-Q04 — Foundational

An infrastructure administrator reviewing and deploying Bicep safely is updating the template deployment runbook. The requirement is to return a deployment value needed by a later workflow. Which statement describes Azure behavior correctly?

- A. A symbolic resource reference creates an implicit dependency when one resource consumes another's property.
- B. Changing a Bicep resource property can update in place or replace the resource according to provider behavior.
- C. Outputs return deployment information but should not expose secrets or sensitive values.
- D. Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations.

## LAB10-Q05 — Foundational

A template deployment peer review asks how the reviewed Bicep deployment pipeline should handle this outcome: ensure one declared resource is deployed after another resource it references. Which explanation is accurate?

- A. What-if predicts resource changes without applying the deployment, although some properties may produce noise.
- B. Decompilation provides a starting point and may require manual refactoring, naming, and semantic review.
- C. Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling.
- D. A symbolic resource reference creates an implicit dependency when one resource consumes another's property.

## LAB10-Q06 — Foundational

For the reviewed Bicep deployment pipeline, the template deployment plan must preview control-plane changes before applying the deployment. Which statement about template deployment belongs in the reviewed Bicep deployment pipeline record?

- A. What-if predicts resource changes without applying the deployment, although some properties may produce noise.
- B. The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope.
- C. ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior.
- D. Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime.

## LAB10-Q07 — Foundational

The template deployment review compares four claims for the reviewed Bicep deployment pipeline requirement to deploy the template at the intended boundary with understood replacement behavior. Which claim is technically sound?

- A. Changing a Bicep resource property can update in place or replace the resource according to provider behavior.
- B. Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations.
- C. Outputs return deployment information but should not expose secrets or sensitive values.
- D. The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope.

## LAB10-Q08 — Foundational

The template deployment architecture note requires the reviewed Bicep deployment pipeline environment to change a declared resource and redeploy the updated desired state. Which statement defines the relevant template deployment boundary?

- A. Decompilation provides a starting point and may require manual refactoring, naming, and semantic review.
- B. Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling.
- C. A symbolic resource reference creates an implicit dependency when one resource consumes another's property.
- D. Changing a Bicep resource property can update in place or replace the resource according to provider behavior.

## LAB10-Q09 — Foundational

A new template deployment operator must explain why the reviewed Bicep deployment pipeline can turn an exported JSON template into maintainable Bicep as a starting point. Which explanation is accurate?

- A. ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior.
- B. Decompilation provides a starting point and may require manual refactoring, naming, and semantic review.
- C. Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime.
- D. What-if predicts resource changes without applying the deployment, although some properties may produce noise.

## LAB10-Q10 — Foundational

The reviewed Bicep deployment pipeline acceptance criteria require operators to modify a JSON deployment template without breaking its schema structure. Which service fact supports that requirement?

- A. Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations.
- B. Outputs return deployment information but should not expose secrets or sensitive values.
- C. The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope.
- D. ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior.

## LAB10-Q11 — Foundational

The reviewed Bicep deployment pipeline window permits only the template deployment change needed to describe desired Azure resources so repeated deployments converge on that state. Which option respects the boundary?

- A. Describe resources and properties declaratively rather than scripting imperative create steps.
- B. Use a variable for a deterministic expression derived from parameters and resource metadata.
- C. Run group what-if and review create, modify, delete, and ignore results before execution.
- D. Decompile the JSON template, build the result, and review warnings before adopting it.

## LAB10-Q12 — Foundational

The template deployment preflight has passed; the reviewed Bicep deployment pipeline must now vary deployment inputs between environments without changing the template body. Which operation should run?

- A. Output nonsecret resource IDs or endpoints needed by later validation stages.
- B. Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed.
- C. Define parameters for environment-specific values and supply them from an approved parameter source.
- D. Validate the modified JSON template and preview its changes before deployment.

## LAB10-Q13 — Foundational

The reviewed Bicep deployment pipeline plan must reuse a computed expression inside the template without exposing it to callers while limiting the mutation scope to template deployment. Which action is appropriate?

- A. Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer.
- B. Use a variable for a deterministic expression derived from parameters and resource metadata.
- C. Modify the symbolic resource and inspect what-if before approving the new deployment.
- D. Describe resources and properties declaratively rather than scripting imperative create steps.

## LAB10-Q14 — Foundational

A template deployment ticket in the reviewed Bicep deployment pipeline says to return a deployment value needed by a later workflow. Which template deployment action completes the reviewed Bicep deployment pipeline request with minimal change?

- A. Run group what-if and review create, modify, delete, and ignore results before execution.
- B. Decompile the JSON template, build the result, and review warnings before adopting it.
- C. Output nonsecret resource IDs or endpoints needed by later validation stages.
- D. Define parameters for environment-specific values and supply them from an approved parameter source.

## LAB10-Q15 — Foundational

The approach for the reviewed Bicep deployment pipeline is approved, but the template deployment environment still cannot ensure one declared resource is deployed after another resource it references. Which implementation step closes the gap?

- A. Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed.
- B. Validate the modified JSON template and preview its changes before deployment.
- C. Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer.
- D. Use a variable for a deterministic expression derived from parameters and resource metadata.

## LAB10-Q16 — Applied

The infrastructure administrator reviewing and deploying Bicep safely may change the reviewed Bicep deployment pipeline only to preview control-plane changes before applying the deployment. Which template deployment action stays within that assignment?

- A. Run group what-if and review create, modify, delete, and ignore results before execution.
- B. Modify the symbolic resource and inspect what-if before approving the new deployment.
- C. Describe resources and properties declaratively rather than scripting imperative create steps.
- D. Output nonsecret resource IDs or endpoints needed by later validation stages.

## LAB10-Q17 — Applied

A template deployment dry run shows no reviewed Bicep deployment pipeline command will deploy the template at the intended boundary with understood replacement behavior. Which action belongs before execution?

- A. Decompile the JSON template, build the result, and review warnings before adopting it.
- B. Define parameters for environment-specific values and supply them from an approved parameter source.
- C. Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed.
- D. Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer.

## LAB10-Q18 — Applied

For the reviewed Bicep deployment pipeline, operators need to change a declared resource and redeploy the updated desired state. Which change realizes that requirement?

- A. Modify the symbolic resource and inspect what-if before approving the new deployment.
- B. Validate the modified JSON template and preview its changes before deployment.
- C. Use a variable for a deterministic expression derived from parameters and resource metadata.
- D. Run group what-if and review create, modify, delete, and ignore results before execution.

## LAB10-Q19 — Applied

Operators must automate the reviewed Bicep deployment pipeline change needed to turn an exported JSON template into maintainable Bicep as a starting point. Which template deployment operation belongs in the runbook?

- A. Decompile the JSON template, build the result, and review warnings before adopting it.
- B. Describe resources and properties declaratively rather than scripting imperative create steps.
- C. Output nonsecret resource IDs or endpoints needed by later validation stages.
- D. Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed.

## LAB10-Q20 — Applied

A reviewed Bicep deployment pipeline review finds template deployment drift from the need to modify a JSON deployment template without breaking its schema structure. Which correction addresses that drift?

- A. Define parameters for environment-specific values and supply them from an approved parameter source.
- B. Validate the modified JSON template and preview its changes before deployment.
- C. Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer.
- D. Modify the symbolic resource and inspect what-if before approving the new deployment.

## LAB10-Q21 — Applied

A reviewed Bicep deployment pipeline review must prove the template deployment ability to describe desired Azure resources so repeated deployments converge on that state. Which check avoids an adjacent feature?

- A. Read deployment outputs and confirm no credential or access token is present.
- B. Build the Bicep file and inspect the resulting template resources and dependencies.
- C. Query deployment scope, provisioning state, mode, and operations after execution.
- D. Run template validation and what-if, then inspect deployment operations after execution.

## LAB10-Q22 — Applied

The reviewed Bicep deployment pipeline evidence bundle needs a template deployment result showing it can vary deployment inputs between environments without changing the template body. Which result belongs in the checkpoint?

- A. Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
- B. Build the template and inspect dependency relationships between the relevant resources.
- C. Compare what-if and deployment operations with the final resource properties.
- D. Build the Bicep file and inspect the resulting template resources and dependencies.

## LAB10-Q23 — Applied

Before reviewed Bicep deployment pipeline cleanup, the template deployment team must reconfirm it can reuse a computed expression inside the template without exposing it to callers. Which read-only inspection should run?

- A. Save the what-if result and confirm no unapproved deletion or replacement is predicted.
- B. Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
- C. Compare resources and expressions in the source template with the compiled Bicep output.
- D. Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.

## LAB10-Q24 — Applied

The reviewed Bicep deployment pipeline setup reports success after the template deployment attempt to return a deployment value needed by a later workflow. Which template deployment read-only observation proves the reviewed Bicep deployment pipeline outcome?

- A. Query deployment scope, provisioning state, mode, and operations after execution.
- B. Run template validation and what-if, then inspect deployment operations after execution.
- C. Read deployment outputs and confirm no credential or access token is present.
- D. Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.

## LAB10-Q25 — Applied

The template deployment log says the reviewed Bicep deployment pipeline can now ensure one declared resource is deployed after another resource it references. Which template deployment state should the reviewed Bicep deployment pipeline acceptance test retain?

- A. Compare what-if and deployment operations with the final resource properties.
- B. Build the Bicep file and inspect the resulting template resources and dependencies.
- C. Build the template and inspect dependency relationships between the relevant resources.
- D. Read deployment outputs and confirm no credential or access token is present.

## LAB10-Q26 — Applied

The reviewed Bicep deployment pipeline rejects template deployment exit status as proof it can preview control-plane changes before applying the deployment. Which reviewed Bicep deployment pipeline result is valid evidence?

- A. Compare resources and expressions in the source template with the compiled Bicep output.
- B. Save the what-if result and confirm no unapproved deletion or replacement is predicted.
- C. Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
- D. Build the template and inspect dependency relationships between the relevant resources.

## LAB10-Q27 — Applied

The template deployment validator needs one reviewed Bicep deployment pipeline query after the change to deploy the template at the intended boundary with understood replacement behavior. Which template deployment property should the reviewed Bicep deployment pipeline validator inspect?

- A. Run template validation and what-if, then inspect deployment operations after execution.
- B. Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
- C. Query deployment scope, provisioning state, mode, and operations after execution.
- D. Save the what-if result and confirm no unapproved deletion or replacement is predicted.

## LAB10-Q28 — Applied

The infrastructure administrator reviewing and deploying Bicep safely must confirm the reviewed Bicep deployment pipeline, without mutation, can change a declared resource and redeploy the updated desired state. Which template deployment check qualifies?

- A. Build the Bicep file and inspect the resulting template resources and dependencies.
- B. Compare what-if and deployment operations with the final resource properties.
- C. Read deployment outputs and confirm no credential or access token is present.
- D. Query deployment scope, provisioning state, mode, and operations after execution.

## LAB10-Q29 — Applied

The reviewed Bicep deployment pipeline configuration is complete; the template deployment reviewers need evidence it can turn an exported JSON template into maintainable Bicep as a starting point. Which observation shows success?

- A. Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
- B. Compare resources and expressions in the source template with the compiled Bicep output.
- C. Build the template and inspect dependency relationships between the relevant resources.
- D. Compare what-if and deployment operations with the final resource properties.

## LAB10-Q30 — Applied

The template deployment validation asks whether the reviewed Bicep deployment pipeline can modify a JSON deployment template without breaking its schema structure. Which observable state is strongest?

- A. Run template validation and what-if, then inspect deployment operations after execution.
- B. Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
- C. Save the what-if result and confirm no unapproved deletion or replacement is predicted.
- D. Compare resources and expressions in the source template with the compiled Bicep output.

## LAB10-Q31 — Applied

The template deployment support team isolated the reviewed Bicep deployment pipeline incident to the attempt to describe desired Azure resources so repeated deployments converge on that state. Which condition prevents success?

- A. A tenant-specific resource name is hard-coded and collides in another environment.
- B. The file embeds an imperative shell sequence instead of declaring Azure resources.
- C. The runbook treats what-if output as proof that resources were actually deployed.
- D. An edited resource reference points to a parameter of the wrong type.

## LAB10-Q32 — Applied

A reviewed Bicep deployment pipeline query surprises the infrastructure administrator reviewing and deploying Bicep safely during the template deployment attempt to vary deployment inputs between environments without changing the template body. Which finding explains it?

- A. A value that operators must choose per environment was hidden in a variable instead of a parameter.
- B. Complete mode targets a shared resource group containing resources not declared by the template.
- C. A tenant-specific resource name is hard-coded and collides in another environment.
- D. The file embeds an imperative shell sequence instead of declaring Azure resources.

## LAB10-Q33 — Applied

Other reviewed Bicep deployment pipeline components are healthy, but the template deployment still cannot reuse a computed expression inside the template without exposing it to callers. Which state causes the isolated failure?

- A. A storage key is emitted as a deployment output and copied into logs.
- B. A property change triggers replacement but the review considered it an in-place update.
- C. A tenant-specific resource name is hard-coded and collides in another environment.
- D. A value that operators must choose per environment was hidden in a variable instead of a parameter.

## LAB10-Q34 — Applied

During a template deployment fault drill, the reviewed Bicep deployment pipeline does not return a deployment value needed by a later workflow. Which finding identifies the defect?

- A. The deployment constructs a resource ID as text and omits a dependency required for correct ordering.
- B. A storage key is emitted as a deployment output and copied into logs.
- C. The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols.
- D. A value that operators must choose per environment was hidden in a variable instead of a parameter.

## LAB10-Q35 — Applied

The reviewed Bicep deployment pipeline setup finishes, yet the template deployment cannot ensure one declared resource is deployed after another resource it references. Which misconfiguration explains the mismatch?

- A. The runbook treats what-if output as proof that resources were actually deployed.
- B. The deployment constructs a resource ID as text and omits a dependency required for correct ordering.
- C. An edited resource reference points to a parameter of the wrong type.
- D. A storage key is emitted as a deployment output and copied into logs.

## LAB10-Q36 — Applied

A template deployment break/fix in the reviewed Bicep deployment pipeline fails when operators try to preview control-plane changes before applying the deployment. Which diagnosis fits?

- A. The runbook treats what-if output as proof that resources were actually deployed.
- B. Complete mode targets a shared resource group containing resources not declared by the template.
- C. The file embeds an imperative shell sequence instead of declaring Azure resources.
- D. The deployment constructs a resource ID as text and omits a dependency required for correct ordering.

## LAB10-Q37 — Applied

The reviewed Bicep deployment pipeline troubleshooting scope is the template deployment need to deploy the template at the intended boundary with understood replacement behavior. Which condition should be corrected first?

- A. A property change triggers replacement but the review considered it an in-place update.
- B. A tenant-specific resource name is hard-coded and collides in another environment.
- C. Complete mode targets a shared resource group containing resources not declared by the template.
- D. The runbook treats what-if output as proof that resources were actually deployed.

## LAB10-Q38 — Applied

The reviewed Bicep deployment pipeline result is partial because the template deployment cannot change a declared resource and redeploy the updated desired state. Which condition accounts for that result?

- A. The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols.
- B. A value that operators must choose per environment was hidden in a variable instead of a parameter.
- C. Complete mode targets a shared resource group containing resources not declared by the template.
- D. A property change triggers replacement but the review considered it an in-place update.

## LAB10-Q39 — Applied

The template deployment evidence shows the reviewed Bicep deployment pipeline cannot turn an exported JSON template into maintainable Bicep as a starting point. Which root cause fits that evidence?

- A. The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols.
- B. An edited resource reference points to a parameter of the wrong type.
- C. A storage key is emitted as a deployment output and copied into logs.
- D. A property change triggers replacement but the review considered it an in-place update.

## LAB10-Q40 — Applied

Although the reviewed Bicep deployment pipeline is meant to let the template deployment modify a JSON deployment template without breaking its schema structure, its checkpoint fails. Which template deployment defect explains the failure?

- A. An edited resource reference points to a parameter of the wrong type.
- B. The file embeds an imperative shell sequence instead of declaring Azure resources.
- C. The deployment constructs a resource ID as text and omits a dependency required for correct ordering.
- D. The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols.

## LAB10-Q41 — Advanced

Only the reviewed Bicep deployment pipeline change needed to describe desired Azure resources so repeated deployments converge on that state is allowed, and template deployment proof is mandatory. Which pair fits?

- A. First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies.
- B. First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
- C. First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.
- D. First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.

## LAB10-Q42 — Advanced

The reviewed Bicep deployment pipeline runbook separates template deployment mutation from validation while it must vary deployment inputs between environments without changing the template body. Which sequence proves it cleanly?

- A. First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
- B. First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.
- C. First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
- D. First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.

## LAB10-Q43 — Advanced

The reviewed Bicep deployment pipeline checkpoint requires both this template deployment outcome—reuse a computed expression inside the template without exposing it to callers—and a read-only reviewed Bicep deployment pipeline state check. Which template deployment response is complete?

- A. First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.
- B. First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
- C. First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.
- D. First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.

## LAB10-Q44 — Advanced

The reviewed Bicep deployment pipeline runbook must return a deployment value needed by a later workflow, then retain template deployment read-back evidence. Which reviewed Bicep deployment pipeline pair completes both duties?

- A. First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
- B. First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted.
- C. First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.
- D. First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies.

## LAB10-Q45 — Advanced

To satisfy the template deployment requirement, operators must change the reviewed Bicep deployment pipeline configuration and prove it can ensure one declared resource is deployed after another resource it references. Which sequence is coherent?

- A. First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.
- B. First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies.
- C. First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.
- D. First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.

## LAB10-Q46 — Advanced

The infrastructure administrator reviewing and deploying Bicep safely needs a safe reviewed Bicep deployment pipeline change to preview control-plane changes before applying the deployment, followed by template deployment evidence. Which pair merits approval?

- A. First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.
- B. First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
- C. First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
- D. First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted.

## LAB10-Q47 — Advanced

The reviewed Bicep deployment pipeline has two template deployment gates: deploy the template at the intended boundary with understood replacement behavior, then prove the reviewed Bicep deployment pipeline state. Which template deployment sequence works?

- A. First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
- B. First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
- C. First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
- D. First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.

## LAB10-Q48 — Advanced

Which template deployment path makes the reviewed Bicep deployment pipeline able to change a declared resource and redeploy the updated desired state, then inspects the defining properties?

- A. First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.
- B. First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.
- C. First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
- D. First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.

## LAB10-Q49 — Advanced

At the reviewed Bicep deployment pipeline approval gate, operators must show that the template deployment can turn an exported JSON template into maintainable Bicep as a starting point. Which template deployment configure-and-check pair is defensible?

- A. First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies.
- B. First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
- C. First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.
- D. First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted.

## LAB10-Q50 — Advanced

The reviewed Bicep deployment pipeline forbids a partial template deployment result. Operators must first modify a JSON deployment template without breaking its schema structure and afterward confirm the reviewed Bicep deployment pipeline outcome. Which template deployment sequence is complete?

- A. First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
- B. First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.
- C. First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted.
- D. First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.

[Open the answer key](./ANSWERS.md)
