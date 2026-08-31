#!/usr/bin/env python3
"""Validate the offline contract for the complete AZ-104 learning environment."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import unquote

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from assessment_contract import (
    ASSESSMENT_PLAN,
    DOMAIN_DISPLAY_NAMES,
    DOMAIN_OBJECTIVE_PREFIXES,
    expected_domain_difficulties,
    metadata_for_lab,
)
from render_diagrams import DiagramError, render_lab_svg


ROOT = Path(__file__).resolve().parents[1]
LAB_PATTERN = re.compile(r"^(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*$")
LAB_IDS = tuple(f"{number:02d}" for number in range(28))
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MERMAID_TYPES = (
    "flowchart",
    "graph",
    "sequenceDiagram",
    "classDiagram",
    "stateDiagram",
    "erDiagram",
)
GENERATED_LAB_BEGIN = "<!-- BEGIN GENERATED AZ104 V2 -->"
GENERATED_LAB_END = "<!-- END GENERATED AZ104 V2 -->"
SCHEMA_FILES = (
    "lab-schema.json",
    "question-schema.json",
    "run-manifest-schema.json",
    "validation-schema.json",
    "cleanup-schema.json",
    "catalog-schema.json",
    "progress-schema.json",
)
LIFECYCLE_FILES = ("Preflight.ps1", "Setup.ps1", "Validate.ps1", "Cleanup.ps1")
REQUIRED_README_SECTIONS = {
    "scenario": (r"scenario",),
    "objectives and checkpoints": (r"objective", r"checkpoint"),
    "architecture walkthrough": (r"architecture",),
    "concept primer or design decisions": (r"concept primer", r"design decision"),
    "inputs": (r"input",),
    "preflight": (r"preflight",),
    "final validation and results": (r"final validation", r"result interpretation"),
    "break/fix": (r"break.?fix",),
    "optional challenge": (r"challenge",),
    "troubleshooting": (r"troubleshoot",),
    "cleanup and residual checks": (r"cleanup", r"residual"),
    "exam debrief": (r"exam debrief",),
    "Microsoft Learn sources": (r"microsoft learn", r"sources"),
    "lifecycle script appendix": (r"script appendix", r"lifecycle script"),
}
TASK_REQUIREMENTS = {
    "expected state": r"expected state",
    "positive validation": r"positive validation",
    "negative validation": r"negative validation",
    "evidence": r"evidence",
    "failure and retry guidance": r"common failure|safe retry|retry guidance",
    "cleanup dependency": r"cleanup depend",
}
GENERIC_CONTENT = re.compile(
    r"\b(?:todo|tbd|placeholder|lorem ipsum|see the official objective map|"
    r"verify the configured resources|confirm the expected resources|generic checkpoint|"
    r"confirm context, prerequisites, inputs, and service availability|"
    r"configure the service-specific security and operational settings|"
    r"inspect expected behavior and the intentionally denied path|"
    r"named service properties agree with the run manifest|"
    r"the service does not yet show the expected state for checkpoint|"
    r"correct only the named prerequisite or choose a supported region/sku|"
    r"query the exact manifest id first; repeat the create command only when|"
    r"read the current property, compare it with the target, and reissue only|"
    r"remove only the injected fault, rerun the same diagnosis|"
    r"rerun validate\.ps1 and the exact read-only failed probe|"
    r"remove this checkpoint only after every dependent checkpoint listed in lab\.yml|"
    r"checkpoint id and utc time|redacted object/resource id|"
    r"queried expected property|negative-check result|"
    r"execute the lab-specific read-only provider, sku, tool, region, or service-capability assertions|"
    r"every authored service capability assertion returns the expected value|"
    r"the service reports the properties associated with|"
    r"no conflicting or unowned state is visible when checking the boundary|"
    r"\bproving\s+(?:prove|verify)\b|"
    r"a disposable non-production azure environment needs|"
    r"confirm the expected state for lab\d{2}-cp\d{2}|"
    r"query returns the recorded object or intended property|"
    r"did not create broader or unsafe access|"
    r"build and prove the .+ checkpoint as part of the administrator workflow)\b",
    re.IGNORECASE,
)
AZURE_POWERSHELL = re.compile(r"\b(?:Connect|Get|New|Set|Update|Remove)-(?:Az|Mg)[A-Z]", re.I)
BASH_MARKER = re.compile(r"(?:```(?:bash|sh|shell)\b|#!/usr/bin/(?:env\s+)?(?:ba)?sh\b|set -euo pipefail)", re.I)
DIRECT_AZURE_COMMAND = re.compile(r"(?m)(?:^|[\s;&|()])(?:az|azcopy)\s+", re.I)
MUTATING_AZURE_COMMAND = re.compile(
    r"(?im)^\s*(?:\$[A-Za-z][A-Za-z0-9]*\s*=\s*)?"
    r"(?:az\s+rest\s+[^\r\n]*--method\s+(?:post|put|patch|delete)\b|"
    r"az\s+[^\r\n]*\b(?:create|update|delete|set|assign|add|remove|start|stop|restart|swap|restore|failover)\b|"
    r"azcopy\s+(?:copy|sync|remove)\b)",
)
PORTAL_WORKFLOW = re.compile(
    r"\b(?:open|sign\s+in\s+to|navigate\s+to|click|select)\b[^.\n]{0,80}\b(?:Azure\s+)?portal\b",
    re.I,
)
IGNORED_DIRECTORY_NAMES = {
    ".cache",
    ".git",
    ".mypy_cache",
    ".packages",
    ".pytest_cache",
    ".site-docs",
    ".state",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "reports",
    "site",
    "site-build",
    "testresults",
    "tmp",
    "venv",
}


def is_ignored_path(path: Path) -> bool:
    """Return true for generated/runtime directories excluded by repository policy."""
    try:
        parts = path.resolve().relative_to(ROOT).parts
    except ValueError:
        return False
    return any(part.lower() in IGNORED_DIRECTORY_NAMES for part in parts)


class Results:
    """Collect checks without stopping at the first migration error."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def ok(self, message: str) -> None:
        self.passes.append(message)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def error_location(error) -> str:
    return ".".join(str(part) for part in error.absolute_path) or "<root>"


def validate_with_schema(instance, schema_path: Path, label: str, results: Results) -> bool:
    """Validate an instance and emit actionable paths for every schema failure."""
    try:
        schema = load_json(schema_path)
    except (OSError, json.JSONDecodeError) as exc:
        results.error(f"{label}: cannot load {schema_path.relative_to(ROOT)}: {exc}")
        return False
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    failures = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
    required_by_location: dict[str, list[str]] = defaultdict(list)
    for failure in failures:
        location = error_location(failure)
        if failure.validator == "required":
            missing = re.match(r"^'(.+)' is a required property$", failure.message)
            required_by_location[location].append(missing.group(1) if missing else failure.message)
            continue
        results.error(f"{label} schema at {location}: {failure.message}")
    for location, fields in required_by_location.items():
        results.error(f"{label} schema at {location}: missing required fields {', '.join(sorted(fields))}")
    if not failures:
        results.ok(f"{label} satisfies {schema_path.name}")
    return not failures


def validate_schema_documents(results: Results) -> None:
    """Ensure the schemas used by CI are themselves valid Draft 2020-12 documents."""
    for name in SCHEMA_FILES:
        path = ROOT / "curriculum" / name
        if not path.exists():
            results.error(f"Missing required schema curriculum/{name}")
            continue
        try:
            Draft202012Validator.check_schema(load_json(path))
        except Exception as exc:  # jsonschema exposes multiple schema exception types
            results.error(f"curriculum/{name} is not a valid Draft 2020-12 schema: {exc}")
        else:
            results.ok(f"curriculum/{name} is a valid Draft 2020-12 schema")


def collect_blueprint(results: Results) -> tuple[set[str], set[str]]:
    path = ROOT / "curriculum" / "blueprint.yml"
    if not path.exists():
        results.error("Missing curriculum/blueprint.yml")
        return set(), set()
    data = load_yaml(path) or {}
    domains = data.get("domains", [])
    official: list[str] = []
    groups = 0
    for domain in domains:
        domain_objectives = 0
        for group in domain.get("groups", []):
            groups += 1
            objectives = group.get("objectives", [])
            domain_objectives += len(objectives)
            official.extend(item.get("id", "") for item in objectives)
            if len(objectives) != group.get("objectiveCount"):
                results.error(f"Blueprint group {group.get('id')} objectiveCount is inconsistent")
        if domain_objectives != domain.get("objectiveCount"):
            results.error(f"Blueprint domain {domain.get('id')} objectiveCount is inconsistent")

    foundations = {item.get("id", "") for item in data.get("foundationObjectives", [])}
    if len(domains) != 5 or groups != 15 or len(official) != 82:
        results.error(
            f"Blueprint count mismatch: domains={len(domains)}, groups={groups}, objectives={len(official)}"
        )
    elif len(set(official)) != 82:
        results.error("Official blueprint objective IDs are not unique")
    else:
        results.ok("Blueprint contains 5 domains, 15 groups, and 82 unique official objectives")

    if len(foundations) != 5 or not all(item.startswith("FD-") for item in foundations):
        results.error("Expected five separate FD-* foundation objectives")
    else:
        results.ok("Blueprint contains five non-exam foundation objectives")
    return set(official), foundations


