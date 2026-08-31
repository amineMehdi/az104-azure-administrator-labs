#!/usr/bin/env python3
"""Render the v2 AZ-104 labs from structured authoring data.

The renderer is deliberately non-destructive: it updates only content enclosed
by stable generated markers, never removes a directory, and supports ``--check``
for CI drift detection.  The initial v2 migration may add a marked region to an
existing file; subsequent runs preserve everything outside that region.

No command in the generated PowerShell is executed by this program.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
LABS_ROOT = ROOT / "labs"
CONTENT_PATH = ROOT / "curriculum" / "lab-content.yml"
BEGIN = "BEGIN GENERATED AZ104 V2"
END = "END GENERATED AZ104 V2"
POWERSHELL_BEGIN = f"# {BEGIN}"
POWERSHELL_END = f"# {END}"
MARKDOWN_BEGIN = f"<!-- {BEGIN} -->"
MARKDOWN_END = f"<!-- {END} -->"
YAML_BEGIN = f"# {BEGIN}"
YAML_END = f"# {END}"
BLUEPRINT_DATE = "2026-04-17"
OFFLINE_DATE = "2026-08-31"
STUDY_GUIDE = (
    "https://learn.microsoft.com/en-us/credentials/certifications/"
    "resources/study-guides/az-104"
)


class _NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: object) -> bool:
        return True


DOMAIN_IDS = {
    "00": "foundation",
    **{f"{value:02d}": "identity-governance" for value in range(1, 6)},
    **{f"{value:02d}": "storage" for value in range(6, 10)},
    **{f"{value:02d}": "compute" for value in range(10, 17)},
    **{f"{value:02d}": "networking" for value in range(17, 22)},
    **{f"{value:02d}": "monitor-recovery" for value in range(22, 26)},
    "26": "capstone",
    "27": "capstone",
}


PRICING_LINKS = {
    "foundation": ("Azure pricing calculator", "https://azure.microsoft.com/pricing/calculator/"),
    "identity-governance": ("Microsoft Entra pricing", "https://azure.microsoft.com/pricing/details/active-directory/"),
    "storage": ("Azure Storage pricing", "https://azure.microsoft.com/pricing/details/storage/"),
    "compute": ("Azure compute pricing", "https://azure.microsoft.com/pricing/details/virtual-machines/"),
    "networking": ("Azure Virtual Network pricing", "https://azure.microsoft.com/pricing/details/virtual-network/"),
    "monitor-recovery": ("Azure Monitor pricing", "https://azure.microsoft.com/pricing/details/monitor/"),
    "capstone": ("Azure pricing calculator", "https://azure.microsoft.com/pricing/calculator/"),
}


EXTRA_INPUTS: dict[str, list[dict[str, Any]]] = {
    "01": [
        {"id": "tenant-domain", "environmentVariable": "AZ104_TENANT_DOMAIN", "description": "Verified disposable tenant domain", "required": True, "secret": False, "gateBehavior": "block", "safeExample": "contoso-lab.onmicrosoft.com", "checkpointIds": ["LAB01-CP01", "LAB01-CP02"]},
        {"id": "initial-password", "environmentVariable": "AZ104_LAB_INITIAL_PASSWORD", "description": "Temporary policy-compliant initial password", "required": True, "secret": True, "gateBehavior": "block", "safeExample": "<secret>", "checkpointIds": ["LAB01-CP02"]},
    ],
    "02": [
        {"id": "guest-email", "environmentVariable": "AZ104_GUEST_EMAIL", "description": "Disposable external invitation address", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "learner@example.test", "checkpointIds": ["LAB02-CP03", "LAB02-CP04"]},
        {"id": "license-sku-id", "environmentVariable": "AZ104_LICENSE_SKU_ID", "description": "Approved subscribed license SKU ID", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "00000000-0000-0000-0000-000000000000", "checkpointIds": ["LAB02-CP04"]},
        {"id": "usage-location", "environmentVariable": "AZ104_USAGE_LOCATION", "description": "Two-letter usage location required for the optional license assignment", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "DE", "checkpointIds": ["LAB02-CP04"]},
        {"id": "allow-sspr-policy-change", "environmentVariable": "AZ104_ALLOW_SSPR_POLICY_CHANGE", "description": "Explicit YES gate for the authorized SSPR change", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "YES", "checkpointIds": ["LAB02-CP05"]},
    ],
    "03": [{"id": "principal-object-id", "environmentVariable": "AZ104_PRINCIPAL_OBJECT_ID", "description": "Disposable principal object ID", "required": True, "secret": False, "gateBehavior": "block", "safeExample": "00000000-0000-0000-0000-000000000000", "checkpointIds": ["LAB03-CP02", "LAB03-CP03", "LAB03-CP04"]}],
    "04": [{"id": "allow-management-group-change", "environmentVariable": "AZ104_ALLOW_MANAGEMENT_GROUP_CHANGE", "description": "Explicit YES gate for optional hierarchy mutation", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "YES", "checkpointIds": ["LAB04-CP05"]}],
    "05": [{"id": "budget-email", "environmentVariable": "AZ104_BUDGET_EMAIL", "description": "Approved budget notification address", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "alerts@example.test", "checkpointIds": ["LAB05-CP04"]}],
    "09": [
        {"id": "files-identity-source", "environmentVariable": "AZ104_FILES_IDENTITY_SOURCE", "description": "Authorized Entra Kerberos, AD DS, or managed-domain integration path", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "entra-kerberos", "checkpointIds": ["LAB09-CP04"]},
        {"id": "files-principal-object-id", "environmentVariable": "AZ104_FILES_PRINCIPAL_OBJECT_ID", "description": "Disposable principal for Azure Files data-plane RBAC", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "00000000-0000-0000-0000-000000000000", "checkpointIds": ["LAB09-CP04"]},
    ],
    "16": [
        {"id": "custom-hostname", "environmentVariable": "AZ104_CUSTOM_HOSTNAME", "description": "Hostname in an owned DNS zone", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "app.lab.example.com", "checkpointIds": ["LAB16-CP04"]},
        {"id": "authorize-custom-domain", "environmentVariable": "AZ104_AUTHORIZE_CUSTOM_DOMAIN", "description": "Exact YES authorization after the App Service domain-verification TXT record is published", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "YES", "checkpointIds": ["LAB16-CP04"]},
    ],
    "20": [
        {"id": "dns-parent-zone", "environmentVariable": "AZ104_DNS_PARENT_ZONE", "description": "Existing Azure DNS parent zone that the learner is authorized to change", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "lab.example.com", "checkpointIds": ["LAB20-CP04"]},
        {"id": "dns-parent-resource-group", "environmentVariable": "AZ104_DNS_PARENT_RESOURCE_GROUP", "description": "Resource group containing the authorized parent zone", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "rg-dns-authority", "checkpointIds": ["LAB20-CP04"]},
        {"id": "dns-parent-zone-id", "environmentVariable": "AZ104_DNS_PARENT_ZONE_ID", "description": "Exact ARM ID used to prove the supplied parent-zone boundary", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-dns-authority/providers/Microsoft.Network/dnsZones/lab.example.com", "checkpointIds": ["LAB20-CP04"]},
        {"id": "authorize-dns-delegation", "environmentVariable": "AZ104_AUTHORIZE_DNS_DELEGATION", "description": "Exact YES authorization to add the run-owned child NS set to the verified parent", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "YES", "checkpointIds": ["LAB20-CP04"]},
    ],
    "23": [{"id": "alert-email", "environmentVariable": "AZ104_ALERT_EMAIL", "description": "Approved action-group receiver", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "alerts@example.test", "checkpointIds": ["LAB23-CP04"]}],
    "25": [
        {"id": "secondary-location", "parameter": "SecondaryLocation", "environmentVariable": "AZ104_SECONDARY_LOCATION", "description": "Approved paired recovery region", "required": True, "secret": False, "source": "parameter-or-environment", "gateBehavior": "block", "safeExample": "northeurope", "checkpointIds": ["LAB25-CP01", "LAB25-CP02", "LAB25-CP03", "LAB25-CP04"]},
        {"id": "enable-asr", "environmentVariable": "AZ104_ENABLE_ASR", "description": "Exact YES authorization for billable Site Recovery replication", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "YES", "checkpointIds": ["LAB25-CP03", "LAB25-CP04"]},
        {"id": "run-asr-test-failover", "environmentVariable": "AZ104_RUN_ASR_TEST_FAILOVER", "description": "Exact YES authorization for an isolated Site Recovery test failover", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "YES", "checkpointIds": ["LAB25-CP04"]},
    ],
    "26": [{"id": "principal-object-id", "environmentVariable": "AZ104_PRINCIPAL_OBJECT_ID", "description": "Optional disposable principal for capstone RBAC", "required": False, "secret": False, "gateBehavior": "skip-checkpoint", "safeExample": "00000000-0000-0000-0000-000000000000", "checkpointIds": ["LAB26-CP04"]}],
}


def _normalized(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip() + "\n"


def _indent(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line if line else line for line in text.splitlines())


def _powershell_ascii(text: str) -> str:
    """Keep generated PowerShell portable without relying on a UTF-8 BOM."""
    translations = str.maketrans(
        {
            "\u00a0": " ",
            "\u2010": "-",
            "\u2011": "-",
            "\u2012": "-",
            "\u2013": "-",
            "\u2014": "-",
            "\u2018": "'",
            "\u2019": "'",
            "\u201c": '"',
            "\u201d": '"',
            "\u2026": "...",
            "\u2192": "->",
            "\u2264": "<=",
            "\u2265": ">=",
        }
    )
    rendered = text.translate(translations)
    non_ascii = sorted({character for character in rendered if ord(character) > 127})
    if non_ascii:
        codepoints = ", ".join(f"U+{ord(character):04X}" for character in non_ascii)
        raise ValueError(f"Generated PowerShell contains unmapped non-ASCII characters: {codepoints}")
    return rendered


def _marked(body: str, kind: str) -> str:
    if kind == "markdown":
        return f"{MARKDOWN_BEGIN}\n{body.rstrip()}\n{MARKDOWN_END}\n"
    if kind == "yaml":
        return f"{YAML_BEGIN}\n{body.rstrip()}\n{YAML_END}\n"
    body = _powershell_ascii(body)
    return f"{POWERSHELL_BEGIN}\n{body.rstrip()}\n{POWERSHELL_END}\n"


def _update_marked(existing: str, rendered: str, kind: str) -> str:
    pairs = {
        "markdown": (MARKDOWN_BEGIN, MARKDOWN_END),
        "yaml": (YAML_BEGIN, YAML_END),
        "powershell": (POWERSHELL_BEGIN, POWERSHELL_END),
    }
    begin, end = pairs[kind]
    existing = existing.replace("\r\n", "\n")
    if begin not in existing or end not in existing:
        return rendered
    prefix, remainder = existing.split(begin, 1)
    _, suffix = remainder.split(end, 1)
    generated_inner = rendered.split(begin, 1)[1].split(end, 1)[0]
    return _normalized(f"{prefix.rstrip()}\n{begin}{generated_inner}{end}\n{suffix.lstrip()}")


def _write_or_check(path: Path, expected: str, check: bool) -> bool:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if _normalized(existing) == _normalized(expected):
        print(f"PASS  {path.relative_to(ROOT)}")
        return True
    if check:
        print(f"FAIL  {path.relative_to(ROOT)} is stale")
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(_normalized(expected))
    print(f"WRITE {path.relative_to(ROOT)}")
    return True


def _input_contract(number: str, checkpoint_ids: list[str]) -> list[dict[str, Any]]:
    common = [
        {"id": "run-id", "parameter": "RunId", "description": "Unique lowercase run ownership identifier", "required": True, "secret": False, "source": "parameter", "safeExample": f"az104l{number}-01", "gateBehavior": "block", "checkpointIds": checkpoint_ids},
        {"id": "subscription-id", "parameter": "SubscriptionId", "environmentVariable": "AZ104_SUBSCRIPTION_ID", "description": "Expected disposable subscription ID", "required": number != "00", "secret": False, "source": "parameter-or-environment", "safeExample": "00000000-0000-0000-0000-000000000000", "gateBehavior": "block", "checkpointIds": checkpoint_ids},
        {"id": "location", "parameter": "Location", "environmentVariable": "AZ104_LOCATION", "description": "Approved primary Azure region", "required": True, "secret": False, "source": "parameter-or-environment", "safeExample": "westeurope", "gateBehavior": "block", "checkpointIds": checkpoint_ids},
    ]
    extras = deepcopy(EXTRA_INPUTS.get(number, []))
    for item in extras:
        item.setdefault("parameter", "".join(part.capitalize() for part in item["id"].split("-")))
        item.setdefault("source", "environment")
    return common + extras


def _pricing_link(domain: str) -> list[dict[str, str]]:
    title, url = PRICING_LINKS[domain]
    return [{"title": title, "url": url}]


def _transformed_command(command: str) -> str:
    return command.replace("$state.external", "$external")


def _instrument_setup_command(command: str, checkpoint_id: str) -> str:
    """Synchronize ARM IDs even when a creation fails part-way through.

    A checkpoint can contain several independently successful creates.  A
    single sync at the end loses the earlier IDs if a later native command
    fails.  Wrapping each authored creation in ``finally`` preserves the
    recoverable ownership trail without changing the learner-facing block.
    """
    rendered: list[str] = []
    mutation = re.compile(
        r"\baz\b.*(?:\bcreate\b|\bimport\b|--method\s+(?:put|post)\b)",
        flags=re.IGNORECASE,
    )
    for line in command.splitlines():
        if mutation.search(line) and not line.lstrip().startswith("#"):
            rendered.extend(
                [
                    "try {",
                    f"    {line}",
                    "} finally {",
                    f"    Sync-ManagedResource -CheckpointId '{checkpoint_id}'",
                    "}",
                ]
            )
        elif re.search(r"\$external\s*\[[^\]]+\]\s*=", line):
            rendered.extend([line, "Save-ExternalState"])
        else:
            rendered.append(line)
    return "\n".join(rendered)


def _independent_task_checks(content: dict[str, Any]) -> dict[str, Any]:
    """Derive ten distinct read-only service checks from each lab's probes.

    Every derived command still executes only the lab-specific queries supplied
    by the authoring catalog. Combining different probes lets each positive and
    negative checkpoint collect independent evidence without adding a generic
    label that merely disguises duplicate commands.
    """
    enriched = deepcopy(content)
    authored = [
        str(task[key]).strip()
        for task in enriched["tasks"]
        for key in ("positiveCommand", "negativeCommand")
        if str(task.get(key, "")).strip()
    ]
    # Substantive authoring wins.  The fallback exists only for older catalog
    # entries whose checks have not yet been rewritten; it must never replace
    # a semantically complete bank of service-specific probes.
    if len({_normalized(command) for command in authored}) >= 8:
        return enriched

    probes: list[str] = []
    for task in enriched["tasks"]:
        for key in ("positiveCommand", "negativeCommand"):
            command = str(task[key]).strip()
            if command and command not in probes:
                probes.append(command)
    if len(probes) < 3:
        raise ValueError("Each lab needs at least three distinct service probes")
    first, second, third = probes[:3]
    variants = [
        first,
        second,
        third,
        f"{first}\n{second}",
        f"{first}\n{third}",
        f"{second}\n{first}",
        f"{second}\n{third}",
        f"{third}\n{first}",
        f"{third}\n{second}",
        f"{first}\n{second}\n{third}",
    ]
    for index, task in enumerate(enriched["tasks"]):
        task["positiveCommand"] = variants[index * 2]
        task["negativeCommand"] = variants[index * 2 + 1]
    return enriched


def _descriptive_source_title(source: dict[str, str]) -> dict[str, str]:
    """Replace a raw-URL label with a readable Microsoft Learn title."""
    rendered = deepcopy(source)
    title = str(rendered.get("title", "")).strip()
    url = str(rendered.get("url", "")).strip()
    if title and not title.lower().startswith(("http://", "https://")):
        return rendered
    slug = url.rstrip("/").rsplit("/", 1)[-1]
    words = slug.replace("_", "-").split("-")
    names = {
        "acr": "ACR",
        "api": "API",
        "arm": "ARM",
        "azure": "Azure",
        "bicep": "Bicep",
        "cli": "CLI",
        "dns": "DNS",
        "https": "HTTPS",
        "ip": "IP",
        "nsg": "NSG",
        "rbac": "RBAC",
        "sas": "SAS",
        "ssl": "TLS/SSL",
        "tls": "TLS",
        "vm": "VM",
        "vms": "VMs",
        "vnet": "VNet",
    }
    readable = " ".join(names.get(word.lower(), word.capitalize()) for word in words if word)
    rendered["title"] = f"Microsoft Learn: {readable}"
    return rendered


def _lower_sentence_start(value: Any) -> str:
    text = str(value)
    return f"{text[:1].lower()}{text[1:]}" if text else text


def _sentence(value: Any) -> str:
    text = str(value).strip()
    if not text:
        return text
    if text.endswith(("!", "?")):
        return text
    return f"{text.rstrip('.')}."


def _normalize_content(content: dict[str, Any]) -> dict[str, Any]:
    normalized = deepcopy(content)
    normalized["sources"] = [
        _descriptive_source_title(source) for source in normalized.get("sources", [])
    ]
    generic_evidence = {
        "checkpoint id and utc time",
        "redacted object/resource id",
        "queried expected property",
        "negative-check result",
    }
    for task in normalized.get("tasks", []):
        evidence = {str(item).strip().casefold() for item in task.get("evidence", [])}
        if evidence == generic_evidence or {
            "checkpoint id and utc time",
            "negative-check result",
        }.intersection(evidence):
            title = str(task["title"]).rstrip(".")
            task["evidence"] = [
                f"`{task['id']}` UTC result for {_lower_sentence_start(title)}.",
                f"Exact run-owned ID and asserted service properties from: {task['positiveExpected']}",
                f"Negative-boundary outcome from: {task['negativeExpected']}",
                f"Cleanup dependency recorded for the objects created or configured by {task['id']}.",
            ]
    return normalized


def _lab_contract(old: dict[str, Any], content: dict[str, Any], number: str) -> dict[str, Any]:
    domain = DOMAIN_IDS[number]
    checkpoint_ids = [task["id"] for task in content["tasks"]]
    cost = deepcopy(old.get("cost") or {})
    cost_class = content.get("costClass", cost.get("class", "none"))
    cost_ack = cost_class in {"moderate", "elevated"}
    tenant_changes = list(old.get("tenantScopedChanges") or [])
    for change in content.get("tenantScopedChanges") or []:
        if change not in tenant_changes:
            tenant_changes.append(change)
    tenant_ack = bool(tenant_changes)
    providers = old.get("providers") or {}
    sources = content.get("sources") or [{"title": "Microsoft AZ-104 study guide", "url": STUDY_GUIDE}]
    checkpoints = []
    for index, task in enumerate(content["tasks"], start=1):
        checkpoint_id = task["id"]
        dependencies = checkpoint_ids[index:]
        checkpoints.append(
            {
                "id": checkpoint_id,
                "title": task["title"],
                "purpose": task["purpose"],
                "objectiveIds": task["objectiveIds"],
                "required": bool(task.get("required", True)),
                "expectedState": task["expectedState"],
                "scriptMarkers": {"setup": checkpoint_id, "validate": checkpoint_id, "cleanup": checkpoint_id},
                "validation": {
                    "positive": {"id": f"cp{index:02d}.positive", "description": f"Read the service properties for {_lower_sentence_start(task['title'])} by using exact run-owned identifiers.", "command": f"$validationId='{checkpoint_id}-positive'; {task['positiveCommand']}", "expected": task["positiveExpected"]},
                    "negative": {"id": f"cp{index:02d}.negative", "description": f"Search for conflicting, unowned, or excessive state after {_lower_sentence_start(task['title'])}.", "command": f"$validationId='{checkpoint_id}-negative'; {task['negativeCommand']}", "expected": task["negativeExpected"]},
                },
                "cleanup": {
                    "dependsOn": dependencies,
                    "action": f"Remove only manifest-recorded objects owned by {checkpoint_id}, after dependent checkpoints are clear.",
                    "residualCheck": {"id": f"cp{index:02d}.residual", "description": f"Prove no active managed object remains for {checkpoint_id}.", "command": "az resource list --resource-group $ResourceGroupName --query '[].id' --output tsv", "expected": "No active manifest-managed object remains for this checkpoint."},
                },
                "remediation": {"anchor": f"task-{index}", "links": sources[:2]},
            }
        )
    creates = deepcopy(old.get("creates") or {})
    creates.setdefault("azureResources", [])
    creates.setdefault("entraObjects", [])
    creates["localArtifacts"] = [".state/<run-id>/run.json", ".state/<run-id>/validation.json", ".state/<run-id>/cleanup.json"]
    preflight = [
        {"id": "preflight.context", "type": "context", "required": True, "description": "Confirm active cloud, tenant, and subscription without changing them.", "command": "az account show --output json", "expected": "Active context matches the supplied subscription and disposable environment."},
        {"id": "preflight.tools", "type": "tool", "required": True, "description": "Confirm PowerShell, Azure CLI, and az bicep are available.", "command": "az version; az bicep version", "expected": "All required tools meet the versions declared by this lab."},
        {"id": "preflight.inputs", "type": "input", "required": True, "description": "Check required parameters and environment gates without printing secrets.", "command": "$PSBoundParameters.Keys; Get-ChildItem Env:AZ104_* | Select-Object Name", "expected": "Every required input is present and optional gates are explicitly reported."},
        {"id": "preflight.providers", "type": "provider", "required": bool(providers.get("observed") or providers.get("required")), "description": "Read registration state for required resource providers.", "command": "az provider show --namespace <provider> --query registrationState --output tsv", "expected": "Every required provider is Registered; preflight performs no registration."},
        {"id": "preflight.region", "type": "region", "required": number != "00", "description": "Confirm the requested region is available to the subscription.", "command": "az account list-locations --query \"[?name=='<location>'].name\" --output tsv", "expected": "The supplied region appears in the subscription location inventory."},
    ]
    if domain in {"compute", "monitor-recovery", "capstone"}:
        preflight.extend(
            [
                {"id": "preflight.quota", "type": "quota", "required": cost_class in {"moderate", "elevated"}, "description": "Read regional compute usage before deployment.", "command": "az vm list-usage --location <location> --output table", "expected": "Required regional vCPU quota has safe headroom."},
                {"id": "preflight.sku", "type": "sku", "required": cost_class in {"moderate", "elevated"}, "description": "Read available VM or service SKUs in the selected region.", "command": "az vm list-skus --location <location> --all --output table", "expected": "The documented lab SKU has no blocking regional restriction."},
            ]
        )
    for authored_check in content.get("preflightChecks") or []:
        preflight.append(
            {
                "id": str(authored_check["id"]),
                "type": str(authored_check.get("type", "sku")),
                "required": bool(authored_check.get("required", True)),
                "description": str(authored_check["description"]),
                "command": str(authored_check["command"]),
                "expected": str(authored_check["expected"]),
            }
        )
    return {
        "schemaVersion": "2.0.0",
        "id": old["id"],
        "slug": old["slug"],
        "title": old["title"],
        "blueprintVersion": BLUEPRINT_DATE,
        "domain": domain,
        "objectives": list(old.get("objectives") or []),
        "track": "azure-cli-bicep" if number in {"10", "26"} else "azure-cli",
        "status": "offline-validated",
        "testedToolVersions": {"azureCli": ">=2.88.0", "powershell": ">=7.4"},
        "estimatedMinutes": old.get("estimatedMinutes", 120),
        "difficulty": {"beginner": "foundational", "intermediate": "applied", "foundational": "foundational", "applied": "applied", "advanced": "advanced"}.get(old.get("difficulty"), "applied"),
        "experience": {"scenario": content.get("scenario") or f"{str(content['role']).rstrip('.')} is responding to an operational request: {content['outcome']}", "role": content["role"], "outcome": content["outcome"], "completionCriteria": content["completionCriteria"]},
        "cost": {"class": cost_class, "billableResources": list(content.get("billableResources") or cost.get("billableResources") or []), "notes": content.get("costNotes") or cost.get("notes") or "Review current pricing and remove resources promptly.", "pricingLinks": _pricing_link(domain), "acknowledgementRequired": cost_ack},
        "permissions": deepcopy(old.get("permissions") or {"azureRbacRoles": [], "entraRoles": [], "graphScopes": []}),
        "prerequisites": list(old.get("prerequisites") or []),
        "providers": {
            "required": list(dict.fromkeys(list(providers.get("required") or providers.get("observed") or []) + list(content.get("requiredProviders") or []))),
            "optional": list(providers.get("optional") or []),
            "registeredByLab": [],
        },
        "inputs": _input_contract(number, checkpoint_ids),
        "acknowledgements": {
            "cost": {"required": cost_ack, "parameter": "AcknowledgeCost", "message": "I reviewed current pricing, quota, and the same-session cleanup plan."},
            "tenantChange": {"required": tenant_ack, "parameter": "AcknowledgeTenantChange", "message": "I am authorized to create or change the declared tenant-scoped objects and will restore recorded settings."},
        },
        "creates": creates,
        "tenantScopedChanges": tenant_changes,
        "externalRequirements": list(old.get("externalRequirements") or []),
        "preflightChecks": preflight,
        "checkpoints": checkpoints,
        "validation": {"script": "scripts/cli/Validate.ps1", "artifact": ".state/<run-id>/validation.json", "modes": ["Deployment", "PostCleanup"], "resultPolicy": {"requiredFailureResult": "fail", "optionalSkipResult": "partial", "allRequiredPassResult": "pass"}},
        "cleanup": {"script": "scripts/cli/Cleanup.ps1", "artifact": ".state/<run-id>/cleanup.json", "previewByDefault": True, "requiresExecuteFlag": True, "ownershipVerification": {"manifestIdMatch": True, "requiredTags": ["purpose", "labId", "runId"] if number not in {"00", "01", "02"} else []}, "residualChecks": [checkpoint["cleanup"]["residualCheck"] for checkpoint in checkpoints], "retainedItemsAllowed": True, "irreversiblePurge": "never"},
        "assessment": deepcopy(old.get("assessment") or {"enabled": False, "questionCount": 0}),
        "lastOfflineValidated": OFFLINE_DATE,
        "lastLiveVerified": None,
    }


def _ps_literal(value: str) -> str:
    return _powershell_ascii(value).replace("'", "''")


def _ps_array(values: list[str], indent: str = "    ") -> str:
    if not values:
        return "@()"
    return "@(\n" + "\n".join(f"{indent}'{_ps_literal(value)}'" for value in values) + "\n)"


def _powershell_header(parameters: str) -> str:
    return f"""#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
{parameters}
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {{
    throw 'Azure CLI is required. Run the repository readiness initializer, then retry.'
}}
"""


def _preflight_probe(check: dict[str, Any]) -> str:
    """Render an authored read-only preflight assertion as a recorded check."""
    check_id = _ps_literal(str(check["id"]))
    command = _transformed_command(str(check["command"])).rstrip()
    required = "$true" if bool(check.get("required", True)) else "$false"
    return f"""
