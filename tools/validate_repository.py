#!/usr/bin/env python3
"""Validate the offline repository contract for the AZ-104 lab curriculum."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
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


ROOT = Path(__file__).resolve().parents[1]
LAB_PATTERN = re.compile(r"^(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MERMAID_TYPES = ("flowchart", "graph", "sequenceDiagram", "classDiagram", "stateDiagram", "erDiagram")
INLINE_COMMANDS_BEGIN = "<!-- BEGIN GENERATED INLINE COMMANDS -->"
INLINE_COMMANDS_END = "<!-- END GENERATED INLINE COMMANDS -->"
IGNORED_DIRECTORY_NAMES = {
    ".cache",
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".state",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "reports",
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


def validate_with_schema(instance, schema_path: Path, label: str, results: Results) -> None:
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    failures = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    for failure in failures:
        location = ".".join(str(part) for part in failure.path) or "<root>"
        results.error(f"{label} schema at {location}: {failure.message}")
    if not failures:
        results.ok(f"{label} satisfies {schema_path.name}")


def collect_blueprint(results: Results) -> tuple[set[str], set[str]]:
    path = ROOT / "curriculum" / "blueprint.yml"
    if not path.exists():
        results.error("Missing curriculum/blueprint.yml")
        return set(), set()
    data = load_yaml(path)
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


def validate_catalog(results: Results) -> dict[str, dict]:
    path = ROOT / "labs" / "catalog.yml"
    if not path.exists():
        results.error("Missing labs/catalog.yml")
        return {}
    data = load_yaml(path)
    labs = data.get("labs", [])
    catalog = {item.get("id", ""): item for item in labs}
    expected = {f"{number:02d}" for number in range(28)}
    if len(labs) != 28 or set(catalog) != expected:
        results.error("Lab catalog must contain each ID from 00 through 27 exactly once")
    else:
        results.ok("Lab catalog contains 28 unique entries from 00 through 27")
    return catalog


def validate_assessment(
    lab_dir: Path,
    lab: dict,
    valid_objectives: set[str],
    results: Results,
) -> tuple[set[str], list[dict]]:
    number = lab_dir.name[:2]
    expected_metadata = metadata_for_lab(number)
    metadata = lab.get("assessment") or {}
    assessment_dir = lab_dir / "assessment"
    if metadata != expected_metadata:
        results.error(
            f"{lab_dir.name}: assessment metadata must match the locked allocation {expected_metadata}"
        )

    if not metadata.get("enabled"):
        if assessment_dir.exists():
            results.error(f"{lab_dir.name}: disabled assessment must not have an assessment directory")
        else:
            results.ok(f"{lab_dir.name}: assessment is intentionally disabled")
        return set(), []

    required = ["questions.yml", "QUESTIONS.md", "ANSWERS.md"]
    for name in required:
        if not (assessment_dir / name).exists():
            results.error(f"{lab_dir.name}: missing assessment/{name}")
    if not all((assessment_dir / name).exists() for name in required):
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

    expected_count = metadata.get("questionCount")
    if len(questions) != expected_count:
        results.error(f"{lab_dir.name}: expected {expected_count} questions; found {len(questions)}")
    else:
        results.ok(f"{lab_dir.name}: contains its declared {expected_count} questions")

    ids = [question.get("id") for question in questions]
    expected_ids = [f"LAB{number}-Q{index:02d}" for index in range(1, len(questions) + 1)]
    if ids != expected_ids:
        results.error(f"{lab_dir.name}: question IDs must be unique and contiguous from Q01")
    else:
        results.ok(f"{lab_dir.name}: question IDs are unique and contiguous")

    difficulties = Counter(question.get("difficulty") for question in questions)
    expected_difficulties = Counter(ASSESSMENT_PLAN[number]["difficulties"])
    if difficulties != expected_difficulties:
        results.error(
            f"{lab_dir.name}: difficulty mix must be {dict(expected_difficulties)}; found {dict(difficulties)}"
        )
    else:
        results.ok(f"{lab_dir.name}: question difficulty mix matches its allocation")

    mapped: set[str] = set()
    domain = metadata.get("primaryDomain")
    objective_prefix = DOMAIN_OBJECTIVE_PREFIXES.get(domain, "")
    for question in questions:
        for objective in question.get("objectiveIds", []):
            mapped.add(objective)
            if objective not in valid_objectives:
                results.error(f"{question.get('id')}: unknown objective ID {objective}")
            elif not objective.startswith(objective_prefix):
                results.error(
                    f"{question.get('id')}: objective {objective} does not belong to primary domain {domain}"
                )

    question_text = (assessment_dir / "QUESTIONS.md").read_text(encoding="utf-8")
    answer_text = (assessment_dir / "ANSWERS.md").read_text(encoding="utf-8")
    for question_id in ids:
        if question_id not in question_text:
            results.error(f"{lab_dir.name}: {question_id} missing from QUESTIONS.md")
        if question_id not in answer_text:
            results.error(f"{lab_dir.name}: {question_id} missing from ANSWERS.md")
    if re.search(r"correctOption|distractorExplanations|^# .*answer key", question_text, re.MULTILINE | re.I):
        results.error(f"{lab_dir.name}: QUESTIONS.md exposes answer-key metadata")
    return mapped, [{"domain": domain, **question} for question in questions]


def validate_diagram(lab_dir: Path, results: Results) -> None:
    mmd = lab_dir / "diagrams" / "architecture.mmd"
    svg = lab_dir / "diagrams" / "architecture.svg"
    if mmd.exists():
        lines = mmd.read_text(encoding="utf-8", errors="replace").splitlines()
        first = next((line.strip() for line in lines if line.strip() and not line.strip().startswith("%%")), "")
        if not first.startswith(MERMAID_TYPES):
            results.error(f"{lab_dir.name}: architecture.mmd does not declare a known Mermaid diagram type")
    if not svg.exists():
        results.error(f"{lab_dir.name}: missing diagrams/architecture.svg")
    elif "<svg" not in svg.read_text(encoding="utf-8", errors="replace"):
        results.error(f"{lab_dir.name}: diagrams/architecture.svg is not a rendered SVG document")


def validate_lab_dirs(
    official: set[str],
    foundations: set[str],
    catalog: dict[str, dict],
    release: bool,
    results: Results,
) -> tuple[set[str], list[dict]]:
    labs_root = ROOT / "labs"
    lab_dirs = sorted(path for path in labs_root.iterdir() if path.is_dir() and LAB_PATTERN.fullmatch(path.name))
    question_coverage: set[str] = set()
    question_records: list[dict] = []
    required_files = ["README.md", "lab.yml", "diagrams/architecture.mmd", "diagrams/architecture.svg"]

    for lab_dir in lab_dirs:
        number = lab_dir.name[:2]
        for relative in required_files:
            if not (lab_dir / relative).exists():
                results.error(f"{lab_dir.name}: missing {relative}")
        lab_path = lab_dir / "lab.yml"
        if not lab_path.exists():
            continue
        lab = load_yaml(lab_path)
        validate_with_schema(
            lab,
            ROOT / "curriculum" / "lab-schema.json",
            f"{lab_dir.name}/lab.yml",
            results,
        )
        if lab.get("slug") != lab_dir.name or lab.get("id") != f"LAB-{number}":
            results.error(f"{lab_dir.name}: folder, slug, and lab ID disagree")
        if number not in catalog:
            results.error(f"{lab_dir.name}: no matching catalog entry")
        elif catalog[number].get("assessmentQuestionCount") != (lab.get("assessment") or {}).get("questionCount"):
            results.error(f"{lab_dir.name}: catalog assessmentQuestionCount disagrees with lab.yml")
        for objective in lab.get("objectives", []):
            if objective not in official | foundations:
                results.error(f"{lab_dir.name}: unknown objective ID {objective}")

        lanes = [path for path in (lab_dir / "scripts").glob("*") if path.is_dir()] if (lab_dir / "scripts").exists() else []
        if not lanes:
            results.error(f"{lab_dir.name}: no complete command lane under scripts/")
        for lane in lanes:
            names = {path.name.lower() for path in lane.iterdir() if path.is_file()}
            for stage in ("preflight", "setup", "validate", "cleanup"):
                if not any(name.startswith(stage.lower()) for name in names):
                    results.error(f"{lab_dir.name}: {lane.name} lane is missing {stage}")

        readme_path = lab_dir / "README.md"
        if readme_path.exists():
            readme = readme_path.read_text(encoding="utf-8", errors="replace")
            if INLINE_COMMANDS_BEGIN not in readme or INLINE_COMMANDS_END not in readme:
                results.error(f"{lab_dir.name}: README does not embed the complete lifecycle commands")
            else:
                results.ok(f"{lab_dir.name}: README contains the generated inline command lane")

        mapped, records = validate_assessment(lab_dir, lab, official | foundations, results)
        question_coverage |= mapped
        question_records.extend(records)
        validate_diagram(lab_dir, results)

        validation_fixture = lab_dir / "tests" / "fixtures" / "validation.sample.json"
        if validation_fixture.exists():
            validate_with_schema(
                load_json(validation_fixture),
                ROOT / "curriculum" / "validation-schema.json",
                f"{lab_dir.name}/tests/fixtures/validation.sample.json",
                results,
            )

        for text_file in lab_dir.rglob("*"):
            if (
                text_file.is_file()
                and not is_ignored_path(text_file)
                and text_file.suffix.lower() in {".md", ".sh", ".ps1"}
            ):
                text = text_file.read_text(encoding="utf-8", errors="replace")
                if re.search(r"\.\.[/\\](?:\d{2}-)[a-z0-9-]+", text, flags=re.IGNORECASE):
                    results.error(f"{text_file.relative_to(ROOT)}: forbidden cross-lab runtime reference")

    if release and len(lab_dirs) != 28:
        results.error(f"Release mode requires 28 implemented lab folders; found {len(lab_dirs)}")
    else:
        results.ok(f"Found {len(lab_dirs)} implemented lab folder(s); catalog retains the full 28-lab roadmap")
    return question_coverage, question_records


def validate_domain_question_contract(question_records: list[dict], results: Results) -> None:
    if len(question_records) != 250:
        results.error(f"Assessment contract requires 250 questions; found {len(question_records)}")
    else:
        results.ok("Assessment bank contains exactly 250 questions")

    expected_difficulties = expected_domain_difficulties()
    for domain, display_name in DOMAIN_DISPLAY_NAMES.items():
        records = [question for question in question_records if question.get("domain") == domain]
        if len(records) != 50:
            results.error(f"{display_name}: expected 50 questions; found {len(records)}")
            continue
        results.ok(f"{display_name}: contains exactly 50 questions")

        difficulties = Counter(question.get("difficulty") for question in records)
        if difficulties != expected_difficulties[domain]:
            results.error(
                f"{display_name}: difficulty mix must be {dict(expected_difficulties[domain])}; "
                f"found {dict(difficulties)}"
            )
        else:
            results.ok(f"{display_name}: difficulty mix is 15 foundational / 25 applied / 10 advanced")

        answers = Counter(question.get("correctOption") for question in records)
        if set(answers) != {"A", "B", "C", "D"} or any(count not in {12, 13} for count in answers.values()):
            results.error(f"{display_name}: answer positions must each occur 12 or 13 times; found {dict(answers)}")
        else:
            results.ok(f"{display_name}: answer positions are balanced 12–13 times each")


def validate_no_screenshot_contract(results: Results) -> None:
    prohibited_paths = [
        ROOT / "curriculum" / "screenshot-manifest-schema.json",
        ROOT / "tools" / "validate_images.py",
    ]
    prohibited_paths.extend((ROOT / "labs").glob("[0-9][0-9]-*/images"))
    existing = [path for path in prohibited_paths if path.exists()]
    for path in existing:
        results.error(f"Obsolete Portal screenshot artifact remains: {path.relative_to(ROOT)}")
    if not existing:
        results.ok("No Portal screenshot directories, schema, or image validator remain")

    patterns = {
        "Portal screenshot requirement": re.compile(r"portal\s+screenshots?", re.I),
        "screenshot manifest reference": re.compile(r"screenshot[- ]manifest|images[/\\]portal", re.I),
        "Portal evidence section": re.compile(r"^##\s+Portal evidence\s*$", re.I | re.M),
    }
    matches = 0
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or is_ignored_path(path)
            or path.resolve() == Path(__file__).resolve()
            or path.suffix.lower() not in {".md", ".py", ".yml", ".yaml", ".json"}
        ):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in patterns.items():
            if pattern.search(text):
                matches += 1
                results.error(f"{path.relative_to(ROOT)} still contains {label}")
    if not matches:
        results.ok("Documentation and tooling contain no Portal screenshot contract")


def validate_markdown_links(results: Results) -> None:
    failures = 0
    for path in ROOT.rglob("*.md"):
        if is_ignored_path(path):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                failures += 1
                results.error(f"{path.relative_to(ROOT)}: broken local link {raw_target}")
    if not failures:
        results.ok("Markdown local links resolve")


def validate_secret_markers(results: Results) -> None:
    patterns = {
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "Azure connection string": re.compile(r"DefaultEndpointsProtocol=https;AccountName=.+;AccountKey=", re.I),
    }
    hits = 0
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or is_ignored_path(path)
            or path == Path(__file__).resolve()
            or path.suffix.lower() in {".png", ".jpg", ".svg"}
        ):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in patterns.items():
            if pattern.search(text):
                hits += 1
                results.error(f"{path.relative_to(ROOT)}: possible committed {label}")
    if not hits:
        results.ok("No private-key or Azure connection-string markers detected")


def validate_workflows_are_offline(results: Results) -> None:
    workflows = ROOT / ".github" / "workflows"
    prohibited = {
        "Azure login action": re.compile(r"azure/login@", re.I),
        "Azure CLI login": re.compile(r"(?<![A-Za-z])az\s+login(?:\s|$)", re.I),
        "Az PowerShell login": re.compile(r"Connect-AzAccount", re.I),
        "Azure credential secret": re.compile(r"AZURE_(?:CLIENT|TENANT|SUBSCRIPTION)(?:_ID)?", re.I),
    }
    hits = 0
    if workflows.exists():
        for path in workflows.glob("*.y*ml"):
            text = path.read_text(encoding="utf-8", errors="replace")
            for label, pattern in prohibited.items():
                if pattern.search(text):
                    hits += 1
                    results.error(f"{path.relative_to(ROOT)}: pull-request workflow contains {label}")
    if not hits:
        results.ok("GitHub workflows contain no Azure authentication path")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="store_true", help="Require all 28 labs and full question coverage")
    args = parser.parse_args()
    results = Results()

    official, foundations = collect_blueprint(results)
    catalog = validate_catalog(results)
    coverage, question_records = validate_lab_dirs(official, foundations, catalog, args.release, results)
    validate_domain_question_contract(question_records, results)
    validate_no_screenshot_contract(results)
    validate_markdown_links(results)
    validate_secret_markers(results)
    validate_workflows_are_offline(results)

    missing = official - coverage
    if missing:
        results.error(
            f"{len(missing)} official objectives have no assessment question: {', '.join(sorted(missing))}"
        )
    else:
        results.ok("All 82 official objectives have assessment coverage")

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
