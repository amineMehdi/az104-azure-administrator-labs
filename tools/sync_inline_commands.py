#!/usr/bin/env python3
"""Embed complete lifecycle command implementations in every lab README."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABS_ROOT = ROOT / "labs"
BEGIN = "<!-- BEGIN GENERATED INLINE COMMANDS -->"
END = "<!-- END GENERATED INLINE COMMANDS -->"
STAGES = ("preflight", "setup", "validate", "cleanup")


def _lifecycle_files(lab_dir: Path) -> list[Path]:
    scripts = lab_dir / "scripts"
    files: list[Path] = []
    if not scripts.exists():
        return files
    for lane in sorted(path for path in scripts.iterdir() if path.is_dir()):
        lane_files = [path for path in lane.iterdir() if path.is_file()]
        for stage in STAGES:
            match = next((path for path in lane_files if path.stem.lower() == stage), None)
            if match is None:
                raise ValueError(f"{lab_dir.name}: {lane.name} is missing its {stage} implementation")
            files.append(match)
    return files


def render_section(lab_dir: Path) -> str:
    lines = [
        BEGIN,
        "## Complete inline command implementation",
        "",
        (
            "The lifecycle commands below are the complete learner-facing implementation. "
            "They are embedded from the retained script files so the README and automation cannot drift. "
            "Review each stage here before running it. Use a different run ID if you later try the optional "
            "scripted lane against the same sandbox."
        ),
        "",
    ]
    for path in _lifecycle_files(lab_dir):
        relative = path.relative_to(lab_dir).as_posix()
        stage = path.stem.lower()
        if path.suffix.lower() != ".ps1":
            raise ValueError(f"{lab_dir.name}: lifecycle files must be PowerShell-hosted Azure CLI scripts")
        fence = "powershell"
        lines.extend(
            [
                f"### {stage.capitalize()}: `{relative}`",
                "",
                f"```{fence}",
                path.read_text(encoding="utf-8").rstrip(),
                "```",
                "",
            ]
        )
    lines.extend([END, ""])
    return "\n".join(lines)


def updated_readme(lab_dir: Path) -> str:
    readme_path = lab_dir / "README.md"
    text = readme_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    section = render_section(lab_dir).rstrip()
    if BEGIN in text and END in text:
        prefix, remainder = text.split(BEGIN, 1)
        _, suffix = remainder.split(END, 1)
        return f"{prefix.rstrip()}\n\n{section}\n{suffix.lstrip()}".rstrip() + "\n"

    insertion_markers = ("\n## Run the lab\n", "\n## Checkpoint 1", "\n## Before you begin\n")
    marker = next((candidate for candidate in insertion_markers if candidate in text), None)
    if marker is None:
        raise ValueError(f"{lab_dir.name}: no stable README insertion point found")
    before, after = text.split(marker, 1)
    return f"{before.rstrip()}\n\n{section}\n{marker.lstrip()}{after}".rstrip() + "\n"


def sync_lab(lab_dir: Path, check: bool) -> bool:
    readme_path = lab_dir / "README.md"
    expected = updated_readme(lab_dir)
    existing = readme_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if existing == expected:
        print(f"PASS  {readme_path.relative_to(ROOT)} inline commands are current")
        return True
    if check:
        print(f"FAIL  {readme_path.relative_to(ROOT)} inline commands are stale")
        return False
    with readme_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(expected)
    print(f"WRITE {readme_path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", nargs="*", help="Optional two-digit lab numbers")
    args = parser.parse_args()
    selected = set(args.only or [])
    labs = sorted(path for path in LABS_ROOT.glob("[0-9][0-9]-*") if path.is_dir())
    if selected:
        labs = [path for path in labs if path.name[:2] in selected]
    results = [sync_lab(lab, args.check) for lab in labs]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
