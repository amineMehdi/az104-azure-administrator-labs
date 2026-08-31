# Lab 10 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB10-Q01 — C

**Question:** A template deployment reviewer challenges whether the reviewed Bicep deployment pipeline can describe desired Azure resources so repeated deployments converge on that state. Which response resolves the concern?

- **A — Incorrect.** Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling.
  Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling. In the reviewed Bicep deployment pipeline, this statement describes Bicep parameters. Reviewed Bicep deployment pipeline asks about declarative resource state; this Bicep parameters choice leaves the declarative resource state explanation missing.
- **B — Incorrect.** A symbolic resource reference creates an implicit dependency when one resource consumes another's property.
  A symbolic resource reference creates an implicit dependency when one resource consumes another's property. In the reviewed Bicep deployment pipeline, this statement describes symbolic dependencies. The symbolic dependencies statement accurately describes symbolic dependencies; however, reviewed Bicep deployment pipeline needs declarative resource state to describe desired Azure resources so repeated deployments converge on that state; symbolic dependencies cannot replace declarative resource state.
- **C — Correct.** Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations.
  Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations. This declarative resource state fact resolves the reviewed Bicep deployment pipeline design question about how to describe desired Azure resources so repeated deployments converge on that state.
- **D — Incorrect.** Changing a Bicep resource property can update in place or replace the resource according to provider behavior.
  Changing a Bicep resource property can update in place or replace the resource according to provider behavior. In the reviewed Bicep deployment pipeline, this statement describes modifying Bicep resources. Declarative resource state governs reviewed Bicep deployment pipeline; modifying Bicep resources cannot support declarative resource state when operators must describe desired Azure resources so repeated deployments converge on that state.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q02 — D

**Question:** The reviewed Bicep deployment pipeline handoff omits the template deployment rule needed to vary deployment inputs between environments without changing the template body. Which statement should the team add?

- **A — Incorrect.** Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime.
  Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime. In the reviewed Bicep deployment pipeline, this statement describes Bicep variables. The Bicep variables statement accurately describes Bicep variables; however, reviewed Bicep deployment pipeline needs Bicep parameters to vary deployment inputs between environments without changing the template body; Bicep variables cannot replace Bicep parameters.
- **B — Incorrect.** What-if predicts resource changes without applying the deployment, although some properties may produce noise.
  What-if predicts resource changes without applying the deployment, although some properties may produce noise. In the reviewed Bicep deployment pipeline, this statement describes deployment what-if. Selecting deployment what-if for reviewed Bicep deployment pipeline leaves Bicep parameters unanswered in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline lacks a Bicep parameters basis to vary deployment inputs between environments without changing the template body.
- **C — Incorrect.** Decompilation provides a starting point and may require manual refactoring, naming, and semantic review.
  Decompilation provides a starting point and may require manual refactoring, naming, and semantic review. In the reviewed Bicep deployment pipeline, this statement describes ARM-to-Bicep decompilation. Bicep parameters governs reviewed Bicep deployment pipeline; ARM-to-Bicep decompilation cannot support Bicep parameters when operators must vary deployment inputs between environments without changing the template body.
- **D — Correct.** Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling.
  Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling. For reviewed Bicep deployment pipeline, Bicep parameters supplies the service rule needed to vary deployment inputs between environments without changing the template body.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Parameters in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters)

**Source reviewed:** 2026-08-31

## LAB10-Q03 — D

**Question:** A template deployment incident review of the reviewed Bicep deployment pipeline depends on the ability to reuse a computed expression inside the template without exposing it to callers. Which platform description is reliable?

- **A — Incorrect.** Outputs return deployment information but should not expose secrets or sensitive values.
  Outputs return deployment information but should not expose secrets or sensitive values. In the reviewed Bicep deployment pipeline, this statement describes Bicep outputs. Selecting Bicep outputs for reviewed Bicep deployment pipeline leaves Bicep variables unanswered in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline lacks a Bicep variables basis to reuse a computed expression inside the template without exposing it to callers.
- **B — Incorrect.** The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope.
  The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope. In the reviewed Bicep deployment pipeline, this statement describes deployment scope and mode. Bicep variables governs reviewed Bicep deployment pipeline; deployment scope and mode cannot support Bicep variables when operators must reuse a computed expression inside the template without exposing it to callers.
- **C — Incorrect.** ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior.
  ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior. In the reviewed Bicep deployment pipeline, this statement describes ARM template modification. Reviewed Bicep deployment pipeline asks about Bicep variables; this ARM template modification choice leaves the Bicep variables explanation missing.
- **D — Correct.** Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime.
  Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime. In the reviewed Bicep deployment pipeline, this Bicep variables rule supports the need to reuse a computed expression inside the template without exposing it to callers.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Variables in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables)

**Source reviewed:** 2026-08-31

## LAB10-Q04 — C

**Question:** An infrastructure administrator reviewing and deploying Bicep safely is updating the template deployment runbook. The requirement is to return a deployment value needed by a later workflow. Which statement describes Azure behavior correctly?

- **A — Incorrect.** A symbolic resource reference creates an implicit dependency when one resource consumes another's property.
  A symbolic resource reference creates an implicit dependency when one resource consumes another's property. In the reviewed Bicep deployment pipeline, this statement describes symbolic dependencies. Bicep outputs governs reviewed Bicep deployment pipeline; symbolic dependencies cannot support Bicep outputs when operators must return a deployment value needed by a later workflow.
- **B — Incorrect.** Changing a Bicep resource property can update in place or replace the resource according to provider behavior.
  Changing a Bicep resource property can update in place or replace the resource according to provider behavior. In the reviewed Bicep deployment pipeline, this statement describes modifying Bicep resources. Reviewed Bicep deployment pipeline asks about Bicep outputs; this modifying Bicep resources choice leaves the Bicep outputs explanation missing.
- **C — Correct.** Outputs return deployment information but should not expose secrets or sensitive values.
  For the reviewed Bicep deployment pipeline, the rule for Bicep outputs is defined by this statement: outputs return deployment information but should not expose secrets or sensitive values. It supports the required outcome to return a deployment value needed by a later workflow.
- **D — Incorrect.** Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations.
  Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations. In the reviewed Bicep deployment pipeline, this statement describes declarative resource state. Selecting declarative resource state for reviewed Bicep deployment pipeline leaves Bicep outputs unanswered in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline lacks a Bicep outputs basis to return a deployment value needed by a later workflow.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Outputs in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/outputs)

**Source reviewed:** 2026-08-31

## LAB10-Q05 — D

**Question:** A template deployment peer review asks how the reviewed Bicep deployment pipeline should handle this outcome: ensure one declared resource is deployed after another resource it references. Which explanation is accurate?

- **A — Incorrect.** What-if predicts resource changes without applying the deployment, although some properties may produce noise.
  What-if predicts resource changes without applying the deployment, although some properties may produce noise. In the reviewed Bicep deployment pipeline, this statement describes deployment what-if. Reviewed Bicep deployment pipeline asks about symbolic dependencies; this deployment what-if choice leaves the symbolic dependencies explanation missing.
- **B — Incorrect.** Decompilation provides a starting point and may require manual refactoring, naming, and semantic review.
  Decompilation provides a starting point and may require manual refactoring, naming, and semantic review. In the reviewed Bicep deployment pipeline, this statement describes ARM-to-Bicep decompilation. The ARM-to-Bicep decompilation statement accurately describes ARM-to-Bicep decompilation; however, reviewed Bicep deployment pipeline needs symbolic dependencies to ensure one declared resource is deployed after another resource it references; ARM-to-Bicep decompilation cannot replace symbolic dependencies.
- **C — Incorrect.** Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling.
  Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling. In the reviewed Bicep deployment pipeline, this statement describes Bicep parameters. Selecting Bicep parameters for reviewed Bicep deployment pipeline leaves symbolic dependencies unanswered in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline lacks a symbolic dependencies basis to ensure one declared resource is deployed after another resource it references.
- **D — Correct.** A symbolic resource reference creates an implicit dependency when one resource consumes another's property.
  A symbolic resource reference creates an implicit dependency when one resource consumes another's property. The reviewed Bicep deployment pipeline applies that symbolic dependencies boundary when operators must ensure one declared resource is deployed after another resource it references.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [Resource dependencies in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies)

**Source reviewed:** 2026-08-31

## LAB10-Q06 — A

**Question:** For the reviewed Bicep deployment pipeline, the template deployment plan must preview control-plane changes before applying the deployment. Which statement about template deployment belongs in the reviewed Bicep deployment pipeline record?

- **A — Correct.** What-if predicts resource changes without applying the deployment, although some properties may produce noise.
  The reviewed Bicep deployment pipeline needs deployment what-if to preview control-plane changes before applying the deployment; this option states the applicable deployment what-if rule: what-if predicts resource changes without applying the deployment, although some properties may produce noise.
- **B — Incorrect.** The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope.
  The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope. In the reviewed Bicep deployment pipeline, this statement describes deployment scope and mode. Selecting deployment scope and mode for reviewed Bicep deployment pipeline leaves deployment what-if unanswered in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline lacks a deployment what-if basis to preview control-plane changes before applying the deployment.
- **C — Incorrect.** ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior.
  ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior. In the reviewed Bicep deployment pipeline, this statement describes ARM template modification. Deployment what-if governs reviewed Bicep deployment pipeline; ARM template modification cannot support deployment what-if when operators must preview control-plane changes before applying the deployment.
- **D — Incorrect.** Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime.
  Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime. In the reviewed Bicep deployment pipeline, this statement describes Bicep variables. Reviewed Bicep deployment pipeline asks about deployment what-if; this Bicep variables choice leaves the deployment what-if explanation missing.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep what-if deployment operation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

**Source reviewed:** 2026-08-31

## LAB10-Q07 — D

**Question:** The template deployment review compares four claims for the reviewed Bicep deployment pipeline requirement to deploy the template at the intended boundary with understood replacement behavior. Which claim is technically sound?

- **A — Incorrect.** Changing a Bicep resource property can update in place or replace the resource according to provider behavior.
  Changing a Bicep resource property can update in place or replace the resource according to provider behavior. In the reviewed Bicep deployment pipeline, this statement describes modifying Bicep resources. Selecting modifying Bicep resources for reviewed Bicep deployment pipeline leaves deployment scope and mode unanswered in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline lacks a deployment scope and mode basis to deploy the template at the intended boundary with understood replacement behavior.
- **B — Incorrect.** Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations.
  Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations. In the reviewed Bicep deployment pipeline, this statement describes declarative resource state. Deployment scope and mode governs reviewed Bicep deployment pipeline; declarative resource state cannot support deployment scope and mode when operators must deploy the template at the intended boundary with understood replacement behavior.
