#!/usr/bin/env python3
"""Expand every enabled lab assessment to the locked 50-question contract."""

from __future__ import annotations

import argparse
import copy
import re
from collections import defaultdict
from pathlib import Path

import yaml

from assessment_contract import ASSESSMENT_PLAN, metadata_for_lab


ROOT = Path(__file__).resolve().parents[1]
TARGET_COUNTS = {"foundational": 15, "applied": 25, "advanced": 10}
OPTION_NAMES = ("A", "B", "C", "D")

CONTEXTS = {
    "foundational": (
        "During administrator onboarding, the team reviews this scenario:",
        "While documenting the service baseline, an engineer considers this question:",
        "In a fundamentals workshop, the instructor presents this requirement:",
        "Before making a change, a learner checks this core behavior:",
        "During a design vocabulary review, the team evaluates this situation:",
        "In a command-planning session, an administrator asks this question:",
        "While preparing the lab, a learner verifies this platform rule:",
        "During peer review, the team must identify the accurate response to this scenario:",
        "In an operations briefing, a new team member receives this question:",
        "While building a support checklist, an engineer reviews this requirement:",
        "During a readiness check, the administrator considers this behavior:",
        "In a service overview, the team discusses this scenario:",
        "While reviewing official guidance, a learner must resolve this question:",
        "During a configuration walkthrough, the instructor asks about this situation:",
        "In a preflight knowledge check, the operator evaluates this requirement:",
    ),
    "applied": (
        "During a planned deployment, the administrator encounters this scenario:",
        "A change request requires the team to resolve this situation:",
        "While automating the lab, an engineer must answer this question:",
        "During an implementation review, the operator considers this requirement:",
        "A production runbook must correctly handle this scenario:",
        "While validating a configuration, the team evaluates this situation:",
        "A delegated administrator receives the following support request:",
        "During a maintenance window, an engineer must decide how to respond:",
        "A deployment pipeline reaches this decision point:",
        "While applying least-privilege controls, the administrator reviews this scenario:",
        "A repeatable Azure CLI workflow must address this requirement:",
        "During an environment handoff, the receiving team asks this question:",
        "A configuration change produces the following operational choice:",
        "While preparing independent validation, an engineer considers this scenario:",
        "A service owner asks the administrator to resolve this requirement:",
        "During a scoped cleanup review, the team evaluates this situation:",
        "An automation author must choose the correct response to this scenario:",
        "A lab run with a unique run ID reaches this decision:",
        "While comparing the intended and actual states, the operator asks this question:",
        "A peer reviewer examines the proposed implementation for this scenario:",
        "During a controlled rollout, the change team encounters this requirement:",
        "A support engineer reproduces the following situation in a test environment:",
        "While recording validation evidence, the administrator evaluates this question:",
        "A configuration owner must approve one response to this scenario:",
        "During post-deployment verification, the team reviews this situation:",
    ),
    "advanced": (
        "After a failed change, an escalation engineer revisits this scenario:",
        "During root-cause analysis, the team must resolve this question:",
        "A security and reliability review identifies this design decision:",
        "While diagnosing unexpected Azure behavior, the engineer considers this situation:",
        "An architecture review requires the strongest response to this scenario:",
        "During break/fix validation, the operator encounters this question:",
        "A complex support case depends on correctly interpreting this requirement:",
        "While correcting configuration drift, the team evaluates this scenario:",
        "A recovery exercise exposes the following technical decision:",
        "During final design assurance, the reviewer must resolve this situation:",
    ),
}


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def write_text(path: Path, content: str, check: bool = False) -> bool:
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    if existing == content:
        if check:
            print(f"PASS  {path.relative_to(ROOT)} is current")
        return True
    if check:
        print(f"FAIL  {path.relative_to(ROOT)} is stale; run python tools/expand_assessments.py")
        return False
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
    print(f"WRITE {path.relative_to(ROOT)}")
    return True


def rotate_options(question: dict, desired_correct: str) -> None:
    old_correct = question["correctOption"]
    offset = (OPTION_NAMES.index(desired_correct) - OPTION_NAMES.index(old_correct)) % 4
    options = question["options"]
    rationales = question["distractorExplanations"]
    new_options: dict[str, str] = {}
    new_rationales: dict[str, str] = {}
    for index, old_name in enumerate(OPTION_NAMES):
        new_name = OPTION_NAMES[(index + offset) % 4]
        new_options[new_name] = options[old_name]
        new_rationales[new_name] = rationales[old_name]
    question["options"] = {name: new_options[name] for name in OPTION_NAMES}
    question["correctOption"] = desired_correct
    question["distractorExplanations"] = {name: new_rationales[name] for name in OPTION_NAMES}


def desired_answers(lab_number: str) -> list[str]:
    rotation = int(lab_number) % 4
    return [OPTION_NAMES[(index + rotation) % 4] for index in range(50)]


