#!/usr/bin/env python3
"""Generate the machine catalog and compact learner indexes from authoritative lab metadata."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from assessment_contract import DOMAIN_DISPLAY_NAMES


ROOT = Path(__file__).resolve().parents[1]
DOMAIN_LABELS = {
    "foundation": "Foundation",
    **DOMAIN_DISPLAY_NAMES,
    "capstone": "Capstone",
}
BLUEPRINT_DOMAIN_IDS = {
    "IG": "identity-governance",
    "ST": "storage",
    "CP": "compute",
    "NW": "networking",
    "MR": "monitor-recovery",
}


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def lab_records() -> list[tuple[Path, dict]]:
    records: list[tuple[Path, dict]] = []
    for path in sorted((ROOT / "labs").glob("[0-9][0-9]-*/lab.yml")):
        records.append((path.parent, load_yaml(path)))
    return records


def objective_catalog() -> tuple[dict[str, str], dict[str, str]]:
    blueprint = load_yaml(ROOT / "curriculum" / "blueprint.yml")
    titles: dict[str, str] = {}
    domains: dict[str, str] = {}
    for item in blueprint.get("foundationObjectives", []):
        titles[item["id"]] = item["title"]
        domains[item["id"]] = "foundation"
    for domain in blueprint.get("domains", []):
        domain_id = domain["id"]
        for group in domain.get("groups", []):
            for item in group.get("objectives", []):
                titles[item["id"]] = item["title"]
                domains[item["id"]] = BLUEPRINT_DOMAIN_IDS[domain_id]
    return titles, domains


def catalog_data(records: list[tuple[Path, dict]]) -> dict:
    if len(records) != 28:
        raise ValueError(f"Catalog generation requires exactly 28 lab.yml files; found {len(records)}")
    versions = {str(lab["blueprintVersion"]) for _, lab in records}
    if len(versions) != 1:
        raise ValueError(f"All labs must use one blueprintVersion; found {sorted(versions)}")
    labs: list[dict] = []
    for index, (folder, lab) in enumerate(records):
        number = folder.name[:2]
        if number != f"{index:02d}":
            raise ValueError(f"Expected lab {index:02d}; found {folder.name}")
        labs.append(
            {
                "id": number,
                "labId": lab["id"],
                "slug": folder.name[3:],
                "folder": folder.name,
                "title": lab["title"],
                "domain": lab["domain"],
                "track": lab["track"],
                "status": lab["status"],
                "difficulty": lab["difficulty"],
                "estimatedMinutes": lab["estimatedMinutes"],
                "costClass": lab["cost"]["class"],
                "questionCount": lab["assessment"]["questionCount"],
                "objectiveIds": lab["objectives"],
                "path": f"labs/{folder.name}/README.md",
                "previousLabId": f"LAB-{index - 1:02d}" if index > 0 else None,
                "nextLabId": f"LAB-{index + 1:02d}" if index < 27 else None,
            }
        )
    return {
        "schemaVersion": "2.0.0",
        "blueprintVersion": next(iter(versions)),
        "expectedLabCount": 28,
        "generatedFrom": "lab.yml",
        "labs": labs,
    }


def render_catalog(records: list[tuple[Path, dict]]) -> str:
    return yaml.safe_dump(
        catalog_data(records),
        sort_keys=False,
        allow_unicode=True,
        width=120,
    )


def assessment_records(records: list[tuple[Path, dict]]) -> list[dict]:
    questions: list[dict] = []
    for folder, lab in records:
        path = folder / "assessment" / "questions.yml"
        if not path.exists():
            continue
        for question in load_yaml(path):
            questions.append({"lab": folder.name, "domain": lab["domain"], **question})
    return questions


def render_question_index(records: list[tuple[Path, dict]]) -> str:
    titles, objective_domains = objective_catalog()
    questions = assessment_records(records)
    question_counts = Counter(question["domain"] for question in questions)
    objective_question_counts: Counter[str] = Counter()
    per_lab: dict[str, list[dict]] = defaultdict(list)
    for question in questions:
        per_lab[question["lab"]].append(question)
        objective_question_counts.update(question.get("objectiveIds", []))

    domain_rows: list[str] = []
    for domain, label in DOMAIN_DISPLAY_NAMES.items():
        domain_objectives = [item for item, item_domain in objective_domains.items() if item_domain == domain]
        assessed = sum(objective_question_counts[item] > 0 for item in domain_objectives)
        domain_rows.append(f"| {label} | {question_counts[domain]} | {assessed}/{len(domain_objectives)} |")

    lab_rows: list[str] = []
    for folder, lab in records:
        if not lab["assessment"]["enabled"]:
            continue
        lab_questions = per_lab[folder.name]
        mix = Counter(question["difficulty"] for question in lab_questions)
        mapped = {objective for question in lab_questions for objective in question.get("objectiveIds", [])}
        lab_objectives = {
            objective
            for objective in lab["objectives"]
            if objective_domains.get(objective) == lab["domain"]
        }
        lab_rows.append(
            f"| [Lab {folder.name[:2]}](../labs/{folder.name}/README.md) | "
            f"{DOMAIN_LABELS[lab['domain']]} | {len(lab_questions)} | "
            f"{mix['foundational']}/{mix['applied']}/{mix['advanced']} | "
            f"{len(mapped & lab_objectives)}/{len(lab_objectives)} | "
            f"[Questions](../labs/{folder.name}/assessment/QUESTIONS.md) |"
        )

    objective_rows: list[str] = []
    for objective_id, title in titles.items():
        if objective_id.startswith("FD-"):
            continue
        objective_rows.append(
            f"| `{objective_id}` | {DOMAIN_LABELS[objective_domains[objective_id]]} | "
            f"{title} | {objective_question_counts[objective_id]} |"
        )

    return f"""# Assessment coverage dashboard