- **C — Incorrect.** Outputs return deployment information but should not expose secrets or sensitive values.
  Outputs return deployment information but should not expose secrets or sensitive values. In the reviewed Bicep deployment pipeline, this statement describes Bicep outputs. Reviewed Bicep deployment pipeline asks about deployment scope and mode; this Bicep outputs choice leaves the deployment scope and mode explanation missing.
- **D — Correct.** The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope.
  The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope. This deployment scope and mode fact resolves the reviewed Bicep deployment pipeline design question about how to deploy the template at the intended boundary with understood replacement behavior.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Deploy Bicep files with Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)

**Source reviewed:** 2026-08-31

## LAB10-Q08 — D

**Question:** The template deployment architecture note requires the reviewed Bicep deployment pipeline environment to change a declared resource and redeploy the updated desired state. Which statement defines the relevant template deployment boundary?

- **A — Incorrect.** Decompilation provides a starting point and may require manual refactoring, naming, and semantic review.
  Decompilation provides a starting point and may require manual refactoring, naming, and semantic review. In the reviewed Bicep deployment pipeline, this statement describes ARM-to-Bicep decompilation. Modifying Bicep resources governs reviewed Bicep deployment pipeline; ARM-to-Bicep decompilation cannot support modifying Bicep resources when operators must change a declared resource and redeploy the updated desired state.
- **B — Incorrect.** Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling.
  Parameters expose deployment-time inputs while decorators can constrain allowed values, length, or security handling. In the reviewed Bicep deployment pipeline, this statement describes Bicep parameters. Reviewed Bicep deployment pipeline asks about modifying Bicep resources; this Bicep parameters choice leaves the modifying Bicep resources explanation missing.
- **C — Incorrect.** A symbolic resource reference creates an implicit dependency when one resource consumes another's property.
  A symbolic resource reference creates an implicit dependency when one resource consumes another's property. In the reviewed Bicep deployment pipeline, this statement describes symbolic dependencies. The symbolic dependencies statement accurately describes symbolic dependencies; however, reviewed Bicep deployment pipeline needs modifying Bicep resources to change a declared resource and redeploy the updated desired state; symbolic dependencies cannot replace modifying Bicep resources.
- **D — Correct.** Changing a Bicep resource property can update in place or replace the resource according to provider behavior.
  Changing a Bicep resource property can update in place or replace the resource according to provider behavior. For reviewed Bicep deployment pipeline, modifying Bicep resources supplies the service rule needed to change a declared resource and redeploy the updated desired state.

**Objectives:** `CP-IAC-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q09 — B

**Question:** A new template deployment operator must explain why the reviewed Bicep deployment pipeline can turn an exported JSON template into maintainable Bicep as a starting point. Which explanation is accurate?

- **A — Incorrect.** ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior.
  ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior. In the reviewed Bicep deployment pipeline, this statement describes ARM template modification. Reviewed Bicep deployment pipeline asks about ARM-to-Bicep decompilation; this ARM template modification choice leaves the ARM-to-Bicep decompilation explanation missing.
- **B — Correct.** Decompilation provides a starting point and may require manual refactoring, naming, and semantic review.
  Decompilation provides a starting point and may require manual refactoring, naming, and semantic review. In the reviewed Bicep deployment pipeline, this ARM-to-Bicep decompilation rule supports the need to turn an exported JSON template into maintainable Bicep as a starting point.
- **C — Incorrect.** Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime.
  Variables derive reusable values inside a Bicep file and are not supplied by the deployer at runtime. In the reviewed Bicep deployment pipeline, this statement describes Bicep variables. Selecting Bicep variables for reviewed Bicep deployment pipeline leaves ARM-to-Bicep decompilation unanswered in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline lacks a ARM-to-Bicep decompilation basis to turn an exported JSON template into maintainable Bicep as a starting point.
- **D — Incorrect.** What-if predicts resource changes without applying the deployment, although some properties may produce noise.
  What-if predicts resource changes without applying the deployment, although some properties may produce noise. In the reviewed Bicep deployment pipeline, this statement describes deployment what-if. ARM-to-Bicep decompilation governs reviewed Bicep deployment pipeline; deployment what-if cannot support ARM-to-Bicep decompilation when operators must turn an exported JSON template into maintainable Bicep as a starting point.

**Objectives:** `CP-IAC-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Decompile ARM templates to Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile)

**Source reviewed:** 2026-08-31

## LAB10-Q10 — D

**Question:** The reviewed Bicep deployment pipeline acceptance criteria require operators to modify a JSON deployment template without breaking its schema structure. Which service fact supports that requirement?

- **A — Incorrect.** Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations.
  Bicep declares the desired resource state and lets Resource Manager determine dependency-aware operations. In the reviewed Bicep deployment pipeline, this statement describes declarative resource state. The declarative resource state statement accurately describes declarative resource state; however, reviewed Bicep deployment pipeline needs ARM template modification to modify a JSON deployment template without breaking its schema structure; declarative resource state cannot replace ARM template modification.
- **B — Incorrect.** Outputs return deployment information but should not expose secrets or sensitive values.
  Outputs return deployment information but should not expose secrets or sensitive values. In the reviewed Bicep deployment pipeline, this statement describes Bicep outputs. Selecting Bicep outputs for reviewed Bicep deployment pipeline leaves ARM template modification unanswered in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline lacks a ARM template modification basis to modify a JSON deployment template without breaking its schema structure.
- **C — Incorrect.** The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope.
  The deployment scope determines available resources, and complete mode can delete resources absent from the template at resource-group scope. In the reviewed Bicep deployment pipeline, this statement describes deployment scope and mode. ARM template modification governs reviewed Bicep deployment pipeline; deployment scope and mode cannot support ARM template modification when operators must modify a JSON deployment template without breaking its schema structure.
- **D — Correct.** ARM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior.
  For the reviewed Bicep deployment pipeline, the rule for ARM template modification is defined by this statement: aRM template edits must preserve valid expressions, dependencies, parameter types, and API-version behavior. It supports the required outcome to modify a JSON deployment template without breaking its schema structure.