$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {{
    $LASTEXITCODE = 0
    & {{
{command}
    }} | Out-Null
    if ($LASTEXITCODE -ne 0) {{ throw "native exit code $LASTEXITCODE" }}
}} catch {{
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}}
Add-PreflightResult -Id '{check_id}' -Required {required} -Passed $probePassed -Actual $probeActual
"""


def _preflight_script(contract: dict[str, Any], content: dict[str, Any], number: str) -> str:
    required_inputs = [
        item for item in contract["inputs"]
        if item["required"] and item.get("environmentVariable") and item["source"] == "environment"
    ]
    required_env = _ps_array([item["environmentVariable"] for item in required_inputs])
    providers = _ps_array(contract["providers"]["required"])
    authored_checks = list(content.get("preflightChecks") or [])
    presence_gates = sorted(
        {
            str(variable)
            for task in content["tasks"]
            for variable in (task.get("gateEnvironmentVariables") or [])
        }
    )
    exact_gates = {
        str(variable): str(expected)
        for task in content["tasks"]
        for variable, expected in (task.get("gateEnvironmentValues") or {}).items()
    }
    needs_azcopy = number in {"08", "09"}
    needs_compute = DOMAIN_IDS[number] in {"compute", "monitor-recovery", "capstone"}
    params = """    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZ104_SECONDARY_LOCATION"""
    body = _powershell_header(params)
    body += f"""
