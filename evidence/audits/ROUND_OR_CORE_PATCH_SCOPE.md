# Round-or-Core update scope

```text
Task: Convert the current Round-or-Core discussion into an auditable finite-interface theorem and synchronize the repository's statement of the genuinely remaining gaps.
Mode: status-promotion
Base version: 3f9cb079b0d486ec10a39e9a733949e6236cc742 (uploaded local repository HEAD). The uploaded worktree also reports unrelated filename-encoding changes under old/ and sources/raw/; those paths are forbidden and excluded from this patch.
Target: S1 / Q-0018 supporting progress; a pathwise finite-depth Round-or-Cut theorem, stable-atlas Core extraction, and a corrected closure map.
Inputs: agent.md, AGENTS.md, README.md, HANDOFF_CURRENT.md, docs/PROJECT_STATE.yaml, docs/PROOF_DAG.md, knowledge/DECISIONS.md, knowledge/FACTS.md, knowledge/FAILURES.md, knowledge/QUESTIONS.md, docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md, evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md, and the current mathematical discussion.
Outputs: one proof document; one new supporting fact, decision, and failure record; synchronized framework/question/state/handoff updates; changelog entry; a user-visible patch and updated archive.
Allowed paths: AGENTS.md, README.md, HANDOFF_CURRENT.md, docs/PROJECT_STATE.yaml, docs/PROOF_DAG.md, docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md, evidence/audits/, evidence/proofs/, knowledge/, history/CHANGELOG.md, tools/check_repository.py.
Forbidden paths: sources/raw/, old/, generated experiment baselines/reports, unrelated implementation, Route-A auditors, and historical frameworks.
Expected status change: add one proved-conditional/formal supporting theorem (F-0055); record one active strategy clarification (D-0009) and one failed interpretation (A-0035); refine but do not close Q-0016, Q-0017, or Q-0018. No theorem is closed and Route A is not reactivated.
Acceptance criteria: the finite theorem has explicit hypotheses, a complete max-flow/min-cut proof, a pathwise no-copy realization, and precise nonclaims; canonical files distinguish finite-interface closure from global entrance, overflow conversion, and actual-core endgame; all required repository checks pass; the full diff touches only allowed paths.
Required checks: compileall, pytest, check_repository, check_generated_artifacts, Q-0015 regression auditor, and Q4 splice validation.
Non-goals: prove the one-quarter theorem; claim a global Round-or-Core construction from every target instance; classify every reversible core; convert overflow without proof; treat finite computation as a general theorem; reinterpret algorithmic residual reverse arcs as actual execution transitions.
```

## Candidate change classification

- **ADD:** a proved-conditional finite faithful execution-tree Round-or-Cut theorem with pathwise realization and stable-atlas Core-or-Overflow extraction.
- **ADD:** F-0055 registering the theorem within its explicit finite/exact hypotheses.
- **ADD:** D-0009 adopting pathwise Round-or-Core as the S1 interface while preserving the three separate capacity ledgers and Route-B anti-drift rules.
- **ADD:** A-0035 rejecting the interpretation of max-flow reverse residual arcs as actual blocker-release dynamics.
- **UPDATE:** Q-0007 so the existing stability algebra is recorded as a conditional backend rather than a new independent taxonomy.
- **UPDATE:** Q-0018 so that critical-profile identification and heavy-pair aggregation are subcontracts of the global entrance/Round backend rather than separate final gaps.
- **UPDATE:** Q-0017 to record that finite stable-atlas Core extraction is available conditionally, while global entrance and overflow remain open.
- **UPDATE:** Q-0016 to identify actual-support Core Endgame as the final structural bridge after a strong Round-or-Core.
- **UPDATE:** framework, proof DAG, project state, README, and handoff to list the current three-gap closure map: global faithful entrance/Round compatibility; overflow conversion; actual-support core endgame.
- **CONFIRM:** the F-0038/F-0051/F-0042 stability algebra is an available conditional backend; it is not promoted to an unconditional global theorem.
- **NO_CHANGE:** the status of the one-quarter theorem, Q-0016, Q-0017, Q-0018, and suspended Route A.

## Validation results

All required checks passed on the detached clean worktree at base
`3f9cb079b0d486ec10a39e9a733949e6236cc742`.

```text
python -m compileall -q src enumerate tools tests
  passed

python -m pytest -q
  34 passed

python tools/check_repository.py
  repository consistency checks passed

python tools/check_generated_artifacts.py
  generated artifact checks passed

python enumerate/q0015_configuration_auditor.py \
  --regressions-only \
  --generated-at 2026-07-28T00:00:00Z \
  --output-dir artifacts/runs/q0015
  passed; payload_sha256=ef02bf6446618026052c1a107913e4d015e3c8f3b48a59441a72afa09429a8ad

python enumerate/q4_splice_pay_cylinder_validation.py
  passed; 272 coordinate matchings, 8 normal matchings, 768 policies,
  categories 192/384/192, minimum splice edge count 8
```

No generated baseline or raw/history source file was modified.