**Objectives:** `CP-IAC-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [ARM template structure and syntax](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax)

**Source reviewed:** 2026-08-31

## LAB10-Q11 — A

**Question:** The reviewed Bicep deployment pipeline window permits only the template deployment change needed to describe desired Azure resources so repeated deployments converge on that state. Which option respects the boundary?

- **A — Correct.** Describe resources and properties declaratively rather than scripting imperative create steps.
  Describe resources and properties declaratively rather than scripting imperative create steps. This changes declarative resource state in the reviewed Bicep deployment pipeline, supplying the missing state needed to describe desired Azure resources so repeated deployments converge on that state.
- **B — Incorrect.** Use a variable for a deterministic expression derived from parameters and resource metadata.
  Use a variable for a deterministic expression derived from parameters and resource metadata. In the reviewed Bicep deployment pipeline, this action changes Bicep variables. Reviewed Bicep deployment pipeline requires declarative resource state; changing Bicep variables leaves declarative resource state absent in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline cannot describe desired Azure resources so repeated deployments converge on that state.
- **C — Incorrect.** Run group what-if and review create, modify, delete, and ignore results before execution.
  Run group what-if and review create, modify, delete, and ignore results before execution. In the reviewed Bicep deployment pipeline, this action changes deployment what-if. Deployment what-if does not implement declarative resource state for reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline still cannot describe desired Azure resources so repeated deployments converge on that state.
- **D — Incorrect.** Decompile the JSON template, build the result, and review warnings before adopting it.
  Decompile the JSON template, build the result, and review warnings before adopting it. In the reviewed Bicep deployment pipeline, this action changes ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline instead needs declarative resource state: Describe resources and properties declaratively rather than scripting imperative create steps. The ARM-to-Bicep decompilation action omits that declarative resource state work.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q12 — C

**Question:** The template deployment preflight has passed; the reviewed Bicep deployment pipeline must now vary deployment inputs between environments without changing the template body. Which operation should run?

- **A — Incorrect.** Output nonsecret resource IDs or endpoints needed by later validation stages.
  Output nonsecret resource IDs or endpoints needed by later validation stages. In the reviewed Bicep deployment pipeline, this action changes Bicep outputs. Reviewed Bicep deployment pipeline requires Bicep parameters; changing Bicep outputs leaves Bicep parameters absent in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline cannot vary deployment inputs between environments without changing the template body.
- **B — Incorrect.** Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed.
  Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. In the reviewed Bicep deployment pipeline, this action changes deployment scope and mode. Deployment scope and mode does not implement Bicep parameters for reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline still cannot vary deployment inputs between environments without changing the template body.
- **C — Correct.** Define parameters for environment-specific values and supply them from an approved parameter source.
  The reviewed Bicep deployment pipeline must vary deployment inputs between environments without changing the template body; this option performs its direct Bicep parameters change: define parameters for environment-specific values and supply them from an approved parameter source.
- **D — Incorrect.** Validate the modified JSON template and preview its changes before deployment.
  Validate the modified JSON template and preview its changes before deployment. In the reviewed Bicep deployment pipeline, this action changes ARM template modification. Reviewed Bicep deployment pipeline approved Bicep parameters, not ARM template modification; only the Bicep parameters change can vary deployment inputs between environments without changing the template body.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Parameters in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters)

**Source reviewed:** 2026-08-31

## LAB10-Q13 — B

**Question:** The reviewed Bicep deployment pipeline plan must reuse a computed expression inside the template without exposing it to callers while limiting the mutation scope to template deployment. Which action is appropriate?

- **A — Incorrect.** Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer.
  Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. In the reviewed Bicep deployment pipeline, this action changes symbolic dependencies. Symbolic dependencies does not implement Bicep variables for reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline still cannot reuse a computed expression inside the template without exposing it to callers.
- **B — Correct.** Use a variable for a deterministic expression derived from parameters and resource metadata.
  Use a variable for a deterministic expression derived from parameters and resource metadata. It is the least-change Bicep variables path for the reviewed Bicep deployment pipeline requirement to reuse a computed expression inside the template without exposing it to callers.
- **C — Incorrect.** Modify the symbolic resource and inspect what-if before approving the new deployment.
  Modify the symbolic resource and inspect what-if before approving the new deployment. In the reviewed Bicep deployment pipeline, this action changes modifying Bicep resources. Reviewed Bicep deployment pipeline approved Bicep variables, not modifying Bicep resources; only the Bicep variables change can reuse a computed expression inside the template without exposing it to callers.
- **D — Incorrect.** Describe resources and properties declaratively rather than scripting imperative create steps.
  Describe resources and properties declaratively rather than scripting imperative create steps. In the reviewed Bicep deployment pipeline, this action changes declarative resource state. Reviewed Bicep deployment pipeline requires Bicep variables; changing declarative resource state leaves Bicep variables absent in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline cannot reuse a computed expression inside the template without exposing it to callers.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Variables in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables)

**Source reviewed:** 2026-08-31

## LAB10-Q14 — C

**Question:** A template deployment ticket in the reviewed Bicep deployment pipeline says to return a deployment value needed by a later workflow. Which template deployment action completes the reviewed Bicep deployment pipeline request with minimal change?

- **A — Incorrect.** Run group what-if and review create, modify, delete, and ignore results before execution.
  Run group what-if and review create, modify, delete, and ignore results before execution. In the reviewed Bicep deployment pipeline, this action changes deployment what-if. Reviewed Bicep deployment pipeline instead needs Bicep outputs: Output nonsecret resource IDs or endpoints needed by later validation stages. The deployment what-if action omits that Bicep outputs work.
- **B — Incorrect.** Decompile the JSON template, build the result, and review warnings before adopting it.
  Decompile the JSON template, build the result, and review warnings before adopting it. In the reviewed Bicep deployment pipeline, this action changes ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline approved Bicep outputs, not ARM-to-Bicep decompilation; only the Bicep outputs change can return a deployment value needed by a later workflow.
- **C — Correct.** Output nonsecret resource IDs or endpoints needed by later validation stages.
  Output nonsecret resource IDs or endpoints needed by later validation stages. In reviewed Bicep deployment pipeline, applying Bicep outputs is the scoped way to return a deployment value needed by a later workflow.
- **D — Incorrect.** Define parameters for environment-specific values and supply them from an approved parameter source.
  Define parameters for environment-specific values and supply them from an approved parameter source. In the reviewed Bicep deployment pipeline, this action changes Bicep parameters. Bicep parameters does not implement Bicep outputs for reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline still cannot return a deployment value needed by a later workflow.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Outputs in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/outputs)

**Source reviewed:** 2026-08-31

## LAB10-Q15 — C

**Question:** The approach for the reviewed Bicep deployment pipeline is approved, but the template deployment environment still cannot ensure one declared resource is deployed after another resource it references. Which implementation step closes the gap?

- **A — Incorrect.** Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed.
  Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. In the reviewed Bicep deployment pipeline, this action changes deployment scope and mode. Reviewed Bicep deployment pipeline approved symbolic dependencies, not deployment scope and mode; only the symbolic dependencies change can ensure one declared resource is deployed after another resource it references.
- **B — Incorrect.** Validate the modified JSON template and preview its changes before deployment.
  Validate the modified JSON template and preview its changes before deployment. In the reviewed Bicep deployment pipeline, this action changes ARM template modification. Reviewed Bicep deployment pipeline requires symbolic dependencies; changing ARM template modification leaves symbolic dependencies absent in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline cannot ensure one declared resource is deployed after another resource it references.
- **C — Correct.** Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer.
  Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. The reviewed Bicep deployment pipeline uses this symbolic dependencies operation to ensure one declared resource is deployed after another resource it references within the approved scope.
- **D — Incorrect.** Use a variable for a deterministic expression derived from parameters and resource metadata.
  Use a variable for a deterministic expression derived from parameters and resource metadata. In the reviewed Bicep deployment pipeline, this action changes Bicep variables. Reviewed Bicep deployment pipeline instead needs symbolic dependencies: Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. The Bicep variables action omits that symbolic dependencies work.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [Resource dependencies in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies)

**Source reviewed:** 2026-08-31

## LAB10-Q16 — A

**Question:** The infrastructure administrator reviewing and deploying Bicep safely may change the reviewed Bicep deployment pipeline only to preview control-plane changes before applying the deployment. Which template deployment action stays within that assignment?

- **A — Correct.** Run group what-if and review create, modify, delete, and ignore results before execution.
  For the reviewed Bicep deployment pipeline, the required deployment what-if action is: run group what-if and review create, modify, delete, and ignore results before execution. It makes the environment able to preview control-plane changes before applying the deployment.
- **B — Incorrect.** Modify the symbolic resource and inspect what-if before approving the new deployment.
  Modify the symbolic resource and inspect what-if before approving the new deployment. In the reviewed Bicep deployment pipeline, this action changes modifying Bicep resources. Modifying Bicep resources does not implement deployment what-if for reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline still cannot preview control-plane changes before applying the deployment.
- **C — Incorrect.** Describe resources and properties declaratively rather than scripting imperative create steps.
  Describe resources and properties declaratively rather than scripting imperative create steps. In the reviewed Bicep deployment pipeline, this action changes declarative resource state. Reviewed Bicep deployment pipeline instead needs deployment what-if: Run group what-if and review create, modify, delete, and ignore results before execution. The declarative resource state action omits that deployment what-if work.
- **D — Incorrect.** Output nonsecret resource IDs or endpoints needed by later validation stages.
  Output nonsecret resource IDs or endpoints needed by later validation stages. In the reviewed Bicep deployment pipeline, this action changes Bicep outputs. Reviewed Bicep deployment pipeline approved deployment what-if, not Bicep outputs; only the deployment what-if change can preview control-plane changes before applying the deployment.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep what-if deployment operation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

**Source reviewed:** 2026-08-31

## LAB10-Q17 — C

**Question:** A template deployment dry run shows no reviewed Bicep deployment pipeline command will deploy the template at the intended boundary with understood replacement behavior. Which action belongs before execution?

- **A — Incorrect.** Decompile the JSON template, build the result, and review warnings before adopting it.
  Decompile the JSON template, build the result, and review warnings before adopting it. In the reviewed Bicep deployment pipeline, this action changes ARM-to-Bicep decompilation. ARM-to-Bicep decompilation does not implement deployment scope and mode for reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline still cannot deploy the template at the intended boundary with understood replacement behavior.
- **B — Incorrect.** Define parameters for environment-specific values and supply them from an approved parameter source.
  Define parameters for environment-specific values and supply them from an approved parameter source. In the reviewed Bicep deployment pipeline, this action changes Bicep parameters. Reviewed Bicep deployment pipeline instead needs deployment scope and mode: Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. The Bicep parameters action omits that deployment scope and mode work.
- **C — Correct.** Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed.
  Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. This changes deployment scope and mode in the reviewed Bicep deployment pipeline, supplying the missing state needed to deploy the template at the intended boundary with understood replacement behavior.
- **D — Incorrect.** Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer.
  Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. In the reviewed Bicep deployment pipeline, this action changes symbolic dependencies. Reviewed Bicep deployment pipeline requires deployment scope and mode; changing symbolic dependencies leaves deployment scope and mode absent in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline cannot deploy the template at the intended boundary with understood replacement behavior.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Deploy Bicep files with Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)

**Source reviewed:** 2026-08-31

## LAB10-Q18 — A

**Question:** For the reviewed Bicep deployment pipeline, operators need to change a declared resource and redeploy the updated desired state. Which change realizes that requirement?

- **A — Correct.** Modify the symbolic resource and inspect what-if before approving the new deployment.
  The reviewed Bicep deployment pipeline must change a declared resource and redeploy the updated desired state; this option performs its direct modifying Bicep resources change: modify the symbolic resource and inspect what-if before approving the new deployment.
- **B — Incorrect.** Validate the modified JSON template and preview its changes before deployment.
  Validate the modified JSON template and preview its changes before deployment. In the reviewed Bicep deployment pipeline, this action changes ARM template modification. Reviewed Bicep deployment pipeline approved modifying Bicep resources, not ARM template modification; only the modifying Bicep resources change can change a declared resource and redeploy the updated desired state.
- **C — Incorrect.** Use a variable for a deterministic expression derived from parameters and resource metadata.
  Use a variable for a deterministic expression derived from parameters and resource metadata. In the reviewed Bicep deployment pipeline, this action changes Bicep variables. Reviewed Bicep deployment pipeline requires modifying Bicep resources; changing Bicep variables leaves modifying Bicep resources absent in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline cannot change a declared resource and redeploy the updated desired state.
- **D — Incorrect.** Run group what-if and review create, modify, delete, and ignore results before execution.
  Run group what-if and review create, modify, delete, and ignore results before execution. In the reviewed Bicep deployment pipeline, this action changes deployment what-if. Deployment what-if does not implement modifying Bicep resources for reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline still cannot change a declared resource and redeploy the updated desired state.

**Objectives:** `CP-IAC-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q19 — A

**Question:** Operators must automate the reviewed Bicep deployment pipeline change needed to turn an exported JSON template into maintainable Bicep as a starting point. Which template deployment operation belongs in the runbook?

- **A — Correct.** Decompile the JSON template, build the result, and review warnings before adopting it.
  Decompile the JSON template, build the result, and review warnings before adopting it. It is the least-change ARM-to-Bicep decompilation path for the reviewed Bicep deployment pipeline requirement to turn an exported JSON template into maintainable Bicep as a starting point.
- **B — Incorrect.** Describe resources and properties declaratively rather than scripting imperative create steps.
  Describe resources and properties declaratively rather than scripting imperative create steps. In the reviewed Bicep deployment pipeline, this action changes declarative resource state. Reviewed Bicep deployment pipeline requires ARM-to-Bicep decompilation; changing declarative resource state leaves ARM-to-Bicep decompilation absent in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline cannot turn an exported JSON template into maintainable Bicep as a starting point.
- **C — Incorrect.** Output nonsecret resource IDs or endpoints needed by later validation stages.
  Output nonsecret resource IDs or endpoints needed by later validation stages. In the reviewed Bicep deployment pipeline, this action changes Bicep outputs. Bicep outputs does not implement ARM-to-Bicep decompilation for reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline still cannot turn an exported JSON template into maintainable Bicep as a starting point.
- **D — Incorrect.** Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed.
  Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. In the reviewed Bicep deployment pipeline, this action changes deployment scope and mode. Reviewed Bicep deployment pipeline instead needs ARM-to-Bicep decompilation: Decompile the JSON template, build the result, and review warnings before adopting it. The deployment scope and mode action omits that ARM-to-Bicep decompilation work.