$account = az account show --output json | ConvertFrom-Json
if (-not $account) {{ throw 'No active Azure CLI context. Run az login deliberately before this lab.' }}
if ($SubscriptionId -and [string]$account.id -ne $SubscriptionId) {{
    throw "Context mismatch: active subscription is $($account.id), expected $SubscriptionId. Preflight will not switch it."
}}
if (-not $SubscriptionId) {{ $SubscriptionId = [string]$account.id }}
# The account read above is the mandatory context gate. All remaining Azure
# probes are collected as results instead of allowing one unavailable SKU or
# provider query to abort the readiness report before it can explain the gap.
$PSNativeCommandUseErrorActionPreference = $false
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$ResourceGroupName = $(if ('{number}' -in @('00', '01', '02')) {{ $null }} else {{ "rg-az104-l{number}-$RunId" }})

$checks = [System.Collections.Generic.List[object]]::new()
function Add-PreflightResult {{
    param([string]$Id, [bool]$Required, [bool]$Passed, [string]$Actual)
    $checks.Add([pscustomobject]@{{ id = $Id; required = $Required; passed = $Passed; actual = $Actual }})
}}

Add-PreflightResult -Id 'context' -Required $true -Passed $true -Actual "cloud=$($account.environmentName); tenant=<redacted>; subscription=<redacted>"
$azVersion = (az version --query '"azure-cli"' --output tsv)
$bicepVersion = (az bicep version 2>&1 | Out-String).Trim()
Add-PreflightResult -Id 'azure-cli' -Required $true -Passed ([bool]$azVersion) -Actual $azVersion
Add-PreflightResult -Id 'powershell' -Required $true -Passed ($PSVersionTable.PSVersion -ge [version]'7.4') -Actual $PSVersionTable.PSVersion.ToString()
Add-PreflightResult -Id 'bicep' -Required $true -Passed ([bool]$bicepVersion) -Actual $bicepVersion

$requiredEnvironmentVariables = {required_env}
foreach ($variableName in $requiredEnvironmentVariables) {{
    $present = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable($variableName))
    Add-PreflightResult -Id "input:$variableName" -Required $true -Passed $present -Actual $(if ($present) {{ 'present (value redacted)' }} else {{ 'missing' }})
}}

$providers = {providers}
foreach ($provider in $providers) {{
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    Add-PreflightResult -Id "provider:$provider" -Required $true -Passed ($registrationState -eq 'Registered') -Actual $(if ($registrationState) {{ $registrationState }} else {{ 'Unavailable' }})
}}

$knownLocation = az account list-locations --query "[?name=='$Location'].name | [0]" --output tsv
Add-PreflightResult -Id 'region' -Required $true -Passed ($knownLocation -eq $Location) -Actual $(if ($knownLocation) {{ $knownLocation }} else {{ 'not available' }})
"""
    for variable in presence_gates:
        literal = _ps_literal(variable)
        body += f"""
$gatePresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('{literal}'))
Add-PreflightResult -Id 'optional-gate:{literal}' -Required $false -Passed $gatePresent -Actual $(if ($gatePresent) {{ 'present (value redacted)' }} else {{ 'absent; checkpoint will be skipped' }})
"""
    for variable, expected in exact_gates.items():
        variable_literal = _ps_literal(variable)
        expected_literal = _ps_literal(expected)
        body += f"""
$gateMatches = [string]::Equals([Environment]::GetEnvironmentVariable('{variable_literal}'), '{expected_literal}', [StringComparison]::Ordinal)
Add-PreflightResult -Id 'optional-gate:{variable_literal}' -Required $false -Passed $gateMatches -Actual $(if ($gateMatches) {{ 'exact affirmative value supplied (value redacted)' }} else {{ 'absent or not exact; checkpoint will be skipped' }})
"""
    if needs_compute:
        body += """
$usage = az vm list-usage --location $Location --output json 2>$null | ConvertFrom-Json
Add-PreflightResult -Id 'regional-compute-quota' -Required $false -Passed ($LASTEXITCODE -eq 0) -Actual "entries=$(@($usage).Count)"
"""
    if needs_azcopy:
        body += """
$azCopy = Get-Command azcopy -ErrorAction SilentlyContinue
Add-PreflightResult -Id 'azcopy' -Required $true -Passed ([bool]$azCopy) -Actual $(if ($azCopy) { $azCopy.Source } else { 'missing' })
"""
    authored_context = _transformed_command(str(content.get("preflightContext", ""))).rstrip()
    if authored_context:
        body += f"\n{authored_context}\n"
    for check in authored_checks:
        body += _preflight_probe(check)
    authored_assertions = _transformed_command(str(content.get("preflightAssertions", ""))).rstrip()
    if authored_assertions:
        body += f"\n{authored_assertions}\n"
    body += """
$checks | Format-Table -AutoSize
$failedRequired = @($checks | Where-Object { $_.required -and -not $_.passed })
if ($failedRequired.Count -gt 0) {
    throw "Preflight blocked: $($failedRequired.id -join ', ')"
}
Write-Host 'Preflight passed. It performed no sign-in, context switch, provider registration, or Azure mutation.'
"""
    return _marked(body, "powershell")


def _state_helpers(number: str) -> str:
    return f"""
function Save-RunState {{
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
}}

function Save-ExternalState {{
    foreach ($key in @($external.Keys)) {{
        $value = $external[$key]
        if ($null -eq $value -or $value -is [string] -or $value -is [ValueType]) {{
            $inputKey = 'external-' + (([string]$key -creplace '([a-z0-9])([A-Z])', '$1-$2') -replace '[^a-zA-Z0-9-]', '-').ToLowerInvariant()
            $state.inputs[$inputKey] = $value
        }}
    }}
    Save-RunState
}}

function Write-CheckpointState {{
    param([string]$CheckpointId, [string]$Status, [string]$Message)
    $entry = @($state.checkpointStates | Where-Object {{ $_.checkpointId -eq $CheckpointId }})[0]
    $entry.status = $Status
    $entry.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $entry.message = $Message
}}

function Add-ManagedObject {{
    param([string]$CheckpointId, [string]$Kind, [string]$Id, [string]$Name, [string]$Type, [string]$Scope, [string]$OwnershipMethod)
    if ([string]::IsNullOrWhiteSpace($Id)) {{ return }}
    $existing = @($state.managedObjects | Where-Object {{ $_.id -eq $Id }})
    if ($existing.Count -gt 0) {{ return }}
    $expectedTags = @{{}}
    if ($OwnershipMethod -eq 'manifest-id-and-tags') {{
        $expectedTags = @{{ purpose = 'az104-lab'; labId = '{number}'; runId = $RunId }}
    }}
    $state.managedObjects += @{{
        checkpointId = $CheckpointId
        kind = $Kind
        id = $Id
        name = $Name
        type = $Type
        scope = $Scope
        ownership = @{{ method = $OwnershipMethod; expectedTags = $expectedTags }}
        recordedAt = (Get-Date).ToUniversalTime().ToString('o')
        lifecycleStatus = 'active'
    }}
    Save-RunState
}}