def find_lab_dirs(results: Results) -> list[Path]:
    labs_root = ROOT / "labs"
    if not labs_root.exists():
        results.error("Missing labs directory")
        return []
    lab_dirs = sorted(path for path in labs_root.iterdir() if path.is_dir() and LAB_PATTERN.fullmatch(path.name))
    numbers = [path.name[:2] for path in lab_dirs]
    if numbers != list(LAB_IDS):
        missing = sorted(set(LAB_IDS) - set(numbers))
        extras = sorted(set(numbers) - set(LAB_IDS))
        results.error(
            "Repository must implement exactly labs 00 through 27; "
            f"found={len(lab_dirs)}, missing={missing or 'none'}, unexpected={extras or 'none'}"
        )
    else:
        results.ok("Repository implements exactly 28 labs numbered 00 through 27")
    return lab_dirs


def validate_catalog(results: Results) -> tuple[dict[str, dict], dict]:
    path = ROOT / "labs" / "catalog.yml"
    if not path.exists():
        results.error("Missing labs/catalog.yml")
        return {}, {}
    data = load_yaml(path) or {}
    validate_with_schema(data, ROOT / "curriculum" / "catalog-schema.json", "labs/catalog.yml", results)
    labs = data.get("labs", []) if isinstance(data, dict) else []
    catalog: dict[str, dict] = {}
    for item in labs if isinstance(labs, list) else []:
        if isinstance(item, dict):
            number = str(item.get("id", "")).zfill(2)
            if number in catalog:
                results.error(f"labs/catalog.yml: duplicate lab ID {number}")
            catalog[number] = item
    if set(catalog) != set(LAB_IDS):
        results.error("labs/catalog.yml must contain every ID from 00 through 27 exactly once")
    return catalog, data


def contains_generic_content(value: str) -> bool:
    return bool(GENERIC_CONTENT.search(value or ""))


