#!/usr/bin/env python3
"""Compatibility CLI wrapper for the Q-0015 auditor."""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hypergraph_il.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