function Sync-ManagedResource {{
    param([string]$CheckpointId)
    # The entire recovery inventory is best effort so a state-helper or Azure
    # query failure cannot mask the original mutation error. Every object that
    # can be recovered is still persisted immediately as it is discovered.
    $nativePreference = $PSNativeCommandUseErrorActionPreference
    $PSNativeCommandUseErrorActionPreference = $false
    try {{
        Save-ExternalState
        $resourceGroupNames = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
        if ($ResourceGroupName) {{ $null = $resourceGroupNames.Add([string]$ResourceGroupName) }}
        foreach ($key in @($external.Keys | Where-Object {{ [string]$_ -match '(?i)ResourceGroupName$' }})) {{
            if ($external[$key]) {{ $null = $resourceGroupNames.Add([string]$external[$key]) }}
        }}
        foreach ($groupName in $resourceGroupNames) {{
            $groupJson = az group show --subscription $SubscriptionId --name $groupName --output json 2>$null
            $group = $(if ($LASTEXITCODE -eq 0 -and $groupJson) {{ $groupJson | ConvertFrom-Json }} else {{ $null }})
            if ($group) {{
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) {{ 'LAB{number}-CP01' }} else {{ $CheckpointId }})
                Add-ManagedObject -CheckpointId $groupCheckpoint -Kind 'azure-resource' -Id ([string]$group.id) -Name ([string]$group.name) -Type 'Microsoft.Resources/resourceGroups' -Scope "/subscriptions/$SubscriptionId" -OwnershipMethod 'manifest-id-and-tags'
                $resourcesJson = az resource list --subscription $SubscriptionId --resource-group $groupName --output json 2>$null
                $resources = @($(if ($LASTEXITCODE -eq 0 -and $resourcesJson) {{ $resourcesJson | ConvertFrom-Json }} else {{ @() }}))
                foreach ($resource in $resources) {{
                    Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$resource.id) -Name ([string]$resource.name) -Type ([string]$resource.type) -Scope ([string]$group.id) -OwnershipMethod 'manifest-id-and-tags'
                }}
            }}
        }}
        if ($external.ContainsKey('groupId') -and $external.groupId) {{ Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$external.groupId) -Name 'lab-group' -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }}
        if ($external.ContainsKey('guestUserId') -and $external.guestUserId) {{ Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$external.guestUserId) -Name 'guest-user' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }}
        if ($external.ContainsKey('userIds')) {{
            foreach ($userId in @($external.userIds)) {{ Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$userId) -Name 'lab-user' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }}
        }}
        if ($external.ContainsKey('delegationRecordId') -and $external.delegationRecordId) {{
            Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$external.delegationRecordId) -Name ([string]$external.delegationRecordName) -Type 'Microsoft.Network/dnsZones/NS' -Scope ([string]$external.parentZoneId) -OwnershipMethod 'manifest-id'
        }}
        if ($external.ContainsKey('connectionMonitorId') -and $external.connectionMonitorId) {{
            Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$external.connectionMonitorId) -Name ([string]$external.connectionMonitorName) -Type 'Microsoft.Network/networkWatchers/connectionMonitors' -Scope ([string]$external.networkWatcherId) -OwnershipMethod 'manifest-id'
        }}
    }} catch {{
        Write-Warning "Recovery inventory for $CheckpointId was incomplete: $($_.Exception.Message)"
    }} finally {{
        $PSNativeCommandUseErrorActionPreference = $nativePreference
    }}
}}
"""


def _checkpoint_block(number: str, index: int, task: dict[str, Any]) -> str:
    checkpoint_id = task["id"]
    command = _transformed_command(task["command"])
    command = re.sub(r"(?m)^az extension add[^\n]*\n?", "", command)
    command = _instrument_setup_command(command, checkpoint_id)
    execution = f"""try {{
    Write-CheckpointState -CheckpointId '{checkpoint_id}' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = '{checkpoint_id}'
    Save-RunState

{_indent(command.rstrip(), 4)}

    Sync-ManagedResource -CheckpointId '{checkpoint_id}'
    Write-CheckpointState -CheckpointId '{checkpoint_id}' -Status 'pass' -Message '{_ps_literal(task['expectedState'])}'
    Save-RunState
}} catch {{
    Sync-ManagedResource -CheckpointId '{checkpoint_id}'
    Write-CheckpointState -CheckpointId '{checkpoint_id}' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}}"""
    gates = list(task.get("gateEnvironmentVariables") or [])
    exact_gates = dict(task.get("gateEnvironmentValues") or {})
    gate_clauses = [
            f"(-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('{_ps_literal(variable)}')))"
            for variable in gates
    ]
    gate_clauses.extend(
        f"[string]::Equals([Environment]::GetEnvironmentVariable('{_ps_literal(str(variable))}'), '{_ps_literal(str(expected))}', [StringComparison]::Ordinal)"
        for variable, expected in exact_gates.items()
    )
    if gate_clauses:
        gate_expression = " -and ".join(gate_clauses)
        if bool(task.get("required", True)):
            blocked = f"""Write-CheckpointState -CheckpointId '{checkpoint_id}' -Status 'fail' -Message 'Required input or exact authorization gate was not satisfied.'
    $state.status = 'failed'
    Save-RunState
    throw 'Required input or exact authorization gate was not satisfied.'"""
        else:
            blocked = f"""Write-CheckpointState -CheckpointId '{checkpoint_id}' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState"""
        execution = f"""if (-not ({gate_expression})) {{
    {blocked}
}} else {{
{execution}
}}"""
    return f"""# CHECKPOINT {checkpoint_id} BEGIN
{execution}
# CHECKPOINT {checkpoint_id} END
"""


def _setup_script(contract: dict[str, Any], content: dict[str, Any], number: str) -> str:
    cost_ack = "$true" if contract["acknowledgements"]["cost"]["required"] else "$false"
    tenant_ack = "$true" if contract["acknowledgements"]["tenantChange"]["required"] else "$false"
    params = """    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZ104_SECONDARY_LOCATION,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange,
    [switch]$Execute"""
    body = _powershell_header(params)
    body += f"""
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$ResourceGroupName = $(if ('{number}' -in @('00', '01', '02')) {{ $null }} else {{ "rg-az104-l{number}-$RunId" }})
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-{number} execution plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  command surface: Azure CLI hosted in PowerShell'
Write-Host '  state: run.json, validation.json, cleanup.json'
if (-not $Execute) {{
    Write-Host 'Preview only. Review context, inputs, cost, tenant scope, and cleanup before using -Execute.'
    return
}}
if ({cost_ack} -and -not $AcknowledgeCost) {{ throw 'This lab requires -AcknowledgeCost before execution.' }}
if ({tenant_ack} -and -not $AcknowledgeTenantChange) {{ throw 'This lab requires -AcknowledgeTenantChange before execution.' }}

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -RunId $RunId -Location $Location -SecondaryLocation $SecondaryLocation
if (Test-Path -LiteralPath $Manifest) {{ throw "State already exists at $Manifest. Choose a new run ID." }}
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) {{ $SubscriptionId = [string]$account.id }}
$now = (Get-Date).ToUniversalTime().ToString('o')
$state = @{{
    schemaVersion = '1.0.0'
    labId = 'LAB-{number}'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }}
    acknowledgements = @{{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }}
    inputs = @{{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }}
    checkpointStates = @(
{chr(10).join(f"        @{{ checkpointId = '{task['id']}'; required = ${str(bool(task.get('required', True))).lower()}; status = 'pending'; updatedAt = $now; message = 'Not started.' }}" for task in content['tasks'])}
    )
    managedObjects = @()
    originalSettings = @()
}}
$external = @{{}}
"""
    body += _state_helpers(number)
    body += """
# The manifest exists before the first Azure mutation.
Save-RunState
$state.status = 'setup-in-progress'
Save-RunState
"""
    if number not in {"00", "01", "02"}:
        body += f"""
$expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd')
try {{
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId={number} runId=$RunId expiresOn=$expiresOn --output none
}} catch {{
    Write-CheckpointState -CheckpointId 'LAB{number}-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}} finally {{
    Sync-ManagedResource -CheckpointId 'LAB{number}-CP01'
}}
"""
    for index, task in enumerate(content["tasks"], start=1):
        body += "\n" + _checkpoint_block(number, index, task)
    body += """
$skippedRequired = @($state.checkpointStates | Where-Object { $_.required -and $_.status -eq 'skipped' })
if ($skippedRequired.Count -gt 0) {
    $state.status = 'failed'
    Save-RunState
    throw "Required checkpoints were skipped: $($skippedRequired.checkpointId -join ', ')"
}
$skippedOptional = @($state.checkpointStates | Where-Object { -not $_.required -and $_.status -eq 'skipped' })
$state.status = $(if ($skippedOptional.Count -gt 0) { 'partial' } else { 'setup-complete' })
Save-RunState
Write-Host "Setup result: $($state.status). State: $Manifest"
Write-Host "Next: ./Validate.ps1 -RunId $RunId -Mode Deployment"
"""
    return _marked(body, "powershell")


def _validation_marker(task: dict[str, Any], use_service_checks: bool) -> str:
    checkpoint_id = task["id"]
    positive_probe = ""
    negative_probe = ""
    if use_service_checks:
        positive_command = _transformed_command(task["positiveCommand"]).rstrip()
        negative_command = _transformed_command(task["negativeCommand"]).rstrip()
        positive_probe = f"""
    # AUTHORED SERVICE ASSERTION: positive
    try {{
        $LASTEXITCODE = 0
        & {{
{positive_command}
        }} | Out-Null
        if ($LASTEXITCODE -ne 0) {{
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        }} else {{
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }}
    }} catch {{
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }}
"""
        negative_probe = f"""
    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {{
        $LASTEXITCODE = 0
        & {{
{negative_command}
        }} | Out-Null
        if ($LASTEXITCODE -ne 0) {{
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }}
    }} catch {{
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }}
"""
    return f"""# CHECKPOINT {checkpoint_id} BEGIN
$checkpointState = @($state.checkpointStates | Where-Object {{ $_.checkpointId -eq '{checkpoint_id}' }})[0]
$checkpointObjects = @($state.managedObjects | Where-Object {{ $_.checkpointId -eq '{checkpoint_id}' }})

if ($Mode -eq 'Deployment') {{
    if ($checkpointState.status -eq 'skipped') {{
        Add-ValidationCheck -Id '{checkpoint_id.lower()}.positive' -CheckpointId '{checkpoint_id}' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id '{checkpoint_id.lower()}.negative' -CheckpointId '{checkpoint_id}' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    }} else {{
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {{
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {{
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) {{ $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }}
        }} elseif ($managedObject.kind -eq 'azure-resource') {{
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) {{ $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }}
        }} elseif ($managedObject.kind -eq 'entra-object') {{
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) {{ $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }}
        }}
    }}
{positive_probe.rstrip()}
    Add-ValidationCheck -Id '{checkpoint_id.lower()}.positive' -CheckpointId '{checkpoint_id}' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object {{ $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) }})
{negative_probe.rstrip()}
    $negativePassed = $unsafe.Count -eq 0{(' -and $negativeProbePassed' if use_service_checks else '')}
    $negativeActual = "unsafeObjects=$($unsafe.Count)"{(' + "; $negativeProbeActual"' if use_service_checks else '')}
    Add-ValidationCheck -Id '{checkpoint_id.lower()}.negative' -CheckpointId '{checkpoint_id}' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }}
}} else {{
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {{
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {{
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) {{ $active.Add([string]$managedObject.id) }}
        }} elseif ($managedObject.kind -eq 'azure-resource') {{
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) {{ $active.Add([string]$managedObject.id) }}
        }} elseif ($managedObject.kind -eq 'entra-object') {{
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) {{ $active.Add([string]$managedObject.id) }}
        }}
    }}
    Add-ValidationCheck -Id '{checkpoint_id.lower()}.residual' -CheckpointId '{checkpoint_id}' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}}
# CHECKPOINT {checkpoint_id} END
"""


def _validate_script(contract: dict[str, Any], content: dict[str, Any], number: str) -> str:
    params = """    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment'"""
    body = _powershell_header(params)
    body += f"""
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$ValidationPath = Join-Path $StateDir 'validation.json'
if (-not (Test-Path -LiteralPath $Manifest)) {{ throw "Run manifest not found: $Manifest" }}
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -AsHashtable
if ($state.labId -ne 'LAB-{number}' -or $state.runId -ne $RunId) {{ throw 'Manifest ownership does not match this lab and run ID.' }}
$PSNativeCommandUseErrorActionPreference = $false
$accountJson = az account show --output json 2>$null
$account = $(if ($LASTEXITCODE -eq 0 -and $accountJson) {{ $accountJson | ConvertFrom-Json }} else {{ $null }})
if (-not $account -or [string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {{
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $actualContext = $(if ($account) {{ "tenant=$($account.tenantId); subscription=$($account.id)" }} else {{ 'active context unavailable' }})
    $contextFailure = @{{
        schemaVersion = '1.0.0'; labId = 'LAB-{number}'; runId = $RunId; mode = $Mode
        generatedAt = $capturedAt; result = 'fail'
        summary = @{{ required = 1; passed = 0; failed = 1; skipped = 0 }}
        checks = @(@{{ id = 'context.active'; checkpointId = 'LAB{number}-CP01'; kind = 'context'; required = $true; status = 'fail'; message = 'Active Azure context does not match the run manifest.'; evidence = @{{ command = 'az account show --output json'; expected = 'tenant and subscription exactly match run.json'; actual = $actualContext; capturedAt = $capturedAt; redacted = $true }} }})
    }}
    $contextFailure | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
    Write-Host "Validation $Mode result: fail"
    Write-Host "Artifact: $ValidationPath"
    exit 1
}}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('{number}' -in @('00', '01', '02')) {{ $null }} else {{ "rg-az104-l{number}-$RunId" }})
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
{_transformed_command(content.get('validationContext', '')).rstrip()}

$checks = [System.Collections.Generic.List[object]]::new()
function Add-ValidationCheck {{
    param([string]$Id, [string]$CheckpointId, [string]$Kind, [bool]$Required, [bool]$Passed, [string]$Command, [string]$Expected, [string]$Actual, [bool]$Skipped = $false)
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $checks.Add(@{{
        id = $Id
        checkpointId = $CheckpointId
        kind = $Kind
        required = $Required
        status = $(if ($Skipped) {{ 'skipped' }} elseif ($Passed) {{ 'pass' }} else {{ 'fail' }})
        message = $(if ($Skipped) {{ 'Optional gate was deliberately skipped.' }} elseif ($Passed) {{ 'Expected state observed.' }} else {{ 'Expected state was not observed.' }})
        evidence = @{{ command = $Command; expected = $Expected; actual = $Actual; capturedAt = $capturedAt; redacted = $true }}
    }})
}}
"""
    use_service_checks = True
    for task in content["tasks"]:
        body += "\n" + _validation_marker(task, use_service_checks)
    tail = """
$requiredChecks = @($checks | Where-Object { $_.required })
$failedChecks = @($checks | Where-Object { $_.status -eq 'fail' })
$requiredSkippedChecks = @($checks | Where-Object { $_.required -and $_.status -eq 'skipped' })
$skippedChecks = @($checks | Where-Object { $_.status -eq 'skipped' })
$result = if ($failedChecks.Count -gt 0 -or $requiredSkippedChecks.Count -gt 0) { 'fail' } elseif ($skippedChecks.Count -gt 0) { 'partial' } else { 'pass' }
$document = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-{number}'
    runId = $RunId
    mode = $Mode
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    result = $result
    summary = @{
        required = $requiredChecks.Count
        passed = @($checks | Where-Object { $_.status -eq 'pass' }).Count
        failed = $failedChecks.Count
        skipped = $skippedChecks.Count
    }
    checks = @($checks)
}
$document | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
Write-Host "Validation $Mode result: $result"
Write-Host "Artifact: $ValidationPath"
if ($result -eq 'fail') { exit 1 }
"""
    body += tail.replace("{number}", number)
    return _marked(body, "powershell")


def _cleanup_marker(checkpoint_id: str) -> str:
    return f"""# CHECKPOINT {checkpoint_id} BEGIN
$targets = @($state.managedObjects | Where-Object {{ $_.checkpointId -eq '{checkpoint_id}' -and $_.lifecycleStatus -eq 'active' }})
foreach ($target in $targets) {{
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{{ checkpointId = '{checkpoint_id}'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }}; status = $(if ($alreadyAbsent) {{ 'skipped' }} else {{ 'preview' }}); message = $(if ($alreadyAbsent) {{ 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' }} elseif ($Execute) {{ 'Pending removal through the dependency-safe ownership boundary.' }} else {{ 'Would remove this exact manifest-recorded target.' }}) }})
}}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT {checkpoint_id} END
"""


