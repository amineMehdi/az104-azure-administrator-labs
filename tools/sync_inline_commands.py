#!/usr/bin/env python3
"""Compatibility entry point for v2 lab and inline-command drift checks."""

from generate_labs import main


if __name__ == "__main__":
    raise SystemExit(main())