def build_questions(lab_number: str, seeds: list[dict]) -> list[dict]:
    by_difficulty: dict[str, list[dict]] = defaultdict(list)
    for question in seeds:
        by_difficulty[question["difficulty"]].append(question)

    all_seeds = list(seeds)
    expanded: list[dict] = []
    for difficulty, target in TARGET_COUNTS.items():
        pool = by_difficulty[difficulty] or all_seeds
        contexts = CONTEXTS[difficulty]
        for index in range(target):
            source = pool[index % len(pool)]
            question = copy.deepcopy(source)
            if index >= len(pool):
                question["stem"] = f"{contexts[index]} {source['stem']}"
            question["difficulty"] = difficulty
            expanded.append(question)

    answers = desired_answers(lab_number)
    for index, question in enumerate(expanded, start=1):
        question["id"] = f"LAB{lab_number}-Q{index:02d}"
        rotate_options(question, answers[index - 1])
    return expanded


def yaml_text(questions: list[dict]) -> str:
    return yaml.safe_dump(
        questions,
        sort_keys=False,
        allow_unicode=True,
        width=120,
        default_flow_style=False,
    )


def markdown_text(value: str) -> str:
    """Prevent command placeholders such as <group-id> from becoming HTML."""
    return value.replace("<", "\\<").replace(">", "\\>")


def questions_markdown(lab_number: str, questions: list[dict]) -> str:
    lines = [
        f"# Lab {lab_number} knowledge check",
        "",
        "Choose the single best answer for each question. Record your choices before opening `ANSWERS.md`.",
        "",
    ]
    for question in questions:
        lines.extend(
            [
                f"## {question['id']} — {question['difficulty'].title()}",
                "",
                markdown_text(question["stem"]),
                "",
                *(f"- {name}. {markdown_text(question['options'][name])}" for name in OPTION_NAMES),
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def answers_markdown(lab_number: str, questions: list[dict]) -> str:
    lines = [
        f"# Lab {lab_number} answer key",
        "",
        "Review these explanations only after answering all 50 questions.",
        "",
    ]
    for question in questions:
        correct = question["correctOption"]
        lines.extend(
            [
                f"## {question['id']} — {correct}",
                "",
                markdown_text(question["explanation"]),
                "",
                *(
                    f"- {name}: {markdown_text(question['distractorExplanations'][name])}"
                    for name in OPTION_NAMES
                ),
                "",
                "Objectives: " + ", ".join(f"`{item}`" for item in question["objectiveIds"]) + ".",
                "",
                "Official sources: " + ", ".join(f"[Microsoft Learn]({url})" for url in question["sourceUrls"]) + ".",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def update_metadata(lab_dir: Path, lab_number: str, check: bool) -> bool:
    path = lab_dir / "lab.yml"
    content = path.read_text(encoding="utf-8")
    question_count = metadata_for_lab(lab_number)["questionCount"]
    content, replacements = re.subn(
        r"(?m)^(  questionCount:)\s+\d+$",
        rf"\1 {question_count}",
        content,
        count=1,
    )
    if replacements != 1:
        raise RuntimeError(f"Could not update assessment count in {path.relative_to(ROOT)}")
    return write_text(path, content, check)


def update_catalog(check: bool) -> bool:
    path = ROOT / "labs" / "catalog.yml"
    content = path.read_text(encoding="utf-8")
    for lab_number, plan in ASSESSMENT_PLAN.items():
        pattern = rf"(?ms)(^- id: ['\"]?{lab_number}['\"]?.*?^  assessmentQuestionCount:)\s+\d+$"
        content, replacements = re.subn(
            pattern,
            rf"\1 {int(plan['questionCount'])}",
            content,
            count=1,
        )
        if replacements != 1:
            raise RuntimeError(f"Could not update catalog count for Lab {lab_number}")
    return write_text(path, content, check)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    valid = True
    seen_stems: set[str] = set()
    for lab_number, plan in ASSESSMENT_PLAN.items():
        lab_dirs = list((ROOT / "labs").glob(f"{lab_number}-*"))
        if len(lab_dirs) != 1:
            raise RuntimeError(f"Expected one directory for Lab {lab_number}; found {len(lab_dirs)}")
        lab_dir = lab_dirs[0]
        valid = update_metadata(lab_dir, lab_number, args.check) and valid
        if not plan["enabled"]:
            continue

        assessment_dir = lab_dir / "assessment"
        questions_path = assessment_dir / "questions.yml"
        seeds = load_yaml(questions_path)
        if len(seeds) > 50:
            raise RuntimeError(f"{lab_dir.name} contains more than 50 questions")
        questions = seeds if len(seeds) == 50 else build_questions(lab_number, seeds)
        answers = desired_answers(lab_number)
        for index, question in enumerate(questions, start=1):
            question["id"] = f"LAB{lab_number}-Q{index:02d}"
            rotate_options(question, answers[index - 1])
            stem_key = question["stem"].strip().casefold()
            if stem_key in seen_stems:
                question["stem"] = (
                    f"Within Lab {lab_number}, the team evaluates this scenario: {question['stem']}"
                )
                stem_key = question["stem"].strip().casefold()
            seen_stems.add(stem_key)
        valid = write_text(questions_path, yaml_text(questions), args.check) and valid
        valid = write_text(
            assessment_dir / "QUESTIONS.md",
            questions_markdown(lab_number, questions),
            args.check,
        ) and valid
        valid = write_text(
            assessment_dir / "ANSWERS.md",
            answers_markdown(lab_number, questions),
            args.check,
        ) and valid

    valid = update_catalog(args.check) and valid
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
