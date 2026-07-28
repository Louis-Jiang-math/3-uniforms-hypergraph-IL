#!/usr/bin/env python3
"""Fetch optional noncanonical upstream bytes without changing project status."""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "raw" / "upstream"
SOURCE_COMMIT = "cfadd24b52546d4d5800c4a3c5a75a2add86f928"
ITEMS = [
    (
        "chatgpt-export_数学语言描述_mathcal T_4图册(2).txt",
        f"https://raw.githubusercontent.com/Louis-Jiang-math/3-uniforms-hypergraph-IL/{SOURCE_COMMIT}/old/chatgpt-export_%E6%95%B0%E5%AD%A6%E8%AF%AD%E8%A8%80%E6%8F%8F%E8%BF%B0_mathcal%20T_4%E5%9B%BE%E5%86%8C%282%29.txt",
        424245,
    ),
    (
        "q0015_first_execution_results.original.json",
        f"https://raw.githubusercontent.com/Louis-Jiang-math/3-uniforms-hypergraph-IL/{SOURCE_COMMIT}/enumerate/q0015_first_execution_results.json",
        36960,
    ),
]


def atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    results = []
    for filename, url, expected_size in ITEMS:
        target = OUT / filename
        with urllib.request.urlopen(url, timeout=60) as response:
            data = response.read()
        atomic_write_bytes(target, data)
        results.append(
            {
                "file": str(target.relative_to(ROOT)),
                "bytes": len(data),
                "expected_bytes": expected_size,
                "size_matches": len(data) == expected_size,
                "sha256": hashlib.sha256(data).hexdigest(),
                "source_commit": SOURCE_COMMIT,
                "url": url,
                "status": "immutable optional raw source",
            }
        )
    payload = (json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    atomic_write_bytes(OUT / "fetch_results.json", payload)
    print(payload.decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
