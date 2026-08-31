#!/usr/bin/env python3
"""Render assessment Markdown from complete, authored question banks.

The historical entrypoint name is retained for workflow compatibility. This tool
never expands, clones, rotates, or writes questions.yml. An incomplete or invalid
bank is rejected before any learner-facing document is rendered.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

from assessment_contract import ASSESSMENT_PLAN


ROOT = Path(__file__).resolve().parents[1]
LETTERS = ("A", "B", "C", "D")


def load_questions(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        questions = yaml.safe_load(handle)
    if not isinstance(questions, list) or len(questions) != 50:
        raise ValueError(f"{path.relative_to(ROOT)} must contain exactly 50 authored questions")
    return questions


def markdown_text(value: str) -> str:
    """Keep placeholders and comparison operators visible in Markdown."""
    return str(value).replace("<", "\\<").replace(">", "\\>")


def questions_markdown(lab_number: str, questions: list[dict]) -> str:
    lines = [
        f"# Lab {lab_number} knowledge check",
        "",
        "[Return to the guided lab](../README.md)",
        "",
        "Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.",
        "",
        "Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.",
        "",
    ]
    for question in questions:
        lines.extend(
            [
                f"## {question['id']} — {question['difficulty'].title()}",
                "",
                markdown_text(question["stem"]),
                "",
                *(f"- {letter}. {markdown_text(question['options'][letter])}" for letter in LETTERS),
                "",
            ]
        )
    lines.extend(["[Open the answer key](./ANSWERS.md)", ""])
    return "\n".join(lines)


def answers_markdown(lab_number: str, questions: list[dict]) -> str:
    lines = [
        f"# Lab {lab_number} answer key and remediation",
        "",
        "[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)",
        "",
        "Score one point per correct response:",
        "",
        "- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.",
        "- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.",
        "- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.",
        "",
    ]
    for question in questions:
        correct = question["correctOption"]
        lines.extend(
            [
                f"## {question['id']} — {correct}",
                "",
                f"**Question:** {markdown_text(question['stem'])}",
                "",
            ]
        )
        for letter in LETTERS:
            verdict = "Correct" if letter == correct else "Incorrect"
            lines.extend(
                [
                    f"- **{letter} — {verdict}.** {markdown_text(question['options'][letter])}",
                    f"  {markdown_text(question['optionExplanations'][letter])}",
                ]
            )
        lines.extend(
            [
                "",
                "**Objectives:** " + ", ".join(f"`{item}`" for item in question["objectiveIds"]),
                "",
                f"**Remediation:** [Repeat the mapped guided task](../README.md{question['remediationAnchor']}) "
                + "(" + ", ".join(f"`{item}`" for item in question["checkpointIds"]) + ").",
                "",
                "**Microsoft Learn sources:**",
                "",
                *(f"- [{source['title']}]({source['url']})" for source in question["sources"]),
                "",
                f"**Source reviewed:** {question['lastVerified']}",
                "",
            ]
        )
    return "\n".join(lines)


def write_or_check(path: Path, content: str, check: bool) -> bool:
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    if existing == content:
        print(f"PASS  {path.relative_to(ROOT)} is current")
        return True
    if check:
        print(f"FAIL  {path.relative_to(ROOT)} is stale; run python tools/expand_assessments.py")
        return False
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
    print(f"WRITE {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if rendered Markdown is stale")
    args = parser.parse_args()

    validator = ROOT / "tools" / "validate_assessments.py"
    validation = subprocess.run(
        [
            sys.executable,
            "-c",
            (
                "import runpy,sys;"
                f"sys.path.insert(0,{str(validator.parent)!r});"
                f"sys.argv=[{str(validator)!r}];"
                f"runpy.run_path({str(validator)!r},run_name='__main__')"
            ),
        ],
        cwd=ROOT,
        check=False,
    )
    if validation.returncode:
        print("Assessment rendering stopped because the authored bank failed validation.")
        return validation.returncode

    valid = True
    for number, plan in ASSESSMENT_PLAN.items():
        if not plan.get("enabled"):
            continue
        matches = sorted((ROOT / "labs").glob(f"{number}-*"))
        if len(matches) != 1:
            raise RuntimeError(f"Expected one directory for Lab {number}; found {len(matches)}")
        assessment_dir = matches[0] / "assessment"
        questions = load_questions(assessment_dir / "questions.yml")
        valid = write_or_check(
            assessment_dir / "QUESTIONS.md",
            questions_markdown(number, questions),
            args.check,
        ) and valid
        valid = write_or_check(
            assessment_dir / "ANSWERS.md",
            answers_markdown(number, questions),
            args.check,
        ) and valid
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