def _cleanup_script(contract: dict[str, Any], content: dict[str, Any], number: str) -> str:
    params = """    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [switch]$Execute"""
    body = _powershell_header(params)
    body += f"""
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$CleanupPath = Join-Path $StateDir 'cleanup.json'
if (-not (Test-Path -LiteralPath $Manifest)) {{ throw "Run manifest not found: $Manifest" }}
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -AsHashtable
$active = @($state.managedObjects | Where-Object {{ $_.lifecycleStatus -eq 'active' }})
function Write-CleanupRefusal {{
    param([string]$Message)
    $refusalActions = @($active | ForEach-Object {{
        @{{ checkpointId = [string]$_.checkpointId; targetId = [string]$_.id; targetType = [string]$_.type; ownership = @{{ method = [string]$_.ownership.method; verified = $false }}; status = 'failed'; message = $Message }}
    }})
    $refusal = @{{
        schemaVersion = '1.0.0'; labId = 'LAB-{number}'; runId = $RunId
        generatedAt = (Get-Date).ToUniversalTime().ToString('o')
        executionMode = $(if ($Execute) {{ 'execute' }} else {{ 'preview' }})
        result = $(if ($Execute) {{ 'fail' }} else {{ 'preview' }})
        ownershipVerified = $false; actions = $refusalActions
        residualChecks = @(@{{ id = 'ownership.refusal'; command = 'compare manifest, active context, exact IDs, and ownership proof'; expected = 'all ownership checks pass before mutation'; actual = $Message; status = $(if ($Execute) {{ 'fail' }} else {{ 'skipped' }}) }})
        activeManagedObjects = @($active | ForEach-Object id); retainedItems = @()
    }}
    $refusal | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
    throw $Message
}}
if ($state.labId -ne 'LAB-{number}' -or $state.runId -ne $RunId) {{
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: manifest lab ID or run ID does not match.'
}}
if ($Execute -and $active.Count -eq 0 -and $state.status -eq 'cleaned') {{
    $priorRetained = @()
    if (Test-Path -LiteralPath $CleanupPath) {{
        try {{ $priorRetained = @((Get-Content -LiteralPath $CleanupPath -Raw | ConvertFrom-Json).retainedItems) }} catch {{ $priorRetained = @() }}
    }}
    $idempotent = @{{
        schemaVersion = '1.0.0'; labId = 'LAB-{number}'; runId = $RunId
        generatedAt = (Get-Date).ToUniversalTime().ToString('o'); executionMode = 'execute'; result = 'pass'
        ownershipVerified = $true; actions = @(); activeManagedObjects = @(); retainedItems = $priorRetained
        residualChecks = @(@{{ id = 'cleanup.idempotent'; command = 'read run.json active managed-object inventory'; expected = 'zero active manifest-managed objects'; actual = 'active=0; prior cleanup already completed'; status = 'pass' }})
    }}
    $idempotent | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
    Write-Host 'Cleanup result: pass (already cleaned)'
    Write-Host "Artifact: $CleanupPath"
    return
}}
try {{
    $account = az account show --output json | ConvertFrom-Json
}} catch {{
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: active Azure context could not be read.'
}}
if ([string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {{
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: active context does not match the manifest.'
}}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('{number}' -in @('00', '01', '02')) {{ $null }} else {{ "rg-az104-l{number}-$RunId" }})
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
{_transformed_command(content.get('cleanupContext', '')).rstrip()}

$ownershipVerified = $true
$verifiedOwnershipById = @{{}}
$absentIds = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$verifiedResourceGroupIds = [System.Collections.Generic.List[string]]::new()
$resourceGroupObjects = @($active | Where-Object {{ $_.type -eq 'Microsoft.Resources/resourceGroups' }})
$resourceGroupObject = $resourceGroupObjects | Select-Object -First 1
$nativeProbePreference = $PSNativeCommandUseErrorActionPreference
$PSNativeCommandUseErrorActionPreference = $false

# A manifest entry is necessary but is not, by itself, proof of ownership. Verify
# each manifest-id-and-tags boundary against the live Azure tags before mutation.
foreach ($groupObject in $resourceGroupObjects) {{
    $groupVerified = $false
    try {{
        $tagJson = az group show --ids $groupObject.id --query tags --output json 2>$null
        if ($LASTEXITCODE -eq 0 -and $tagJson) {{
            $tags = $tagJson | ConvertFrom-Json -AsHashtable
            $expectedTags = $groupObject.ownership.expectedTags
            $groupVerified =
                $groupObject.ownership.method -eq 'manifest-id-and-tags' -and
                [string]$tags['purpose'] -eq [string]$expectedTags['purpose'] -and
                [string]$tags['labId'] -eq [string]$expectedTags['labId'] -and
                [string]$tags['runId'] -eq [string]$expectedTags['runId'] -and
                [string]$tags['purpose'] -eq 'az104-lab' -and
                [string]$tags['labId'] -eq '{number}' -and
                [string]$tags['runId'] -eq $RunId
        }} else {{
            $groupExists = az group exists --subscription $state.context.subscriptionId --name $groupObject.name --output tsv 2>$null
            if ($LASTEXITCODE -eq 0 -and $groupExists -eq 'false') {{
                $null = $absentIds.Add([string]$groupObject.id)
                $groupVerified = $true
            }}
        }}
    }} catch {{
        $groupVerified = $false
    }}
    $verifiedOwnershipById[[string]$groupObject.id] = $groupVerified
    if ($groupVerified) {{ $verifiedResourceGroupIds.Add([string]$groupObject.id) }}
    if (-not $groupVerified) {{ $ownershipVerified = $false }}
}}

foreach ($object in $active) {{
    $objectId = [string]$object.id
    if ($verifiedOwnershipById.ContainsKey($objectId)) {{ continue }}
    $method = [string]$object.ownership.method
    $objectVerified = $false

    $absentGroupBoundary = @($resourceGroupObjects | Where-Object {{
        $absentIds.Contains([string]$_.id) -and $objectId.StartsWith("$($_.id)/", [System.StringComparison]::OrdinalIgnoreCase)
    }}).Count -gt 0
    if ($absentGroupBoundary) {{
        $null = $absentIds.Add($objectId)
        $verifiedOwnershipById[$objectId] = $true
        continue
    }}

    if ($method -eq 'manifest-id-and-tags' -and $object.kind -eq 'azure-resource') {{
        $expectedTags = $object.ownership.expectedTags
        $manifestTagsMatch =
            [string]$expectedTags['purpose'] -eq 'az104-lab' -and
            [string]$expectedTags['labId'] -eq '{number}' -and
            [string]$expectedTags['runId'] -eq $RunId
        $verifiedByGroupBoundary = @($verifiedResourceGroupIds | Where-Object {{
            $objectId.StartsWith("$_/", [System.StringComparison]::OrdinalIgnoreCase)
        }}).Count -gt 0
        $verifiedByOwnTags = $false
        try {{
            $tagJson = az resource show --ids $objectId --query tags --output json 2>$null
            if ($LASTEXITCODE -eq 0 -and $tagJson) {{
                $tags = $tagJson | ConvertFrom-Json -AsHashtable
                $verifiedByOwnTags =
                    [string]$tags['purpose'] -eq [string]$expectedTags['purpose'] -and
                    [string]$tags['labId'] -eq [string]$expectedTags['labId'] -and
                    [string]$tags['runId'] -eq [string]$expectedTags['runId']
            }} elseif ($verifiedByGroupBoundary) {{
                $parentGroupObject = $resourceGroupObjects | Where-Object {{ $objectId.StartsWith("$($_.id)/", [System.StringComparison]::OrdinalIgnoreCase) }} | Select-Object -First 1
                $exactCount = az resource list --resource-group $parentGroupObject.name --query "[?id=='$objectId'] | length(@)" --output tsv 2>$null
                if ($LASTEXITCODE -eq 0 -and [int]$exactCount -eq 0) {{
                    $null = $absentIds.Add($objectId)
                    $verifiedByOwnTags = $true
                }}
            }}
        }} catch {{
            $verifiedByOwnTags = $false
        }}
        $objectVerified = $manifestTagsMatch -and ($verifiedByOwnTags -or $verifiedByGroupBoundary)
    }} elseif ($method -eq 'manifest-id' -and $object.kind -eq 'azure-resource' -and $object.type -eq 'Microsoft.Management/managementGroups') {{
        try {{
            $managementGroupJson = az account management-group show --name $object.name --expand --recurse --output json 2>&1
            if ($LASTEXITCODE -eq 0) {{
                $managementGroup = $managementGroupJson | ConvertFrom-Json
                $objectVerified = [string]$managementGroup.id -eq $objectId -and @($managementGroup.children).Count -eq 0
            }} elseif ([string]$managementGroupJson -match '(?i)404|not.?found') {{
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }}
        }} catch {{
            $objectVerified = $false
        }}
    }} elseif ($method -eq 'manifest-id' -and $object.kind -eq 'entra-object') {{
        try {{
            $graphResult = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$objectId" --output none 2>&1
            if ($LASTEXITCODE -eq 0) {{
                $objectVerified = $true
            }} elseif ([string]$graphResult -match '(?i)404|Request_ResourceNotFound') {{
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }}
        }} catch {{
            $objectVerified = $false
        }}
    }} elseif ($method -eq 'manifest-id' -and $object.kind -eq 'azure-resource') {{
        try {{
            $resourceResult = az resource show --ids $objectId --output none 2>&1
            if ($LASTEXITCODE -eq 0) {{
                $objectVerified = $true
            }} elseif ([string]$resourceResult -match '(?i)404|ResourceNotFound|could not be found') {{
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }}
        }} catch {{
            $objectVerified = $false
        }}
    }} elseif ($method -eq 'local-path') {{
        try {{
            $candidate = if ([System.IO.Path]::IsPathRooted($objectId)) {{ $objectId }} else {{ Join-Path $LabRoot $objectId }}
            $fullPath = [System.IO.Path]::GetFullPath($candidate)
            $statePrefix = [System.IO.Path]::GetFullPath($StateDir).TrimEnd([System.IO.Path]::DirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
            $inStateBoundary = $fullPath.StartsWith($statePrefix, [System.StringComparison]::OrdinalIgnoreCase)
            $objectVerified = $inStateBoundary
            if ($inStateBoundary -and -not (Test-Path -LiteralPath $fullPath)) {{ $null = $absentIds.Add($objectId) }}
        }} catch {{
            $objectVerified = $false
        }}
    }}

    $verifiedOwnershipById[$objectId] = $objectVerified
    if (-not $objectVerified) {{ $ownershipVerified = $false }}
}}
$PSNativeCommandUseErrorActionPreference = $nativeProbePreference

if (-not $ownershipVerified) {{
    $failedOwnershipIds = @($active | Where-Object {{ -not $verifiedOwnershipById[[string]$_.id] }} | ForEach-Object id)
    Write-CleanupRefusal -Message "Cleanup ownership refusal: live ID and ownership proof failed for $($failedOwnershipIds -join ', ')."
}}

$actions = [System.Collections.Generic.List[object]]::new()
$residualChecks = [System.Collections.Generic.List[object]]::new()
if (-not $Execute) {{
    Write-Host 'Preview only. The exact manifest-owned targets below will not be changed.'
}}
"""
    for task in reversed(content["tasks"]):
        body += "\n" + _cleanup_marker(task["id"])
    pre_cleanup_command = _transformed_command(content.get("preCleanupCommand", "")).rstrip()
    residual_check_lines = "\n".join(
        f"$checkpointRemaining = @($remaining | Where-Object {{ $_ -in @($state.managedObjects | Where-Object {{ $_.checkpointId -eq '{task['id']}' }} | ForEach-Object id) }}); $residualChecks.Add(@{{ id = 'cp{index:02d}.residual'; command = 'query manifest-recorded IDs for {task['id']}'; expected = 'zero active objects for {task['id']}'; actual = \"active=$($checkpointRemaining.Count)\"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) {{ 'pass' }} elseif (-not $Execute) {{ 'skipped' }} else {{ 'fail' }}) }})"
        for index, task in enumerate(content["tasks"], start=1)
    )
    retained_item_lines = "\n".join(
        f"        @{{ id = {item['idExpression']}; type = '{_ps_literal(item['type'])}'; reason = '{_ps_literal(item['reason'])}'; expectedDisposition = '{_ps_literal(item['expectedDisposition'])}' }}"
        for item in content.get("retainedItems", [])
    )
    body += f"""
$cleanupFailure = $null
if ($Execute) {{
    $PSNativeCommandUseErrorActionPreference = $true
    $state.status = 'cleanup-in-progress'
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8

    try {{
        # Restore shared or tenant-wide settings before removing the disposable
        # objects that were used to exercise them.
        foreach ($setting in @($state.originalSettings)) {{
            if ($setting.targetId -eq 'authorizationPolicy' -and $setting.property -eq 'allowedToUseSSPR') {{
                $restoreBody = @{{ allowedToUseSSPR = [bool]$setting.value }} | ConvertTo-Json -Compress
                az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --headers 'Content-Type=application/json' --body $restoreBody --output none
                $restored = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowedToUseSSPR' --query allowedToUseSSPR --output tsv
                if ([bool]::Parse([string]$restored) -ne [bool]$setting.value) {{
                    throw 'Cleanup stopped because authorizationPolicy.allowedToUseSSPR was not restored.'
                }}
            }}
        }}
        foreach ($object in @($active | Where-Object {{ $_.type -eq 'Microsoft.Management/managementGroups' -and -not $absentIds.Contains([string]$_.id) }})) {{
            az account management-group delete --name $object.name --output none
        }}
        $hasLiveManagedTarget = @($active | Where-Object {{ -not $absentIds.Contains([string]$_.id) }}).Count -gt 0
        if ($hasLiveManagedTarget) {{
{pre_cleanup_command}
        }}
        foreach ($groupToDelete in @($resourceGroupObjects | Where-Object {{ -not $absentIds.Contains([string]$_.id) }})) {{
            az group delete --ids $groupToDelete.id --yes
        }}
        foreach ($object in @($active | Where-Object {{ $_.kind -eq 'entra-object' -and -not $absentIds.Contains([string]$_.id) }})) {{
            $collection = switch ([string]$object.type) {{
                'Microsoft.Graph/user' {{ 'users' }}
                'Microsoft.Graph/group' {{ 'groups' }}
                default {{ 'directoryObjects' }}
            }}
            az rest --method delete --url "https://graph.microsoft.com/v1.0/$collection/$($object.id)" --output none 2>$null
        }}
        foreach ($object in $state.managedObjects) {{
            $object.lifecycleStatus = 'deleted'
        }}
        foreach ($action in $actions) {{
            if ($action.status -eq 'skipped') {{ continue }}
            $action.status = 'deleted'
            $action.message = 'The exact manifest-recorded target was removed through its ownership boundary.'
        }}
    }} catch {{
        $cleanupFailure = "Cleanup mutation failed: $($_.Exception.GetType().Name)"
        foreach ($action in $actions) {{
            if ($action.status -eq 'preview') {{
                $action.status = 'failed'
                $action.message = $cleanupFailure
            }}
        }}
    }}
}}

$PSNativeCommandUseErrorActionPreference = $false
$remaining = [System.Collections.Generic.List[string]]::new()
foreach ($object in $state.managedObjects) {{
    if (-not $Execute -and $object.lifecycleStatus -eq 'active') {{ $remaining.Add([string]$object.id); continue }}
    if ($Execute -and $object.type -eq 'Microsoft.Management/managementGroups') {{
        $null = az account management-group show --name $object.name --output none 2>$null
        if ($LASTEXITCODE -eq 0) {{ $remaining.Add([string]$object.id) }}
    }} elseif ($Execute -and $object.type -eq 'Microsoft.Resources/resourceGroups') {{
        $groupExists = az group exists --subscription $SubscriptionId --name $object.name --output tsv 2>$null
        if ($LASTEXITCODE -ne 0 -or $groupExists -ne 'false') {{ $remaining.Add([string]$object.id) }}
    }} elseif ($Execute -and $object.kind -eq 'azure-resource') {{
        $null = az resource show --ids $object.id --output none 2>$null
        if ($LASTEXITCODE -eq 0) {{
            $remaining.Add([string]$object.id)
        }} elseif ($object.type -eq 'Microsoft.RecoveryServices/vaults' -and {('$true' if content.get('retainedItems') else '$false')}) {{
            $deletedVault = az backup deleted-vault get --location $Location --name $object.name --output json 2>$null
            if ($LASTEXITCODE -eq 0 -and $deletedVault) {{
                $object.lifecycleStatus = 'soft-deleted'
                foreach ($action in @($actions | Where-Object {{ [string]$_.targetId -eq [string]$object.id -and $_.status -ne 'skipped' }})) {{
                    $action.status = 'soft-deleted'
                    $action.message = 'The active ARM vault is absent and the exact recoverable deleted-vault record was confirmed; no purge was performed.'
                }}
            }} else {{
                $remaining.Add([string]$object.id)
            }}
        }}
    }} elseif ($Execute -and $object.kind -eq 'entra-object') {{
        $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($object.id)" --output none 2>$null
        if ($LASTEXITCODE -eq 0) {{ $remaining.Add([string]$object.id) }}
    }}
}}
$residualChecks.Clear()
{residual_check_lines}
if ($Execute -and $remaining.Count -gt 0) {{
    foreach ($object in $state.managedObjects) {{
        if ([string]$object.id -in @($remaining)) {{ $object.lifecycleStatus = 'active' }}
    }}
    foreach ($action in $actions) {{
        if ([string]$action.targetId -in @($remaining) -and $action.status -ne 'skipped') {{
            $action.status = 'failed'
            $action.message = 'Residual query found the target still active after cleanup.'
        }}
    }}
}}
$result = if (-not $Execute) {{ 'preview' }} elseif ($cleanupFailure -or $remaining.Count -gt 0) {{ 'fail' }} else {{ 'pass' }}
$cleanup = @{{
    schemaVersion = '1.0.0'
    labId = 'LAB-{number}'
    runId = $RunId
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    executionMode = $(if ($Execute) {{ 'execute' }} else {{ 'preview' }})
    result = $result
    ownershipVerified = $ownershipVerified
    actions = @($actions)
    residualChecks = @($residualChecks)
    activeManagedObjects = @($remaining)
    retainedItems = @(
{retained_item_lines}
    )
}}
$cleanup | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
if ($Execute) {{
    if ($result -eq 'pass') {{ $state.status = 'cleaned' }}
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
}}
Write-Host "Cleanup result: $result"
Write-Host "Artifact: $CleanupPath"
Write-Host 'Irreversible purge is never automated; retained or soft-deleted items must be documented explicitly.'
if ($result -eq 'fail') {{ exit 1 }}
"""
    return _marked(body, "powershell")


