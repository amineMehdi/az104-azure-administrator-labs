#!/usr/bin/env python3
"""Shared assessment allocation for the AZ-104 curriculum."""

from __future__ import annotations

from collections import Counter


DOMAIN_DISPLAY_NAMES = {
    "identity-governance": "Manage Azure identities and governance",
    "storage": "Implement and manage storage",
    "compute": "Deploy and manage Azure compute resources",
    "networking": "Implement and manage virtual networking",
    "monitor-recovery": "Monitor and maintain Azure resources",
}

DOMAIN_OBJECTIVE_PREFIXES = {
    "identity-governance": "IG-",
    "storage": "ST-",
    "compute": "CP-",
    "networking": "NW-",
    "monitor-recovery": "MR-",
}


def _mix(foundational: int, applied: int, advanced: int) -> tuple[str, ...]:
    return (
        *("foundational" for _ in range(foundational)),
        *("applied" for _ in range(applied)),
        *("advanced" for _ in range(advanced)),
    )


ASSESSMENT_PLAN: dict[str, dict[str, object]] = {
    "00": {"enabled": False, "questionCount": 0},
    "01": {"enabled": True, "primaryDomain": "identity-governance", "difficulties": _mix(3, 5, 2)},
    "02": {"enabled": True, "primaryDomain": "identity-governance", "difficulties": _mix(3, 5, 2)},
    "03": {"enabled": True, "primaryDomain": "identity-governance", "difficulties": _mix(3, 5, 2)},
    "04": {"enabled": True, "primaryDomain": "identity-governance", "difficulties": _mix(3, 5, 2)},
    "05": {"enabled": True, "primaryDomain": "identity-governance", "difficulties": _mix(3, 5, 2)},
    "06": {"enabled": True, "primaryDomain": "storage", "difficulties": _mix(4, 6, 2)},
    "07": {"enabled": True, "primaryDomain": "storage", "difficulties": _mix(4, 6, 2)},
    "08": {"enabled": True, "primaryDomain": "storage", "difficulties": _mix(4, 7, 3)},
    "09": {"enabled": True, "primaryDomain": "storage", "difficulties": _mix(3, 6, 3)},
    "10": {"enabled": True, "primaryDomain": "compute", "difficulties": _mix(3, 5, 2)},
    "11": {"enabled": True, "primaryDomain": "compute", "difficulties": _mix(2, 4, 2)},
    "12": {"enabled": True, "primaryDomain": "compute", "difficulties": _mix(2, 4, 2)},
    "13": {"enabled": True, "primaryDomain": "compute", "difficulties": _mix(2, 3, 1)},
    "14": {"enabled": True, "primaryDomain": "compute", "difficulties": _mix(1, 2, 1)},
    "15": {"enabled": True, "primaryDomain": "compute", "difficulties": _mix(2, 4, 1)},
    "16": {"enabled": True, "primaryDomain": "compute", "difficulties": _mix(3, 3, 1)},
    "17": {"enabled": True, "primaryDomain": "networking", "difficulties": _mix(3, 5, 2)},
    "18": {"enabled": True, "primaryDomain": "networking", "difficulties": _mix(3, 5, 2)},
    "19": {"enabled": True, "primaryDomain": "networking", "difficulties": _mix(3, 5, 2)},
    "20": {"enabled": True, "primaryDomain": "networking", "difficulties": _mix(3, 5, 2)},
    "21": {"enabled": True, "primaryDomain": "networking", "difficulties": _mix(3, 5, 2)},
    "22": {"enabled": True, "primaryDomain": "monitor-recovery", "difficulties": _mix(5, 7, 3)},
    "23": {"enabled": True, "primaryDomain": "monitor-recovery", "difficulties": _mix(3, 5, 2)},
    "24": {"enabled": True, "primaryDomain": "monitor-recovery", "difficulties": _mix(4, 8, 3)},
    "25": {"enabled": True, "primaryDomain": "monitor-recovery", "difficulties": _mix(3, 5, 2)},
    "26": {"enabled": False, "questionCount": 0},
    "27": {"enabled": False, "questionCount": 0},
}

for _entry in ASSESSMENT_PLAN.values():
    if _entry["enabled"]:
        _entry["questionCount"] = len(_entry["difficulties"])


def metadata_for_lab(number: str) -> dict[str, object]:
    """Return the serializable lab.yml assessment contract."""
    plan = ASSESSMENT_PLAN[number]
    metadata: dict[str, object] = {
        "enabled": bool(plan["enabled"]),
        "questionCount": int(plan["questionCount"]),
    }
    if plan["enabled"]:
        metadata["primaryDomain"] = str(plan["primaryDomain"])
    return metadata


def expected_domain_difficulties() -> dict[str, Counter[str]]:
    """Aggregate the locked 15/25/10 mix for each official domain."""
    totals = {domain: Counter() for domain in DOMAIN_DISPLAY_NAMES}
    for plan in ASSESSMENT_PLAN.values():
        if plan["enabled"]:
            totals[str(plan["primaryDomain"])].update(plan["difficulties"])
    return totals


def domain_lab_numbers(domain: str) -> list[str]:
    return [
        number
        for number, plan in ASSESSMENT_PLAN.items()
        if plan.get("enabled") and plan.get("primaryDomain") == domain
    ]