This generated dashboard intentionally omits correct answers. Complete a lab's questions before opening its answer key.

## Domain coverage

| Official domain | Questions | Objectives assessed |
|---|---:|---:|
{chr(10).join(domain_rows)}

## Per-lab assessment

Difficulty is shown as foundational/applied/advanced.

| Lab | Official domain | Questions | Difficulty mix | Primary-domain objectives covered | Start |
|---|---|---:|---:|---:|---|
{chr(10).join(lab_rows)}

## Objective coverage

| Objective | Official domain | Topic | Questions |
|---|---|---|---:|
{chr(10).join(objective_rows)}

Generated by `python tools/generate_indexes.py`. Do not edit by hand.
"""


def render_lab_index(records: list[tuple[Path, dict]]) -> str:
    rows: list[str] = []
    for folder, lab in records:
        rows.append(
            f"| [Lab {folder.name[:2]}](../labs/{folder.name}/README.md) | {lab['title']} | "
            f"{DOMAIN_LABELS[lab['domain']]} | {lab['difficulty']} | {lab['estimatedMinutes']} min | "
            f"{lab['cost']['class']} | {len(lab['checkpoints'])} | {lab['assessment']['questionCount']} |"
        )
    return f"""# Lab catalog

Choose a lab by topic, difficulty, time, or cost. Repository validation metadata is intentionally omitted from this learner-facing page.

| Lab | Outcome | Domain | Difficulty | Time | Cost | Checkpoints | Questions |
|---|---|---|---|---:|---|---:|---:|
{chr(10).join(rows)}

Generated from the 28 authoritative `lab.yml` files by `python tools/generate_indexes.py`. Do not edit by hand.
"""


def update(path: Path, content: str, check: bool) -> bool:
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    if existing == content:
        print(f"PASS  {path.relative_to(ROOT)} is current")
        return True
    if check:
        print(f"FAIL  {path.relative_to(ROOT)} is stale; run python tools/generate_indexes.py")
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
    print(f"WRITE {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail rather than rewriting stale generated files")
    args = parser.parse_args()
    records = lab_records()
    outputs = (
        (ROOT / "labs" / "catalog.yml", render_catalog(records)),
        (ROOT / "docs" / "question-bank-index.md", render_question_index(records)),
        (ROOT / "docs" / "implementation-status.md", render_lab_index(records)),
    )
    return 0 if all(update(path, content, args.check) for path, content in outputs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