**Objectives:** `CP-IAC-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Decompile ARM templates to Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile)

**Source reviewed:** 2026-08-31

## LAB10-Q20 — B

**Question:** A reviewed Bicep deployment pipeline review finds template deployment drift from the need to modify a JSON deployment template without breaking its schema structure. Which correction addresses that drift?

- **A — Incorrect.** Define parameters for environment-specific values and supply them from an approved parameter source.
  Define parameters for environment-specific values and supply them from an approved parameter source. In the reviewed Bicep deployment pipeline, this action changes Bicep parameters. Reviewed Bicep deployment pipeline requires ARM template modification; changing Bicep parameters leaves ARM template modification absent in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline cannot modify a JSON deployment template without breaking its schema structure.
- **B — Correct.** Validate the modified JSON template and preview its changes before deployment.
  Validate the modified JSON template and preview its changes before deployment. In reviewed Bicep deployment pipeline, applying ARM template modification is the scoped way to modify a JSON deployment template without breaking its schema structure.
- **C — Incorrect.** Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer.
  Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. In the reviewed Bicep deployment pipeline, this action changes symbolic dependencies. Reviewed Bicep deployment pipeline instead needs ARM template modification: Validate the modified JSON template and preview its changes before deployment. The symbolic dependencies action omits that ARM template modification work.
- **D — Incorrect.** Modify the symbolic resource and inspect what-if before approving the new deployment.
  Modify the symbolic resource and inspect what-if before approving the new deployment. In the reviewed Bicep deployment pipeline, this action changes modifying Bicep resources. Reviewed Bicep deployment pipeline approved ARM template modification, not modifying Bicep resources; only the ARM template modification change can modify a JSON deployment template without breaking its schema structure.

**Objectives:** `CP-IAC-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [ARM template structure and syntax](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax)

**Source reviewed:** 2026-08-31

## LAB10-Q21 — B

**Question:** A reviewed Bicep deployment pipeline review must prove the template deployment ability to describe desired Azure resources so repeated deployments converge on that state. Which check avoids an adjacent feature?

- **A — Incorrect.** Read deployment outputs and confirm no credential or access token is present.
  Read deployment outputs and confirm no credential or access token is present. In the reviewed Bicep deployment pipeline, this check observes Bicep outputs. Reviewed Bicep deployment pipeline output covers Bicep outputs, not declarative resource state; the declarative resource state requirement to describe desired Azure resources so repeated deployments converge on that state remains unverified.
- **B — Correct.** Build the Bicep file and inspect the resulting template resources and dependencies.
  Build the Bicep file and inspect the resulting template resources and dependencies. The reviewed Bicep deployment pipeline reads declarative resource state directly; that declarative resource state result proves the reviewed Bicep deployment pipeline can describe desired Azure resources so repeated deployments converge on that state without another mutation.
- **C — Incorrect.** Query deployment scope, provisioning state, mode, and operations after execution.
  Query deployment scope, provisioning state, mode, and operations after execution. In the reviewed Bicep deployment pipeline, this check observes deployment scope and mode. Reviewed Bicep deployment pipeline reads deployment scope and mode, leaving declarative resource state unproved in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline still has no declarative resource state proof.
- **D — Incorrect.** Run template validation and what-if, then inspect deployment operations after execution.
  Run template validation and what-if, then inspect deployment operations after execution. In the reviewed Bicep deployment pipeline, this check observes ARM template modification. Reviewed Bicep deployment pipeline could pass ARM template modification while declarative resource state is wrong; reviewed Bicep deployment pipeline still lacks declarative resource state proof.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q22 — A

**Question:** The reviewed Bicep deployment pipeline evidence bundle needs a template deployment result showing it can vary deployment inputs between environments without changing the template body. Which result belongs in the checkpoint?

- **A — Correct.** Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
  For the reviewed Bicep deployment pipeline, this Bicep parameters observation is decisive: build the file and inspect parameter types, defaults, decorators, and supplied deployment values. It is reviewed Bicep deployment pipeline evidence that operators can vary deployment inputs between environments without changing the template body.
- **B — Incorrect.** Build the template and inspect dependency relationships between the relevant resources.
  Build the template and inspect dependency relationships between the relevant resources. In the reviewed Bicep deployment pipeline, this check observes symbolic dependencies. Reviewed Bicep deployment pipeline reads symbolic dependencies, leaving Bicep parameters unproved in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline still has no Bicep parameters proof.
- **C — Incorrect.** Compare what-if and deployment operations with the final resource properties.
  Compare what-if and deployment operations with the final resource properties. In the reviewed Bicep deployment pipeline, this check observes modifying Bicep resources. Reviewed Bicep deployment pipeline could pass modifying Bicep resources while Bicep parameters is wrong; reviewed Bicep deployment pipeline still lacks Bicep parameters proof.
- **D — Incorrect.** Build the Bicep file and inspect the resulting template resources and dependencies.
  Build the Bicep file and inspect the resulting template resources and dependencies. In the reviewed Bicep deployment pipeline, this check observes declarative resource state. Reviewed Bicep deployment pipeline output covers declarative resource state, not Bicep parameters; the Bicep parameters requirement to vary deployment inputs between environments without changing the template body remains unverified.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Parameters in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters)

**Source reviewed:** 2026-08-31

## LAB10-Q23 — B

**Question:** Before reviewed Bicep deployment pipeline cleanup, the template deployment team must reconfirm it can reuse a computed expression inside the template without exposing it to callers. Which read-only inspection should run?

- **A — Incorrect.** Save the what-if result and confirm no unapproved deletion or replacement is predicted.
  Save the what-if result and confirm no unapproved deletion or replacement is predicted. In the reviewed Bicep deployment pipeline, this check observes deployment what-if. Reviewed Bicep deployment pipeline reads deployment what-if, leaving Bicep variables unproved in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline still has no Bicep variables proof.
- **B — Correct.** Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
  Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter. Because the reviewed Bicep deployment pipeline check observes Bicep variables, it independently verifies the requirement to reuse a computed expression inside the template without exposing it to callers.
- **C — Incorrect.** Compare resources and expressions in the source template with the compiled Bicep output.
  Compare resources and expressions in the source template with the compiled Bicep output. In the reviewed Bicep deployment pipeline, this check observes ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline output covers ARM-to-Bicep decompilation, not Bicep variables; the Bicep variables requirement to reuse a computed expression inside the template without exposing it to callers remains unverified.
- **D — Incorrect.** Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
  Build the file and inspect parameter types, defaults, decorators, and supplied deployment values. In the reviewed Bicep deployment pipeline, this check observes Bicep parameters. Bicep parameters success in reviewed Bicep deployment pipeline cannot verify Bicep variables; reviewed Bicep deployment pipeline cannot reuse a computed expression inside the template without exposing it to callers until Bicep variables evidence exists.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Variables in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables)

**Source reviewed:** 2026-08-31

## LAB10-Q24 — C

**Question:** The reviewed Bicep deployment pipeline setup reports success after the template deployment attempt to return a deployment value needed by a later workflow. Which template deployment read-only observation proves the reviewed Bicep deployment pipeline outcome?

- **A — Incorrect.** Query deployment scope, provisioning state, mode, and operations after execution.
  Query deployment scope, provisioning state, mode, and operations after execution. In the reviewed Bicep deployment pipeline, this check observes deployment scope and mode. Reviewed Bicep deployment pipeline could pass deployment scope and mode while Bicep outputs is wrong; reviewed Bicep deployment pipeline still lacks Bicep outputs proof.
- **B — Incorrect.** Run template validation and what-if, then inspect deployment operations after execution.
  Run template validation and what-if, then inspect deployment operations after execution. In the reviewed Bicep deployment pipeline, this check observes ARM template modification. Reviewed Bicep deployment pipeline output covers ARM template modification, not Bicep outputs; the Bicep outputs requirement to return a deployment value needed by a later workflow remains unverified.
- **C — Correct.** Read deployment outputs and confirm no credential or access token is present.
  The reviewed Bicep deployment pipeline validator needs this Bicep outputs result: read deployment outputs and confirm no credential or access token is present. It proves the outcome to return a deployment value needed by a later workflow rather than an adjacent checkpoint.
- **D — Incorrect.** Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
  Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter. In the reviewed Bicep deployment pipeline, this check observes Bicep variables. Reviewed Bicep deployment pipeline reads Bicep variables, leaving Bicep outputs unproved in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline still has no Bicep outputs proof.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Outputs in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/outputs)

**Source reviewed:** 2026-08-31

## LAB10-Q25 — C

**Question:** The template deployment log says the reviewed Bicep deployment pipeline can now ensure one declared resource is deployed after another resource it references. Which template deployment state should the reviewed Bicep deployment pipeline acceptance test retain?

- **A — Incorrect.** Compare what-if and deployment operations with the final resource properties.
  Compare what-if and deployment operations with the final resource properties. In the reviewed Bicep deployment pipeline, this check observes modifying Bicep resources. Reviewed Bicep deployment pipeline output covers modifying Bicep resources, not symbolic dependencies; the symbolic dependencies requirement to ensure one declared resource is deployed after another resource it references remains unverified.
- **B — Incorrect.** Build the Bicep file and inspect the resulting template resources and dependencies.
  Build the Bicep file and inspect the resulting template resources and dependencies. In the reviewed Bicep deployment pipeline, this check observes declarative resource state. Declarative resource state success in reviewed Bicep deployment pipeline cannot verify symbolic dependencies; reviewed Bicep deployment pipeline cannot ensure one declared resource is deployed after another resource it references until symbolic dependencies evidence exists.
- **C — Correct.** Build the template and inspect dependency relationships between the relevant resources.
  Build the template and inspect dependency relationships between the relevant resources. This is independent symbolic dependencies evidence for the reviewed Bicep deployment pipeline, even if reviewed Bicep deployment pipeline setup reports success before symbolic dependencies becomes observable.
- **D — Incorrect.** Read deployment outputs and confirm no credential or access token is present.
  Read deployment outputs and confirm no credential or access token is present. In the reviewed Bicep deployment pipeline, this check observes Bicep outputs. Reviewed Bicep deployment pipeline could pass Bicep outputs while symbolic dependencies is wrong; reviewed Bicep deployment pipeline still lacks symbolic dependencies proof.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [Resource dependencies in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies)

**Source reviewed:** 2026-08-31

## LAB10-Q26 — B

**Question:** The reviewed Bicep deployment pipeline rejects template deployment exit status as proof it can preview control-plane changes before applying the deployment. Which reviewed Bicep deployment pipeline result is valid evidence?

- **A — Incorrect.** Compare resources and expressions in the source template with the compiled Bicep output.
  Compare resources and expressions in the source template with the compiled Bicep output. In the reviewed Bicep deployment pipeline, this check observes ARM-to-Bicep decompilation. ARM-to-Bicep decompilation success in reviewed Bicep deployment pipeline cannot verify deployment what-if; reviewed Bicep deployment pipeline cannot preview control-plane changes before applying the deployment until deployment what-if evidence exists.