def normalized_words(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", value.casefold())


def near_duplicate_pairs(stems: list[str]) -> list[tuple[int, int]]:
    """Find high-confidence near clones without penalizing shared AZ-104 terminology."""
    token_sets = [set(normalized_words(stem)) for stem in stems]
    duplicates: list[tuple[int, int]] = []
    for left in range(len(stems)):
        for right in range(left + 1, len(stems)):
            union = token_sets[left] | token_sets[right]
            if not union:
                continue
            jaccard = len(token_sets[left] & token_sets[right]) / len(union)
            if jaccard < 0.78:
                continue
            similarity = SequenceMatcher(None, stems[left], stems[right], autojunk=False).ratio()
            if similarity >= 0.88:
                duplicates.append((left, right))
    return duplicates


def command_is_allowed(command: str) -> bool:
    """Accept Azure CLI/AzCopy and PowerShell host checks; reject alternate Azure shells."""
    if AZURE_POWERSHELL.search(command) or BASH_MARKER.search(command):
        return False
    return bool(
        DIRECT_AZURE_COMMAND.search(command)
        or re.search(
            r"\b(?:Get-Command|Get-ChildItem|Test-Path)\b|\$PSVersionTable\b|"
            r"\b(?:pwsh|node|python|npm)\s+--?version\b",
            command,
            re.I,
        )
    )


def command_signature(command: str) -> str:
    """Normalize non-executing evidence labels before comparing independent checks."""
    without_label = re.sub(
        r"(?is)^\s*\$validationId\s*=\s*(['\"]).*?\1\s*;\s*",
        "",
        command,
        count=1,
    )
    return re.sub(r"\s+", " ", without_label).strip().casefold()


def detect_dependency_cycle(graph: dict[str, set[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        if any(visit(dependency) for dependency in graph.get(node, set())):
            return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in graph)


def validate_lab_contract(
    lab_dir: Path,
    lab: dict,
    valid_objectives: set[str],
    results: Results,
) -> set[str]:
    """Validate semantic relationships that JSON Schema cannot express."""
    number = lab_dir.name[:2]
    label = lab_dir.name
    expected_ids = [f"LAB{number}-CP{index:02d}" for index in range(1, 6)]
    if lab.get("id") != f"LAB-{number}" or lab.get("slug") != lab_dir.name:
        results.error(f"{label}: folder, slug, and lab ID must agree")
    if lab.get("status") == "live-verified" or lab.get("lastLiveVerified") is not None:
        results.error(f"{label}: offline overhaul must not claim live verification")

    objectives = lab.get("objectives", []) if isinstance(lab.get("objectives"), list) else []
    unknown_objectives = sorted(set(objectives) - valid_objectives)
    if unknown_objectives:
        results.error(f"{label}: unknown objective IDs: {', '.join(unknown_objectives)}")

    checkpoints = lab.get("checkpoints", []) if isinstance(lab.get("checkpoints"), list) else []
    checkpoint_ids = [item.get("id") for item in checkpoints if isinstance(item, dict)]
    if checkpoint_ids != expected_ids:
        results.error(f"{label}: checkpoint IDs must be ordered exactly as {expected_ids}; found {checkpoint_ids}")
    checkpoint_set = set(checkpoint_ids)

    mapped_objectives: set[str] = set()
    check_ids: list[str] = []
    purpose_values: list[str] = []
    expected_values: list[str] = []
    validation_commands: list[str] = []
    graph: dict[str, set[str]] = {}
    for index, checkpoint in enumerate(checkpoints, start=1):
        if not isinstance(checkpoint, dict):
            continue
        checkpoint_id = checkpoint.get("id", f"checkpoint-{index}")
        if contains_generic_content(str(checkpoint.get("title", ""))):
            results.error(f"{label}/{checkpoint_id}: title contains placeholder or generic content")
        objective_ids = set(checkpoint.get("objectiveIds", []))
        mapped_objectives |= objective_ids
        outside = objective_ids - set(objectives)
        if outside:
            results.error(f"{label}/{checkpoint_id}: maps objectives absent from lab.yml: {sorted(outside)}")

        purpose = str(checkpoint.get("purpose", ""))
        expected_state = str(checkpoint.get("expectedState", ""))
        purpose_values.append(purpose.strip().casefold())
        expected_values.append(expected_state.strip().casefold())
        for field_name, field_value in (("purpose", purpose), ("expectedState", expected_state)):
            if contains_generic_content(field_value):
                results.error(f"{label}/{checkpoint_id}: {field_name} contains placeholder or generic content")

        markers = checkpoint.get("scriptMarkers") or {}
        for stage in ("setup", "validate", "cleanup"):
            if markers.get(stage) != checkpoint_id:
                results.error(f"{label}/{checkpoint_id}: scriptMarkers.{stage} must equal {checkpoint_id}")

        remediation = checkpoint.get("remediation") or {}
        expected_anchor = f"task-{index}"
        if remediation.get("anchor") != expected_anchor:
            results.error(f"{label}/{checkpoint_id}: remediation.anchor must be {expected_anchor}")

        validation = checkpoint.get("validation") or {}
        for kind in ("positive", "negative"):
            check = validation.get(kind) or {}
            check_id = check.get("id")
            if check_id:
                check_ids.append(check_id)
            description = str(check.get("description", ""))
            command = str(check.get("command", ""))
            validation_commands.append(command_signature(command))
            if contains_generic_content(description):
                results.error(f"{label}/{checkpoint_id}: {kind} validation is generic")
            if command and not command_is_allowed(command):
                results.error(
                    f"{label}/{checkpoint_id}: {kind} validation must use Azure CLI/AzCopy "
                    "hosted in PowerShell (PowerShell-only local checks are allowed only in preflight)"
                )
        positive_command = command_signature(str((validation.get("positive") or {}).get("command", "")))
        negative_command = command_signature(str((validation.get("negative") or {}).get("command", "")))
        if positive_command and positive_command == negative_command:
            results.error(f"{label}/{checkpoint_id}: positive and negative validation commands must be independent")

        cleanup = checkpoint.get("cleanup") or {}
        dependencies = set(cleanup.get("dependsOn", []))
        graph[checkpoint_id] = dependencies
        if checkpoint_id in dependencies:
            results.error(f"{label}/{checkpoint_id}: cleanup dependency cannot reference itself")
        unknown_dependencies = dependencies - checkpoint_set
        if unknown_dependencies:
            results.error(f"{label}/{checkpoint_id}: unknown cleanup dependencies {sorted(unknown_dependencies)}")
        residual = cleanup.get("residualCheck") or {}
        if residual.get("id"):
            check_ids.append(residual["id"])
        residual_command = str(residual.get("command", ""))
        if residual_command and not command_is_allowed(residual_command):
            results.error(f"{label}/{checkpoint_id}: residual check is not an allowed CLI-hosted command")
        if contains_generic_content(str(cleanup.get("action", ""))):
            results.error(f"{label}/{checkpoint_id}: cleanup action is generic")

    if mapped_objectives != set(objectives):
        missing = sorted(set(objectives) - mapped_objectives)
        results.error(f"{label}: every lab objective must map to a checkpoint; missing={missing}")
    if len(check_ids) != len(set(check_ids)):
        duplicates = sorted(item for item, count in Counter(check_ids).items() if count > 1)
        results.error(f"{label}: validation/residual check IDs must be unique; duplicates={duplicates}")
    if len(purpose_values) != len(set(purpose_values)):
        results.error(f"{label}: every checkpoint needs a distinct operational purpose")
    if len(expected_values) != len(set(expected_values)):
        results.error(f"{label}: every checkpoint needs a distinct expected state")
    if len(set(validation_commands)) < min(8, len(validation_commands)):
        results.error(f"{label}: checkpoint validation commands are overly repeated; use service-specific checks")
    if detect_dependency_cycle(graph):
        results.error(f"{label}: checkpoint cleanup dependencies contain a cycle")

    input_ids: list[str] = []
    for item in lab.get("inputs", []) if isinstance(lab.get("inputs"), list) else []:
        if not isinstance(item, dict):
            continue
        input_ids.append(str(item.get("id", "")))
        unknown_checkpoints = set(item.get("checkpointIds", [])) - checkpoint_set
        if unknown_checkpoints:
            results.error(f"{label}/input {item.get('id')}: unknown checkpoint IDs {sorted(unknown_checkpoints)}")
        safe_example = str(item.get("safeExample", ""))
        if item.get("secret") and not (
            re.search(r"(?i)redacted|interactive|environment|not stored", safe_example)
            or re.fullmatch(r"<[^>]+>", safe_example)
        ):
            results.error(f"{label}/input {item.get('id')}: secret safeExample must be a non-secret placeholder")
    if len(input_ids) != len(set(input_ids)):
        results.error(f"{label}: input IDs must be unique")

    acknowledgements = lab.get("acknowledgements") or {}
    if (acknowledgements.get("cost") or {}).get("parameter") != "AcknowledgeCost":
        results.error(f"{label}: acknowledgements.cost.parameter must be AcknowledgeCost")
    if (acknowledgements.get("tenantChange") or {}).get("parameter") != "AcknowledgeTenantChange":
        results.error(f"{label}: acknowledgements.tenantChange.parameter must be AcknowledgeTenantChange")
    required_artifacts = {
        ".state/<run-id>/run.json",
        ".state/<run-id>/validation.json",
        ".state/<run-id>/cleanup.json",
    }
    declared_artifacts = set((lab.get("creates") or {}).get("localArtifacts", []))
    if not required_artifacts.issubset(declared_artifacts):
        results.error(f"{label}: creates.localArtifacts must declare run.json, validation.json, and cleanup.json")

    preflight = lab.get("preflightChecks", []) if isinstance(lab.get("preflightChecks"), list) else []
    preflight_types = {item.get("type") for item in preflight if isinstance(item, dict)}
    for required_type in ("context", "tool", "input"):
        if required_type not in preflight_types:
            results.error(f"{label}: preflightChecks must include a {required_type} check")
    if (lab.get("providers") or {}).get("required") and "provider" not in preflight_types:
        results.error(f"{label}: required resource providers need a read-only provider preflight check")
    if (lab.get("creates") or {}).get("azureResources") and not preflight_types.intersection({"quota", "sku", "region"}):
        results.error(f"{label}: Azure resource labs need at least one quota, SKU, or region preflight check")
    for check in preflight:
        if not isinstance(check, dict):
            continue
        if contains_generic_content(str(check.get("description", ""))):
            results.error(f"{label}/preflight {check.get('id')}: description is generic")
        command = str(check.get("command", ""))
        if command and not command_is_allowed(command):
            results.error(f"{label}/preflight {check.get('id')}: command uses an unsupported command surface")

    residual_ids = [
        item.get("id")
        for item in (lab.get("cleanup") or {}).get("residualChecks", [])
        if isinstance(item, dict)
    ]
    if len(residual_ids) != len(set(residual_ids)):
        results.error(f"{label}: cleanup.residualChecks IDs must be unique")

    if not results.errors or not any(message.startswith(f"{label}:") for message in results.errors):
        results.ok(f"{label}: substantive five-checkpoint lab contract is internally consistent")
    return checkpoint_set


def validate_scripts(lab_dir: Path, lab: dict, checkpoint_ids: set[str], results: Results) -> None:
    label = lab_dir.name
    scripts_root = lab_dir / "scripts"
    lanes = sorted(path for path in scripts_root.glob("*") if path.is_dir()) if scripts_root.exists() else []
    if [lane.name for lane in lanes] != ["cli"]:
        results.error(f"{label}: scripts/ must contain only scripts/cli")
        return

    lane = lanes[0]
    files = sorted(path for path in lane.iterdir() if path.is_file())
    if {path.name for path in files} != set(LIFECYCLE_FILES):
        results.error(f"{label}: scripts/cli must contain exactly {', '.join(LIFECYCLE_FILES)}")
    if any(path.suffix.lower() != ".ps1" for path in files):
        results.error(f"{label}: every learner lifecycle script must be a PowerShell .ps1 host")

    texts: dict[str, str] = {}
    for name in LIFECYCLE_FILES:
        path = lane / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        texts[name] = text
        relative = path.relative_to(ROOT)
        if "LAB-{number}" in text:
            results.error(f"{relative}: contains an unsubstituted LAB-{{number}} template token")
        if not DIRECT_AZURE_COMMAND.search(text):
            results.error(f"{relative}: must contain at least one direct Azure CLI or AzCopy command")
        if AZURE_POWERSHELL.search(text):
            results.error(f"{relative}: contains an Azure PowerShell or Microsoft Graph PowerShell cmdlet")
        if BASH_MARKER.search(text):
            results.error(f"{relative}: contains Bash syntax or a Bash code fence")
        if re.search(r"(?im)^\s*(?:&\s*)?az\s+login\b", text):
            results.error(f"{relative}: lifecycle scripts must not sign in on the learner's behalf")

    setup = texts.get("Setup.ps1", "")
    validate = texts.get("Validate.ps1", "")
    cleanup = texts.get("Cleanup.ps1", "")
    preflight = texts.get("Preflight.ps1", "")
    if setup and not re.search(r"\[switch\]\s*\$Execute\b", setup, re.I):
        results.error(f"{label}/Setup.ps1: must expose [switch]$Execute and preview by default")
    if setup and not re.search(r"if\s*\(\s*-not\s+\$Execute\s*\)", setup, re.I):
        results.error(f"{label}/Setup.ps1: must return from an explicit preview guard before mutations")
    if cleanup and not re.search(r"\[switch\]\s*\$Execute\b", cleanup, re.I):
        results.error(f"{label}/Cleanup.ps1: must expose [switch]$Execute and preview by default")
    if cleanup and not re.search(r"if\s*\(\s*-not\s+\$Execute\s*\)", cleanup, re.I):
        results.error(f"{label}/Cleanup.ps1: must implement an explicit preview branch")
    if validate and not (
        re.search(r"\$Mode\b", validate)
        and "Deployment" in validate
        and "PostCleanup" in validate
    ):
        results.error(f"{label}/Validate.ps1: must expose -Mode Deployment|PostCleanup")
    if validate:
        positive_assertions = len(re.findall(r"AUTHORED SERVICE ASSERTION:\s*positive", validate))
        negative_assertions = len(re.findall(r"AUTHORED SERVICE ASSERTION:\s*negative", validate))
        expected_assertions = len(checkpoint_ids)
        if positive_assertions != expected_assertions or negative_assertions != expected_assertions:
            results.error(
                f"{label}/Validate.ps1: every checkpoint needs authored positive and negative "
                f"service assertions; found {positive_assertions}/{negative_assertions}, "
                f"expected {expected_assertions}/{expected_assertions}"
            )
        if "serviceProbe=pass" not in validate:
            results.error(f"{label}/Validate.ps1: must execute authored service probes, not only manifest/tag checks")

    for checkpoint in lab.get("checkpoints", []):
        validation_contract = checkpoint.get("validation") or {}
        for kind in ("positive", "negative"):
            assertion = str((validation_contract.get(kind) or {}).get("command", ""))
            if not re.search(r"(?i)\bthrow\b", assertion):
                results.error(
                    f"{label}/lab.yml {checkpoint.get('id')} {kind}: validation command must "
                    "self-assert the returned state with an explicit throw"
                )

    for stage_name, stage_text in (("Setup.ps1", setup), ("Validate.ps1", validate), ("Cleanup.ps1", cleanup)):
        for checkpoint_id in sorted(checkpoint_ids):
            if checkpoint_id not in stage_text:
                results.error(f"{label}/{stage_name}: missing stable marker {checkpoint_id}")

    acknowledgement = lab.get("acknowledgements") or {}
    if (acknowledgement.get("cost") or {}).get("required"):
        if "AcknowledgeCost" not in setup:
            results.error(f"{label}/Setup.ps1: cost acknowledgement is required but -AcknowledgeCost is absent")
    if (acknowledgement.get("tenantChange") or {}).get("required"):
        if "AcknowledgeTenantChange" not in setup:
            results.error(
                f"{label}/Setup.ps1: tenant-change acknowledgement is required but "
                "-AcknowledgeTenantChange is absent"
            )

    if "run.json" not in setup:
        results.error(f"{label}/Setup.ps1: must persist .state/<run-id>/run.json")
    if "validation.json" not in validate:
        results.error(f"{label}/Validate.ps1: must persist .state/<run-id>/validation.json")
    if "cleanup.json" not in cleanup:
        results.error(f"{label}/Cleanup.ps1: must persist .state/<run-id>/cleanup.json")
    if "run.json" not in cleanup:
        results.error(f"{label}/Cleanup.ps1: must scope deletion to the recorded run manifest")

    if setup:
        first_mutation = MUTATING_AZURE_COMMAND.search(setup)
        manifest_writes = list(re.finditer(r"(?im)Set-Content[^\r\n]*(?:\$Manifest|run\.json)", setup))
        save_calls = list(re.finditer(r"(?im)^\s*Save-RunState\s*$", setup))
        persistence_points = save_calls if save_calls else manifest_writes
        if first_mutation and (not persistence_points or persistence_points[0].start() > first_mutation.start()):
            results.error(f"{label}/Setup.ps1: run state must be written before the first Azure mutation")
        if not manifest_writes:
            results.error(f"{label}/Setup.ps1: state persistence helper must write to the run manifest")
        if len(persistence_points) < 6:
            results.error(
                f"{label}/Setup.ps1: expected an initial manifest write plus one after each checkpoint; "
                f"found {len(persistence_points)} persistence calls"
            )

    if cleanup:
        if not re.search(r"(?i)ownership|owned", cleanup):
            results.error(f"{label}/Cleanup.ps1: must explicitly verify ownership before deletion")
        if not re.search(r"(?i)throw|refus", cleanup):
            results.error(f"{label}/Cleanup.ps1: must refuse cleanup when ownership cannot be proven")
        if re.search(r"(?i)\bpurge\b[^\r\n]*(?:--yes|--force|execute)", cleanup):
            results.error(f"{label}/Cleanup.ps1: irreversible purge must never execute automatically")

    if preflight:
        mutation = MUTATING_AZURE_COMMAND.search(preflight)
        if mutation:
            line = preflight.count("\n", 0, mutation.start()) + 1
            results.error(f"{label}/Preflight.ps1:{line}: preflight must be read-only")
        service_checks = [
            item for item in (lab.get("preflightChecks") or [])
            if isinstance(item, dict) and str(item.get("id", "")).startswith("preflight.authored")
        ]
        if lab.get("id") != "LAB-00" and not service_checks:
            results.error(f"{label}: preflight needs at least one authored service/SKU/quota assertion")
        for check in service_checks:
            if not re.search(r"(?i)\bthrow\b", str(check.get("command", ""))):
                results.error(
                    f"{label}/preflight {check.get('id')}: service check must self-assert its result"
                )


def heading_texts(markdown: str) -> list[str]:
    return [match.group(1).strip().casefold() for match in re.finditer(r"(?m)^#{2,4}\s+(.+?)\s*$", markdown)]


def has_semantic_heading(headings: list[str], alternatives: tuple[str, ...]) -> bool:
    return any(any(re.search(pattern, heading, re.I) for pattern in alternatives) for heading in headings)


def task_body(readme: str, task_number: int) -> str:
    anchor = re.search(
        rf"(?i)(?:<a\s+id=[\"']task-{task_number}[\"']\s*></a>|\{{\s*#task-{task_number}\s*\}})",
        readme,
    )
    if not anchor:
        return ""
    next_anchor = re.search(
        rf"(?i)(?:<a\s+id=[\"']task-{task_number + 1}[\"']\s*></a>|"
        rf"\{{\s*#task-{task_number + 1}\s*\}})",
        readme[anchor.end() :],
    ) if task_number < 5 else None
    if next_anchor:
        return readme[anchor.end() : anchor.end() + next_anchor.start()]
    appendix = re.search(r"(?im)^##\s+.*(?:script appendix|lifecycle script)", readme[anchor.end() :])
    if appendix:
        return readme[anchor.end() : anchor.end() + appendix.start()]
    return readme[anchor.end() :]


def validate_readme(lab_dir: Path, lab: dict, checkpoint_ids: set[str], results: Results) -> None:
    path = lab_dir / "README.md"
    label = lab_dir.name
    if not path.exists():
        results.error(f"{label}: missing README.md")
        return
    readme = path.read_text(encoding="utf-8", errors="replace")
    headings = heading_texts(readme)
    for section, alternatives in REQUIRED_README_SECTIONS.items():
        if not has_semantic_heading(headings, alternatives):
            results.error(f"{label}/README.md: missing learner section for {section}")

    if GENERATED_LAB_BEGIN not in readme or GENERATED_LAB_END not in readme:
        results.error(f"{label}/README.md: missing AZ104 v2 generated-section markers")
    if re.search(r"(?im)^\s*\*\*Status:\*\*", readme):
        results.error(f"{label}/README.md: learner-facing status banners are prohibited")
    if PORTAL_WORKFLOW.search(readme):
        results.error(f"{label}/README.md: contains a Portal workflow; use direct Azure CLI commands")
    if BASH_MARKER.search(readme):
        results.error(f"{label}/README.md: contains a Bash fence or Bash syntax")
    if AZURE_POWERSHELL.search(readme):
        results.error(f"{label}/README.md: contains Azure PowerShell or Graph PowerShell cmdlets")
    if contains_generic_content(readme):
        results.error(f"{label}/README.md: contains placeholder or generic instructional content")
    if "LAB-{number}" in readme:
        results.error(f"{label}/README.md: contains an unsubstituted LAB-{{number}} template token")
    if re.search(
        r"(?im)^Scenario: .*?(?:\.\s+is responding\b|\bassigns the (?:a|an)\b|\.\s+to build\b)",
        readme,
    ):
        results.error(f"{label}/README.md: contains malformed generated scenario prose")
    if re.search(r"(?m)^- .*\.\.$", readme):
        results.error(f"{label}/README.md: contains a generated evidence bullet with doubled punctuation")

    first_lines = "\n".join(readme.splitlines()[:50])
    last_lines = "\n".join(readme.splitlines()[-80:])
    for location, content in (("top", first_lines), ("bottom", last_lines)):
        if not re.search(r"(?i)\bcatalog\b", content):
            results.error(f"{label}/README.md: {location} navigation must link to the catalog")
        number = int(lab_dir.name[:2])
        if number > 0 and not re.search(r"(?i)\bprevious\b", content):
            results.error(f"{label}/README.md: {location} navigation must include Previous")
        if number < 27 and not re.search(r"(?i)\bnext\b", content):
            results.error(f"{label}/README.md: {location} navigation must include Next")

    for index, checkpoint_id in enumerate(sorted(checkpoint_ids), start=1):
        body = task_body(readme, index)
        if not body:
            results.error(f"{label}/README.md: missing stable remediation anchor #task-{index}")
            continue
        if checkpoint_id not in body:
            results.error(f"{label}/README.md#task-{index}: must identify checkpoint {checkpoint_id}")
        command_blocks = re.findall(r"```powershell\s*(.*?)```", body, flags=re.I | re.S)
        if not any(DIRECT_AZURE_COMMAND.search(block) for block in command_blocks):
            results.error(
                f"{label}/README.md#task-{index}: guided task needs a direct Azure CLI/AzCopy PowerShell block"
            )
        for requirement, pattern in TASK_REQUIREMENTS.items():
            if not re.search(pattern, body, re.I):
                results.error(f"{label}/README.md#task-{index}: missing {requirement}")

    break_fix_match = re.search(r"(?ims)^##\s+.*break.?fix.*?(?=^##\s+|\Z)", readme)
    break_fix = break_fix_match.group(0) if break_fix_match else ""
    for element in ("inject", "symptom", "diagnos", "repair", "evidence"):
        if element not in break_fix.casefold():
            results.error(f"{label}/README.md: break/fix section must include {element}")

    if (lab.get("assessment") or {}).get("enabled") and "assessment/QUESTIONS.md" not in readme:
        results.error(f"{label}/README.md: assessment-enabled lab must link to assessment/QUESTIONS.md")
    if not re.search(r"\[[^\]]{8,}\]\(https://learn\.microsoft\.com/", readme):
        results.error(f"{label}/README.md: Microsoft Learn sources need descriptive link titles")


def validate_diagram(lab_dir: Path, results: Results) -> None:
    mmd = lab_dir / "diagrams" / "architecture.mmd"
    svg = lab_dir / "diagrams" / "architecture.svg"
    label = lab_dir.name
    allowed_visuals = {
        (lab_dir / "diagrams" / "architecture.mmd").resolve(),
        (lab_dir / "diagrams" / "architecture.svg").resolve(),
    }
    visual_suffixes = {".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".ico", ".avif"}
    extra_visuals = [
        path.relative_to(lab_dir)
        for path in lab_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in visual_suffixes and path.resolve() not in allowed_visuals
    ]
    extra_diagram_files = [
        path.relative_to(lab_dir)
        for path in (lab_dir / "diagrams").glob("*")
        if path.is_file() and path.resolve() not in allowed_visuals
    ] if (lab_dir / "diagrams").exists() else []
    if extra_visuals or extra_diagram_files:
        extras = sorted({str(path) for path in extra_visuals + extra_diagram_files})
        results.error(
            f"{label}: instructional visuals are limited to diagrams/architecture.mmd and "
            f"diagrams/architecture.svg; found {extras}"
        )
    source_exists = mmd.exists()
    if not source_exists:
        results.error(f"{label}: missing diagrams/architecture.mmd")
    else:
        lines = mmd.read_text(encoding="utf-8", errors="replace").splitlines()
        first = next((line.strip() for line in lines if line.strip() and not line.strip().startswith("%%")), "")
        if not first.startswith(MERMAID_TYPES):
            results.error(f"{label}: architecture.mmd does not declare a known Mermaid diagram type")
    if not svg.exists():
        results.error(f"{label}: missing diagrams/architecture.svg")
        return
    text = svg.read_text(encoding="utf-8", errors="replace")
    if "<svg" not in text:
        results.error(f"{label}: architecture.svg is not an SVG document")
    for requirement, pattern in (
        ("role=img", r"<svg\b[^>]*\brole=[\"']img[\"']"),
        ("accessible title", r"<title(?:\s|>)"),
        ("accessible description", r"<desc(?:\s|>)"),
        ("aria-labelledby", r"<svg\b[^>]*\baria-labelledby="),
    ):
        if not re.search(pattern, text, re.I):
            results.error(f"{label}: architecture.svg is missing {requirement}")
    if source_exists:
        try:
            expected = render_lab_svg(lab_dir)
        except (DiagramError, OSError, UnicodeError) as exc:
            results.error(f"{label}: architecture.mmd cannot be rendered deterministically: {exc}")
        else:
            if text != expected:
                results.error(
                    f"{label}: architecture.svg has drifted from architecture.mmd; "
                    "run python tools/render_diagrams.py"
                )
            else:
                results.ok(f"{label}: architecture.mmd and accessible architecture.svg are synchronized")


def validate_pester_contract(lab_dir: Path, checkpoint_ids: set[str], results: Results) -> None:
    path = lab_dir / "tests" / "Contract.Tests.ps1"
    label = lab_dir.name
    if not path.exists():
        results.error(f"{label}: missing tests/Contract.Tests.ps1")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    if not re.search(r"(?im)^\s*Mock\s+az\b", text):
        results.error(f"{label}/tests/Contract.Tests.ps1: Azure CLI calls must be mocked")
    if not re.search(r"(?is)function\s+global:az\b.+unmocked Azure CLI call", text):
        results.error(
            f"{label}/tests/Contract.Tests.ps1: missing the hard offline guard beneath the az mock"
        )
    if "$TestDrive" not in text:
        results.error(
            f"{label}/tests/Contract.Tests.ps1: lifecycle invocations must use an isolated TestDrive harness"
        )

    invocation_requirements = {
        "Setup preview invocation": (
            r"(?is)&\s*\$script:HarnessSetup\b.+?-RunId\s+\$runId.+?-Location\b"
        ),
        "Setup preview no-state assertion": (
            r"(?is)HarnessSetup.+?\.state/\$runId.+?Should\s+-Not\s+-Exist"
        ),
        "Cleanup ownership-refusal invocation": (
            r"(?is)\{\s*&\s*\$script:HarnessCleanup\b.+?-Execute\s*\}"
            r"\s*\|\s*Should\s+-Throw.+?ownership refusal"
        ),
        "PostCleanup validation invocation": (
            r"(?is)&\s*\$script:HarnessValidate\b.+?-Mode\s+PostCleanup\b"
        ),
        "PostCleanup artifact assertion": (
            r"(?is)validation\.json.+?artifact\.mode.+?PostCleanup.+?artifact\.result.+?pass"
        ),
        "idempotent Cleanup assertion": (
            r"(?is)status\s*=\s*'cleaned'.+?\$script:HarnessCleanup\b.+?cleanup\.idempotent"
        ),
        "mocked no-call boundaries": r"(?is)Should\s+-Invoke\s+az\s+-Times\s+0",
        "mocked residual-query boundary": (
            r"(?is)Az104ContractAzCalls.+?Should\s+-BeGreaterThan\s+0.+?Should\s+-Invoke\s+az"
        ),
        "Pester-safe failure isolation": (
            r"(?is)\$text\s*=\s*\$text\s+-replace.+?exit 1.+?Lifecycle script reported failure"
        ),
    }
    for requirement, pattern in invocation_requirements.items():
        if not re.search(pattern, text):
            results.error(
                f"{label}/tests/Contract.Tests.ps1: missing executable contract evidence for {requirement}"
            )

    cleanup_invocations = re.findall(r"(?im)&\s*\$script:HarnessCleanup\b", text)
    if len(cleanup_invocations) < 2:
        results.error(
            f"{label}/tests/Contract.Tests.ps1: must invoke Cleanup for both refusal and idempotency"
        )

    substantive_fixture_requirements = {
        "independent positive and negative checks": r"ValidationFixture\.checks.+?negative.+?positive",
        "partial failure persistence": r"Sync-ManagedResource.+?status = 'failed'.+?Save-RunState",
        "successful cleanup ownership": r"CleanupFixture\.ownershipVerified.+?activeManagedObjects",
    }
    for requirement, pattern in substantive_fixture_requirements.items():
        if not re.search(pattern, text, re.I | re.S):
            results.error(
                f"{label}/tests/Contract.Tests.ps1: missing substantive fixture assertion for {requirement}"
            )
    for checkpoint_id in checkpoint_ids:
        if checkpoint_id not in text:
            results.error(f"{label}/tests/Contract.Tests.ps1: missing checkpoint {checkpoint_id}")


def validate_run_fixture(
    lab_dir: Path,
    lab: dict,
    checkpoint_ids: set[str],
    results: Results,
) -> None:
    path = lab_dir / "tests" / "fixtures" / "run.sample.json"
    label = f"{lab_dir.name}/tests/fixtures/run.sample.json"
    if not path.exists():
        results.error(f"{lab_dir.name}: missing tests/fixtures/run.sample.json")
        return
    data = load_json(path)
    if not validate_with_schema(data, ROOT / "curriculum" / "run-manifest-schema.json", label, results):
        return
    if data.get("labId") != lab.get("id"):
        results.error(f"{label}: labId must match lab.yml")
    states = data.get("checkpointStates", [])
    state_ids = [item.get("checkpointId") for item in states]
    if set(state_ids) != checkpoint_ids or len(state_ids) != len(checkpoint_ids):
        results.error(f"{label}: checkpointStates must contain each lab checkpoint exactly once")
    for item in data.get("managedObjects", []):
        if item.get("checkpointId") not in checkpoint_ids:
            results.error(f"{label}: managed object references unknown checkpoint {item.get('checkpointId')}")
    for item in data.get("originalSettings", []):
        if item.get("checkpointId") not in checkpoint_ids:
            results.error(f"{label}: original setting references unknown checkpoint {item.get('checkpointId')}")
    shared_change_text = " ".join(str(item) for item in lab.get("tenantScopedChanges", []))
    shared_setting_recorded = any(
        item.get("kind") == "shared-setting" for item in data.get("managedObjects", [])
    )
    if (
        shared_setting_recorded
        or re.search(r"(?i)\b(?:policy|scope|setting|configuration)\b", shared_change_text)
    ) and not data.get("originalSettings"):
        results.error(f"{label}: shared policy/setting changes require a recorded originalSettings sample")
    secret_inputs = {
        item.get("id")
        for item in lab.get("inputs", [])
        if isinstance(item, dict) and item.get("secret")
    }
    leaked = secret_inputs.intersection((data.get("inputs") or {}).keys())
    if leaked:
        results.error(f"{label}: run manifests must omit secret inputs; found {sorted(leaked)}")


def expected_validation_result(checks: list[dict]) -> str:
    if any(
        item.get("status") == "fail"
        or (item.get("status") == "skipped" and item.get("required"))
        for item in checks
    ):
        return "fail"
    if any(item.get("status") == "skipped" for item in checks):
        return "partial"
    return "pass"


def validate_validation_fixture(
    lab_dir: Path,
    lab: dict,
    checkpoint_ids: set[str],
    results: Results,
) -> None:
    path = lab_dir / "tests" / "fixtures" / "validation.sample.json"
    label = f"{lab_dir.name}/tests/fixtures/validation.sample.json"
    if not path.exists():
        results.error(f"{lab_dir.name}: missing tests/fixtures/validation.sample.json")
        return
    data = load_json(path)
    if not validate_with_schema(data, ROOT / "curriculum" / "validation-schema.json", label, results):
        return
    if data.get("labId") != lab.get("id"):
        results.error(f"{label}: labId must match lab.yml")
    if data.get("mode") != "Deployment":
        results.error(f"{label}: canonical validation fixture must exercise Deployment mode")
    checks = data.get("checks", [])
    summary = data.get("summary") or {}
    derived_summary = {
        "required": sum(bool(item.get("required")) for item in checks),
        "passed": sum(item.get("status") == "pass" for item in checks),
        "failed": sum(item.get("status") == "fail" for item in checks),
        "skipped": sum(item.get("status") == "skipped" for item in checks),
    }
    if summary != derived_summary:
        results.error(f"{label}: summary must equal derived check counts {derived_summary}; found {summary}")
    expected_result = expected_validation_result(checks)
    if data.get("result") != expected_result:
        results.error(f"{label}: result must be {expected_result} for the recorded check statuses")

    check_ids: list[str] = []
    kinds_by_checkpoint: dict[str, set[str]] = defaultdict(set)
    for check in checks:
        check_ids.append(str(check.get("id", "")))
        checkpoint_id = check.get("checkpointId")
        if checkpoint_id not in checkpoint_ids:
            results.error(f"{label}: check {check.get('id')} references unknown checkpoint {checkpoint_id}")
        kinds_by_checkpoint[checkpoint_id].add(str(check.get("kind")))
    if len(check_ids) != len(set(check_ids)):
        results.error(f"{label}: validation check IDs must be unique")
    for checkpoint_id in checkpoint_ids:
        missing_kinds = {"positive", "negative"} - kinds_by_checkpoint[checkpoint_id]
        if missing_kinds:
            results.error(f"{label}: {checkpoint_id} lacks {sorted(missing_kinds)} evidence")


def validate_cleanup_fixture(
    lab_dir: Path,
    lab: dict,
    checkpoint_ids: set[str],
    results: Results,
) -> None:
    path = lab_dir / "tests" / "fixtures" / "cleanup.sample.json"
    label = f"{lab_dir.name}/tests/fixtures/cleanup.sample.json"
    if not path.exists():
        results.error(f"{lab_dir.name}: missing tests/fixtures/cleanup.sample.json")
        return
    data = load_json(path)
    if not validate_with_schema(data, ROOT / "curriculum" / "cleanup-schema.json", label, results):
        return
    if data.get("labId") != lab.get("id"):
        results.error(f"{label}: labId must match lab.yml")
    if data.get("executionMode") != "execute" or data.get("result") != "pass":
        results.error(f"{label}: canonical cleanup fixture must demonstrate a successful execute path")
    if data.get("activeManagedObjects"):
        results.error(f"{label}: successful cleanup cannot retain active managed objects")
    if data.get("retainedItems") and not (lab.get("cleanup") or {}).get("retainedItemsAllowed"):
        results.error(f"{label}: retained items are not permitted by lab.yml")
    for action in data.get("actions", []):
        if action.get("checkpointId") not in checkpoint_ids:
            results.error(f"{label}: cleanup action references unknown checkpoint {action.get('checkpointId')}")
        if action.get("status") in {"deleted", "soft-deleted", "retained"} and not (
            action.get("ownership") or {}
        ).get("verified"):
            results.error(f"{label}: cleanup action {action.get('targetId')} changed an unverified target")
    expected_residual_ids = {
        item.get("id")
        for item in (lab.get("cleanup") or {}).get("residualChecks", [])
        if isinstance(item, dict)
    }
    fixture_residual_ids = {item.get("id") for item in data.get("residualChecks", [])}
    missing = expected_residual_ids - fixture_residual_ids
    if missing:
        results.error(f"{label}: missing declared residual checks {sorted(missing)}")


def validate_assessment(
    lab_dir: Path,
    lab: dict,
    checkpoint_ids: set[str],
    valid_objectives: set[str],
    results: Results,
) -> tuple[set[str], list[dict]]:
    number = lab_dir.name[:2]
    expected_metadata = metadata_for_lab(number)
    metadata = lab.get("assessment") or {}
    assessment_dir = lab_dir / "assessment"
    if metadata != expected_metadata:
        results.error(f"{lab_dir.name}: assessment metadata must match {expected_metadata}; found {metadata}")

    if not metadata.get("enabled"):
        if assessment_dir.exists():
            results.error(f"{lab_dir.name}: disabled assessment must not have an assessment directory")
        else:
            results.ok(f"{lab_dir.name}: assessment is intentionally disabled")
        return set(), []

    required_files = ("questions.yml", "QUESTIONS.md", "ANSWERS.md")
    missing_files = [name for name in required_files if not (assessment_dir / name).exists()]
    if missing_files:
        results.error(f"{lab_dir.name}: missing assessment files {missing_files}")
        return set(), []

    questions = load_yaml(assessment_dir / "questions.yml")
    validate_with_schema(
        questions,
        ROOT / "curriculum" / "question-schema.json",
        f"{lab_dir.name}/assessment/questions.yml",
        results,
    )
    if not isinstance(questions, list):
        return set(), []

    expected_count = int(metadata.get("questionCount", 0))
    if len(questions) != expected_count:
        results.error(f"{lab_dir.name}: expected {expected_count} questions; found {len(questions)}")
    ids = [question.get("id") for question in questions]
    expected_ids = [f"LAB{number}-Q{index:02d}" for index in range(1, expected_count + 1)]
    if ids != expected_ids:
        results.error(f"{lab_dir.name}: question IDs must be contiguous from LAB{number}-Q01 to Q50")

    difficulties = Counter(question.get("difficulty") for question in questions)
    expected_difficulties = Counter(ASSESSMENT_PLAN[number]["difficulties"])
    if difficulties != expected_difficulties:
        results.error(
            f"{lab_dir.name}: difficulty mix must be {dict(expected_difficulties)}; found {dict(difficulties)}"
        )
    answers = Counter(question.get("correctOption") for question in questions)
    if set(answers) != {"A", "B", "C", "D"} or any(count not in {12, 13} for count in answers.values()):
        results.error(f"{lab_dir.name}: answer positions must each occur 12 or 13 times; found {dict(answers)}")

    stems = [str(question.get("stem", "")).strip().casefold() for question in questions]
    if len(stems) != len(set(stems)):
        results.error(f"{lab_dir.name}: question stems must be unique")
    near_duplicates = near_duplicate_pairs(stems)
    if near_duplicates:
        examples = [f"Q{left + 1:02d}/Q{right + 1:02d}" for left, right in near_duplicates[:8]]
        results.error(
            f"{lab_dir.name}: near-duplicate question stems detected ({', '.join(examples)}"
            f"{'…' if len(near_duplicates) > 8 else ''})"
        )
    option_sets: list[tuple[str, ...]] = []
    mapped: set[str] = set()
    domain = metadata.get("primaryDomain")
    objective_prefix = DOMAIN_OBJECTIVE_PREFIXES.get(domain, "")
    checkpoint_anchors = {
        checkpoint.get("id"): f"#{(checkpoint.get('remediation') or {}).get('anchor')}"
        for checkpoint in lab.get("checkpoints", [])
        if isinstance(checkpoint, dict)
    }
    for question in questions:
        question_id = question.get("id", "<unknown>")
        options = question.get("options") or {}
        normalized_options = [str(options.get(letter, "")).strip().casefold() for letter in "ABCD"]
        if len(set(normalized_options)) != 4:
            results.error(f"{question_id}: all four options must be distinct")
        option_sets.append(tuple(sorted(normalized_options)))

        for objective in question.get("objectiveIds", []):
            mapped.add(objective)
            if objective not in valid_objectives:
                results.error(f"{question_id}: unknown objective ID {objective}")
            elif not objective.startswith(objective_prefix):
                results.error(f"{question_id}: objective {objective} is outside primary domain {domain}")

        mapped_checkpoints = set(question.get("checkpointIds", []))
        unknown_checkpoints = mapped_checkpoints - checkpoint_ids
        if unknown_checkpoints:
            results.error(f"{question_id}: unknown checkpoint IDs {sorted(unknown_checkpoints)}")
        remediation_anchor = question.get("remediationAnchor")
        valid_anchors = {checkpoint_anchors.get(item) for item in mapped_checkpoints}
        if remediation_anchor not in valid_anchors:
            results.error(
                f"{question_id}: remediationAnchor {remediation_anchor!r} must match one mapped checkpoint"
            )

        explanations = question.get("optionExplanations") or {}
        if set(explanations) != {"A", "B", "C", "D"}:
            results.error(f"{question_id}: optionExplanations must explain A, B, C, and D")
        for letter, explanation in explanations.items():
            if contains_generic_content(str(explanation)):
                results.error(f"{question_id}: option {letter} explanation is generic")
        for source in question.get("sources", []):
            url = str(source.get("url", "")).casefold()
            if any(token in url for token in ("/powershell/", "azure-powershell", "portal.azure", "azure-portal")):
                results.error(f"{question_id}: procedural source must support the Azure CLI, API, or concept lane: {url}")

    repeated_sets = [item for item, count in Counter(option_sets).items() if count > 1]
    if repeated_sets:
        results.error(f"{lab_dir.name}: contains {len(repeated_sets)} repeated four-option sets")
    answer_sequence = [question.get("correctOption") for question in questions]
    for period in range(1, 11):
        if len(answer_sequence) > period and all(
            answer_sequence[index] == answer_sequence[index % period]
            for index in range(len(answer_sequence))
        ):
            results.error(f"{lab_dir.name}: answer key repeats a predictable period of {period}")
            break

    question_text = (assessment_dir / "QUESTIONS.md").read_text(encoding="utf-8")
    answer_text = (assessment_dir / "ANSWERS.md").read_text(encoding="utf-8")
    for question in questions:
        question_id = str(question.get("id"))
        if question_id not in question_text:
            results.error(f"{lab_dir.name}: {question_id} missing from QUESTIONS.md")
        if question_id not in answer_text:
            results.error(f"{lab_dir.name}: {question_id} missing from ANSWERS.md")
        for option in (question.get("options") or {}).values():
            if str(option) not in answer_text:
                results.error(f"{lab_dir.name}: {question_id} answer key does not repeat every option")
    if re.search(r"correctOption|optionExplanations|^# .*answer key|\bCorrect answer\b", question_text, re.M | re.I):
        results.error(f"{lab_dir.name}: QUESTIONS.md exposes answers or answer-key metadata")
    for band in ("85", "70"):
        if band not in answer_text:
            results.error(f"{lab_dir.name}: ANSWERS.md must document the {band}% learning-band threshold")
    return mapped, [{"domain": domain, "lab": number, **question} for question in questions]


def validate_catalog_consistency(
    catalog: dict[str, dict],
    lab_metadata: dict[str, dict],
    results: Results,
) -> None:
    fields = (
        "labId",
        "folder",
        "title",
        "domain",
        "track",
        "status",
        "difficulty",
        "estimatedMinutes",
        "costClass",
        "questionCount",
        "objectiveIds",
    )
    for number in LAB_IDS:
        if number not in catalog or number not in lab_metadata:
            continue
        lab = lab_metadata[number]
        expected = {
            "labId": lab.get("id"),
            "folder": lab.get("slug"),
            "title": lab.get("title"),
            "domain": lab.get("domain"),
            "track": lab.get("track"),
            "status": lab.get("status"),
            "difficulty": lab.get("difficulty"),
            "estimatedMinutes": lab.get("estimatedMinutes"),
            "costClass": (lab.get("cost") or {}).get("class"),
            "questionCount": (lab.get("assessment") or {}).get("questionCount"),
            "objectiveIds": lab.get("objectives"),
        }
        for field in fields:
            if catalog[number].get(field) != expected[field]:
                results.error(
                    f"labs/catalog.yml lab {number}: {field} is {catalog[number].get(field)!r}; "
                    f"expected {expected[field]!r} from lab.yml"
                )
        expected_previous = f"LAB-{int(number) - 1:02d}" if int(number) > 0 else None
        expected_next = f"LAB-{int(number) + 1:02d}" if int(number) < 27 else None
        if catalog[number].get("previousLabId") != expected_previous:
            results.error(f"labs/catalog.yml lab {number}: previousLabId must be {expected_previous!r}")
        if catalog[number].get("nextLabId") != expected_next:
            results.error(f"labs/catalog.yml lab {number}: nextLabId must be {expected_next!r}")


def validate_domain_question_contract(question_records: list[dict], results: Results) -> None:
    expected_total = sum(int(plan["questionCount"]) for plan in ASSESSMENT_PLAN.values())
    if len(question_records) != expected_total:
        results.error(f"Assessment contract requires {expected_total} questions; found {len(question_records)}")
    else:
        results.ok(f"Assessment bank contains exactly {expected_total} questions")

    stems = [str(question.get("stem", "")).strip().casefold() for question in question_records]
    if len(stems) != len(set(stems)):
        results.error("Assessment bank contains duplicate stems across labs")
    else:
        results.ok("All assessment stems are unique across the repository")

    option_signatures = [
        tuple(sorted(str(value).strip().casefold() for value in (question.get("options") or {}).values()))
        for question in question_records
    ]
    repeated_option_sets = sum(count - 1 for count in Counter(option_signatures).values() if count > 1)
    if repeated_option_sets:
        results.error(f"Assessment bank contains {repeated_option_sets} repeated four-option sets across labs")

    expected_difficulties = expected_domain_difficulties()
    for domain, display_name in DOMAIN_DISPLAY_NAMES.items():
        records = [question for question in question_records if question.get("domain") == domain]
        expected_count = sum(
            int(plan["questionCount"])
            for plan in ASSESSMENT_PLAN.values()
            if plan.get("enabled") and plan.get("primaryDomain") == domain
        )
        if len(records) != expected_count:
            results.error(f"{display_name}: expected {expected_count} questions; found {len(records)}")
            continue
        difficulties = Counter(question.get("difficulty") for question in records)
        if difficulties != expected_difficulties[domain]:
            results.error(
                f"{display_name}: difficulty mix must be {dict(expected_difficulties[domain])}; "
                f"found {dict(difficulties)}"
            )
        answers = Counter(question.get("correctOption") for question in records)
        minimum = expected_count // 4
        maximum = minimum + (1 if expected_count % 4 else 0)
        if set(answers) != {"A", "B", "C", "D"} or any(
            count not in {minimum, maximum} for count in answers.values()
        ):
            results.error(
                f"{display_name}: answer positions must each occur {minimum}–{maximum} times; found {dict(answers)}"
            )
        else:
            results.ok(f"{display_name}: count, difficulty, and answer-position contracts pass")


def validate_no_screenshot_contract(results: Results) -> None:
    prohibited_paths = [
        ROOT / "curriculum" / "screenshot-manifest-schema.json",
        ROOT / "tools" / "validate_images.py",
    ]
    prohibited_paths.extend((ROOT / "labs").glob("[0-9][0-9]-*/images"))
    existing = [path for path in prohibited_paths if path.exists()]
    for path in existing:
        results.error(f"Obsolete Portal screenshot artifact remains: {path.relative_to(ROOT)}")

    patterns = {
        "Portal screenshot requirement": re.compile(r"portal\s+screenshots?", re.I),
        "screenshot manifest reference": re.compile(r"screenshot[- ]manifest|images[/\\]portal", re.I),
        "Portal evidence section": re.compile(r"^##\s+Portal evidence\s*$", re.I | re.M),
    }
    hits = 0
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or is_ignored_path(path)
            or path.resolve() == Path(__file__).resolve()
            or path.suffix.lower() not in {".md", ".py", ".ps1", ".yml", ".yaml", ".json"}
        ):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in patterns.items():
            if pattern.search(text):
                hits += 1
                results.error(f"{path.relative_to(ROOT)} still contains {label}")
    if not existing and not hits:
        results.ok("No Portal screenshot directory, evidence section, schema, or requirement remains")


def validate_global_command_surface(results: Results) -> None:
    bad_shell_files = [
        path.relative_to(ROOT)
        for path in (ROOT / "labs").rglob("*")
        if path.is_file() and path.suffix.lower() in {".sh", ".bash"}
    ]
    if bad_shell_files:
        results.error(f"Learner labs contain prohibited Bash files: {bad_shell_files}")
    for path in (ROOT / "labs").rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".ps1"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if BASH_MARKER.search(text):
            results.error(f"{path.relative_to(ROOT)}: Bash is not a learner command surface")
        if AZURE_POWERSHELL.search(text):
            results.error(f"{path.relative_to(ROOT)}: Azure operations must use Azure CLI, not Az/Mg cmdlets")


def validate_markdown_links(results: Results) -> None:
    failures = 0
    for path in ROOT.rglob("*.md"):
        if is_ignored_path(path):
            continue
        # docs/site is staged into .site-docs by build_docs_site.py; its links
        # intentionally target the staged tree and are checked by the strict
        # MkDocs build rather than against the authoring-source directory.
        if (ROOT / "docs" / "site") in path.parents:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        prose = re.sub(r"`[^`\n]+`", "", prose)
        for raw_target in MARKDOWN_LINK.findall(prose):
            target = raw_target.strip().split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            try:
                resolved = (path.parent / target).resolve()
            except OSError:
                failures += 1
                results.error(f"{path.relative_to(ROOT)}: invalid local link target {raw_target}")
                continue
            if not resolved.exists():
                failures += 1
                results.error(f"{path.relative_to(ROOT)}: broken local link {raw_target}")
    if not failures:
        results.ok("Markdown local links resolve")


def validate_secret_markers(results: Results) -> None:
    patterns = {
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "Azure connection string": re.compile(r"DefaultEndpointsProtocol=https;AccountName=.+;AccountKey=", re.I),
        "client secret assignment": re.compile(r"(?i)(?:AZURE_CLIENT_SECRET|clientSecret)\s*[:=]\s*[\"']?[A-Za-z0-9+/=_-]{16,}"),
    }
    hits = 0
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or is_ignored_path(path)
            or path.resolve() == Path(__file__).resolve()
            or path.suffix.lower() in {".png", ".jpg", ".svg"}
        ):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in patterns.items():
            if pattern.search(text):
                hits += 1
                results.error(f"{path.relative_to(ROOT)}: possible committed {label}")
    if not hits:
        results.ok("No private-key, client-secret, or Azure connection-string markers detected")


def validate_workflows_are_offline(results: Results) -> None:
    workflows = ROOT / ".github" / "workflows"
    prohibited = {
        "Azure login action": re.compile(r"azure/login@", re.I),
        "Azure CLI login": re.compile(r"(?<![A-Za-z])az\s+login(?:\s|$)", re.I),
        "alternate Azure login": re.compile(r"Connect-AzAccount", re.I),
        "Azure credential secret": re.compile(r"AZURE_(?:CLIENT|TENANT|SUBSCRIPTION)(?:_ID)?", re.I),
    }
    hits = 0
    if workflows.exists():
        for path in workflows.glob("*.y*ml"):
            text = path.read_text(encoding="utf-8", errors="replace")
            for label, pattern in prohibited.items():
                if pattern.search(text):
                    hits += 1
                    results.error(f"{path.relative_to(ROOT)}: workflow contains {label}")
    if not hits:
        results.ok("GitHub workflows contain no Azure authentication path")


def validate_generated_indexes(results: Results) -> None:
    question_index = ROOT / "docs" / "question-bank-index.md"
    status_index = ROOT / "docs" / "implementation-status.md"
    if question_index.exists():
        text = question_index.read_text(encoding="utf-8", errors="replace")
        question_rows = len(re.findall(r"(?m)^\|\s*LAB\d{2}-Q\d{2}\s*\|", text))
        if question_rows:
            results.error(
                "docs/question-bank-index.md must be a compact per-lab/objective dashboard, "
                f"not a {question_rows}-question table"
            )
    if status_index.exists():
        text = status_index.read_text(encoding="utf-8", errors="replace")
        if re.search(r"(?im)\boffline-validated\b|\blab status\b", text):
            results.error("docs/implementation-status.md must not expose learner-facing validation status")


def validate_lab_dirs(
    lab_dirs: list[Path],
    valid_objectives: set[str],
    results: Results,
) -> tuple[dict[str, dict], set[str], list[dict]]:
    metadata: dict[str, dict] = {}
    question_coverage: set[str] = set()
    question_records: list[dict] = []
    required_files = ("README.md", "lab.yml", "diagrams/architecture.mmd", "diagrams/architecture.svg")

    for lab_dir in lab_dirs:
        number = lab_dir.name[:2]
        for relative in required_files:
            if not (lab_dir / relative).exists():
                results.error(f"{lab_dir.name}: missing {relative}")
        lab_path = lab_dir / "lab.yml"
        if not lab_path.exists():
            continue
        lab = load_yaml(lab_path)
        if not isinstance(lab, dict):
            results.error(f"{lab_dir.name}/lab.yml: root must be a mapping")
            continue
        schema_ok = validate_with_schema(
            lab,
            ROOT / "curriculum" / "lab-schema.json",
            f"{lab_dir.name}/lab.yml",
            results,
        )
        if not schema_ok:
            results.error(
                f"{lab_dir.name}: fix lab.yml schema errors before semantic checkpoint, artifact, "
                "README, and assessment cross-checks run"
            )
            validate_diagram(lab_dir, results)
            continue
        metadata[number] = lab
        checkpoint_ids = validate_lab_contract(lab_dir, lab, valid_objectives, results)
        validate_scripts(lab_dir, lab, checkpoint_ids, results)
        validate_readme(lab_dir, lab, checkpoint_ids, results)
        validate_diagram(lab_dir, results)
        validate_pester_contract(lab_dir, checkpoint_ids, results)
        validate_run_fixture(lab_dir, lab, checkpoint_ids, results)
        validate_validation_fixture(lab_dir, lab, checkpoint_ids, results)
        validate_cleanup_fixture(lab_dir, lab, checkpoint_ids, results)
        mapped, records = validate_assessment(lab_dir, lab, checkpoint_ids, valid_objectives, results)
        question_coverage |= mapped
        question_records.extend(records)

        for text_file in lab_dir.rglob("*"):
            if text_file.is_file() and text_file.suffix.lower() in {".md", ".ps1"}:
                text = text_file.read_text(encoding="utf-8", errors="replace")
                if text_file.suffix.lower() == ".md":
                    # Previous/next navigation is required. Remove legitimate
                    # Markdown links before checking prose for runtime coupling.
                    text = re.sub(
                        r"\[[^\]]+\]\(\.\.[/\\](?:\d{2}-)[a-z0-9-]+/README\.md(?:#[^)]+)?\)",
                        "",
                        text,
                        flags=re.I,
                    )
                if re.search(r"\.\.[/\\](?:\d{2}-)[a-z0-9-]+", text, flags=re.I):
                    results.error(f"{text_file.relative_to(ROOT)}: forbidden cross-lab runtime reference")

    return metadata, question_coverage, question_records


def run_validation(release: bool = False) -> Results:
    """Run all checks and return structured results for CI or focused diagnostics."""
    results = Results()

    validate_schema_documents(results)
    official, foundations = collect_blueprint(results)
    lab_dirs = find_lab_dirs(results)
    catalog, _ = validate_catalog(results)
    metadata, coverage, question_records = validate_lab_dirs(
        lab_dirs,
        official | foundations,
        results,
    )
    validate_catalog_consistency(catalog, metadata, results)
    validate_domain_question_contract(question_records, results)
    validate_no_screenshot_contract(results)
    validate_global_command_surface(results)
    validate_markdown_links(results)
    validate_secret_markers(results)
    validate_workflows_are_offline(results)
    validate_generated_indexes(results)

    missing = official - coverage
    if missing:
        results.error(f"{len(missing)} official objectives lack assessment coverage: {', '.join(sorted(missing))}")
    else:
        results.ok("All 82 official objectives have assessment coverage")

    if release and results.warnings:
        for warning in results.warnings:
            results.error(f"Release warning: {warning}")
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--release",
        action="store_true",
        help="Treat warnings as failures after enforcing the complete 28-lab contract",
    )
    args = parser.parse_args()
    results = run_validation(release=args.release)

    print("\nPASS")
    for message in results.passes:
        print(f"  - {message}")
    if results.warnings:
        print("\nWARN")
        for message in results.warnings:
            print(f"  - {message}")
    if results.errors:
        print("\nFAIL")
        for message in results.errors:
            print(f"  - {message}")
    print(
        f"\nSummary: {len(results.passes)} passed, {len(results.warnings)} warning(s), "
        f"{len(results.errors)} failure(s)"
    )
    return 1 if results.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