def _objective_titles() -> dict[str, str]:
    blueprint = yaml.safe_load((ROOT / "curriculum" / "blueprint.yml").read_text(encoding="utf-8"))
    titles = {item["id"]: item["title"] for item in blueprint.get("foundationObjectives", [])}
    for domain in blueprint.get("domains", []):
        for group in domain.get("groups", []):
            for objective in group.get("objectives", []):
                titles[objective["id"]] = objective["title"]
    return titles


def _navigation(labs: list[Path], index: int) -> str:
    links = ["[Catalog](../README.md)"]
    if index > 0:
        links.insert(0, f"[Previous: Lab {labs[index - 1].name[:2]}](../{labs[index - 1].name}/README.md)")
    if index < len(labs) - 1:
        links.append(f"[Next: Lab {labs[index + 1].name[:2]}](../{labs[index + 1].name}/README.md)")
    return " · ".join(links)


def _input_table(inputs: list[dict[str, Any]]) -> str:
    lines = [
        "| Input | Required | Source | Safe example | Gate behavior |",
        "|---|:---:|---|---|---|",
    ]
    for item in inputs:
        source = item["source"]
        if item.get("environmentVariable"):
            source += f" (`{item['environmentVariable']}`)"
        example = str(item["safeExample"]).replace("<", "&lt;").replace(">", "&gt;")
        lines.append(f"| `{item['id']}` — {item['description']} | {'Yes' if item['required'] else 'No'} | {source} | `{example}` | `{item['gateBehavior']}` |")
    return "\n".join(lines)


def _task_markdown(task: dict[str, Any], index: int) -> str:
    command = _transformed_command(task["command"])
    positive = _transformed_command(task["positiveCommand"])
    negative = _transformed_command(task["negativeCommand"])
    evidence = "\n".join(f"- {_sentence(item)}" for item in task["evidence"])
    return f"""## Task {index} — {task['title']} {{#task-{index}}}

Checkpoint: `{task['id']}`

Purpose and operational relevance: {task['purpose']} {task['operationalRelevance']}

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
{command.rstrip()}
```

Expected state: {task['expectedState']}

Representative redacted output:

```text
{task['representativeOutput']}
```

Positive validation:

```powershell
{positive.rstrip()}
```

Expected positive result: {task['positiveExpected']}

Negative validation:

```powershell
{negative.rstrip()}
```

Expected negative result: {task['negativeExpected']}

Evidence to retain:

{evidence}

Common failure and safe retry: {task['commonFailure']} {task['safeRetry']}

Cleanup dependency: {task['cleanupDependency']}
"""


def _readme(
    contract: dict[str, Any],
    content: dict[str, Any],
    number: str,
    navigation: str,
    scripts: dict[str, str],
    objective_titles: dict[str, str],
) -> str:
    objectives = "\n".join(
        f"| `{objective}` | {objective_titles.get(objective, 'Repository foundation objective')} | "
        + ", ".join(f"`{checkpoint['id']}`" for checkpoint in contract["checkpoints"] if objective in checkpoint["objectiveIds"])
        + " |"
        for objective in contract["objectives"]
    )
    decisions = "\n".join(f"- {decision}" for decision in content["designDecisions"])
    completion = "\n".join(f"- {criterion}" for criterion in contract["experience"]["completionCriteria"])
    task_sections = "\n\n".join(_task_markdown(task, index).rstrip() for index, task in enumerate(content["tasks"], start=1))
    sources = "\n".join(f"- [{source['title']}]({source['url']})" for source in content["sources"])
    assessment = (
        "Complete [QUESTIONS.md](assessment/QUESTIONS.md), then use [ANSWERS.md](assessment/ANSWERS.md) for option-by-option remediation. "
        "Scores of 85–100% indicate mastery, 70–84% indicate targeted review, and below 70% means repeat the mapped tasks."
        if contract["assessment"]["enabled"]
        else "This hands-on lab has no separate question set. Use the [domain assessment dashboard](../../docs/question-bank-index.md) to choose review questions."
    )
    appendix_parts = []
    for name in ("Preflight.ps1", "Setup.ps1", "Validate.ps1", "Cleanup.ps1"):
        appendix_parts.append(f"### `{name}`\n\n```powershell\n{scripts[name].rstrip()}\n```")
    appendix = "\n\n".join(appendix_parts)
    first_task = content["tasks"][0]
    if number == "00":
        final_inventory = """az group list --tag runId=az104l00-01 --query '[].{name:name,id:id}' --output table
Test-Path -LiteralPath './.state/az104l00-01/run.json'"""
        cleanup_query = "az group list --tag runId=az104l00-01 --query '[].id' --output tsv"
    else:
        final_inventory = f"az resource list --resource-group 'rg-az104-l{number}-az104l{number}-01' --query '[].{{name:name,type:type}}' --output table"
        cleanup_query = _transformed_command(content["tasks"][-1]["negativeCommand"])
    break_fix = content["breakFix"]
    break_fix_commands = ""
    if break_fix.get("injectCommand"):
        break_fix_commands += f"""

Inject the bounded fault:

```powershell
{_transformed_command(break_fix['injectCommand']).rstrip()}
```
"""
    if break_fix.get("diagnoseCommand"):
        break_fix_commands += f"""

Capture the failed state with a read-only query:

```powershell
{_transformed_command(break_fix['diagnoseCommand']).rstrip()}
```
"""
    if break_fix.get("repairCommand"):
        break_fix_commands += f"""

Repair only the injected setting, then repeat the same query:

```powershell
{_transformed_command(break_fix['repairCommand']).rstrip()}
{_transformed_command(break_fix.get('verifyCommand', break_fix['diagnoseCommand'])).rstrip()}
```
"""
    break_fix_commands = re.sub(r"\n{3,}", "\n\n", break_fix_commands).strip()
    break_fix_block = f"\n\n{break_fix_commands}" if break_fix_commands else ""
    body = f"""# Lab {number}: {contract['title']}

{navigation}

This self-contained lab uses Azure CLI commands hosted in PowerShell. Complete the guided lane or the automated lane—not both with the same run ID.

## Scenario, role, and outcome

Scenario: {contract['experience']['scenario']}

Learner role: {contract['experience']['role']}

Outcome: {contract['experience']['outcome']}

| Item | Value |
|---|---|
| Duration | {contract['estimatedMinutes']} minutes |
| Difficulty | {contract['difficulty']} |
| Cost class | `{contract['cost']['class']}` |
| Command surface | Azure CLI (`az`, `az rest`, Bicep, AzCopy, or KQL where required) hosted in PowerShell |
| Live state | Not executed during this offline rebuild |

Completion criteria:

{completion}

## Objectives and checkpoints

| Objective | Skill | Checkpoints |
|---|---|---|
{objectives}

The authoritative objective wording comes from the [Microsoft AZ-104 study guide]({STUDY_GUIDE}), skills measured as of {BLUEPRINT_DATE}.

## Architecture and service topology

![Lab {number} service topology](diagrams/architecture.svg)

The editable source is [architecture.mmd](diagrams/architecture.mmd). {content['architectureWalkthrough']}

## Concept primer and design decisions

{content['primer']}

Design decisions:

{decisions}

## Required and optional inputs

{_input_table(contract['inputs'])}

Secrets stay in temporary environment variables and are never written to `run.json`, validation evidence, or Git. A `skip-checkpoint` gate produces a visible partial result; it never becomes a pass.

## Read-only preflight

Sign in deliberately, inspect the active context, then run the lab preflight. It never signs in, changes context, installs an extension, registers a provider, or creates a resource.

```powershell
az login
az account show --query '{{cloud:environmentName,subscription:id,tenant:tenantId,user:user.name}}' --output json
./scripts/cli/Preflight.ps1 -SubscriptionId $env:AZ104_SUBSCRIPTION_ID -RunId 'az104l{number}-01' -Location 'westeurope'
```

Representative redacted output:

```text
context                 True  cloud=AzureCloud; tenant=<redacted>; subscription=<redacted>
azure-cli               True  2.88.x
provider:<namespace>    True  Registered
region                  True  westeurope
Preflight passed. It performed no Azure mutation.
```

If a required row fails, stop. Correct the local tool, context, provider, quota, SKU, region, permission, or input outside the lab, then rerun preflight.

{task_sections}

## Final validation and result interpretation

Run independent deployment validation after all required checkpoints:

```powershell
./scripts/cli/Validate.ps1 -RunId 'az104l{number}-01' -Mode Deployment
{final_inventory}
```

- `pass`: every required positive and negative check passed.
- `partial`: every required check passed, but at least one optional gate was deliberately skipped.
- `fail`: a required checkpoint failed; do not record the lab as complete.

Keep the redacted `validation.json`; do not retain credentials, tokens, access keys, certificate material, email addresses, tenant IDs, or unredacted command output.

## Deterministic break/fix exercise

Injection: {content['breakFix']['injection']}{break_fix_block}

Expected symptom: {content['breakFix']['symptom']}

Diagnose with a read-only service query:

```powershell
{_transformed_command(break_fix.get('diagnoseCommand', first_task['negativeCommand'])).rstrip()}
```

Diagnosis: {content['breakFix']['diagnosis']}

Repair: {content['breakFix']['repair']}

Before/after evidence must show the failed negative or positive check before repair and the same check passing afterward. Do not inject a second fault until the first is removed.

## Optional job-style challenge

{content['challenge']}

Deliver a short change record containing assumptions, exact commands, redacted evidence, cost and risk notes, rollback, and residual results. The challenge is optional and never changes required checkpoint status.

## Troubleshooting

| Symptom | Likely cause | Safe next step |
|---|---|---|
| Context mismatch | Active CLI context differs from `run.json` | Stop, inspect `az account show`, and select the intended disposable context yourself. |
| Provider or feature unavailable | Registration, region, feature, or SKU gate is unmet | Read the preflight result; do not register or enable tenant features implicitly. |
| Name already exists | The run ID is reused or a globally unique name collided | Keep existing state intact and choose a new run ID. |
| Expected state is delayed | The service is converging asynchronously | Repeat only the read-only query with bounded retries; do not duplicate creation. |
| Permission denied | Role, Graph scope, or data-plane authorization is insufficient | Confirm the declared least-privilege boundary; do not broaden access automatically. |
| Cleanup refuses ownership | ID, context, or tags differ from the manifest | Investigate the mismatch; never bypass ownership verification. |

## Cleanup and residual verification

Preview exact targets first, execute only after ownership review, then validate post-cleanup:

```powershell
./scripts/cli/Cleanup.ps1 -RunId 'az104l{number}-01'
./scripts/cli/Cleanup.ps1 -RunId 'az104l{number}-01' -Execute
./scripts/cli/Validate.ps1 -RunId 'az104l{number}-01' -Mode PostCleanup
{cleanup_query.rstrip()}
```

`cleanup.json` passes only when no active manifest-managed object remains. Soft-deleted or intentionally retained items must be listed with their reason and expected disposition. The lifecycle never performs irreversible purge automatically.

## Exam debrief and assessment

Explain why the expected state, negative check, and cleanup boundary matter—not only which command was used. Map any missed concept back to its task anchor before reviewing the answer key.

{assessment}

## Microsoft Learn sources

{sources}

## Lifecycle script appendix

The guided task blocks above and these executable scripts are generated from the same checkpoint data. The scripts are an optional automated lane; use a different run ID if you already completed the guided lane.

{appendix}

{navigation}
"""
    return _marked(body, "markdown")