- **B — Correct.** Save the what-if result and confirm no unapproved deletion or replacement is predicted.
  Save the what-if result and confirm no unapproved deletion or replacement is predicted. For reviewed Bicep deployment pipeline, this deployment what-if read confirms the service can preview control-plane changes before applying the deployment.
- **C — Incorrect.** Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
  Build the file and inspect parameter types, defaults, decorators, and supplied deployment values. In the reviewed Bicep deployment pipeline, this check observes Bicep parameters. Reviewed Bicep deployment pipeline could pass Bicep parameters while deployment what-if is wrong; reviewed Bicep deployment pipeline still lacks deployment what-if proof.
- **D — Incorrect.** Build the template and inspect dependency relationships between the relevant resources.
  Build the template and inspect dependency relationships between the relevant resources. In the reviewed Bicep deployment pipeline, this check observes symbolic dependencies. Reviewed Bicep deployment pipeline output covers symbolic dependencies, not deployment what-if; the deployment what-if requirement to preview control-plane changes before applying the deployment remains unverified.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep what-if deployment operation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

**Source reviewed:** 2026-08-31

## LAB10-Q27 — C

**Question:** The template deployment validator needs one reviewed Bicep deployment pipeline query after the change to deploy the template at the intended boundary with understood replacement behavior. Which template deployment property should the reviewed Bicep deployment pipeline validator inspect?

- **A — Incorrect.** Run template validation and what-if, then inspect deployment operations after execution.
  Run template validation and what-if, then inspect deployment operations after execution. In the reviewed Bicep deployment pipeline, this check observes ARM template modification. Reviewed Bicep deployment pipeline reads ARM template modification, leaving deployment scope and mode unproved in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline still has no deployment scope and mode proof.
- **B — Incorrect.** Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
  Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter. In the reviewed Bicep deployment pipeline, this check observes Bicep variables. Reviewed Bicep deployment pipeline could pass Bicep variables while deployment scope and mode is wrong; reviewed Bicep deployment pipeline still lacks deployment scope and mode proof.
- **C — Correct.** Query deployment scope, provisioning state, mode, and operations after execution.
  Query deployment scope, provisioning state, mode, and operations after execution. The reviewed Bicep deployment pipeline reads deployment scope and mode directly; that deployment scope and mode result proves the reviewed Bicep deployment pipeline can deploy the template at the intended boundary with understood replacement behavior without another mutation.
- **D — Incorrect.** Save the what-if result and confirm no unapproved deletion or replacement is predicted.
  Save the what-if result and confirm no unapproved deletion or replacement is predicted. In the reviewed Bicep deployment pipeline, this check observes deployment what-if. Deployment what-if success in reviewed Bicep deployment pipeline cannot verify deployment scope and mode; reviewed Bicep deployment pipeline cannot deploy the template at the intended boundary with understood replacement behavior until deployment scope and mode evidence exists.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Deploy Bicep files with Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)

**Source reviewed:** 2026-08-31

## LAB10-Q28 — B

**Question:** The infrastructure administrator reviewing and deploying Bicep safely must confirm the reviewed Bicep deployment pipeline, without mutation, can change a declared resource and redeploy the updated desired state. Which template deployment check qualifies?

- **A — Incorrect.** Build the Bicep file and inspect the resulting template resources and dependencies.
  Build the Bicep file and inspect the resulting template resources and dependencies. In the reviewed Bicep deployment pipeline, this check observes declarative resource state. Reviewed Bicep deployment pipeline could pass declarative resource state while modifying Bicep resources is wrong; reviewed Bicep deployment pipeline still lacks modifying Bicep resources proof.
- **B — Correct.** Compare what-if and deployment operations with the final resource properties.
  For the reviewed Bicep deployment pipeline, this modifying Bicep resources observation is decisive: compare what-if and deployment operations with the final resource properties. It is reviewed Bicep deployment pipeline evidence that operators can change a declared resource and redeploy the updated desired state.
- **C — Incorrect.** Read deployment outputs and confirm no credential or access token is present.
  Read deployment outputs and confirm no credential or access token is present. In the reviewed Bicep deployment pipeline, this check observes Bicep outputs. Bicep outputs success in reviewed Bicep deployment pipeline cannot verify modifying Bicep resources; reviewed Bicep deployment pipeline cannot change a declared resource and redeploy the updated desired state until modifying Bicep resources evidence exists.
- **D — Incorrect.** Query deployment scope, provisioning state, mode, and operations after execution.
  Query deployment scope, provisioning state, mode, and operations after execution. In the reviewed Bicep deployment pipeline, this check observes deployment scope and mode. Reviewed Bicep deployment pipeline reads deployment scope and mode, leaving modifying Bicep resources unproved in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline still has no modifying Bicep resources proof.

**Objectives:** `CP-IAC-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q29 — B

**Question:** The reviewed Bicep deployment pipeline configuration is complete; the template deployment reviewers need evidence it can turn an exported JSON template into maintainable Bicep as a starting point. Which observation shows success?

- **A — Incorrect.** Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
  Build the file and inspect parameter types, defaults, decorators, and supplied deployment values. In the reviewed Bicep deployment pipeline, this check observes Bicep parameters. Reviewed Bicep deployment pipeline output covers Bicep parameters, not ARM-to-Bicep decompilation; the ARM-to-Bicep decompilation requirement to turn an exported JSON template into maintainable Bicep as a starting point remains unverified.
- **B — Correct.** Compare resources and expressions in the source template with the compiled Bicep output.
  Compare resources and expressions in the source template with the compiled Bicep output. Because the reviewed Bicep deployment pipeline check observes ARM-to-Bicep decompilation, it independently verifies the requirement to turn an exported JSON template into maintainable Bicep as a starting point.
- **C — Incorrect.** Build the template and inspect dependency relationships between the relevant resources.
  Build the template and inspect dependency relationships between the relevant resources. In the reviewed Bicep deployment pipeline, this check observes symbolic dependencies. Reviewed Bicep deployment pipeline reads symbolic dependencies, leaving ARM-to-Bicep decompilation unproved in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline still has no ARM-to-Bicep decompilation proof.
- **D — Incorrect.** Compare what-if and deployment operations with the final resource properties.
  Compare what-if and deployment operations with the final resource properties. In the reviewed Bicep deployment pipeline, this check observes modifying Bicep resources. Reviewed Bicep deployment pipeline could pass modifying Bicep resources while ARM-to-Bicep decompilation is wrong; reviewed Bicep deployment pipeline still lacks ARM-to-Bicep decompilation proof.

**Objectives:** `CP-IAC-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Decompile ARM templates to Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile)

**Source reviewed:** 2026-08-31

## LAB10-Q30 — A

**Question:** The template deployment validation asks whether the reviewed Bicep deployment pipeline can modify a JSON deployment template without breaking its schema structure. Which observable state is strongest?

- **A — Correct.** Run template validation and what-if, then inspect deployment operations after execution.
  The reviewed Bicep deployment pipeline validator needs this ARM template modification result: run template validation and what-if, then inspect deployment operations after execution. It proves the outcome to modify a JSON deployment template without breaking its schema structure rather than an adjacent checkpoint.
- **B — Incorrect.** Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
  Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter. In the reviewed Bicep deployment pipeline, this check observes Bicep variables. Reviewed Bicep deployment pipeline reads Bicep variables, leaving ARM template modification unproved in reviewed Bicep deployment pipeline; reviewed Bicep deployment pipeline still has no ARM template modification proof.
- **C — Incorrect.** Save the what-if result and confirm no unapproved deletion or replacement is predicted.
  Save the what-if result and confirm no unapproved deletion or replacement is predicted. In the reviewed Bicep deployment pipeline, this check observes deployment what-if. Reviewed Bicep deployment pipeline could pass deployment what-if while ARM template modification is wrong; reviewed Bicep deployment pipeline still lacks ARM template modification proof.
- **D — Incorrect.** Compare resources and expressions in the source template with the compiled Bicep output.
  Compare resources and expressions in the source template with the compiled Bicep output. In the reviewed Bicep deployment pipeline, this check observes ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline output covers ARM-to-Bicep decompilation, not ARM template modification; the ARM template modification requirement to modify a JSON deployment template without breaking its schema structure remains unverified.

