#!/usr/bin/env python3
"""Report the local lab-authoring toolchain without changing it."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


TOOLS = {
    "git": ["git", "--version"],
    "azure-cli": ["az", "--version"],
    "powershell": ["pwsh", "-NoLogo", "-NoProfile", "-Command", "$PSVersionTable.PSVersion.ToString()"],
    "jq": ["jq", "--version"],
    "bicep": ["bicep", "--version"],
    "azcopy": ["azcopy", "--version"],
    "python": ["python", "--version"],
    "node": ["node", "--version"],
}


def main() -> int:
    missing: list[str] = []
    for label, command in TOOLS.items():
        executable = command[0]
        resolved = shutil.which(executable)
        if not resolved:
            print(f"WARN  {label}: not found")
            missing.append(label)
            continue

        invocation = [resolved, *command[1:]]
        if os.name == "nt" and Path(resolved).suffix.lower() in {".bat", ".cmd"}:
            invocation = [
                os.environ.get("COMSPEC", "cmd.exe"),
                "/d",
                "/s",
                "/c",
                "call",
                resolved,
                *command[1:],
            ]

        try:
            result = subprocess.run(invocation, text=True, capture_output=True, check=False)
        except OSError as exc:
            print(f"WARN  {label}: could not start ({exc})")
            missing.append(label)
            continue

        output = (result.stdout or result.stderr).strip().splitlines()
        summary = output[0][:160] if output else "no version output"
        if result.returncode == 0:
            print(f"PASS  {label}: {summary}")
        else:
            print(f"WARN  {label}: version check exited {result.returncode} ({summary})")
            missing.append(label)

    if missing:
        print("\nMissing optional or lab-specific tools: " + ", ".join(missing))
        print("Individual lab preflight scripts decide whether a missing tool blocks that lab.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
