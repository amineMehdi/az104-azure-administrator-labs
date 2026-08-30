#!/usr/bin/env python3
"""Validate committed portal screenshots: format, size, stripped metadata, and OCR privacy scan."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_WIDTH = 1920
MAX_BYTES_ERROR = 600_000
MAX_BYTES_WARN = 500_000
IGNORED_DIRECTORY_NAMES = {".git", ".state", ".venv", "__pycache__", "node_modules", "tmp", "venv"}
# Text that must never appear readable inside committed evidence.
SENSITIVE_TEXT = {
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "GUID (tenant/subscription/object ID)": re.compile(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
    ),
    "connection string": re.compile(r"AccountKey=|SharedAccessSignature=|sig=", re.IGNORECASE),
}
ALLOWED_PNG_INFO_KEYS = {"dpi", "gamma", "srgb", "transparency", "interlace", "aspect"}


def is_ignored(path: Path) -> bool:
    return any(part.lower() in IGNORED_DIRECTORY_NAMES for part in path.parts)


def iter_pngs() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() == ".png" and not is_ignored(path.relative_to(ROOT))
    )


def ocr_text(image) -> str | None:
    try:
        import pytesseract

        return pytesseract.image_to_string(image)
    except Exception:  # missing module or tesseract binary: OCR is best-effort
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-ocr", action="store_true", help="Skip the OCR privacy warning scan")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    pngs = iter_pngs()
    if not pngs:
        print("PASS: no committed PNG images to validate")
        return 0

    try:
        from PIL import Image
    except ImportError:
        print("GATED: Pillow is not installed; run python -m pip install -r requirements-dev.txt")
        return 2

    ocr_available = not args.skip_ocr
    for path in pngs:
        rel = path.relative_to(ROOT)
        if "images" in path.parts and "portal" not in path.parts:
            errors.append(f"{rel}: PNG evidence must live under images/portal/")
        size = path.stat().st_size
        if size > MAX_BYTES_ERROR:
            errors.append(f"{rel}: {size} bytes exceeds the {MAX_BYTES_ERROR} byte limit")
        elif size > MAX_BYTES_WARN:
            warnings.append(f"{rel}: {size} bytes exceeds the {MAX_BYTES_WARN} byte optimization target")
        try:
            with Image.open(path) as image:
                if image.format != "PNG":
                    errors.append(f"{rel}: file is {image.format}, not PNG")
                if image.width > MAX_WIDTH:
                    errors.append(f"{rel}: width {image.width} exceeds {MAX_WIDTH} px")
                exif = image.getexif()
                if len(exif) > 0:
                    errors.append(f"{rel}: EXIF metadata must be stripped")
                text_chunks = set(getattr(image, "text", {}) or {})
                stray = {key for key in set(image.info) | text_chunks if key.lower() not in ALLOWED_PNG_INFO_KEYS}
                if "icc_profile" in stray:
                    stray.discard("icc_profile")
                    warnings.append(f"{rel}: embedded ICC profile; prefer re-encoding without it")
                if stray:
                    errors.append(f"{rel}: metadata chunks must be stripped: {', '.join(sorted(stray))}")
                if ocr_available:
                    extracted = ocr_text(image)
                    if extracted is None:
                        ocr_available = False
                        warnings.append("OCR scan skipped: pytesseract or the tesseract binary is unavailable")
                    else:
                        for label, pattern in SENSITIVE_TEXT.items():
                            match = pattern.search(extracted)
                            if match:
                                warnings.append(f"{rel}: OCR found a possible {label}: {match.group(0)!r} — review redaction")
        except OSError as failure:
            errors.append(f"{rel}: unreadable image ({failure})")

    for message in warnings:
        print(f"WARN  {message}")
    for message in errors:
        print(f"FAIL  {message}")
    print(f"Summary: {len(pngs)} image(s), {len(warnings)} warning(s), {len(errors)} failure(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
