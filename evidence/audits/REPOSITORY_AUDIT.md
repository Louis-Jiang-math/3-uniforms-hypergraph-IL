# Repository restructure audit

## Scope

- **Base commit:** `cfadd24b52546d4d5800c4a3c5a75a2add86f928`
- **Write mode:** implementation
- **Status promotion:** none
- **Purpose:** align the complete project with the generic conversation-driven repository protocol.

## Information architecture

The repository now separates:

- reusable protocol (`agent.md`);
- project-specific instructions (`AGENTS.md`);
- canonical registries (`knowledge/`);
- evidence and experiments (`evidence/`);
- immutable raw sources (`sources/raw/`);
- superseded monoliths (`history/`);
- current operational state (`HANDOFF_CURRENT.md`).

Root `FACTS.md`, `FAILURES.md`, `QUESTIONS.md`, and legacy framework names are compatibility pointers only.

## Implementation changes

- added atomic JSON replacement and payload hashing;
- added explicit artifact metadata: generator, command, parameters, result type, source commit, timestamp, platform, and payload hash;
- moved the CLI implementation into the importable package while retaining a wrapper;
- added deterministic committed-baseline regeneration;
- sorted cut certificates and resource insertion so the regression payload is deterministic across repeated runs;
- added generated-artifact verification and tests;
- updated CI and repository consistency checks for the new architecture.

## Mathematical audit

No mathematical claim status changed:

- the one-quarter theorem remains open;
- G1c/Q-0015 remains active;
- Q-0016 and Q-0017 remain open;
- future-complete lift remains formal supporting infrastructure;
- AMCG remains a specification;
- transition capping remains unsupported as the missing general theorem.

## Historical completeness

Included raw conversations are listed with hashes in `sources/raw/MANIFEST.json`. One very large optional upstream transcript and the byte-for-byte original first-execution JSON were not available through the artifact transport used for this delivery; the manifest records these limitations. Canonical project status does not depend on those missing raw bytes.

## Required acceptance commands

```bash
python -m compileall -q src enumerate tools tests
python -m pytest -q
python tools/check_repository.py
python tools/check_generated_artifacts.py
python enumerate/q0015_configuration_auditor.py --regressions-only --output-dir artifacts/runs/q0015
```
