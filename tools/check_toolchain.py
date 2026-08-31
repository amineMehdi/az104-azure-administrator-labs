#!/usr/bin/env python3
"""Compatibility entry point for the blocking PowerShell readiness report."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READINESS = ROOT / "tools" / "Test-LabEnvironment.ps1"


def main() -> int:
    """Run the authoritative offline readiness check without duplicating policy."""

    powershell = shutil.which("pwsh")
    if not powershell:
        print("FAIL  PowerShell 7.4 or later is required to run readiness.")
        return 1
    if not READINESS.is_file():
        print("FAIL  tools/Test-LabEnvironment.ps1 is missing.")
        return 1

    completed = subprocess.run(
        [
            powershell,
            "-NoLogo",
            "-NoProfile",
            "-File",
            str(READINESS),
            "-OfflineOnly",
        ],
        cwd=ROOT,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
