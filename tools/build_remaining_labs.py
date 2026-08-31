#!/usr/bin/env python3
"""Compatibility entry point for the Azure CLI-only lab generator."""

from azure_cli_labs import main


if __name__ == "__main__":
    raise SystemExit(main())
