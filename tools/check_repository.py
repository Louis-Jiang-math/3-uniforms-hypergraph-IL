#!/usr/bin/env python3
from __future__ import annotations

import hashlib
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
    "pyproject.toml", ".github/workflows/enumerate-smoke.yml",
    "FACTS.md", "FAILURES.md", "QUESTIONS.md",
    "PIVOT_SWITCH_ESCAPE_FRAMEWORK.md", "SINGLE_DEFECT_FRAMEWORK.md",
    "knowledge/FACTS.md", "knowledge/FAILURES.md", "knowledge/QUESTIONS.md",
    "knowledge/DECISIONS.md", "knowledge/DEFINITIONS.md",
    "docs/PROJECT_STATE.yaml", "docs/PROOF_DAG.md", "docs/QUICKSTART_10_MINUTES.md",
    "docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md",
    "evidence/audits/REPOSITORY_AUDIT.md",
    "evidence/proofs/ROUTE_B_REORIENTATION_AUDIT.md",
    "evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md",
    "evidence/experiments/route_b/MANIFEST.json",
    "evidence/experiments/route_b/baselines/route_b_lp_atlas_validation.json",
    "evidence/experiments/route_b/reports/q4_splice_pay_cylinder_validation.md",
    "evidence/experiments/route_b/reports/route_b_lp_atlas_validation.md",
    "evidence/experiments/q0015/baselines/q0015_audit_results.json",
    "evidence/experiments/q0015/MANIFEST.json",
    "sources/raw/MANIFEST.json", "history/legacy-frameworks/single-defect-monolith.md",
    "src/hypergraph_il/artifacts.py", "src/hypergraph_il/cli.py",
    "enumerate/q0015_configuration_auditor.py",
    "enumerate/q4_splice_pay_cylinder_validation.py",
    "enumerate/route_b_b3_reduced_core_search.py",
    "enumerate/route_b_lp_atlas_validation.py",
    "src/hypergraph_il/route_b_atlas.py",
    "tests/test_artifacts.py",
    "tests/test_route_b_atlas.py",
]
for item in required:
    require(item)


agent_path = require("agent.md")
agent_text = agent_path.read_text(encoding="utf-8")
agent_lines = len(agent_text.splitlines())
if agent_lines > 260:
    ERRORS.append(f"agent.md is too long: {agent_lines} lines (maximum 260)")
if "WORKFLOW.md" not in agent_text:
    ERRORS.append("agent.md must link the detailed WORKFLOW.md")
for token in ["Q-0015", "Q-0016", "Q-0017", "one-quarter theorem", "genealogy"]:
    if token in agent_text:
        ERRORS.append(f"generic agent.md contains project-specific token: {token}")

workflow_lines = len(require("WORKFLOW.md").read_text(encoding="utf-8").splitlines())
if workflow_lines > 500:
    ERRORS.append(f"WORKFLOW.md is too long: {workflow_lines} lines (maximum 500)")

for pointer, canonical in [
    ("FACTS.md", "knowledge/FACTS.md"),
    ("FAILURES.md", "knowledge/FAILURES.md"),
    ("QUESTIONS.md", "knowledge/QUESTIONS.md"),
]:
    text = require(pointer).read_text(encoding="utf-8")
    if canonical not in text or len(text.splitlines()) > 8:
        ERRORS.append(f"{pointer} is not a short compatibility pointer")

for pointer in ["PIVOT_SWITCH_ESCAPE_FRAMEWORK.md", "SINGLE_DEFECT_FRAMEWORK.md"]:
    if len(require(pointer).read_text(encoding="utf-8").splitlines()) > 10:
        ERRORS.append(f"{pointer} is not a short compatibility pointer")