**Objectives:** `CP-IAC-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [ARM template structure and syntax](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax)

**Source reviewed:** 2026-08-31

## LAB10-Q31 — B

**Question:** The template deployment support team isolated the reviewed Bicep deployment pipeline incident to the attempt to describe desired Azure resources so repeated deployments converge on that state. Which condition prevents success?

- **A — Incorrect.** A tenant-specific resource name is hard-coded and collides in another environment.
  A tenant-specific resource name is hard-coded and collides in another environment. The reviewed Bicep deployment pipeline fault concerns Bicep parameters. Reviewed Bicep deployment pipeline has Bicep parameters impact, but declarative resource state is the reviewed Bicep deployment pipeline failed path; the Bicep parameters state cannot produce declarative resource state failure.
- **B — Correct.** The file embeds an imperative shell sequence instead of declaring Azure resources.
  The file embeds an imperative shell sequence instead of declaring Azure resources. Removing this declarative resource state condition lets the reviewed Bicep deployment pipeline describe desired Azure resources so repeated deployments converge on that state while leaving healthy controls unchanged.
- **C — Incorrect.** The runbook treats what-if output as proof that resources were actually deployed.
  The runbook treats what-if output as proof that resources were actually deployed. The reviewed Bicep deployment pipeline fault concerns deployment what-if. Reviewed Bicep deployment pipeline failed on declarative resource state; this deployment what-if finding redirects reviewed Bicep deployment pipeline remediation away from declarative resource state.
- **D — Incorrect.** An edited resource reference points to a parameter of the wrong type.
  An edited resource reference points to a parameter of the wrong type. The reviewed Bicep deployment pipeline fault concerns ARM template modification. Reviewed Bicep deployment pipeline may fix ARM template modification, yet declarative resource state still fails; this reviewed Bicep deployment pipeline diagnosis of ARM template modification is wrong for declarative resource state.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q32 — C

**Question:** A reviewed Bicep deployment pipeline query surprises the infrastructure administrator reviewing and deploying Bicep safely during the template deployment attempt to vary deployment inputs between environments without changing the template body. Which finding explains it?

- **A — Incorrect.** A value that operators must choose per environment was hidden in a variable instead of a parameter.
  A value that operators must choose per environment was hidden in a variable instead of a parameter. The reviewed Bicep deployment pipeline fault concerns Bicep variables. Reviewed Bicep deployment pipeline could repair Bicep variables while Bicep parameters stays broken in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline remains unable to vary deployment inputs between environments without changing the template body.
- **B — Incorrect.** Complete mode targets a shared resource group containing resources not declared by the template.
  Complete mode targets a shared resource group containing resources not declared by the template. The reviewed Bicep deployment pipeline fault concerns deployment scope and mode. Reviewed Bicep deployment pipeline failed on Bicep parameters; this deployment scope and mode finding redirects reviewed Bicep deployment pipeline remediation away from Bicep parameters.
- **C — Correct.** A tenant-specific resource name is hard-coded and collides in another environment.
  A tenant-specific resource name is hard-coded and collides in another environment. In reviewed Bicep deployment pipeline, this Bicep parameters cause matches the failure to vary deployment inputs between environments without changing the template body.
- **D — Incorrect.** The file embeds an imperative shell sequence instead of declaring Azure resources.
  The file embeds an imperative shell sequence instead of declaring Azure resources. The reviewed Bicep deployment pipeline fault concerns declarative resource state. Reviewed Bicep deployment pipeline has declarative resource state impact, but Bicep parameters is the reviewed Bicep deployment pipeline failed path; the declarative resource state state cannot produce Bicep parameters failure.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Parameters in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters)

**Source reviewed:** 2026-08-31

## LAB10-Q33 — D

**Question:** Other reviewed Bicep deployment pipeline components are healthy, but the template deployment still cannot reuse a computed expression inside the template without exposing it to callers. Which state causes the isolated failure?

- **A — Incorrect.** A storage key is emitted as a deployment output and copied into logs.
  A storage key is emitted as a deployment output and copied into logs. The reviewed Bicep deployment pipeline fault concerns Bicep outputs. Reviewed Bicep deployment pipeline failed on Bicep variables; this Bicep outputs finding redirects reviewed Bicep deployment pipeline remediation away from Bicep variables.
- **B — Incorrect.** A property change triggers replacement but the review considered it an in-place update.
  A property change triggers replacement but the review considered it an in-place update. The reviewed Bicep deployment pipeline fault concerns modifying Bicep resources. Reviewed Bicep deployment pipeline may fix modifying Bicep resources, yet Bicep variables still fails; this reviewed Bicep deployment pipeline diagnosis of modifying Bicep resources is wrong for Bicep variables.
- **C — Incorrect.** A tenant-specific resource name is hard-coded and collides in another environment.
  A tenant-specific resource name is hard-coded and collides in another environment. The reviewed Bicep deployment pipeline fault concerns Bicep parameters. Reviewed Bicep deployment pipeline has Bicep parameters impact, but Bicep variables is the reviewed Bicep deployment pipeline failed path; the Bicep parameters state cannot produce Bicep variables failure.
- **D — Correct.** A value that operators must choose per environment was hidden in a variable instead of a parameter.
  A value that operators must choose per environment was hidden in a variable instead of a parameter. This reviewed Bicep deployment pipeline condition breaks Bicep variables, explaining why operators cannot reuse a computed expression inside the template without exposing it to callers.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Variables in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables)

**Source reviewed:** 2026-08-31

## LAB10-Q34 — B

**Question:** During a template deployment fault drill, the reviewed Bicep deployment pipeline does not return a deployment value needed by a later workflow. Which finding identifies the defect?

- **A — Incorrect.** The deployment constructs a resource ID as text and omits a dependency required for correct ordering.
  The deployment constructs a resource ID as text and omits a dependency required for correct ordering. The reviewed Bicep deployment pipeline fault concerns symbolic dependencies. Reviewed Bicep deployment pipeline may fix symbolic dependencies, yet Bicep outputs still fails; this reviewed Bicep deployment pipeline diagnosis of symbolic dependencies is wrong for Bicep outputs.
- **B — Correct.** A storage key is emitted as a deployment output and copied into logs.
  For the reviewed Bicep deployment pipeline, the Bicep outputs failure is causal: a storage key is emitted as a deployment output and copied into logs. Correcting it restores the ability to return a deployment value needed by a later workflow.
- **C — Incorrect.** The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols.
  The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols. The reviewed Bicep deployment pipeline fault concerns ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline could repair ARM-to-Bicep decompilation while Bicep outputs stays broken in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline remains unable to return a deployment value needed by a later workflow.
- **D — Incorrect.** A value that operators must choose per environment was hidden in a variable instead of a parameter.
  A value that operators must choose per environment was hidden in a variable instead of a parameter. The reviewed Bicep deployment pipeline fault concerns Bicep variables. Reviewed Bicep deployment pipeline failed on Bicep outputs; this Bicep variables finding redirects reviewed Bicep deployment pipeline remediation away from Bicep outputs.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Outputs in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/outputs)

**Source reviewed:** 2026-08-31

## LAB10-Q35 — B

**Question:** The reviewed Bicep deployment pipeline setup finishes, yet the template deployment cannot ensure one declared resource is deployed after another resource it references. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The runbook treats what-if output as proof that resources were actually deployed.
  The runbook treats what-if output as proof that resources were actually deployed. The reviewed Bicep deployment pipeline fault concerns deployment what-if. Reviewed Bicep deployment pipeline has deployment what-if impact, but symbolic dependencies is the reviewed Bicep deployment pipeline failed path; the deployment what-if state cannot produce symbolic dependencies failure.
- **B — Correct.** The deployment constructs a resource ID as text and omits a dependency required for correct ordering.
  The deployment constructs a resource ID as text and omits a dependency required for correct ordering. The finding is specific to symbolic dependencies in the reviewed Bicep deployment pipeline; repairing symbolic dependencies restores the reviewed Bicep deployment pipeline ability to ensure one declared resource is deployed after another resource it references.
- **C — Incorrect.** An edited resource reference points to a parameter of the wrong type.
  An edited resource reference points to a parameter of the wrong type. The reviewed Bicep deployment pipeline fault concerns ARM template modification. Reviewed Bicep deployment pipeline failed on symbolic dependencies; this ARM template modification finding redirects reviewed Bicep deployment pipeline remediation away from symbolic dependencies.
- **D — Incorrect.** A storage key is emitted as a deployment output and copied into logs.
  A storage key is emitted as a deployment output and copied into logs. The reviewed Bicep deployment pipeline fault concerns Bicep outputs. Reviewed Bicep deployment pipeline may fix Bicep outputs, yet symbolic dependencies still fails; this reviewed Bicep deployment pipeline diagnosis of Bicep outputs is wrong for symbolic dependencies.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [Resource dependencies in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies)

**Source reviewed:** 2026-08-31

## LAB10-Q36 — A

**Question:** A template deployment break/fix in the reviewed Bicep deployment pipeline fails when operators try to preview control-plane changes before applying the deployment. Which diagnosis fits?

- **A — Correct.** The runbook treats what-if output as proof that resources were actually deployed.
  The reviewed Bicep deployment pipeline cannot preview control-plane changes before applying the deployment because of this deployment what-if defect: the runbook treats what-if output as proof that resources were actually deployed. The symptom and repair align.
- **B — Incorrect.** Complete mode targets a shared resource group containing resources not declared by the template.
  Complete mode targets a shared resource group containing resources not declared by the template. The reviewed Bicep deployment pipeline fault concerns deployment scope and mode. Reviewed Bicep deployment pipeline failed on deployment what-if; this deployment scope and mode finding redirects reviewed Bicep deployment pipeline remediation away from deployment what-if.
- **C — Incorrect.** The file embeds an imperative shell sequence instead of declaring Azure resources.
  The file embeds an imperative shell sequence instead of declaring Azure resources. The reviewed Bicep deployment pipeline fault concerns declarative resource state. Reviewed Bicep deployment pipeline may fix declarative resource state, yet deployment what-if still fails; this reviewed Bicep deployment pipeline diagnosis of declarative resource state is wrong for deployment what-if.
- **D — Incorrect.** The deployment constructs a resource ID as text and omits a dependency required for correct ordering.
  The deployment constructs a resource ID as text and omits a dependency required for correct ordering. The reviewed Bicep deployment pipeline fault concerns symbolic dependencies. Reviewed Bicep deployment pipeline has symbolic dependencies impact, but deployment what-if is the reviewed Bicep deployment pipeline failed path; the symbolic dependencies state cannot produce deployment what-if failure.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep what-if deployment operation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

**Source reviewed:** 2026-08-31

## LAB10-Q37 — C

**Question:** The reviewed Bicep deployment pipeline troubleshooting scope is the template deployment need to deploy the template at the intended boundary with understood replacement behavior. Which condition should be corrected first?

- **A — Incorrect.** A property change triggers replacement but the review considered it an in-place update.
  A property change triggers replacement but the review considered it an in-place update. The reviewed Bicep deployment pipeline fault concerns modifying Bicep resources. Reviewed Bicep deployment pipeline failed on deployment scope and mode; this modifying Bicep resources finding redirects reviewed Bicep deployment pipeline remediation away from deployment scope and mode.
- **B — Incorrect.** A tenant-specific resource name is hard-coded and collides in another environment.
  A tenant-specific resource name is hard-coded and collides in another environment. The reviewed Bicep deployment pipeline fault concerns Bicep parameters. Reviewed Bicep deployment pipeline may fix Bicep parameters, yet deployment scope and mode still fails; this reviewed Bicep deployment pipeline diagnosis of Bicep parameters is wrong for deployment scope and mode.
- **C — Correct.** Complete mode targets a shared resource group containing resources not declared by the template.
  Complete mode targets a shared resource group containing resources not declared by the template. Removing this deployment scope and mode condition lets the reviewed Bicep deployment pipeline deploy the template at the intended boundary with understood replacement behavior while leaving healthy controls unchanged.
- **D — Incorrect.** The runbook treats what-if output as proof that resources were actually deployed.
  The runbook treats what-if output as proof that resources were actually deployed. The reviewed Bicep deployment pipeline fault concerns deployment what-if. Reviewed Bicep deployment pipeline could repair deployment what-if while deployment scope and mode stays broken in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline remains unable to deploy the template at the intended boundary with understood replacement behavior.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Deploy Bicep files with Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)

**Source reviewed:** 2026-08-31

## LAB10-Q38 — D

**Question:** The reviewed Bicep deployment pipeline result is partial because the template deployment cannot change a declared resource and redeploy the updated desired state. Which condition accounts for that result?

- **A — Incorrect.** The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols.
  The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols. The reviewed Bicep deployment pipeline fault concerns ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline may fix ARM-to-Bicep decompilation, yet modifying Bicep resources still fails; this reviewed Bicep deployment pipeline diagnosis of ARM-to-Bicep decompilation is wrong for modifying Bicep resources.
- **B — Incorrect.** A value that operators must choose per environment was hidden in a variable instead of a parameter.
  A value that operators must choose per environment was hidden in a variable instead of a parameter. The reviewed Bicep deployment pipeline fault concerns Bicep variables. Reviewed Bicep deployment pipeline has Bicep variables impact, but modifying Bicep resources is the reviewed Bicep deployment pipeline failed path; the Bicep variables state cannot produce modifying Bicep resources failure.
- **C — Incorrect.** Complete mode targets a shared resource group containing resources not declared by the template.
  Complete mode targets a shared resource group containing resources not declared by the template. The reviewed Bicep deployment pipeline fault concerns deployment scope and mode. Reviewed Bicep deployment pipeline could repair deployment scope and mode while modifying Bicep resources stays broken in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline remains unable to change a declared resource and redeploy the updated desired state.
- **D — Correct.** A property change triggers replacement but the review considered it an in-place update.
  A property change triggers replacement but the review considered it an in-place update. In reviewed Bicep deployment pipeline, this modifying Bicep resources cause matches the failure to change a declared resource and redeploy the updated desired state.

**Objectives:** `CP-IAC-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q39 — A