def _fixtures(contract: dict[str, Any], number: str) -> dict[str, str]:
    created = "2026-08-31T10:00:00Z"
    run_id = f"fixture-{number}"
    subscription = "11111111-1111-4111-8111-111111111111"
    tenant = "22222222-2222-4222-8222-222222222222"
    managed = []
    for index, checkpoint in enumerate(contract["checkpoints"], start=1):
        if not checkpoint["required"]:
            continue
        if number == "00":
            kind, object_id, object_type, method, tags = "local-artifact", f".state/{run_id}/artifact-{index}.json", "local/state", "local-path", {}
        elif number in {"01", "02"}:
            kind, object_id, object_type, method, tags = "entra-object", f"33333333-3333-4333-8333-3333333333{index:02d}", "Microsoft.Graph/directoryObject", "manifest-id", {}
        else:
            kind = "azure-resource"
            object_id = f"/subscriptions/{subscription}/resourceGroups/rg-az104-l{number}-{run_id}/providers/Microsoft.Resources/deployments/cp{index}"
            object_type, method = "Microsoft.Resources/deployments", "manifest-id-and-tags"
            tags = {"purpose": "az104-lab", "labId": number, "runId": run_id}
        managed.append({"checkpointId": checkpoint["id"], "kind": kind, "id": object_id, "name": f"fixture-{number}-{index}", "type": object_type, "scope": None, "ownership": {"method": method, "expectedTags": tags}, "recordedAt": created, "lifecycleStatus": "active"})
    skipped_checkpoint_count = sum(1 for checkpoint in contract["checkpoints"] if not checkpoint["required"])
    run = {
        "schemaVersion": "1.0.0", "labId": f"LAB-{number}", "runId": run_id, "createdAt": created, "updatedAt": created, "status": ("partial" if skipped_checkpoint_count else "setup-complete"),
        "context": {"cloud": "AzureCloud", "tenantId": tenant, "subscriptionId": subscription},
        "acknowledgements": {"cost": contract["acknowledgements"]["cost"]["required"], "tenantChange": contract["acknowledgements"]["tenantChange"]["required"]},
        "inputs": {"location": "westeurope"},
        "checkpointStates": [{"checkpointId": checkpoint["id"], "required": checkpoint["required"], "status": ("pass" if checkpoint["required"] else "skipped"), "updatedAt": created, "message": ("Fixture checkpoint passed." if checkpoint["required"] else "Fixture optional gate skipped.")} for checkpoint in contract["checkpoints"]],
        "managedObjects": managed,
        "originalSettings": ([{"checkpointId": contract["checkpoints"][0]["id"], "targetId": tenant, "property": "tenant-change-baseline", "value": "recorded-before-mutation", "recordedAt": created}] if contract["tenantScopedChanges"] else []),
    }
    checks = []
    for checkpoint in contract["checkpoints"]:
        for kind in ("positive", "negative"):
            checks.append({"id": f"{checkpoint['id'].lower()}.{kind}", "checkpointId": checkpoint["id"], "kind": kind, "required": checkpoint["required"], "status": ("pass" if checkpoint["required"] else "skipped"), "message": ("Fixture expected state observed." if checkpoint["required"] else "Fixture optional gate skipped."), "evidence": {"command": f"fixture {kind} read-only query", "expected": "expected fixture state", "actual": ("observed fixture state" if checkpoint["required"] else "optional gate absent"), "capturedAt": created, "redacted": True}})
    required_check_count = sum(2 for checkpoint in contract["checkpoints"] if checkpoint["required"])
    skipped_check_count = 10 - required_check_count
    validation = {"schemaVersion": "1.0.0", "labId": f"LAB-{number}", "runId": run_id, "mode": "Deployment", "generatedAt": created, "result": ("partial" if skipped_check_count else "pass"), "summary": {"required": required_check_count, "passed": required_check_count, "failed": 0, "skipped": skipped_check_count}, "checks": checks}
    actions = [{"checkpointId": item["checkpointId"], "targetId": item["id"], "targetType": item["type"], "ownership": {"method": item["ownership"]["method"], "verified": True}, "status": "deleted", "message": "Fixture target removed after ownership verification."} for item in managed]
    residual_checks = [{"id": f"cp{index:02d}.residual", "command": f"query fixture IDs for {checkpoint['id']} after cleanup", "expected": "zero active objects", "actual": "active=0", "status": "pass"} for index, checkpoint in enumerate(contract["checkpoints"], start=1)]
    cleanup = {"schemaVersion": "1.0.0", "labId": f"LAB-{number}", "runId": run_id, "generatedAt": created, "executionMode": "execute", "result": "pass", "ownershipVerified": True, "actions": actions, "residualChecks": residual_checks, "activeManagedObjects": [], "retainedItems": []}
    return {
        "run.sample.json": json.dumps(run, indent=2) + "\n",
        "validation.sample.json": json.dumps(validation, indent=2) + "\n",
        "cleanup.sample.json": json.dumps(cleanup, indent=2) + "\n",
    }