# Canonical Markdown must not contain hidden control characters introduced by
# incorrectly escaped generator strings.
canonical_paths = [
    ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "agent.md", ROOT / "WORKFLOW.md",
    ROOT / "HANDOFF_CURRENT.md",
    *sorted((ROOT / "knowledge").glob("*.md")),
    *sorted((ROOT / "docs").rglob("*.md")),
    *sorted((ROOT / "evidence").rglob("*.md")),
]
for path in canonical_paths:
    text = path.read_text(encoding="utf-8")
    bad = [(index, ord(char)) for index, char in enumerate(text)
           if ord(char) < 32 and char not in "\n"]
    if bad:
        ERRORS.append(
            f"control character in {path.relative_to(ROOT)}: "
            + ", ".join(f"offset {index}=0x{code:02x}" for index, code in bad[:5])
        )

readme_text = require("README.md").read_text(encoding="utf-8")
for expected in [r"\frac14", r"\right", r"\text{", r"\to"]:
    if expected not in readme_text:
        ERRORS.append(f"README.md missing intact LaTeX token: {expected}")

ci_text = require(".github/workflows/enumerate-smoke.yml").read_text(encoding="utf-8")
for expected in ['actions/checkout@v7', 'actions/setup-python@v7', 'pip install -e ".[test]"']:
    if expected not in ci_text:
        ERRORS.append(f"CI workflow missing: {expected}")

pyproject_text = require("pyproject.toml").read_text(encoding="utf-8")
for expected in ["[build-system]", "[project]", "[project.optional-dependencies]", "[tool.setuptools.packages.find]"]:
    if expected not in pyproject_text:
        ERRORS.append(f"pyproject.toml missing section: {expected}")

state_text = require("docs/PROJECT_STATE.yaml").read_text(encoding="utf-8")
for expected in [
    "commit: cfadd24b52546d4d5800c4a3c5a75a2add86f928",
    "commit: 2f930000fdc1cc7838475be2cb69b3ebf0f1b5c7",
    "status: open",
    "primary: route_b_critical_stability",
    "route_a_status: suspended",
    "id: S1",
    "question: Q-0018",
    "question: Q-0017",
    "question: Q-0016",
]:
    if expected not in state_text:
        ERRORS.append(f"PROJECT_STATE.yaml missing: {expected}")

handoff = require("HANDOFF_CURRENT.md").read_text(encoding="utf-8")
if "S1 / Q-0018" not in handoff:
    ERRORS.append("handoff does not name the Route-B active node")
if "Route A status:" not in handoff or "suspended" not in handoff:
    ERRORS.append("handoff does not explicitly suspend Route A")
if re.search(r"Q-0016.{0,50}(closed|已证明|已关闭)", handoff, re.I):
    ERRORS.append("handoff overclaims Q-0016")
if re.search(r"Q-0017.{0,50}(closed|已证明|已关闭)", handoff, re.I):
    ERRORS.append("handoff overclaims Q-0017")
if re.search(r"^## .*update", handoff, re.I | re.M):
    ERRORS.append("handoff contains append-only update sections")

registries = "\n".join(require(path).read_text(encoding="utf-8") for path in [
    "knowledge/FACTS.md", "knowledge/FAILURES.md", "knowledge/QUESTIONS.md"
])
for token in [
    "F-0035", "F-0036", "F-0043", "F-0048", "F-0053",
    "A-0025", "A-0026", "A-0029", "A-0033",
    "Q-0015", "Q-0016", "Q-0017", "Q-0018",
]:
    if token not in registries:
        ERRORS.append(f"stable registry ID disappeared: {token}")

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
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if entry.get("sha256") != actual or entry.get("bytes") != path.stat().st_size:
        ERRORS.append(f"raw source manifest mismatch: {path.relative_to(ROOT)}")

baseline = json.loads(
    require("evidence/experiments/q0015/baselines/q0015_audit_results.json")
    .read_text(encoding="utf-8")
)
if baseline.get("metadata", {}).get("schema_version") != "research-artifact-v1":
    ERRORS.append("baseline does not use research-artifact-v1")
if baseline.get("metadata", {}).get("result_type") != "exhaustive-regression":
    ERRORS.append("baseline result type is not exhaustive-regression")

link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
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
