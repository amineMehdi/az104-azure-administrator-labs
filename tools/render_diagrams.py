#!/usr/bin/env python3
"""Render the repository's Mermaid flowcharts as deterministic accessible SVG.

The curriculum deliberately uses a small, documented Mermaid subset: left-to-right
flowcharts, labelled directed edges, class definitions, and class assignments.  A
repository-owned renderer keeps generated SVG byte-for-byte stable without a
browser, network access, fonts, or an unpinned JavaScript dependency.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAB_PATTERN = re.compile(r"^\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
RENDERER_ID = "az104-mermaid-flowchart-svg/1.0.0"


class DiagramError(ValueError):
    """Raised when a diagram uses syntax outside the deterministic subset."""


@dataclass
class Node:
    identifier: str
    label: str
    shape: str = "rect"
    class_name: str | None = None
    order: int = 0
    rank: int = 0
    x: float = 0
    y: float = 0
    width: float = 260
    height: float = 68


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str = ""


@dataclass
class Diagram:
    nodes: dict[str, Node] = field(default_factory=dict)
    edges: list[Edge] = field(default_factory=list)
    styles: dict[str, dict[str, str]] = field(default_factory=dict)


def normalized_source(text: str) -> str:
    """Normalize only transport-level differences before hashing the source."""
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines) + "\n"


def clean_label(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    value = re.sub(r"(?i)<br\s*/?>", "\n", value)
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value).strip()


def parse_node(expression: str, diagram: Diagram) -> str:
    expression = expression.strip().rstrip(";").strip()
    match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*)(.*)", expression)
    if not match:
        raise DiagramError(f"unsupported node expression: {expression!r}")
    identifier, descriptor = match.groups()
    label = identifier
    shape = "rect"
    descriptor = descriptor.strip()
    if descriptor:
        if descriptor.startswith("([") and descriptor.endswith("])"):
            label = descriptor[2:-2]
            shape = "stadium"
        elif descriptor.startswith("[(") and descriptor.endswith(")]"):
            label = descriptor[2:-2]
            shape = "database"
        elif descriptor.startswith("[") and descriptor.endswith("]"):
            label = descriptor[1:-1]
        else:
            raise DiagramError(f"unsupported shape for node {identifier}: {descriptor!r}")
        label = clean_label(label)
    existing = diagram.nodes.get(identifier)
    if existing is None:
        diagram.nodes[identifier] = Node(
            identifier=identifier,
            label=label,
            shape=shape,
            order=len(diagram.nodes),
        )
    elif descriptor:
        existing.label = label
        existing.shape = shape
    return identifier


def parse_mermaid(text: str) -> Diagram:
    source = normalized_source(text)
    lines = source.splitlines()
    first_index = next(
        (index for index, line in enumerate(lines) if line.strip() and not line.lstrip().startswith("%%")),
        None,
    )
    if first_index is None or not re.fullmatch(r"flowchart\s+LR", lines[first_index].strip(), re.I):
        raise DiagramError("architecture diagrams must begin with 'flowchart LR'")

    diagram = Diagram()
    class_assignments: list[tuple[list[str], str]] = []
    edge_pattern = re.compile(r"^(.*?)\s*-->\s*(?:\|([^|]*)\|\s*)?(.*?)\s*;?$")
    for number, raw_line in enumerate(lines[first_index + 1 :], start=first_index + 2):
        line = raw_line.strip()
        if not line or line.startswith("%%"):
            continue
        if line.startswith("classDef "):
            match = re.fullmatch(r"classDef\s+([A-Za-z_][\w-]*)\s+(.+?)\s*;?", line)
            if not match:
                raise DiagramError(f"line {number}: invalid classDef")
            name, declarations = match.groups()
            style: dict[str, str] = {}
            for declaration in declarations.rstrip(";").split(","):
                if ":" not in declaration:
                    raise DiagramError(f"line {number}: invalid style declaration {declaration!r}")
                key, value = declaration.split(":", 1)
                key = key.strip()
                if key not in {"fill", "stroke", "color"}:
                    raise DiagramError(f"line {number}: unsupported style property {key!r}")
                style[key] = value.strip()
            diagram.styles[name] = style
            continue
        if line.startswith("class "):
            match = re.fullmatch(r"class\s+([A-Za-z0-9_,-]+)\s+([A-Za-z_][\w-]*)\s*;?", line)
            if not match:
                raise DiagramError(f"line {number}: invalid class assignment")
            class_assignments.append((match.group(1).split(","), match.group(2)))
            continue
        edge_match = edge_pattern.fullmatch(line)
        if edge_match:
            source_expression, label, target_expression = edge_match.groups()
            source_id = parse_node(source_expression, diagram)
            target_id = parse_node(target_expression, diagram)
            diagram.edges.append(Edge(source_id, target_id, clean_label(label or "")))
            continue
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*(?:\(\[.*\]\)|\[\(.*\)\]|\[.*\])", line):
            parse_node(line, diagram)
            continue
        raise DiagramError(f"line {number}: unsupported Mermaid syntax: {line!r}")

    if not diagram.nodes or not diagram.edges:
        raise DiagramError("a diagram must contain at least one node and one directed edge")
    for identifiers, class_name in class_assignments:
        if class_name not in diagram.styles:
            raise DiagramError(f"class {class_name!r} has no classDef")
        for identifier in identifiers:
            if identifier not in diagram.nodes:
                raise DiagramError(f"class assignment references unknown node {identifier!r}")
            diagram.nodes[identifier].class_name = class_name
    return diagram


def assign_layout(diagram: Diagram) -> tuple[int, int]:
    """Assign stable ranks with breadth-first distance from declaration roots."""
    adjacency: dict[str, list[str]] = {identifier: [] for identifier in diagram.nodes}
    incoming: dict[str, int] = {identifier: 0 for identifier in diagram.nodes}
    for edge in diagram.edges:
        adjacency[edge.source].append(edge.target)
        incoming[edge.target] += 1

    ordered = sorted(diagram.nodes.values(), key=lambda node: node.order)
    roots = [node.identifier for node in ordered if incoming[node.identifier] == 0]
    if not roots:
        roots = [ordered[0].identifier]
    distance: dict[str, int] = {}
    queue: deque[str] = deque()
    for root in roots:
        distance[root] = 0
        queue.append(root)
    while queue:
        source = queue.popleft()
        for target in adjacency[source]:
            candidate = distance[source] + 1
            if target not in distance or candidate < distance[target]:
                distance[target] = candidate
                queue.append(target)
    for node in ordered:
        if node.identifier not in distance:
            distance[node.identifier] = 0
            queue.append(node.identifier)
            while queue:
                source = queue.popleft()
                for target in adjacency[source]:
                    candidate = distance[source] + 1
                    if target not in distance:
                        distance[target] = candidate
                        queue.append(target)

    columns: dict[int, list[Node]] = {}
    for node in ordered:
        node.rank = distance[node.identifier]
        node.height = 68 + max(0, len(node.label.splitlines()) - 1) * 20
        columns.setdefault(node.rank, []).append(node)

    margin_x, margin_y = 64, 80
    node_width, column_gap, row_gap = 260, 120, 34
    maximum_rows_height = max(
        sum(node.height for node in nodes) + row_gap * (len(nodes) - 1)
        for nodes in columns.values()
    )
    for rank, nodes in sorted(columns.items()):
        group_height = sum(node.height for node in nodes) + row_gap * (len(nodes) - 1)
        y = margin_y + (maximum_rows_height - group_height) / 2
        for node in nodes:
            node.width = node_width
            node.x = margin_x + rank * (node_width + column_gap)
            node.y = y
            y += node.height + row_gap
    width = int(margin_x * 2 + (max(columns) + 1) * node_width + max(columns) * column_gap)
    height = int(margin_y * 2 + maximum_rows_height)
    return width, height


def svg_text_lines(node: Node, color: str) -> list[str]:
    lines = node.label.splitlines() or [node.identifier]
    center_x = node.x + node.width / 2
    first_y = node.y + node.height / 2 - (len(lines) - 1) * 10
    rendered = []
    for index, line in enumerate(lines):
        rendered.append(
            f'    <text x="{center_x:g}" y="{first_y + index * 20:g}" '
            f'class="node-label" fill="{html.escape(color, quote=True)}">{html.escape(line)}</text>'
        )
    return rendered


def node_shape(node: Node, style: dict[str, str]) -> list[str]:
    fill = html.escape(style.get("fill", "#f6f8fa"), quote=True)
    stroke = html.escape(style.get("stroke", "#57606a"), quote=True)
    color = html.escape(style.get("color", "#24292f"), quote=True)
    common = f'fill="{fill}" stroke="{stroke}"'
    if node.shape == "stadium":
        shape = (
            f'    <rect x="{node.x:g}" y="{node.y:g}" width="{node.width:g}" '
            f'height="{node.height:g}" rx="{node.height / 2:g}" {common}/>'
        )
        return [shape, *svg_text_lines(node, color)]
    if node.shape == "database":
        ellipse_height = 18
        body_y = node.y + ellipse_height / 2
        body_height = node.height - ellipse_height
        return [
            f'    <rect x="{node.x:g}" y="{body_y:g}" width="{node.width:g}" '
            f'height="{body_height:g}" {common}/>',
            f'    <ellipse cx="{node.x + node.width / 2:g}" cy="{body_y:g}" '
            f'rx="{node.width / 2:g}" ry="{ellipse_height / 2:g}" {common}/>',
            f'    <path d="M {node.x:g} {node.y + node.height - ellipse_height / 2:g} '
            f'a {node.width / 2:g} {ellipse_height / 2:g} 0 0 0 {node.width:g} 0" '
            f'fill="none" stroke="{stroke}"/>',
            *svg_text_lines(node, color),
        ]
    return [
        f'    <rect x="{node.x:g}" y="{node.y:g}" width="{node.width:g}" '
        f'height="{node.height:g}" rx="10" {common}/>',
        *svg_text_lines(node, color),
    ]


def edge_path(edge: Edge, diagram: Diagram, index: int) -> tuple[str, float, float]:
    source = diagram.nodes[edge.source]
    target = diagram.nodes[edge.target]
    if source.rank < target.rank:
        start_x, start_y = source.x + source.width, source.y + source.height / 2
        end_x, end_y = target.x, target.y + target.height / 2
        middle_x = (start_x + end_x) / 2
        path = f"M {start_x:g} {start_y:g} C {middle_x:g} {start_y:g}, {middle_x:g} {end_y:g}, {end_x:g} {end_y:g}"
        return path, middle_x, (start_y + end_y) / 2
    if source.rank == target.rank:
        start_x, start_y = source.x + source.width / 2, source.y + source.height
        end_x, end_y = target.x + target.width / 2, target.y
        offset = 24 + (index % 3) * 10
        path = f"M {start_x:g} {start_y:g} C {start_x + offset:g} {(start_y + end_y) / 2:g}, {end_x + offset:g} {(start_y + end_y) / 2:g}, {end_x:g} {end_y:g}"
        return path, (start_x + end_x) / 2 + offset, (start_y + end_y) / 2
    start_x, start_y = source.x, source.y + source.height / 2
    end_x, end_y = target.x + target.width, target.y + target.height / 2
    detour_y = max(source.y + source.height, target.y + target.height) + 30 + (index % 3) * 14
    path = f"M {start_x:g} {start_y:g} C {start_x - 50:g} {detour_y:g}, {end_x + 50:g} {detour_y:g}, {end_x:g} {end_y:g}"
    return path, (start_x + end_x) / 2, detour_y


def read_lab_title(lab_dir: Path) -> tuple[str, str]:
    metadata = (lab_dir / "lab.yml").read_text(encoding="utf-8", errors="replace")
    lab_id = re.search(r"(?m)^id:\s*['\"]?(LAB-\d{2})['\"]?\s*$", metadata)
    title = re.search(r"(?m)^title:\s*(.+?)\s*$", metadata)
    if not lab_id or not title:
        raise DiagramError(f"{lab_dir.name}/lab.yml must declare id and title")
    clean_title = title.group(1).strip().strip("'\"")
    return lab_id.group(1), clean_title


def render_lab_svg(lab_dir: Path) -> str:
    source_path = lab_dir / "diagrams" / "architecture.mmd"
    source = normalized_source(source_path.read_text(encoding="utf-8", errors="strict"))
    diagram = parse_mermaid(source)
    width, height = assign_layout(diagram)
    lab_id, title = read_lab_title(lab_dir)
    prefix = lab_id.casefold().replace("-", "")
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
    labels = ", ".join(node.label.replace("\n", " ") for node in sorted(diagram.nodes.values(), key=lambda item: item.order))
    relationships = "; ".join(
        f"{diagram.nodes[edge.source].label.replace(chr(10), ' ')} to "
        f"{diagram.nodes[edge.target].label.replace(chr(10), ' ')}"
        + (f" ({edge.label})" if edge.label else "")
        for edge in diagram.edges
    )
    description = (
        f"Left-to-right service topology with {len(diagram.nodes)} components and "
        f"{len(diagram.edges)} directed relationships. Components: {labels}. "
        f"Relationships: {relationships}."
    )
    metadata = json.dumps(
        {"renderer": RENDERER_ID, "source": "architecture.mmd", "sourceSha256": digest},
        sort_keys=True,
        separators=(",", ":"),
    )

    output = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{prefix}-title {prefix}-desc">',
        f'  <title id="{prefix}-title">{html.escape(lab_id)} architecture: {html.escape(title)}</title>',
        f'  <desc id="{prefix}-desc">{html.escape(description)}</desc>',
        f'  <metadata id="{prefix}-metadata">{html.escape(metadata)}</metadata>',
        "  <defs>",
        '    <marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto" markerUnits="strokeWidth">',
        '      <path d="M 0 0 L 10 4 L 0 8 z" fill="#57606a"/>',
        "    </marker>",
        "    <style>",
        "      .edge { fill: none; stroke: #57606a; stroke-width: 2; marker-end: url(#arrow); }",
        "      .edge-label-bg { fill: #ffffff; opacity: .94; }",
        "      .edge-label { fill: #57606a; font: 13px 'Segoe UI', Arial, sans-serif; text-anchor: middle; dominant-baseline: central; }",
        "      .node-label { font: 600 15px 'Segoe UI', Arial, sans-serif; text-anchor: middle; dominant-baseline: central; }",
        "    </style>",
        "  </defs>",
        '  <rect width="100%" height="100%" fill="#ffffff"/>',
        '  <g aria-hidden="true">',
    ]
    edge_labels: list[tuple[str, float, float]] = []
    for index, edge in enumerate(diagram.edges):
        path, label_x, label_y = edge_path(edge, diagram, index)
        output.append(f'    <path class="edge" d="{path}"/>')
        if edge.label:
            edge_labels.append((edge.label, label_x, label_y))
    for edge_label, x, y in edge_labels:
        label_width = max(50, len(edge_label) * 7 + 14)
        output.append(
            f'    <rect class="edge-label-bg" x="{x - label_width / 2:g}" y="{y - 11:g}" '
            f'width="{label_width:g}" height="22" rx="4"/>'
        )
        output.append(f'    <text class="edge-label" x="{x:g}" y="{y:g}">{html.escape(edge_label)}</text>')
    for node in sorted(diagram.nodes.values(), key=lambda item: item.order):
        style = diagram.styles.get(node.class_name or "", {})
        output.extend(node_shape(node, style))
    output.extend(["  </g>", "</svg>", ""])
    return "\n".join(output)


def lab_directories(only: list[str]) -> list[Path]:
    directories = sorted(
        path for path in (ROOT / "labs").iterdir() if path.is_dir() and LAB_PATTERN.fullmatch(path.name)
    )
    if not only:
        return directories
    requested = {value.casefold() for value in only}
    selected = [
        path
        for path in directories
        if path.name.casefold() in requested or path.name[:2] in requested or f"lab-{path.name[:2]}" in requested
    ]
    missing = requested - {
        key
        for path in selected
        for key in (path.name.casefold(), path.name[:2], f"lab-{path.name[:2]}")
        if key in requested
    }
    if missing:
        raise DiagramError(f"unknown lab selector(s): {', '.join(sorted(missing))}")
    return selected


def run(check: bool, only: list[str]) -> int:
    failures = 0
    directories = lab_directories(only)
    if not directories:
        print("FAIL  no lab directories found")
        return 1
    for lab_dir in directories:
        relative = lab_dir.relative_to(ROOT)
        svg_path = lab_dir / "diagrams" / "architecture.svg"
        try:
            expected = render_lab_svg(lab_dir)
        except (DiagramError, OSError, UnicodeError) as exc:
            failures += 1
            print(f"FAIL  {relative}: {exc}")
            continue
        if check:
            actual = svg_path.read_text(encoding="utf-8", errors="replace") if svg_path.exists() else ""
            if actual != expected:
                failures += 1
                print(f"FAIL  {relative}/diagrams/architecture.svg is stale; run python tools/render_diagrams.py")
            else:
                print(f"PASS  {relative}/diagrams/architecture.svg")
        else:
            svg_path.parent.mkdir(parents=True, exist_ok=True)
            with svg_path.open("w", encoding="utf-8", newline="\n") as handle:
                handle.write(expected)
            print(f"WRITE {relative}/diagrams/architecture.svg")
    return 1 if failures else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if a committed SVG differs from deterministic output.")
    parser.add_argument("--only", action="append", default=[], metavar="LAB", help="Render one lab ID or folder; repeat as needed.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        return run(args.check, args.only)
    except DiagramError as exc:
        print(f"FAIL  {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
