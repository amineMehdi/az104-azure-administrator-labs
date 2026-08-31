#!/usr/bin/env python3
"""Stage authoritative repository content for the Material for MkDocs site."""

# cspell:ignore labelledby

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / ".site-docs"
SITE_SOURCE = REPO_ROOT / "docs" / "site"
SITE_ASSETS = REPO_ROOT / "docs" / "site-assets"
CATALOG_PATH = REPO_ROOT / "labs" / "catalog.yml"

DOMAIN_LABELS = {
    "foundation": "Foundation",
    "identity-governance": "Identity and governance",
    "storage": "Storage",
    "compute": "Compute",
    "networking": "Networking",
    "monitor-recovery": "Monitoring and recovery",
    "capstone": "Capstones",
}

ALLOWED_LAB_SUFFIXES = {
    ".bicep",
    ".json",
    ".kql",
    ".md",
    ".mmd",
    ".ps1",
    ".svg",
    ".yaml",
    ".yml",
}


class SiteBuildError(RuntimeError):
    """Raised when authoritative site inputs violate the staging contract."""


class AccessibilityParser(HTMLParser):
    """Collect a small set of deterministic accessibility signals from HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.has_language = False
        self.has_viewport = False
        self.main_count = 0
        self.h1_count = 0
        self.images_without_alt = 0
        self.external_active_resources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html" and attributes.get("lang"):
            self.has_language = True
        elif tag == "meta" and attributes.get("name", "").lower() == "viewport":
            self.has_viewport = True
        elif tag == "main":
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "img" and "alt" not in attributes:
            self.images_without_alt += 1
        active_resource = None
        if tag in {"img", "script", "source"}:
            active_resource = attributes.get("src")
        elif tag == "link" and attributes.get("rel"):
            relationships = set(attributes["rel"].casefold().split())
            if relationships & {"icon", "manifest", "modulepreload", "preload", "stylesheet"}:
                active_resource = attributes.get("href")
        if active_resource and re.match(r"^https?://", active_resource, re.IGNORECASE):
            self.external_active_resources.append(active_resource)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise SiteBuildError(f"Cannot read {path.relative_to(REPO_ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise SiteBuildError(f"Expected a mapping in {path.relative_to(REPO_ROOT)}")
    return value


def normalized_lab_id(value: Any) -> str:
    text = str(value)
    if not re.fullmatch(r"\d{1,2}", text):
        raise SiteBuildError(f"Invalid catalog lab ID: {value!r}")
    number = int(text)
    if not 0 <= number <= 27:
        raise SiteBuildError(f"Catalog lab ID is outside 00-27: {value!r}")
    return f"{number:02d}"


def load_labs() -> list[dict[str, Any]]:
    catalog = load_yaml(CATALOG_PATH)
    entries = catalog.get("labs")
    if not isinstance(entries, list) or len(entries) != 28:
        raise SiteBuildError("labs/catalog.yml must declare exactly 28 labs")

    labs: list[dict[str, Any]] = []
    seen: set[str] = set()
    for raw in entries:
        if not isinstance(raw, dict):
            raise SiteBuildError("Every catalog lab entry must be a mapping")
        lab_id = normalized_lab_id(raw.get("id"))
        if lab_id in seen:
            raise SiteBuildError(f"Duplicate catalog lab ID: {lab_id}")
        seen.add(lab_id)
        slug = raw.get("slug")
        domain = raw.get("domain")
        if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9-]+", slug):
            raise SiteBuildError(f"LAB-{lab_id} has an invalid slug")
        if domain not in DOMAIN_LABELS:
            raise SiteBuildError(f"LAB-{lab_id} has an unsupported domain: {domain!r}")
        estimated_minutes = raw.get("estimatedMinutes")
        if (
            not isinstance(estimated_minutes, int)
            or isinstance(estimated_minutes, bool)
            or estimated_minutes <= 0
        ):
            raise SiteBuildError(f"LAB-{lab_id} has an invalid estimatedMinutes value")
        question_count = raw.get("questionCount")
        expected_question_count = 0 if lab_id in {"00", "26", "27"} else 50
        if question_count != expected_question_count:
            raise SiteBuildError(
                f"LAB-{lab_id} must declare questionCount {expected_question_count}"
            )
        folder = REPO_ROOT / "labs" / f"{lab_id}-{slug}"
        metadata_path = folder / "lab.yml"
        readme_path = folder / "README.md"
        if not folder.is_dir() or not metadata_path.is_file() or not readme_path.is_file():
            raise SiteBuildError(f"LAB-{lab_id} is missing its folder, lab.yml, or README.md")
        metadata = load_yaml(metadata_path)
        title = metadata.get("title")
        if not isinstance(title, str) or not title.strip():
            raise SiteBuildError(f"LAB-{lab_id} has no title in lab.yml")
        labs.append(
            {
                **raw,
                "id": lab_id,
                "labId": f"LAB-{lab_id}",
                "folder": folder,
                "folderName": folder.name,
                "title": title.strip(),
            }
        )

    expected = {f"{number:02d}" for number in range(28)}
    if seen != expected:
        missing = ", ".join(sorted(expected - seen))
        raise SiteBuildError(f"Catalog IDs must be contiguous from 00 through 27; missing: {missing}")
    return sorted(labs, key=lambda item: item["id"])


def copy_file(source: Path, destination: Path) -> None:
    if source.is_symlink():
        raise SiteBuildError(
            f"Refusing to stage symbolic link: {source.relative_to(REPO_ROOT)}"
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_site_sources(output: Path) -> None:
    required_pages = {
        "index.md": "index.md",
        "learning-pathways.md": "learning-pathways.md",
        "environment-readiness.md": "environment-readiness.md",
        "learner-progress.md": "learner-progress.md",
        "glossary.md": "glossary.md",
    }
    for source_name, destination_name in required_pages.items():
        source = SITE_SOURCE / source_name
        if not source.is_file():
            raise SiteBuildError(f"Missing site source: {source.relative_to(REPO_ROOT)}")
        content = source.read_text(encoding="utf-8")
        link_rewrites = {
            "../../labs/": "labs/",
            "../objective-map.md": "docs/objective-map.md",
            "../study-plan.md": "docs/study-plan.md",
            "../../learner.config.example.yml": "downloads/learner.config.example.yml",
            "../../curriculum/progress-schema.json": "contracts/progress-schema.json",
        }
        for source_link, staged_link in link_rewrites.items():
            content = content.replace(source_link, staged_link)
        destination = output / destination_name
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)

    if not SITE_ASSETS.is_dir():
        raise SiteBuildError("docs/site-assets is missing")
    shutil.copytree(SITE_ASSETS, output / "assets", dirs_exist_ok=True)


def copy_repository_docs(output: Path) -> None:
    docs_root = REPO_ROOT / "docs"
    for source in sorted(docs_root.rglob("*")):
        if not source.is_file():
            continue
        relative = source.relative_to(docs_root)
        # Branding/raster source assets are not staged. The learning site uses
        # only each lab's reproducible architecture.svg instructional visual.
        if relative.parts[0] in {"site", "site-assets", "visuals"}:
            continue
        copy_file(source, output / "docs" / relative)

    curriculum_root = REPO_ROOT / "curriculum"
    for source in sorted(curriculum_root.iterdir()):
        if source.is_file() and source.suffix.lower() in {".json", ".yml", ".yaml"}:
            copy_file(source, output / "contracts" / source.name)
    copy_file(
        REPO_ROOT / "learner.config.example.yml",
        output / "downloads" / "learner.config.example.yml",
    )


def navigation_line(labs: list[dict[str, Any]], index: int) -> str:
    parts: list[str] = []
    if index > 0:
        previous = labs[index - 1]
        parts.append(f"[← {previous['labId']}](../{previous['folderName']}/README.md)")
    parts.append("[Lab catalog](../README.md)")
    if index + 1 < len(labs):
        following = labs[index + 1]
        parts.append(f"[{following['labId']} →](../{following['folderName']}/README.md)")
    return " · ".join(parts)


def add_staged_navigation(markdown: str, navigation: str) -> str:
    lines = markdown.splitlines()
    heading_index = next((index for index, line in enumerate(lines) if line.startswith("# ")), None)
    if heading_index is None:
        raise SiteBuildError("Every staged lab README must contain one H1 heading")
    if re.search(r"\[(?:Lab )?Catalog\]\(", markdown, re.IGNORECASE):
        return markdown if markdown.endswith("\n") else f"{markdown}\n"
    body = [*lines[: heading_index + 1], "", navigation, "", *lines[heading_index + 1 :]]
    while len(body) > 1 and body[-1] == "":
        body.pop()
    body.extend(["", "---", "", navigation, ""])
    return "\n".join(body)


def validate_svg(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    required = ("role=\"img\"", "<title", "<desc", "aria-labelledby=")
    missing = [token for token in required if token not in content]
    if missing:
        relative = path.relative_to(REPO_ROOT)
        raise SiteBuildError(f"{relative} is missing accessible SVG markup: {', '.join(missing)}")


def copy_labs(output: Path, labs: list[dict[str, Any]]) -> None:
    copy_file(REPO_ROOT / "labs" / "README.md", output / "labs" / "README.md")
    copy_file(CATALOG_PATH, output / "labs" / "catalog.yml")
    for index, lab in enumerate(labs):
        source_root: Path = lab["folder"]
        destination_root = output / "labs" / lab["folderName"]
        for source in sorted(source_root.rglob("*")):
            if not source.is_file() or source.suffix.lower() not in ALLOWED_LAB_SUFFIXES:
                continue
            relative = source.relative_to(source_root)
            destination = destination_root / relative
            if relative == Path("README.md"):
                content = source.read_text(encoding="utf-8")
                staged = add_staged_navigation(content, navigation_line(labs, index))
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("w", encoding="utf-8", newline="\n") as handle:
                    handle.write(staged)
            elif relative.as_posix() == "assessment/ANSWERS.md":
                content = source.read_text(encoding="utf-8")
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("w", encoding="utf-8", newline="\n") as handle:
                    handle.write("---\nsearch:\n  exclude: true\n---\n\n" + content)
            else:
                copy_file(source, destination)
            if source.name == "architecture.svg":
                validate_svg(source)


def domain_page(domain: str, labs: list[dict[str, Any]]) -> str:
    label = DOMAIN_LABELS[domain]
    lab_ids = ",".join(lab["labId"] for lab in labs)
    lines = [
        f"# {label}",
        "",
        f"This generated dashboard lists the authoritative {label.lower()} labs in catalog order.",
        "",
        f'<div class="az104-progress-card" data-az104-domain-labs="{lab_ids}"></div>',
        "",
        "| Lab | Guided time | Questions |",
        "|---|---:|---:|",
    ]
    for lab in labs:
        minutes = int(lab.get("estimatedMinutes", 0))
        count = int(lab["questionCount"])
        lines.append(
            f"| [{lab['labId']}: {lab['title']}](../labs/{lab['folderName']}/README.md) | "
            f"{minutes} minutes | {count} |"
        )
    lines.extend(
        [
            "",
            "Completion requires successful deployment validation and post-cleanup validation.",
            "Assessment scores are learning signals rather than claims about the certification exam.",
            "",
        ]
    )
    return "\n".join(lines)


def write_domain_pages(output: Path, labs: list[dict[str, Any]]) -> None:
    grouped: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for lab in labs:
        grouped[lab["domain"]].append(lab)
    domain_root = output / "domains"
    domain_root.mkdir(parents=True, exist_ok=True)
    for domain in DOMAIN_LABELS:
        path = domain_root / f"{domain}.md"
        with path.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(domain_page(domain, grouped[domain]))


def write_manifest(output: Path) -> None:
    files: list[dict[str, Any]] = []
    for path in sorted(output.rglob("*")):
        if not path.is_file() or path.name == ".stage-manifest.json":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        files.append({"path": path.relative_to(output).as_posix(), "sha256": digest})
    manifest = {
        "schemaVersion": "1.0.0",
        "generatedFrom": "authoritative repository sources",
        "fileCount": len(files),
        "files": files,
    }
    with (output / ".stage-manifest.json").open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(manifest, indent=2) + "\n")


def populate_staging_tree(output: Path, labs: list[dict[str, Any]]) -> None:
    """Create one complete site source tree from authoritative inputs."""

    copy_site_sources(output)
    copy_repository_docs(output)
    copy_labs(output, labs)
    write_domain_pages(output, labs)
    write_manifest(output)


def stage(output: Path) -> None:
    labs = load_labs()
    output = output.resolve()
    repository = REPO_ROOT.resolve()
    if (
        output.parent != repository
        or not re.fullmatch(r"\.site-docs(?:-[a-z0-9][a-z0-9-]*)?", output.name)
    ):
        raise SiteBuildError(
            "The site staging directory must be the repository's .site-docs "
            "directory or a direct .site-docs-<name> sibling"
        )

    temporary = output.with_name(f"{output.name}.tmp")
    for target in (temporary,):
        if target.exists():
            shutil.rmtree(target)
    temporary.mkdir(parents=True)
    try:
        populate_staging_tree(temporary, labs)
        if output.exists():
            shutil.rmtree(output)
        temporary.replace(output)
    except Exception:
        if temporary.exists():
            shutil.rmtree(temporary)
        raise


def check() -> None:
    with tempfile.TemporaryDirectory(prefix="az104-site-check-") as temp_dir:
        first_output = Path(temp_dir) / "site-docs-first"
        second_output = Path(temp_dir) / "site-docs-second"
        labs = load_labs()
        populate_staging_tree(first_output, labs)
        populate_staging_tree(second_output, labs)
        if not (first_output / "index.md").is_file():
            raise SiteBuildError("Site staging check did not produce index.md")
        if len(list((first_output / "labs").glob("[0-2][0-9]-*/README.md"))) != 28:
            raise SiteBuildError("Site staging check did not produce all 28 lab guides")
        first_manifest = (first_output / ".stage-manifest.json").read_bytes()
        second_manifest = (second_output / ".stage-manifest.json").read_bytes()
        if first_manifest != second_manifest:
            raise SiteBuildError("Two consecutive staging passes produced different manifests")


def check_built_site(site_root: Path) -> None:
    site_root = site_root.resolve()
    representative = (
        site_root / "index.html",
        site_root / "learner-progress" / "index.html",
        site_root / "labs" / "00-safe-bootstrap" / "index.html",
        site_root / "labs" / "14-container-apps" / "index.html",
        site_root / "labs" / "27-capstone-operate-recover" / "index.html",
    )
    for page in representative:
        if not page.is_file():
            raise SiteBuildError(f"Built site is missing representative page: {page}")
        parser = AccessibilityParser()
        parser.feed(page.read_text(encoding="utf-8"))
        failures: list[str] = []
        if not parser.has_language:
            failures.append("document language")
        if not parser.has_viewport:
            failures.append("responsive viewport")
        if parser.main_count != 1:
            failures.append(f"one main landmark (found {parser.main_count})")
        if parser.h1_count != 1:
            failures.append(f"one H1 (found {parser.h1_count})")
        if parser.images_without_alt:
            failures.append(f"alt text for {parser.images_without_alt} image(s)")
        if parser.external_active_resources:
            failures.append(
                "no externally hosted runtime assets "
                f"(found {len(parser.external_active_resources)})"
            )
        if failures:
            raise SiteBuildError(f"{page} failed static accessibility checks: {', '.join(failures)}")

    progress_script = site_root / "assets" / "progress.js"
    progress_styles = site_root / "assets" / "progress.css"
    if not progress_script.is_file() or not progress_styles.is_file():
        raise SiteBuildError("Built site is missing local progress assets")
    styles = progress_styles.read_text(encoding="utf-8")
    if "prefers-reduced-motion" not in styles or "auto-fit" not in styles:
        raise SiteBuildError("Progress styles must retain reduced-motion and responsive-grid behavior")

    search_index = site_root / "search" / "search_index.json"
    if not search_index.is_file():
        raise SiteBuildError("Built site is missing the client-side search index")
    try:
        search_document = json.loads(search_index.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SiteBuildError(f"Client-side search index is invalid: {exc}") from exc
    indexed_documents = search_document.get("docs", [])
    if not isinstance(indexed_documents, list) or not indexed_documents:
        raise SiteBuildError("Client-side search index contains no documents")
    answer_hits = [
        item.get("location", "")
        for item in indexed_documents
        if isinstance(item, dict)
        and "/assessment/answers/" in str(item.get("location", "")).casefold()
    ]
    if answer_hits:
        raise SiteBuildError(
            "Assessment answer keys must be excluded from learner search; found "
            + ", ".join(answer_hits[:3])
        )
    indexed_locations = {
        str(item.get("location", ""))
        for item in indexed_documents
        if isinstance(item, dict)
    }
    indexed_lab_roots = {
        match.group(1)
        for location in indexed_locations
        if (
            match := re.match(
                r"^(labs/(?:0[0-9]|1[0-9]|2[0-7])-[a-z0-9-]+/)",
                location,
            )
        )
    }
    if len(indexed_lab_roots) != 28:
        raise SiteBuildError(
            "Client-side search must include every lab guide; "
            f"found {len(indexed_lab_roots)} of 28"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    operation = parser.add_mutually_exclusive_group()
    operation.add_argument(
        "--check",
        action="store_true",
        help="Validate a temporary staging tree without changing the local staging directory.",
    )
    operation.add_argument(
        "--check-built-site",
        type=Path,
        metavar="SITE_DIR",
        help="Check representative built pages for deterministic accessibility signals.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Site staging directory (default: .site-docs).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.check_built_site:
            check_built_site(args.check_built_site)
            print("PASS  representative built pages satisfy static accessibility checks")
        elif args.check:
            check()
            print("PASS  documentation site sources stage cleanly")
        else:
            stage(args.output)
            print(f"PASS  staged documentation site at {args.output}")
    except SiteBuildError as exc:
        print(f"FAIL  {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
