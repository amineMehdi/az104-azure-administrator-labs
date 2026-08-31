#!/usr/bin/env python3
"""Validate the authored AZ-104 assessment bank without using Azure.

This validator deliberately treats questions.yml as authored curriculum. It never
creates, clones, pads, rotates, or otherwise repairs question records.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlparse

import yaml

from assessment_contract import ASSESSMENT_PLAN, DOMAIN_OBJECTIVE_PREFIXES
from assessment_sources import expected_source, validate_source_contract


ROOT = Path(__file__).resolve().parents[1]
LETTERS = ("A", "B", "C", "D")
EXPECTED_MIX = Counter({"foundational": 15, "applied": 25, "advanced": 10})
PROHIBITED_SOURCE_TERMS = ("powershell", "azure-portal", "-portal", "/portal")
OLD_GENERIC_RATIONALES = (
    "correct. this option aligns with the documented azure behavior",
    "this option changes a related setting but does not satisfy the requirement",
    "this option is broader than necessary and does not provide the requested outcome",
    "this option does not configure or validate the requested capability",
)
PROHIBITED_RATIONALE_FRAGMENTS = (
    "real but separate behavior",
    "documented service behavior",
    "leaving the required",
    "queried state directly exposes",
    "condition directly breaks",
    "pair implements and checks",
    "first step establishes",
    "alternatives change unrelated configuration",
    "providing evidence independent of setup exit status",
)
WORD_RE = re.compile(r"[a-z0-9]+")
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "azure", "be", "best", "by", "configure",
    "correctly", "does", "for", "from", "in", "is", "it", "must", "of", "on", "or",
    "should", "that", "the", "this", "to", "using", "which", "with", "you",
}
SCAFFOLD_WORDS = {
    "action", "answer", "behavior", "boundary", "capability", "change", "check",
    "claim", "complete", "condition", "configuration", "correct", "decisive",
    "criteria", "description", "directly", "evidence", "exact", "explain", "explains", "finding",
    "implementation", "independent", "option", "pair", "proof", "question",
    "record", "requirement", "required", "result", "review", "scenario", "separate",
    "sequence", "statement", "state", "step", "technical", "unrelated", "validation", "which",
}


class Findings:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.passes: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def ok(self, message: str) -> None:
        self.passes.append(message)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def normalized(value: str) -> str:
    return " ".join(WORD_RE.findall(str(value).casefold()))


def content_words(value: str) -> set[str]:
    return {word for word in WORD_RE.findall(value.casefold()) if word not in STOPWORDS and len(word) > 2}


def ngrams(value: str, size: int) -> list[tuple[str, ...]]:
    words = normalized(value).split()
    return [tuple(words[index : index + size]) for index in range(max(0, len(words) - size + 1))]


def collapsed_stem_skeleton(stem: str, options: dict) -> str:
    """Remove question-local technical vocabulary to expose a reused prose mold."""
    technical_words = {
        word
        for option in options.values()
        for word in content_words(str(option))
    }
    skeleton: list[str] = []
    for word in normalized(stem).split():
        token = "<technical>" if word in technical_words else word
        if not skeleton or token != skeleton[-1] or token != "<technical>":
            skeleton.append(token)
    return " ".join(skeleton)


def check_cross_bank_scaffolding(
    stem_records: list[tuple[str, str, str, dict]],
    rationale_records: list[tuple[str, str, str]],
    findings: Findings,
) -> None:
    """Reject cross-lab templates while tolerating repeated Azure terminology."""
    prefixes: dict[tuple[str, ...], list[tuple[str, str]]] = defaultdict(list)
    skeletons: dict[str, list[tuple[str, str]]] = defaultdict(list)
    stem_grams: dict[tuple[str, ...], list[tuple[str, str]]] = defaultdict(list)
    for lab_name, question_id, stem, options in stem_records:
        words = normalized(stem).split()
        if len(words) >= 6:
            prefixes[tuple(words[:6])].append((lab_name, question_id))
        skeleton = collapsed_stem_skeleton(stem, options)
        if len(skeleton.split()) >= 8:
            skeletons[skeleton].append((lab_name, question_id))
        for gram in ngrams(stem, 7):
            stem_grams[gram].append((lab_name, question_id))

    repeated_prefixes = [
        (key, locations)
        for key, locations in prefixes.items()
        if len({lab for lab, _ in locations}) > 1
    ]
    for key, locations in sorted(repeated_prefixes, key=lambda item: (-len(item[1]), item[0]))[:10]:
        sample = ", ".join(question_id for _, question_id in locations[:4])
        findings.error(
            f"assessment bank: repeated cross-lab six-word lead-in "
            f"'{ ' '.join(key) }' in {sample}"
        )
    if len(repeated_prefixes) > 10:
        findings.error(
            f"assessment bank: {len(repeated_prefixes) - 10} additional repeated cross-lab lead-ins"
        )

    repeated_skeletons = [
        (key, locations)
        for key, locations in skeletons.items()
        if len({lab for lab, _ in locations}) > 1
    ]
    for _, locations in sorted(repeated_skeletons, key=lambda item: -len(item[1]))[:10]:
        sample = ", ".join(question_id for _, question_id in locations[:4])
        findings.error(f"assessment bank: cross-lab stem skeleton is reused by {sample}")
    if len(repeated_skeletons) > 10:
        findings.error(
            f"assessment bank: {len(repeated_skeletons) - 10} additional repeated stem skeletons"
        )

    generic_stem_grams = [
        (gram, locations)
        for gram, locations in stem_grams.items()
        if len(locations) >= 10
        and len({lab for lab, _ in locations}) >= 5
        and len(set(gram) & SCAFFOLD_WORDS) >= 2
    ]
    for gram, locations in sorted(generic_stem_grams, key=lambda item: -len(item[1]))[:10]:
        findings.error(
            f"assessment bank: generic seven-word stem scaffold '{' '.join(gram)}' "
            f"is reused {len(locations)} times"
        )
    if len(generic_stem_grams) > 10:
        findings.error(
            f"assessment bank: {len(generic_stem_grams) - 10} additional repeated stem scaffolds"
        )

    rationale_grams: dict[tuple[str, ...], list[tuple[str, str]]] = defaultdict(list)
    rationale_four_grams: dict[tuple[str, ...], list[tuple[str, str]]] = defaultdict(list)
    for lab_name, rationale_id, rationale in rationale_records:
        normalized_rationale = normalized(rationale)
        for fragment in PROHIBITED_RATIONALE_FRAGMENTS:
            if normalized(fragment) in normalized_rationale:
                findings.error(f"{rationale_id}: uses canned rationale fragment '{fragment}'")
        for gram in ngrams(rationale, 7):
            rationale_grams[gram].append((lab_name, rationale_id))
        for gram in ngrams(rationale, 4):
            rationale_four_grams[gram].append((lab_name, rationale_id))

    generic_rationale_grams = [
        (gram, locations)
        for gram, locations in rationale_grams.items()
        if len(locations) >= 12
        and len({lab for lab, _ in locations}) >= 3
        and len(set(gram) & SCAFFOLD_WORDS) >= 2
    ]
    for gram, locations in sorted(generic_rationale_grams, key=lambda item: -len(item[1]))[:10]:
        findings.error(
            f"assessment bank: generic seven-word rationale scaffold '{' '.join(gram)}' "
            f"is reused {len(locations)} times"
        )
    if len(generic_rationale_grams) > 10:
        findings.error(
            f"assessment bank: {len(generic_rationale_grams) - 10} additional repeated rationale scaffolds"
        )

    high_frequency_short_scaffolds = [
        (gram, locations)
        for gram, locations in rationale_four_grams.items()
        if len(locations) >= 100
        and len({lab for lab, _ in locations}) >= 5
        and bool(set(gram) & SCAFFOLD_WORDS)
    ]
    for gram, locations in sorted(
        high_frequency_short_scaffolds, key=lambda item: -len(item[1])
    )[:10]:
        findings.error(
            f"assessment bank: high-frequency four-word rationale scaffold "
            f"'{' '.join(gram)}' is reused {len(locations)} times"
        )
    if len(high_frequency_short_scaffolds) > 10:
        findings.error(
            f"assessment bank: {len(high_frequency_short_scaffolds) - 10} additional "
            "high-frequency short rationale scaffolds"
        )

    if not repeated_prefixes and not repeated_skeletons and not generic_stem_grams:
        findings.ok("Assessment stems contain no repeated cross-lab lead-ins or generic scaffolds")
    if not generic_rationale_grams and not high_frequency_short_scaffolds and not any(
        normalized(fragment) in normalized(rationale)
        for _, _, rationale in rationale_records
        for fragment in PROHIBITED_RATIONALE_FRAGMENTS
    ):
        findings.ok("Assessment rationales contain no prohibited or high-frequency generic scaffolds")


def objective_catalog() -> tuple[dict[str, str], dict[str, set[str]]]:
    blueprint = load_yaml(ROOT / "curriculum" / "blueprint.yml")
    titles: dict[str, str] = {}
    labs: dict[str, set[str]] = defaultdict(set)
    for domain in blueprint.get("domains", []):
        for group in domain.get("groups", []):
            for objective in group.get("objectives", []):
                objective_id = objective["id"]
                titles[objective_id] = objective["title"]
                labs[objective_id].update(objective.get("labs", []))
    return titles, labs


def schema_errors(data, schema: dict) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return []
    validator = jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )
    return [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path))
    ]


def has_short_period(sequence: list[str], maximum: int = 12) -> int | None:
    for period in range(1, min(maximum, len(sequence) // 2) + 1):
        if all(value == sequence[index % period] for index, value in enumerate(sequence)):
            return period
    return None


def max_run(sequence: list[str]) -> int:
    longest = current = 0
    previous = None
    for value in sequence:
        current = current + 1 if value == previous else 1
        longest = max(longest, current)
        previous = value
    return longest


def check_near_duplicates(lab_name: str, questions: list[dict], findings: Findings) -> None:
    for left_index, left in enumerate(questions):
        left_stem = normalized(left.get("stem", ""))
        left_words = content_words(left_stem)
        for right in questions[left_index + 1 :]:
            right_stem = normalized(right.get("stem", ""))
            right_words = content_words(right_stem)
            if not left_words or not right_words:
                continue
            overlap = len(left_words & right_words) / len(left_words | right_words)
            if overlap < 0.72:
                continue
            similarity = SequenceMatcher(None, left_stem, right_stem, autojunk=False).ratio()
            if overlap >= 0.82 and similarity >= 0.88:
                findings.error(
                    f"{lab_name}: near-duplicate stems {left.get('id')} and {right.get('id')} "
                    f"(word overlap {overlap:.2f}, similarity {similarity:.2f})"
                )


def validate_question(
    question: dict,
    lab_number: str,
    lab_name: str,
    allowed_objectives: set[str],
    findings: Findings,
) -> None:
    if not isinstance(question, dict):
        findings.error(f"{lab_name}: every question record must be an object")
        return
    question_id = question.get("id", "<missing-id>")
    stem = str(question.get("stem", ""))
    if re.search(r"\bA\s+[aeio][A-Za-z-]*", stem, flags=re.IGNORECASE):
        findings.error(
            f"{question_id}: stem contains an indefinite-article error ('A' before a vowel sound)"
        )
    objectives = question.get("objectiveIds", [])
    if not objectives or not set(objectives) <= allowed_objectives:
        findings.error(
            f"{question_id}: objectives {objectives} are not assessment objectives for {lab_name}"
        )

    expected_checkpoints = {
        f"LAB{lab_number}-CP0{index}" for index in range(1, 6)
    }
    checkpoints = question.get("checkpointIds", [])
    if not checkpoints or not set(checkpoints) <= expected_checkpoints:
        findings.error(f"{question_id}: checkpoint IDs must belong to Lab {lab_number}")
    anchor = question.get("remediationAnchor", "")
    if not re.fullmatch(r"#task-[1-5]", anchor):
        findings.error(f"{question_id}: remediationAnchor must be #task-1 through #task-5")
    elif checkpoints and anchor[-1] not in {item[-1] for item in checkpoints}:
        findings.error(f"{question_id}: remediation anchor and checkpoint ID disagree")

    options = question.get("options", {})
    if not isinstance(options, dict):
        findings.error(f"{question_id}: options must be an A–D mapping")
        options = {}
    option_values = [normalized(options.get(letter, "")) for letter in LETTERS]
    if len(option_values) != len(set(option_values)):
        findings.error(f"{question_id}: all four option texts must be distinct")

    correct = question.get("correctOption")
    explanations = question.get("optionExplanations", {})
    if not isinstance(explanations, dict):
        findings.error(f"{question_id}: optionExplanations must be an A–D mapping")
        explanations = {}
    if correct not in LETTERS:
        findings.error(f"{question_id}: correctOption must be A, B, C, or D")
    for letter in LETTERS:
        rationale = explanations.get(letter, "")
        rationale_key = normalized(rationale)
        if len(rationale) < 30:
            findings.error(f"{question_id}: option {letter} needs a complete explanation")
        if any(generic in rationale_key for generic in OLD_GENERIC_RATIONALES):
            findings.error(f"{question_id}: option {letter} uses a prohibited generic rationale")
        option_terms = content_words(options.get(letter, ""))
        stem_terms = content_words(question.get("stem", ""))
        rationale_terms = content_words(rationale)
        if (option_terms or stem_terms) and not (option_terms | stem_terms).intersection(rationale_terms):
            findings.error(
                f"{question_id}: option {letter} explanation does not discuss the option or scenario"
            )

    # Reject stems that reproduce a distinctive phrase found only in the correct
    # option. Shared service terminology is tolerated because the phrase must be
    # unique among all four choices and contain at least two content words.
    if correct in LETTERS:
        stem_grams = set(ngrams(question.get("stem", ""), 3))
        correct_grams = set(ngrams(options.get(correct, ""), 3))
        distractor_grams = {
            gram
            for letter in LETTERS
            if letter != correct
            for gram in ngrams(options.get(letter, ""), 3)
        }
        giveaways = [
            gram
            for gram in stem_grams & (correct_grams - distractor_grams)
            if len(content_words(" ".join(gram))) == 3
        ]
        if giveaways:
            findings.error(
                f"{question_id}: stem repeats a correct-option-only phrase "
                f"'{' '.join(sorted(giveaways)[0])}'"
            )

    sources = question.get("sources", [])
    if not isinstance(sources, list):
        findings.error(f"{question_id}: sources must be a list")
        sources = []
    if not sources:
        findings.error(f"{question_id}: at least one Microsoft Learn source is required")
    for source in sources:
        if not isinstance(source, dict):
            findings.error(f"{question_id}: each source must contain a title and URL")
            continue
        title = str(source.get("title", "")).strip()
        url = str(source.get("url", "")).strip()
        parsed = urlparse(url)
        if title.casefold() in {"microsoft learn", "learn", "official source"} or len(title) < 12:
            findings.error(f"{question_id}: source title must describe the referenced article")
        if parsed.scheme != "https" or parsed.netloc != "learn.microsoft.com":
            findings.error(f"{question_id}: source must use https://learn.microsoft.com/")
        lowered = url.casefold()
        if any(term in lowered for term in PROHIBITED_SOURCE_TERMS):
            findings.error(f"{question_id}: Portal/PowerShell procedural source is not allowed: {url}")

    match = re.fullmatch(rf"LAB{lab_number}-Q([0-9]{{2}})", str(question_id))
    if match:
        direct_source = expected_source(lab_number, int(match.group(1)))
        matching_sources = [
            source
            for source in sources
            if isinstance(source, dict) and source.get("url") == direct_source["url"]
        ]
        if not matching_sources:
            findings.error(
                f"{question_id}: source does not directly match its concept; expected "
                f"{direct_source['url']}"
            )
        elif all(source.get("title") != direct_source["title"] for source in matching_sources):
            findings.error(
                f"{question_id}: direct source title must be '{direct_source['title']}'"
            )

    try:
        reviewed = date.fromisoformat(str(question.get("lastVerified", "")))
        if reviewed > date.today():
            findings.error(f"{question_id}: lastVerified cannot be in the future")
    except ValueError:
        findings.error(f"{question_id}: lastVerified must be an ISO date")


def validate_lab(
    lab_dir: Path,
    schema: dict,
    objective_titles: dict[str, str],
    objective_labs: dict[str, set[str]],
    findings: Findings,
) -> list[dict]:
    number = lab_dir.name[:2]
    path = lab_dir / "assessment" / "questions.yml"
    if not path.exists():
        findings.error(f"{lab_dir.name}: missing assessment/questions.yml")
        return []
    questions = load_yaml(path)
    if not isinstance(questions, list):
        findings.error(f"{lab_dir.name}: questions.yml must contain a list")
        return []

    for message in schema_errors(questions, schema):
        findings.error(f"{lab_dir.name}: schema {message}")
    if len(questions) != 50:
        findings.error(f"{lab_dir.name}: expected 50 authored questions; found {len(questions)}")
        return questions

    expected_ids = [f"LAB{number}-Q{index:02d}" for index in range(1, 51)]
    ids = [question.get("id") if isinstance(question, dict) else None for question in questions]
    if ids != expected_ids:
        findings.error(f"{lab_dir.name}: IDs must be contiguous from Q01 through Q50")

    mix = Counter(
        question.get("difficulty") if isinstance(question, dict) else None
        for question in questions
    )
    if mix != EXPECTED_MIX:
        findings.error(f"{lab_dir.name}: difficulty mix is {dict(mix)}, expected 15/25/10")

    answers = [
        question.get("correctOption") if isinstance(question, dict) else None
        for question in questions
    ]
    answer_counts = Counter(answers)
    if set(answer_counts) != set(LETTERS) or any(value not in {12, 13} for value in answer_counts.values()):
        findings.error(f"{lab_dir.name}: answer positions are not balanced 12–13 times each")
    period = has_short_period(answers)
    if period:
        findings.error(f"{lab_dir.name}: answer key repeats a predictable period-{period} pattern")
    if max_run(answers) > 3:
        findings.error(f"{lab_dir.name}: answer key contains a run longer than three identical positions")

    metadata = load_yaml(lab_dir / "lab.yml")
    domain = (metadata.get("assessment") or {}).get("primaryDomain", "")
    prefix = DOMAIN_OBJECTIVE_PREFIXES.get(domain, "")
    allowed = {
        objective_id
        for objective_id, mapped_labs in objective_labs.items()
        if lab_dir.name in mapped_labs and objective_id.startswith(prefix)
    }
    for question in questions:
        validate_question(question, number, lab_dir.name, allowed, findings)

    covered = {
        item
        for question in questions
        if isinstance(question, dict)
        for item in question.get("objectiveIds", [])
    }
    missing = allowed - covered
    if missing:
        findings.error(f"{lab_dir.name}: missing mapped objectives {', '.join(sorted(missing))}")

    stems = [
        normalized(question.get("stem", "")) if isinstance(question, dict) else ""
        for question in questions
    ]
    if len(stems) != len(set(stems)):
        findings.error(f"{lab_dir.name}: contains exact duplicate stems")
    findings.ok(f"{lab_dir.name}: checked 50 questions against its objective blueprint")
    return questions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report-json",
        type=Path,
        help="Optionally write the offline validation summary as JSON.",
    )
    args = parser.parse_args()

    findings = Findings()
    for message in validate_source_contract():
        findings.error(f"assessment source contract: {message}")
    schema = json.loads((ROOT / "curriculum" / "question-schema.json").read_text(encoding="utf-8"))
    objective_titles, objective_labs = objective_catalog()
    all_questions: list[dict] = []
    question_locations: dict[str, str] = {}
    option_sets: dict[tuple[str, ...], str] = {}
    rationales: dict[str, str] = {}
    stem_records: list[tuple[str, str, str, dict]] = []
    rationale_records: list[tuple[str, str, str]] = []

    for number, plan in ASSESSMENT_PLAN.items():
        if not plan.get("enabled"):
            continue
        matches = sorted((ROOT / "labs").glob(f"{number}-*"))
        if len(matches) != 1:
            findings.error(f"Lab {number}: expected one lab directory; found {len(matches)}")
            continue
        questions = validate_lab(matches[0], schema, objective_titles, objective_labs, findings)
        for question in questions:
            if not isinstance(question, dict):
                continue
            question_id = question.get("id", "<missing-id>")
            stem_key = normalized(question.get("stem", ""))
            if stem_key in question_locations:
                findings.error(
                    f"{question_id}: exact stem duplicates {question_locations[stem_key]}"
                )
            question_locations[stem_key] = question_id

            options = question.get("options", {})
            stem_records.append(
                (matches[0].name, question_id, question.get("stem", ""), options)
            )
            option_key = tuple(sorted(normalized(options.get(letter, "")) for letter in LETTERS))
            if option_key in option_sets:
                findings.error(
                    f"{question_id}: reuses the complete option set from {option_sets[option_key]}"
                )
            option_sets[option_key] = question_id

            for letter, rationale in question.get("optionExplanations", {}).items():
                rationale_records.append(
                    (matches[0].name, f"{question_id}/{letter}", rationale)
                )
                rationale_key = normalized(rationale)
                if rationale_key in rationales:
                    findings.error(
                        f"{question_id}/{letter}: rationale duplicates {rationales[rationale_key]}"
                    )
                rationales[rationale_key] = f"{question_id}/{letter}"
        all_questions.extend(questions)

    check_near_duplicates(
        "assessment bank",
        [question for question in all_questions if isinstance(question, dict)],
        findings,
    )
    check_cross_bank_scaffolding(stem_records, rationale_records, findings)

    if len(all_questions) != 1250:
        findings.error(f"Assessment bank must contain 1,250 questions; found {len(all_questions)}")
    else:
        findings.ok("Assessment bank contains exactly 1,250 authored questions")

    covered = {item for question in all_questions for item in question.get("objectiveIds", [])}
    missing = set(objective_titles) - covered
    if missing:
        findings.error(f"Official objective coverage is incomplete: {', '.join(sorted(missing))}")
    else:
        findings.ok("All 82 official objectives have assessment coverage")

    report = {
        "questionCount": len(all_questions),
        "objectiveCount": len(covered & set(objective_titles)),
        "passes": findings.passes,
        "errors": findings.errors,
    }
    if args.report_json:
        args.report_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    for message in findings.passes:
        print(f"PASS  {message}")
    for message in findings.errors:
        print(f"FAIL  {message}")
    print(f"\nAssessment summary: {len(findings.passes)} passed, {len(findings.errors)} failed")
    return 1 if findings.errors else 0


if __name__ == "__main__":
    sys.exit(main())