**Question:** The template deployment evidence shows the reviewed Bicep deployment pipeline cannot turn an exported JSON template into maintainable Bicep as a starting point. Which root cause fits that evidence?

- **A — Correct.** The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols.
  The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols. This reviewed Bicep deployment pipeline condition breaks ARM-to-Bicep decompilation, explaining why operators cannot turn an exported JSON template into maintainable Bicep as a starting point.
- **B — Incorrect.** An edited resource reference points to a parameter of the wrong type.
  An edited resource reference points to a parameter of the wrong type. The reviewed Bicep deployment pipeline fault concerns ARM template modification. Reviewed Bicep deployment pipeline could repair ARM template modification while ARM-to-Bicep decompilation stays broken in reviewed Bicep deployment pipeline; the reviewed Bicep deployment pipeline remains unable to turn an exported JSON template into maintainable Bicep as a starting point.
- **C — Incorrect.** A storage key is emitted as a deployment output and copied into logs.
  A storage key is emitted as a deployment output and copied into logs. The reviewed Bicep deployment pipeline fault concerns Bicep outputs. Reviewed Bicep deployment pipeline failed on ARM-to-Bicep decompilation; this Bicep outputs finding redirects reviewed Bicep deployment pipeline remediation away from ARM-to-Bicep decompilation.
- **D — Incorrect.** A property change triggers replacement but the review considered it an in-place update.
  A property change triggers replacement but the review considered it an in-place update. The reviewed Bicep deployment pipeline fault concerns modifying Bicep resources. Reviewed Bicep deployment pipeline may fix modifying Bicep resources, yet ARM-to-Bicep decompilation still fails; this reviewed Bicep deployment pipeline diagnosis of modifying Bicep resources is wrong for ARM-to-Bicep decompilation.

**Objectives:** `CP-IAC-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Decompile ARM templates to Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile)

**Source reviewed:** 2026-08-31

## LAB10-Q40 — A

**Question:** Although the reviewed Bicep deployment pipeline is meant to let the template deployment modify a JSON deployment template without breaking its schema structure, its checkpoint fails. Which template deployment defect explains the failure?

- **A — Correct.** An edited resource reference points to a parameter of the wrong type.
  For the reviewed Bicep deployment pipeline, the ARM template modification failure is causal: an edited resource reference points to a parameter of the wrong type. Correcting it restores the ability to modify a JSON deployment template without breaking its schema structure.
- **B — Incorrect.** The file embeds an imperative shell sequence instead of declaring Azure resources.
  The file embeds an imperative shell sequence instead of declaring Azure resources. The reviewed Bicep deployment pipeline fault concerns declarative resource state. Reviewed Bicep deployment pipeline failed on ARM template modification; this declarative resource state finding redirects reviewed Bicep deployment pipeline remediation away from ARM template modification.
- **C — Incorrect.** The deployment constructs a resource ID as text and omits a dependency required for correct ordering.
  The deployment constructs a resource ID as text and omits a dependency required for correct ordering. The reviewed Bicep deployment pipeline fault concerns symbolic dependencies. Reviewed Bicep deployment pipeline may fix symbolic dependencies, yet ARM template modification still fails; this reviewed Bicep deployment pipeline diagnosis of symbolic dependencies is wrong for ARM template modification.
- **D — Incorrect.** The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols.
  The generated Bicep was accepted without resolving decompiler warnings or restoring meaningful symbols. The reviewed Bicep deployment pipeline fault concerns ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline has ARM-to-Bicep decompilation impact, but ARM template modification is the reviewed Bicep deployment pipeline failed path; the ARM-to-Bicep decompilation state cannot produce ARM template modification failure.

**Objectives:** `CP-IAC-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [ARM template structure and syntax](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax)

**Source reviewed:** 2026-08-31

## LAB10-Q41 — A

**Question:** Only the reviewed Bicep deployment pipeline change needed to describe desired Azure resources so repeated deployments converge on that state is allowed, and template deployment proof is mandatory. Which pair fits?

- **A — Correct.** First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies.
  First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies. The reviewed Bicep deployment pipeline uses its declarative resource state mutation gate and declarative resource state verification gate before it can describe desired Azure resources so repeated deployments converge on that state.
- **B — Incorrect.** First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
  First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter. This reviewed Bicep deployment pipeline pair serves Bicep variables. Reviewed Bicep deployment pipeline proves Bicep variables, but declarative resource state lacks implementation in reviewed Bicep deployment pipeline and declarative resource state proof; the declarative resource state outcome to describe desired Azure resources so repeated deployments converge on that state remains open.
- **C — Incorrect.** First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.
  First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution. This reviewed Bicep deployment pipeline pair serves deployment scope and mode. Reviewed Bicep deployment pipeline uses deployment scope and mode for both steps; declarative resource state remains untouched in reviewed Bicep deployment pipeline, so its declarative resource state gate to describe desired Azure resources so repeated deployments converge on that state fails.
- **D — Incorrect.** First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.
  First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties. This reviewed Bicep deployment pipeline pair serves modifying Bicep resources. Reviewed Bicep deployment pipeline closes modifying Bicep resources, not declarative resource state; without the declarative resource state workflow, it cannot describe desired Azure resources so repeated deployments converge on that state.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q42 — D

**Question:** The reviewed Bicep deployment pipeline runbook separates template deployment mutation from validation while it must vary deployment inputs between environments without changing the template body. Which sequence proves it cleanly?

- **A — Incorrect.** First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
  First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present. This reviewed Bicep deployment pipeline pair serves Bicep outputs. Reviewed Bicep deployment pipeline proves Bicep outputs, but Bicep parameters lacks implementation in reviewed Bicep deployment pipeline and Bicep parameters proof; the Bicep parameters outcome to vary deployment inputs between environments without changing the template body remains open.
- **B — Incorrect.** First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.
  First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties. This reviewed Bicep deployment pipeline pair serves modifying Bicep resources. Reviewed Bicep deployment pipeline uses modifying Bicep resources for both steps; Bicep parameters remains untouched in reviewed Bicep deployment pipeline, so its Bicep parameters gate to vary deployment inputs between environments without changing the template body fails.
- **C — Incorrect.** First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
  First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output. This reviewed Bicep deployment pipeline pair serves ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline closes ARM-to-Bicep decompilation, not Bicep parameters; without the Bicep parameters workflow, it cannot vary deployment inputs between environments without changing the template body.
- **D — Correct.** First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
  The reviewed Bicep deployment pipeline gets a complete Bicep parameters sequence here: first, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values. Read-back evidence follows the change.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Parameters in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters)

**Source reviewed:** 2026-08-31

## LAB10-Q43 — D

**Question:** The reviewed Bicep deployment pipeline checkpoint requires both this template deployment outcome—reuse a computed expression inside the template without exposing it to callers—and a read-only reviewed Bicep deployment pipeline state check. Which template deployment response is complete?

- **A — Incorrect.** First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.
  First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources. This reviewed Bicep deployment pipeline pair serves symbolic dependencies. Reviewed Bicep deployment pipeline uses symbolic dependencies for both steps; Bicep variables remains untouched in reviewed Bicep deployment pipeline, so its Bicep variables gate to reuse a computed expression inside the template without exposing it to callers fails.
- **B — Incorrect.** First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
  First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output. This reviewed Bicep deployment pipeline pair serves ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline closes ARM-to-Bicep decompilation, not Bicep variables; without the Bicep variables workflow, it cannot reuse a computed expression inside the template without exposing it to callers.
- **C — Incorrect.** First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.
  First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution. This reviewed Bicep deployment pipeline pair serves ARM template modification. ARM template modification cannot replace Bicep variables in reviewed Bicep deployment pipeline. Use this Bicep variables pair instead: First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
- **D — Correct.** First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
  First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter. This ordered Bicep variables workflow lets the reviewed Bicep deployment pipeline reuse a computed expression inside the template without exposing it to callers and then verify the resulting state.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Variables in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables)

**Source reviewed:** 2026-08-31

## LAB10-Q44 — A

**Question:** The reviewed Bicep deployment pipeline runbook must return a deployment value needed by a later workflow, then retain template deployment read-back evidence. Which reviewed Bicep deployment pipeline pair completes both duties?

- **A — Correct.** First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
  First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present. For reviewed Bicep deployment pipeline, the Bicep outputs operation precedes its Bicep outputs read-back check, allowing it to return a deployment value needed by a later workflow.
- **B — Incorrect.** First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted.
  First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted. This reviewed Bicep deployment pipeline pair serves deployment what-if. Deployment what-if cannot replace Bicep outputs in reviewed Bicep deployment pipeline. Use this Bicep outputs pair instead: First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
- **C — Incorrect.** First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.
  First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution. This reviewed Bicep deployment pipeline pair serves ARM template modification. Reviewed Bicep deployment pipeline proves ARM template modification, but Bicep outputs lacks implementation in reviewed Bicep deployment pipeline and Bicep outputs proof; the Bicep outputs outcome to return a deployment value needed by a later workflow remains open.
- **D — Incorrect.** First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies.
  First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies. This reviewed Bicep deployment pipeline pair serves declarative resource state. Reviewed Bicep deployment pipeline uses declarative resource state for both steps; Bicep outputs remains untouched in reviewed Bicep deployment pipeline, so its Bicep outputs gate to return a deployment value needed by a later workflow fails.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Outputs in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/outputs)

**Source reviewed:** 2026-08-31

## LAB10-Q45 — C

**Question:** To satisfy the template deployment requirement, operators must change the reviewed Bicep deployment pipeline configuration and prove it can ensure one declared resource is deployed after another resource it references. Which sequence is coherent?

