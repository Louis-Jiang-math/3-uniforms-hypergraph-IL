#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def require(path: str) -> Path:
    target = ROOT / path
    if not target.exists():
        ERRORS.append(f"missing required path: {path}")
    return target


required = [
    "README.md", "AGENTS.md", "agent.md", "WORKFLOW.md", "HANDOFF_CURRENT.md",
    "knowledge/FACTS.md", "knowledge/FAILURES.md", "knowledge/QUESTIONS.md",
    "knowledge/DECISIONS.md", "knowledge/DEFINITIONS.md",
    "docs/PROJECT_STATE.yaml", "docs/PROOF_DAG.md", "docs/QUICKSTART_10_MINUTES.md",
    "docs/changes/2026-07-28-general-workflow-restructure.md",
    "evidence/audits/REPOSITORY_AUDIT.md",
    "evidence/experiments/q0015/baselines/q0015_audit_results.json",
    "evidence/experiments/q0015/MANIFEST.json",
    "sources/raw/MANIFEST.json", "history/legacy-frameworks/single-defect-monolith.md",
    "src/hypergraph_il/artifacts.py", "src/hypergraph_il/cli.py",
    "enumerate/q0015_configuration_auditor.py", "tests/test_artifacts.py",
]
for item in required:
    require(item)


# Generic protocol must not contain project-specific status.
agent_text = require("agent.md").read_text(encoding="utf-8")
for token in ["Q-0015", "Q-0016", "Q-0017", "one-quarter theorem", "genealogy"]:
    if token in agent_text:
        ERRORS.append(f"generic agent.md contains project-specific token: {token}")

# Compatibility files must remain pointers, not duplicate authorities.
for pointer, canonical in [
    ("FACTS.md", "knowledge/FACTS.md"),
    ("FAILURES.md", "knowledge/FAILURES.md"),
    ("QUESTIONS.md", "knowledge/QUESTIONS.md"),
]:
    text = require(pointer).read_text(encoding="utf-8")
    if canonical not in text or len(text.splitlines()) > 8:
        ERRORS.append(f"{pointer} is not a short compatibility pointer")

state_text = require("docs/PROJECT_STATE.yaml").read_text(encoding="utf-8")
for expected in [
    "commit: cfadd24b52546d4d5800c4a3c5a75a2add86f928",
    "status: open", "id: G1c", "question: Q-0015", "question: Q-0017", "question: Q-0016",
]:
    if expected not in state_text:
        ERRORS.append(f"PROJECT_STATE.yaml missing: {expected}")

handoff = require("HANDOFF_CURRENT.md").read_text(encoding="utf-8")
if "G1c / Q-0015" not in handoff:
    ERRORS.append("handoff does not name the active node")
if re.search(r"Q-0016.{0,50}(closed|已证明|已关闭)", handoff, re.I):
    ERRORS.append("handoff overclaims Q-0016")
if re.search(r"Q-0017.{0,50}(closed|已证明|已关闭)", handoff, re.I):
    ERRORS.append("handoff overclaims Q-0017")
if re.search(r"^## .*update", handoff, re.I | re.M):
    ERRORS.append("handoff contains append-only update sections")

# Stable IDs must remain.
registries = "\n".join(require(path).read_text(encoding="utf-8") for path in [
    "knowledge/FACTS.md", "knowledge/FAILURES.md", "knowledge/QUESTIONS.md"
])
for token in ["F-0035", "F-0036", "A-0025", "A-0026", "Q-0015", "Q-0016", "Q-0017"]:
    if token not in registries:
        ERRORS.append(f"stable registry ID disappeared: {token}")

# Raw source files are represented in the manifest.
source_manifest = json.loads(require("sources/raw/MANIFEST.json").read_text(encoding="utf-8"))
manifested_entries = {entry["path"]: entry for entry in source_manifest.get("files", [])}
for path in (ROOT / "sources/raw/conversations").glob("*"):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT).as_posix()
    entry = manifested_entries.get(rel)
    if entry is None:
        ERRORS.append(f"raw source missing from manifest: {path.relative_to(ROOT)}")
        continue
    import hashlib
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if entry.get("sha256") != actual or entry.get("bytes") != path.stat().st_size:
        ERRORS.append(f"raw source manifest mismatch: {path.relative_to(ROOT)}")

# Generated baseline must use the artifact envelope.
baseline = json.loads(require("evidence/experiments/q0015/baselines/q0015_audit_results.json").read_text(encoding="utf-8"))
if baseline.get("metadata", {}).get("schema_version") != "research-artifact-v1":
    ERRORS.append("baseline does not use research-artifact-v1")
if baseline.get("metadata", {}).get("result_type") != "exhaustive-regression":
    ERRORS.append("baseline result type is not exhaustive-regression")

# Local Markdown links in current/canonical documents.
link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
canonical_paths = [
    ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "agent.md", ROOT / "WORKFLOW.md",
    ROOT / "HANDOFF_CURRENT.md",
    *sorted((ROOT / "knowledge").glob("*.md")),
    *sorted((ROOT / "docs").rglob("*.md")),
    *sorted((ROOT / "evidence").rglob("*.md")),
]
for path in canonical_paths:
    text = path.read_text(encoding="utf-8")
    for raw_target in link_pattern.findall(text):
        target = raw_target.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#", "sandbox:")):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            ERRORS.append(f"link escapes repository: {path.relative_to(ROOT)} -> {raw_target}")
            continue
        if not resolved.exists():
            ERRORS.append(f"broken link: {path.relative_to(ROOT)} -> {raw_target}")

if ERRORS:
    print("Repository consistency errors:")
    for error in ERRORS:
        print(f"- {error}")
    raise SystemExit(1)
print("repository consistency checks passed")