def _contract_test(number: str, checkpoints: list[dict[str, Any]]) -> str:
    checkpoint_ids = [item["id"] for item in checkpoints]
    ids = ", ".join(f"'{item}'" for item in checkpoint_ids)
    optional_ids = [item["id"] for item in checkpoints if not item["required"]]
    optional = ", ".join(f"'{item}'" for item in optional_ids)
    body = fr"""#requires -Version 7.4
Describe 'LAB-{number} offline lifecycle contract' {{
    BeforeAll {{
        $script:LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
        $script:SetupSource = Get-Content -LiteralPath (Join-Path $script:LabRoot 'scripts/cli/Setup.ps1') -Raw
        $script:ValidateSource = Get-Content -LiteralPath (Join-Path $script:LabRoot 'scripts/cli/Validate.ps1') -Raw
        $script:CleanupSource = Get-Content -LiteralPath (Join-Path $script:LabRoot 'scripts/cli/Cleanup.ps1') -Raw
        $script:RunFixtureSource = Get-Content -LiteralPath (Join-Path $script:LabRoot 'tests/fixtures/run.sample.json') -Raw
        $script:ValidationFixture = Get-Content -LiteralPath (Join-Path $script:LabRoot 'tests/fixtures/validation.sample.json') -Raw | ConvertFrom-Json
        $script:CleanupFixture = Get-Content -LiteralPath (Join-Path $script:LabRoot 'tests/fixtures/cleanup.sample.json') -Raw | ConvertFrom-Json
        $script:CheckpointIds = @({ids})
        $script:OptionalCheckpointIds = @({optional})
        $script:ExpectedSubscriptionId = '11111111-1111-4111-8111-111111111111'
        $script:ExpectedTenantId = '22222222-2222-4222-8222-222222222222'

        function global:az {{
            throw 'Offline lifecycle contract blocked an unmocked Azure CLI call.'
        }}

        function New-LifecycleHarness {{
            param([Parameter(Mandatory)][string]$Root)
            $cli = Join-Path $Root 'scripts/cli'
            New-Item -ItemType Directory -Path $cli -Force | Out-Null
            foreach ($name in @('Setup.ps1', 'Preflight.ps1', 'Validate.ps1', 'Cleanup.ps1')) {{
                $source = Join-Path $script:LabRoot "scripts/cli/$name"
                $target = Join-Path $cli $name
                $text = Get-Content -LiteralPath $source -Raw
                # A failing generated script must fail this test, not terminate the
                # complete Pester process. Only the isolated harness copy is changed.
                $text = $text -replace '(?m)^\s*exit 1\s*$', "throw 'Lifecycle script reported failure.'"
                Set-Content -LiteralPath $target -Value $text -Encoding utf8
            }}
            return $cli
        }}

        function Write-HarnessRun {{
            param(
                [Parameter(Mandatory)][string]$HarnessRoot,
                [Parameter(Mandatory)][object]$Run
            )
            $stateDirectory = Join-Path $HarnessRoot ".state/$($Run.runId)"
            New-Item -ItemType Directory -Path $stateDirectory -Force | Out-Null
            $Run | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath (Join-Path $stateDirectory 'run.json') -Encoding utf8
            return $stateDirectory
        }}
    }}

    BeforeEach {{
        $script:HarnessRoot = Join-Path $TestDrive ([guid]::NewGuid().ToString('n'))
        $script:HarnessCli = New-LifecycleHarness -Root $script:HarnessRoot
        $script:HarnessSetup = Join-Path $script:HarnessCli 'Setup.ps1'
        $script:HarnessValidate = Join-Path $script:HarnessCli 'Validate.ps1'
        $script:HarnessCleanup = Join-Path $script:HarnessCli 'Cleanup.ps1'
        $global:Az104ContractAzCalls = 0
        $global:LASTEXITCODE = 0
        Mock az {{
            $global:Az104ContractAzCalls++
            $commandLine = @($args) -join ' '
            if ($commandLine -match '^account show(?:\s|$)') {{
                $global:LASTEXITCODE = 0
                return (@{{
                    id = '11111111-1111-4111-8111-111111111111'
                    tenantId = '22222222-2222-4222-8222-222222222222'
                    environmentName = 'AzureCloud'
                }} | ConvertTo-Json -Compress)
            }}
            # Every exact-object query reports absence. Post-cleanup validation
            # therefore proves residual reporting without reaching Azure.
            $global:LASTEXITCODE = 1
            return ''
        }}
    }}

    AfterAll {{
        Remove-Item -LiteralPath Function:\az -Force -ErrorAction SilentlyContinue
        Remove-Variable -Name Az104ContractAzCalls -Scope Global -ErrorAction SilentlyContinue
    }}

    It 'actually invokes Setup preview without Azure calls, mutations, or state' {{
        $runId = 'preview-{number}'
        $output = & $script:HarnessSetup -SubscriptionId $script:ExpectedSubscriptionId -RunId $runId -Location 'westeurope' 6>&1 | Out-String

        $output | Should -Match 'Preview only'
        (Join-Path $script:HarnessRoot ".state/$runId") | Should -Not -Exist
        $global:Az104ContractAzCalls | Should -Be 0
        Should -Invoke az -Times 0 -Scope It
    }}

    It 'asserts successful and denied checks are independent in the complete fixture' {{
        @($script:ValidationFixture.checks).Count | Should -Be ($script:CheckpointIds.Count * 2)
        foreach ($id in $script:CheckpointIds) {{
            $pair = @($script:ValidationFixture.checks | Where-Object checkpointId -eq $id)
            @($pair.kind | Sort-Object -Unique) | Should -Be @('negative', 'positive')
            @($pair | Where-Object required).Count | Should -Be $(if ($id -in $script:OptionalCheckpointIds) {{ 0 }} else {{ 2 }})
            @($pair | Where-Object {{ $_.required -and $_.status -ne 'pass' }}).Count | Should -Be 0
        }}
        $script:ValidateSource | Should -Match "-Kind 'positive'"
        $script:ValidateSource | Should -Match "-Kind 'negative'"
        $script:ValidateSource | Should -Match '\$failedChecks\.Count -gt 0'
    }}

    It 'persists recoverable state before mutation and across partial failure' {{
        $initialSave = $script:SetupSource.IndexOf('# The manifest exists before the first Azure mutation.')
        $firstCheckpoint = $script:SetupSource.IndexOf('# CHECKPOINT ' + $script:CheckpointIds[0] + ' BEGIN')
        $initialSave | Should -BeGreaterOrEqual 0
        $firstCheckpoint | Should -BeGreaterThan $initialSave
        $script:SetupSource.Substring($initialSave, $firstCheckpoint - $initialSave) | Should -Match 'Save-RunState'

        foreach ($id in $script:CheckpointIds) {{
            $pattern = '(?s)# CHECKPOINT ' + [regex]::Escape($id) + ' BEGIN(?<body>.*?)# CHECKPOINT ' + [regex]::Escape($id) + ' END'
            $block = [regex]::Match($script:SetupSource, $pattern).Groups['body'].Value
            $block | Should -Not -BeNullOrEmpty
            $block | Should -Match 'catch \{{'
            $block | Should -Match ("Sync-ManagedResource -CheckpointId '" + [regex]::Escape($id) + "'")
            $block | Should -Match "-Status 'fail'"
            $block | Should -Match "\$state.status = 'failed'"
            $block | Should -Match 'Save-RunState'
            $block | Should -Match 'throw'
        }}
    }}

    It 'models optional checkpoint skips as a partial deployment result' {{
        if ($script:OptionalCheckpointIds.Count -eq 0) {{
            $script:ValidationFixture.summary.skipped | Should -Be 0
            $script:ValidationFixture.result | Should -Be 'pass'
            return
        }}
        $script:ValidationFixture.result | Should -Be 'partial'
        $script:ValidationFixture.summary.skipped | Should -BeGreaterThan 0
        foreach ($id in $script:OptionalCheckpointIds) {{
            @($script:ValidationFixture.checks | Where-Object checkpointId -eq $id | Select-Object -ExpandProperty status -Unique) | Should -Be @('skipped')
        }}
    }}

    It 'actually invokes Cleanup ownership refusal against an isolated fixture copy' {{
        $run = $script:RunFixtureSource | ConvertFrom-Json
        $run.labId = 'LAB-mismatch'
        $stateDirectory = Write-HarnessRun -HarnessRoot $script:HarnessRoot -Run $run

        {{ & $script:HarnessCleanup -RunId $run.runId -Execute }} | Should -Throw '*Cleanup ownership refusal*'

        $artifact = Get-Content -LiteralPath (Join-Path $stateDirectory 'cleanup.json') -Raw | ConvertFrom-Json
        $artifact.result | Should -Be 'fail'
        $artifact.ownershipVerified | Should -BeFalse
        @($artifact.activeManagedObjects).Count | Should -Be @($run.managedObjects | Where-Object lifecycleStatus -eq 'active').Count
        @($artifact.actions | Where-Object status -ne 'failed').Count | Should -Be 0
        $global:Az104ContractAzCalls | Should -Be 0
        Should -Invoke az -Times 0 -Scope It
    }}

    It 'actually invokes PostCleanup validation and writes passing residual evidence' {{
        $run = $script:RunFixtureSource | ConvertFrom-Json
        $stateDirectory = Write-HarnessRun -HarnessRoot $script:HarnessRoot -Run $run

        $output = & $script:HarnessValidate -RunId $run.runId -Mode PostCleanup 6>&1 | Out-String

        $artifact = Get-Content -LiteralPath (Join-Path $stateDirectory 'validation.json') -Raw | ConvertFrom-Json
        $output | Should -Match 'Validation PostCleanup result: pass'
        $artifact.mode | Should -Be 'PostCleanup'
        $artifact.result | Should -Be 'pass'
        @($artifact.checks).Count | Should -Be $script:CheckpointIds.Count
        @($artifact.checks | Where-Object {{ $_.kind -ne 'residual' -or $_.status -ne 'pass' }}).Count | Should -Be 0
        @($artifact.checks | Where-Object {{ $_.evidence.actual -notmatch '^active=' }}).Count | Should -Be 0
        $global:Az104ContractAzCalls | Should -BeGreaterThan 0
        Should -Invoke az -Scope It
    }}

    It 'actually invokes idempotent Cleanup for an already-cleaned empty state' {{
        $run = $script:RunFixtureSource | ConvertFrom-Json
        $run.status = 'cleaned'
        foreach ($managedObject in @($run.managedObjects)) {{ $managedObject.lifecycleStatus = 'deleted' }}
        $stateDirectory = Write-HarnessRun -HarnessRoot $script:HarnessRoot -Run $run
        $script:CleanupFixture | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath (Join-Path $stateDirectory 'cleanup.json') -Encoding utf8

        $output = & $script:HarnessCleanup -RunId $run.runId -Execute 6>&1 | Out-String

        $artifact = Get-Content -LiteralPath (Join-Path $stateDirectory 'cleanup.json') -Raw | ConvertFrom-Json
        $persistedRun = Get-Content -LiteralPath (Join-Path $stateDirectory 'run.json') -Raw | ConvertFrom-Json
        $output | Should -Match 'already cleaned'
        $artifact.result | Should -Be 'pass'
        $artifact.ownershipVerified | Should -BeTrue
        @($artifact.actions).Count | Should -Be 0
        @($artifact.activeManagedObjects).Count | Should -Be 0
        @($artifact.residualChecks).Count | Should -Be 1
        $artifact.residualChecks[0].id | Should -Be 'cleanup.idempotent'
        $artifact.residualChecks[0].status | Should -Be 'pass'
        $persistedRun.status | Should -Be 'cleaned'
        $global:Az104ContractAzCalls | Should -Be 0
        Should -Invoke az -Times 0 -Scope It
    }}

    It 'retains a fully owned, residual-free successful cleanup fixture' {{
        $script:CleanupFixture.result | Should -Be 'pass'
        $script:CleanupFixture.ownershipVerified | Should -BeTrue
        @($script:CleanupFixture.activeManagedObjects).Count | Should -Be 0
        @($script:CleanupFixture.actions | Where-Object {{ -not $_.ownership.verified -or $_.status -notin @('deleted', 'soft-deleted', 'skipped') }}).Count | Should -Be 0
        @($script:CleanupFixture.residualChecks | Where-Object status -ne 'pass').Count | Should -Be 0
        $script:CleanupSource | Should -Match 'Irreversible purge is never automated'
    }}
}}
"""
    return body


def _accessible_svg(path: Path, title: str, number: str, check: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = text
    svg_match = re.search(r"<svg\b[^>]*>", updated)
    if not svg_match:
        print(f"FAIL  {path.relative_to(ROOT)} has no svg root")
        return False
    root_tag = svg_match.group(0)
    replacement = root_tag
    if not re.search(r"\brole=", replacement):
        replacement = replacement[:-1] + ' role="img">'
    if not re.search(r"\baria-labelledby=", replacement):
        replacement = replacement[:-1] + f' aria-labelledby="lab{number}-diagram-title lab{number}-diagram-desc">'
    updated = updated[: svg_match.start()] + replacement + updated[svg_match.end() :]
    insertion = ""
    if not re.search(r"<title(?:\s|>)", updated):
        insertion += f'<title id="lab{number}-diagram-title">{title} architecture</title>'
    if not re.search(r"<desc(?:\s|>)", updated):
        insertion += f'<desc id="lab{number}-diagram-desc">Service topology and validation boundary for AZ-104 Lab {number}.</desc>'
    if insertion:
        position = updated.find(">", updated.find("<svg")) + 1
        updated = updated[:position] + insertion + updated[position:]
    if updated == text:
        print(f"PASS  {path.relative_to(ROOT)} accessibility metadata")
        return True
    if check:
        print(f"FAIL  {path.relative_to(ROOT)} accessibility metadata is stale")
        return False
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(updated)
    print(f"WRITE {path.relative_to(ROOT)} accessibility metadata")
    return True


def _render_lab(
    lab_dir: Path,
    content: dict[str, Any],
    navigation: str,
    objective_titles: dict[str, str],
    check: bool,
) -> bool:
    number = lab_dir.name[:2]
    content = _independent_task_checks(_normalize_content(content))
    old = yaml.safe_load((lab_dir / "lab.yml").read_text(encoding="utf-8"))
    contract = _lab_contract(old, content, number)
    yaml_body = yaml.dump(contract, Dumper=_NoAliasDumper, sort_keys=False, width=120, allow_unicode=True)
    yaml_rendered = _marked(yaml_body, "yaml")
    yaml_existing = (lab_dir / "lab.yml").read_text(encoding="utf-8")
    yaml_expected = _update_marked(yaml_existing, yaml_rendered, "yaml")

    scripts = {
        "Preflight.ps1": _preflight_script(contract, content, number),
        "Setup.ps1": _setup_script(contract, content, number),
        "Validate.ps1": _validate_script(contract, content, number),
        "Cleanup.ps1": _cleanup_script(contract, content, number),
    }
    readme_rendered = _readme(contract, content, number, navigation, scripts, objective_titles)
    readme_existing = (lab_dir / "README.md").read_text(encoding="utf-8")
    readme_expected = _update_marked(readme_existing, readme_rendered, "markdown")

    results = [
        _write_or_check(lab_dir / "lab.yml", yaml_expected, check),
        _write_or_check(lab_dir / "README.md", readme_expected, check),
    ]
    for name, rendered in scripts.items():
        path = lab_dir / "scripts" / "cli" / name
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        expected = _update_marked(existing, rendered, "powershell")
        results.append(_write_or_check(path, expected, check))

    for name, rendered in _fixtures(contract, number).items():
        results.append(_write_or_check(lab_dir / "tests" / "fixtures" / name, rendered, check))
    results.append(_write_or_check(lab_dir / "tests" / "Contract.Tests.ps1", _contract_test(number, contract["checkpoints"]), check))
    results.append(_accessible_svg(lab_dir / "diagrams" / "architecture.svg", contract["title"], number, check))
    return all(results)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report drift without writing files")
    parser.add_argument("--only", nargs="*", help="Optional two-digit lab numbers")
    args = parser.parse_args()

    if not CONTENT_PATH.exists():
        print(f"ERROR {CONTENT_PATH.relative_to(ROOT)} is missing", file=sys.stderr)
        return 2
    catalog = yaml.safe_load(CONTENT_PATH.read_text(encoding="utf-8"))
    if catalog.get("schemaVersion") != "1.0.0" or not isinstance(catalog.get("labs"), dict):
        print("ERROR curriculum/lab-content.yml has an unsupported contract", file=sys.stderr)
        return 2

    lab_dirs = sorted(path for path in LABS_ROOT.glob("[0-9][0-9]-*") if path.is_dir())
    selected = set(args.only or [])
    if selected:
        lab_dirs = [path for path in lab_dirs if path.name[:2] in selected]
    objective_titles = _objective_titles()
    all_labs = sorted(path for path in LABS_ROOT.glob("[0-9][0-9]-*") if path.is_dir())
    positions = {path.name: index for index, path in enumerate(all_labs)}
    results = []
    for lab_dir in lab_dirs:
        content = catalog["labs"].get(lab_dir.name)
        if not content:
            print(f"FAIL  curriculum/lab-content.yml is missing {lab_dir.name}")
            results.append(False)
            continue
        results.append(_render_lab(lab_dir, content, _navigation(all_labs, positions[lab_dir.name]), objective_titles, args.check))
    return 0 if results and all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