- **A — Incorrect.** First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.
  First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution. This reviewed Bicep deployment pipeline pair serves deployment scope and mode. Deployment scope and mode cannot replace symbolic dependencies in reviewed Bicep deployment pipeline. Use this symbolic dependencies pair instead: First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.
- **B — Incorrect.** First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies.
  First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies. This reviewed Bicep deployment pipeline pair serves declarative resource state. Reviewed Bicep deployment pipeline proves declarative resource state, but symbolic dependencies lacks implementation in reviewed Bicep deployment pipeline and symbolic dependencies proof; the symbolic dependencies outcome to ensure one declared resource is deployed after another resource it references remains open.
- **C — Correct.** First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.
  First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources. In the reviewed Bicep deployment pipeline, the first symbolic dependencies step runs; the reviewed Bicep deployment pipeline then reads symbolic dependencies state to prove it can ensure one declared resource is deployed after another resource it references.
- **D — Incorrect.** First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
  First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values. This reviewed Bicep deployment pipeline pair serves Bicep parameters. Reviewed Bicep deployment pipeline closes Bicep parameters, not symbolic dependencies; without the symbolic dependencies workflow, it cannot ensure one declared resource is deployed after another resource it references.

**Objectives:** `CP-IAC-01`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [Resource dependencies in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies)

**Source reviewed:** 2026-08-31

## LAB10-Q46 — D

**Question:** The infrastructure administrator reviewing and deploying Bicep safely needs a safe reviewed Bicep deployment pipeline change to preview control-plane changes before applying the deployment, followed by template deployment evidence. Which pair merits approval?

- **A — Incorrect.** First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.
  First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties. This reviewed Bicep deployment pipeline pair serves modifying Bicep resources. Reviewed Bicep deployment pipeline proves modifying Bicep resources, but deployment what-if lacks implementation in reviewed Bicep deployment pipeline and deployment what-if proof; the deployment what-if outcome to preview control-plane changes before applying the deployment remains open.
- **B — Incorrect.** First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
  First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values. This reviewed Bicep deployment pipeline pair serves Bicep parameters. Reviewed Bicep deployment pipeline uses Bicep parameters for both steps; deployment what-if remains untouched in reviewed Bicep deployment pipeline, so its deployment what-if gate to preview control-plane changes before applying the deployment fails.
- **C — Incorrect.** First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
  First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter. This reviewed Bicep deployment pipeline pair serves Bicep variables. Reviewed Bicep deployment pipeline closes Bicep variables, not deployment what-if; without the deployment what-if workflow, it cannot preview control-plane changes before applying the deployment.
- **D — Correct.** First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted.
  For the reviewed Bicep deployment pipeline, the safe deployment what-if order is: first, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted. The reviewed Bicep deployment pipeline records deployment what-if proof after configuration.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB10-CP01`).

**Microsoft Learn sources:**

- [Bicep what-if deployment operation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

**Source reviewed:** 2026-08-31

## LAB10-Q47 — D

**Question:** The reviewed Bicep deployment pipeline has two template deployment gates: deploy the template at the intended boundary with understood replacement behavior, then prove the reviewed Bicep deployment pipeline state. Which template deployment sequence works?

- **A — Incorrect.** First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
  First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output. This reviewed Bicep deployment pipeline pair serves ARM-to-Bicep decompilation. Reviewed Bicep deployment pipeline uses ARM-to-Bicep decompilation for both steps; deployment scope and mode remains untouched in reviewed Bicep deployment pipeline, so its deployment scope and mode gate to deploy the template at the intended boundary with understood replacement behavior fails.
- **B — Incorrect.** First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter.
  First, Use a variable for a deterministic expression derived from parameters and resource metadata. Then, Inspect the compiled expression and confirm the value is not exposed as an unnecessary parameter. This reviewed Bicep deployment pipeline pair serves Bicep variables. Reviewed Bicep deployment pipeline closes Bicep variables, not deployment scope and mode; without the deployment scope and mode workflow, it cannot deploy the template at the intended boundary with understood replacement behavior.
- **C — Incorrect.** First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
  First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present. This reviewed Bicep deployment pipeline pair serves Bicep outputs. Bicep outputs cannot replace deployment scope and mode in reviewed Bicep deployment pipeline. Use this deployment scope and mode pair instead: First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.
- **D — Correct.** First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.
  First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution. The reviewed Bicep deployment pipeline uses its deployment scope and mode mutation gate and deployment scope and mode verification gate before it can deploy the template at the intended boundary with understood replacement behavior.

**Objectives:** `CP-IAC-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB10-CP02`).

**Microsoft Learn sources:**

- [Deploy Bicep files with Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)

**Source reviewed:** 2026-08-31

## LAB10-Q48 — A

**Question:** Which template deployment path makes the reviewed Bicep deployment pipeline able to change a declared resource and redeploy the updated desired state, then inspects the defining properties?

- **A — Correct.** First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.
  The reviewed Bicep deployment pipeline gets a complete modifying Bicep resources sequence here: first, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties. Read-back evidence follows the change.
- **B — Incorrect.** First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.
  First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution. This reviewed Bicep deployment pipeline pair serves ARM template modification. ARM template modification cannot replace modifying Bicep resources in reviewed Bicep deployment pipeline. Use this modifying Bicep resources pair instead: First, Modify the symbolic resource and inspect what-if before approving the new deployment. Then, Compare what-if and deployment operations with the final resource properties.
- **C — Incorrect.** First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present.
  First, Output nonsecret resource IDs or endpoints needed by later validation stages. Then, Read deployment outputs and confirm no credential or access token is present. This reviewed Bicep deployment pipeline pair serves Bicep outputs. Reviewed Bicep deployment pipeline proves Bicep outputs, but modifying Bicep resources lacks implementation in reviewed Bicep deployment pipeline and modifying Bicep resources proof; the modifying Bicep resources outcome to change a declared resource and redeploy the updated desired state remains open.
- **D — Incorrect.** First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.
  First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources. This reviewed Bicep deployment pipeline pair serves symbolic dependencies. Reviewed Bicep deployment pipeline uses symbolic dependencies for both steps; modifying Bicep resources remains untouched in reviewed Bicep deployment pipeline, so its modifying Bicep resources gate to change a declared resource and redeploy the updated desired state fails.

**Objectives:** `CP-IAC-03`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB10-CP03`).

**Microsoft Learn sources:**

- [Bicep language overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

**Source reviewed:** 2026-08-31

## LAB10-Q49 — B

**Question:** At the reviewed Bicep deployment pipeline approval gate, operators must show that the template deployment can turn an exported JSON template into maintainable Bicep as a starting point. Which template deployment configure-and-check pair is defensible?

- **A — Incorrect.** First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies.
  First, Describe resources and properties declaratively rather than scripting imperative create steps. Then, Build the Bicep file and inspect the resulting template resources and dependencies. This reviewed Bicep deployment pipeline pair serves declarative resource state. Declarative resource state cannot replace ARM-to-Bicep decompilation in reviewed Bicep deployment pipeline. Use this ARM-to-Bicep decompilation pair instead: First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
- **B — Correct.** First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output.
  First, Decompile the JSON template, build the result, and review warnings before adopting it. Then, Compare resources and expressions in the source template with the compiled Bicep output. This ordered ARM-to-Bicep decompilation workflow lets the reviewed Bicep deployment pipeline turn an exported JSON template into maintainable Bicep as a starting point and then verify the resulting state.
- **C — Incorrect.** First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources.
  First, Reference the symbolic resource directly and add dependsOn only for dependencies Bicep cannot infer. Then, Build the template and inspect dependency relationships between the relevant resources. This reviewed Bicep deployment pipeline pair serves symbolic dependencies. Reviewed Bicep deployment pipeline uses symbolic dependencies for both steps; ARM-to-Bicep decompilation remains untouched in reviewed Bicep deployment pipeline, so its ARM-to-Bicep decompilation gate to turn an exported JSON template into maintainable Bicep as a starting point fails.
- **D — Incorrect.** First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted.
  First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted. This reviewed Bicep deployment pipeline pair serves deployment what-if. Reviewed Bicep deployment pipeline closes deployment what-if, not ARM-to-Bicep decompilation; without the ARM-to-Bicep decompilation workflow, it cannot turn an exported JSON template into maintainable Bicep as a starting point.

**Objectives:** `CP-IAC-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB10-CP04`).

**Microsoft Learn sources:**

- [Decompile ARM templates to Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile)

**Source reviewed:** 2026-08-31

## LAB10-Q50 — B

**Question:** The reviewed Bicep deployment pipeline forbids a partial template deployment result. Operators must first modify a JSON deployment template without breaking its schema structure and afterward confirm the reviewed Bicep deployment pipeline outcome. Which template deployment sequence is complete?

- **A — Incorrect.** First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values.
  First, Define parameters for environment-specific values and supply them from an approved parameter source. Then, Build the file and inspect parameter types, defaults, decorators, and supplied deployment values. This reviewed Bicep deployment pipeline pair serves Bicep parameters. Reviewed Bicep deployment pipeline proves Bicep parameters, but ARM template modification lacks implementation in reviewed Bicep deployment pipeline and ARM template modification proof; the ARM template modification outcome to modify a JSON deployment template without breaking its schema structure remains open.
- **B — Correct.** First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.
  First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution. For reviewed Bicep deployment pipeline, the ARM template modification operation precedes its ARM template modification read-back check, allowing it to modify a JSON deployment template without breaking its schema structure.
- **C — Incorrect.** First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted.
  First, Run group what-if and review create, modify, delete, and ignore results before execution. Then, Save the what-if result and confirm no unapproved deletion or replacement is predicted. This reviewed Bicep deployment pipeline pair serves deployment what-if. Reviewed Bicep deployment pipeline closes deployment what-if, not ARM template modification; without the ARM template modification workflow, it cannot modify a JSON deployment template without breaking its schema structure.
- **D — Incorrect.** First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution.
  First, Use the intended scope and choose incremental behavior unless complete-mode deletion is explicitly reviewed. Then, Query deployment scope, provisioning state, mode, and operations after execution. This reviewed Bicep deployment pipeline pair serves deployment scope and mode. Deployment scope and mode cannot replace ARM template modification in reviewed Bicep deployment pipeline. Use this ARM template modification pair instead: First, Validate the modified JSON template and preview its changes before deployment. Then, Run template validation and what-if, then inspect deployment operations after execution.

**Objectives:** `CP-IAC-02`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB10-CP05`).

**Microsoft Learn sources:**

- [ARM template structure and syntax](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax)

**Source reviewed:** 2026-08-31
