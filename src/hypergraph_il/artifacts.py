from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

SOURCE_COMMIT = "cfadd24b52546d4d5800c4a3c5a75a2add86f928"


def canonical_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def payload_sha256(payload: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def build_artifact(
    payload: Mapping[str, Any],
    *,
    artifact_type: str,
    result_type: str,
    generator: str,
    command: str,
    parameters: Mapping[str, Any],
    scope: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    timestamp = generated_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "metadata": {
            "schema_version": "research-artifact-v1",
            "artifact_type": artifact_type,
            "result_type": result_type,
            "generator": generator,
            "command": command,
            "parameters": dict(parameters),
            "scope": scope,
            "source_commit": SOURCE_COMMIT,
            "generated_at": timestamp,
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "payload_sha256": payload_sha256(payload),
        },
        "payload": dict(payload),
    }


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def validate_artifact(value: Mapping[str, Any]) -> None:
    metadata = value.get("metadata")
    payload = value.get("payload")
    if not isinstance(metadata, Mapping) or not isinstance(payload, Mapping):
        raise ValueError("artifact requires metadata and payload objects")
    if metadata.get("schema_version") != "research-artifact-v1":
        raise ValueError("unsupported artifact schema")
    expected = metadata.get("payload_sha256")
    actual = payload_sha256(payload)
    if expected != actual:
        raise ValueError(f"payload hash mismatch: expected {expected}, got {actual}")
    if metadata.get("result_type") in {"timeout", "interrupted", "unresolved"} and metadata.get("artifact_type") == "proof":
        raise ValueError("inconclusive result cannot be typed as proof")
